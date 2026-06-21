#!/usr/bin/env python3
"""Cross-corpus lifecycle analysis.

Joins the four corpora — prospective (study.unimelb), current-students
(faculty + students.unimelb), faculty full domains, and alumni — to surface
connections across the end-to-end student lifecycle that no single-corpus view
can see. Substrates:
  * data/clean/pages-clean.csv  (1,569 topic-tagged, corpus-labelled pages)
  * crawl/pages/{study-unimelb,alumni-unimelb}.json  (parentFaculty mapping)
  * crawl/full-faculty/*.json   (full faculty sites incl. research/news/about)

Deterministic. Run: python3 data/clean/cross_corpus_lifecycle.py
"""
import csv
import json
import glob
import re
import collections
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]


def H(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)


def tags(r):
    return [t.strip() for t in re.split(r'[;,|]', r['topicTags']) if t.strip() and t.strip() != '<untagged>']


# ---- load substrates -------------------------------------------------------
rows = list(csv.DictReader(open(ROOT / 'data/clean/pages-clean.csv')))
by_corpus = collections.defaultdict(list)
for r in rows:
    by_corpus[r['corpus']].append(r)

def load_raw(name):
    d = json.load(open(ROOT / f'crawl/pages/{name}.json'))
    return d if isinstance(d, list) else d.get('pages', [])

alumni_raw = load_raw('alumni-unimelb')
study_raw = load_raw('study-unimelb')

FULL = {}
for f in sorted(glob.glob(str(ROOT / 'crawl/full-faculty/*.json'))):
    if f.endswith('_summary.json'):
        continue
    d = json.load(open(f))
    if isinstance(d, dict) and d.get('pages_crawled', 0) >= 5:
        FULL[d['slug']] = d['pages']

print(f"corpora: current={len(by_corpus['current-students'])} study={len(by_corpus['study'])} "
      f"alumni={len(by_corpus['alumni'])} | full-faculty={sum(len(v) for v in FULL.values())} ({len(FULL)} domains)")

# ===========================================================================
H("LENS 1 — Topic x lifecycle-stage matrix (which topics span the journey)")
# stage = prospective (study) | current | alumni
topic_stage = collections.defaultdict(lambda: collections.Counter())
for r in rows:
    stage = {'study': 'prospective', 'current-students': 'current', 'alumni': 'alumni'}[r['corpus']]
    for t in tags(r):
        # fold the study-* prospective vocabulary onto its lifecycle concept
        base = (t.replace('study-course-info', 'course-info')
                 .replace('study-how-to-apply', 'apply')
                 .replace('study-campus-life', 'student-life')
                 .replace('study-international', 'international')
                 .replace('study-scholarships', 'scholarships'))
        topic_stage[base][stage] += 1
print(f"{'topic':26} {'prospective':>11} {'current':>8} {'alumni':>7}  spans")
for t, c in sorted(topic_stage.items(), key=lambda kv: -sum(kv[1].values())):
    stages = [s for s in ('prospective', 'current', 'alumni') if c[s]]
    if sum(c.values()) < 8:
        continue
    flag = '  <<< all 3 stages' if len(stages) == 3 else ('  << 2 stages' if len(stages) == 2 else '')
    print(f"{t:26} {c['prospective']:>11} {c['current']:>8} {c['alumni']:>7}{flag}")

# ===========================================================================
H("LENS 2 — CAREERS across the whole lifecycle (the headline thread)")
def has(r, *needles):
    blob = (r['url'] + ' ' + r['title'] + ' ' + r['topicTags']).lower()
    return any(n in blob for n in needles)
career_by_stage = collections.Counter()
career_fac = collections.defaultdict(lambda: collections.Counter())
for r in rows:
    if 'careers-employability' in tags(r) or has(r, 'career', 'employab', 'mentor', 'internship'):
        stage = {'study': 'prospective', 'current-students': 'current', 'alumni': 'alumni'}[r['corpus']]
        career_by_stage[stage] += 1
        career_fac[r['faculty']][stage] += 1
