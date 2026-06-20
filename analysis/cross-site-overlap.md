# Cross-site overlap analysis — University web estate
### Scope: current-students estate (13 sites) × study.unimelb × alumni.unimelb

---

> **Data:** All rows are from the June 2026 crawl. Current-students estate: 1,173 pages across hub + 9 faculties + 3 schools. study.unimelb: 300 pages (271 unique). alumni.unimelb (www.unimelb.edu.au/alumni): 116 pages (112 unique).

---

## 1. How the sites connect (or don't)

### Outbound link traffic from current-students faculty sections

| Destination | Total outbound links | From # of faculty sections | Signal |
|---|--:|--:|---|
| `students.unimelb.edu.au` | 4,629 | all 13 | Hub is the primary cross-link target |
| `study.unimelb.edu.au` | 529 | multiple faculties | Students sent BACK to prospective site |
| `alumni.unimelb.edu.au` | **0** | 0 of 13 | **Alumni site is invisible from current-student estate** |
| `giving.unimelb.edu.au` | 399 | multiple | Giving/philanthropy linked directly |
| `scholarships.unimelb.edu.au` | 515 | multiple | Scholarships has its own dedicated domain |
| `careers.unimelb.edu.au` | 5 | ~3 | Careers hub almost entirely absent from faculty CS links |

**Key finding — the estate is not circular:** Students are being sent TO study.unimelb (529 links) for prospective-style content they're looking for during their enrolment/course-planning journey, but there is no path forward to alumni from anywhere in the current-students estate. The lifecycle continuity (student → graduate → alumni) is structurally broken at the web level.

### Faculty alumni sub-paths (Part 2c)

A scan of all 1,161 current-students pages for outbound alumni.unimelb.edu.au links found zero. No faculty section carries an internal `/alumni` sub-path within its current-students scope that would warrant a targeted crawl. Alumni content — where it exists at the faculty level — is either absent or on a completely separate path not linked from the students section.

---

## 2. Cross-site topic distribution

For each topic where content exists in more than one part of the estate, the table shows page counts and a verdict.

| Topic | Hub (students.) | Faculty CS | study.unimelb | alumni.unimelb | Verdict |
|---|---|---|--:|--:|---|
| Course / degree info | Planner + Handbook | Every faculty | **224 pp** — course brochures, degree finders | — | **Intentional split:** study for entry, faculties for ongoing planning. study→students has 273 outbound links to the hub but the handoff is undesigned. |
| Fees & finance | Thin hub | Some faculties | **34 pp** — fees + living costs | — | study.unimelb is the authoritative source for prospective fees; hub replicates HECS/FEE-HELP. Low overlap risk. |
| Scholarships | 0 | **141 pp** | **75 pp** (scholarships + study-scholarships) | **1 pp** — alumni-funded | `scholarships.unimelb.edu.au` exists as a consolidation point but isn't consistently linked from any of the three sites. **Classic three-way duplication.** |
| Careers | Central platform | **141 pp** (8 of 9) | **37 pp** — entry only | **38 pp** + mentoring (20 pp) | Four parallel careers presences with no cross-linking. The alumni mentoring pipeline (graduates back into current students) is the clearest missing link. |
| Placements / WIL | 0 | **207 pp** (every faculty) | 10 pp — overview only | — | Hub gap; faculty-owned. No alumni angle; study.unimelb has surface-level WIL mentions only. |
| Research candidature | Thin | Heavy | **1 pp** — entry info | **1 pp** | study.unimelb has minimal PhD entry content; faculties own the candidature lifecycle; no handoff. |
| Alumni engagement | — | Some (patchy) | — | **116 pp** — full estate | **The most broken handoff in the estate.** Zero links from current-students → alumni. Graduation is the exit from the current-students estate with nowhere to go next. |
| Student life / community | Heavy (UMSU) | Faculty-owned | **47 pp** — campus life (entry framing) | **21 pp** — alumni community | Three distinct framings (UMSU, faculty societies, alumni network) with no narrative thread. |
| International | Hub + some faculties | Some | **66 pp** — full international (entry) | **20 pp** — international alumni | Outbound mobility is faculty-owned; inbound visa/OSHC is a hub gap. study.unimelb has full international applicant coverage. |

---

## 3. Unique to study.unimelb (no counterpart in current-students estate)

Confirmed from the June 2026 crawl (300 pages, 271 unique):

