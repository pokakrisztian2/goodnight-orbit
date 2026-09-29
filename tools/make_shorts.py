"""Cut vertical YouTube Shorts (1080x1920) out of a finished long video.

Rules come from ideas/research-2026-09-29-shorts.md (viral science/sleep Shorts, measured):
  - sound from 0.0 s: a spoken hook ("say") in Otto's voice, then the segment. No silence, no fade-in.
  - normal talking speed: the segment is played 1.25x (the long video is slowed to 0.8x), ~165 words/min
  - end 0.15 s after the last word, so the Short loops back into the hook
  - everything inside the safe zone (YouTube covers the top ~170 px, the bottom ~330 px, the right ~120 px)
  - a slow push-in on the picture, the hook text pops in, a quiet station hum under the voice
  - last 3 s: "Full 1h 41m version for sleep"

Layout (1080x1920):
  top     hook text, y 190-350, max 2 lines
  middle  1080x1080 square of the station (Otto + window), y 360-1440, slowly zooming 100->108%
  lower   word-timed captions, 1-3 words, y ~1260 (over the bottom of the picture)

Which paragraphs: the "shorts" list in videos/<name>.json, e.g.
  {"hook": "I'm not floating. I'm falling.",
   "say": "Everyone thinks I float because there's no gravity up here. That's not true.",
   "from": "The reason I float", "paras": 2}
"from" = the first words of the first paragraph, "paras" = how many paragraphs, "say" = optional
spoken first line (made with the Gemini voice, cached in assets/audio/<name>/shorts/).

Needs (made by render_job.py): assets/audio/<name>/narration.wav, timings.json, captions.ass,
assets/loops/<name>/01.mp4.  Writes renders/shorts/<name>-NN.mp4 + renders/shorts/<name>.txt
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = "Varela Round"
FONT_DIR = os.path.join(ROOT, "tools", "fonts")
OFFSET = 2.0          # the long video starts with 2 s of silence (make_loop_video.py START_SILENCE)
SPEED = 1.25          # segment speed: undoes the long video's 0.8x slowdown
GAP = 0.3             # pause between the spoken hook and the segment
MAX_LEN = 59.0        # Shorts that stay under a minute get the widest reach
SQUARE_X = 380        # left edge of the 1080 square cut from the 1920-wide station (Otto + window)
SQUARE_Y = 360        # where the square sits in the 1920-high Short (360-1440)
ZOOM = 0.08           # slow push-in over the whole Short
PY = sys.executable


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
        sec = lambda p: int(p[0]) * 3600 + int(p[1]) * 60 + float(p[2])
        out.append((sec(parts[1].split(":")), sec(parts[2].split(":")), parts[9]))
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


def say_path(name, text):
    """Where the spoken hook for this text is cached (render_job.py fetches/uploads it)."""
    h = hashlib.sha1(text.encode()).hexdigest()[:10]
    return "assets/audio/%s/shorts/say-%s.wav" % (name, h)


def duration(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                 path], check=True, capture_output=True, text=True).stdout)


def make_say(name, text):
    """Otto's voice saying the hook, at normal speed, silence trimmed at both ends."""
    wav = os.path.join(ROOT, say_path(name, text))
    if not os.path.exists(wav):
        os.makedirs(os.path.dirname(wav), exist_ok=True)
        txt = wav[:-4] + ".txt"
        open(txt, "w").write(text + "\n")
        raw = wav[:-4] + ".raw.wav"
        # its own folder: narrate_gemini writes a timings.json next to the file
        subprocess.run([PY, os.path.join(ROOT, "tools", "narrate_gemini.py"), "--name", name, "--text", txt,
                        "--out", raw, "--tempo", "1.0"], check=True, cwd=ROOT)
        trim = ("silenceremove=start_periods=1:start_threshold=-45dB,areverse,"
                "silenceremove=start_periods=1:start_threshold=-45dB,areverse")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", trim, "-ar", "24000", "-ac", "1", wav],
                       check=True)
        os.remove(raw)
    return wav


