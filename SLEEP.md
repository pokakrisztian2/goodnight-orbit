# SLEEP.md — strategy, format, brand, ideas

> ## 🔄 CHANGED (2026-09-28): **Goodnight Orbit — see `ORBIT.md`.**
>
> Name, character (Otto the astronaut, not Lumen), viewer (curious adults, not 55+), topics
> (hard science and tech) and length (~2h) now live in `ORBIT.md`.
> **Still valid here:** §1 "not mass-produced" checklist, §3 script basics, §7 rules, §8 numbers.

Decided 2026-09-27. This is **the** plan for the channel.
It replaces the 12–20 minute "background cinema" videos and the slideshow idea.
Research behind it: `ideas/research-2026-09-27.md`.

---

## 1. Strategy — why this works

- People put on a long, calm video to fall asleep. It plays for 1–2 hours.
- That is **huge watch time** (minutes people watched). We need 4,000 hours.
  A 15-minute video gives ~7 minutes per view. A sleep video gives ~30+.
  → we need about **4x fewer views**.
- The format is cheap: **one calm voice + one slow, looping animated scene**.
- Proof it works (checked 2026-09-27):

| Channel | Subs | Videos | Format |
|---|---|---|---|
| Sleepy Science Channel | 345,000 | 324 | ~2h, "Most Relaxing Facts About X to Fall Asleep To" |
| Science Before Sleep | 65,500 | 472 | ~3h, space science |
| Silence of the Earth | 60,900 | **81** | ~2.5h, deep time, dinosaurs, Earth |
| **Sleep HushTV** | **15,400** | **12** | ~4h, just calm talking: "Soothing Truths About X" |

- Sleep HushTV got 15,400 subs from **12 videos**. Simple talking works.

### The big danger: "AI slop"

- Viewers are tired of cheap AI videos. Winning titles now say "No AI".
- YouTube removes money from "mass-produced, repetitive" videos. That means videos that are all the same.
- **Our answer: do NOT hide the AI. Make the AI the star.**
  A robot character with a name and a personality. Same robot every video.
  Then it is a **show**, not slop. People come back for the character.
- Plus: every script is new, researched, and true. Every video gets new scenes.

### How we stay NOT mass-produced (checklist for every video)

Learned from Lights Out Physics (see research file). YouTube's rule hits videos that are
"template-like with little variation" or "easy to copy at scale". So every video must have:

- [ ] **One real question** in the title, and a real answer by the end. Not a list of facts.
- [ ] **A path**: each chapter builds on the last one. It teaches something step by step.
- [ ] **Real research**: 8–15 real sources (universities, museums, NASA, papers) in the description.
- [ ] **Named chapters** with timestamps.
- [ ] **Lumen's own voice**: small reactions, and links to earlier nights ("Remember the Ice Age fire?").
- [ ] **New scenes** made for this video. Never reuse loops from another video.
- [ ] **Disclaimer** in the description: education + relaxation, facts from real research, guesses are marked.
- [ ] **Every script checked** before voice: facts true, no copy of another channel's text.

Daily posting is allowed **only** if every video passes this list. If a video fails → do not post it.

---

## 2. Brand

### The character: **Lumen**

- A small, old, gentle robot. A little worn. One soft glowing eye/lamp.
- It is the keeper of a quiet archive at the edge of the world. It has read everything humans ever wrote.
- Every night, it opens the archive and tells you one story. Slowly. Kindly.
- It is curious about humans. It finds small things beautiful: bread, fire, stars, rain.
- It never pretends to be human. It is honest: *"I am a machine. But I have read about the rain for a very long time."*

### Channel name (pick one — handles checked free on 2026-09-27)

| Name | Handle | Why |
|---|---|---|
| **Goodnight, Lumen** ⭐ | @GoodnightLumen | Soft. Easy to remember. Says "sleep" and names the character. |
| Sleep with Lumen | @SleepWithLumen | Clear, but a bit strange in English. |
| The Bedtime Robot | @TheBedtimeRobot | Very clear, less magical. |

### Look

- Dark, warm, calm. Deep blues and amber lamp light. Never bright.
- Lumen is **in every scene**, but small. The world around it changes with the topic:
  by a fire in the Ice Age, at a porthole deep in the ocean, on the Moon looking at Earth.
- Same art style every video. It must look like one show.

### Voice

- `am_michael` (Kokoro, free), sleep speed. Same voice forever. **The voice is Lumen.**

### Rituals (the same words every video — this is the brand)

- **Opening:** *"Hello. It is Lumen. The archive is open, and the night is long. Get comfortable. Tonight, I will tell you about..."*
- **Closing:** *"That is all for tonight. The archive is closing now. Sleep well. I will be here tomorrow."*

---

