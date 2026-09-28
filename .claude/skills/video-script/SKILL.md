---
name: video-script
description: Write faceless YouTube scripts. DEFAULT is the 1-3 hour SLEEP format (calm history/science for sleep, see "Sleep mode" section). The older 10-20 minute cinematic format is below it. Use when the user asks to write a script, a voice-over, a narration, a cold open, or "make video number X".
---

# Video script — background cinema

Talk to the user in short simple sentences. The user is Hungarian.

Read `STRATEGY.md` before writing. Copy `templates/script-template.md` into `scripts/`.

---

## SLEEP MODE (default since 2026-09-27)

Read `SLEEP.md` first. For sleep scripts, these rules **replace** sections 1, 3, 4 and 5 below:

| Old rule (awake videos) | Sleep rule |
|---|---|
| Cold open trailer, no greeting | **Soft welcome**, 1–2 min: where and when we go tonight, "get comfortable", the subscribe ask |
| Micro-hooks, question loops, binary questions | **None after minute 5.** Nothing that makes the brain sit up |
| Chapters every 90–120 s | **Chapters every 8–15 min**, calm labels ("Morning in the Kitchen") |
| Scale paragraph = dopamine | Numbers are fine, said **softly**, never as a burst |
| Rise → excess → fall | **Flat arc.** A day, a season, a place. Ending = night falls, all quiet |
| 60% eerie | **0–10% eerie.** Mild mystery OK, nothing scary, no gore |
| 1,700–2,000 words | **6,500 words = 60 min** (at `--sleep`, measured 108 words/min incl. pauses). 13,000 = 2 h |

**How to write a long sleep script:**

1. Plan all chapters first (title + 5 facts each, with sources). Show the user the plan.
2. Write **one chapter at a time**, 600–1,000 words each. Save after each chapter.
3. Second person works well: "You wake before dawn. The floor is cold under your feet."
4. Short, soft sentences. Sensory details: light, fire, rain, food, fabric, sounds.
5. Gentle repetition is allowed. Come back to the same fire, the same window, the same rain.
6. Every fact true and sourced. List sources at the end of the file.
7. Write the narration file as **plain text** (`scripts/<video>.txt`), one paragraph per beat, blank line between. No headings inside the .txt — put chapter times in the description instead.
8. One image idea per ~250 words (≈ every 1–2 min). Keep them in `scripts/<video>-images.md`.

Everything below is the **older awake format**. Still valid for facts, sources, style and honesty.

## What we are actually making

**Not "content". Background cinema.**

These videos are **NOT** meant to be:

- intensely watched
- paused
- rewatched for details

They **are** meant to be:

- played on the TV
- played while cooking
- played while resting
- played late at night

So: never say "look at this", never "as you can see", never "pause here". The viewer is not looking at the screen. The **voice must carry the whole story alone**. If the story stops working with your eyes closed, rewrite it.

## Hard rules

- **Length ladder:**
  - **Start:** 1700–2000 words = ~12 minutes at 145 words/min. Never shorter.
  - **Normal:** 15–25 minutes once the workflow is smooth.
  - **Later:** 60–100 minute "documentary" episodes. Chapters are what make these work — with 12–18 chapters a 90-minute video still feels digestible. Huge watch time. Do this only after the first 6 videos.
- **Audience: US, 55+, on a TV.** They are not in a hurry.
- **Tone: a documentary narrator, late at night.** Calm. Warm. A little sad.
- **Never:** "Top 10", countdowns, ALL CAPS, "!!!", "SHOCKING", "you won't believe", "hey guys", "let's dive in", "buckle up", fake urgency.
- **Never** invent facts about real, named people. Shaky fact → "records suggest", or cut it.
- **Sources** at the bottom of the script and in the description. Always.

---

## 1. The ANTI-HOOK — a cinematic cold open

The first 20–30 seconds. **No greeting. No channel intro. No "in this video".**

Open like a movie trailer, not like a YouTuber.

**Three moves, in this order:**

