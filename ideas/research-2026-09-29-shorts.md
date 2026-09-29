# Research — What makes Shorts work (for Goodnight Orbit), 2026-09-29

Goal: Shorts that bring people to Otto's long sleep videos.
Method: yt-dlp data from 20+ channels (2,862 Shorts titles, 256 Shorts with full details),
12 viral Shorts downloaded and checked frame by frame, plus web research (sources at the end).
Code checked: `tools/make_shorts.py`.

---

## 1. The short version

1. **Sleep channels almost never make Shorts.** Cosmo Explains, Sleepy Science Channel, The Sleepy Scientist, SleepWise, Sleepless Historian, Bub Explains, Science Before Sleep: **0 Shorts**. The few sleep channels that do make Shorts get small numbers (median 5,300–6,600 views).
2. **Science Shorts win big.** Kurzgesagt median 2.6M, Zack D. Films 7.2M, Cleo Abram 3.3M, Science of Infinity 656K. So our Shorts must work as **science Shorts**. The calm comes from Otto's voice and picture, not from being slow.
3. **Length: 30–60 s is right.** Top Shorts cluster at 51–60 s. Very short ones (≤20 s) do worse (8 top vs 22 middle). Our 35–56 s is fine.
4. **Sound starts at 0.0 s.** Every viral narrated Short we checked speaks in the first 0.00–0.17 s. We start at ~0.25–0.4 s, with a fade.
5. **The first sentence must make sense alone.** Our Shorts start with "He used two graphics cards" or "Today, clocks are even more precise". A new viewer does not know who "he" is. Viral Shorts say the hook out loud in second 1.
6. **Viral narrators talk faster:** 155–240 words per minute. Ours is ~120–135 (slowed 20%). The closest calm format (Stephen Dalton sleep stories, 88 wpm) has a median of only 6,600 views. (That could be the sleep niche, not the pace. So we test it, we don't assume.)
7. **Loops help.** A Science Time Short (1.1M) starts mid-sentence and ends so it flows back into the start. Kurzgesagt ends on the same picture it started with.
8. **Our layout is proven.** Astrum's "The Gravity Illusion" (9.2M) and Science of Infinity (83.7M) use the same shape as ours: text on top, a square picture in the middle, text below. Only our **positions** need small fixes (the hook sits under YouTube's top bar).
9. **Titles barely matter.** In 2,862 titles, top Shorts and normal Shorts use the same patterns (questions 25% vs 25%, numbers 11% vs 11%, emoji 30% vs 27%). The picture and the first 2 seconds decide.
10. **The funnel is small.** The "Related video" link gets only a few hundred clicks per 100,000 Short views (creator data). Shorts need volume.

---

## 2. Channels studied (data from 2026-09-29)

Median = the middle Short of the last ≤300 Shorts. "Top length" = median length of the channel's 8 biggest Shorts.

