#!/usr/bin/env python3
"""Assemble the final improvements register from round-1 + round-2 outputs.

The round-2 merge agent went off-task (it finished a crawl instead), so the
merge is done here deterministically: strip round-1's code-fence wrapper,
insert a Scope & confidence section, append the round-2 gap sections
(Performance & Mobile; High-stakes Journeys; near-dup + freshness), and patch
the stubbed freshness/ownership dimension by hand from the evidence pack.

Run: python3 analysis/improvements/assemble_register.py
"""
import json
from pathlib import Path

D = Path(__file__).resolve().parent
r1 = (D / '_round1-register.md').read_text().splitlines()
# round-1 clean markdown is between the ```markdown fence (line 7) and trailing ``` (line 295)
start = next(i for i, l in enumerate(r1) if l.startswith('# UoM'))
end = len(r1) - 1
while not r1[end].strip().startswith('# ') and '```' not in r1[end] and end > start:
    end -= 1
# find the closing fence
fence = next((i for i in range(len(r1) - 1, start, -1) if r1[i].strip().startswith('```')), len(r1))
base = '\n'.join(r1[start:fence]).rstrip()

imps = json.loads((D / '_round2-improvements.json').read_text())
by_dim = {}
for i in imps:
    by_dim.setdefault(i['dimension'], []).append(i)

def fmt(items, drop_titles=()):
    out = []
    for i in items:
        if any(t in i['title'] for t in drop_titles):
            continue
        if i['title'].strip() in ('t', 'test'):
            continue
        tag = f"`[{i['severity'].upper()} · {i['effort']}]`"
        out.append(f"### {i['title']} {tag}\n*Evidence:* {i['evidence']}\n\n**Do:** {i['recommendation']}")
    return '\n\n'.join(out)

SCOPE = """## Scope, confidence & what is NOT yet verified

This register is grounded in the **public** estate scrape (21,250 content pages, 20 domains, the path-level link graph). Five honesty boundaries a reviewer must carry forward before any item ships:

1. **The authenticated core is uncrawlable.** `my.unimelb` (SIS: enrolment, results, fees, timetable), Canvas/LMS, and the ~18 `*.app`/`forms.your` microsites sit behind login and appear only as outbound destinations. Every "wire X to my.unimelb / Careers Online / a form" recommendation is inferred from the public side — confirm the logged-in flow doesn't already do it (request screenshots / a walkthrough).
2. **All 404 / redirect / "phantom-404" claims are URL-string inference, not live HTTP.** Nothing in this project issued an HTTP request. The `?a=` artifact (2.3), the dead-link sweep (2.4), the www-vs-bare pairs (5.4) and the parallel-tree leaves (1.1) need **HEAD-probe confirmation** of real status codes before remediation is scoped.
3. **Findings are structural-evidence-only, not CX-validated** (carries `data-and-synthesis-issues.md` D6). The "add a bridge / CTA" items (3.1, 3.2, 8.x) rest on link-graph absence, not observed student failure — validate the costliest seams with real users.
4. **No analytics / traffic data.** Link-volume is the importance proxy throughout; it is not demand. The internal `in_c=` tracking params in the crawled URLs imply GA/search-log data exists — **requesting it is the single highest-value next step**, so priority can follow pages students actually hit.
5. **Two evidence notes:** near-duplicate claims are now reproducible via `analysis/full-scrape/near_dup.py` (4.x corrected below); the Handbook "14% orphaned" figure is largely an Incapsula bot-block artifact pending a JS-enabled re-crawl; and `students.unimelb` is **833 pages crawled / 679 with substantive content after de-dup** (both figures correct, different denominators — neither is the deck's "74")."""

