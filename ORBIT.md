# ORBIT.md — Goodnight Orbit (the plan)

Decided **2026-09-28**. This is **the** plan for the channel now.
It replaces the brand, viewer, character and topic list in `SLEEP.md`.
`SLEEP.md` still holds the "not mass-produced" checklist (§1) and the safety rules (§7). Those still apply.
Research behind it: `ideas/research-2026-09-28-cosmo-explains.md`.

---

## 0. Changed from yesterday (2026-09-27 → 2026-09-28)

| | Yesterday (SLEEP.md) | **Now** | Why |
|---|---|---|---|
| Name | Goodnight, Lumen | **Goodnight Orbit** | Unique. Checked free. |
| Character | Lumen, robot in an archive | **Otto, an astronaut on the night shift in orbit** | A robot looks like a copy of Cosmo Explains. |
| Viewer | US 55+, on a TV | **Curious adults who can't switch their brain off at night** | That is who watches the winning videos (data below). |
| Topics | Ice Age, ocean, castles, deep time | **Hard science and tech: physics, AI, electricity, engineering** | Space/biology median ~3K. AI/physics median ~9K. |
| Length | 60–120 min | **~2 hours** | Every Cosmo hit is ~2h. |

The user can overrule any line. Write the new decision here, with the date.

---

## 1. The viewer (think about them first)

**Who:** an adult, 20–50. Likes science, tech, AI. Watches Kurzgesagt, Veritasium in the day.
**When:** in bed, lights off, phone on the nightstand or earbuds in. 11 pm–2 am.
**Their problem:** the brain will not stop. Scrolling makes it worse. Silence makes it worse.
**What they want:**

- Something **interesting enough to stop the thoughts**…
- …but **slow enough to let them drift off**.
- To feel **a little smarter**, not stupid. No pressure to understand everything.
- **Company.** Someone calm who is awake, so they don't have to be.

**What they hate:** loud intros, ads-like hype, music with words, sudden sounds, "SMASH that like", bright screens.

**So every video promises three things:**
1. A hard topic, made gentle.
2. It is OK to fall asleep in the middle. Nothing to miss.
3. Otto is there, keeping watch.

---

## 2. The name: **Goodnight Orbit**

- **Handle @GoodnightOrbit — free** on YouTube (checked 2026-09-28).
- **No channel** with this name in YouTube search. Nearest: "Low Orbit FM", "Somnia's in Orbit" (music, different).
- **goodnightorbit.com / .net — free** (whois, 2026-09-28).
- TikTok / Instagram / X: **check at signup** (the sites hide this without login).
- Why it works: sounds like *Goodnight Moon* (a famous bedtime book). Says **sleep + space** in two words.

Backup names (handles also free): **Orbit Night Shift** (@OrbitNightShift), **Night Shift Astronaut** (@NightShiftAstronaut).

---

## 3. The character: **Otto**

- A small, round astronaut. Soft, worn, cream-white suit with patches and old tape.
- **Visor down.** You never see a face. The visor reflects Earth and a warm lamp. (Easy to keep the same in every AI image.)
- Works the **night shift alone** on a small, old, cozy space station. Plants, books, fairy lights, a tea bag floating.
- **Signature detail: the floating tea.** A ball of tea floats next to Otto in zero gravity, every video.
- **Reference image (approved 2026-09-28): `assets/characters/otto-reference-v1.png`.** Use it in every Otto prompt.
  Its look (soft, warm, a bit 3D, like a toy) is now the style. The station must match it.
- Otto's job: **keep watch over Earth while you sleep.** That is the story. That is why people come back.
- Otto is curious and gentle. Finds hard ideas beautiful. Never shows off. Admits when something is strange.

### The rituals (same words every video — this is the brand)

- **Opening:** *"Hi. It's Otto. It's night on your side of the Earth, and I'm up here on the night shift. I'll keep watch, so you don't have to. Tonight, let's think slowly about…"*
- **Permission line (in every intro):** *"You don't need to understand all of it. If you fall asleep halfway, that's the plan."*
- **Closing:** *"The sun is coming up over the ocean now. My shift is almost over. Sleep well. I'll be up here tomorrow night."*

---

## 4. The twist that makes it ours

Cosmo is a mascot in a room. **We make a show.** Three things nobody in this niche does:

1. **The station falls asleep with you.** Over the 2 hours the scene gets darker, in 4 stages:
   lamps on → lamps dim → only screens glowing → dark, Otto asleep, Earth glowing in the window.
   It matches the viewer's own night. (And "watch the end" makes a good Short.)
2. **Otto has a life.** Small moments in the script: *"The tea's gone cold again."* *"We just passed over Japan. Someone down there is waking up."*
   Links to other nights: *"Remember the night we talked about electricity?"* People come back for Otto.
3. **Shorts funnel.** Cosmo has zero Shorts. Every video gives 3 Shorts: one clear, wow 45-second idea + Otto + "full 2 hours to fall asleep to on the channel".

---

## 5. Format

