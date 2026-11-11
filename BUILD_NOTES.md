# Daily Edge v3 build notes (resume file)

Goal: home page with six sections in two groups.
- Work: Stock Watch (world indexes, yesterday's move and why), Daily Edge (4 short reads), Tech to learn (weekly track, one step per weekday; Stack Watch folded in here)
- Build: What's selling in vibe-coded apps (Mon), Distribution playbook (Wed), Underserved AI-first markets (Fri)

Rules: plain language, reads 300 to 400 words, about 15 minutes a day, visuals drawn from data, no em dashes, sources on everything. Palette: paper #F3F2EF, graphite #1B1E22, orange #EE5A2E.

Edition schema v3 (editions/YYYY-MM-DD.json): existing keys plus
- markets {asof, title, summary, indexes[{name,region,close,change,why}], extras[{name,value,change}], body[], sources[]}
- learn {topic, total, steps[{n,title,body[],diagram[{label,note}],try}], sources[]}
- build {selling{}, distribution{}, gaps{}} each {updated, title, figure{}, what, why, use, bars[{label,value,unit,note}], body[], sources[]}; gaps also has scores[{label,score}]
Old editions (8 articles + stack) must still render.

## Status
- [ ] 1. Content for 2026-11-11: markets, learn, build added to the edition file
- [ ] 2. index.html rebuilt (home + section views + visuals)
- [ ] 3. Rendered and checked at phone width
- [ ] 4. Pushed to main and mirrored to artifact fa307d16-f022-41bd-86d6-dc26c3f2e9d7
- [ ] 5. Morning task trig_01EuCQHL7o6Vsxs4DMvo4GSE updated to schema v3
