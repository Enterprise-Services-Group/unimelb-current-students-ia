# The Authenticated Core — Seam Audit

*The walled systems where every student journey's decisive action happens. 42 authenticated hosts, 3,641 contextual links from the public estate. The public side describes; the authenticated side transacts. This audit maps the seam — what students see before they click, which journeys depend on which systems, and what we can verify without login access. June 2026.*

---

## Executive summary

The public estate describes enrolment, payment, counselling booking, special consideration, and visa compliance — but the actual action happens behind 42 distinct authenticated hosts. The public→authenticated seam is where the student experience either works or breaks, and it's the one layer this project cannot crawl.

Three findings define the seam:

1. **The links exist but the labels are generic.** "my.unimelb" appears 18 times in 200 hub pages as link text. "Go to my.unimelb to enrol" appears twice. The specific action the student needs to perform is described in prose but the link text itself is a generic system name. Students know *where* to go but not *what to do* when they get there.

2. **forms.your is a black box with 84 indistinguishable links.** "Enquiry," "Enquiry (recommended)," "Submit an enquiry" are the dominant labels. Fee remission, leave of absence, course transfer — all funneled through the same generic form host with SID query parameters as the only differentiator. A student cannot tell which form does what.

3. **The counterexample proves the pattern.** "Apply for special consideration" is the only consistently action-labeled link to an authenticated host. It appears twice — and both times the label says exactly what it does. Every other authenticated link should follow this pattern.

---

## The authenticated host inventory — 42 systems

### Tier 1 — Core transactional (every student journey)

| Host | Links | Sources | What it does | Link label quality |
|---|---|---|---|---|
| **my.unimelb.edu.au** | 237 | 10 | SIS — enrol, results, fees, timetable, study plan | ⚠ Generic: "my.unimelb," "Go to my.unimelb" |
| **forms.your.unimelb.edu.au** | 2,044 | 19 | Fee remission, leave, withdrawal, course transfer, hardship | ❌ Indistinguishable: "Enquiry," "Enquiry (recommended)" |
| **lms.unimelb.edu.au** | 148 | 12 | Canvas/LMS — learning materials, assignments | ⚠ Generic: "log in to the LMS" |
| **canvas.lms.unimelb.edu.au** | 115 | 15 | Canvas direct — quizzes, modules | ⚠ Generic: "LMS quiz," "Open module on LMS" |
| **studyos.students.unimelb.edu.au** | 168 | 6 | My Course Planner — subject planning | ❌ Generic: "Log back in," "Summer," "Winter" |
| **mytimetable.students.unimelb.edu.au** | 10 | 2 | Class timetabling | ⚠ Too few links to assess |

### Tier 2 — Journey-specific (one or two personas)

| Host | Links | What it does | Which persona |
|---|---|---|---|
| **specialconsideration.app** | 12 | Apply for special consideration, deferred exams | Alex (at-risk), Taylor (wellbeing) |
| **enrolmentvariations.app** | 2 | Reduced study load, leave, withdrawal | Alex, Priya |
| **mycounselling.app** | 3 | Counselling appointment booking | Taylor |
| **tes.app** | 11 | Thesis examination system | HDR candidate |
| **feit-vocational-placement.app** | 8 | FEIT vocational placements | Jordan |
| **enquiry.app** | 8 | General enquiry form | All |
| **intlstudaccept.unimelb.edu.au** | 3 | International student acceptance | Priya |
| **overseasstudyplanner.unimelb.edu.au** | 6 | Study abroad planner | Sam |
| **course-planner.unimelb.edu.au** | 10 | Legacy course planner | Sam, Jordan |

### Tier 3 — Administrative / non-student

| Host | Links | What it does |
|---|---|---|
| **q.surveys.unimelb.edu.au** | 231 | Survey platform — course evaluations, research |
| **ecommerce.unimelb.edu.au** | 191 | Payment gateway — fees, sport memberships |
| **go.unimelb.edu.au** | 175 | URL shortener/redirect |
| **your.unimelb.edu.au** | 102 | Staff/student portal redirect |
| **accounts.unimelb.edu.au** | 21 | Account management |
| **catalog.lms.unimelb.edu.au** | 81 | LMS course catalogue — Melbourne Plus, communities |
| **my.unilife.unimelb.edu.au** | 10 | Student life portal |

### Tier 4 — Legacy / single-purpose (1-2 links)

| Host | Links |
|---|---|
| slidelibrary.app, thesislibrary.app, booklibrary.app | 1 each |
| studenteforms.app, ffam-mcm.app, law.app | 1-2 each |
| casemanagementform.unimelb.edu.au | 5 |
| feerefundform.unimelb.edu.au | 4 |
| student-advising-system.unimelb.edu.au | 2 |
| coursesearch.unimelb.edu.au | 2 |
| portal.unimelb.edu.au | 3 |
| sis.unimelb.edu.au | 3 |
| prod.ss.unimelb.edu.au | 3 (the eStudent eApplications portal) |
| myuniapps.unimelb.edu.au | 2 |

---

## The link-label problem: what students see before they click

### my.unimelb (237 links, 10 sources)

| Label | Count (in 200 hub pages) | Verdict |
|---|---|---|
| "my.unimelb" | 18 | Generic — student doesn't know what to do there |
| "my.unimelb admin pages" | 7 | Vague |
| "Go to my.unimelb" | 4 | Generic |
| "Log in to my.unimelb" | 2 | Generic |
| "Go to my.unimelb to enrol" | 2 | **Specific — the pattern to follow** |
| "my.unimelb (student portal)" | 2 | Generic |

