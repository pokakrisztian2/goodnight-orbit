#!/usr/bin/env python3
"""Put your loop animation(s) + the voice together into one long video. Free, fast.

    python3 tools/make_loop_video.py --name ice-age

Expects:
    assets/loops/<name>/      your loop clips, sorted = the order (01.mp4, 02.mp4, ...)
                              1 clip  -> it loops for the whole video
                              many    -> each one gets an equal share of the video
                              (or give --times "0,11:30,24:00" = when each clip starts)
    assets/audio/<name>/narration.wav     the voice (narrate.py --sleep writes it)
    assets/audio/<name>/ambience.mp3      optional: rain, fire... loops quietly under the voice

Writes:
    renders/<name>.mp4   1080p. Sound at sleep loudness. Fades to black at the end.

Fast because each loop is encoded ONCE, then copied over and over (no re-encoding
of the full 1-2 hours). A 90 minute video takes a few minutes.
"""

import argparse
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile

FPS = 24          # Veo clips are 24 fps: no frame repeats, no judder
W, H = 1920, 1080
LOUDNESS = -20          # LUFS. Sleep level: quieter than normal YouTube (-14)
AMBIENCE_DB = -14.0     # ambience this many dB under the voice
START_SILENCE = 2.0     # seconds of picture before the voice starts
END_TAIL = 20.0         # seconds after the voice ends: picture fades to black
VIDEO_EXTS = (".mp4", ".mov", ".m4v", ".webm", ".mkv")
AUDIO_EXTS = (".wav", ".mp3", ".m4a", ".aac", ".flac")


def run(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)


def duration(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
               "-of", "json", path]).stdout
    return float(json.loads(out)["format"]["duration"])


def find_one(folder, stem):
    if not os.path.isdir(folder):
        return None
    for f in sorted(os.listdir(folder)):
        name, ext = os.path.splitext(f)
        if name.lower() == stem and ext.lower() in AUDIO_EXTS:
            return os.path.join(folder, f)
    return None


def parse_time(t):
    parts = [float(p) for p in t.strip().split(":")]
    secs = 0.0
    for p in parts:
        secs = secs * 60 + p
    return secs


def encoder():
    enc = run(["ffmpeg", "-hide_banner", "-encoders"]).stdout
    return "h264_videotoolbox" if "h264_videotoolbox" in enc else "libx264"


def already_ok(src):
    """True if the clip is already h264 1920x1080 at our fps (make_station_loop output)."""
    out = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
               "stream=codec_name,width,height,r_frame_rate,pix_fmt", "-of", "json", src]).stdout
    st = json.loads(out)["streams"][0]
    return (st["codec_name"], st["width"], st["height"], st["r_frame_rate"], st["pix_fmt"]) == \
        ("h264", W, H, "%d/1" % FPS, "yuv420p")


def normalise(src, dst, enc, fade_out_at=None):
    """Re-encode one loop to the same size/fps/codec so copies join cleanly."""
    if fade_out_at is None and already_ok(src):
        run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-an", "-c", "copy", dst])
        return
    vf = ("scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d,fps=%d,"
          "setsar=1,format=yuv420p" % (W, H, W, H, FPS))
    if fade_out_at is not None:
        vf += ",fade=t=out:st=%.2f:d=%.2f" % fade_out_at
    # Mac hardware encoder needs a bitrate. libx264 (cloud) uses quality mode:
    # the picture barely moves, so this keeps a 2-hour file small.
    rate = ["-b:v", "8M"] if enc == "h264_videotoolbox" else ["-crf", "24", "-preset", "veryfast"]
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-an", "-vf", vf,
         "-c:v", enc, *rate, "-g", str(FPS * 2), "-pix_fmt", "yuv420p", dst])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--times", help='start time of each loop, e.g. "0,11:30,24:00"')
    ap.add_argument("--root", default=os.getcwd())
    args = ap.parse_args()

    for b in ("ffmpeg", "ffprobe"):
        if shutil.which(b) is None:
            sys.exit("error: %s not found. Install: brew install ffmpeg" % b)

    root = os.path.abspath(args.root)
    loop_dir = os.path.join(root, "assets", "loops", args.name)
    aud_dir = os.path.join(root, "assets", "audio", args.name)
    out_dir = os.path.join(root, "renders")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, args.name + ".mp4")

    loops = [os.path.join(loop_dir, f) for f in sorted(os.listdir(loop_dir))
             if f.lower().endswith(VIDEO_EXTS) and not f.startswith(".")] \
        if os.path.isdir(loop_dir) else []
    if not loops:
        sys.exit("error: no loop clips in %s" % loop_dir)
    narration = find_one(aud_dir, "narration")
    if not narration:
        sys.exit("error: no narration.wav in %s" % aud_dir)
    ambience = find_one(aud_dir, "ambience")

    voice = duration(narration)
    total = START_SILENCE + voice + END_TAIL

    # When does each loop start and end?
    if args.times:
        starts = [parse_time(t) for t in args.times.split(",")]
        if len(starts) != len(loops):
            sys.exit("error: %d loops but %d times" % (len(loops), len(starts)))
    else:
        starts = [total * i / len(loops) for i in range(len(loops))]
    ends = starts[1:] + [total]

    enc = encoder()
    print("%d loop(s), voice %.1f min -> video %.1f min" % (len(loops), voice / 60, total / 60))

    tmp = tempfile.mkdtemp(prefix="loopvid-")
    try:
        listfile = os.path.join(tmp, "list.txt")
        with open(listfile, "w") as lf:
            for i, (src, a, b) in enumerate(zip(loops, starts, ends)):
                clip = os.path.join(tmp, "n%02d.mp4" % i)
                normalise(src, clip, enc)
                clen = duration(clip)
                need = b - a
                reps = max(1, int(math.ceil(need / clen)))
                last = i == len(loops) - 1
                # The very last copy of the last loop fades to black.
                for r in range(reps - 1 if last else reps):
                    lf.write("file '%s'\n" % clip)
                if last:
                    tail = os.path.join(tmp, "tail.mp4")
                    fade_len = min(END_TAIL, clen)
                    normalise(src, tail, enc, fade_out_at=(max(0.0, clen - fade_len), fade_len))
                    lf.write("file '%s'\n" % tail)
                print("  loop %d/%d: %.0fs clip x %d" % (i + 1, len(loops), clen, reps))

        video = os.path.join(tmp, "video.mp4")
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
             "-i", listfile, "-c", "copy", video])

        # Sound: voice starts after a short silence, sleep loudness, ambience under it.
        delay = int(START_SILENCE * 1000)
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-i", narration]
        voice_chain = "[1:a]loudnorm=I=%d:TP=-2:LRA=7,adelay=%d:all=1,apad[v]" % (LOUDNESS, delay)
        if ambience:
            cmd += ["-stream_loop", "-1", "-i", ambience]
            fc = (voice_chain + ";"
                  "[2:a]loudnorm=I=%d:TP=-2,volume=%.1fdB,afade=t=in:d=3,"
                  "afade=t=out:st=%.2f:d=%.1f[m];"
                  "[v][m]amix=inputs=2:duration=first:normalize=0[a]"
                  % (LOUDNESS, AMBIENCE_DB, total - END_TAIL, END_TAIL))
        else:
            fc = voice_chain.replace("[v]", "[a]")
        cmd += ["-filter_complex", fc, "-map", "0:v", "-map", "[a]",
                "-t", "%.2f" % total, "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
                "-movflags", "+faststart", out_path]
        run(cmd)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("done -> %s  (%.1f minutes)" % (out_path, duration(out_path) / 60))


if __name__ == "__main__":
    main()
