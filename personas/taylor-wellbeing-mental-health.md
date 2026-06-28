# Taylor — Wellbeing & mental health crisis

> *"I searched 'mental health support' on the student hub and got a page about academic skills. I clicked through three more pages before I found counselling. By then I'd already given up and called a friend instead."*

## Bio
Taylor is a third-year undergraduate who has been struggling with anxiety and depression throughout the semester. After missing two assignment deadlines and receiving a concerning email from their subject coordinator, Taylor decides to seek help. They navigate to students.unimelb, search for "mental health," and land on a page whose dominant brand signal is "Academic Skills Unit" — not "Counselling." The service exists (counselling, health, and safer community are all real, funded services) but Taylor must route through 3–4 hosts with inconsistent labels before reaching the right one. This is the journey where the estate's fragmentation costs the most: a student in crisis has the least margin to hunt across systems.

## Journey pain points

| Pain point | Crawl evidence | Severity |
|---|---|---|
| **Counselling delivery is off-brand** | services.unimelb branded "Academic Skills Unit" (614× anchor mentions) vs "Counselling" (39×) | HIGH |
| **Wellbeing support forked across parallel hub trees** | `/support-and-wellbeing` (canonical, 152 pages) vs `/student-support` (deprecated, 80+ pages, linked by 12 domains) | HIGH |
| **Student crosses 3-4 hosts to reach help** | students.unimelb → services.unimelb → safercommunity.unimelb → safety.unimelb | HIGH |
| **Financial hardship support is ~5 pages** | Thin for the cohort most likely to need it — request funnels into one opaque form | HIGH |
| **Special consideration scattered behind walls** | Content across trees and faculties; application at specialconsideration.app / my.unimelb | MEDIUM |
| **Safer community on separate uncrawled domain** | safercommunity.unimelb — critical safety service with zero presence on the main hub | MEDIUM |
| **No unified "I need help now" front door** | Support scattered across counselling, health, safety, financial, academic progress — no single crisis entry | HIGH |

## Top frustrations
1. **Counselling is hiding behind the wrong label.** The wellbeing link lands on a page dominated by "Academic Skills Unit" branding — Taylor doesn't know they've found the counselling service.
2. **Two competing versions of support exist.** The deprecated `/student-support` tree is still live and still linked by 12 external domains — Taylor may read the wrong, outdated version.
3. **The crisis services are on a completely separate domain.** Safer community and safety services live on uncrawled domains with no reciprocal linking from the main hub.
4. **Financial help is near-invisible.** Five pages for the cohort most likely to need emergency financial support — and the request path is an opaque form with SID parameters.

## Service touchpoints
| Touchpoint | Where it lives | What's wrong |
|---|---|---|
| Mental health / counselling | services.unimelb /counsel | Off-brand — labeled "Academic Skills Unit" 16× more than "Counselling" |
| Health services | services.unimelb /health | Separate from counselling; no unified wellbeing home |
| Safer community | safercommunity.unimelb | Separate uncrawled domain; zero presence on main hub |
| Safety / emergency | safety.unimelb | Another separate domain |
| Financial hardship | students.unimelb (~5 pages) | Thin; opaque form with SID params |
| Special consideration | specialconsideration.app / my.unimelb | Behind wall; content scattered |
| Academic progress | students.unimelb (2 trees) | Competing content across parallel URL trees |
| Disability support (SEDS) | students.unimelb (3 trees) | Registration wizard exists on only 1 of 3 trees — 12 domains link the 2 that lack it |

## The wellbeing footprint
| Component | Pages | Note |
|---|---|---|
| Hub front door (canonical) | 152 raw / 109 unique | Genuine router — fans out to providers |
| Hub legacy tree | ~80 pages | Deprecated but still linked by 12 domains |
| Counselling delivery | ~100 pages (services.unimelb) | Off-brand host |
| Health delivery | ~20 pages (services.unimelb) | Separate from counselling |
| Faculty wellbeing stubs | ~41 pages | Scattered across education, law, science, fbe, eng |
| **True current-student footprint** | **~244 unique paths** | After filtering 1,488 medical-school false positives + 428 study.unimelb prospective |

## Systems traversed
~6: students.unimelb (2-3 trees) → services.unimelb → specialconsideration.app → my.unimelb → safercommunity.unimelb → forms.your

## Linked improvements from the register
| # | Improvement | Severity · Effort |
|---|---|---|
| 1 | Finish the stalled hub migration & collapse parallel URL trees | HIGH · medium |
| — | Build one "I need help now" front door collapsing parallel trees | HIGH · medium |
| — | Rebrand services.unimelb counselling pages to be findable as "Counselling" | MEDIUM · quick-win |
| — | Surface safer community from the main hub with reciprocal linking | MEDIUM · medium |

## Related deep-dives
- `analysis/student-services-fragmentation.md` — wellbeing service audit
- `analysis/student-services-profiles.json` — wellbeing, health & safety profile
- `analysis/lifecycle-journeys.md` — At-risk student journey trace
- `report/Student-Services-Fragmentation.html` — formatted report

---

*Built from: student-services-profiles.json (wellbeing profile — 244 true current-student paths), lifecycle-journeys.md, improvements-register.md, and the full-scrape link graph. June 2026.*
