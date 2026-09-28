# CLAUDE.md — Youtube Business

## How to talk to me (IMPORTANT)

The user is Hungarian. English is not their first language.

**Always write in short, simple sentences. Small words. Like talking to a smart kid.**

- One idea per sentence.
- No big words when a small word works.
- Bullet lists, not long paragraphs.
- If a word is technical (RPM, CTR, retention), say what it means in 5 words.
- Always end with: what we do next — step 1, 2, 3.

## What this project is

A faceless YouTube channel. AI makes the pictures and the voice.
For **curious adults (20–50) who can't switch their brain off at night**. Language: **English (US)**.
Goal: **money from YouTube ads**.

**Format (changed 2026-09-28): GOODNIGHT ORBIT.** ~2 hour sleep videos. **Otto**, an astronaut on the
night shift in orbit, explains hard science and tech (physics, AI, electricity) slowly. AI voice + 12 slow
looping scenes per video; the station gets darker as the night goes on. **Read `ORBIT.md` first — it
overrides `SLEEP.md` on name, character, viewer, topics and length.** `SLEEP.md` §1 checklist and §7 rules still apply.

_Older note (2026-09-27, replaced):_

**Format (changed 2026-09-27): SLEEP VIDEOS, 60–120 min.** A robot character, **Lumen**, reads
calm history, science and "soothing truths" to you at night. AI voice + one slow looping animated
scene per chapter (the user makes the loop animations). No slideshow. **Read `SLEEP.md` first — it overrides the older
12–20 minute rules below where they disagree** (length, cold open, micro-hooks, cliffhangers,
chapter length, loudness). The old rules still apply for facts, sources, safety and money.

## Read these before making anything

| File | What |
|---|---|
| `ORBIT.md` | **the current plan. Read first.** (2026-09-28) |
| `SLEEP.md` | sleep format basics: not-mass-produced checklist (§1), safety rules (§7) |
| `START-HERE.md` | the whole project on one page |
| `STRATEGY.md` | **why** it works. The most important file. |
| `MONETIZATION-PLAN.md` | the goal, the deadline, the weekly numbers |
| `TOOLS.md` | which AI does which job |
| `NICHE-TEST.md` | the niche decision (closed — do not re-open) |

## The goal (this governs everything)

**Get into the YouTube Partner Program before 1 February 2027.**

Before that date the bar is 1,000 subs + **4,000** watch hours. After it, **8,000**. Same subs, double the hours.

So until February 2027 only two numbers matter: **watch hours** and **subscribers**. RPM does not exist yet — do not optimise for it. Details and the weekly pace table: `MONETIZATION-PLAN.md`.

## The niche

**Hard science and tech, explained gently for sleep, by Otto the night-shift astronaut** (2026-09-28).
Channel name: **Goodnight Orbit** (@GoodnightOrbit — free on 2026-09-28). First 10 videos: `ORBIT.md` §7.
Research: `ideas/research-2026-09-28-cosmo-explains.md` (Cosmo Explains, the channel we learn from).
Replaced: Lumen the robot (2026-09-27, see `SLEEP.md`) and Grand Manors (2026-08-16, see `NICHE-TEST.md`).

## Skills (use them)

| Skill | When |
|---|---|
| `video-idea` | finding topics, scoring ideas, writing titles |
| `video-script` | writing the script, cold open, chapters, beats |
| `thumbnail` | making or checking a thumbnail |

## The rules, short version

