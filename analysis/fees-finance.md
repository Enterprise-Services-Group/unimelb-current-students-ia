# Fees & Finance — Deep-Dive

*The financial spine of the student experience — census dates, fee payments, HELP loans, and hardship support. 593 pages across 16 domains, but 62% are on the applicant-facing study.unimelb while only 46 serve enrolled students. The census-dates page canonicalises to /page-not-found. Core answers are outsourced to a legacy FAQ. June 2026.*

---

## Executive summary

Fees and finance is the highest-stakes operational content in the estate. Get a census date wrong and a student pays for a subject they didn't want. Miss a fee deadline and enrolment is cancelled. Can't find hardship support and a student drops out over rent. Yet the financial spine is fractured across three live URL trees on the hub, reverse-funnelled through the applicant-facing study.unimelb (366 pages for applicants vs 46 for enrolled students), and dependent on a legacy ask.unimelb FAQ for the actual answers.

Three acute failures define it:
1. **The census-dates page canonicalises to `/page-not-found`** — the single most financially consequential page tells search engines it doesn't exist.
2. **The reverse-funnel**: 366 fee pages on study.unimelb (for applicants) vs 46 on students.unimelb (for enrolled students) — an 8:1 ratio. Enrolled students searching for fee information are routed to the applicant site.
3. **Financial hardship is ~5 pages with opaque form parameters** — the pathway a fee-stressed student needs most is the hardest to find.

The fix: one canonical "Fees and finance" hub on students.unimelb, fix the census canonical, bring answers back from the FAQ, and build a findable hardship front door.

---

## The fee footprint: where fee content actually lives

| Domain | Pages | Audience | Note |
|---|---|---|---|
| study.unimelb.edu.au | 366 | Applicants | 62% of all fee pages — the reverse-funnel problem |
| law.unimelb.edu.au | 68 | Mixed | Faculty-specific fee content |
| students.unimelb.edu.au | **46** | **Enrolled students** | The hub — but only 8% of fee pages |
| fbe.unimelb.edu.au | 39 | Mixed | Business/economics fees |
| msd.unimelb.edu.au | 18 | Mixed | Architecture/building fees |
| medicine.unimelb.edu.au | 13 | Mixed | Medicine fees |
| Other (10 domains) | 43 | Mixed | Scattered |
| **Total** | **593** | | **8:1 ratio of applicant to enrolled pages** |

---

## The triple-tree duplication on the hub

The hub's 46 enrolled-student fee/finance pages are split across three URL trees — the same mid-migration debt pattern that fractures everything else:

| Tree | Pages | Role |
|---|---|---|
| `/course-admin/` | ~17 | Canonical — fees, census, HELP loans |
| `/your-course/` | ~12 | Legacy — duplicated fee content |
| `/admin/fees` | ~17 | Administrative — payment, sanctions, refunds |

Plus a fourth dimension: `/support-and-wellbeing` hosts the financial-aid/hardship pages (mis-titled "Support and wellbeing"), and `/student-support` hosts legacy copies. A student looking for "how much do I owe" or "when is census" can land on any of 3-4 versions of the same answer.

---

## The three acute failures

### 1. Census-dates page canonicalises to /page-not-found `[HIGH]`

The census date is the deadline that determines whether a student pays for a subject. Withdraw before census and the subject disappears from your record and your fee statement. Withdraw after and you pay full fees and/or take an academic fail. It is the single most financially consequential date in the student lifecycle.

The page at `/course-admin/census-dates` carries `<link rel="canonical" href="/page-not-found">`. The authoritative date page tells search engines — and any tool that respects canonical tags — that it doesn't exist. A student googling "unimelb census date 2026" may never find the real page.

This is a one-line fix. It's been broken through the entire duration of this project. It should have been fixed on day one.

### 2. The reverse-funnel: enrolled students sent to the applicant site `[HIGH]`

366 fee pages live on study.unimelb.edu.au — the applicant-facing recruitment site. These pages explain course fees, HELP loan eligibility, and payment options to *prospective* students. Only 46 fee pages live on students.unimelb.edu.au — the *enrolled* student hub.

An enrolled student searching for "how to pay my fees" or "check my fee statement" lands on study.unimelb pages that assume they haven't applied yet. The content is written for the wrong audience. 363 fee pages on the applicant site vs ~17 on the enrolled hub — a 21:1 ratio in the wrong direction.

