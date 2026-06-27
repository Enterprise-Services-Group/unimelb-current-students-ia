#!/usr/bin/env python3
"""Emit report/research-report/improvements.js — the cleaned, track-assigned
improvement data the HTML report renders into cards + detail modals.

- track from category: experience (ux/service/content) vs technical (technical/governance)
- theme label from the audit dimension
- text cleaned of all prior-context cross-references (round-1/deck/corrected/etc.)
  so the report reads standalone on first read
Run: python3 analysis/improvements/prep_improvements.py
"""
import json, re, collections
from pathlib import Path

D = Path(__file__).resolve().parent
raw = [i for i in json.loads((D / '_round1-improvements.json').read_text())
       + json.loads((D / '_round2-improvements.json').read_text())
       if i.get('title', '').strip() not in ('t', 'test')
       and not i.get('title', '').lower().startswith('correct round-1')]

TRACK = {'ux': 'experience', 'service': 'experience', 'content': 'experience',
         'technical': 'technical', 'governance': 'technical'}

def theme_of(i):
    """Clean, track-specific buckets (no theme name appears in both tracks)."""
    cat, dim = i['category'], i.get('dimension', '')
    if cat == 'ux':
        return 'Information architecture & navigation'
    if cat == 'service':
        return 'Service design & lifecycle seams'
    if cat == 'content':
        return 'Content quality & connections'
    if cat == 'governance':
        return 'Governance, standards & platform'
    if dim == 'performance-mobile':
        return 'Performance & page weight'
    if dim == 'accessibility-tech':
        return 'Accessibility & front-end markup'
    return 'Link integrity, redirects & metadata'

# strip prior-context cross-references so the report stands alone on first read
SUBS = [
    (r'\bround[\s-]?1\b', ''), (r'\bround[\s-]?2\b', ''),
    (r"\bthe deck'?s?\b", 'earlier reporting'),
    (r'\bthe analyst’?s?\b', 'the'), (r"\bthe analyst'?s?\b", 'the'),
    (r'\bpreviously (asserted|assumed|claimed|stated)\b', ''),
    (r'\bcorrect(ed|ion|s)?\b', ''), (r'\bphantom\b', 'spurious'),
    (r'\bnot the "?74"?\b', ''), (r'\bvs the "?74"?\b', ''),
    (r'\bextends?\b(?=[^.]*\bfinding\b)', 'complements'),
    (r'\bfinding\s+\d+(\.\d+)?\b', 'a related fix'),
    (r'\(was [^)]*\)', ''), (r'\bre-?verif(y|ied|ication)\b', 'check'),
]

def clean(t):
    if not t:
        return ''
    for pat, rep in SUBS:
        t = re.sub(pat, rep, t, flags=re.I)
    t = re.sub(r'\s{2,}', ' ', t)
    t = re.sub(r'\s+([,.;:])', r'\1', t)
    t = re.sub(r'\(\s*[;,]?\s*\)', '', t)            # empty parens left by subs
    t = re.sub(r'\s{2,}', ' ', t).strip(' ;,')
    return t

out = []
for n, i in enumerate(raw, 1):
    out.append({
        'id': f'imp{n:02d}',
        'track': TRACK.get(i['category'], 'technical'),
        'theme': theme_of(i),
        'category': i['category'],
        'severity': i['severity'],
        'effort': i['effort'],
        'title': clean(i['title']),
        'evidence': clean(i['evidence']),
        'recommendation': clean(i['recommendation']),
    })

js = 'window.IMPROVEMENTS = ' + json.dumps(out, ensure_ascii=False, indent=1) + ';\n'
(D.parent.parent / 'report/research-report/improvements.js').write_text(js)
print(f"wrote report/research-report/improvements.js  ({len(out)} improvements)")
print("track split:", dict(collections.Counter(x['track'] for x in out)))
print("experience themes:", dict(collections.Counter(x['theme'] for x in out if x['track'] == 'experience')))
print("technical themes:", dict(collections.Counter(x['theme'] for x in out if x['track'] == 'technical')))
# leak check: any residual cross-reference words?
blob = json.dumps(out).lower()
for w in ['round-1', 'round 1', 'the deck', 'corrected', 'phantom']:
    if w in blob:
        print(f"  ⚠ residual '{w}' present")
