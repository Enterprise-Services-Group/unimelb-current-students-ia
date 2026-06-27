#!/usr/bin/env python3
"""Assemble the Student-Services Fragmentation deep-dive report from the 14
per-service profiles (the workflow's synthesis agent went off-task, so the
cross-service synthesis is written here and the profiles are formatted in).

Run: python3 analysis/improvements/assemble_services_report.py
"""
import json, csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
profs = json.loads((ROOT / 'analysis/student-services-profiles.json').read_text())
frag = {r['service']: r for r in csv.DictReader(open(ROOT / 'analysis/full-scrape/service-fragmentation.csv'))}

SEV = {'high': 3, 'medium': 2, 'low': 1}
profs.sort(key=lambda p: (-SEV.get(p['severity'], 0), -int(frag.get(p['service'], {}).get('frag_score', 0))))

EXEC = """# Student Services — Fragmentation Deep-Dive

*How each current-student service is spread across the University's 20-domain public web estate, traced through the path-level link graph (21,250 pages). One profile per service: its true footprint, canonical owner, the seams a student hits, the duplication, and the consolidation action. June 2026.*

---

## Executive summary

Read service-by-service, the estate's fragmentation has a consistent shape. For most services the **central hub `students.unimelb.edu.au` *is* the right owner and *is* reached** — the problem is rarely "no front door." The problem is what happens **downstream of the front door**: the hub duplicates itself across parallel URL trees, the actual service delivery sits on a *different* host (often branded as something else, or behind login, or off the crawled estate entirely), and every faculty re-hosts its own copy rather than linking the centre. A student looking for one service routes through **three or four hosts with inconsistent labels** to reach the thing they need — and sometimes the most authoritative version is a draft, a deprecated tree, or a prospective-marketing page.

Six structural patterns recur across the services below. They are not fourteen separate problems; they are **six systemic faults expressed fourteen times** — which is what makes them fixable as patterns, not page-by-page.
"""

PATTERNS = """## The six recurring fragmentation patterns

**1. The hub duplicates *itself* — parallel URL trees mid-migration.** Almost every service that the hub owns is served under two or three live URL roots at once — `/support-and-wellbeing` vs legacy `/student-support` (wellbeing, equity, international, contacts), `/course-admin` vs `/your-course` vs `/admin` (fees, enrolment, graduation, exams). The legacy tree usually carries `rel=canonical` to the new one yet stays live and internally linked, so the same content competes with itself for inbound links and search rank. *Affects: wellbeing, equity, fees, international, enrolment, graduation, exams, contacts.*

**2. The canonical owner exists but is barely reached — or doesn't exist at all.** Scholarships has a dedicated 2,124-page `scholarships.unimelb` but the hub links it ~37×; Student IT's real home `studentit.unimelb` and HDR's `gradresearch.unimelb` sit **outside the student estate entirely**; placements/WIL has **no central owner at all** (zero WIL front door on the hub). The owner is an afterthought, off-estate, or absent. *Affects: scholarships, IT, HDR, careers, placements.*

**3. The action lives behind login; the public estate only *describes* it.** The thing a student actually does — pay fees, enrol in a subject, book a counselling appointment, apply to graduate, log an IT ticket, RSVP a careers event — happens in `my.unimelb`, Canvas, ServiceNow or a `*.app` form, all behind auth and uncrawlable. The public pages narrate the service and link to a login wall, so the find→act seam is invisible from the outside and unverifiable. *Affects: IT, careers, enrolment, graduation, fees, wellbeing.*

**4. Delivery sits on a shared or off-brand host.** Counselling and the Health Service live on `services.unimelb`, a multi-service host that is described as "Academic Skills Unit" (614×) and "DELA" (613×) far more than "Counselling" (39×) — so a wellbeing link lands on a page branded as something else. Safer Community and campus safety are separate sites again. The student crosses a host boundary onto an unfamiliar brand mid-task. *Affects: wellbeing, academic skills, safety.*

**5. The reverse-funnel — prospective owns the content the enrolled student needs.** Fees content is 363 pages on the prospective `study.unimelb` vs ~17 on the hub; careers' single biggest owner is `study.unimelb` (440 pages); scholarships' discovery engine is prospective-facing. Enrolled students are bounced *back up the funnel* to marketing pages for answers they need *now*. *Affects: fees, careers, scholarships.*

**6. Faculty re-invention and byte-identical clones.** Faculties re-host the central service rather than link it — and often verbatim: 5 Jaccard-1.0 wellbeing clones and the entire HDR candidature lifecycle duplicated byte-for-byte across Education and MDHS; the BCom careers tree double-hosted by FBE and MBS; placements scattered across 8 faculty silos under 4 different names; student-life across 12+ faculty silos. The same content is maintained N times and drifts out of sync. *Affects: HDR, wellbeing, placements, student-life, careers, equity.*
"""

