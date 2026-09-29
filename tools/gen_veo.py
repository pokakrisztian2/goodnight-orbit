"""Make one 8-second Veo clip in the cloud and put it in R2.

  python tools/gen_veo.py --prompt assets/scenes/quantum-physics/sky-veo.txt \
      --out assets/space/earth-aurora-veo-v1.mp4 [--image assets/scenes/quantum-physics/room-v1.png]

--image = start picture (image-to-video), fetched from R2 if it is not in the repo.
Needs GEMINI_API_KEY (GitHub secret). Veo 3.1 Lite 1080p = $0.08/s -> $0.64 per clip.
"""
import argparse, base64, json, os, sys, time, urllib.error, urllib.request

sys.path.insert(0, os.path.dirname(__file__))
from render_job import ROOT, fetch, upload

API = "https://generativelanguage.googleapis.com/v1beta/"


def call(path, body=None):
    req = urllib.request.Request(API + path, data=json.dumps(body).encode() if body else None,
                                 headers={"x-goog-api-key": os.environ["GEMINI_API_KEY"],
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        sys.exit("error %s: %s" % (e.code, e.read().decode()[:1000]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True, help="text file with the prompt")
    ap.add_argument("--out", required=True)
    ap.add_argument("--image")
    ap.add_argument("--model", default="veo-3.1-lite-generate-preview")
    ap.add_argument("--resolution", default="1080p")
    a = ap.parse_args()

    inst = {"prompt": open(os.path.join(ROOT, a.prompt)).read().strip()}
    if a.image:
        if not fetch(a.image):
            sys.exit("error: missing %s" % a.image)
        mime = "image/png" if a.image.lower().endswith(".png") else "image/jpeg"
        inst["image"] = {"inlineData": {"mimeType": mime, "data":
                         base64.b64encode(open(os.path.join(ROOT, a.image), "rb").read()).decode()}}
    body = {"instances": [inst], "parameters": {"aspectRatio": "16:9", "resolution": a.resolution,
                                                "durationSeconds": 8}}
    if a.image:
        body["parameters"]["personGeneration"] = "allow_adult"   # the only value image-to-video accepts
    op = call("models/%s:predictLongRunning" % a.model, body)
    print("started", op.get("name"), flush=True)
    while not op.get("done"):
        time.sleep(15)
        op = call(op["name"])
    if "error" in op:
        sys.exit("error: %s" % op["error"])
    samples = op["response"]["generateVideoResponse"].get("generatedSamples")
    if not samples:
        sys.exit("error: no video (filtered?): %s" % json.dumps(op["response"])[:500])
    req = urllib.request.Request(samples[0]["video"]["uri"],
                                 headers={"x-goog-api-key": os.environ["GEMINI_API_KEY"]})
    full = os.path.join(ROOT, a.out)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with urllib.request.urlopen(req, timeout=300) as r, open(full, "wb") as f:
        f.write(r.read())
    print("saved", a.out, os.path.getsize(full), "bytes")
    upload(a.out)


if __name__ == "__main__":
    main()
