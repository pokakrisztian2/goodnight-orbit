---
name: thumbnail
description: Make or check a YouTube thumbnail in the anti-design style (quiet, one object, one emotion, muted, few words). Use when the user asks for a thumbnail, a cover image, a title card, or asks "is this thumbnail good?".
---

# Thumbnail — anti-design

Talk to the user in short simple sentences. The user is Hungarian.

## The one law

> **One object. One idea. One emotion.**

A thumbnail must have exactly:

- **one visual anchor** — one thing the eye lands on
- **one emotional tone** — sad, or lonely, or grand. Never two.
- **one intellectual promise** — one question the brain wants answered

**No collage. No chaos.** Never split the image into 2 or 3 panels.

## Why this works (say this if the user asks)

- The brain reads it instantly.
- No decision fatigue. The viewer does not have to choose what to look at.
- No confusion.

> **Confusion kills clicks more than boredom.**
> Most thumbnails fail not because they are boring — but because they are **too busy**.

## Why YouTube likes it (algorithm)

The anti-design thumbnail gives:

- **lower but stable CTR** (fewer clicks, but always the same — no crash)
- **very high watch time**
- **low bounce rate** (people do not leave after 10 seconds)
- **long sessions**
- **frequent returns**

YouTube reads all that as: *"This content satisfies viewers."*

**Satisfaction beats excitement.** A clickbait thumbnail gets the click, then the viewer feels cheated and leaves — YouTube sees that and stops pushing. Our quiet thumbnail gets fewer clicks but happy ones.

Target feeling: **a museum, not TikTok.**

That does two things: we **stand out in the feed**, and we look like **intelligent content**.

## GOOD example (copy this)

Real thumbnail, 301,000 views — *"The Dark Story of America's Most Controversial Mansion: Mar-a-Lago"*

- One black-and-white photo of one mansion. That is the whole image.
- Top: `1923` — one year, warm yellow, classic serif font.
- Bottom: `MAR-A-LAGO MANSION` — serif capitals, one line.
- No face. No arrow. No emoji. No box. No collage.
- One anchor (the house). One tone (old, grand, gone). One promise (what happened in 1923?).

## BAD example (never do this)

Real thumbnail, 742 views — *"Tracing the Roman Empire Through Collapse Till Today"*

- Three pictures glued side by side (Colosseum + Roman street + US Capitol).
- Two yellow arrows between them.
- `ROME NEVER DIED?` in yellow + white + red, huge.
- `ROME AFTER FALL` in red at the bottom, plus 3 little labels and a flag.
- The eye does not know where to go. Too busy → confusion → no click.

Same topic family. 400× fewer views.

## How to make one

1. Read the script. Find the **single saddest or grandest object** in the story. That is the anchor.
2. Generate the image with the `higgsfield-generate` skill. Prompt shape:

   ```
   A single <object>, <state of decay/grandeur>, photographed from <angle>.
   Faded black-and-white archival photograph, soft grain, muted tones,
   overcast light, wide empty space around the subject, no people,
   no text. Calm, quiet, melancholic. 16:9.
   ```

3. Add text **after**, in an editor:
   - 2–4 words maximum, **or** one year + one name.
   - Classic **serif** font (Playfair, Times, Georgia). Never a fat sans-serif.
   - Warm off-white or pale gold. Never pure red. Never a stroke or a glow.
   - Place bottom-left, bottom-right, or top-centre. Keep the bottom-right corner clear — the video length sits there.
4. Save to `thumbnails/<video-name>.png`, 1280×720, under 2 MB.

## Checker (run this on any thumbnail)

Score it. Any ❌ means redo.

- [ ] Only **one** main object?
- [ ] Only **one** feeling?
- [ ] 4 words or fewer? (a year counts as one word)
- [ ] Serif font?
- [ ] Muted / faded colours? No neon, no pure red, no extreme contrast?
- [ ] Zero arrows, circles, emojis, boxes, panels?
- [ ] No face looking at the camera, no shocked face?
- [ ] Empty space around the subject?
- [ ] Readable tiny on a phone **and** big on a TV?
- [ ] Would it look calm and expensive next to 10 loud thumbnails?
- [ ] Does it tell the truth about the video?

## Never say yes to

Big face · red arrow · circle · emoji · 3-panel collage · CAPS everywhere · neon · glow · drop shadow · "SHOCKING" · "YOU WON'T BELIEVE"
