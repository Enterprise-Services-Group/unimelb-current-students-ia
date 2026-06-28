# Alex — At-risk & considering withdrawal

> *"I'm failing a subject and I think I might need to drop out. I searched 'academic progress' and found two different pages. One says 'at risk' means a warning. The other says something different. I just need to know what happens next and who to talk to."*

## Bio
Alex is a second-year domestic coursework student who has hit academic difficulty for the first time. They failed one subject last semester, are struggling in another, and received an "at risk" notification through my.unimelb. Alex is now in a high-stakes help-seeking spiral: they need to understand unsatisfactory progress rules, possibly apply for special consideration, find wellbeing support, check whether withdrawing affects their HELP loan, and decide whether to take a leave of absence. Every one of these tasks lives on a different system, several on off-brand hosts, and the most panic-critical action — census-date withdrawal — has a canonical URL that points to `/page-not-found`.

## Journey pain points

| Pain point | Crawl evidence | Severity |
|---|---|---|
| **Support is split across parallel hub trees** — a panicking student hits two competing versions of the same help | 24 leaf pages dual-served under `/student-support` AND `/support-and-wellbeing`; old Stop 1 linked 1,648× vs 224× new | HIGH |
| **Counselling delivery is off-brand** — services.unimelb branded "Academic Skills Unit" (614×) far more than "Counselling" (39×) | The wellbeing link lands on a page whose dominant brand signal is academic skills, not mental health | HIGH |
| **Special consideration is scattered and behind a wall** | Content spread across trees and faculties; application at specialconsideration.app / my.unimelb | HIGH |
| **Census-date page canonicalises to 404** | `/course-admin/census-dates` → `/page-not-found` — the withdrawal consequence is invisible | HIGH |
| **Financial hardship support is ~5 pages** | Thin for the cohort most likely to need it | HIGH |
| **Every decisive action is behind login** | Special con, leave, withdrawal, counselling booking — all walled | MEDIUM |
| **Student crosses 5–6 hosts in one help-seeking episode** | students.unimelb (2-3 trees) → services.unimelb → specialconsideration.app → my.unimelb → safercommunity.unimelb → forms.your | MEDIUM |

## Top frustrations
1. **Two competing versions of "support."** Alex searches for help and lands on a deprecated `/student-support` page linked by 12 domains — different content from the canonical `/support-and-wellbeing` tree.
2. **Counselling isn't where it says it is.** The wellbeing page routes to a service host branded "Academic Skills Unit" — a student in crisis may not recognise they've arrived at the right place.
3. **The census-date page is broken.** If Alex decides to withdraw, the deadline page that determines the financial and academic consequence canonicalises to `/page-not-found`.
4. **Everything requires another login.** Special consideration, counselling booking, leave of absence — every action is behind a different authentication wall with no unified status view.

## Service touchpoints
| Touchpoint | System | Current state |
|---|---|---|
| Academic progress check | students.unimelb (2 parallel trees) | Competing content; legacy tree linked by 12 domains |
| Special consideration | specialconsideration.app / my.unimelb | Application behind wall; guidance scattered |
| Counselling & health | services.unimelb /counsel + /health | Off-brand host; dominant label is "Academic Skills" |
| Financial hardship | students.unimelb (~5 pages) | Thin; request funnels into opaque form |
| Leave of absence | forms.your.unimelb | Separate form, separate host |
| Withdrawal / census | students.unimelb → /page-not-found | Broken canonical; consequence invisible |
| Safety/crisis | safercommunity.unimelb | Separate uncrawled domain |

## Systems traversed
~6: students.unimelb (2-3 trees) → services.unimelb → specialconsideration.app → my.unimelb → safercommunity.unimelb → forms.your

## Linked improvements from the register
| # | Improvement | Severity · Effort |
|---|---|---|
| 1 | Finish the stalled hub migration & collapse parallel URL trees | HIGH · medium |
| 7 | Build the graduation→alumni bridge | HIGH · quick-win |
| — | Consolidate wellbeing/support behind one "I need help now" front door | HIGH · medium |

## Related deep-dives
- `analysis/student-services-fragmentation.md` — wellbeing service audit
- `analysis/student-services-profiles.json` — wellbeing, health & safety service profile
- `analysis/lifecycle-journeys.md` — At-risk student journey trace
- `report/Student-Services-Fragmentation.html` — formatted report

---

*Built from: lifecycle-journeys.md, student-services-profiles.json (wellbeing profile), improvements-register.md, and the full-scrape link graph. June 2026.*
