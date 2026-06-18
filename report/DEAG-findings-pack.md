# Current Students Web Estate — Findings & Decision Pack
### For the Digital Experience Advisory Group (DEAG) · June 2026

---

> ## Decision at a glance
> A full crawl of the University's current-students web estate — **1,173 pages** across the central hub, **9 faculty** sections and **3 school** sections — finds the estate is **85% unique, discipline-specific content**, not duplication. The service model is **structurally sound but the seams are broken**: six different URL conventions, careers content siloed across 9 faculties with zero cross-linking, the hub missing whole services that students need (placements, course planning), school-level sites splintering the experience, and ~50 broken pages.
>
> **DEAG is asked to endorse three things:**
> 1. **Direction** — a *hub-and-spoke* model (hub owns the transactional spine + fills its gaps; faculties keep their discipline-specific estates under shared standards). **Not** full centralisation; **not** status quo.
> 2. **No-regrets actions now** — standard URL, a "where do I go for X" component, fix the broken links, and connect careers. These need no structural decision and can start immediately.
> 3. **A standards mandate + a scoped Phase 2** — so the seams actually get fixed and stay fixed.

---

## 1. Purpose & scope

The student web experience is delivered jointly by the central hub (`students.unimelb.edu.au`) and current-students sections run independently by each faculty (and, in some cases, individual schools). DEAG asked whether that **service model is still working**, where content **overlaps or has gaps**, and what — if anything — should change.

This pack answers those questions from **direct evidence**: every reachable current-students page across the estate was crawled, classified and topic-tagged. It then sets out the options and the decision we recommend DEAG take.

**In scope:** the central hub + the current-students sections of all 9 faculties + the 3 schools that run their own (Melbourne Business School, Biomedical Sciences, Melbourne Dental School).
**Out of scope:** authenticated systems (my.unimelb, Canvas/LMS, SIS, Stop 1 service desk), prospective-student content, and staff content.

## 2. Method (and its limits)

A browser-based crawler walked each current-students section breadth-first, capturing for every page its content, word count, in-section structure, outbound links (where it sends students), a unique/duplicative classification, and topic tags. **1,173 pages** were captured.

*Limitations, stated honestly:* ABP/MSD hit a 250-page ceiling because of a large self-referencing studio archive (~700 further pages of one repeating type — counted as a single content class, not omitted findings). The central hub was mapped at IA + section-landing level, not leaf-by-leaf. Classification is automated (a page is "unique" if it carries substantive original prose, "link-farm" if it mostly routes elsewhere) and is indicative, not hand-audited. Cloudflare actively blocked conventional/headless crawling — a finding in itself for any future automated audit.

## 3. What we found

### Finding 1 — The estate is large, and overwhelmingly *unique*
**997 of 1,173 pages (85%) are unique, substantive content.** Only ~4% are pure link-farms and ~7% are mixed. The dominant content is exactly what *can't* live centrally: subjects & timetabling (324 pages), research candidature (243), forms & admin (213), course planning (208), **placements & WIL (207)**. This is the single most important finding: **the faculty estate is real content, not redundant signposting.** "Just centralise it" is not a credible option.

### Finding 2 — Every faculty hosts a real estate; the "link directory" picture was wrong
Earlier sampling suggested some faculties (ABP, FBE) were thin link directories. The full crawl disproves it: ABP runs **240 unique pages** (sample course plans, studios, mentoring); FFAM runs a substantive 37-page section (ensembles, facilities, forms); MDHS runs **104 unique pages** of clinical-placement compliance. What faculties *do* delegate is **transactional admin** — they correctly send students to the hub for enrolment, fees, exams. The duplication problem is **smaller and thinner** than feared; the *seam* problem is bigger.

### Finding 3 — Six URL conventions for one idea
"Information for current students" lives at six different addresses: `/students` · `/current-students` · `/study/current-students` · `/study/student-resources` · `/study/current-student-information` · (and the hub). A student cannot guess their faculty's URL, and `fbe…/current-students` is a dead 404 where one would expect the page.

