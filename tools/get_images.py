#!/usr/bin/env python3
"""Find and download FREE pictures you are allowed to use. $0.

    python3 tools/get_images.py --name ice-age --search "woolly mammoth painting" --max 10
    python3 tools/get_images.py --name ice-age --category "Paintings by Charles R. Knight"
    python3 tools/get_images.py --name space --nasa "saturn rings" --max 10

Sources:
    Wikimedia Commons  - millions of museum paintings and photos
    NASA Image Library - all space pictures, public domain (great for science videos)

Only keeps pictures with a free license: public domain, CC0, CC BY, CC BY-SA.
Only keeps wide pictures (landscape), at least 1200 px wide.

Writes:
    assets/images/<name>/_new/<file>   the downloads (you pick, rename to 01.jpg, 02.jpg ...)
    assets/images/<name>/CREDITS.md    who made each picture + license. Paste into the description.
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = {"User-Agent": "QuietHoursChannel/1.0 (youtube research; contact via github)"}
OK_LICENSES = ("public domain", "pd", "cc0", "no restrictions", "cc by")


def get_json(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def strip_html(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def commons(params):
    params.update(format="json", prop="imageinfo", iiprop="url|size|extmetadata",
                  iiurlwidth=1920)  # a standard size: Wikimedia blocks odd sizes
    d = get_json("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params))
    out = []
    for p in d.get("query", {}).get("pages", {}).values():
        ii = p["imageinfo"][0]
        m = ii.get("extmetadata", {})
        lic = m.get("LicenseShortName", {}).get("value", "")
        out.append(dict(
            title=p["title"].replace("File:", ""),
            w=ii["width"], h=ii["height"], license=lic,
            author=strip_html(m.get("Artist", {}).get("value", ""))[:120] or "unknown",
            url=ii.get("thumburl") or ii["url"], page=ii["descriptionurl"]))
    return out


def commons_search(q, n):
    return commons(dict(action="query", generator="search", gsrnamespace=6,
                        gsrsearch=q + " filetype:bitmap", gsrlimit=min(n * 3, 50)))


def commons_category(c, n):
    return commons(dict(action="query", generator="categorymembers", gcmtype="file",
                        gcmtitle="Category:" + c, gcmlimit=min(n * 3, 100)))


def nasa(q, n):
    d = get_json("https://images-api.nasa.gov/search?media_type=image&q=" + urllib.parse.quote(q))
    out = []
    for item in d["collection"]["items"][: n * 3]:
        data = item["data"][0]
        nid = data["nasa_id"]
        try:
            assets = get_json("https://images-api.nasa.gov/asset/" + urllib.parse.quote(nid))
        except Exception:
            continue
        urls = [a["href"] for a in assets["collection"]["items"]]
        pick = next((u for u in urls if "~large" in u), None) or next(
            (u for u in urls if "~orig" in u and u.lower().endswith((".jpg", ".png"))), None)
        if not pick:
            continue
        out.append(dict(title=data.get("title", nid)[:80] + ".jpg", w=0, h=0,
                        license="Public domain (NASA)",
                        author=data.get("center", "NASA"),
                        url=pick.replace("http://", "https://"),
                        page="https://images.nasa.gov/details/" + nid))
    return out


def safe_name(s):
    s = re.sub(r"[^A-Za-z0-9._-]+", "_", s)
    return s[:90]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True, help="video folder name")
    ap.add_argument("--search", help="search Wikimedia Commons")
    ap.add_argument("--category", help="a Wikimedia Commons category")
    ap.add_argument("--nasa", help="search the NASA image library")
    ap.add_argument("--max", type=int, default=10)
    ap.add_argument("--root", default=os.getcwd())
    args = ap.parse_args()

    if args.search:
        found = commons_search(args.search, args.max)
    elif args.category:
        found = commons_category(args.category, args.max)
    elif args.nasa:
        found = nasa(args.nasa, args.max)
    else:
        sys.exit("give --search, --category or --nasa")

    img_dir = os.path.join(os.path.abspath(args.root), "assets", "images", args.name)
    new_dir = os.path.join(img_dir, "_new")
    os.makedirs(new_dir, exist_ok=True)
    credits = os.path.join(img_dir, "CREDITS.md")
    if not os.path.exists(credits):
        with open(credits, "w") as fh:
            fh.write("# Picture credits\n\nPaste this list into the video description.\n\n")

    got = 0
    for f in found:
        lic = f["license"].lower()
        if not any(k in lic for k in OK_LICENSES) or "nc" in lic.split() or "-nc" in lic:
            continue
        if f["w"] and (f["w"] < 1200 or f["w"] < f["h"]):
            continue
        fname = safe_name(f["title"])
        if not fname.lower().endswith((".jpg", ".jpeg", ".png")):
            fname += ".jpg"
        path = os.path.join(new_dir, fname)
        if os.path.exists(path):
            continue
        data = None
        for wait in (2, 10, 30):  # be polite: Wikimedia blocks fast downloaders
            time.sleep(wait)
            try:
                req = urllib.request.Request(f["url"], headers=UA)
                with urllib.request.urlopen(req, timeout=120) as r:
                    data = r.read()
                break
            except urllib.error.HTTPError as e:
                if e.code != 429:
                    break
            except Exception:
                break
        if data is None:
            print("  skip (download failed): %s" % fname)
            continue
        with open(path, "wb") as out:
            out.write(data)
        with open(credits, "a") as fh:
            fh.write("- %s — %s — %s — %s\n" % (f["title"], f["author"], f["license"], f["page"]))
        got += 1
        print("  %-14s %s" % (f["license"][:14], fname))
        if got >= args.max:
            break

    print("done: %d free pictures in %s" % (got, new_dir))
    print("credits: %s" % credits)


if __name__ == "__main__":
    main()