| | |
|---|---|
| **Length** | ~2 hours (target 120 min). |
| **Words** | ~13,000 at our sleep speed (~108 per minute). |
| **Voice** | Kokoro `am_michael`, `narrate.py --sleep`. Same voice forever. Free. **The voice is Otto.** |
| **Picture** | 12 clips per video: 4 light stages × 3 window views. Each clip 8–15 s, looped. `make_loop_video.py` gives each ~10 min. No new code needed. |
| **Motion** | tiny only: Otto breathes, tea drifts, Earth turns, lights blink. Nothing fast. |
| **Captions** | not burned in (lights-off viewers don't read). Upload the script as YouTube subtitles. |
| **Sound** | voice at -20 LUFS (loudness level). Optional very quiet station hum. No music with words. |
| **Also** | post the audio to Spotify as a podcast. Free extra reach. |

### Script shape (learned from Cosmo's #1 video)

1. **0:00–1:30** Opening ritual → one **surprising human fact** as the hook ("It started with a question a 16-year-old asked.").
2. **~1:30** Permission line + soft subscribe ask: *"If you'd like me on watch again tomorrow, you can subscribe. Then close your eyes."*
3. **Tell it as a story.** Start long before the famous person (Galileo before Einstein). People, not formulas.
4. **Chapters of 8–12 min.** Each one complete. No cliffhangers (we want them asleep).
5. **Otto moments** every few minutes (tea, window, Earth).
6. **Closing:** second person, very slow. Connect the idea to the listener's body in bed: *"the same gravity is holding you gently to your mattress right now."*
7. Closing ritual. Fade to black.

---

## 6. Titles and thumbnails

**Do not copy Cosmo's title.** Keep the same promise (hard + gentle + sleep) in our own words.

- **Main shape:** `The Confusing Parts of [Topic], Explained Gently (For Sleep)`
- **Test shape:** `[Topic], Explained Slowly From Orbit | Science for Sleep`
- Test both in the first 10 videos. Keep the winner.

**Thumbnail (same layout every time):**
- Dark navy-black. Otto small, bottom-left, in the window light. Earth curve in the window.
- **Topic word huge, warm cream colour, middle.** Max 3 words ("RELATIVITY").
- 4–6 small hand-drawn icons of the chapters around it (a menu of the video — this is what works for Cosmo).
- One accent colour per topic (amber, teal, rose). Never bright white.

---

## 7. The first 10 videos

| # | Topic | Why | Proof (Cosmo views) |
|---|---|---|---|
| 1 | The Theory of Relativity | their #1 | 287K |
| 2 | Machine Learning | their #2, AI is the best lane | 239K |
| 3 | Quantum Physics | their #3 | 224K |
| 4 | **How ChatGPT Actually Thinks** | AI gap, big search | LLMs 35K |
| 5 | Electricity | two hits | 41K + 32K |
| 6 | **How a GPU Works (the chip behind AI)** | AI gap, nobody did it | — |
| 7 | Radio Waves and Wi-Fi | RF hit | 79K |
| 8 | Thermodynamics (why everything cools down) | hit | 43K |
| 9 | Nuclear Power | hit | 68K |
| 10 | Time | hit | 29K |

Topics are not owned. Our script, character and pictures are new. That makes it ours.
More ideas: `ideas/ideas-backlog.md`.

**Rhythm:** start with 3 a week. Go daily only when one video takes under 2 hours of work **and** still passes the `SLEEP.md` §1 checklist.

---

## 8. Pictures — the prompts

The user makes the pictures in Higgsfield (Nano Banana for images, image-to-video for motion).
**Paste the STYLE block into every prompt, word for word.** That keeps it one show.

### STYLE (paste into every prompt)

> Style: soft painterly illustration, gouache and colored pencil texture, cozy and quiet, like a frame from a gentle animated film. Muted deep navy and teal shadows, warm amber lamp light, small pops of soft rose. Low contrast, dark overall, calm. Subtle film grain. No text, no letters, no logos, no watermark. 16:9.

### P1 — Otto, character sheet (make first, save as the reference)

> Character reference sheet of "Otto", a small, round, chubby astronaut with a friendly, huggable shape. Cream-white soft spacesuit, a little worn, with faded mission patches, a strip of old grey tape on one knee, a small warm-orange stripe on the arms. Round helmet with the gold visor fully down, no face visible; the visor softly reflects a warm lamp. Short thick legs, mitten-like gloves. Views: front, three-quarter, side, back, and sitting cross-legged floating. Plain soft dark-navy background, even lighting, full body in every view, same proportions in every view. [STYLE]

### P2 — the station module (the "home set", reused every video)

> Inside a small, old, cozy space station module at night, seen from inside. One big round window in the middle-back wall showing the curve of Earth at night with city lights and a thin blue glow of atmosphere. Curved padded walls with handles, cables tied with string, small plants in pouches, a few books strapped to the wall, a string of warm fairy lights, one small amber desk lamp, old screens with soft green lines. Otto (use the reference image) floats cross-legged in front of the window, small in the frame, slightly left of centre, looking out at Earth. A ball of tea floats next to Otto with a tea bag string. Calm, safe, lonely in a nice way. [STYLE]

### P3 — the topic version (one per video)

Edit P2, keep everything, add props for the topic. Example for video 1:

> Same scene, same camera, same Otto. Add a few relativity props floating or stuck to the walls: two old pocket watches showing different times, a hand-drawn sketch of a light beam and a train pinned to the wall, a small chalkboard with a curved grid drawn on it, a tiny model of a clock tower. Keep it tidy and dark. [STYLE]

### P4 — the 4 light stages (edit the topic image 3 times)

- **Stage 1:** the P3 image as it is. (lamps on)
- **Stage 2:** "Same image. Dim all lamps and fairy lights to half. The room is darker and bluer. Earth's glow is stronger." [STYLE]
- **Stage 3:** "Same image. All lamps off. Only the small screens and the Earth light the room. Otto's head tilts a little, sleepy." [STYLE]
- **Stage 4:** "Same image. Almost dark. Otto is asleep, curled up floating, holding the tea ball loosely. Only Earth's blue glow and a few city lights light the room." [STYLE]

### P5 — the window views (3 per stage)

Change only the window, same room: (a) Earth at night with city lights, (b) sunrise line on the horizon, a thin orange glow, (c) aurora green over the dark planet.
Then 4 stages × 3 views = **12 images → 12 clips.**

### P6 — make it move (image-to-video, each image)

> Very slow, calm, seamless loop, 10 seconds. The camera does not move. Otto breathes gently, the tea ball drifts a few centimetres and back, the Earth turns very slowly in the window, fairy lights twinkle softly, tiny dust floats. Nothing else moves. No cuts, no zoom. The last frame matches the first frame.

Save as `assets/loops/<video-name>/01.mp4 … 12.mp4` (order: stage 1 a,b,c → stage 4 a,b,c).

### P7 — the thumbnail base

> Dark navy space station window, huge curve of Earth at night filling the lower half. Otto (reference) small in the bottom-left corner, floating, looking up. Big empty dark space in the middle and top for text. Soft amber light on Otto. [STYLE]

(Add the topic word + icons after, in Canva or with the `thumbnail` skill.)

---

## 8b. The green window (decided 2026-09-28)

- Station image: `assets/scenes/station/station-base-v1.png`. The window is **solid green** (#014413).
- We put space **behind** the window. A mask (`window-mask-v1.png`) opens only the window,
  so the dark room does not turn see-through. Tested: `renders/test-window.mp4` works.
- **Space behind the window:** NASA photos from the ISS (free, public domain, in `assets/space/`),
  drifting very slowly. Or a Veo loop of Earth from orbit. Credit NASA in the description.
- **Animating the room with Veo:** the camera must NOT move, or the mask breaks.
  Veo prompt: *"Static locked camera, no camera movement. The astronaut breathes slowly and gently bobs in zero gravity, the tea floats and sways a little, fairy lights twinkle softly, the desk lamp glows. The round window stays one flat, solid, even green colour the whole time. Nothing else moves. Calm, slow."*
- Loop trick: we play the clip forward, then backward. The seam is invisible. No need for a perfect loop.

## 9. How a video is made

| Step | Tool | Cost |
|---|---|---|
| Topic | this list + `video-idea` skill | $0 |
| Research | NotebookLM / web. Every fact with a source. | $0 |
| Script (~13K words) | Claude, one chapter at a time, `video-script` skill | $0 |
| Voice | `tools/.venv/bin/python tools/narrate.py --name <v> --text scripts/<v>.txt --sleep` | $0 |
| 12 images | Higgsfield, prompts above | a few credits |
| 12 loops | Higgsfield image-to-video | the main cost |
| **Save money:** | make only 4 loops (one per stage) and reuse the 3 window views as still images with ffmpeg motion | cheaper |
| Put together | `python3 tools/make_loop_video.py --name <v>` | $0 |
| Thumbnail | P7 + `thumbnail` skill | $0 |
| Upload | `templates/upload-checklist.md`. Tick "altered or synthetic content". | $0 |

---

## 10. Which channel to use (decided 2026-09-28)

- **Not "chrispokaaa".** It carries Chris's own name and his business brand. Wrong audience.
- **Reuse "Grace & Rest Worship"** (0 subs, 1 video). One weak video does **not** hurt a channel.
  1. Set the worship video to **Private** (not delete — keeps it safe, and it disappears).
  2. Change the **name** to *Goodnight Orbit* and the **handle** to *@GoodnightOrbit*.
     Careful: YouTube allows only **2 changes in 14 days** for each. Do it once, right.
  3. New picture, banner and description.
- A brand-new channel is also fine. At 0 subs it is the same thing.

---

## 11. Numbers to watch

Same as `MONETIZATION-PLAN.md`: **watch hours** and **subscribers** until 1 February 2027.
Plus: **which title shape** wins (§6), and **views from Shorts**.