| Channel | Type | Shorts | Median views | Top Short | Its length | Top length | Top Short title (hook) |
|---|---|---|---|---|---|---|---|
| Zack D. Films | animated 3D characters, facts | 300+ | **7,200,000** | 42.5M | 36 s | 38 s | Eagle Gets A 3D Printed Beak 🥲 |
| Cleo Abram | science, face | 300+ | 3,300,000 | 31.2M | 56 s | 60 s | The ISS Is Crashing Into The Ocean |
| Kurzgesagt | animated science | 140 | 2,600,000 | 20.1M | 56 s | 58 s | The Deadly Power of a Coin-Sized Black Hole |
| SolarBalls | animated planet characters | 58 | 1,200,000 | 10.8M | 29 s | 29 s | A Commercial Plane vs the Solar System |
| Science of Infinity | faceless space, meme music | 300+ | 655,500 | 83.7M | 41 s | 30 s | Are Aliens Avoiding Us? 💀👽 |
| AstroKobi | space facts, voice-over | 300+ | 620,500 | 11.8M | 41 s | 60 s | What if we put Solar Panels in Space? |
| Astrum | space, calm voice-over | 35 | 354,000 | 9.2M | 56 s | 56 s | The Gravity Illusion |
| asmr zeitgeist | ASMR | 105 | 249,000 | 3.4M | 41 s | 46 s | ASMR 🧠 BRAIN TINGLES… Literally! |
| Lofi Girl | cozy looping character | 300+ | 129,500 | 5.4M | 60 s | 7 s | Lofi Girl x Ketnipz ✨ |
| StarTalk | science talk | 300+ | 100,000 | 3.4M | 80 s | 57 s | Was Interstellar WRONG? Kip Thorne ANSWERS! |
| Jared Owen | animated 3D explainers | 33 | 76,000 | 2.4M | 59 s | 59 s | Inside of Big Ben |
| Cool Worlds | calm astrophysics | 40 | 35,000 | 237K | 58 s | 59 s | Record Breaking Galaxy Discovered |
| Science Time | space clips + calm voice | 300+ | 20,000 | 26.7M | 52 s | 51 s | An Alien 5% Smarter Than Us |
| Let's Find Out | soft-spoken space ASMR | 3 | 11,000 | 12K | — | — | Light bends and time SLOWS deep in our sun's gravity well |
| Stephen Dalton | sleep stories | 105 | 6,600 | 23K | 57 s | 58 s | A Soothing Sleep Story About Michelangelo 😴 |
| Calm (the app) | sleep sounds | 300+ | 5,800 | 95K | 29 s | 30 s | White noise + pink noise + brown noise + green noise… |
| Get Sleepy | sleep stories | 159 | 5,300 | 90K | 33 s | 47 s | What is Green Noise? |
| MindBlown Daily | generic AI fact Shorts | 66 | **24** | 346 | — | — | 9 Mind-Blowing Shark Facts You Won't Believe! |
| Survival Science Facts | generic AI Shorts | 300 | **23** | 28K | — | — | Ai ASMR #asmr … |
| Cosmo Explains, Sleepy Science Channel, The Sleepy Scientist, SleepWise, Sleepless Historian, Bub Explains, Science Before Sleep, Calm Space, Science for Sleep | sleep science/history | **0** (re-checked: "does not have a shorts tab") | — | — | — | — | (no Shorts at all) |