FRESHNESS = """## 9. Content freshness & current-state ownership

*(Round-2 patch: the freshness/ownership analyst stubbed out; these are assembled from the evidence pack.)*

### Draft / sandbox content is live and indexed in production `[HIGH · quick-win]`
*Evidence:* `freshness-signals.csv` — **182 `/sandbox/`, `/draft/`, `-test`, `/uplift` URLs are live**, concentrated on arts (118). The equity-international audit found the clearest harm: a `/sandbox/2026-uplifts/student-visas` tree is fully live (812 KB "Support with student visas"), indexed, and accumulating **90 inbound links** — draft immigration-compliance content reaching students. 402 `…2`-suffixed duplicate URLs and 2,234 pages carrying ≤2023 year references compound the staleness signal.

**Do:** Block `/sandbox/`, `/draft/`, `-test` paths from indexing and external linking at the platform/robots layer; audit the 182 URLs and either promote-and-canonicalise or unpublish (start with the live student-visas draft). Add a pre-publish gate so staging trees cannot acquire production inbound links.

### Governance actions have no addressee — there is no current-state ownership map `[MEDIUM · medium]`
*Evidence:* Round-1's governance actions (5.1 registry, 5.2 template mandate, 5.5 forms registry) all say "assign an owner" but nothing documents **who runs what today** — `students.unimelb` vs the 12 faculty Squiz/Matrix instances vs the Handbook (different platform) vs the ~18 `*.app` form microsites vs scholarships/services. `analysis/service-model-matrix.md` is the only seed and isn't surfaced in the register.

**Do:** Before any "assign an owner" action, produce the as-is RACI: per domain/system — owning team, CMS/platform, publish workflow, last-reviewed date. This is the prerequisite addressee list for every governance item, and the input to the subdomain registry (5.1)."""

new_sections = '\n\n---\n\n'.join([
    "## 7. Performance & Mobile\n\n*Round-2 dimension (round 1 omitted both). Mobile **setup** is fine — viewport meta is present on 600/600 sampled pages; the problem is payload weight and render cost, which hits students on phones/limited data hardest.*\n\n" + fmt(by_dim.get('performance-mobile', [])),
    "## 8. High-stakes journeys — fees, international compliance, equity\n\n*Round-2 dimension. These are the journeys where an error costs a student money or their visa, and they were the least-covered in round 1.*\n\n### 8a. Fees, census dates & finance\n\n" + fmt(by_dim.get('fees-finance', [])) + "\n\n### 8b. International compliance & equity (incl. Indigenous)\n\n" + fmt(by_dim.get('equity-international', [])),
    "## 9b. Content quality — near-duplicate actions (now reproducible)\n\n*Round-1 findings 4.1–4.3 are now backed by `analysis/full-scrape/near_dup.py` → `near-duplicates.csv` (96 scored pairs). Verdict: all three hold; counts corrected (4.1 = 18 byte-identical Jaccard 1.0 + ~7 drifted of 33 path-tail pairs).*\n\n" + fmt(by_dim.get('reproducibility-neardup', []), drop_titles=('Correct round-1',)),
    FRESHNESS,
])

INTRO_NOTE = "\n\n> **Round-2 update.** This register now carries ~75 improvements: the round-1 set (UX/IA, findability, seams, content, governance, accessibility) plus round-2 additions — Performance & Mobile (§7), High-stakes Journeys (§8), reproducible near-duplicate actions (§9b) and content-freshness/ownership (§9). Read the Scope & confidence section first."

# splice: intro note after the first italic line; SCOPE before Top-12; new sections before Quick wins
lines = base.split('\n')
out = []
inserted_intro = inserted_scope = inserted_new = False
for ln in lines:
    if not inserted_intro and ln.startswith('*Master deliverable'):
        out.append(ln); out.append(INTRO_NOTE); inserted_intro = True; continue
    if not inserted_scope and ln.startswith('## Prioritised Top 12'):
        out.append(SCOPE); out.append('\n---\n'); inserted_scope = True
    if not inserted_new and ln.startswith('## Quick wins'):
        out.append(new_sections); out.append('\n---\n'); inserted_new = True
    out.append(ln)

final = '\n'.join(out).rstrip() + '\n'
(D.parent / 'improvements-register.md').write_text(final)
print(f"wrote analysis/improvements-register.md  ({len(final):,} chars)")
print(f"  round-2 improvements merged: {sum(len(v) for v in by_dim.values())}")
print(f"  scope inserted: {inserted_scope} | sections inserted: {inserted_new}")
