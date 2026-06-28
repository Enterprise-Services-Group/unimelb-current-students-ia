#!/usr/bin/env python3
"""Reproduce the analyst's a11y audit claims over raw crawl HTML."""
import json, glob, os, re, collections, sys
from html.parser import HTMLParser

ROOT = '/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia/crawl'
DOMAINS = {
  'finearts-music': 'finearts-music-unimelb-edu-au',
  'study': 'study-unimelb-edu-au',
  'mbs': 'mbs-unimelb-edu-au',
  'scholarships': 'scholarships-unimelb-edu-au',
  'law': 'law-unimelb-edu-au',
  'fbe': 'fbe-unimelb-edu-au',
  'services': 'services-unimelb-edu-au',
  'mdhs': 'mdhs-unimelb-edu-au',
  'msd': 'msd-unimelb-edu-au',
  'students': 'students-full',
  'arts': 'arts-unimelb-edu-au',
  'alumni': 'www-unimelb-edu-au-alumni',
  'handbook': 'handbook-unimelb-edu-au',
}

INCAPSULA = 'Request unsuccessful'

def is_shell(html):
    return INCAPSULA in html or len(html) < 1500

class HExtract(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings = []   # (level, text)
        self._cur = None
        self._buf = []
        self.title = None
        self._in_title = False
        self.imgs = []       # list of dict(has_alt, alt_empty)
        self.target_blank = 0
        self.target_blank_no_rel = 0
        self.has_lang = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html':
            if a.get('lang'): self.has_lang = True
        if tag in ('h1','h2','h3','h4','h5','h6'):
            self._cur = int(tag[1]); self._buf=[]
        if tag == 'title':
            self._in_title = True; self._buf=[]
        if tag == 'img':
            self.imgs.append({'has_alt':'alt' in a, 'alt_empty': a.get('alt','')=='' if 'alt' in a else False})
        if tag == 'a':
            if a.get('target') == '_blank':
                self.target_blank += 1
                rel = (a.get('rel') or '').lower()
                if 'noopener' not in rel and 'noreferrer' not in rel:
                    self.target_blank_no_rel += 1
    def handle_endtag(self, tag):
        if tag in ('h1','h2','h3','h4','h5','h6') and self._cur:
            txt = ''.join(self._buf).strip()
            self.headings.append((self._cur, txt)); self._cur=None
        if tag == 'title':
            self.title = ''.join(self._buf).strip(); self._in_title=False
    def handle_data(self, d):
        if self._cur or self._in_title:
            self._buf.append(d)

def first_skip(headings):
    """Return (skipped_bool, jump_str) for first heading-level skip going down."""
    prev = None
    for lvl, txt in headings:
        if prev is not None and lvl > prev + 1:
            return True, f"h{prev}->h{lvl}"
        prev = lvl
    return False, None

def parse_page(html):
    p = HExtract()
    try:
        p.feed(html)
    except Exception:
        pass
    return p

def iter_rendered(dirn, limit=None):
    metas = sorted(glob.glob(f'{ROOT}/{dirn}/pages/*/meta.json'))
    out = []
    for m in metas:
        pd = os.path.dirname(m)
        hp = os.path.join(pd, 'page.html')
        if not os.path.exists(hp): continue
        try:
            html = open(hp, encoding='utf-8', errors='replace').read()
        except: continue
        if is_shell(html): continue
        out.append((m, hp, html))
    if limit and len(out) > limit:
        step = len(out)/limit
        out = [out[int(i*step)] for i in range(limit)]
    return out

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv)>1 else 'all'
    print(f"MODE={mode}")
