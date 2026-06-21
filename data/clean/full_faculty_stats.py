#!/usr/bin/env python3
"""Full-faculty-context statistics.

Regenerates every figure cited in analysis/full-faculty-context.md from the
full-domain crawls in crawl/full-faculty/*.json. The original audit crawled
only the current-students *slice* of each domain (crawl/pages/*.json); these
crawls captured the whole faculty marketing domain, giving the denominator the
slice never had.

Deterministic: same inputs -> identical output. Run:
    python3 data/clean/full_faculty_stats.py
"""
import json
import glob
import re
import collections
import statistics
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
STUD = re.compile(r'/(current-students|students|student-)', re.I)


def load_full():
    """slug -> list[page]; skip the empty feit/ffam shells (pages_crawled < 5)."""
    out = {}
    for f in sorted(glob.glob(str(ROOT / 'crawl/full-faculty/*.json'))):
        if f.endswith('_summary.json'):
            continue
        d = json.load(open(f))
        if not isinstance(d, dict) or 'pages' not in d or d.get('pages_crawled', 0) < 5:
            continue
        out[d['slug']] = d['pages']
    return out


def first_seg(u):
    p = urlparse(u).path.strip('/').split('/')
    return p[0].lower() if p and p[0] else '(root)'


def norm_title(t):
    t = re.sub(r'\s*[|\-–—]\s*(the )?university of melbourne.*$', '', t, flags=re.I)
    t = re.sub(r'\s*[|\-–—].*$', '', t)
    return re.sub(r'[^a-z0-9 ]', '', t.lower()).strip()


def main():
    full = load_full()
    allpages = [(slug, p) for slug, ps in full.items() for p in ps]
    print(f"Full faculty crawl: {len(full)} domains, {len(allpages)} pages\n")

    # (1) Burial: current-students footprint as a share of the full domain.
    print("== current-students footprint on faculty marketing domain (/students/ path) ==")
    tot = stud = 0
    for slug, ps in sorted(full.items()):
        cur = sum(1 for p in ps if STUD.search(urlparse(p['url']).path))
        tot += len(ps)
        stud += cur
        print(f"  {slug:16} {cur:3}/{len(ps):3} = {100*cur/len(ps):4.1f}%")
    print(f"  {'ALL':16} {stud:3}/{tot:3} = {100*stud/tot:4.1f}%\n")

    # (2) No shared IA: dominant top-level section per domain.
    print("== top section per domain (largest first-path-segment) ==")
    for slug, ps in sorted(full.items()):
        segs = collections.Counter(first_seg(p['url']) for p in ps)
        s, c = segs.most_common(1)[0]
        print(f"  {slug:16} /{s}/ = {c}/{len(ps)} ({100*c/len(ps):.0f}%)  | top6: "
              + ', '.join(f'{x}:{n}' for x, n in segs.most_common(6)))
    print()

    # (3) Parallel reinvention: identical normalized title across >=3 domains.
    print("== parallel reinvention (same page title on >=3 domains) ==")
    concept = collections.defaultdict(set)
    example = {}
    for slug, ps in full.items():
        for p in ps:
            n = norm_title(p['title'])
            if 2 <= len(n) <= 40:
                concept[n].add(slug)
                example.setdefault(n, p['title'])
    for n, fs in sorted(((n, fs) for n, fs in concept.items() if len(fs) >= 3),
                        key=lambda x: -len(x[1]))[:15]:
        print(f"  {len(fs)}x  \"{example[n]}\"  {sorted(fs)}")
    print()

    # (4) Fingerprint dedup — the null result.
    fp = collections.defaultdict(set)
    for slug, ps in full.items():
        for p in ps:
            fp[p['fingerprint']].add(slug)
    cross = sum(1 for v in fp.values() if len(v) > 1)
    print(f"== fingerprint collisions across domains: {cross} "
          f"(0 expected — hash is per-page unique, near-dup needs title/shingle) ==\n")

    # (5) Thin content across the estate.
    print("== thin content (<160 words) ==")
    wc = [p['wordCount'] for _, p in allpages]
    thin = sum(1 for w in wc if w < 160)
    print(f"  estate: {thin}/{len(wc)} = {100*thin/len(wc):.0f}% thin | median wc={int(statistics.median(wc))}")
    for slug, ps in sorted(full.items()):
        t = sum(1 for p in ps if p['wordCount'] < 160)
        print(f"  {slug:16} {t:3}/{len(ps):3} = {100*t/len(ps):4.1f}%")

    # cheap self-check: the headline denominator must hold
    assert tot == sum(len(ps) for ps in full.values())
    assert 0 <= stud <= tot
    assert cross == 0, "fingerprint collisions appeared — revisit the null-result claim"


if __name__ == '__main__':
    main()