**The problem:** 237 links to the SIS, but only 2 tell the student what to do there. The prose describes "enrol in subjects," "check your results," "pay your fees" — but the link text is always "my.unimelb." The student arrives at the SIS homepage with no context for what action to take.

### forms.your (2,044 links, 19 sources)

| Label | Count | Verdict |
|---|---|---|
| "Enquiry" | 12 | Completely generic |
| "Enquiry (recommended)" | 8 | Completely generic |
| "Submit an enquiry" | 5 | Completely generic |
| "Enquiry (3-5 business days)" | 5 | Adds timing, still generic |
| "Get help with your student card form" | 2 | **Specific — the pattern to follow** |

**The problem:** 2,044 links to the form host. Nearly all labeled "Enquiry." Fee remission, leave of absence, course transfer, hardship grant — every high-stakes form uses the same generic label. The SID query parameter is the only differentiator: `?SID=...fbZ` (waiver) vs `?SID=...fdB` (review) vs `?SID=...fZx` (enquiry). A student cannot distinguish them.

### The counterexample: specialconsideration.app

| Label | Count |
|---|---|
| "Apply for special consideration" | 2 |

Only 2 links, but both are perfectly labeled. This proves the pattern exists in the estate — the other hosts just don't use it.

---

## Journey seam map: which personas depend on which walls

| Journey step | Public page describes | Authenticated host transacts | Link label | Find→act gap |
|---|---|---|---|---|
| **Enrol in subjects** | Hub /course-admin (343 pages) | my.unimelb /sone/STUDYPLN | "my.unimelb" | ⚠ Described, not directed |
| **Plan course** | Hub /course-admin | studyos.students (My Course Planner) | "Log back in" | ❌ Generic label, two tools |
| **Check results** | Hub | my.unimelb | "my.unimelb" | ⚠ Generic |
| **Pay fees** | Hub /admin/fees | my.unimelb + ecommerce | "my.unimelb" | ⚠ Generic |
| **Timetable** | Hub /class-timetable | mytimetable.students | — | ⚠ Separate subdomain |
| **Special consideration** | Hub /support-and-wellbeing | specialconsideration.app | "Apply for special consideration" | ✅ Labeled correctly |
| **Counselling booking** | services.unimelb /counsel | mycounselling.app | — | ❌ 3 links, buried in prose |
| **Fee remission** | Hub /admin/fees | forms.your + SID params | "Enquiry" | ❌ Indistinguishable |
| **Leave of absence** | Hub | forms.your / enrolmentvariations.app | "Enquiry" | ❌ Indistinguishable |
| **Academic progress** | Hub /course-admin | my.unimelb | "my.unimelb" | ⚠ Generic |
| **Accept international offer** | study.unimelb | eStudent / prod.ss | — | ❌ JS-injected, invisible to link graph |
| **CoE / visa compliance** | Hub (3 trees) | my.unimelb | "my.unimelb" | ❌ Highest-risk pages link 0 forms |
| **Graduate / complete** | Hub | my.unimelb | "my.unimelb" | ⚠ Generic |
| **Access learning materials** | Hub | lms / canvas | "log in to the LMS" | ⚠ Generic |
| **Book sport** | sport.unimelb | ecommerce.unimelb | "Join," "Book," "Register" | ✅ Sport is the exemplar |

---

## What we can verify without login access

| Claim | Verifiable? | How |
|---|---|---|
| "The link goes to the right system" | ✅ Yes | Outbound link audit confirms destinations |
| "The link text says what the action is" | ✅ Yes | Link text audit above — mostly ❌ |
| "The form works after login" | ❌ No | Behind authentication wall |
| "The logged-in side guides the next step" | ❌ No | Cannot see post-login UI |
| "The form has plain-language labels" | ❌ No | SID params are opaque from outside |
| "Confirmation and tracking exist" | ❌ No | Cannot submit forms |
| "The my.unimelb dashboard routes to the right task" | ❌ No | Post-login IA is invisible |
| "The SIS shows the same data as the public page described" | ❌ No | Requires authenticated access |

---

## Recommendations

### 1. Label every authenticated link with the action it performs `[HIGH · medium]`

Replace "my.unimelb" with "Enrol in subjects in my.unimelb." Replace "Enquiry" with "Apply for fee remission," "Request leave of absence," "Submit a hardship enquiry." Use the specialconsideration.app pattern: verb + noun + system name.

### 2. Route forms.your links through a descriptive intermediary `[HIGH · medium]`

Build a "Forms and requests" page on the hub that lists every form with its plain-language name, expected processing time, and status tracking. Link to this page instead of directly to SID-param URLs. This makes the 2,044 indistinguishable "Enquiry" links into one clear "Find the right form" CTA.

### 3. Add a "What you'll do there" preview to authenticated links `[MEDIUM · medium]`

Every link to my.unimelb should include a one-line preview: "You'll enrol in subjects, check your timetable, and pay fees." Students shouldn't have to cross the login wall to discover what's on the other side.

### 4. Walk through the authenticated core with real credentials `[HIGH · validation]`

Request a walkthrough of: my.unimelb enrolment flow, special consideration form, counselling booking, fee remission form, CoE/visa compliance in the SIS. Every "the public side describes; confirm the logged-in side guides" claim in this project depends on this validation.

### 5. Add analytics tracking to authenticated link clicks `[MEDIUM · medium]`

Currently we can't measure which links students actually click. The 2,044 forms.your links are invisible to analytics. Add click-tracking to every authenticated outbound link so journey drop-off can be measured.

---

*Built from: cross-site-flow.csv (42 auth hosts, 3,641 links), links.json sampling (200 hub pages for link text), forms-microsite-audit.md, and the 5 persona journey traces. June 2026.*
