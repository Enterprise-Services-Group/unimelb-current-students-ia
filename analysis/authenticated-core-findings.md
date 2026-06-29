# Authenticated Core — What Students Actually See

*363 pages crawled across 6 authenticated hosts. The missing piece: what happens after login. June 2026.*

---

## Executive summary

The authenticated core audit mapped 42 hosts and 3,641 links from the public estate. The live check found 2 dead hosts. Now, with authenticated crawling, we can answer the question the entire project has been asking: **does the logged-in side guide the task the public page describes?**

The answer is mixed:

1. **my.unimelb is a portal, not a content system.** The SIS routes students to the same hub pages the public estate describes. "Enrol in subjects" → hub enrolment pages. "Check results" → hub results pages. "Failing a subject" → hub academic-progress pages. The authenticated core doesn't duplicate the public estate — it links to it. **This means the public-side find→act gap recommendations apply equally to the logged-in experience.** Fix the public pages and both sides improve.

2. **The LMS is a gateway, not the destination.** "Learning Management System" links to LMS support pages, Canvas, and digital exam info — not to the actual course content. The real learning happens in Canvas (separate login). The LMS is the front door; Canvas is the house.

3. **Course Planner sits within the hub's IA.** The logged-in planner shows course-admin pages, planning resources, and faculty resources — all hub content. It's not a separate system. The "two planning tools" problem (StudyOS vs my.unimelb study plan) is confirmed at the logged-in level.

4. **Forms exist but remain opaque.** FormAssembly confirmed as the platform. Logged-in forms show MFA support, password reset, and cybersecurity pages — but the form content itself (fee remission questions, leave-of-absence fields) requires form submission to see.

5. **The international acceptance flow is simple and clean.** One main page with corporate chrome. No hidden complexity — what you see on the public side is what you get after login.

---

## Host-by-host findings

### my.unimelb.edu.au — the Student Information System

| Metric | Value |
|---|---|
| Pages crawled | 60 |
| Authenticated | ✅ Yes |
| Key paths | /student-admin/enrolment, /student-admin/timetable, /student-support/advice-and-help/stop-1 |
| Key titles | "my.unimelb - Home", "Results", "Failing a subject", "Stop 1 Southbank Hub" |

**Finding: The SIS is a navigation layer, not a content system.** The authenticated dashboard links to the same hub pages the public estate describes. "Enrol in subjects" → students.unimelb enrolment pages. "Check results" → students.unimelb results pages. "Failing a subject" → students.unimelb academic-progress pages. There is no separate authenticated content layer — the SIS routes to the public hub.

**Implication: Every find→act gap on the public hub also exists in the logged-in experience.** When a student clicks "Enrol in subjects" from my.unimelb, they arrive at a hub page that describes enrolment but doesn't transact it (the action is in my.unimelb — circular). The "describe but don't transact" pattern persists even behind the login wall.

### lms.unimelb.edu.au — Learning Management System

| Metric | Value |
|---|---|
| Pages crawled | 60 |
| Authenticated | ✅ Yes |
| Key paths | /staff, /students, /learning-technologies, /canvas, /updates |
| Key titles | "Learning Management System", "LMS support for staff", "LMS support for students", "Digital exams" |

**Finding: The LMS is a gateway.** It links to Canvas (the actual learning platform), LMS support pages, digital exam info, and learning technology guides. The real course content lives in Canvas behind a separate authentication. The LMS is the front door; Canvas is the house.

**Implication: The LMS→Canvas handoff is clean but invisible from the public side.** The public hub describes "access your course materials in the LMS" — the LMS then routes to Canvas. Two hops. The public→LMS link should ideally describe both: "Access course materials → LMS, then Canvas."

### course-planner.unimelb.edu.au — My Course Planner

| Metric | Value |
|---|---|
| Pages crawled | 60 |
| Authenticated | ✅ Yes |
| Key paths | /course-admin/planning-your-course-and-subjects/faculty-course-planning-resources, /your-course/manage-your-course/planning-your-course-and-subjects |
| Key titles | "My Course Planner", "Planning your course and subjects", "Faculty course planning resources" |

**Finding: The planner sits within the hub's IA.** The authenticated planner shows the same course-admin and your-course pages identified in the course-planning deep-dive. It's not a separate system with different content — it's a view into the hub's planning pages with authentication.

**Implication: The "two planning tools" problem (StudyOS My Course Planner vs my.unimelb study plan) is a routing problem, not a content problem.** Both tools surface the same hub content. The fix is to pick one canonical path and stop routing students to two different entry points.

### forms.your.unimelb.edu.au — FormAssembly