### Finding 4 — Careers is the clearest failure: parallel everywhere, connected nowhere
**8 of 9 faculties plus MBS run their own careers/employability content** (mentoring, internships, industry programs) in parallel with the central Careers hub — and the hub and faculty careers pages **do not cross-link in either direction.** A student using the hub's career checklist may never discover their faculty's mentoring program, and vice-versa. This is the highest-value, lowest-cost fix in the estate.

### Finding 5 — The hub has real gaps where every faculty has built
The hub covers the transactional spine well but has **no presence** in services every faculty provides: **placements & WIL** (207 faculty pages; hub ≈ 0), **degree-specific course planning**, **discipline academic skills** (legal writing, lab reports, studio practice), **faculty forms** (213 pages), and **program regulatory pathways** (LANTITE for teaching, Fitness-to-Practice / AHPRA for health). These gaps are *why* faculties build parallel sites.

### Finding 6 — School-level fragmentation multiplies the experience
Three schools run their own current-students sites *beneath* their faculty: **MBS (61 pages**, plus its own "Career Elevation" service), **Biomedical Sciences (42)**, **Dental (4)**. A Biomedicine student can traverse **three** different "home" experiences — the hub, the MDHS faculty section, and the Biomedical school site — each with a different URL pattern and template.

### Finding 7 — Quality debt is visible and fixable
~**50 pages are broken or misrouting**, concentrated in: Biomedical Sciences (18 — including 16 "major" pages with duplicate CMS slugs bouncing students to the *prospective* catalogue), FEIT (17 duplicate/broken URLs), ABP (6), MDHS (3), Arts (3), FBE (2). The Dental site even depends on case-sensitive paths (`/Forms` works, `/forms` 404s) and splits its own forms across two external form hosts.

### Finding 8 — No page tells students "what's where"
Not one faculty section carries a consistent "for X go to the hub; for Y stay here" signpost. Students learn the split by trial and error, and faculty pages routinely re-explain hub services (special consideration, leave of absence) that the hub owns definitively.

### Finding 9 — The topic evidence sharpens the consolidation target — and flags a data-quality clean-up
A topic-by-topic crawl (18 topics) pinpoints where consolidation pays. The **transactional spine** (enrolment, exams & results, special consideration, fees, library — 227 pages) has **only 6 pages on the hub domain**; the rest are faculty restatements of content the hub already owns — the single clearest target. **Scholarships** (faculties hold 141 pages of generic process scaffolding while a central catalogue already exists) and the duplicated "Employability in X" / "Wellbeing + Ambassadors" landing pages are next. The same pass shows topic page-counts are **inflated by content-quality artifacts** — ABP/MSD's ~700-page studio archive, FEIT nesting its estate under `/orientation` and `/students/it`, and ~70 Law researcher bios — i.e. a meaningful share of the apparent "volume" is archival bloat and URL/CMS hygiene to fix at source, independent of the unification decision. Full breakdown in Appendix B.

## 4. The service-model verdict

**The hub-and-faculty division of labour is the right one — but it is being run without the connective tissue that makes it work.** The hub is the correct owner of the transactional spine; faculties are the correct owners of placements, course plans, discipline skills and forms. What's missing is everything *between* them: consistent addressing, mutual signposting, a hub presence for placements/course-planning, connected careers, consolidated school sites, and enforced standards. The fix is therefore **not** re-drawing ownership (centralise/decentralise) — it is **engineering the seams**.

## 5. Discussion points for DEAG