1. **Sensory scene.** Put them in a place, at a time, with weather.
   > "Midnight in California. Fog on the lawn. A crooked house with too many windows."
2. **Stack strange visual details, fast.** Three or four, one line each. No explaining.
   > "Stairs that climb into a ceiling. Doors that open into a wall. Windows that look into other windows."
3. **Drop the core thesis in ONE line.**
   > "She believed that if she ever stopped building, she would die."

Then stop. Let it breathe. Then start the story.

**Why this works:**

- You give the viewer a **movie trailer**, not "hey guys".
- It triggers **mental imagery instantly** — perfect for TV, where they are listening more than watching.
- It creates a **question loop in 20 seconds**: madness, or real danger? The brain must stay for the answer.

**Rules for the cold open:** present tense or plain past. Short lines. No numbers yet. No names yet. Never explain what the video is about — show it.

**Prompt tactic (copy this):**

> "Write a 120–160 word cold open. Start with a cinematic scene, list 3–5 unsettling physical details, then reveal a single sentence that reframes the entire story. End on a question that forces a binary interpretation."

**Binary question** = only two possible answers. "Madness, or real danger?" Two doors, not five. The brain must pick a side, so it stays.

More exact prompts: `references/prompt-tactics.md`

---

## 2. Three-block structure

After the cold open, the body is **three blocks**. Each block is a small complete story with its own beginning and end. This is what keeps a 15-minute video from sagging.

| Block | Time | Job |
|---|---|---|
| **Cold open** | 0:00–0:30 | trailer + question loop |
| **Block 1 — The world** | 0:30–5:00 | build it. Make it beautiful, rich, alive. Names, numbers, small details. |
| **Block 2 — The crack** | 5:00–9:00 | the excess. The mistake. The moment it turns. |
| **Block 3 — The fall & what remains** | 9:00–13:00 | the collapse, slow and sad. Then: what stands there today. |
| **Quiet ending** | last 30s | one thought they take to bed. |

The pattern under every video: **rise → excess → fall.** Use it every time. It is the shape our viewers learn to expect and love.

---

## 3. Micro-hooks

At the **end of every block**, plant one line that makes leaving impossible.

- "But the house was not the strange part. The will was."
- "Nobody knew it yet, but the money had already run out."
- "The last train left in 1968. What came back was not a train."

Also drop a small one every ~90 seconds inside a block. One sentence. No shouting. Just a promise that something is coming.

---

## 4. Chapters — they do algorithm work

Put chapters in the video (YouTube timestamps in the description).

**How many:** about **one chapter every 90–120 seconds**.

| Video length | Chapters |
|---|---|
| 12 minutes | 6–8 |
| 20 minutes | 10–12 |
| 60–100 minutes (later) | 12–18 |

Chapters do three things:

1. Make even a very long video feel **digestible**.
2. Give **mini-starts** for viewers who join late.
3. Create **re-entry points** — people come back the next day and continue.

**Because: long videos die when they feel endless.** Chapters are psychological checkpoints. "Two more minutes and I reach the next one."

**Prompt tactic:**

> "Create 12–18 chapters. Each chapter must have: a headline that implies conflict + a first sentence that re-hooks."

(Use 6–8 instead of 12–18 for a 12-minute video. The 12–18 number is for the long-form episodes.)

Chapter headline = a small conflict, never a label.
❌ "The Early Years" → ✅ "The Architect Who Refused To Stop"

---

## 5. The numbers section — dopamine for adults

Every 8–12 minutes, drop a **scale paragraph**: a burst of hard numbers.

> "One hundred and sixty rooms. Forty staircases. Ten thousand windows. Two thousand doors — and some of them opened onto nothing but air."

**Why it works:**

- Older viewers **love concrete specifics and facts**.
- Numbers make the story feel **documentary-real**, not made up.
- It is a **title and thumbnail multiplier** — you reuse "160 rooms" everywhere.

**Prompt tactic:**

> "Insert a 'scale paragraph' every 8–12 minutes: 4–8 verified numbers that quantify the madness."

