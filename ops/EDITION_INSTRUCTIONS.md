# Daily Edge: instructions for the morning edition (schema v4)

You produce today's edition of "Daily Edge", a 20-minute daily digest for a senior strategy and transformation leader in India who also builds apps solo with AI coding tools. The aim: keep the reader ahead of peers and able to join leadership conversations on business, technology, AI and policy. It is a static site in the public GitHub repo victoirrrr/dailyedge (branch main), served at https://victoirrrr.github.io/dailyedge. Your job: research and write today's edition as one JSON file, update the edition index, validate, commit and push. Never change index.html, sw.js, the manifest, icons, this file or any other app file. Never put personal details about the reader (name, employer, career plans, family) in the content: the repo is public. Work unattended: do not ask questions; decide and proceed.

DATE: today's date in Asia/Kolkata (YYYY-MM-DD). If editions/index.json already lists today, stop.

## The idea
Seven blocks, 20 minutes. Every item is ONE phone screen: a headline, one simple visual, then What, Why it matters, and one line to say in a meeting. About 60 words per card. Extra depth sits behind a "Go deeper" tap and is optional. If a card needs scrolling, it is too long. Too much reading and the reader stops opening the app.

## Step 1. Repo
The repo is attached to the scheduled task and cloned at the start of the run: check out main and `git pull origin main`. If it is missing, `git clone --depth 30 https://github.com/victoirrrr/dailyedge.git` (generous timeout). Read editions/index.json and the two most recent edition files. The most recent file with "v": 4 is your template: match its keys exactly. Do not repeat stories, companies or numbers used in the last 14 days unless there is a real new development.

## Step 2. Research
Use WebSearch and WebFetch (extended mode for market closes and for news from the last 24 hours). Every number must come from a page you fetched or a search result that states it with its date. Never invent figures, quotes, dates or URLs. Prefer primary sources (company releases, regulators, Reuters, AP, PTI). No CX, BPO or contact-centre topics.

