"""Validate a Daily Edge edition file (schema v4). Usage: python3 ops/validate.py editions/YYYY-MM-DD.json"""
import json, sys, datetime
errs = []
def e(m): errs.append(m)
def wc(s): return len(str(s or '').split())
p = sys.argv[1]
raw = open(p, encoding='utf-8').read()
d = json.loads(raw)
json.load(open('editions/index.json', encoding='utf-8'))
if '—' in raw or '–' in raw: e('contains an em or en dash')
for k in ['v', 'date', 'label', 'blocks']:
    if k not in d: e('missing top-level key: ' + k)
if d.get('v') != 4: e('"v" must be 4')
friday = datetime.date.fromisoformat(d['date']).weekday() == 4
want = ['top3', 'ai', 'strategy', 'india', 'markets', 'concept', 'learn', 'case', 'shelf', 'term'] + (['builder'] if friday else []) + ['question']
bl = d.get('blocks', [])
if [b.get('id') for b in bl] != want: e('blocks must be exactly, in order: ' + ', '.join(want))
MIN = {'top3': 3, 'ai': 2, 'strategy': 2, 'india': 2, 'markets': 1, 'concept': 3, 'learn': 2, 'case': 2, 'shelf': 1, 'term': 1, 'builder': 2, 'question': 1}
GROUP = {'top3': 'News scan', 'ai': 'News scan', 'strategy': 'News scan', 'india': 'News scan', 'markets': 'News scan', 'concept': 'Learn', 'learn': 'Learn', 'case': 'Learn', 'shelf': 'Learn', 'term': 'Learn', 'builder': 'Build', 'question': 'Close'}
LEARN = ('concept', 'learn', 'case', 'shelf', 'term')
NCARDS = {'top3': 3, 'concept': 2}
def card(c, where, lo=70, labels=False):
    for k in ['tag', 'title', 'what', 'why', 'say', 'deeper', 'sources']:
        if not c.get(k): e(where + ': missing ' + k)
    if wc(c.get('title')) > 12: e(where + ': title over 12 words')
    if wc(c.get('what')) > 25: e(where + ': what over 25 words')
    if wc(c.get('why')) > 22: e(where + ': why over 22 words')
    if wc(c.get('say')) > 20: e(where + ': say over 20 words')
    n = wc(' '.join(c.get('deeper', [])))
    if not lo <= n <= 150: e(where + ': deeper is %d words (want %d to 150)' % (n, lo))
    if labels:
        for k in ['whatLabel', 'whyLabel', 'sayLabel']:
            if not c.get(k) or wc(c[k]) > 5: e(where + ': needs ' + k + ' (max 5 words)')
    if not 1 <= len(c.get('deeper', [])) <= 2: e(where + ': deeper needs 1 or 2 paragraphs')
    for s in c.get('sources', []):
        if not s.get('title') or not str(s.get('url', '')).startswith('https://'): e(where + ': each source needs a title and an https url')
    v = c.get('visual')
    if not v: e(where + ': missing visual'); return
    t = v.get('type')
    if t == 'stat':
        if not v.get('value') or len(str(v['value'])) > 7: e(where + ': stat value missing or over 7 characters')
        if not v.get('label') or wc(v['label']) > 14: e(where + ': stat label missing or over 14 words')
    elif t == 'bars':
        it = v.get('items', [])
        if not 2 <= len(it) <= 4: e(where + ': bars need 2 to 4 items')
        if any(not isinstance(x.get('value'), (int, float)) for x in it): e(where + ': bar values must be numbers')
        if sum(1 for x in it if x.get('hot')) != 1: e(where + ': exactly one bar must be hot')
    elif t == 'steps':
        it = v.get('items', [])
        if not 3 <= len(it) <= 4: e(where + ': steps need 3 or 4 items')
        if any(wc(x.get('label')) > 3 for x in it): e(where + ': step labels max 3 words')
    elif t == 'flow':
        it = v.get('items', [])
        if not 3 <= len(it) <= 4: e(where + ': flow needs 3 or 4 items')
        if any(wc(x.get('label')) > 3 or not x.get('note') or wc(x.get('note')) > 10 for x in it): e(where + ': flow items need a label (max 3 words) and a note (max 10 words)')
        if sum(1 for x in it if x.get('hot')) != 1: e(where + ': exactly one flow item must be hot')
    else: e(where + ': visual type must be stat, bars, steps or flow')
for b in bl:
    i = b.get('id')
    if not b.get('title') or not b.get('sub'): e('%s: needs title and sub' % i)
    if b.get('minutes') != MIN.get(i): e('%s: minutes must be %s' % (i, MIN.get(i)))
    if b.get('group') != GROUP.get(i): e('%s: group must be "%s"' % (i, GROUP.get(i)))
    if wc(b.get('sub')) > 9: e('%s: sub over 9 words' % i)
    if i in ('top3', 'ai', 'strategy', 'india', 'builder') + LEARN:
        cs = b.get('cards', [])
        if len(cs) != NCARDS.get(i, 1): e('%s: needs %d card(s)' % (i, NCARDS.get(i, 1)))
        for n, c in enumerate(cs): card(c, '%s card %d' % (i, n + 1), lo=(35 if i in ('term', 'shelf') else 60), labels=(i in LEARN))
    if i == 'learn':
        t = b.get('track') or {}
        if not t.get('topic') or t.get('total') != 5 or t.get('step') not in (1, 2, 3, 4, 5) or len(t.get('plan', [])) != 5 or not t.get('next'): e('learn: track needs topic, step 1 to 5, total 5, plan of 5 titles and next')
    if i == 'markets':
        m = b.get('markets') or {}
        NAMES = ['Nifty 50', 'Sensex', 'Nikkei 225', 'Hang Seng', 'Shanghai', 'FTSE 100', 'DAX', 'S&P 500', 'Nasdaq', 'Dow Jones']
        ix = m.get('indexes', [])
        if [x.get('name') for x in ix] != NAMES: e('markets.indexes must be exactly, in order: ' + ', '.join(NAMES))
        for x in ix + m.get('extras', []):
            c = x.get('change')
            if c is not None and not isinstance(c, (int, float)): e('markets: change for %s must be a number or null' % x.get('name'))
        if any(not x.get('close') or not x.get('region') for x in ix): e('markets: every index needs close and region')
        if [x.get('name') for x in m.get('extras', [])] != ['Gold', 'Brent crude', 'USD/INR']: e('markets.extras must be Gold, Brent crude, USD/INR')
        if not m.get('asof') or not m.get('sources'): e('markets: missing asof or sources')
        if not m.get('why') or wc(m['why']) > 22: e('markets: why missing or over 22 words')
    if i == 'question':
        q = b.get('question') or {}
        if not q.get('text') or wc(q['text']) > 22: e('question: text missing or over 22 words')
        if not q.get('context') or wc(q['context']) > 35: e('question: context missing or over 35 words')
print('OK' if not errs else 'ERRORS:\n- ' + '\n- '.join(errs))
sys.exit(1 if errs else 0)