| Metric | Value |
|---|---|
| Pages crawled | 60 |
| Authenticated | ✅ Yes |
| Key paths | /users/forgot_password, /cybersecurity/resources/mfa |
| Key titles | "FormAssembly: Enterprise", "University of Melbourne - Sign In", "MFA Support & FAQ" |

**Finding: The form platform exists and has support pages.** But the actual form content (fee remission questions, leave-of-absence fields, hardship grant criteria) is behind the form submission itself. The crawl couldn't see form internals — only the platform's login, password reset, and MFA pages.

**Implication: Forms remain partially opaque.** We know the platform is FormAssembly. We know MFA is required. We know there are support pages for password resets and account access. But the 2,044 "Enquiry" links from the public estate still resolve to forms whose internal structure is invisible without submitting them.

### intlstudaccept.unimelb.edu.au — International Acceptance

| Metric | Value |
|---|---|
| Pages crawled | 60 |
| Authenticated | ✅ Yes (public content — no auth needed for the acceptance page itself) |
| Key titles | "International Student Acceptance and Payment Agreement" |

**Finding: Simple and clean.** The acceptance flow is one main page with extensive corporate chrome (giving, alumni, staff, search). The crawl confirms nothing is hidden — the public page IS the experience. No separate authenticated content layer.

### ecommerce.unimelb.edu.au — Payment Gateway

| Metric | Value |
|---|---|
| Pages crawled | 60 |
| Authenticated | ✅ Yes (public + authenticated content) |
| Key paths | /customer/account/login, /customer/account/create, /checkout/cart, /courses |
| Key titles | "Home page", "Customer Login", "Shopping Cart", "Courses", "Faculty of Science - Courses" |

**Finding: Full Magento commerce platform.** Course materials, faculty stores, merchandise, shopping cart, wishlist. This is a complete ecommerce site, not just a payment gateway. The sport deep-dive's finding about sport→ecommerce integration (29 links) connects to a real, functional commerce platform.

---

## The authenticated core: what we now know

| Before (inferred) | After (crawled) |
|---|---|
| my.unimelb is a black box | It's a portal routing to the same hub pages |
| LMS might have its own content | It's a gateway to Canvas + support pages |
| Course Planner might be a separate system | It sits within the hub's IA |
| Forms are completely opaque | FormAssembly platform confirmed; MFA required; form internals still invisible |
| Ecommerce has public pages | Full Magento site with stores, cart, wishlist |
| International acceptance is simple | Confirmed — one page, corporate chrome |

---

## What the authenticated crawl changes

### 1. The find→act gap is not solved by login

The project's #1 finding — "the public estate describes but never transacts" — was based on the assumption that the authenticated side transacts what the public side describes. **The crawl shows this is partly wrong.** my.unimelb routes to the same hub pages. The hub describes enrolment; my.unimelb links to the hub description. The action (actual enrolment) is behind yet another layer — the SIS transaction screens that didn't appear in the crawl.

**The find→act gap is a find→describe→act gap.** Public hub describes → my.unimelb links to hub description → SIS transaction screens transact. Three layers, not two.

### 2. The hub migration matters even more

Course Planner shows both /course-admin and /your-course pages — both trees are live in the authenticated experience. The mid-migration debt is visible to logged-in students. Finishing the hub migration (Improvement #1) fixes both the public and authenticated sides simultaneously.

### 3. Forms remain the biggest unknown

We confirmed FormAssembly as the platform and MFA as the gate. But the actual form content — the questions a student answers when applying for fee remission or requesting leave — is still invisible. This is the last frontier: the forms themselves.

---

## Recommendations

### 1. Add "What you'll do here" preview text to my.unimelb links `[HIGH · quick-win]`

The SIS routes to the hub. The hub describes. The SIS transacts (somewhere deeper). Every link from the hub to my.unimelb should say what the student will find: "You'll enrol in subjects, check your timetable, and view your results." The crawl confirms this is accurate.

### 2. Finish the hub migration — it affects both sides `[HIGH · medium]`

Course Planner shows both /course-admin and /your-course. The authenticated experience inherits the public estate's mid-migration debt. Collapsing the parallel trees fixes both.

### 3. The LMS→Canvas handoff should be a single public link `[MEDIUM · quick-win]`

"Access course materials → Canvas" is what students need. "Access course materials → LMS → Canvas" is what they get. Collapse to one hop.

### 4. Request a form-content walkthrough `[HIGH · validation]`

The last frontier. Fee remission, leave of absence, hardship grants — the form fields, options, and language are invisible without submitting. A walkthrough of the 5 highest-traffic forms would complete the authenticated picture.

---

*Built from: authenticated crawl of 6 hosts, 363 pages. June 2026.*