## 3. Format

| | |
|---|---|
| **Length** | **60–120 minutes.** Default 90. Every video different topic. |
| **Words** | ~108 words per minute → 60 min = 6,500 · 90 min = 9,700 · 120 min = 13,000 |
| **Picture** | 1 looping animated scene per chapter (6–10 per video). Each 8–15 seconds, looped. |
| **Motion** | tiny: fire flickers, stars twinkle, snow falls, Lumen's lamp breathes. Nothing fast. |
| **Sound** | voice, quiet (-20 LUFS = loudness level). Optional soft ambience (rain, fire). No music with words. |
| **End** | closing ritual, then fade to black. |

### Script shape

1. **0:00–1:30** Opening ritual + what tonight's story is.
2. **~1:30** Subscribe ask (they are still awake): *"If you would like me to read to you again, you can subscribe. Then close your eyes."*
3. **Chapters, 8–12 minutes each.** Calm. Complete. No cliffhangers.
4. Lumen's small comments between facts: *"I like this part. The bread is still warm."* That is personality.
5. **Closing ritual.**

### Three lanes (topics rotate)

| Lane | Example | Research needed |
|---|---|---|
| 🏛 **History** — "what life was like" | A Winter in the Ice Age | medium |
| 🔭 **Science** — space, Earth, ocean, deep time | A Slow Journey to the Edge of the Solar System | medium |
| 🌙 **Comfort** — "soothing truths" | Soothing Truths About the Universe | low |

**Rhythm:** 2 videos a week. History, Science, History, Science, then 1 Comfort every 4th slot.

---

## 4. How a video is made (cheap)

| Step | Tool | Cost |
|---|---|---|
| Topic | `video-idea` skill + this list | $0 |
| Research | NotebookLM / web, every fact sourced | $0 |
| Script | Claude, one chapter at a time | $0 |
| Voice | Kokoro on this Mac: `narrate.py --sleep` | $0 |
| Lumen scene pictures | AI image with a Lumen reference picture (Higgsfield or fal.ai) | ~$0.03 each |
| Make scenes move | AI image-to-video, 5–10 s (Higgsfield / fal.ai) | ~$0.25–0.50 each |
| — **or free:** | ffmpeg on this Mac: slow zoom, flicker, stars, snow, grain | $0 |
| Loop + put together | a new tool (to build): loops each scene under its chapter | $0 |

**Cost per video: $0 (free motion) to ~$4 (8 AI-animated scenes). ~$16–30 a month at 2 per week.**

---

## 5. The first 10 videos

| # | Lane | Title | Length |
|---|---|---|---|
| 1 | 🏛 | What Humans Did All Winter in the Ice Age \| Calm History for Sleep | 90 min |
| 2 | 🔭 | A Slow Journey to the Edge of the Solar System \| Science for Sleep | 90 min |
| 3 | 🏛 | A Winter Night in a Medieval Castle \| Calm History for Sleep | 90 min |
| 4 | 🌙 | Soothing Truths About the Universe to Fall Asleep To | 60 min |
| 5 | 🔭 | The Deep Ocean, From Sunlight to the Bottom \| Science for Sleep | 90 min |
| 6 | 🏛 | A Day in Ancient Rome, Dawn to Night \| Calm History for Sleep | 90 min |
| 7 | 🔭 | What Earth Looked Like Before Humans \| Science for Sleep | 120 min |
| 8 | 🌙 | Soothing Truths About Being Tired to Fall Asleep To | 60 min |
| 9 | 🏛 | Life Inside a Lighthouse in 1880 \| Calm History for Sleep | 90 min |
| 10 | 🔭 | The Life of a Star, From Birth to Silence \| Science for Sleep | 90 min |

Why these: deep past, cold + warmth, space and ocean are the topics that win right now (see research file).

---

## 6. Titles and thumbnails

- Title = the topic + "for Sleep". Search words matter: people type "history for sleep", "science for sleep".
- Thumbnail: dark scene, Lumen small with its warm lamp, 3–4 words max. Same layout every time.
- Upload in the US evening (7–9 pm Eastern). Sleep searches happen at night.

## 7. Rules that do not change

- **Every fact real and sourced.** Sources in the description.
- **Every script new.** Never reuse a script. Never the same scenes twice.
- **Tick "altered or synthetic content"** at upload. Lumen is openly AI anyway.
- **No medical claims.** Never "cures insomnia". Say "calm history for sleep".
- **One channel, one real account.**

## 8. Numbers to watch (YouTube Studio)

- **Watch hours** and **subscribers** — the only two that matter until February 2027.
- **Average view duration** (how long one person watched) — want 25+ minutes.
- **Subscribers per video** — the hard one. Sleeping people do not click subscribe. Watch it every week.
