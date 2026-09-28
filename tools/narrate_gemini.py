#!/usr/bin/env python3
"""Turn the narration text into narration.wav with Google Gemini TTS (the Otto voice).

    GEMINI_API_KEY=... python3 tools/narrate_gemini.py --name relativity --text scripts/relativity.txt

Writes assets/audio/<name>/narration.wav and prints the real cost (from Google's token count).
Paragraphs are sent in chunks of ~1,200 characters. Same voice + same style prompt every chunk.
Plain text only: one paragraph per beat, blank line between beats.
"""

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

import numpy as np
import soundfile as sf

MODEL = "gemini-3.8-flash-tts"
VOICE = "Charon"
# Prices from ai.google.dev/gemini-api/docs/pricing (checked 2026-09-28, valid to 2026-12-31)
PRICE_IN = 0.50 / 1e6       # $ per input token
PRICE_OUT = 9.00 / 1e6      # $ per audio output token (25 tokens = 1 second)
SR = 24000
MAX_CHARS = 1200
PAUSE_PARAGRAPH = 0.6       # seconds between beats (Cosmo averages ~0.7 s pauses)

STYLE = ("Read this as a deep, warm, bass-baritone male narrator, American accent. Calm, friendly and curious, "
         "like a smart friend explaining something fascinating late at night. Relaxed conversational pace, "
         "about 130 words per minute: unhurried, not slow. Low, steady pitch with small natural rises on questions. "
         "Short natural pauses between sentences. Close to the microphone, clear and crisp, soft breath, "
         "not whispering, not muffled. Intimate and reassuring. No announcer energy.")


def clean(text):
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", text)]
    return [p.replace("—", ", ").replace("–", ", ") for p in paras if p and not p.startswith("#")]


def chunks(paragraphs):
    """Group whole paragraphs into chunks up to MAX_CHARS (split long ones on sentences)."""
    out, cur = [], ""
    for p in paragraphs:
        pieces = [p] if len(p) <= MAX_CHARS else re.split(r"(?<=[.!?])\s+", p)
        for s in pieces:
            if cur and len(cur) + len(s) + 2 > MAX_CHARS:
                out.append(cur)
                cur = ""
            cur = (cur + "\n\n" + s) if cur else s
    if cur:
        out.append(cur)
    return out


def tts(text, voice, model, key, style):
    url = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent" % model
    body = {
        "contents": [{"parts": [{"text": "%s\n\n%s" % (style, text)}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}},
        },
    }
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json", "x-goog-api-key": key})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                data = json.load(r)
            part = data["candidates"][0]["content"]["parts"][0]["inlineData"]["data"]
            pcm = np.frombuffer(base64.b64decode(part), dtype="<i2").astype(np.float32) / 32768
            u = data.get("usageMetadata", {})
            return pcm, u.get("promptTokenCount", 0), u.get("candidatesTokenCount", 0)
        except (urllib.error.HTTPError, urllib.error.URLError, KeyError, TimeoutError) as e:
            msg = e.read().decode()[:300] if isinstance(e, urllib.error.HTTPError) else str(e)
            wait = 10 * (attempt + 1)
            print("  retry in %ds: %s" % (wait, msg), flush=True)
            time.sleep(wait)
    sys.exit("error: Gemini TTS failed 6 times")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--text", required=True)
    ap.add_argument("--voice", default=VOICE)
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--out", help="default: assets/audio/<name>/narration.wav")
    ap.add_argument("--root", default=os.getcwd())
    args = ap.parse_args()
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("error: set GEMINI_API_KEY")

    parts = chunks(clean(open(args.text).read()))
    out = args.out or os.path.join(os.path.abspath(args.root), "assets", "audio", args.name, "narration.wav")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    words = sum(len(c.split()) for c in parts)
    print("%d chunks, %d words, voice %s, model %s" % (len(parts), words, args.voice, args.model), flush=True)

    tin = tout = 0
    t0 = time.time()
    with sf.SoundFile(out, "w", samplerate=SR, channels=1, subtype="PCM_16") as f:
        for i, c in enumerate(parts, 1):
            pcm, a, b = tts(c, args.voice, args.model, key, STYLE)
            tin, tout = tin + a, tout + b
            f.write(pcm)
            f.write(np.zeros(int(SR * PAUSE_PARAGRAPH), np.float32))
            print("  chunk %d/%d  %.0fs audio" % (i, len(parts), len(pcm) / SR), flush=True)
    secs = sf.info(out).duration
    cost = tin * PRICE_IN + tout * PRICE_OUT
    print("done: %.1f min audio, %d words -> %.0f words/min, in %.0fs" % (secs / 60, words, words / (secs / 60), time.time() - t0))
    print("COST: %d input + %d audio tokens = $%.4f  ->  $%.2f per hour of audio" % (tin, tout, cost, cost / secs * 3600))


if __name__ == "__main__":
    main()
