#!/usr/bin/env python3
"""Assemble the Prospective Student Experience deep-dive from the 8 journey-stage
profiles. Cross-stage synthesis written here; profiles formatted in.
Run: python3 analysis/improvements/assemble_prospective_report.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
profs = json.loads((ROOT / 'analysis/prospective-experience-profiles.json').read_text())
SEV = {'high': 3, 'medium': 2, 'low': 1}
profs.sort(key=lambda p: -SEV.get(p['severity'], 0))

EXEC = """# The Prospective Student Experience — Deep-Dive

*The applicant journey across the University's public web estate — discover → compare → check eligibility & cost → apply → offer → accept → enrol — traced through the path-level link graph. Focus: prospective/future students, the audience `study.unimelb.edu.au` (4,048 pages) is built to convert. June 2026.*

---

## Executive summary

The prospective estate is large, content-rich and, in places, genuinely good — tuition is per-course, the persuasion layer is wired to the practical funnel, and `study.unimelb` is unambiguously the canonical owner. But read end-to-end, the applicant journey has one defining flaw: **it never closes the loop on its own site.** At every decisive moment the journey hands off — to the **Handbook** for what a degree actually contains, to a **CRM form** that captures a *lead* rather than starting an application, or to a **walled portal** (VTAC, eStudent eApplications) where the real action happens out of view. The site that exists to *convert* prospective students is structurally unable to take them from "interested" to "applied" without ejecting them into a different platform, a different standard, or a different system.

Three faults compound this. **Comparison — the single most important prospective task — does not exist:** 427 courses are rendered as isolated 7-tab micro-sites with no shortlist or compare, so a student weighing three degrees juggles 21 browser tabs by hand. **The "Apply" action is fragmented across at least three disconnected systems** (VTAC for domestic undergraduates, eStudent for graduate/international, a CRM enquiry form everywhere) with no single "Apply" path and the loudest button collecting an email address. And **the apply→enrol handoff is a single cold cross-domain link** — only domestic VTAC undergraduates get a guided "you got in, here's what's next"; everyone else falls off the prospective site into the current-student estate with no transition.

The prize is conversion and continuity: make the catalogue comparable, make "Apply" one owned path, pull the decision-critical Handbook detail into the course view, and build the offer→enrol bridge the funnel is missing.
"""

PATTERNS = """## The recurring patterns across the journey

**1. The journey never closes the loop on-site.** Every stage funnels OUT — to the Handbook (course/subject detail, 4,391 links), to `forms.your` (1,493 CRM "Register for updates" leads), or to a walled application portal. Discovery, eligibility and apply all terminate in a system the prospect can't evaluate from the catalogue. *(course discovery, how-to-apply, eligibility, international)*

**2. "Apply" is not one path.** The most decisive action forks silently by audience across VTAC (external government admissions, domestic UG), the eStudent eApplications portal (graduate/international), and the CRM enquiry form — the applicant must self-diagnose which applies. There is no single owned "Apply" path. *(how-to-apply, international)*

**3. Comparison — the core prospective task — is absent.** 427 courses as isolated 7-tab micro-sites (landing + structure + entry + fees + how-to-apply + outcomes + experience), a keyword-only Funnelback search, no shortlist/compare. Decision-critical attributes are split across seven tabs and two platforms. *(course discovery)*

**4. Decision-critical detail lives on a different platform.** What a degree actually contains (subjects, electives, prerequisites) is on the Handbook — a different platform, visual standard and academic register — so the prospect is ejected mid-decision. 88% of the 4,483 Handbook deep-links come from just 153 `/structure/` pages. *(course discovery, eligibility)*

**5. Cost and eligibility are present but not self-serviceable.** Tuition is per-course (good), but the wider affordability story (loans, cost-of-living, scholarships) is scattered and audience-split, and eligibility rarely resolves to a yes/no — the authoritative requirements deep-link the Handbook again. *(fees/cost, eligibility)*

**6. Faculty and multi-owner duplication.** 817 faculty-hosted `/study/` pages parallel the central catalogue, and faculties push prospective traffic back the other way (medicine→study 604, education→study 545) — multiple owners describing the same courses, with the central catalogue the only place a course is fully described and transacted. *(central-vs-faculty)*