- **Graduate Degree Package pages** (14+ substantive pages, 2k–4.7k words each, 8–24 links per page to students.unimelb) — the University's enrolled-student pathway product lives entirely on a prospective site with no enrolled-student mirror
- **ATAR / selection rank tables and entry requirement detail** (23 pages, study-entry-requirements)
- **Moving Guide** — a post-offer, pre-arrival guide for international students; highest-stakes misplaced content in the estate
- **Living costs and fee estimators** (21 pages study-fees-costs + 13 fees-finance) — the prospective site holds the canonical version, enrolled students who return here find no path to the hub
- **Course finder / degree browser** — `/find` section (81 pages) has no equivalent in the current-students estate
- **The Glossary** (6,294 words, 44 links to students hub) — functions as an enrolled-student orientation document but lives on the prospective site
- **Campus life content** (109 pages, study-campus-life) framed at "will I fit in?" rather than "how do I participate?"

**Why this matters:** 273 outbound links from study.unimelb → students.unimelb confirm prospective content is already being used post-enrolment. But study.unimelb has no "you're enrolled: start here" pathway, so new students land mid-prospectus.

---

## 4. Unique to alumni.unimelb (no counterpart in current-students estate)

Confirmed from the June 2026 crawl (116 pages, 112 unique; www.unimelb.edu.au/alumni):

- **Global chapter network** — 12 faculty-specific mentoring streams (accounting, arts, business, education, engineering, fine arts, law, MDHS, medicine, MLS, science, vet science) each with their own pages; none visible from the current-students estate
- **Alumni awards** (5 award-year archives) — no equivalent in current-students pages
- **Alumni council** (15+ council member bios)
- **Graduate benefits package** (20 pages: library access, alumni email, sports centre, career tools, language learning, journal access, lifestyle benefits) — graduating students are not told this exists
- **Giving / philanthropy** (1 page — alumni-giving tag) — clean separation from current-students content
- **"Welcome new alumni" page** (1,745w) — the natural first destination for a graduate, but zero links point to it from anywhere in the current-students estate; it is discoverable only via the alumni site itself or external channels

**Why this matters:** Alumni benefits, the global chapter network, and the mentoring pipeline are things a graduating student needs to know exist BEFORE they leave the current-students estate. Zero current-students pages link to alumni.unimelb — graduates discover this site through external channels or not at all.

---

## 5. Related but not duplicated (same lifecycle stage, different audience)

| Content area | Current-students version | Alumni version | Assessment |
|---|---|---|---|
| Careers | Faculty careers offices + central hub | Alumni mentoring network | Different service, same broad need. Cross-linking would be additive, not duplicative. |
| Events | Faculty student events, UMSU | Alumni reunions, lecture series | Separate audiences but common venue (campus). Alumni events currently invisible to current students. |
| Community / belonging | UMSU, student societies | Alumni network, chapters | Lifecycle continuity: student society → alumni chapter. No web path connecting them. |
| Research | HDR candidature milestones | Alumni research collaborations | Separate pages serving different needs — this overlap is not a problem. |

---

## 6. The structural handoff problem

The University's web estate has three distinct lifecycle phases:

```
PROSPECTIVE           CURRENT STUDENT           GRADUATE/ALUMNI
study.unimelb   →   students.unimelb + faculties   →   alumni.unimelb
```

The left handoff (prospective → current) partially works: 529 outbound links from faculty CS sections back to study.unimelb suggest students crossing back. But there is no forward signpost FROM study.unimelb INTO the current-students estate for new enrolees.

The right handoff (current → alumni) is **completely absent**: 0 links from any current-students page to alumni.unimelb. The graduation milestone — the natural exit point from the current-students estate — has no "what comes next" signpost anywhere in the web experience.

---

## 7. Verdicts by topic

| Topic | Verdict | Priority |
|---|---|---|
| Scholarships | Three-way duplication (`scholarships.unimelb`, faculty, study.unimelb) — consolidate around `scholarships.unimelb` as the single entry point | High |
| Careers | Four parallel presences (hub, 8 faculties, study, alumni) — connect rather than consolidate; alumni mentoring is the highest-value missing link | High |
| Alumni handoff | Structurally absent — add "what happens after you graduate" signpost at graduation pages | High |
| study.unimelb → students handoff | No web path for new enrolees from prospective to current site — add prominent "you're enrolled: start here" pathway | Medium |
| Fees / course info | Intentional split (prospective vs ongoing) — keep separate but cross-link clearly at enrolment transition | Low |
| Research candidature | Different lifecycle stages (entry info vs candidature milestones) — keep separate | Low |

---

*Source: faculty crawl June 2026 (1,173 pages across 13 units); study.unimelb crawl June 2026 (300 pages, 271 unique); alumni.unimelb crawl June 2026 (116 pages, 112 unique). Graphify cross-site analysis: graphify-out/graph.json (updated June 2026 with all three corpora).*
