# Alumni ↔ Current-Student Overlap Zones — Deep Dive

Sourced from: `crawl/pages/alumni-unimelb.json` (116 pages, crawled 2026-06-20)

---

## 1. Careers: Three Competing Lanes

### What exists on the alumni site

The alumni careers footprint is substantial and internally doubled:

| Path | Page title | Words |
|---|---|---|
| `/alumni/support-resources/career-support` | Career support for alumni | 1,119 |
| `/alumni/support-resources/career-support/career-tools` | Career tools for alumni | 1,289 |
| `/alumni/support-resources/career-support/career-tools/insights/job-applications` | Job applications career insights | ~800 |
| `/alumni/support-resources/career-support/career-tools/insights/the-future-of-health-careers` | Future of health careers | ~750 |
| `/alumni/support-resources/career-support/career-tools/insights/your-career-going-global` | Your career going global | ~780 |
| `/alumni/benefits/professional-development` | Professional development benefits for alumni | 609 |
| `/alumni/benefits/professional-development/career-tools` | Career tools (under benefits) | ~600 |
| `/alumni/benefits/professional-development/professional-development-courses` | PD courses | ~580 |
| `/alumni/benefits/professional-development/language-learning` | Language learning | ~650 |
| `/alumni/benefits/professional-development/online-journal-access` | Online journal access | 1,038 |

The alumni site has **two separate "career tools" pages** — one under `/support-resources/career-support/` and one under `/benefits/professional-development/` — without evident differentiation.

### What the current-student estate offers

The central Careers service at `students.unimelb.edu.au` (and its per-faculty equivalents) provides:
- Career appointments, job boards, industry networking events
- Faculty-specific career resources (fbe, law, engineering etc.)
- Graduate recruiter events (open to current students)

### Mentoring: same programs, different framing

The alumni site's mentoring structure exists in two places:
- `/alumni/get-involved/volunteer/mentoring/faculty-specific-mentoring/` — 12 faculty-specific pages for **alumni who want to mentor students**
- `/alumni/impact/become-a-mentor/business-and-economics-career-mentoring/faqs` — business-specific FAQ for mentors

The current-student estate (and the central Careers service) frames the same programs from the student perspective: "find a mentor." The alumni site frames it from the mentor perspective: "become a mentor." These are two ends of the same pipeline, but they are **not cross-linked**. A student looking for a mentor and an alumnus looking to mentor are searching independently rather than being matched through a unified discovery experience.

### Handoff clarity: Weak

There is no page on the alumni site that says "if you are a current student, go here for career support." Conversely, the career pages on the current-student estate do not say "when you graduate, your career resources move to alumni.unimelb.edu.au." The career lifecycle — student → graduate — is **not signposted** across the IA boundary.

### Recommendation

- Establish a single "Career lifecycle" framing with explicit transitions: current student → new graduate → established professional
- The central Careers service should link forward to the alumni career tools for post-graduation use
- The alumni mentoring "become a mentor" pages should cross-link to the student-facing "find a mentor" discovery flow
- Consolidate the two internal "career tools" pages on the alumni site into one

---

## 2. Events: Calendar Fragmentation

### Overlap diagnosis

The alumni site's events page (`/alumni/stay-connected/find-an-event`) uses a separate alumni events management calendar. The current-student estate surfaces events through multiple channels: Union events, faculty calendars, Careers events, UniMelb central events.

Many event types are substantively shared:
- **Lectures and panels**: Alumni panels (alumni side) and campus public lectures (student side) both attract a mixed current/former student audience but are listed on separate calendars
- **Networking events**: Career networking events appear on both Careers pages and alumni pages
- **Reunions and homecomings**: Alumni-only, no student-side equivalent

### Key issue: No unified events discovery

A graduating student looking for "what events is the University running this month" has no single discovery point. The alumni site's event calendar is not referenced from the student-facing event listings, and vice versa.

### Recommendation

- Create a unified event taxonomy with audience tagging ("current students," "recent graduates," "alumni," "open")
- The alumni events page should acknowledge and link to student-facing events that are open attendance
- Consider a "recent graduate" events filter that spans both estates during the 0–2 year post-graduation window

---

## 3. Community: Student Life vs Alumni Community

### Language comparison

