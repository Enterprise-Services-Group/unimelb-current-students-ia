# Priya — International student navigating 9 stages

> *"I came to Australia for the post-study work visa. But no page on the entire University website mentions the 485 visa. I found my CoE, paid my deposit, got my student visa — and now I'm told I need to stay full-time to keep it, but no one tells me what happens if I drop a subject. Where do I even check?"*

## Bio
Priya is an international postgraduate coursework student from India, studying a 2-year Master of Data Science. She applied through an authorised education agent (mandatory for Indian applicants who completed tertiary studies in India), navigated the conditional CoE process, paid the AUD$17,000 tuition deposit, secured her subclass-500 student visa, and has now commenced her first semester. Her entire legal status in Australia depends on maintaining visa conditions — full-time study load, satisfactory course progress, and work-hour limits — but the estate that describes these conditions never connects them to the enrolment actions that breach them. Everything Priya needs is *described* somewhere; nothing is *wired* to the action.

## Journey pain points

| Pain point | Crawl evidence | Severity |
|---|---|---|
| **CoE/visa/OSHC compliance forked across 3 live trees** | Canonical `/support-and-wellbeing` (27 pages), deprecated `/student-support` (12 pages, linked by 12 domains), AND live `/sandbox/2026-uplifts` draft (10 pages) | HIGH |
| **Highest-risk pages link to zero action forms** | "Manage enrolment changes that affect your visa" and "reduced study load" pages carry zero links to my.unimelb or the *.app forms that action them | HIGH |
| **Post-study work visa (485) has no page anywhere on the estate** | Zero pages reference subclass 485 — the single largest reason international students choose Australia | HIGH |
| **OSHC link targets wrong page** | UG fees page + PG offer page link OSHC to `/healthcare-for-other-visa-types` — not the subclass-500 OSHC page | HIGH |
| **Mandatory-agent rule undiscoverable** | Agent page states India/Pakistan/China must apply through agents; zero in-text anchors link to it; per-course "How to apply" pages never surface the rule | HIGH |
| **ESOS/Tuition Protection invisible at deposit moment** | Deposit page (AUD$17,000 commitment) never links the Tuition Protection Service — zero ESOS links from any offer/acceptance page | HIGH |
| **Agent page duplicated across two URLs** | `/authorised-education-agent` and `/find-an-overseas-representative` are byte-identical — one page, two URLs, split authority | MEDIUM |
| **2025 English requirements still live in 2026** | Year-stamped eligibility page still published and linked from current hub — an applicant can apply against superseded IELTS thresholds | MEDIUM |

## Top frustrations
1. **The most important content is forked across three trees.** Priya's visa picture depends on which fork she lands on — canonical, deprecated, or a live sandbox draft.
2. **The visa condition and the academic action never meet.** "You must stay full-time" is described on a guidance page with no link to the study-load action that keeps her compliant.
3. **The biggest reason she chose Australia doesn't exist on the website.** The post-study work visa (subclass 485) — the primary drawcard for international students — has zero pages.
4. **Her AUD$17,000 deposit has no visible protection.** The Tuition Protection Service, which guarantees her deposit if the provider defaults, is never linked from the payment page.

## Service touchpoints — 9 journey stages
| Stage | System(s) | Key friction |
|---|---|---|
| 1. Discover & decide | study.unimelb /student-life/international-students | Strong hub but sends visa queries to deprecated tree |
| 2. Eligibility & English | study.unimelb /how-to-apply | 2025 thresholds still live; case-by-case has no SLA |
| 3. Application & agents | study.unimelb + AscentOne agent directory | Mandatory agent rule undiscoverable; portal seam invisible |
| 4. Offer & deposit | study.unimelb /fees-and-payments | AUD$17,000 — no ESOS link at commitment point |
| 5. CoE (conditional → full) | eStudent (walled) + study.unimelb | Conditional CoE agent-gated; conversion page missing |
| 6. Student visa (subclass 500) | students.unimelb (3 trees) + Home Affairs | Conditions described, never wired to action forms |
| 7. Arrival & enrolment | my.unimelb (behind login) | Public estate only describes enrolment |
| 8. Ongoing compliance | students.unimelb + my.unimelb | Study-load change invisible at enrolment moment |
| 9. Post-study / alumni | www.unimelb/alumni (~97 links) | Graduation→alumni severed; 485 visa absent |

## Systems traversed
~8: study.unimelb → eStudent portal (auth) → my.unimelb → students.unimelb (3 visa trees) → services.unimelb → forms.your → faculty → www.unimelb/alumni

## Linked improvements from the register
| # | Improvement | Severity · Effort |
|---|---|---|
| 1 | Finish the stalled hub migration & collapse parallel URL trees | HIGH · medium |
| — | Designate ONE canonical visa/compliance tree; 301 deprecated + unpublish sandbox | HIGH · medium |
| — | Wire visa-condition pages to enrolment action forms | HIGH · medium |
| — | Build the subclass-485 post-study work visa page | HIGH · medium |
| — | Fix OSHC link targets; surface ESOS at deposit point | HIGH · quick-win |

## Related deep-dives
- `analysis/international-student-experience.md` — full 9-stage audit
- `analysis/lifecycle-journeys.md` — International postgraduate journey trace
- `report/International-Student-Experience.html` — formatted report

---

*Built from: international-student-experience.md (full 9-stage audit), lifecycle-journeys.md, improvements-register.md, theydo_export/insights.csv and opportunities.csv. June 2026.*
