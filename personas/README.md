# Persona Profiles — Current Students IA

Five personas synthesised from the full-scrape link graph, deep-dive analyses, lifecycle journey traces, and the ~75-item improvements register. Each persona represents a real journey through the University's 20-domain web estate, grounded in crawl evidence.

| Persona | Journey | Severity | Key insight |
|---|---|---|---|
| [Sam — Planning their path](sam-planning-their-path.md) | Course planning & enrolment | HIGH | 7 systems to plan one semester; census page → 404 |
| [Alex — At-risk & withdrawal](alex-at-risk-withdrawal.md) | Academic difficulty → support seeking | HIGH | Counselling branded "Academic Skills Unit"; withdrawal page broken |
| [Priya — International student](priya-international-student.md) | 9-stage international journey | HIGH | Visa conditions described, never wired to actions; 485 visa absent |
| [Jordan — Course planning maze](jordan-course-planning-maze.md) | Enrolment toolchain navigation | HIGH | 41% of hub pages for this task; most fragmented single journey |
| [Taylor — Wellbeing & crisis](taylor-wellbeing-mental-health.md) | Mental health help-seeking | HIGH | 3-4 hosts to reach help; off-brand delivery host |

## Cross-cutting patterns

All five personas share four patterns that emerge from the evidence:

1. **The decisive action is always behind a wall.** Enrol, pay, book, submit — every journey's critical step terminates in my.unimelb, eStudent, or a *.app form. The public estate describes; never transacts.
2. **The hub competes with itself.** Mid-migration parallel trees (`/student-support` vs `/support-and-wellbeing`, `/your-course` vs `/course-admin`) fork the journey mid-stride — and 12 domains still link the deprecated trees.
3. **The joints between stages are broken.** The transitions — apply→enrol, complete→graduate, graduate→alumni — are the thinnest links in the chain.
4. **Fragmentation is regressive.** The international, at-risk, and equity journeys break hardest — the students with the least margin to hunt across 5-8 systems pay the highest cost.

## Evidence base

- **Crawl:** 38,331 pages across 20 domains, 261,652 contextual links
- **Deep-dives:** Course planning & enrolment (343 hub pages), International student experience (9 stages), Student services fragmentation (wellbeing profile), Lifecycle journeys (6 personas + 4 moments)
- **Improvements register:** ~75 actionable items with severity, effort, and evidence citations
- **TheyDo export:** insights.csv (10 pain points), opportunities.csv (4 HMWs), journeys.csv (1 L2 journey)

## Outputs

- `personas/*.md` — full persona profiles with pain points, service touchpoints, system traces, and linked improvements
- `theydo_export/personas.csv` — machine-readable CSV with all 5 personas
- `analysis/improvements-register.md` — ~75 improvements with per-item evidence citations
- `report/` — formatted HTML/PDF/PPTX outputs for each deep-dive

---

*June 2026. Built from the full-scrape evidence pack.*