**Current-student estate ("student life"):**
> "Connect with clubs, societies, and student groups. Build your community during your degree."

**Alumni site ("alumni community"):**
> "With over 500,000 alumni across the globe, you're part of a vibrant network. Reconnect, grow your career, and get involved."

The framing is parallel but not identical. "Student life" emphasises joining and belonging during study; "alumni community" emphasises reconnecting and contribution after graduation. However:

- Both use "community," "network," "connect"
- Both surface groups/chapters (student orgs vs alumni chapters)
- The India Alumni Network (`/alumni/stay-connected/find-a-group/india-alumni-network`, 1,868 words) is one of the most content-rich pages on the alumni site — longer than most faculty CS pages. There is no corresponding current-student discovery for "find Indian students on campus" — the ecosystem exists but operates on separate planes

### Differentiation: present but not marked

The distinction between "student life community" and "alumni community" is clear in concept but poorly sign-posted in practice. A recently-graduated student would find that their existing student community (clubs, societies, Facebook groups) goes quiet without any institutional guide to what the alumni equivalent looks like or where to find it.

The alumni site does not provide a "what happens to your student community when you graduate" explanation. The welcome-new-alumni page (`/support-resources/welcome-new-alumni`) is the closest thing, but it does not reference the student-life transition explicitly.

### Recommendation

- The welcome-new-alumni page should explicitly address the community transition: "Your student clubs wind down — here's how to stay connected as an alum"
- Alumni chapters that have a geographic or faculty basis should be discoverable from the current-student faculty pages as a "what's next" destination
- Consider a "community handoff" pattern at graduation that automatically surfaces relevant alumni networks based on faculty and location

---

## 4. Handoff Points: Clear vs Blurry

### Clearest handoff points

| Trigger | Alumni entry point | Quality |
|---|---|---|
| Graduation ceremony | `/alumni/support-resources/welcome-new-alumni` | Good page, but not linked from graduation comms |
| Benefits inquiry | `/alumni/benefits` | Self-contained, clearly alumni-only |
| Giving/philanthropy | `/alumni/get-involved/give-back` | Alumni-only intent, no overlap |
| Reconnecting with peers | `/alumni/stay-connected/find-a-group` | Alumni-only scope |

### Blurry boundary zones

| Topic | Student-side entry | Alumni-side entry | Problem |
|---|---|---|---|
| Career tools | `students.unimelb.edu.au/careers` | `/alumni/support-resources/career-support/career-tools` | Parallel content, no handoff link |
| Professional development | Faculty CS pages + Careers | `/alumni/benefits/professional-development` | No sequencing signal |
| Health and wellbeing | `students.unimelb.edu.au/wellbeing` | `/alumni/benefits/lifestyle/health` | Different content, same label |
| Mentoring | Student-facing "find a mentor" | Alumni-facing "become a mentor" | Same pipeline, disconnected discovery |
| Library access | Student library card (auto) | `/alumni/benefits/university-access/library-access` | Transition not explained |
| Events | Student event calendars | `/alumni/stay-connected/find-an-event` | Separate calendars, no crossover |

---

## 5. Summary Recommendations

### Priority 1 — Lifecycle handoff (graduation transition)
Build an explicit "graduation bridge" — a page or campaign that activates when a student is within 90 days of graduation, surfacing: alumni email transition, career tool continuation, community shift, library access retention. Neither site currently does this.

### Priority 2 — Careers cross-linking
The central Careers service should include a "Post-graduation" section that explicitly links to alumni career tools and names the transition. The alumni career pages should reference the Careers service for current access context.

### Priority 3 — Mentoring pipeline unification
The student-facing "find a mentor" flow and the alumni-facing "become a mentor" flow should be presented as two ends of the same program with mutual discovery: students see "your mentors are alumni"; alumni see "your mentees are current students."

### Priority 4 — Consolidate alumni internal career duplication
Two "career tools" pages exist within the alumni site (`/support-resources/career-support/career-tools` and `/benefits/professional-development/career-tools`). These should be merged or one should redirect to the other with a clear content distinction.

### Priority 5 — Events taxonomy
Establish audience tagging for events so that "events for both students and alumni" are discoverable from either estate, reducing the invisible wall between the two calendar systems.
