#!/usr/bin/env python3
"""Turn the narration text into narration.wav, free, on this Mac (Kokoro).

    tools/.venv/bin/python tools/narrate.py --name millionaires-row \
        --text scripts/millionaires-row.txt

Writes assets/audio/<name>/narration.wav.

Give it PLAIN narration text only — no markdown, no headings, no table rows,
no "Block 2" labels. One paragraph per beat. Blank line between beats.
"""

import argparse
import os
import re
import sys
import time

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro, EspeakConfig

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, "models", "kokoro-v1.0.onnx")
VOICES = os.path.join(HERE, "models", "voices-v1.0.bin")
ESPEAK_LIB = "/opt/homebrew/lib/libespeak-ng.dylib"
ESPEAK_DATA = "/opt/homebrew/share/espeak-ng-data"

# The channel voice. Pick once, never change it — the voice IS the channel.
VOICE = "am_michael"
SPEED = 0.88          # slow, documentary pace (~145 words/min)
PAUSE_SENTENCE = 0.35  # seconds of silence between sentences
PAUSE_PARAGRAPH = 0.9  # seconds of silence between beats
MAX_CHARS = 380        # chunk size fed to the model

# Sleep videos: slower voice, longer silences. Same voice, never change it.
SLEEP_SPEED = 0.80
SLEEP_PAUSE_SENTENCE = 0.7
SLEEP_PAUSE_PARAGRAPH = 1.8


def clean(text):
    """Strip anything that is not meant to be spoken."""
    out = []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            out.append("")
            continue
        if s.startswith("#") or s.startswith("|") or s.startswith("---"):
            continue
        if s.startswith(("- ", "* ", "> ")):
            s = s[2:]
        s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
        s = re.sub(r"\*(.+?)\*", r"\1", s)
        s = re.sub(r"\[(.+?)\]\(.*?\)", r"\1", s)
        s = s.replace("—", ", ").replace("–", ", ")
        out.append(s)
    text = "\n".join(out)
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def chunk(paragraph):
    """Split a paragraph into pieces the model can handle, on sentence ends."""
    sentences = re.split(r"(?<=[.!?])\s+", paragraph)
    chunks, cur = [], ""
    for s in sentences:
        if len(cur) + len(s) + 1 <= MAX_CHARS:
            cur = (cur + " " + s).strip()
        else:
            if cur:
                chunks.append(cur)
            cur = s.strip()
    if cur:
        chunks.append(cur)
    return chunks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--text", required=True, help="plain text file of the narration")
    ap.add_argument("--voice", default=VOICE)
    ap.add_argument("--speed", type=float, default=None)
    ap.add_argument("--sleep", action="store_true",
                    help="sleep video: slower voice, longer pauses")
    ap.add_argument("--root", default=os.getcwd())
    ap.add_argument("--list-voices", action="store_true")
    args = ap.parse_args()

    for path in (MODEL, VOICES):
        if not os.path.exists(path):
            sys.exit("error: missing %s\nRun: bash tools/setup.sh" % path)

    # Mac: use Homebrew espeak-ng. Linux/cloud: kokoro-onnx's bundled espeak.
    espeak = (EspeakConfig(lib_path=ESPEAK_LIB, data_path=ESPEAK_DATA)
              if os.path.exists(ESPEAK_LIB) else None)
    kokoro = Kokoro(MODEL, VOICES, espeak_config=espeak)

    if args.list_voices:
        print(" ".join(sorted(kokoro.get_voices())))
        return

    with open(args.text) as fh:
        paragraphs = clean(fh.read())
    if not paragraphs:
        sys.exit("error: nothing to say in %s" % args.text)

    out_dir = os.path.join(os.path.abspath(args.root), "assets", "audio", args.name)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "narration.wav")

    speed = args.speed or (SLEEP_SPEED if args.sleep else SPEED)
    pause_s = SLEEP_PAUSE_SENTENCE if args.sleep else PAUSE_SENTENCE
    pause_p = SLEEP_PAUSE_PARAGRAPH if args.sleep else PAUSE_PARAGRAPH

    words = sum(len(p.split()) for p in paragraphs)
    print("%d beats, %d words -> %s" % (len(paragraphs), words, out_path))

    # Write straight to disk as we go. A 2-3 hour narration is too big to
    # hold in memory twice.
    sr, started, total = 24000, time.time(), 0
    with sf.SoundFile(out_path, "w", samplerate=sr, channels=1,
                      subtype="PCM_16") as out:
        for i, para in enumerate(paragraphs, 1):
            for part in chunk(para):
                samples, sr = kokoro.create(part, voice=args.voice,
                                            speed=speed, lang="en-us")
                out.write(samples)
                out.write(np.zeros(int(sr * pause_s), dtype=samples.dtype))
                total += len(samples) + int(sr * pause_s)
            out.write(np.zeros(int(sr * pause_p), dtype=np.float32))
            total += int(sr * pause_p)
            print("  beat %d/%d" % (i, len(paragraphs)), end="\r")
    print()

    mins = total / sr / 60
    print("done: %.1f minutes of narration in %.0fs (voice: %s)"
          % (mins, time.time() - started, args.voice))
    if mins < 10:
        print("WARNING: under 10 minutes. Make the script longer.")


if __name__ == "__main__":
    main()
