# Daily Edge

A personal 20-minute daily digest. News scan: Top 3 that matter, AI in the enterprise, Strategy move decoded, India and GCC lens, Markets in 60 seconds. Learn: Concept of the day, Tech to learn, Case file, Reference shelf, Term of the day. Then Builder edition (Fridays) and Question of the day.

- `index.html` is the whole app (static, no build step). Light, dark and auto appearance.
- `editions/index.json` lists editions; `editions/YYYY-MM-DD.json` holds each day's blocks (schema v4). Older editions (8 articles) still open through the "Earlier editions" list.
- `ops/EDITION_INSTRUCTIONS.md` is what the morning task follows; `ops/validate.py` checks an edition before it is pushed.

New editions are committed every morning at about 7:30 AM IST by a scheduled task. GitHub Pages serves the site from the `main` branch root.
