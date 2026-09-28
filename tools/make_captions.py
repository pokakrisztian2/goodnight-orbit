#!/usr/bin/env python3
"""Burn Cosmo-style captions (a few words at a time, bottom centre) into a finished video.

    python3 tools/make_captions.py --name relativity

Reads  assets/audio/<name>/narration.wav  and  renders/<name>.mp4
Writes renders/<name>.mp4 (with captions) and assets/audio/<name>/captions.ass

Word times come from faster-whisper (free, runs on CPU). The voice starts OFFSET seconds
into the video (make_loop_video.py START_SILENCE), so captions are shifted by that.
"""

import argparse
import os
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--model", default="base.en")
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
        segments, _ = model.transcribe(narration, word_timestamps=True, vad_filter=False,
                                       condition_on_previous_text=False)
        words = [w for seg in segments for w in seg.words]
        print("%d words timed" % len(words), flush=True)

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