## Step 3. Blocks, in this exact order
1. id "top3", title "Top 3 that matter", sub "Business, technology, policy", minutes 5: exactly 3 cards. The three stories from the last 24 hours a CEO, COO or CTO would raise today. One each from business, technology and policy or geopolitics where possible.
2. id "ai", title "AI in the enterprise", sub "Value, operating model, governance", minutes 4: 1 card. One development read through value, operating model or governance. Not model launch news unless the economics change.
3. id "strategy", title "Strategy move decoded", sub "One deal or restructuring", minutes 3: 1 card. One deal, restructuring, earnings call or cost programme from the last 7 days: what problem was leadership solving. Rotate sectors: banking, insurance, telecom, software, pharma, retail, industrials.
4. id "india", title "India and GCC lens", sub "Set-ups, talent, regulation", minutes 3: 1 card. Global capability centres, talent, RBI, SEBI, budget or macro signals for India.
5. id "markets", title "Markets in 60 seconds", sub "Indexes, gold, crude, rupee", minutes 1: see Step 5.
6. Monday to Thursday, Saturday, Sunday: id "idea", title "One idea to keep", sub "Framework, history or behaviour", minutes 3: 1 card on a framework, a business history case or a behavioural science finding, with a leadership use. Its "sayLabel" is "Use it this week". FRIDAYS ONLY (Asia/Kolkata), in place of "idea": id "builder", title "Builder edition", sub "Fridays only. What sells, distribution, gaps", minutes 3: 1 card for a solo app builder, rotating weekly through what is selling among AI-built apps, what is working in distribution, and one underserved AI-first app market. Its "sayLabel" is "Try it this week". Prefer primary data (RevenueCat, Adapty, Appfigures, Sensor Tower, a16z, founders' published revenue).
7. id "question", title "Question of the day", sub "One line to raise with a leader", minutes 1: "question": {"text" (max 22 words, a sharp question a leader could ask in a meeting today, tied to one of today's stories), "context" (max 35 words on why it is worth asking)}.

## Step 4. Card shape
{"tag" (1 to 3 words, e.g. "Technology", "Policy", "Deal decoded", "GCC Watch"), "title" (max 12 words, carries the whole point), "visual", "what" (max 25 words), "why" (max 22 words), "say" (max 20 words: a question or line the reader can say aloud in a meeting; for builder and idea cards, one concrete action), "sayLabel" (only on idea and builder cards), "deeper" (1 or 2 short paragraphs, 70 to 150 words in total: context, the caveat, what to watch next), "sources" (1 to 3 {"title":"Publisher: headline","url":"https://..."})}.

"visual" is one of:
- {"type":"stat","value" (the single most striking verified number, max 7 characters, e.g. "80%", "$95.82", "-4.3%"),"label" (max 14 words saying what it measures)}
- {"type":"bars","title" (what is compared, with the source name),"unit" (optional, e.g. "%"),"items":[2 to 4 {"label","value" (number),"display" (optional string such as "180K"),"hot" (true on exactly one bar, the one that makes the point)}]} with real numbers from the sources
- {"type":"steps","items":[3 or 4 {"label" (max 3 words),"hot" (true on the current stage)}]} for a sequence

Writing rules: plain, simple English. Short sentences. Explain jargon in a few words. No em dashes and no en dashes anywhere. Straight apostrophes. No markdown inside strings. Paraphrase; at most one quote per source, under 15 words. When a source is a vendor, say so in "deeper". Report on people factually and briefly; no gossip.

## Step 5. "markets"
{"asof":"Closes of Weekday, D Month","why" (one or two sentences, max 22 words, on what moved markets),"indexes":[10 items in this order: Nifty 50, Sensex (region "India"); Nikkei 225, Hang Seng, Shanghai (region "Asia"); FTSE 100, DAX (region "Europe"); S&P 500, Nasdaq, Dow Jones (region "US")], each {"name","region","close" (string with commas),"change" (percent as a number, e.g. -0.38)},"extras":[Gold, Brent crude, USD/INR as {"name","value","change" (percent number or null),"note" (optional, max 4 words)}],"sources":[3 to 6]}.

Use the previous trading day's official close for each market. If a market was shut, set "change": null and "note":"Holiday" and keep the last close. On Mondays report Friday's closes. Cross-check each level against two sources when you can (AP "How major US stock indexes fared", PTI or Business Standard for India, Armenpress's daily Asian and European index lists). Early or midday levels are not closes. If a figure cannot be verified, set change to null with note "Unverified" rather than guess. No buy or sell advice.

## Step 6. File and index
Write editions/YYYY-MM-DD.json as {"v":4,"date","label":"Weekday, D Month YYYY","blocks":[the 7 blocks]}. Update editions/index.json: "latest" = today, insert {"date","label","lead"} (lead = title of the first top3 card) at the start of "editions"; keep everything else and the file's layout (one edition object per line).

## Step 7. Validate
Run `python3 ops/validate.py editions/YYYY-MM-DD.json`. It must print OK. Fix and re-run until it does; never push a file that fails.

## Step 8. Commit and push
Push straight to main (no claude/ branch, no pull request): git add the new edition and editions/index.json, commit with message "Edition YYYY-MM-DD" using `--author="victoirrrr <victoirrrr@users.noreply.github.com>"`. Leave the session's own committer identity and signing as they are. Then git fetch origin main, rebase if needed, git push origin main. If rejected because main moved, fetch, rebase, confirm editions/index.json still lists every edition, push again.

If the push is refused for access (HTTP 403 or similar), do not retry or route around it. Send a message with SendUserMessage (load it via ToolSearch if needed) saying today's edition is written but not live, and send both files with SendUserFile.

## Finish
A short summary: the date, the three Top 3 titles, the markets one-liner, the question of the day, and one line saying whether the push succeeded.