print("careers/employability/mentoring pages by lifecycle stage:")
for s in ('prospective', 'current', 'alumni'):
    print(f"  {s:12} {career_by_stage[s]}")
print("\nfaculties running their own careers content (current stage), top:")
for fac, c in sorted(career_fac.items(), key=lambda kv: -kv[1]['current'])[:8]:
    print(f"  {fac:12} current={c['current']:3} prospective={c['prospective']:3} alumni={c['alumni']:3}")
# faculty /alumni/ + /careers/ presence in FULL crawl
print("\nfaculty full-domain pages mentioning careers/mentoring/alumni in URL:")
for slug, ps in sorted(FULL.items()):
    car = sum(1 for p in ps if re.search(r'/(career|employab|mentor|alumni)', urlparse(p['url']).path, re.I))
    print(f"  {slug:16} {car}")

# ===========================================================================
H("LENS 3 — SCHOLARSHIPS prospective vs current (where the catalogue splits)")
sch = collections.defaultdict(lambda: collections.Counter())
for r in rows:
    if any('scholarship' in t for t in tags(r)) or has(r, 'scholarship', 'bursary', 'grant'):
        stage = {'study': 'prospective', 'current-students': 'current', 'alumni': 'alumni'}[r['corpus']]
        sch[r['faculty']][stage] += 1
tot = collections.Counter()
for fac, c in sch.items():
    tot.update(c)
print(f"scholarship pages: prospective={tot['prospective']} current={tot['current']} alumni={tot['alumni']}")
for fac, c in sorted(sch.items(), key=lambda kv: -sum(kv[1].values()))[:8]:
    print(f"  {fac:12} prospective={c['prospective']:3} current={c['current']:3}")

# ===========================================================================
H("LENS 4 — RESEARCH domain thread: prospective PhD -> HDR candidate -> faculty research")
# current HDR candidature
hdr = [r for r in rows if 'research-candidature' in tags(r)]
print(f"current research-candidature (HDR) pages: {len(hdr)}")
print("  by faculty:", dict(collections.Counter(r['faculty'] for r in hdr).most_common(8)))
# faculty /research/ estate from FULL crawl
print("\nfaculty /research/ section size (full domain) vs HDR-candidature support (current):")
hdr_fac = collections.Counter(r['faculty'] for r in hdr)
slug2fac = {'law': 'Law', 'eng': 'FEIT', 'arts': 'Arts', 'science': 'Science',
            'education': 'Education', 'fbe': 'FBE', 'finearts-music': 'FFAM',
            'mdhs': 'MDHS', 'msd': 'ABP'}
for slug, ps in sorted(FULL.items()):
    research = sum(1 for p in ps if re.search(r'/research', urlparse(p['url']).path, re.I))
    fac = slug2fac.get(slug, slug)
    print(f"  {slug:16} faculty /research/ = {research:3}   |   current HDR support = {hdr_fac.get(fac,0):3}")
# study research-degree pages
study_research = [r for r in by_corpus['study'] if has(r, 'research', 'phd', 'doctora', 'graduate-research', 'masters by research')]
print(f"\nprospective research-degree pages on study.unimelb: {len(study_research)}")

# ===========================================================================
H("LENS 5 — ALUMNI -> FACULTY (the graduation handoff)")
print(f"central alumni corpus: {len(by_corpus['alumni'])} pages on www.unimelb.edu.au")
# alumni topics
atags = collections.Counter()
for r in by_corpus['alumni']:
    for t in tags(r):
        atags[t] += 1
print("  alumni page topics:", dict(atags.most_common(10)))
# alumni parentFaculty distribution (faculty-specific alumni content centrally)
apf = collections.Counter((p.get('parentFaculty') or p.get('faculty') or 'central') for p in alumni_raw)
print("  alumni pages by parentFaculty (central corpus):", dict(apf.most_common()))
# every faculty also runs /alumni/ (from cdp probe + full crawl)
cdp = json.load(open(ROOT / 'crawl/faculty_alumni_cdp.json'))
print(f"\n  faculties with their OWN /alumni section (probed): {len(cdp)}/9")
for slug, ps in sorted(FULL.items()):
    al = [p for p in ps if '/alumni' in urlparse(p['url']).path.lower()]
    if al:
        print(f"    {slug:16} {len(al):2} alumni pages on faculty domain  e.g. {al[0]['title'][:45]!r}")