- **Audience:** US, 55+, watching on a TV. Never in a hurry.
- **Length:** 12–20 minutes to start. Never under 10. Long-form (60–100 min) later.
- **Pictures only.** Slow AI slideshow, slow zoom. No fast cuts.
- **Calm voice.** ~145 words per minute. Warm. Slightly sad. Never shouting.
- **The voice carries everything.** It must work with eyes closed. Never "look at this".
- **No hype.** No "SHOCKING!!!", no "Top 10", no "hey guys", no clickbait faces.
- **Anti-design look.** One object, one idea, one emotion. We whisper while everyone shouts.
- **Evergreen.** Never news. It must still work in 3 years.
- **Feeling:** loss and nostalgia. Things that are gone.
- **Mix:** 60% eerie story + 40% real history. Looks spooky, delivers facts.
- **Chapters:** one every 90–120 seconds (6–8 in a 12-min video), each headline implies conflict.
- **Numbers:** a scale paragraph (4–8 verified numbers) every 8–12 minutes.
- **Compounding:** same world every video. Video 20 makes video 21 stronger.

## The workflow (every video)

1. **Idea** → `video-idea` skill → pick from `ideas/ideas-backlog.md`.
2. **Research** → **NotebookLM** (free). One notebook per video. Every name, date and number comes out of it **with its citation**. See `TOOLS.md`.
3. **Script** → `video-script` skill → copy `templates/script-template.md` into `scripts/`.
4. **Images** → one per ~20s of script (35–45 for 12 min). Use `higgsfield-generate`. Save in `assets/images/<video-name>/`. One style per video.
5. **Voice** → free, local, one command. One fixed voice forever (`am_michael`; `--sleep` = speed 0.80 + long pauses).
   `tools/.venv/bin/python tools/narrate.py --name <video> --text scripts/<video>.txt --sleep`
   (Pay for ElevenLabs $22/mo **only** if Kokoro sounds robotic over a full 15 minutes.)
6. **Assemble** → free, automatic. Zoom, crossfades, loudness, music ducking all handled:
   `python3 tools/make_video.py --name <video> --sleep` → `renders/<video>.mp4`
7. **Thumbnail** → `thumbnail` skill → `thumbnails/`.
8. **Upload** → `templates/upload-checklist.md`, line by line.
9. **Archive** → move the script to `published/`, and log watch hours + subs in `MONETIZATION-PLAN.md` every Sunday.

## Rules that keep the money safe

Not optional. Breaking these can kill the channel's income.

- **Tick "altered or synthetic content"** at upload. AI voice + AI images must be disclosed.
- **Every video original and useful.** YouTube demonetizes "inauthentic content" — mass-produced repetitive videos. Real research, our own script, every time.
- **Never state a myth as fact.** Say who claimed it, then give the grounded explanation, then leave it open. Ambiguity is allowed; lying is not.
- **Every number verified and sourced.** Sources go in the script and in the description.
- **One channel, one real account.** No proxies, no multi-accounts, no fake aged accounts.
- **No other people's footage or photos** unless clearly free to use. AI images are ours.
- **No medical or money advice.** We tell stories.

## Folders

```
ideas/       video ideas, scored
scripts/     scripts in progress
assets/      images/ and audio/ per video
thumbnails/  thumbnail pictures
renders/     the finished .mp4 files
published/   finished videos + their numbers
templates/   copy these to start something new
tools/       narrate.py (free voice) + make_video.py (free editor)
.claude/skills/   the three skills
```

**Cost: $0–5 a month.** Voice and video assembly are free and local. Full stack in `TOOLS.md`.

## Numbers we watch

**Until February 2027 — only these two:**

- **Watch hours** — need 4,000. Pace: ~800 per month.
- **Subscribers** — need 1,000. Pace: ~200 per month.

**Per video, to see what is working:**

- **Average view duration** — minutes watched. Want 50%+ of the video. **This is our real weapon.**
- **CTR** (click rate) — of people who saw the thumbnail, how many clicked. Ours will be lower than 4% but **stable** — that is expected and fine.

**Later (after monetization only):**

- **RPM** — money per 1000 views. Want $8+ (US, 55+). Ignore it until we are in the program.

Log the weekly totals in `MONETIZATION-PLAN.md`. Log per-video numbers in `published/<video>.md` after 14 and 30 days.