def say_captions(wav):
    """Word times for the spoken hook (faster-whisper), grouped 1-3 words."""
    from faster_whisper import WhisperModel
    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    segs, _ = model.transcribe(wav, word_timestamps=True, condition_on_previous_text=False)
    words = [w for s in segs for w in s.words]
    out, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) == 3 or w.word.strip()[-1:] in ".?!,;:":
            out.append((cur[0].start, cur[-1].end, " ".join(x.word.strip() for x in cur).upper()))
            cur = []
    if cur:
        out.append((cur[0].start, cur[-1].end, " ".join(x.word.strip() for x in cur).upper()))
    return out


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
    topic = job.get("topic", name.replace("-", " "))

    audio_dir = os.path.join(ROOT, "assets", "audio", name)
    narration = os.path.join(audio_dir, "narration.wav")
    timings = json.load(open(os.path.join(audio_dir, "timings.json")))
    caps = parse_ass(os.path.join(audio_dir, "captions.ass"))
    paras = [p.strip() for p in open(os.path.join(ROOT, job["script"])).read().split("\n\n") if p.strip()]
    assert len(paras) == len(timings), "script changed since the voice was made"
    loop = os.path.join(ROOT, "assets", "loops", name, "01.mp4")
    long_len = duration(narration) + OFFSET
    lh, lm = divmod(int(round(long_len / 60)), 60)
    long_label = ("%dH %02dM" % (lh, lm)) if lh else ("%d MIN" % lm)

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
            b = min(last[-1][1] + 0.15 * SPEED, nxt - 0.05) if last else nxt
        else:
            b = long_len
        a = max(a - 0.03, 0)
        seg = (b - a) / SPEED            # segment length after speeding up

        # spoken hook first (optional)
        lines = []
        if sh.get("say"):
            wav = make_say(name, sh["say"])
            head = duration(wav) + GAP
            lines += say_captions(wav)
        else:
            wav, head = None, 0.0
        dur = head + seg

        # segment captions on the Short's clock (sped up), 1-3 words each
        for s, e, text in caps:
            if s >= a - 0.05 and s < b:
                for s2, e2, t2 in split_caption(s, min(e, b), text):
                    lines.append((head + (s2 - a) / SPEED, head + (e2 - a) / SPEED, t2))
        flag = "" if dur <= MAX_LEN else "  (LONGER than %.0f s)" % MAX_LEN
        print("short %d: %.1f-%.1f s -> %.1f s%s  %s" % (n, a, b, dur, flag, sh["hook"]), flush=True)

        hook = sh["hook"].upper().replace("{", "(").replace("}", ")")
        pop = r"{\fscx88\fscy88\alpha&HFF&\t(0,350,\fscx100\fscy100\alpha&H00&)}"
        events = ["Dialogue: 0,%s,%s,Hook,,0,0,0,,%s%s" % (ts(0), ts(dur), pop, hook),
                  "Dialogue: 0,%s,%s,Foot,,0,0,0,,{\\fad(300,0)}FULL %s VERSION FOR SLEEP"
                  % (ts(max(dur - 3.0, 0)), ts(dur), long_label)]
        events += ["Dialogue: 1,%s,%s,Cap,,0,0,0,,%s" % (ts(s), ts(e), t) for s, e, t in lines]
        ass = os.path.join(out_dir, "%s-%02d.ass" % (name, n))
        with open(ass, "w", encoding="utf-8") as fh:
            fh.write("""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Hook,{f},72,&H00FFFFFF,&H00FFFFFF,&H00100A06,&H96000000,-1,0,0,0,100,100,2,0,1,5,2,8,60,120,190,1
Style: Cap,{f},100,&H00C4E2F5,&H00C4E2F5,&H00100A06,&H96000000,-1,0,0,0,100,100,3,0,1,7,3,8,90,150,1260,1
Style: Foot,{f},54,&H00C4E2F5,&H00C4E2F5,&H64000000,&H64000000,-1,0,0,0,100,100,2,0,3,14,0,8,60,120,1150,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""".format(f=FONT) + "\n".join(events) + "\n")

        out = os.path.join(out_dir, "%s-%02d.mp4" % (name, n))
        # picture: square, slow push-in, placed on the dark background, text burned in
        vf = ("[0]crop=1080:1080:%d:0,scale=w='trunc(1080*(1+%.3f*t/%.3f)/2)*2':h=-2:eval=frame,"
              "crop=1080:1080,pad=1080:1920:0:%d:color=0x05070d,ass=%s:fontsdir=%s[v]"
              % (SQUARE_X, ZOOM, dur, SQUARE_Y, os.path.relpath(ass, ROOT), os.path.relpath(FONT_DIR, ROOT)))
        inputs = ["-stream_loop", "-1", "-i", os.path.relpath(loop, ROOT), "-i", os.path.relpath(narration, ROOT)]
        segf = ("[1]atrim=start=%.3f:duration=%.3f,asetpts=PTS-STARTPTS,atempo=%.3f,aresample=48000[seg]"
                % (a - OFFSET, b - a, SPEED))
        if wav:
            inputs += ["-i", os.path.relpath(wav, ROOT)]
            voice = ("[2]aresample=48000,apad=pad_dur=%.3f[say];%s;[say][seg]concat=n=2:v=0:a=1[voice]"
                     % (GAP, segf))
        else:
            voice = segf + ";[seg]anull[voice]"
        # quiet station hum ~20 dB under the voice, then loud enough for phones
        hum = "anoisesrc=color=brown:amplitude=0.012:sample_rate=48000,lowpass=f=320[hum]"
        af = (voice + ";" + hum + ";[voice][hum]amix=inputs=2:duration=first:normalize=0,"
              "afade=t=in:d=0.02,afade=t=out:st=%.3f:d=0.12,loudnorm=I=-14:TP=-1.5:LRA=11[a]" % max(dur - 0.12, 0))
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", vf + ";" + af,
                        "-map", "[v]", "-map", "[a]", "-t", "%.3f" % dur,
                        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
                        "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-movflags", "+faststart", out],
                       check=True, cwd=ROOT)
        title = "%s | Otto explains %s 🌙" % (sh["hook"], topic)
        notes.append("%s-%02d.mp4  (%.0f s)\nTitle: %s\nDescription first line: Full slow version for sleep: %s\n"
                     "Hashtags: #science #sleep\nRelated video: the full %s video\n"
                     % (name, n, dur, title, job.get("title", ""), topic))
        print("  -> " + out, flush=True)

    with open(os.path.join(out_dir, name + ".txt"), "w") as fh:
        fh.write("\n".join(notes))


if __name__ == "__main__":
    main()