**What the table says:**
- Sleep channels: few Shorts, weak Shorts. Nobody has proven that sleep Shorts work. That is a risk, and also an empty space.
- Generic "9 mind-blowing facts" AI channels die (median 23–24 views). A character and a real story matter.
- Channels with a **character** win (Zack D. Films, SolarBalls, Kurzgesagt's bird, Lofi Girl).

### Length (256 Shorts with details, top 8 vs middle 8 of each channel)

| Length | Top Shorts | Middle Shorts |
|---|---|---|
| ≤ 20 s | 8 | 22 |
| 21–35 s | 25 | 21 |
| 36–50 s | 27 | 23 |
| **51–60 s** | **51** | 42 |
| 61–90 s | 12 | 14 |
| 91–180 s | 5 | 6 |

→ **30–60 s.** No gain above 60 s. Very short loses.

---

## 3. Twelve viral Shorts, checked frame by frame

Frames at 0 s, 1 s, 2 s, middle, end −1 s, last frame. Speech start and pace from YouTube's captions.
Positions are on a 1080×1920 frame.

| Short | Views | Length | First sound | Words/min | On-screen hook | Captions | Loop / ending |
|---|---|---|---|---|---|---|---|
| Kurzgesagt — Coin-Sized Black Hole | 20.1M | 56 s | music from 0 s | — | "A BLACK HOLE appears!" big, top, from second 1 | small, 1–2 words, y≈1500 | **Last frame = first frame** (coin toss). Seamless visual loop. |
| Astrum — The Gravity Illusion | 9.2M | 56 s | voice at 0.00 s | 191 | **"WHICH BALL / WILL WIN?" on screen the whole time**, top y≈320 + under the picture y≈1600 | none | One single shot, **0 cuts**. The question carries it. |
| Science of Infinity — Are Aliens Avoiding Us? | 83.7M | 41 s | meme song at 0 s | (no voice) | "Pov: Are Aliens Avoiding Us?" white bar, y≈260–420, whole time | none | Square picture in the middle, black above/below — **our layout**. |
| Science Time — Problem With the Speed of Light | 1.1M | 43 s | voice at 0.12 s | 169 | none | none | **Starts mid-sentence** ("because light does not travel at an infinitely fast speed…") and ends "…to cross the known universe takes time" → flows back into the start. |
| StarTalk — "When you die, you don't disappear" | 2.0M | 77 s | voice at 0.00 s | 155 | none | 2 lines, bold, y≈1440 | Calm voice. Ends on a slow galaxy shot. |
| Cool Worlds — Faster-Than-Light = Time Paradoxes | 138K | 155 s | voice at 0.16 s | 210 | Title **types itself in** during seconds 0–2 ("WHY GOING FASTER THAN THE SPEED OF…") | — | **Ends by showing the long video** on the YouTube search page (a direct funnel). |
| Cleo Abram — The ISS Is Crashing Into The Ocean | 31.2M | 56 s | voice at 0.08 s | 241 | the hook is the first spoken sentence | 1 line, y≈1330 | Ends with her pointing + "SUBSCRIBE" sticker. 24 cuts (one every 2.3 s). |
| Zack D. Films — What Is Plato's Cave | 26M | 62 s | sound at 0 s (no silence) | — | no text at 0 s; the character is on screen at once | 1–3 words, white, y≈1500 | Animated characters, camera always moving. |
| SolarBalls — A Commercial Plane vs the Solar System | 10.8M | 29 s | at once | — | planet characters with faces | — | Ends on a title card. |
| Get Sleepy — What is Green Noise? | 90K | 33 s | at once | — | "Time To Relax" small serif, top | long text blocks (hard to read) | Ends with "comment which was most relaxing" + a plug for another channel. |
| Lofi Girl — Infinite pages 😎 | 4.3M | 5 s | music | — | meme text top, y≈270–330 | — | The cozy character **does something** (a joke). The static stream look alone is not what wins. |
| Stephen Dalton — Sleep Story About Michelangelo | 23K | 57 s | music + voice at 0.17 s | **88** | — | — | Slow and calm, like ours. **Low views.** |

**Loudness** of the viral ones: −10 to −21 LUFS (most −12 to −16). Our −14 is fine.

---

## 4. What works — the rules

Each rule has its proof in brackets.

1. **Talk in the first 0.1 s.** No silence, no fade-in. (Every narrated viral Short: first word at 0.00–0.17 s. OpusClip: 50–60% of people who leave do it in the first 3 s.)
2. **The first spoken sentence is the hook.** It must make sense to a stranger. (Cleo: "The International Space Station is crashing down into the ocean in 2030." StarTalk: "In death, you've got pretty much two choices.")
3. **Show the question on screen the whole time.** (Astrum 9.2M, Science of Infinity 83.7M: the text never leaves.)
4. **Something must change in the first 1–2 s.** Text appears, types in, or the camera moves. (Kurzgesagt text pops in at 1 s. Cool Worlds types the title in 0–2 s. Cleo cuts at 0.7 s.)
5. **30–60 s.** Under 20 s loses (8 top vs 22 middle). Over 60 s gains nothing. Between 21 and 60 s the difference is small. (Length table above. YouTube's own guide: ~60 s for Shorts that push people to long videos.) Our `MAX_LEN = 59` is right.
6. **End so it loops.** The last sentence should lead back into the first. Or the last picture = the first picture. (Science Time, Kurzgesagt.) Note: since 31 March 2025 every replay counts as a view, but money and YPP use "engaged views". A loop helps watch-through, not money directly.
7. **One fact, one surprise, one payoff.** Not a list. (Generic list channels: median 23–24 views. Top Shorts are one idea: "coin-sized black hole", "which ball wins".)
8. **A character helps.** (Zack D. Films, SolarBalls, Kurzgesagt's bird, Lofi Girl.) Otto is our advantage. Let Otto say "I" in the Short ("The reason I float is that I'm falling").
9. **Use a quiet sound bed.** Most viral Shorts we checked have music or ambience under the voice. Silence between sentences feels "dead" in the feed.
10. **Point to the long video.** Set the "Related video" link on every Short. Say or show where the full video is. (YouTube's guide, July 2026: match the Short's topic to the linked video; say the call to action out loud or point at the link. Cool Worlds shows the long video at the end.)
11. **Keep text out of YouTube's buttons.** (Safe zone numbers in section 5.)
12. **Post a lot.** (vidIQ, 10.2M channels: channels with 12+ uploads a month grew 4.1× faster. Science of Infinity posts 1 per day. Zack D. Films posts 4–5 per day.)
13. **Don't look mass-made.** YouTube's "inauthentic content" rule (July 2025) hits "mass-produced, generic, repetitive" AI content. Cutting from our own long video is fine. But vary the hook, the picture and the ending between Shorts.

---

## 5. Changes for our Shorts maker (`tools/make_shorts.py`) — in priority order

### 1. Start the sound at 0.0 s
- Now: `a = max(a - 0.25, 0)` and `afade=t=in:d=0.15` → the first word comes at ~0.25–0.4 s.
- Change: cut at the first word's start **minus 0.03 s**. Fade-in **0.02 s** (only to stop a click).

### 2. A spoken hook in the first second
- Now: the Short starts with a sentence from the middle of the story ("He used two graphics cards…").
- Change: add a field `"say"` to each Short in `videos/<name>.json`. Make it with `narrate_gemini.py` (same voice). Put it **before** the segment, with a 0.3 s gap.
- Rule: `say` = the hook text, or a spoken version of it. Max 12 words. Max 3 s.
- Example: `{"hook": "I'm not floating. I'm falling.", "say": "People think I float because there's no gravity up here. That's not true.", "from": "The reason I float", "paras": 2}`

### 3. Pick segments that end on the payoff (loop)
- Now: `b = last caption + 0.6 s`, then a 0.5 s fade-out.
- Change: end **0.15 s after the last word**. Fade-out 0.1 s.
- Choose segments whose **last sentence is the surprise** ("Your head is older than your feet." is already the last line — good).
- Then the loop works: the last line → back to the hook text on top.
- Test by watching 3 loops in a row. It should feel like one thought.

### 4. Normal voice speed for Shorts
- Now: voice slowed 20% → ~120–135 words/min.
- Change: for Shorts, **use the voice at its natural speed** (~169 words/min). Keep the deep, calm tone.
- How: `narrate_gemini.py` slows the voice with `TEMPO = 0.8` (ffmpeg `atempo`). To undo it in the Short, add `atempo=1.25` to the audio filter (pitch stays the same).
- Then **multiply every caption start/end time by 0.8** (the captions in `captions.ass` are timed to the slow audio). Same for the cut points `a` and `b`.
- Make the `say` lines with `--tempo 1.0` (no slowdown).
- Why: viral narrators speak at 155–240 wpm. The slow sleep-story Shorts (88 wpm) have a median of 6,600 views.
- The Short is the trailer. The long video is the bed.
- **Test it:** post 4 Shorts at normal speed and 4 slowed. Compare "Viewed vs swiped away" in Studio after 7 days.

### 5. Fix the positions (safe zones)
YouTube's buttons cover parts of the 1080×1920 frame:
- **Top:** ~170 px (phone app bar). Google's stricter ads guide says 288 px.
- **Bottom:** ~330 px (title, channel, "Related video" chip). The stricter guide says 672 px.
- **Right:** ~120 px (like, comment, share buttons, from about y = 900 down). The stricter guide says 192 px.
- **Left:** ~50 px.

**Rule: put all text between y = 180 and y = 1400, and between x = 60 and x = 900.**

Now in the code:
- Hook: `MarginV 40` → the hook sits at y ≈ 40–170, **under the top bar**. ❌
- Square: `SQUARE_Y = 260` → square from y = 260 to y = 1340.
- Captions: top-aligned, `MarginV 1275` → y ≈ 1275–1400. They overlap the bottom of the square (OK), and they fit.

New values:
| Item | New value |
|---|---|
| Hook style | font 72, **MarginV 190**, MarginL 60, MarginR 120, max 2 lines, max 7 words |
| `SQUARE_Y` | **360** (square y = 360–1440; 2 hook lines end at ~y 350) |
| Captions | font 100, 1–3 words, **MarginV 1260** (y ≈ 1260–1380, over the lower part of the square — check it is readable on the station image; keep the dark outline), MarginL 90, MarginR 150 |
| Nothing | below y = 1400 except the picture |

### 6. Add motion (cheap)
- Now: the loop barely moves. A still picture gets swiped.
- Change 1: **slow push-in** over the whole Short, 100% → 108%. ffmpeg: `zoompan=z='1+0.08*on/(DUR*30)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1080:fps=30` on the square.
- Change 2: **in the first second**, the hook text pops in (scale 90% → 100% in 0.3 s, ASS `\t` tag), not already there at frame 0.
- Change 3: at the middle, **switch the window view** (e.g. night → aurora clip). One soft cut. (Astrum shows that 0 cuts is OK if the question is strong. So this is optional.)

### 7. Add a quiet sound bed
- A soft station hum or a slow ambient pad, **~18–20 dB under the voice**. No melody with words.
- Starts at 0.0 s together with the voice. Same bed every Short = brand sound.

### 8. Point to the long video
- **Every Short: set "Related video"** in YouTube Studio → the full long video. (Links in Shorts descriptions are not clickable since 2023.)
- Last 3 s: small text above the captions, y ≈ 1150: *"Full 1h 40m version for sleep ↓"*. Do **not** add a spoken call to action (it breaks the loop).
- Later test: a spoken line "The full slow version is linked below" on 3 Shorts. YouTube's guide says spoken CTAs help. Compare clicks.

### 9. How many
- **2 Shorts per day**, at least 6 hours apart. (3 per long video × daily long videos = enough material.)
- If the material runs out, 1 per day. Never less than 12 per month (vidIQ: 12+/month = 4.1× growth).

### 10. Which segments to pick
Pick a segment if it has **all four**:
1. **A surprise that sounds wrong but is true** ("Your head is older than your feet", "Astronauts are falling").
2. **A number or a real object** (33 cm, 1 in 10,000, two gaming cards, radio knobs).
3. **It works without the rest of the video.** No "he", "it", "this" at the start that points back.
4. **It ends on the payoff sentence.**

Best topics for Shorts (from Cosmo's long-video data + Shorts data): AI and physics facts, "you" facts (something happening to your body right now), famous-person surprises.
Avoid: slow history setup, lists, formulas without a picture.

### 11. Title and hashtags
- Titles don't change views much in Shorts (section 1, point 9). Keep them simple and searchable.
- **Title formula:** `[the hook, ≤ 60 characters] | Otto explains [topic] 🌙`
  - e.g. `Your head is older than your feet | Otto explains relativity 🌙`
- `#shorts` is **not needed** (also remove it from the `Title:` line that `make_shorts.py` writes) (YouTube detects Shorts by shape + length ≤ 3 min). Use 2–3 topic hashtags in the description: `#physics #science #sleep`.
- First line of the description: "Full slow version for sleep: [title of the long video]".

---

## 6. New hooks for our 9 Shorts

Top text = the hook on screen (≤ 7 words). Spoken = the new `say` line for the first second.

| # | Now | New on-screen hook | Spoken first line (`say`) |
|---|---|---|---|
| 1 | Your head is older than your feet | **Your head is older than your feet** (keep — it's strong, and it is the last line → perfect loop) | "Right now, your head is aging faster than your feet. Scientists measured it." |
| 2 | Einstein never actually wrote E = mc squared | **E = mc² is not in Einstein's paper** | "Einstein's famous 1905 paper never writes E equals m c squared." |
| 3 | Astronauts don't float because there's no gravity | **I'm not floating. I'm falling.** | "Everyone thinks I float because there's no gravity up here. That's not true." |
| 4 | Particles that should be dead before they reach you | **Something from space is passing through you** | "Right now, tiny particles from space are passing through your body. They shouldn't be." |
| 5 | The AI that changed everything was trained in a bedroom | **Modern AI started in a bedroom** | "The AI boom started on two gaming cards, in a student's bedroom." |
| 6 | The first learning machine turned its own knobs | **This 1958 machine learned by turning knobs** | "The first machine that learned didn't have code. It had knobs. And it turned them itself." |
| 7 | The Go move that stunned the world | **Move 37: 1 in 10,000 humans** | "In 2016, a computer played a move so strange that its opponent walked out of the room." |
| 8 | King minus man plus woman equals... | **King − man + woman = ?** | "Take the word king. Take away man. Add woman. An AI knows the answer." |
| 9 | Why AI makes things up | **AI bluffs like a student in an exam** | "Why does AI make things up? Researchers found a very human reason." |
| 10 | (spare for #3, test A/B) | **Astronauts aren't floating** | "The reason I float is that I'm falling. All the time." (this is already the first line of the segment — no new audio needed) |

Checks for #6: the Mark I Perceptron was built 1957–58 at Cornell Aeronautical Laboratory, Buffalo. The script says "sixty-odd years ago" — fine.
Checks for #7: DeepMind's "1 in 10,000" estimate is in our script. Lee Sedol left the room (script). OK.

**Hook wording rules:**
- ≤ 7 words on screen. One idea.
- Say something that **sounds wrong** but is true. Or ask a question with a clear answer coming.
- Use **"you"** or **"I" (Otto)** when possible.
- A number or a real object beats an abstract word ("two gaming cards" > "limited hardware").
- No hype words: no "INSANE", "mind-blowing", no 💀. Calm and sure is our voice.
- The on-screen hook and the spoken first line say the **same thing** in different words.

---

## 7. What to watch in YouTube Studio

- **Viewed vs swiped away** (Studio → the Short → Analytics; it sits next to "Shown in feed"). Creator benchmarks: 70%+ good, under 60% the hook fails. (Creator numbers, not YouTube's. Compare with our own Shorts.)
- **Average % viewed**: aim for 80%+ (loops can push it above 100%).
- **Related video clicks** → how many long-video views come from Shorts (Studio → long video → Traffic source → "Shorts feed").
- **Subscribers from each Short.** Expect low: creator data says 0.05–0.5% of views.

**Remember:** Shorts views do **not** add watch hours for YPP (the 4,000 / 8,000 hours count long videos only). The Shorts path to YPP is 10M Shorts views in 90 days (reportedly 20M from 1 Feb 2027 — secondary sources: ppc.land, vidIQ, Aug 2026). That is far away. **So a Short is only worth it if it sends people to the long video or makes them subscribe.** Watch the Related-video clicks first.

## 8. What we do next

1. **Change `make_shorts.py`:** sound at 0.0 s, tight end (+0.15 s), new hook/caption positions, `atempo=1.25` (+ caption times ×0.8), slow push-in, quiet sound bed. (Section 5, items 1, 3–7.)
2. **Add the `say` lines** from section 6 to `videos/relativity.json` and `videos/machine-learning.json`, make them with `narrate_gemini.py`, and re-render the 9 Shorts.
3. **Upload 2 per day** with "Related video" set to the long video. After 7 days, read "Viewed vs swiped away" and Related-video clicks, and keep what works.

---

## Sources

- YouTube Help — Shorts up to 3 minutes: https://support.google.com/youtube/answer/15424877
- YouTube blog — longer Shorts (Oct 2024): https://blog.youtube/news-and-events/tall-updates-coming-to-shorts/
- YouTube blog — Related video traffic guide (Jul 2026): https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/
- YouTube Help — Shorts features, related video, hashtags: https://support.google.com/youtube/answer/10059070 , https://support.google.com/youtube/answer/6390658
- YouTube Help — "Viewed vs swiped away": https://support.google.com/youtube/answer/12942217
- YouTube monetization policy ("inauthentic content", Jul 2025): https://support.google.com/youtube/answer/1311392
- Google Ads Shorts safe-zone overlay (measured: safe box x 48–888, y 288–1248): https://services.google.com/fh/files/misc/youtubesafezoneoverlay_vertical_final.png (from https://support.google.com/google-ads/answer/13547298)
- Organic safe zones (top ~170, bottom ~330, right ~120): https://www.pod2reels.com/blog/youtube-shorts-safe-zone-guide
- Shorts views count every replay (Mar 2025): https://techcrunch.com/2025/03/26/youtube-is-changing-how-youtube-shorts-views-are-counted
- Rene Ritchie, "Shorts will not hurt your long-form": https://www.tubefilter.com/2024/08/26/rene-ritchie-shorts-creator-faqs/
- Todd Beaupré, Creator Insider (Sep 2026), Shorts ranking uses satisfaction: https://www.youtube.com/watch?v=rHLjxrbXmmY
- OpusClip retention/length data (Nov 2025): https://www.opus.pro/blog/ideal-youtube-shorts-length-format-retention
- vidIQ posting frequency (10.2M channels): https://vidiq.com/blog/post/How-Often-Post-on-Youtube/
- Related-video click rates (creator data, Sep 2026): https://outlierkit.com/resources/youtube-shorts-to-long-form/
- Swipe-away benchmarks (creator data): https://www.shortimize.com/blog/youtube-shorts-retention-rate
- Metricool Shorts vs long-form study (Aug 2026): https://www.tubefilter.com/2026/08/03/youtube-shorts-long-form-study-metricool/
- YPP 2027 change (secondary): https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/ , https://vidiq.com/blog/post/youtube-partner-program-changes-2027/

**Limits of this data:** channel medians use the newest ≤300 Shorts. yt-dlp view counts on Shorts tabs are rounded (e.g. "7.2M"). Viral Shorts are a small sample (12). Treat numbers as direction, not law. Our own Studio data beats all of this after ~20 Shorts.
