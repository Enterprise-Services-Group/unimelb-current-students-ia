#!/usr/bin/env python3
"""International student experience deep-dive — 9 journey stages (8 from the
workflow + the student-visa stage composed from the prior visa/compliance
evidence). Cross-stage synthesis written here; profiles formatted in.
Run: python3 analysis/improvements/build_international.py
"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
profs = json.loads((ROOT / 'analysis/international-experience-profiles.json').read_text())

# the student-visa stage failed the schema retry; composed from the prior evidence
# (the visa-breach moment, the international-PG persona, the forked-tree finding)
VISA = {
 "stage": "Student visa (subclass 500) & the immigration link",
 "headline": "The University correctly hands the visa APPLICATION to Home Affairs, but its own job — explaining the conditions a student must meet to KEEP the visa, and connecting them to the enrolment actions that breach them — is forked across the same three live trees and never wired to the action.",
 "what_exists": "Visa guidance lives under the forked international-student-support trees on students.unimelb — /support-and-wellbeing/international-student-support/visas (canonical), /student-support/international-student-support/visas (deprecated), and the /sandbox/2026-uplifts/student-visas draft (a live, indexed, 812KB 'Support with student visas' page). The subclass-500 conditions a student must maintain — 8202 (satisfactory course progress + full-time enrolment) and 8105 (work-hour limits) — are described, and the visa APPLICATION itself is correctly handed off to the external Department of Home Affairs (immigration.gov.au). The Genuine Student / financial-capacity requirement keys off the per-course international fee figure that (see Discover) is dual-authored on a single domestic-shared page.",
 "friction": [
   "The visa CONDITIONS (8202 progress/load, 8105 work) are described on a guidance page but never connected to the enrolment ACTIONS that breach them — a student reading 'you must stay full-time' has no in-page path to the study-load / enrolment-variation action that would keep them compliant (the find→act break, with immigration consequences).",
   "A prospect forming the visa picture during DECIDE is sent to the DEPRECATED /student-support visa tree (per the discover-stage finding), and 12 external domains link the deprecated tree — so the highest-consequence guidance a student reads may be the diverging, out-of-date fork.",
   "The University guidance ↔ Home Affairs boundary is a hard external handoff: the estate explains some conditions then points offshore, with no clear 'what the University does vs what immigration does' framing — leaving the student to reconcile two authorities under visa risk.",
   "A live /sandbox/2026-uplifts/student-visas DRAFT competes with the canonical page for the single most immigration-critical content — and one of its URLs still hits a UoM Sign-In wall."],
 "fragmentation": [
   "Three simultaneously-live visa trees (canonical 27 / deprecated 12 / sandbox draft 10) author overlapping visa-condition content; 12 domains link the deprecated one.",
   "Visa-condition content is scattered across /visas, study-load, work-rights and the family/under-18 sub-pages, with no single 'your visa conditions and how to keep them' spine.",
   "The financial-capacity input (the international fee) is itself dual-authored and can desync from the figure a visa application is built on."],
 "the_seam": "Two unclosed seams. OUTWARD: the visa application correctly leaves for Home Affairs (immigration.gov.au) — but the estate doesn't frame the University-vs-immigration boundary, so the student straddles two authorities. INWARD and worse: the KNOW→ACT seam — every visa CONDITION (full-time load, progress, work limits) is described on a students.unimelb guidance page whose only routes to the ACTION that maintains or breaches it (study-load change, enrolment variation in my.unimelb / the *.app forms) are absent on the highest-risk pages.",
 "severity": "high",
 "recommendation": "Build one canonical 'Your student visa & conditions' page that (1) connects each condition to the action that maintains it — study load → enrolment, progress → results/special consideration, work → the limit — with the action link in-page; (2) frames the University-vs-Home-Affairs boundary explicitly; (3) 301s the deprecated tree, deletes the sandbox draft, and repoints the 12 domains; and (4) governs the financial-capacity fee figure as an accuracy-critical field.",
}

ORDER = ['Discover', 'Eligibility', 'Application', 'Offer, CoE', 'Student visa', 'OSHC', 'Arrival', 'Ongoing', 'Work rights']
allp = profs + [VISA]
def rank(p):
    for i, k in enumerate(ORDER):
        if p['stage'].startswith(k): return i
    return 99
allp.sort(key=rank)

EXEC = """# The International Student Experience — Deep-Dive

*An end-to-end audit of the University's highest-stakes audience — where a web fault doesn't cost convenience, it costs a visa. Nine journey stages from discovery to post-study, traced across study.unimelb, the forked current-student support trees, and the external immigration and application systems. June 2026.*

---

## Executive summary

International students are the journey the University can least afford to get wrong, and the one where its estate-wide faults turn legally consequential. The work is, in parts, genuinely good — there is a purpose-built international decide-hub, CoE and OSHC guidance are well-written, eligibility self-serves for listed countries. But end to end, the journey has a single defining failure repeated at every compliance moment: **the estate explains the rule but never connects it to the action**, and the rules in question are the ones that keep a visa valid.

It compounds in three ways. First, **the most immigration-critical content is forked across three live, simultaneously-published trees** — a canonical `/support-and-wellbeing` tree, a deprecated `/student-support` tree that **12 domains still link**, and a live `/sandbox/2026-uplifts` *draft* — so a student forms their visa picture from whichever fork they happen to land on. Second, **the visa condition and the academic action never meet**: the full-time study-load requirement that maintains the visa is invisible at the moment of enrolment, and the highest-risk pages ("reduced study load", "enrolment changes that affect your visa") link to **zero** action forms. Third, **the biggest drawcards and the dominant channel are absent or undiscoverable**: the post-study work visa (subclass 485) — the single largest reason many international students choose Australia — has **no destination page anywhere on the estate**, and the education-agent channel most international students actually apply through is content-rich but functionally undiscoverable and duplicated across two URLs.

