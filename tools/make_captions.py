#!/usr/bin/env python3
"""Burn Cosmo-style captions (a few words at a time, bottom centre) into a finished video.

    python3 tools/make_captions.py --name relativity

Reads  assets/audio/<name>/narration.wav  and  renders/<name>.mp4
Writes renders/<name>.mp4 (with captions) and assets/audio/<name>/captions.ass

Word times come from faster-whisper (free, runs on CPU). The voice starts OFFSET seconds
into the video (make_loop_video.py START_SILENCE), so captions are shifted by that.

Whisper sometimes skips a phrase or mishears a name, so the words shown come from the script
(scripts/<name>.txt): whisper only gives the timing. Script words whisper missed get times
between their neighbours, and a caption that starts after a pause is snapped to the moment
the voice really starts (found in the sound itself).
"""

import argparse
import difflib
import os
import re
import shutil
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(ROOT, "tools", "fonts")
FONT = "Varela Round"
OFFSET = 2.0          # = START_SILENCE in make_loop_video.py
MAX_WORDS = 4         # words on screen at once
MAX_GAP = 0.6         # a pause longer than this starts a new caption


def ts(t):
    h, r = divmod(max(t, 0), 3600)
    m, s = divmod(r, 60)
    return "%d:%02d:%05.2f" % (h, m, s)


class W:
    def __init__(self, word, start, end):
        self.word, self.start, self.end = word, start, end


def key(w):
    return re.sub(r"[^a-z0-9]", "", w.lower())


def align(script_text, heard):
    """Script words, each with a time taken from the whisper words it matches."""
    paras = [p for p in re.split(r"\n\s*\n", script_text) if p.strip() and not p.strip().startswith("#")]
    said = [w for p in paras for w in p.replace("—", ", ").replace("–", ", ").split()]   # as narrate_gemini reads it
    heard = [w for w in heard if key(w.word)]
    sm = difflib.SequenceMatcher(None, [key(w) for w in said], [key(w.word) for w in heard], autojunk=False)
    out = []
    for op, a0, a1, b0, b1 in sm.get_opcodes():
        if op == "equal":
            out += [W(said[a0 + k], heard[b0 + k].start, heard[b0 + k].end) for k in range(a1 - a0)]
        elif op == "replace" and any(c.isdigit() for w in heard[b0:b1] for c in w.word):
            out += [W(w.word.strip(), w.start, w.end) for w in heard[b0:b1]]  # "1935" reads better than "nineteen thirty-five"
        elif op in ("replace", "delete"):
            span = (heard[b0].start, heard[b1 - 1].end) if op == "replace" else None
            out += [W(w, None, None) for w in said[a0:a1]] if span is None else spread(said[a0:a1], *span)
        # "insert" = whisper heard something not in the script (a stutter): drop it
    # words with no time yet: share the gap between the timed words around them
    i = 0
    while i < len(out):
        if out[i].start is not None:
            i += 1
            continue
        j = i
        while j < len(out) and out[j].start is None:
            j += 1
        a = out[i - 1].end if i else 0.0
        b = out[j].start if j < len(out) else a + 0.4 * (j - i)
        out[i:j] = spread([w.word for w in out[i:j]], a, max(b, a + 0.1))
        i = j
    for a, b in zip(out, out[1:]):               # keep times in order
        b.start = max(b.start, a.start)
        b.end = max(b.end, b.start)
    return out


def spread(words, a, b):
    total = sum(len(w) + 1 for w in words)
    res, t = [], a
    for w in words:
        d = (b - a) * (len(w) + 1) / total
        res.append(W(w, t, t + d))
        t += d
    return res


