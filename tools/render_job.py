#!/usr/bin/env python3
"""Make one whole video from a job file. Runs on this Mac or in the cloud (GitHub Actions).

    python3 tools/render_job.py videos/relativity.json

Job file (videos/<name>.json):
    {
      "name": "relativity",
      "script": "scripts/relativity.txt",
      "loop_seconds": 60,
      "scenes": [
        {"station": "assets/scenes/relativity/01.mp4", "space": "assets/space/iss040e091231.jpg"},
        {"station": "assets/scenes/relativity/02.mp4", "space": "assets/space/iss035e017357.jpg"}
      ]
    }

Steps: get missing pictures/clips from R2 -> voice (skipped if already made) ->
one loop per scene (space behind the window) -> the long video -> upload to R2.

Cloud storage (R2) is used only when R2_BUCKET and R2_ENDPOINT are set.
Pictures and clips live in R2 under the same path as on this Mac (assets/...).
"""

import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUCKET = os.environ.get("R2_BUCKET")
ENDPOINT = os.environ.get("R2_ENDPOINT")
PY = sys.executable


def sh(cmd):
    print("$ " + " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True, cwd=ROOT)


def s3(*args, check=True):
    cmd = ["aws", "s3", *args, "--endpoint-url", ENDPOINT, "--only-show-errors"]
    return subprocess.run(cmd, check=check, cwd=ROOT)


def fetch(path):
    """Download path from R2 if it is not here yet. True if we have it now."""
    full = os.path.join(ROOT, path)
    if os.path.exists(full):
        return True
    if not BUCKET:
        return False
    os.makedirs(os.path.dirname(full), exist_ok=True)
    return s3("cp", "s3://%s/%s" % (BUCKET, path), full, check=False).returncode == 0


def upload(path):
    if BUCKET:
        s3("cp", os.path.join(ROOT, path), "s3://%s/%s" % (BUCKET, path))


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    job = json.load(open(os.path.join(ROOT, sys.argv[1])))
    name = job["name"]

    # 1. pictures and clips
    for sc in job["scenes"]:
        for key in ("station", "space"):
            if not fetch(sc[key]):
                sys.exit("error: missing %s (put it in R2 with tools/push.sh)" % sc[key])

    # 2. voice (slow, so keep it in R2 and reuse it on the next run)
    narration = "assets/audio/%s/narration.wav" % name
    new_voice = not fetch(narration)
    if new_voice:
        if job.get("voice", "gemini") == "kokoro":
            sh([PY, "tools/narrate.py", "--name", name, "--text", job["script"], "--sleep"])
        else:   # Otto's voice: Gemini custom voice "ASMR Orbit 2", 20% slower
            sh([PY, "tools/narrate_gemini.py", "--name", name, "--text", job["script"]])
            upload("assets/audio/%s/timings.json" % name)
        upload(narration)

    # 3. one loop per scene
    loop_dir = os.path.join(ROOT, "assets", "loops", name)
    os.makedirs(loop_dir, exist_ok=True)
    for f in os.listdir(loop_dir):
        os.remove(os.path.join(loop_dir, f))
    for i, sc in enumerate(job["scenes"], 1):
        sh([PY, "tools/make_station_loop.py", "--station", sc["station"], "--space", sc["space"],
            "--seconds", str(job.get("loop_seconds", 60)),
            "--out", "assets/loops/%s/%02d.mp4" % (name, i)])

    # 4. the long video
    sh([PY, "tools/make_loop_video.py", "--name", name])

    # 4b. Cosmo-style captions, a few words at a time (word times from faster-whisper)
    if job.get("captions", True):
        if not new_voice:
            fetch("assets/audio/%s/captions.ass" % name)   # same voice -> reuse its word times
        sh([PY, "tools/make_captions.py", "--name", name])
        upload("assets/audio/%s/captions.ass" % name)

    # 5. upload + a download link (works 7 days)
    render = "renders/%s.mp4" % name
    if BUCKET:
        upload(render)
        url = subprocess.run(["aws", "s3", "presign", "s3://%s/%s" % (BUCKET, render),
                              "--endpoint-url", ENDPOINT, "--expires-in", "604800"],
                             check=True, capture_output=True, text=True).stdout.strip()
        print("\nDOWNLOAD (7 days): " + url)
        summary = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary:
            with open(summary, "a") as fh:
                fh.write("## %s is ready\n\n[Download the video](%s) (link works 7 days)\n" % (name, url))


if __name__ == "__main__":
    main()
