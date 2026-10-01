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
import math
import os
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

W, H, FPS = 1920, 1080, 24   # = Veo, so no frame repeats
VIDEO_EXTS = (".mp4", ".mov", ".m4v", ".webm", ".mkv")


def run(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)


def first_frame(path, dst, at=0.0):
    if path.lower().endswith(VIDEO_EXTS):
        run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "%.2f" % at, "-i", path, "-frames:v", "1", dst])
    else:
        Image.open(path).convert("RGB").save(dst)
    return Image.open(dst).convert("RGB").resize((W, H))


def frames(path):
    """Number of video frames in a clip."""
    out = subprocess.run(["ffprobe", "-v", "error", "-count_packets", "-select_streams", "v:0",
                          "-show_entries", "stream=nb_read_packets", "-of", "csv=p=0", path],
                         check=True, capture_output=True, text=True).stdout
    return int(out.strip())


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
    ap.add_argument("--space-margin", type=float, default=1.02,
                    help="space video: how much bigger than the window (1.0 = just covers it)")
    ap.add_argument("--room-saturation", type=float, default=1.0,
                    help="colour strength of the room only (0.7 = calmer); the sky is not touched")
    ap.add_argument("--space-slow", type=float, default=1.0, help="space video: play this many times slower")
    args = ap.parse_args()

    tmp = tempfile.mkdtemp(prefix="station-")
    frame = first_frame(args.station, os.path.join(tmp, "f0.png"))
    mask, share = window_mask(frame)
    if args.station.lower().endswith(VIDEO_EXTS):
        # things float over the window (the tea mug), so one frame is not enough:
        # a spot counts as window if it is green in any of 8 frames across the clip
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                    "-of", "csv=p=0", args.station],
                                   check=True, capture_output=True, text=True).stdout)
        for k in range(1, 8):
            m, _ = window_mask(first_frame(args.station, os.path.join(tmp, "f%d.png" % k), dur * k / 8))
            mask = Image.fromarray(np.maximum(np.asarray(mask), np.asarray(m)))
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
             "-filter_complex", "[0]scale=%d:%d,fps=%d,setsar=1,eq=saturation=%.2f,split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1"
             % (W, H, FPS, args.room_saturation),
             "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", room])
        room_in = ["-stream_loop", "-1", "-i", room]
        a = np.asarray(ImageEnhance.Color(frame).enhance(args.room_saturation)).astype(int)
        key = np.median(a[np.asarray(mask) > 200], axis=0).astype(int)
        keyhex = "0x%02x%02x%02x" % tuple(key)
        # layer 1: the room with green made see-through on every frame
        # layer 2: the room again, solid everywhere except the window area (so green screens on the wall stay)
        room_f = ("[1]setsar=1,split[r1][r2];"
                  "[r1]format=rgba,colorkey=%s:0.38:0.04,despill=type=green:mix=0.6[keyed];"
                  "[2]loop=loop=-1:size=1,setpts=N/%d/TB,format=gray,negate[out];"
                  "[r2]format=rgba[r2a];[r2a][out]alphamerge[outside];" % (keyhex, FPS))
    else:
        # resize once here, not on every frame
        room = os.path.join(tmp, "room.png")
        Image.open(args.station).convert("RGB").resize((W, H), Image.LANCZOS).save(room)
        room_in = ["-i", room]
        room_f = "[1]loop=loop=-1:size=1,setpts=N/%d/TB,setsar=1,format=rgba[fg0];" % FPS

    space_is_video = args.space.lower().endswith(VIDEO_EXTS)
    if space_is_video:
        # play at its own speed (Veo skies are calm already; slowing made it jerky), forward + backward: the Earth never jumps at the loop point
        # fit the clip to the window (a bit bigger), not the whole screen:
        # more Earth in view, and a 4K clip shrunk down stays sharp
        win = np.asarray(window_mask(frame)[0]) > 128
        ys, xs = np.nonzero(win)
        bw, bh = (xs.max() - xs.min()) * args.space_margin, (ys.max() - ys.min()) * args.space_margin
        cx, cy = (xs.max() + xs.min()) / 2, (ys.max() + ys.min()) / 2
        vw, vh = [int(v) for v in subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
             "-of", "csv=p=0", args.space], check=True, capture_output=True, text=True).stdout.strip().split(",")[:2]]
        f = max(bw / vw, bh / vh)
        sw, sh_ = int(vw * f) // 2 * 2, int(vh * f) // 2 * 2
        x0, y0 = int(cx - sw / 2), int(cy - sh_ / 2)
        # keep only the part that is on screen, then place it on a black frame
        cl, ct = max(0, -x0), max(0, -y0)
        cw, ch = min(sw - cl, W - max(0, x0)) // 2 * 2, min(sh_ - ct, H - max(0, y0)) // 2 * 2
        print("space clip %dx%d -> %dx%d around the window" % (vw, vh, sw, sh_))
        sp = os.path.join(tmp, "space-pingpong.mp4")
        run(["ffmpeg", "-y", "-loglevel", "error", "-i", args.space, "-an", "-filter_complex",
             ("[0]scale=%d:%d:flags=lanczos,crop=%d:%d:%d:%d,pad=%d:%d:%d:%d:black,setpts=%.2f*PTS,"
              + ("fps=%d," if args.space_slow == 1 else "minterpolate=fps=%d:mi_mode=blend,")   # blend: fast, smooth
              + "setsar=1,split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1")
             % (sw, sh_, cw, ch, cl, ct, W, H, max(0, x0), max(0, y0), args.space_slow, FPS),
             "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", sp])
        space_in = ["-stream_loop", "-1", "-i", sp]
        space_f = "[0]setsar=1[bg]"
    else:
        # drift right for half the loop, back for the other half -> same at start and end
        travel = args.drift * L / 2
        sp = Image.open(args.space).convert("RGB")
        sw = W + int(travel) + 200
        sh_ = max(H, round(sp.height * sw / sp.width))
        sp = sp.resize((sw, sh_), Image.LANCZOS)   # resize once, not on every frame
        space = os.path.join(tmp, "space.png")
        sp.save(space)
        space_in = ["-i", space]
        space_f = ("[0]loop=loop=-1:size=1,setpts=N/%d/TB,setsar=1,crop=%d:%d:'(iw-%d)/2-%.1f+%.1f*(1-abs(2*t/%.3f-1))':'(ih-%d)/2'[bg]"
                   % (FPS, W, H, W, travel / 2, travel, L, H))

    # every moving layer must finish a whole cycle at the loop point, or it jumps there.
    # so make the loop a multiple of each cycle (smallest one that is at least --seconds)
    cycles = [frames(f) for f, moving in ((room, is_video), (sp, space_is_video)) if moving]
    if cycles:
        step = 1
        for c in cycles:
            step = step * c // math.gcd(step, c)
        n = max(1, math.ceil(L * FPS / step))
        if L * FPS % step:
            print("loop %.0fs -> %.1fs so every clip ends where it started" % (L, n * step / FPS))
        L = n * step / FPS

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    if is_video:
        # window area = mask made bigger, so a small wobble in the Veo clip is fine
        big = mask.filter(ImageFilter.MaxFilter(15))
        big.save(mask_path)
        comp = "[bg][keyed]overlay[b1];[b1][outside]overlay=shortest=0,format=yuv420p"
    else:
        comp = ("[2]loop=loop=-1:size=1,setpts=N/%d/TB,format=gray,negate[a];" % FPS +
                "[fg0][a]alphamerge[fg];[bg][fg]overlay=shortest=0,format=yuv420p")
    run(["ffmpeg", "-y", "-loglevel", "error", *space_in, *room_in,
         "-i", mask_path,
         "-filter_complex",
         space_f + ";" + room_f + comp,
         "-t", "%.2f" % L, "-r", str(FPS), "-an",
         "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-x264-params", "aq-mode=3",
         "-g", str(FPS * 2), args.out])   # high quality: tiny stars and letters smear at crf 24
    print("done -> %s (%.0fs loop)" % (args.out, L))


if __name__ == "__main__":
    main()
