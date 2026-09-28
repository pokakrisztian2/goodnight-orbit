#!/bin/bash
# Upload pictures / clips to the cloud (Cloudflare R2), same path as here.
#   bash tools/push.sh assets/scenes/relativity/01.mp4 assets/space/*.jpg
# Uses your Cloudflare login on this Mac (npx wrangler login).
set -e
cd "$(dirname "$0")/.."
BUCKET=goodnight-orbit
for f in "$@"; do
  [ -f "$f" ] || { echo "skip (not a file): $f"; continue; }
  npx --yes wrangler r2 object put "$BUCKET/$f" --file "$f" --remote >/dev/null
  echo "up: $f"
done