1. **Autonomy vs consistency.** Faculties have invested years in genuinely useful content. Standards must be *mandated* (the URL chaos proves advisory guidance has failed) without gutting faculty ownership. How much standardisation will DEAG require, and with what authority?
2. **The 85%-unique reality.** It takes "lift-and-shift to the hub" off the table. Does DEAG accept that the goal is a *connected federation*, not a single site?
3. **School-level sites (MBS, Biomedical, Dental).** Tolerate, standardise, or consolidate into their faculty? MBS in particular is effectively a second business-school experience under FBE.
4. **The careers silo.** The clearest single win — but who owns the hub↔faculty careers bridge, and will faculties agree to embed the central tools?
5. **Hub gaps.** Filling placements / course-planning gateways means the central team owns *new* content. Is there capacity, or should these be thin "connector" pages that point into faculty content?
6. **Governance teeth.** What mandate will DEAG actually back — standards as policy, with audit and consequences, or another advisory guideline?
7. **Personalisation as an accelerator.** If Optimizely + Tealium (CDP) are in the University's martech stack, a *personalised hub* could surface the right faculty content to a known student without moving any pages — potentially leapfrogging migration. **This needs confirming** (see decision ask).

## 6. Options (recalibrated to the evidence)

| Option | What it is | Verdict against the evidence |
|---|---|---|
| **A. Full centralisation** | Move faculty CS content to the hub | **Reject.** 997 unique, discipline-specific pages (clinical compliance, studios, legal skills) cannot be owned or maintained centrally. |
| **B. Status quo + light governance** | Keep everything, add advisory standards | **Insufficient.** Advisory standards already failed (6 URL conventions). Doesn't fix careers, gaps or school sites. |
| **C. Hub-and-spoke with standards *(recommended)*** | Hub owns the transactional spine **and fills its gaps** (placements, course-planning, careers bridge); faculties keep discipline content under a mandated template, URL and signposting standard; school sites consolidated | **Best fit.** Matches the 85%-unique reality, fixes the seams, preserves faculty investment, achievable in ~12 months. |
| **D. Hub-and-spoke + CDP personalisation** | Option C **plus** a personalised hub (Optimizely/Tealium) that surfaces a student's faculty content automatically | **Strongest *if* the martech exists.** Adds a modern, personalised front door with no extra migration. Contingent on stack + data. |

**Recommendation: adopt C now, and upgrade to D if Optimizely/Tealium are confirmed.**

## 7. The decision asked of DEAG

- **Decision 1 — Endorse the direction (C/D), ruling out full centralisation and status quo.**
- **Decision 2 — Approve the no-regrets actions to begin immediately** (Section 8). These deliver visible improvement inside a quarter and need no structural change.
- **Decision 3 — Mandate a standards baseline and commission a scoped Phase 2** (hub gap-fill + school-site consolidation policy + governance with audit). Confirm whether Optimizely/Tealium are available to determine C vs D.

## 8. No-regrets actions (start now, regardless of the above)

| Action | Why | Effort |
|---|---|---|
| **Standardise the URL** to `faculty.unimelb.edu.au/students` + 301-redirect the five variants | Discoverability; kills the 404 trap | Low |
| **Ship a "Where do I go for X?" component** on every faculty CS page | Directly fixes Finding 8 — the single highest-impact student fix | Low–Med |
| **Fix the ~50 broken/misrouting pages** (Biomedical 18, FEIT 17 first) | Removes the worst quality debt; stops routing students to the wrong catalogue | Low |
| **Cross-link careers** both ways (hub ↔ every faculty) | Fixes the clearest failure in the estate | Low |
| **Publish the standard CS template** (key contacts · course planning · placements · faculty life · forms · "where to go") | Baseline every faculty/school section can adopt | Med |

## Appendix A — Measured evidence (per unit)