def fmt_profile(p):
    f = frag.get(p['service'], {})
    out = [f"## {p['service']}  `[{p['severity'].upper()}]`", f"**{p['headline']}**", ""]
    meta = []
    if f:
        meta.append(f"*Spread: {f['domains']} domains · {f['url_trees']} URL trees · "
                    f"central-hub pages {f['central_hub_pages']} · top owner {f['top_domain'].split('.')[0]} ({f['top_domain_pages']}).*")
    meta.append(f"**True footprint.** {p['true_pages_note']}")
    meta.append(f"**Canonical owner.** {p['canonical_owner']}")
    out += meta + [""]
    if p.get('key_locations'):
        out.append("**Where it lives**\n")
        out.append("| Location | Role | Note |\n|---|---|---|")
        for k in p['key_locations']:
            note = k['note'].replace('|', '\\|')
            out.append(f"| {k['where']} | {k['role']} | {note} |")
        out.append("")
    if p.get('seams'):
        out.append("**The seams a student hits**\n")
        out += [f"- {s}" for s in p['seams']]
        out.append("")
    if p.get('duplication'):
        out.append("**Duplication**\n")
        out += [f"- {d}" for d in p['duplication']]
        out.append("")
    out.append(f"**Consolidation action.** {p['recommendation']}")
    return "\n".join(out)

# league table
league = ["## Fragmentation league table\n",
          "Services ranked by spread (domains × URL trees). Raw page counts include keyword false positives (filtered in each profile); the spread itself is the fragmentation signal.\n",
          "| Service | Raw pages | Domains | URL trees | Central hub | Top owner | Spread score |",
          "|---|--:|--:|--:|--:|---|--:|"]
for s, r in sorted(frag.items(), key=lambda kv: -int(kv[1]['frag_score'])):
    league.append(f"| {s} | {r['pages']} | {r['domains']} | {r['url_trees']} | {r['central_hub_pages']} | "
                  f"{r['top_domain'].split('.')[0]} ({r['top_domain_pages']}) | {r['frag_score']} |")

CONSOLIDATION = """## The consolidation map

Each pattern has one systemic fix; together they are the service-level expression of the central-and-spoke model.

| Pattern | Systemic fix | Owner |
|---|---|---|
| 1 · Hub duplicates itself | Finish the hub URL migration: pick one canonical root per service, 301 the legacy/duplicate trees, enforce a "no live inbound on two trees" check | Central platform |
| 2 · Canonical owner unreached / absent | For each service name ONE system of record (scholarships.unimelb, studentit.unimelb, gradresearch.unimelb, a new central WIL page) and make the hub deep-link it from the relevant task pages | Central + service owners |
| 3 · Action behind login | Map the public→authenticated seam per service; expose the *action* (deep-link the my.unimelb/Canvas/form entry) from the public page, and confirm the logged-in side isn't already doing the linking | Central + my.unimelb |
| 4 · Off-brand delivery host | Re-brand or sub-path shared hosts (surface Counselling/Health under a wellbeing-branded entry); use consistent destination labels | Service owners |
| 5 · Reverse-funnel | Give enrolled students their own fees/careers/scholarships home on the hub; stop routing them back to study.unimelb | Central |
| 6 · Faculty re-invention / clones | Mandate "link, don't re-host" in the standardised student overlay; 301 the byte-identical clones to the canonical page | Governance + faculties |

**The through-line:** the centre mostly already holds — every faculty links into `students.unimelb`, and the hub is the right owner for most services. The work is not to *build* a centre; it is to **finish the hub's own migration, name the off-estate owners, and stop the faculties (and the hub itself) from duplicating what the centre already has.**

---

*Source: per-service link-graph profiles in `analysis/student-services-profiles.json`; classifier + metrics in `analysis/full-scrape/service_fragmentation.py`, `service-fragmentation.csv`, `service-pages.csv`. The authenticated core (my.unimelb, Canvas) and off-estate service sites (studentit, gradresearch, services, safercommunity) were not crawled — claims about them are inferred from inbound links and noted per profile.*
"""

doc = "\n\n".join([EXEC, PATTERNS, "\n".join(league), "## Per-service deep-dives\n"]
                  + [fmt_profile(p) for p in profs] + [CONSOLIDATION])
(ROOT / 'analysis/student-services-fragmentation.md').write_text(doc)
print(f"wrote analysis/student-services-fragmentation.md ({len(doc):,} chars, {len(profs)} services)")
