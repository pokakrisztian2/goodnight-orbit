#!/usr/bin/env python3
"""Build the slideshow video: images + narration (+ music) -> 1080p mp4.

Free. Runs on this Mac with ffmpeg. No accounts, no subscriptions.

    python3 tools/make_video.py --name millionaires-row

Expects:
    assets/images/<name>/   images, named so they sort in order (01.png, 02.png, ...)
    assets/audio/<name>/narration.wav (or .mp3)
    assets/audio/<name>/music.mp3      optional

Writes:
    renders/<name>.mp4

Each image gets an equal share of the narration length, with a slow zoom
(Ken Burns) and a soft crossfade between images.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

FPS = 25
W, H = 1920, 1080
XFADE = 1.0          # seconds of crossfade between images
ZOOM_MAX = 1.12      # how far the slow zoom goes in by the end of each image
MUSIC_DB = -20.0     # music this many dB under the voice
LOUDNESS = -14       # LUFS, normal videos

# Sleep videos: quieter, slower fades, fade to black at the very end.
SLEEP_LOUDNESS = -20
SLEEP_XFADE = 3.0
SLEEP_END_FADE = 30.0
IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".webp")
AUDIO_EXTS = (".wav", ".mp3", ".m4a", ".aac", ".flac")


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def need(binary):
    if shutil.which(binary) is None:
        sys.exit("error: %s not found. Install it with: brew install %s" % (binary, binary))


def duration(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
               "-of", "json", path]).stdout
    return float(json.loads(out)["format"]["duration"])


def find_one(folder, exts, stem=None):
    if not os.path.isdir(folder):
        return None
    for f in sorted(os.listdir(folder)):
        if f.startswith("."):
            continue
        name, ext = os.path.splitext(f)
        if ext.lower() in exts and (stem is None or name.lower() == stem):
            return os.path.join(folder, f)
    return None


def has_videotoolbox():
    try:
        return "h264_videotoolbox" in run(["ffmpeg", "-hide_banner", "-encoders"]).stdout
    except subprocess.CalledProcessError:
        return False


def build_clip(image, seconds, out_path, encoder):
    """One image -> one silent clip with a slow zoom."""
    frames = max(2, int(round(seconds * FPS)))
    # Crop to 16:9 and upscale a little first: zoompan on a raw image jitters,
    # but upscaling to 8K (the usual advice) is far too slow for 45 images.
    # Reach ZOOM_MAX exactly at the end of the clip, whatever its length.
    zoom_in = "min(zoom+%.6f,%.3f)" % ((ZOOM_MAX - 1.0) / frames, ZOOM_MAX)
    vf = (
        "scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d,"
        "scale=%d:%d,"
        "zoompan=z='%s':d=%d:s=%dx%d:fps=%d"
        ":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)',"
        "setsar=1,format=yuv420p"
        % (W, H, W, H, W * 2, H * 2, zoom_in, frames, W, H, FPS)
    )
    run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", image,
         "-vf", vf, "-t", "%.3f" % seconds, "-r", str(FPS),
         "-c:v", encoder, "-b:v", "8M", "-pix_fmt", "yuv420p", out_path])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True, help="video folder name, e.g. millionaires-row")
    ap.add_argument("--root", default=os.getcwd())
    ap.add_argument("--no-xfade", action="store_true", help="hard cuts instead of crossfades")
    ap.add_argument("--sleep", action="store_true",
                    help="sleep video: quieter, slow fades, fade to black at the end")
    args = ap.parse_args()

    need("ffmpeg")
    need("ffprobe")

    root = os.path.abspath(args.root)
    img_dir = os.path.join(root, "assets", "images", args.name)
    aud_dir = os.path.join(root, "assets", "audio", args.name)
    out_dir = os.path.join(root, "renders")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, args.name + ".mp4")

    if not os.path.isdir(img_dir):
        sys.exit("error: no image folder at %s" % img_dir)
    images = [os.path.join(img_dir, f) for f in sorted(os.listdir(img_dir))
              if f.lower().endswith(IMAGE_EXTS) and not f.startswith(".")]
    if not images:
        sys.exit("error: no images in %s" % img_dir)

    narration = find_one(aud_dir, AUDIO_EXTS, stem="narration")
    if narration is None:
        sys.exit("error: no narration file at %s/narration.wav" % aud_dir)
    music = find_one(aud_dir, AUDIO_EXTS, stem="music")

    total = duration(narration)
    n = len(images)
    xfade = 0.0 if (args.no_xfade or n < 2) else (SLEEP_XFADE if args.sleep else XFADE)
    loud = SLEEP_LOUDNESS if args.sleep else LOUDNESS
    end_fade = SLEEP_END_FADE if args.sleep else 3.0
    # With crossfades the clips overlap, so each clip must be a bit longer.
    per = (total + xfade * (n - 1)) / n
    if per <= xfade + 0.5:
        xfade = 0.0
        per = total / n

    print("%d images, narration %.1fs -> %.2fs per image" % (n, total, per))

    encoder = "h264_videotoolbox" if has_videotoolbox() else "libx264"
    print("encoder: %s" % encoder)

    tmp = tempfile.mkdtemp(prefix="ytb-")
    try:
        clips = []
        for i, img in enumerate(images):
            clip = os.path.join(tmp, "c%04d.mp4" % i)
            build_clip(img, per, clip, encoder)
            clips.append(clip)
            print("  image %d/%d" % (i + 1, n), end="\r")
        print()

        # Video: concat, or chain crossfades.
        if xfade == 0.0:
            listfile = os.path.join(tmp, "list.txt")
            with open(listfile, "w") as fh:
                for c in clips:
                    fh.write("file '%s'\n" % c)
            video = os.path.join(tmp, "video.mp4")
            run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                 "-i", listfile, "-c", "copy", video])
        else:
            cmd = ["ffmpeg", "-y", "-loglevel", "error"]
            for c in clips:
                cmd += ["-i", c]
            parts, last, offset = [], "0:v", 0.0
            for i in range(1, n):
                offset += per - xfade
                label = "v%d" % i
                parts.append("[%s][%d:v]xfade=transition=fade:duration=%.3f:offset=%.3f[%s]"
                             % (last, i, xfade, offset, label))
                last = label
            video = os.path.join(tmp, "video.mp4")
            cmd += ["-filter_complex", ";".join(parts), "-map", "[%s]" % last,
                    "-c:v", encoder, "-b:v", "8M", "-pix_fmt", "yuv420p", "-r", str(FPS), video]
            run(cmd)

        # Audio: normalise the voice, duck the music under it.
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-i", narration]
        if music:
            cmd += ["-stream_loop", "-1", "-i", music,
                    "-filter_complex",
                    "[1:a]loudnorm=I=%d:TP=-1.5:LRA=11[v];"
                    "[2:a]volume=%.1fdB,afade=t=out:st=%.2f:d=%.1f[m];"
                    "[v][m]amix=inputs=2:duration=first:dropout_transition=0[a]"
                    % (loud, MUSIC_DB, max(0.0, total - end_fade), end_fade),
                    "-map", "0:v", "-map", "[a]"]
        else:
            cmd += ["-filter_complex", "[1:a]loudnorm=I=%d:TP=-1.5:LRA=11[a]" % loud,
                    "-map", "0:v", "-map", "[a]"]
        if args.sleep:
            # Fade the picture to black over the last seconds. Re-encodes the video.
            cmd += ["-vf", "fade=t=out:st=%.2f:d=%.1f" % (max(0.0, total - end_fade), end_fade),
                    "-c:v", encoder, "-b:v", "6M", "-pix_fmt", "yuv420p"]
        else:
            cmd += ["-c:v", "copy"]
        cmd += ["-c:a", "aac", "-b:a", "192k", "-shortest", out_path]
        run(cmd)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("done -> %s  (%.1f minutes)" % (out_path, duration(out_path) / 60))


if __name__ == "__main__":
    main()
