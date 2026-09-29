"""Cut vertical YouTube Shorts (1080x1920) out of a finished long video.

Each Short = a few whole paragraphs of Otto's voice, over the station loop, with:
  top     a hook line (the Short's title idea)
  middle  a 1080x1080 square of the station: Otto + the window
  below   big word-timed captions, 2-3 words at a time, right under the square
  (nothing in the bottom ~500 px: YouTube covers it with the title and buttons;
   link the full video with the Short's "Related video" setting instead)

Which paragraphs: the "shorts" list in videos/<name>.json, e.g.
  {"hook": "AlexNet was trained in a bedroom", "from": "The training took five", "paras": 3}
"from" = the first words of the first paragraph, "paras" = how many paragraphs.

Needs (made by render_job.py): assets/audio/<name>/narration.wav, timings.json, captions.ass,
assets/loops/<name>/01.mp4.  Writes renders/shorts/<name>-NN.mp4 + renders/shorts/<name>.txt
"""
import argparse
import json
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = "Varela Round"
FONT_DIR = os.path.join(ROOT, "tools", "fonts")
OFFSET = 2.0          # the long video starts with 2 s of silence (make_loop_video.py START_SILENCE)
MAX_LEN = 59.0        # Shorts that stay under a minute get the widest reach
SQUARE_X = 380        # left edge of the 1080 square cut from the 1920-wide station (Otto + window)
SQUARE_Y = 300        # where the square sits in the 1920-high Short (ends at 1380)


def ts(t):
    t = max(t, 0)
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    return "%d:%02d:%05.2f" % (h, m, s)


def parse_ass(path):
    out = []
    for line in open(path, encoding="utf-8"):
        if not line.startswith("Dialogue:"):
            continue
        parts = line.rstrip("\n").split(",", 9)
        s = parts[1].split(":")
        e = parts[2].split(":")
        sec = lambda p: int(p[0]) * 3600 + int(p[1]) * 60 + float(p[2])
        out.append((sec(s), sec(e), parts[9]))
    return out


def first_word(text):
    m = re.search(r"[A-Za-z']+", text)
    return m.group(0).upper() if m else ""


def snap(caps, est, word):
    """Caption start nearest to the estimated time, preferring one that begins with the right word."""
    near = [c for c in caps if abs(c[0] - est) < 3.0]
    good = [c for c in near if first_word(c[2]) == word]
    pool = good or near or caps
    return min(pool, key=lambda c: abs(c[0] - est))[0]


def split_caption(s, e, text):
    """Cut a 4-word caption into two short ones, timed by length."""
    words = text.split()
    if len(text) <= 14 or len(words) < 3:
        return [(s, e, text)]
    k = (len(words) + 1) // 2
    first, second = " ".join(words[:k]), " ".join(words[k:])
    mid = s + (e - s) * len(first) / (len(first) + len(second))
    return [(s, mid, first), (mid, e, second)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    args = ap.parse_args()
    name = args.name
    job = json.load(open(os.path.join(ROOT, "videos", name + ".json")))
    shorts = job.get("shorts", [])
    if not shorts:
        print("no shorts in videos/%s.json" % name)
        return

    audio_dir = os.path.join(ROOT, "assets", "audio", name)
    narration = os.path.join(audio_dir, "narration.wav")
    timings = json.load(open(os.path.join(audio_dir, "timings.json")))
    caps = parse_ass(os.path.join(audio_dir, "captions.ass"))
    paras = [p.strip() for p in open(os.path.join(ROOT, job["script"])).read().split("\n\n") if p.strip()]
    assert len(paras) == len(timings), "script changed since the voice was made"
    loop = os.path.join(ROOT, "assets", "loops", name, "01.mp4")
    audio_len = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                      "-of", "csv=p=0", narration], check=True,
                                     capture_output=True, text=True).stdout) + OFFSET

    out_dir = os.path.join(ROOT, "renders", "shorts")
    os.makedirs(out_dir, exist_ok=True)
    notes = []
    for n, sh in enumerate(shorts, 1):
        i = next(k for k, p in enumerate(paras) if p.startswith(sh["from"]))
        j = i + sh.get("paras", 1)
        a = snap(caps, timings[i]["t"] + OFFSET, first_word(paras[i]))
        if j < len(paras):
            nxt = snap(caps, timings[j]["t"] + OFFSET, first_word(paras[j]))
            last = [c for c in caps if a <= c[0] < nxt - 0.05]
            b = min(last[-1][1] + 0.6, nxt - 0.1) if last else nxt
        else:
            b = audio_len
        a = max(a - 0.25, 0)
        dur = b - a
        flag = "" if dur <= MAX_LEN else "  (LONGER than %.0f s)" % MAX_LEN
        print("short %d: %.1f-%.1f s = %.1f s%s  %s" % (n, a, b, dur, flag, sh["hook"]), flush=True)

        # captions for this piece, moved to the Short's own clock
        # short lines (2-3 words) so the text can be big and still fit beside YouTube's buttons
        lines = []
        for s, e, text in caps:
            if s >= a - 0.05 and s < b:
                for s2, e2, t2 in split_caption(s, min(e, b), text):
                    lines.append("Dialogue: 1,%s,%s,Cap,,0,0,0,,%s" % (ts(s2 - a), ts(e2 - a), t2))
        hook = sh["hook"].upper().replace("{", "(").replace("}", ")")
        ass = os.path.join(out_dir, "%s-%02d.ass" % (name, n))
        with open(ass, "w", encoding="utf-8") as fh:
            fh.write("""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Hook,{f},68,&H00FFFFFF,&H00FFFFFF,&H00100A06,&H96000000,-1,0,0,0,100,100,2,0,1,5,2,8,80,80,55,1
Style: Cap,{f},104,&H00C4E2F5,&H00C4E2F5,&H00100A06,&H96000000,-1,0,0,0,100,100,3,0,1,7,3,8,110,110,1410,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,{z},{d},Hook,,0,0,0,,{h}
""".format(f=FONT, z=ts(0), d=ts(dur), h=hook) + "\n".join(lines) + "\n")

        out = os.path.join(out_dir, "%s-%02d.mp4" % (name, n))
        vf = ("[0]crop=1080:1080:%d:0,pad=1080:1920:0:%d:color=0x05070d,"
              "ass=%s:fontsdir=%s[v]" % (SQUARE_X, SQUARE_Y, os.path.relpath(ass, ROOT), os.path.relpath(FONT_DIR, ROOT)))
        af = ("[1]atrim=start=%.3f:duration=%.3f,asetpts=PTS-STARTPTS,afade=t=in:d=0.15,"
              "afade=t=out:st=%.3f:d=0.5,loudnorm=I=-14:TP=-1.5:LRA=11[a]" % (a - OFFSET, dur, max(dur - 0.5, 0)))
        # relative paths + cwd: the project folder name has a space, which the ass filter can't take
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-stream_loop", "-1", "-i", os.path.relpath(loop, ROOT),
                        "-i", os.path.relpath(narration, ROOT), "-filter_complex", vf + ";" + af,
                        "-map", "[v]", "-map", "[a]", "-t", "%.3f" % dur,
                        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
                        "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-movflags", "+faststart", out],
                       check=True, cwd=ROOT)
        notes.append("%s-%02d.mp4  (%.0f s)\nTitle: %s 🌙 #shorts\n" % (name, n, dur, sh["hook"]))
        print("  -> " + out, flush=True)

    with open(os.path.join(out_dir, name + ".txt"), "w") as fh:
        fh.write("\n".join(notes))


if __name__ == "__main__":
    main()