def voice_starts(wav):
    """Moments the voice starts again after a short pause."""
    r = subprocess.run(["ffmpeg", "-v", "info", "-i", wav, "-af", "silencedetect=noise=-40dB:d=0.25",
                        "-f", "null", "-"], capture_output=True, text=True)
    return [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", r.stderr)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--model", default="base.en")
    ap.add_argument("--script", help="default scripts/<name>.txt")
    args = ap.parse_args()
    narration = os.path.join(ROOT, "assets", "audio", args.name, "narration.wav")
    video = os.path.join(ROOT, "renders", args.name + ".mp4")
    ass = os.path.join(ROOT, "assets", "audio", args.name, "captions.ass")

    # same voice as last time -> same word times, so skip the slow listening step
    if os.path.exists(ass) and os.path.getmtime(ass) >= os.path.getmtime(narration):
        print("reusing %s" % ass, flush=True)
    else:
        from faster_whisper import WhisperModel
        model = WhisperModel(args.model, device="cpu", compute_type="int8")
        # decode the voice ourselves (16 kHz mono float): faster-whisper's own decoder breaks
        # whenever a new PyAV comes out
        import numpy as np
        pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", narration, "-ac", "1", "-ar", "16000",
                              "-f", "f32le", "-"], capture_output=True, check=True).stdout
        audio = np.frombuffer(pcm, np.float32)
        segments, _ = model.transcribe(audio, word_timestamps=True, vad_filter=False,
                                       condition_on_previous_text=False)
        words = [W(w.word.strip(), w.start, w.end) for seg in segments for w in seg.words]
        print("%d words timed" % len(words), flush=True)
        script = args.script or os.path.join(ROOT, "scripts", args.name + ".txt")
        if os.path.exists(script):
            words = align(open(script).read(), words)
            print("aligned to the script: %d words" % len(words), flush=True)

        # group into short captions
        groups, cur = [], []
        for w in words:
            if cur and (len(cur) >= MAX_WORDS or w.start - cur[-1].end > MAX_GAP
                        or cur[-1].word.strip()[-1:] in ".?!,;:"):
                groups.append(cur)
                cur = []
            cur.append(w)
        if cur:
            groups.append(cur)

        head = """[Script Info]
    ScriptType: v4.00+
    PlayResX: 1920
    PlayResY: 1080
    WrapStyle: 2

    [V4+ Styles]
    Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
    Style: Cap,%s,80,&H00C4E2F5,&H00C4E2F5,&H00100A06,&H96000000,-1,0,0,0,100,100,3,0,1,5,3,2,80,80,80,1

    [Events]
    Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
    """ % FONT
        onsets = voice_starts(narration)
        import bisect
        for i, g in enumerate(groups):
            lo = groups[i - 1][-1].end + 0.1 if i else 0.0
            k = bisect.bisect_right(onsets, lo)
            if k < len(onsets) and onsets[k] <= g[0].start + 0.05 and g[0].start - onsets[k] <= 2.5:
                g[0].start = onsets[k]
        lines = []
        for i, g in enumerate(groups):
            start = g[0].start + OFFSET
            end = g[-1].end + OFFSET
            if i + 1 < len(groups):
                end = min(max(end, start + 0.4), groups[i + 1][0].start + OFFSET)
            text = " ".join(w.word.strip() for w in g).upper().replace("{", "(").replace("}", ")")
            lines.append("Dialogue: 0,%s,%s,Cap,,0,0,0,,%s" % (ts(start), ts(end), text))
        with open(ass, "w") as fh:
            fh.write(head + "\n".join(lines) + "\n")
        print("%d captions -> %s" % (len(lines), ass), flush=True)

    # burn in: re-encode the picture once, keep the sound as it is
    tmp = video + ".cap.mp4"
    # relative paths: the folder name "Youtube Business" has a space, which the filter can't take
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video,
                    "-vf", "ass=%s:fontsdir=%s" % (os.path.relpath(ass, ROOT), os.path.relpath(FONT_DIR, ROOT)),
                    "-c:v", "libx264", "-preset", "superfast", "-crf", "24", "-g", "50",
                    "-c:a", "copy", "-movflags", "+faststart", tmp], check=True, cwd=ROOT)
    shutil.move(tmp, video)
    print("captions burned -> %s" % video)


if __name__ == "__main__":
    main()
