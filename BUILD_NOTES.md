# Daily Edge v4 build notes

Goal: a digest that fits 20 minutes and never feels like reading. Seven blocks, one phone screen per item, about 60 words per card, depth behind a tap.

Blocks and minutes: Top 3 that matter (5), AI in the enterprise (4), Strategy move decoded (3), India and GCC lens (3), Markets in 60 seconds (1), One idea to keep or, on Fridays, Builder edition (3), Question of the day (1).

Card: tag, title (max 12 words), one visual (stat, bars or steps), What, Why it matters, Say it in the room, optional "Go deeper" (70 to 150 words) with sources.

Appearance: Auto, Light, Dark. Stored on the device under `de-theme`. Palette: paper #F3F2EF, graphite #1B1E22, orange #EE5A2E.

Edition schema v4: {"v":4,"date","label","blocks":[{id,title,sub,minutes,cards[]|markets{}|question{}}]}. Full rules in ops/EDITION_INSTRUCTIONS.md; ops/validate.py enforces them. Editions without "blocks" (v2 and v3) are mapped to blocks by the app so the archive still opens.

## Status (13 Nov 2026)
- [x] index.html rebuilt for v4 with light and dark mode
- [x] 2026-11-13 edition rewritten in v4
- [x] Instructions and validator moved to v4
- [ ] Morning task still runs its old prompt; owner to replace it with one that follows ops/EDITION_INSTRUCTIONS.md. Until then new editions arrive in the old shape and open as "Earlier format".