There is also a quiet accuracy risk under all of it: the international fee and entry figures a student builds a visa financial-capacity plan on are **dual-authored on a single domestic-shared page** (with a still-live "2025" requirements fork), so a desync feeds a wrong number into a legally-tested decision. The fix is not more content — the content largely exists — it is **closure**: one canonical international spine, every condition wired to its action, the forks retired, and the absent drawcards (485, agents) actually built.
"""

PATTERNS = """## The recurring patterns — where the estate's faults turn legal

**1. Know but can't act — at every compliance moment.** CoE, OSHC, study-load, visa conditions and work limits are all *described* on guidance pages whose route to the *action* (eStudent, my.unimelb, the `*.app` forms, the deposit flow) is missing or behind a wall. The find→act break is the estate's signature fault; here each instance carries an immigration consequence.

**2. The most critical content is forked across three live trees.** International support runs on `/support-and-wellbeing` (canonical, 27), `/student-support` (deprecated, 12) and a live `/sandbox/2026-uplifts` *draft* (10) at once — and 12 domains link the deprecated one. On the estate's highest-stakes topic, the student may read the wrong fork.

**3. The visa condition and the academic action never meet.** The full-time study-load requirement that keeps the visa valid is invisible at the enrolment moment; the academic enrolment task (my.unimelb) and the visa rule (a guidance page) are managed in different places and never connected at the point of action.

**4. The drawcards and the dominant channel are missing.** The post-study work visa (485) — the biggest reason to choose Australia — has no page at all. The education-agent channel most international students apply through is duplicated across two byte-identical URLs and has no per-country authorised-agent verification. The estate under-builds exactly where international demand concentrates.

**5. Accuracy is ungoverned on legally-tested fields.** International fees and entry are dual-authored on one domestic-shared page, with a still-live "2025" English-requirements fork — and these feed the subclass-500 financial-capacity and eligibility tests. A silent desync is a compliance error, not a typo.

**6. Everything decisive is off-estate.** The application (eStudent), enrolment and CoE (my.unimelb), the visa (Home Affairs) and OSHC (provider sites) all happen behind walls or offshore. The public estate is an instruction manual for systems it cannot show — so the handoffs are where the journey lives, and they are exactly what isn't governed.
"""

def fmt(p):
    out = [f"## {p['stage']}  `[{p['severity'].upper()}]`", f"**{p['headline']}**", "",
           f"**What exists.** {p['what_exists']}", "", "**Friction (immigration/compliance consequences flagged)**", ""]
    out += [f"- {x}" for x in p.get('friction', [])]
    if p.get('fragmentation'):
        out += ["", "**Fragmentation**", ""] + [f"- {x}" for x in p['fragmentation']]
    out += ["", f"**The seam.** {p['the_seam']}", "", f"**Recommendation.** {p['recommendation']}"]
    return "\n".join(out)

CONS = """## Consolidation — close the loop on the highest-stakes journey

1. **One canonical 'International students' spine** that owns the sequence discover → eligibility → apply → CoE → visa → OSHC → arrive → comply → work/post-study; retire the deprecated `/student-support` tree and the `/sandbox` draft, and repoint the 12 domains.
2. **Wire every condition to its action** — study load → enrolment, progress → results/special consideration, work → the limit, OSHC → the arrange/verify step — with the action link in-page, not described-and-deferred.
3. **Build the missing drawcards** — a post-study work-visa (485) destination connected to careers, and a discoverable, per-country authorised-agent channel (de-duplicate the two agent URLs).
4. **Govern the accuracy-critical fields** — treat international fees, entry and English thresholds as compliance fields with a verified-date stamp and a desync check; retire the stale "2025" forks.
5. **Frame the University ↔ Home Affairs boundary** so a student knows what the University does and what immigration does, and isn't left straddling two authorities under visa risk.

**The through-line:** international is not a different problem from the rest of the estate — it is the same find→act, forked-tree and off-estate-action faults, with the volume turned up to legal consequence. Fixing it is the clearest case for the central-and-spoke discipline the whole report argues for.

---

*Source: 8 per-stage workflow profiles in `analysis/international-experience-profiles.json` + the student-visa stage composed from `analysis/lifecycle-traces.json` (the visa-breach moment, international-PG persona) and the forked-tree evidence. The application (eStudent), enrolment/CoE (my.unimelb), the visa (Home Affairs) and OSHC providers are behind walls / offshore — inferred from outbound links.*
"""

doc = "\n\n".join([EXEC, PATTERNS, "## The nine stages, end to end\n"] + [fmt(p) for p in allp] + [CONS])
(ROOT / 'analysis/international-student-experience.md').write_text(doc)
js = [{'subject': p['stage'], 'kind': 'stage', 'severity': p['severity'], 'headline': p['headline'],
       'what_exists': p['what_exists'], 'friction': p.get('friction', []),
       'fragmentation': p.get('fragmentation', []), 'seam': p['the_seam'], 'recommendation': p['recommendation']} for p in allp]
open(ROOT / 'report/research-report/international.js', 'w').write('window.INTERNATIONAL=' + json.dumps(js, ensure_ascii=False) + ';\n')
print(f"wrote analysis/international-student-experience.md ({len(doc):,} chars) + international.js ({len(allp)} stages)")
