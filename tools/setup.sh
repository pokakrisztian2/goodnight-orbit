#!/bin/bash
# One-time setup for the free local voice (Kokoro).
# Run once:  bash tools/setup.sh
set -e

cd "$(dirname "$0")/.."
TOOLS=tools

echo "== 1. espeak-ng (needed to turn text into sounds)"
if [ ! -f /opt/homebrew/lib/libespeak-ng.dylib ]; then
  brew install espeak-ng
else
  echo "   already installed"
fi

echo "== 2. python environment"
if [ ! -d "$TOOLS/.venv" ]; then
  uv venv --python 3.12 "$TOOLS/.venv"
fi
uv pip install --quiet --python "$TOOLS/.venv/bin/python" kokoro-onnx soundfile
echo "   ok"

echo "== 3. voice model (337 MB, one time)"
mkdir -p "$TOOLS/models"
BASE=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
[ -f "$TOOLS/models/kokoro-v1.0.onnx" ] || curl -L --progress-bar -o "$TOOLS/models/kokoro-v1.0.onnx" "$BASE/kokoro-v1.0.onnx"
[ -f "$TOOLS/models/voices-v1.0.bin" ]  || curl -L --progress-bar -o "$TOOLS/models/voices-v1.0.bin"  "$BASE/voices-v1.0.bin"
echo "   ok"

echo
echo "Done. Now you can run:"
echo "  tools/.venv/bin/python tools/narrate.py --name my-video --text scripts/my-video.txt"
echo "  python3 tools/make_video.py --name my-video"
