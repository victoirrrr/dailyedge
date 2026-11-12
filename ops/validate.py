"""Validate a Daily Edge edition file. Usage: python3 ops/validate.py editions/YYYY-MM-DD.json"""
import json, sys, re
errs = []
def e(m): errs.append(m)
p = sys.argv[1]
raw = open(p, encoding='utf-8').read()
d = json.loads(raw)
json.load(open('editions/index.json', encoding='utf-8'))
if '—' in raw or '–' in raw: e('contains an em or en dash')
for k in ['date', 'label', 'articles', 'markets', 'learn', 'build']:
    if k not in d: e('missing top-level key: ' + k)
if 'stack' in d: e('remove the old "stack" section')
SECS = ['AI Signal', 'GCC Watch', 'Geopolitics', 'Transformation', 'Good to Know', 'Good to Know', 'Startup Story', 'The Story']
arts = d.get('articles', [])
if len(arts) != 8: e('need 8 articles, found %d' % len(arts))
for i, a in enumerate(arts):
    if a.get('n') != i + 1: e('article %d: n should be %d' % (i + 1, i + 1))
    if i < 8 and a.get('section') != SECS[i]: e('article %d: section should be "%s"' % (i + 1, SECS[i]))
    for k in ['title', 'what', 'why', 'use', 'body', 'sources']:
        if not a.get(k): e('article %d: missing %s' % (i + 1, k))
    w = len(' '.join(a.get('body', [])).split())
    if not 280 <= w <= 420: e('article %d: body is %d words (want 300 to 400)' % (i + 1, w))
def fig(f, where):
    if f and len(str(f.get('value', ''))) > 7: e(where + ': figure value over 7 characters')
for a in arts: fig(a.get('figure'), 'article %s' % a.get('n'))
m = d.get('markets') or {}
NAMES = ['Nifty 50', 'Sensex', 'Nikkei 225', 'Hang Seng', 'Shanghai', 'FTSE 100', 'DAX', 'S&P 500', 'Nasdaq', 'Dow Jones']
ix = m.get('indexes', [])
if [x.get('name') for x in ix] != NAMES: e('markets.indexes must be exactly, in order: ' + ', '.join(NAMES))
for x in ix:
    c = x.get('change')
    if c is not None and not isinstance(c, (int, float)): e('markets: change for %s must be a number or null' % x.get('name'))
    if not x.get('close') or not x.get('why'): e('markets: %s needs close and why' % x.get('name'))
if len(m.get('extras', [])) != 3: e('markets.extras needs Gold, Brent crude, USD/INR')
for k in ['asof', 'title', 'summary', 'body', 'calendar', 'sources']:
    if not m.get(k): e('markets: missing ' + k)
l = d.get('learn') or {}
st = l.get('steps', [])
if len(st) != 5: e('learn needs 5 steps')
for s in st:
    if not 3 <= len(s.get('diagram', [])) <= 5: e('learn step %s: diagram needs 3 to 5 boxes' % s.get('n'))
b = d.get('build') or {}
for k in ['selling', 'distribution', 'gaps']:
    if k not in b: e('build: missing ' + k)
    else: fig(b[k].get('figure'), 'build.' + k)
print('OK' if not errs else 'ERRORS:\n- ' + '\n- '.join(errs))
sys.exit(1 if errs else 0)
