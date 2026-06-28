# Forms & Transactional Microsite Audit

*Every student journey terminates in a form or a walled portal. The public estate describes the action; these hosts ARE the action. 14 distinct *.app microsites plus forms.your (2,044 contextual links) — the hidden operational layer of the University. June 2026.*

---

## Executive summary

The University's web estate has a hidden operational layer: the forms, portals, and transactional microsites where every journey's decisive action happens. These hosts are uncrawlable — behind login walls, JS-injected, or single-purpose form endpoints. But the outbound link graph reveals them clearly: **14 distinct `*.app.unimelb.edu.au` hosts plus `forms.your.unimelb.edu.au`**, collectively referenced by **2,101 contextual links** across the estate.

This audit maps every transactional host, how many links reach it, which journeys depend on it, and which are reachable vs invisible. The key finding: **the most important actions have the fewest links.** Enrolment variations gets 2 links. Counselling bookings gets 3. Special consideration gets 12. Meanwhile the generic forms.your host gets 2,044 — a catch-all that obscures which form does what.

---

## The transactional host inventory

### *.app microsites

| Host | Links | Journey | What it does | Reachable? |
|---|---|---|---|---|
| specialconsideration.app | 12 | At-risk / academic | Apply for special consideration, deferred exams | Behind login |
| tes.app | 11 | Enrolment | Timetable/exam system | Behind login |
| feit-vocational-placement.app | 8 | WIL / placements | FEIT vocational placement system | Behind login |
| enquiry.app | 8 | Prospective / general | General enquiry form | Public? |
| ctrs.app | 6 | Research / HDR | Contract research tracking | Behind login |
| mycounselling.app | 3 | Wellbeing / crisis | **Counselling appointment booking** | Behind login |
| law.app | 2 | Law faculty | Law-specific form/application | Behind login |
| enrolmentvariations.app | 2 | Enrolment | **Reduced study load, leave, withdrawal** | Behind login |
| slidelibrary.app | 1 | Teaching/learning | Slide repository | Behind login |
| thesislibrary.app | 1 | HDR / research | Thesis repository | Behind login |
| booklibrary.app | 1 | Teaching/learning | Book repository | Behind login |
| studenteforms.app | 1 | General | Student e-forms | Behind login |
| ffam-mcm.app | 1 | Fine Arts/Music | MCM application | Behind login |
| **Total *.app** | **58** | | | |

### forms.your.unimelb.edu.au

The catch-all form host: **2,044 contextual links** estate-wide. This single host handles:

- Fee remission forms (SID params: waiver, review, enquiry)
- Leave of absence applications
- Course transfer requests
- Advanced standing applications
- Enrolment variation requests
- Hardship grant applications
- And hundreds more — none labeled in plain language

The 2,044 links obscure which specific forms are linked. The SID query-string parameters are the only differentiator, making it impossible for a student (or this audit) to identify which link does what without clicking through.

---

## The discoverability problem

| Journey action | Links to its form | Verdict |
|---|---|---|
| Fee remission | Opaque SID params in forms.your | Effectively invisible |
| Reduced study load / leave | **2 links** to enrolmentvariations.app | Near-invisible |
| Counselling booking | **3 links** to mycounselling.app | Near-invisible |
| Special consideration | 12 links to specialconsideration.app | Barely discoverable |
| Enrol in subjects | 187 links to my.unimelb (behind login) | Described, not transacted |
| General enquiries | 8 links to enquiry.app | Adequate |

The most consequential actions — changing enrolment, booking counselling — have the fewest links to their transactional hosts. A student in crisis cannot find the counselling booking form; a student needing to reduce study load cannot find the enrolment variation form.

---

## The forms.your opacity

forms.your.unimelb.edu.au is the estate's single largest transactional dependency (2,044 links), but it's a black box:

- **No plain-language labels.** Three fee-remission form links use indistinguishable SID query parameters. A student cannot tell which is for a waiver, which for a review, and which for an enquiry.
- **No inventory.** There is no public directory of forms, no categorisation by journey, no indication of which office processes which form.
- **No status tracking.** Once submitted, a form disappears into a processing queue. The student has no visibility into whether their request was received, who's handling it, or when to expect a response.
- **143 hub pages reference form ID 4747166** — a single form with widespread links, completely undescribed.

---

## The hub's transactional outbound

The hub (students.unimelb) is the primary router to transactional hosts. Its top destinations:

| Destination | Links | What it is |
|---|---|---|
| ask.unimelb.edu.au | 444 | Legacy FAQ — the actual answers |
| services.unimelb.edu.au | 290 | Counselling, health, academic skills |
| forms.your.unimelb.edu.au | 260 | Forms catch-all |
| my.unimelb.edu.au | 187 | SIS — enrolment, results, fees |
| studyos.students.unimelb.edu.au | 79 | My Course Planner |
| safercommunity.unimelb.edu.au | 62 | Safety/crisis |
| q.surveys.unimelb.edu.au | 43 | Surveys |

The hub describes → these hosts transact. But the handoff is never surfaced as a consistent CTA. A student reads about counselling on the hub and must find the mycounselling.app link buried in prose or a sidebar.

---

## Recommendations

### 1. Label every forms.your link in plain language `[HIGH · medium]`
Replace opaque SID-param links with labeled CTAs: "Apply for fee remission (waiver)" / "Request a fee review" / "Submit a hardship enquiry." The 143 instances of form 4747166 should all carry a descriptive label.

### 2. Surface the highest-stakes transactional links prominently `[HIGH · medium]`
Mycounselling.app (3 links), enrolmentvariations.app (2 links), and specialconsideration.app (12 links) should be surfaced as prominent CTAs from their guidance pages — not buried in prose or sidebars.

### 3. Build a forms directory `[MEDIUM · medium]`
A single "Forms and requests" page on the hub, categorised by journey (enrolment, fees, support, careers), linking every form with its plain-language name and expected processing time.

### 4. Add status-tracking to high-consequence forms `[MEDIUM · large]`
Fee remission, leave of absence, and special consideration forms should provide a confirmation page with a reference number, expected processing time, and contact for follow-up. Currently the student submits into a void.

### 5. Audit the 14 *.app hosts for retirement dates `[MEDIUM · medium]`
Every *.app host should have a registered owner, documented purpose, and planned retirement date. Several (slidelibrary, thesislibrary, booklibrary) appear to be legacy single-purpose microsites.

---

*Built from: cross-site-flow.csv (forms + app link audit), improvements-register.md (§5.5 forms registry), and the hub outbound link graph (students.unimelb outbound). June 2026.*
