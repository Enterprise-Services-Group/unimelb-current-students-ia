# Sam — Planning their path

> *"I just need to know what subjects to pick and when — but the course plan is on the faculty site, the planner tool is somewhere else, and the actual rules are in FAQ articles from years ago."*

## Bio
Sam is a first-year domestic undergraduate, the first in their family to attend university. They arrived via VTAC, accepted their offer through the standard channel, and now face the core task that determines everything downstream: planning a degree and enrolling in subjects. Sam is digitally literate but has never navigated a university system before. They don't know what "census date" means, haven't used My Course Planner, and assume the University's website will walk them through it. It won't.

## Journey pain points

| Pain point | Crawl evidence | Severity |
|---|---|---|
| **Planning requires 7 systems** — hub guidance, My Course Planner, Handbook, ask.unimelb FAQ, my.unimelb, MyTimetable, variation forms | 343 hub pages (41% of total) span 7 distinct platforms; no single page assembles the toolchain | HIGH |
| **Hub guidance is duplicated** — two parallel URL trees compete for the same content | 120 leaf pages dual-served under `/your-course` + `/course-admin`; 19 core leaves byte-near duplicates | HIGH |
| **My Course Planner is off-hub and there are two planning surfaces** | StudyOS subdomain + my.unimelb /sone/STUDYPLN — two tools with no clear delineation | HIGH |
| **The actual answers live in a legacy FAQ** | 396 links to ask.unimelb across two inconsistent URL formats; hub describes, FAQ answers | HIGH |
| **Census dates page canonicalises to /page-not-found** | The single most financially consequential date page tells search engines it doesn't exist | HIGH |
| **Course structure requires a Handbook switch mid-decision** | 195 links to handbook.unimelb — different platform, different visual standard | MEDIUM |
| **Faculties re-host planning content instead of linking the centre** | 71 faculty course-planning pages parallel the central guidance | MEDIUM |

## Top frustrations
1. **No single planning home.** Sam assembles their degree plan by bouncing between 7 systems — the estate provides no unified journey.
2. **The hub competes with itself.** Sam lands on `/your-course` from a faculty link but the canonical version is `/course-admin` — they don't know which to trust.
3. **Answers are one hop away.** Every "how do I…" question sends Sam to a legacy FAQ on a different system with a different visual standard.
4. **The census date page is broken.** The deadline that could cost Sam money and enrolment has a self-defeating canonical tag.

## Service touchpoints
| Touchpoint | System | Current state |
|---|---|---|
| Course discovery | study.unimelb /find | Good — 7-tab micro-site per course |
| Entry requirements | Handbook | Requires platform switch mid-decision |
| Application | VTAC (external) | Leaves University estate entirely |
| Offer → Enrol | my.unimelb (behind login) | Thin seam — 373 contextual links estate-wide |
| Plan subjects | My Course Planner (StudyOS) + my.unimelb study plan | Two tools, no clear delineation |
| Enrol | my.unimelb (behind login) | Public estate only describes |
| Timetable | MyTimetable (separate subdomain) | Another login, another system |
| Census/variations | ask.unimelb + forms.your + *.app | Scattered across legacy FAQ and microsites |

## Systems traversed
~6: study.unimelb → vtac.edu.au (external) → my.unimelb (auth) → students.unimelb → handbook.unimelb → faculty site

## Linked improvements from the register
| # | Improvement | Severity · Effort |
|---|---|---|
| 1 | Finish the stalled hub migration & collapse parallel URL trees | HIGH · medium |
| 3 | Mandate a thin standardised student overlay on Squiz | HIGH · medium |
| 5 | Guarantee 301s for MSD's ~8,000 deep-links into legacy hub paths | HIGH · quick-win |

## Related deep-dives
- `analysis/course-planning-enrolment.md` — full toolchain audit
- `analysis/lifecycle-journeys.md` — Domestic undergraduate journey trace
- `report/Course-Planning-Enrolment.html` — formatted report

---

*Built from: theydo_export/personas.csv, course-planning-enrolment.md deep-dive, lifecycle-journeys.md, improvements-register.md, and the full-scrape link graph (students-full crawl, 833 hub pages, cross-site-flow.csv). June 2026.*
