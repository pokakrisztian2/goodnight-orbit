#!/usr/bin/env python3
"""Put space behind the green station window and make one seamless loop clip.

    python3 tools/make_station_loop.py \
        --station assets/scenes/station/station-base-v1.png \
        --space assets/space/iss040e091231.jpg \
        --out assets/loops/relativity/01.mp4

--station   the room: a Veo clip (.mp4) or a still picture (.png). Window = solid green.
--space     what is outside: a photo (drifts slowly) or a video (loops).
--seconds   how long the loop is (default 60). make_loop_video.py repeats it.

The window mask is found by itself: the biggest green area in the first frame.
Video rooms play forward then backward (ping-pong), so the join is invisible.
The space photo drifts right, then back, so it also joins cleanly.
Camera must NOT move in the Veo clip — the mask is made once.
"""

import argparse
import collections
import os
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image, ImageFilter

W, H, FPS = 1920, 1080, 25
VIDEO_EXTS = (".mp4", ".mov", ".m4v", ".webm", ".mkv")


def run(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)


def first_frame(path, dst):
    if path.lower().endswith(VIDEO_EXTS):
        run(["ffmpeg", "-y", "-loglevel", "error", "-i", path, "-frames:v", "1", dst])
    else:
        Image.open(path).convert("RGB").save(dst)
    return Image.open(dst).convert("RGB").resize((W, H))


def window_mask(img):
    """White = window (show space). Biggest connected green area."""
    a = np.asarray(img).astype(int)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    green = (g > 40) & (g > r * 1.8) & (g > b * 1.5)
    seen = np.zeros_like(green)
    best = None
    ys, xs = np.nonzero(green)
    for y0, x0 in zip(ys[::500], xs[::500]):
        if seen[y0, x0]:
            continue
        comp, q = [], collections.deque([(y0, x0)])
        seen[y0, x0] = True
        while q:
            y, x = q.popleft()
            comp.append((y, x))
            for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if 0 <= ny < H and 0 <= nx < W and green[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True
                    q.append((ny, nx))
        if best is None or len(comp) > len(best):
            best = comp
    if not best or len(best) < W * H * 0.02:
        sys.exit("error: no green window found in the station picture")
    m = np.zeros((H, W), dtype=np.uint8)
    yy, xx = zip(*best)
    m[list(yy), list(xx)] = 255
    mask = Image.fromarray(m).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(1.5))
    return mask, len(best) / (W * H)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--station", required=True)
    ap.add_argument("--space", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--seconds", type=float, default=60)
    ap.add_argument("--drift", type=float, default=6, help="space photo drift, pixels per second")
    args = ap.parse_args()

    tmp = tempfile.mkdtemp(prefix="station-")
    frame = first_frame(args.station, os.path.join(tmp, "f0.png"))
    mask, share = window_mask(frame)
    mask_path = os.path.join(tmp, "mask.png")
    mask.save(mask_path)
    print("window = %.0f%% of the picture" % (share * 100))

    L = args.seconds
    is_video = args.station.lower().endswith(VIDEO_EXTS)
    room = args.station
    if is_video:
        # forward + backward = seamless, then repeat to fill the loop
        room = os.path.join(tmp, "pingpong.mp4")
        run(["ffmpeg", "-y", "-loglevel", "error", "-i", args.station, "-an",
             "-filter_complex", "[0]scale=%d:%d,fps=%d,setsar=1,split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1" % (W, H, FPS),
             "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", room])
        room_in = ["-stream_loop", "-1", "-i", room]
    else:
        room_in = ["-loop", "1", "-framerate", str(FPS), "-i", room]

    space_is_video = args.space.lower().endswith(VIDEO_EXTS)
    if space_is_video:
        space_in = ["-stream_loop", "-1", "-i", args.space]
        space_f = "[0]scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d,fps=%d,setsar=1[bg]" % (W, H, W, H, FPS)
    else:
        # drift right for half the loop, back for the other half -> same at start and end
        travel = args.drift * L / 2
        space_in = ["-loop", "1", "-framerate", str(FPS), "-i", args.space]
        space_f = ("[0]scale=%d:-2,setsar=1,crop=%d:%d:'(iw-%d)/2-%.1f+%.1f*(1-abs(2*t/%.3f-1))':'(ih-%d)/2'[bg]"
                   % (W + int(travel) + 200, W, H, W, travel / 2, travel, L, H))

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    run(["ffmpeg", "-y", "-loglevel", "error", *space_in, *room_in,
         "-loop", "1", "-i", mask_path,
         "-filter_complex",
         space_f + ";"
         "[1]scale=%d:%d,fps=%d,setsar=1,format=rgba[fg0];"
         "[2]scale=%d:%d,format=gray,negate[a];"
         "[fg0][a]alphamerge[fg];[bg][fg]overlay=shortest=0,format=yuv420p" % (W, H, FPS, W, H),
         "-t", "%.2f" % L, "-r", str(FPS), "-an",
         "-c:v", "libx264", "-crf", "24", "-preset", "veryfast", "-g", str(FPS * 2), args.out])
    print("done -> %s (%.0fs loop)" % (args.out, L))


if __name__ == "__main__":
    main()