**Rule: every number must be real and sourced.** A fake number kills the trust the whole channel runs on.

---

## 6. Ambiguity on purpose

When the story has a legend, a ghost, a curse, a mystery:

- **present the folklore** — what people said, what they believed
- **then quietly offer the practical explanation** — the draft, the debt, the illness
- **never fully resolve it**

**Why it works:**

- The viewer stays, hunting for the real answer.
- But you never kill the myth completely. **Myth sells.**
- Comments stay alive for years ("my grandmother worked there and she said...") — and comments keep the video alive.

**Prompt tactic:**

> "For every paranormal claim, include one grounded explanation and leave the verdict open."

**Honesty guard:** never *state* the myth as fact. Say "the family claimed", "locals told each other", "the newspaper reported". Then give the grounded reason. Then stop. That is ambiguity done honestly — it is a real open question, not a lie.

---

## 7. Two-layer audience design

Every script serves **two completely different viewers at once**:

| Layer | Who they are | What they want |
|---|---|---|
| **The paranormal crowd** | came for the strange | seances, bells, curses, the locked room, the thing in the hallway |
| **The history / documentary crowd** | came for the facts | economics, wages, payroll, the Depression, charity, arthritis, architecture |

**That is why it scales faster than a pure ghost story.** Two audiences, one video.

**The mix: 60% eerie narrative + 40% historical context.**

**How to frame it:** *dual-intent packaging.* It **looks** spooky — that is what makes people click. But it **delivers real history** — that is what makes them stay, trust us, and come back.

**Prompt tactic:**

> "Write for two audiences at once: 60% eerie narrative + 40% historical contextualization."

Serve both in **the same section**. The legend gives the feeling; the fact gives the authority. Never drop one — that halves the audience.

Notice the history layer is where the **money words** live: wages, payroll, property, debt, charity, illness. Those are the topics premium advertisers pay for.

---

## 8. Writing style

- **Short sentences.** The AI voice reads them better.
- **Concrete beats adjective.** Not "very rich" → "fourteen fireplaces, and a man whose only job was to keep them lit."
- **Numbers and years** anchor older viewers. Use them often.
- **Pause lines.** After a sad fact, one line alone on its own paragraph. The voice breathes there.
- **Zero filler.** No "as we all know", "without further ado".

---

## 9. Beats and images

Break the script into **beats**. One beat = one image = ~50 words = ~20 seconds.

12 minutes = **35–45 beats**. Write the image idea beside each beat as you write. One visual style for the whole video — never mix.

---

## 10. The compounding rule (important)

Every video must teach the viewer **one era, one class of people, one pattern**.

That way the next video feels easier: *"I already understand this world."* The viewer becomes fluent in our little universe and keeps coming back.

So:

- Stay in the **same world** across videos (same country, same decades, same kind of people).
- **Reuse vocabulary** across videos: the same words for the same things.
- **Reference earlier videos** in one calm line: "The same thing happened on Millionaire's Row, forty years earlier."
- Never explain the whole world from zero every time. Assume a little fluency. Reward the regulars.

---

## Before you call it done

- [ ] Cold open: scene → strange details → one thesis line → binary question. No greeting.
- [ ] 1700+ words, 35–45 beats, each with an image idea
- [ ] 3 blocks, each ending on a micro-hook
- [ ] A chapter every 90–120 seconds (6–8 for a 12-min video), each headline implies conflict, each opens with a re-hook
- [ ] A scale paragraph (4–8 verified numbers) every 8–12 minutes
- [ ] Any legend is presented as a claim, given a grounded explanation, verdict left open
- [ ] Serves both the mystery viewer and the history viewer
- [ ] rise → excess → fall is visible
- [ ] Works with eyes closed (voice carries everything)
- [ ] Zero hype words, zero "hey guys"
- [ ] One era, one class, one pattern — and it fits the channel's world
- [ ] Every name/date/place sourced; nothing invented about a living person
- [ ] Read the cold open out loud, slowly. Does it feel like a trailer?
