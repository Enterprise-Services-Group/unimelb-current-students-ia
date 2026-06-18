# Phase 1 findings — academic-unit structure & CS-section routing

_Captured live via Claude-in-Chrome, 2026-06-15. Every one of the ~43 academic units in `data/unit-registry.csv` was probed for a Current Students section._

## Headline structural findings

1. **Every faculty (9/9) runs its own local Current Students section** — none rely solely on the central hub. But they live at **four different URL conventions**, an early consistency red flag:
   | Pattern | Faculties |
   |---|---|
   | `/students` | Arts, FEIT (`eng`), Law, Science |
   | `/current-students` | ABP (`msd`), FBE, FFAM (`finearts-music`) |
   | `/study/current-students` | Education, MDHS |

2. **Schools / departments / institutes / centres do NOT run their own CS sections** (0 of ~33). They are **pass-throughs** that send students either to their *faculty's* CS section or straight to the *central hub*. This is the unit-level "link-farm" pattern, before we even crawl page-level.

3. **The shared global UoM header** carries a "Students" link that points to `students.unimelb.edu.au` on **every** unit site — so the central hub is always one click away, yet faculties simultaneously maintain parallel local sections. This dual-path is the core of the fragmented experience.

4. **Inconsistent sub-unit routing — even within the same faculty cohort:**
   - **Science** schools (safes, biosciences, chemistry, sgeas, ms, physics, mvs) → all route to the **faculty** CS (`science.unimelb.edu.au/students`).
   - **FEIT** schools (cis, chem-biomed, EMI) → all route to the **faculty** CS (`eng.unimelb.edu.au/students`).
   - **Arts** schools → route to the **faculty** CS (`arts.unimelb.edu.au/students`), some deep-linking into it (language placement tests, Diploma in Languages).
   - **FFAM** units (MCM, VCA, Wilin) → route to the **faculty** CS; **Wilin** additionally keeps its **own** Indigenous student-support page.
   - **MDHS** schools (dental, medicine, health sciences, psych, biomedical, MSPGH) → route to the **central hub**, **NOT** their own faculty CS section. So MDHS students get a different "home" depending on whether they land on the faculty site vs a school site.
   - **FBE** departments (accounting, economics, finance, management & marketing) and **MBS / Melbourne Institute** → route to the **central hub** (no faculty-CS link surfaced).

5. **URL-convention traps already cause dead ends:** Education and MDHS both **404** on `/students` and `/current-students` — their real CS sections are only at `/study/current-students`. A student (or staffer) guessing the "usual" URL hits a Page Not Found.

## CS-section "shape" varies by faculty (from the probe)
- **Science** — single landing page with in-page anchors (course guides UG/PG, studying & student life, news, support) + per-degree "course guide" pages.
- **Law** — true sub-tree: `/students/jd`, `/students/masters`, `/students/graduate-research`.
- **Education** — task pages: timetable, Academic Skills module, LANTITE, ICAS, ITEA, enrolment/re-enrolment.
- **MDHS** — fitness-to-practice, Student Enrichment & Support ("MDHS Student Hub"), Student Placements (WIL).
- (Arts, FBE, FFAM, ABP/MSD, FEIT depth to be mapped in the Phase 2 crawl.)

## Implication for the crawl scope
The exhaustive crawl therefore has **10 roots**: the **9 faculty CS sections** + the **central hub**. The ~33 sub-units are recorded with their `routes_to` target (see `unit-registry.csv`) rather than crawled as separate trees — their routing *is* the finding.