**7. A performance tax at the top of funnel.** `study.unimelb` is the heaviest estate (median 304 KB, max 1.1 MB) — the decision pages are the slowest to load, on the audience most likely to be on mobile or limited data. *(decision/persuasion)*
"""

ESTATE = """## The prospective estate at a glance

| | |
|---|--:|
| `study.unimelb.edu.au` total pages | 4,048 |
| Course catalogue (`/find/courses`) | 2,944 (73%) |
| Distinct courses behind it | ~427 (rendered as 7-tab micro-sites) |
| Application journey (`/how-to-apply`) | 280 (segmented by audience) |
| Persuasion (`/study-with-us` + `/student-life`) | 274 |
| Links OUT to the Handbook (course detail) | 4,391 |
| Links OUT to the CRM funnel (`forms.your`) | 1,493 |
| Links to scholarships discovery | 411 |
| Apply→enrol handoff (study → students.unimelb) | **373 (thin)** |
| Faculty-hosted `/study/` pages (parallel funnel) | 817 across 14 faculties |
| Page weight (median / max) | 304 KB / 1.1 MB (heaviest estate) |
"""

def fmt(p):
    out = [f"## {p['stage']}  `[{p['severity'].upper()}]`", f"**{p['headline']}**", "",
           f"**What exists.** {p['what_exists']}", ""]
    if p.get('journey_friction'):
        out.append("**Journey friction**\n")
        out += [f"- {x}" for x in p['journey_friction']]
        out.append("")
    if p.get('fragmentation'):
        out.append("**Fragmentation**\n")
        out += [f"- {x}" for x in p['fragmentation']]
        out.append("")
    out.append(f"**The seam.** {p['the_seam']}")
    out.append("")
    out.append(f"**Recommendation.** {p['recommendation']}")
    return "\n".join(out)

RECS = """## What to do — conversion and continuity

The prospective estate doesn't need rebuilding; it needs the loop closed. Six moves, in priority order:

1. **Build compare.** Add a persistent shortlist/compare across the 427 courses surfacing fees, entry, duration, intake and a subject snapshot on one card — so comparison stops being manual tab-juggling. *(highest-traffic, highest-stakes stage)*
2. **Make "Apply" one owned path.** A single "Apply" entry that routes by audience to the right system (VTAC / eStudent / research) behind one consistent button, and visually separates "Apply" from "Enquire" so the loudest button starts an application, not a lead.
3. **Pull Handbook detail into the course view.** Embed or surface course structure / subject list / entry requirements inside the `study.unimelb` course pages; reserve the deep Handbook link for full academic reference — stop ejecting the prospect to a different-standard platform mid-decision.
4. **Make eligibility and cost self-serviceable.** A yes/no-leaning eligibility view per course and a complete per-course affordability picture (tuition + loans + cost-of-living + relevant scholarships) on the course card, not scattered across audience-split pages.
5. **Build the offer→enrol bridge.** A guided "you got in — here's what's next" path for ALL accepted students (not just domestic VTAC UG) that carries them across the thin study→students seam into the current-student estate.
6. **Rationalise faculty duplication and the funnel weight.** One canonical course record (collapse the 817 faculty `/study/` parallels to links), and a page-weight budget on the heaviest-in-the-University decision pages.

**The through-line with the current-student findings:** the same estate-wide faults — content owned centrally but the *action* behind a wall, the same thing authored on faculty sites, decision-critical detail on a different platform — shape *both* ends of the lifecycle. The prospective fix is the same shape as the current-student fix: connect the seams, name the canonical owner, and stop the journey ejecting into systems the user can't see.

---

*Source: per-stage link-graph profiles in `analysis/prospective-experience-profiles.json`; estate evidence in `analysis/full-scrape/prospective_estate.py`, `prospective-estate-SUMMARY.md`, `prospective-sections.csv`. The application portals (VTAC, eStudent eApplications, my.unimelb) are behind walls and uncrawled — claims about them are inferred from outbound links.*
"""

doc = "\n\n".join([EXEC, ESTATE, PATTERNS, "## Per-stage deep-dives\n"] + [fmt(p) for p in profs] + [RECS])
(ROOT / 'analysis/prospective-student-experience.md').write_text(doc)
print(f"wrote analysis/prospective-student-experience.md ({len(doc):,} chars, {len(profs)} stages)")
