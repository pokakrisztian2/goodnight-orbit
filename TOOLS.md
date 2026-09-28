# TOOLS.md — what AI does what, and what it costs

Updated 2026-08-16.

## Short answer: no single AI does the whole thing

Tools that promise "one click → finished video" (Pictory, Fliki, InVideo, Revid) are built for **short, fast, loud** videos. Ours are **long, slow, calm, 15 minutes**. Those tools make our videos worse, and they cost $30–100 a month.

We use one tool per job, and **most of them are free on your Mac.**

---

## Two lanes. Start on the cheap one.

| Step | 🟢 Cheap lane (start here) | 💰 Quality lane (only if needed) |
|---|---|---|
| Idea | Claude + `video-idea` skill — **free** | + NexLev MCP (niche data) |
| Research | NotebookLM — **free** | same |
| Script | Claude + `video-script` skill — **free** | same |
| Images | Higgsfield (you have the skill) | same, or fal.ai FLUX ≈ **$0.12 per video** |
| Voice | **Kokoro, on your Mac — free, unlimited** | ElevenLabs **$22/mo** |
| Edit | **`tools/make_video.py` — free, automatic** | same |
| Thumbnail | Higgsfield + Canva — **free** | same |

**Cheap lane total: $0–5 a month.** (Old plan was $15–50.)

---

## The automation is built. It is in `tools/`.

### One time only

```bash
bash tools/setup.sh
```

Installs the voice model (337 MB) and the little Python it needs. Already done on this Mac.

### Every video — two commands

```bash
# 1. text -> voice  (free, on your Mac, about 4 min for a 15-min script)
tools/.venv/bin/python tools/narrate.py --name my-video --text scripts/my-video.txt

# 2. images + voice -> finished 1080p video (about 6 min)
python3 tools/make_video.py --name my-video
```

That is it. No editor, no timeline, no dragging. **Both tested and working.**

What `make_video.py` does for you automatically:

- slow zoom (Ken Burns) on every image, no jitter
- 1-second soft crossfade between images
- every image gets an equal share of the narration
- voice loudness normalised to broadcast level (-14 LUFS), so the TV volume never jumps
- music automatically ducked 20 dB under the voice, and faded out at the end
- 1920×1080, hardware-encoded on your M2

Folders it expects:

```
assets/images/my-video/   01.png, 02.png, 03.png ...  (sorted = the order)
assets/audio/my-video/narration.wav                   (narrate.py writes this)
assets/audio/my-video/music.mp3                       (optional)
→ renders/my-video.mp4
```

---

## Voice: free first, pay only if you must

**The voice IS the channel.** It is the only human thing the viewer gets. So this is the one place where paying is allowed.

**The rule:** test **Kokoro** (free) on script #1. Listen to 5 full minutes.

- Sounds calm and human → **keep it. $0 forever.**
- Sounds robotic or tiring over 15 minutes → **pay ElevenLabs, $22/mo.** Nothing else.

Kokoro settings we use (already in `narrate.py`):

- voice `am_michael` — calm American man. **Pick one voice and never change it.**
- speed 0.88 → about 145 words a minute, documentary pace
- 0.35s pause between sentences, 0.9s between beats

See all 54 voices:

```bash
tools/.venv/bin/python tools/narrate.py --name x --text x --list-voices
```

Good calm alternatives to try: `am_onyx`, `am_adam`, `bm_george` (British).

---

## NotebookLM — what it is really for

**What it is:** Google's research assistant. You upload your sources. It answers **only from them**, and shows which source each answer came from. Free.

**That is exactly our "every number must be sourced" rule.** Use it at step 2, every video:

1. New notebook per video.
2. Drop in every source: Wikipedia, newspaper scans, historical society pages, National Register listings.
3. Ask: *"List every verified number about this house — rooms, cost, acres, years."* → your **scale paragraph**.
4. Ask: *"What did people claim about the ghost, and who claimed it?"* → your **ambiguity section**.
5. Ask: *"What was happening with wages, money and the local economy in these years?"* → your **history layer**.
6. Copy the answers **with citations** into the script's Sources.

**What it will NOT do:**

- Its **Video Overviews** are slide-explainers. Wrong format for us.
- The cinematic ones need **Google AI Ultra — $200/month.** No.
- It will not write our cold open, blocks or micro-hooks. That is Claude's job.

**Verdict: free NotebookLM, research only.**

---

## NexLev MCP (added 2026-08-16)

YouTube niche and channel research, 60+ tools, straight inside Claude Code. Free with a free NexLev account. Read-only — it cannot touch your channel.

**It is connected but not logged in yet.** To finish:

1. Type `/mcp` in Claude Code.
2. Pick **nexlev** → Authenticate.
3. A browser opens → sign in / make a free NexLev account → done.

Then you can ask me things like *"find channels in the abandoned-mansion niche and show their views per video"*.

---

## Images: Higgsfield

- One style for the whole video. Write the style line once, paste it into every prompt.
- 35–45 images for a 12-minute video.
- Ask for: faded archival photograph, muted colours, soft grain, no faces, no text, 16:9.
- Name them `01.png`, `02.png`… in the order they appear.

Cheaper option if you ever need bulk: fal.ai FLUX schnell, about $0.003 per image → **$0.12 for a whole video**. Needs an account and an API key.

---

## Do NOT buy

- ❌ "Full YouTube automation" tools ($50–100/mo) — wrong format for us, and we already automated the editing for free.
- ❌ Google AI Ultra ($200/mo) for NotebookLM video.
- ❌ Views, subscribers or watch-hour services. They are fake, they do not count toward the 4,000 hours, and they get channels terminated.
