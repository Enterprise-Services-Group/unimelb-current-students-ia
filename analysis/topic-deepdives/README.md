# Topic Deep-Dives — index

Eighteen topic notes covering the full current-students content estate (1,161 deduped pages across 9 faculties + 3 schools + the hub). Each note follows the same structure: intro · distribution table · content-type typology · legitimate-vs-hub-overlapping · recommendation · full per-faculty page-list appendix. Raw per-topic lists are in `_pagelists/`; structured data in `../../data/`.

## The notes (by page count)

| Topic | Pages | Verdict | Headline finding |
|---|--:|---|---|
| [subjects-timetable](subjects-timetable.md) | 319 | mixed | Largest topic, but **64% is ABP/MSD's design-studio archive**; the rest is a thin hub-owned timetabling spine (MyTimetable, census, overloading) echoed by faculties + legit discipline subject catalogues. |
| [orientation](orientation.md) | 289 | inflated | **FEIT holds 204 (71%)** by nesting its whole estate under `/orientation/` paths; genuine orientation is a thin faculty-owned welcome layer. |
| [transactional-admin](transactional-admin.md) | 227 | **hub-owned** | enrolment + exams/results + special-con + fees + library: only **6 of 227 pages sit on the hub domain**; faculty content is restatement/local-wrappers/noise — the estate's clearest consolidation target. |
| [research-candidature](research-candidature.md) | 241 | faculty-owned | Legit (milestones, studios, faculty funding) but inflated by ~70 Law researcher-profile pages; hub-own the candidature lifecycle spine, convert bios to a directory. |
| [it-systems](it-systems.md) | 235 | artefact tag | **78% is mis-classified FEIT** content; genuine ~30–40 pages — faculty-owned only for physical labs/equipment loans; hub owns the Student IT / LMS / portal spine. |
| [student-life](student-life.md) | 214 | faculty-owned | Largely legit (clubs, mentoring, awards, enrichment); ~⅓ is internal bloat (MSD studio archive, Science committee rosters). |
| [forms-admin](forms-admin.md) | 212 | mixed | Concentrated in Law (66) + MDHS (70 pre-placement compliance); faculty forms hubs are legit, but offer-acceptance/enrolment/special-con admin overlaps the hub. |
| [course-planning](course-planning.md) | 207 | faculty-owned | Degree-specific plans dominate; **MBS + Biomedical = 46%**; thin hub-overlapping layer (generic advice, re-hosted My Course Planner). |
| [placements-wil](placements-wil.md) | 206 | **faculty-owned** | MDHS holds 47% (clinical compliance); near-zero hub overlap; the gap is **discoverability** (hub has no WIL front door), not duplication. |
| [contacts-support](contacts-support.md) | 177 | mixed | Most diffuse topic; ~half is Arts+Law restatements of hub wellbeing/equity/careers + duplicate/stub pages. |
| [careers-employability](careers-employability.md) | 141 | mixed | Legit core (regulated pathways, internship subjects, mentoring) beneath a heavily duplicated hub-overlap layer (7 near-identical "Employability in X" pages). *Deeper ESI analysis held separately in the employability workspace.* |
| [scholarships](scholarships.md) | 141 | consolidate | Hub holds zero; FEIT 50%; mostly generic process scaffolding (rounds, T&Cs, FAQs, winner galleries) → consolidate into central `scholarships.unimelb.edu.au`. |
| [international](international.md) | 135 | mislabelled | ~80% is faculty-owned **outbound** mobility (exchange, partnerships); genuine **inbound** support (visas/OSHC/ESOS) is absent and hub-owned. |
| [graduation](graduation.md) | 125 | misnomer | Almost no ceremony content — captures HDR candidature lifecycle + honours/awards; the hub-owned apply-to-graduate spine is missing here. |
| [clubs-events](clubs-events.md) | 104 | faculty-owned | Overwhelmingly faculty community content; only hub overlap is the generic club-admin wrapper + self-duplication. |
| [wellbeing-health](wellbeing-health.md) | 87 | mixed | Half is MDHS clinical-placement compliance (mis-tagged); genuine pastoral content is **6 near-duplicate "Wellbeing + Ambassadors" landings** to collapse into one hub page. |
| [inclusion-equity](inclusion-equity.md) | 49 | consolidate | Noise-heavy (~45% false positives); genuine ~13 pages of Indigenous/equity/disability that parallel-reinvent the central service. |
| [academic-skills](academic-skills.md) | 37 | hub-overlapping | Only discipline-bound skills (legal research, academic English, thesis writing) are legit; generic landings duplicate the central service. |

## ⚠️ Data-quality caveat — topic counts are inflated by classifier artifacts
The full crawl's topic tags carry systematic noise; the **counts overstate real content** and the notes correct for it. Four recurring artifacts:
1. **MSD studio archive** (~700 near-identical past-studio pages) inflates *subjects-timetable* and *student-life*.
2. **FEIT path-nesting** (its whole estate under `/orientation/`, `/students/it…`) inflates *orientation* and *it-systems*.
3. **Law researcher-profile pages** (~70 GRD bios) inflate *research-candidature* and *inclusion-equity*.
4. **Tag mislabelling** — *international* is mostly outbound mobility; *graduation* is mostly HDR lifecycle.

These should be fixed at source (de-archive MSD studios; flatten FEIT path-nesting and URL-churn; convert researcher bios to a directory; fix Biomedical's 16 redirect stubs).

## Cross-cutting takeaways (feed the recommendations)
- **Clearest consolidation targets:** transactional-admin (hub already owns it), scholarships (central catalogue exists), the duplicated "Employability in X" / "Wellbeing + Ambassadors" landings, and contacts-support restatements.
- **Genuinely faculty-owned (do not centralise):** placements/WIL, course plans, research candidature, clubs/events, discipline-specific skills.
- **Real hub gaps:** placements/WIL discovery, inbound international support, the apply-to-graduate spine, a faculty-course-planning gateway.
- **The recurring fix is the same as the estate-wide finding:** connect the seams + trim a thin duplicative layer + fix data-quality artifacts — not relocate the large unique faculty estate.