| Unit | Level | Pages | Unique | Mixed | Link-farm | Broken | CS URL pattern |
|---|---|--:|--:|--:|--:|--:|---|
| Law | Faculty | 195 | 162 | 10 | 23 | 0 | `/students` |
| FEIT | Faculty | 204 | 174 | 13 | 0 | 17 | `/students` |
| Arts | Faculty | 91 | 51 | 24 | 13 | 3 | `/students` |
| Science | Faculty | 94 | 91 | 2 | 0 | 1 | `/students` |
| ABP / MSD | Faculty | 250* | 240 | 4 | 0 | 6 | `/current-students` |
| FBE | Faculty | 36 | 31 | 3 | 0 | 2 | `/students` |
| Education | Faculty | 47 | 32 | 10 | 5 | 0 | `/study/current-students` |
| FFAM | Faculty | 37 | 28 | 4 | 5 | 0 | `/current-students` |
| MDHS | Faculty | 112 | 104 | 4 | 1 | 3 | `/study/current-students` |
| **MBS** | School (FBE) | 61 | 60 | 1 | 0 | 0 | `/students` |
| **Biomedical Sci.** | School (MDHS) | 42 | 21 | 3 | 0 | 18 | `/study/current-student-information` |
| **Dental** | School (MDHS) | 4 | 3 | 1 | 0 | 0 | `/study/student-resources` |
| **Total** | | **1,173** | **997 (85%)** | **79** | **47** | **50** | **6 conventions** |

\* ABP capped at 250; a further ~700 studio-archive pages of one repeating type were not individually crawled.

## Appendix B — Topic evidence (18 topics)

*Page counts are deduped topic-tag totals, inflated by classifier artifacts (see "Verdict"); the per-topic deep-dive notes (`analysis/topic-deepdives/`) correct for this.*

| Topic | Pages | Verdict | What the evidence shows |
|---|--:|---|---|
| Subjects & timetabling | 319 | mixed | 64% is ABP/MSD's design-studio archive; rest a thin hub-owned timetabling spine echoed by faculties. |
| Orientation | 289 | inflated | FEIT holds 71% via `/orientation` path-nesting; genuine orientation is a thin faculty welcome layer. |
| Research candidature | 241 | faculty-owned | Legit (milestones, studios, funding); +~70 Law researcher bios; hub-own the candidature lifecycle spine. |
| IT & systems | 235 | artefact tag | 78% mis-classified FEIT content; hub owns the Student IT / LMS / portal spine. |
| **Transactional admin** (enrol · exams · special-con · fees · library) | 227 | **hub-owned** | **Only 6 of 227 pages on the hub domain**; rest are faculty restatements — the clearest consolidation target. |
| Student life | 214 | faculty-owned | Largely legit (clubs, mentoring, awards); ~⅓ is MSD/Science roster bloat. |
| Forms & admin | 212 | mixed | Law + MDHS heavy (compliance); offer/enrolment/special-con admin overlaps the hub. |
| Course planning | 207 | faculty-owned | Degree-specific plans; MBS + Biomedical = 46%; thin hub-overlap. |
| Placements & WIL | 206 | faculty-owned | MDHS 47% (clinical compliance); near-zero hub overlap; gap is discoverability, not duplication. |
| Contacts & support | 177 | mixed | ~half is Arts + Law restatements of hub wellbeing/equity/careers + stub pages. |
| Careers & employability | 141 | mixed | Legit core (pathways, internships, mentoring) + a duplicated "Employability in X" layer. |
| Scholarships | 141 | consolidate | Hub holds zero; mostly generic process scaffolding → fold into central `scholarships.unimelb.edu.au`. |
| International | 135 | mislabelled | ~80% is outbound mobility; genuine inbound support (visas/OSHC) is absent and hub-owned. |
| Graduation | 125 | misnomer | HDR candidature lifecycle + honours, not ceremonies; the apply-to-graduate spine is missing. |
| Clubs & events | 104 | faculty-owned | Community content; only the generic club-admin wrapper overlaps the hub. |
| Wellbeing & health | 87 | mixed | Half is MDHS clinical compliance; 6 near-duplicate "Wellbeing + Ambassadors" landings to collapse. |
| Inclusion & equity | 49 | consolidate | Noise-heavy; ~13 real pages parallel-reinvent the central service. |
| Academic skills | 37 | hub-overlap | Discipline skills are legit; generic landings duplicate the central service. |

*Evidence base: `crawl/pages/*.json` (1,173 records), `analysis/`, `data/`. Full corpus available on request.*