# ===========================================================================
H("LENS 6 — STUDY (prospective) vs faculty/current (the apply->enrol handoff)")
print(f"central prospective corpus: {len(by_corpus['study'])} pages on study.unimelb.edu.au")
spf = collections.Counter((p.get('parentFaculty') or p.get('faculty') or 'cross') for p in study_raw)
print("  study.unimelb pages by parentFaculty:", dict(spf.most_common()))
# faculty /study/ on their own domain (prospective content faculties ALSO host)
print("\n  faculty /study/ (prospective) on own domain vs central study.unimelb coverage:")
for slug, ps in sorted(FULL.items()):
    st = sum(1 for p in ps if re.search(r'/study', urlparse(p['url']).path, re.I))
    print(f"    {slug:16} faculty /study/ = {st:3}")

# ===========================================================================
H("LENS 7 — IA across the lifecycle (one journey, four architectures)")
print("host that owns each lifecycle stage:")
stage_host = {'prospective': 'study.unimelb.edu.au', 'current (central)': 'students.unimelb.edu.au',
              'current (faculty)': '{faculty}.unimelb.edu.au', 'alumni': 'www.unimelb.edu.au/alumni'}
for s, h in stage_host.items():
    print(f"  {s:20} {h}")
print("\nmedian depth + URL first-segment vocabulary per corpus:")
for corpus in ('study', 'current-students', 'alumni'):
    rs = by_corpus[corpus]
    depths = sorted(int(r['depth']) for r in rs if r['depth'].isdigit())
    med = depths[len(depths)//2] if depths else 0
    segs = collections.Counter()
    for r in rs:
        p = urlparse(r['url']).path.strip('/').split('/')
        segs[p[0].lower() if p and p[0] else '(root)'] += 1
    print(f"  {corpus:16} n={len(rs):4} med-depth={med}  top-segs: "
          + ', '.join(f'{s}:{c}' for s, c in segs.most_common(5)))

# ===========================================================================
H("LENS 8 — Full faculty estate composition (research/news/about vs student)")
print(f"{'faculty':16} {'pages':>5} {'research':>8} {'news':>6} {'about':>6} {'study':>6} {'students':>8} {'engage':>7}")
agg = collections.Counter()
for slug, ps in sorted(FULL.items()):
    sec = collections.Counter()
    for p in ps:
        seg = urlparse(p['url']).path.strip('/').split('/')
        s = seg[0].lower() if seg and seg[0] else '(root)'
        sec[s] += 1
    def g(*ks): return sum(sec.get(k, 0) for k in ks)
    research = sum(c for s, c in sec.items() if 'research' in s)
    news = sum(c for s, c in sec.items() if 'news' in s)
    about = sum(c for s, c in sec.items() if 'about' in s)
    study = sum(c for s, c in sec.items() if s.startswith('study'))
    students = sum(c for s, c in sec.items() if s in ('students', 'current-students', 'student'))
    engage = sum(c for s, c in sec.items() if 'engage' in s or s == 'industry')
    agg['research'] += research; agg['news'] += news; agg['about'] += about
    agg['study'] += study; agg['students'] += students; agg['total'] += len(ps)
    print(f"  {slug:14} {len(ps):>5} {research:>8} {news:>6} {about:>6} {study:>6} {students:>8} {engage:>7}")
print(f"\n  ESTATE: research={agg['research']} news={agg['news']} about={agg['about']} "
      f"study={agg['study']} students={agg['students']} / {agg['total']} total")
print(f"  research is {100*agg['research']/agg['total']:.0f}% of faculty estate vs students {100*agg['students']/agg['total']:.0f}%")

# self-check
assert len(rows) == len(by_corpus['current-students']) + len(by_corpus['study']) + len(by_corpus['alumni'])