The fix recommended in §8a: build a single enrolled-student "Fees and finance" hub that owns payment, census, HELP loans, fee remission, and hardship — and bridge every applicant fee page to it with "Already enrolled? Go here."

### 3. Financial hardship: ~5 pages, opaque forms, buried under wrong titles `[HIGH]`

A student who can't pay rent, fees, or eat needs emergency grants, fee remission, hardship bursaries, or emergency accommodation. What they find:

| Resource | Coverage | Findability |
|---|---|---|
| Financial hardship pages | ~5 on students.unimelb | Buried under "Support and wellbeing" |
| Bursary pages | ~2 | Near-invisible |
| Fee remission form | 1 — forms.your.unimelb.edu.au/4747166 | Three opaque SID query params; no plain-language labels |
| Emergency accommodation | Scattered | No single entry point |
| Food relief | Unknown | No dedicated page found |

The financial-aid page is mis-titled "Support and wellbeing" — not "Financial aid" or "Emergency support." A panicking student searching "financial hardship unimelb" may never find it. The fee-remission form uses indistinguishable SID parameters — a student can't tell which link is for a waiver, which for a review, and which for an enquiry.

---

## The ask.unimelb dependency

Core fee answers — census dates, HELP loan eligibility, fee payment methods, Statement of Liability — live on ask.unimelb.edu.au, a legacy FAQ knowledge base with two inconsistent URL formats. The hub describes the topic; the actual answer is one hop away on an unmaintained system. This is the same pattern as enrolment (396 ask.unimelb links), mirrored in fees.

---

## _nocache URL leakage

15 pages link to _nocache versions of fee/eligibility pages — e.g. the CSP/HELP-loans eligibility page. These are cache-bust artifacts that dilute link equity and create duplicate destinations. A student who bookmarks a _nocache URL gets a URL that may break.

---

## Recommendations

### 1. Fix the census-dates canonical tag `[HIGH · quick-win]`
One-line fix: change `<link rel="canonical" href="/page-not-found">` to the actual page URL. Should have been done on day one. The highest-priority single-page fix in the entire estate.

### 2. Build one enrolled-student "Fees and finance" hub `[HIGH · medium]`
One canonical home on students.unimelb (under /course-admin/) linking out to: pay my fees (my.unimelb), understanding your fees, census dates, FEE-HELP/HECS eligibility, fee remission/refunds, financial aid/hardship, and scholarship payments. Keep study.unimelb fee pages scoped to applicants/cost-to-study. Add "Already enrolled? Go here" bridge from every applicant fee page.

### 3. Build a findable "Financial difficulty / emergency support" front door `[HIGH · medium]`
Consolidate fee remission, payment extensions, hardship grants, emergency loans, and Stop 1 financial advice into one clearly-titled entry point. Link prominently from the fees hub, census page, and paying-your-fees. Label the three fee-remission form actions in plain language. Strip _nocache query-string variants from internal links.

### 4. Migrate core fee answers off ask.unimelb `[HIGH · large]`
Bring census dates, HELP eligibility, fee payment methods, and Statement of Liability answers into the maintained hub pages. Stop describing-then-deferring on the financial core.

### 5. Collapse the triple-tree duplication `[HIGH · medium]`
One canonical fee tree on students.unimelb. 301-redirect the legacy `/your-course/` and `/admin/fees` duplicates. This is part of the hub migration (Improvement #1).

---

## Linked improvements from the register

| § | Improvement | Severity · Effort |
|---|---|---|
| 8a.1 | Collapse the triple-tree URL duplication on core enrolled-student fee pages | HIGH · medium |
| 8a.2 | Fix broken/mismatched metadata on the highest-stakes fee and census pages | HIGH · quick-win |
| 8a.3 | Migrate core fee answers off the legacy ask.unimelb FAQ system into the maintained IA | HIGH · large |
| 8a.4 | Build a single enrolled-student "Fees and finance" hub; stop sending enrolled students to study.unimelb | HIGH · medium |
| 8a.5 | Consolidate the cross-domain census-date duplication into one authoritative source | MEDIUM · quick-win |
| 8a.6 | Surface and strengthen the financial-hardship / emergency-support and fee-remission pathway | MEDIUM · medium |

---

*Built from: fees-finance.csv (593 pages, 16 domains), improvements-register.md (§8a Fees, census dates & finance), course-planning-enrolment.md (census-date canonical finding), cross-site-flow.csv, and crawl/students-full/ (hub fee pages). June 2026.*
