# Topic Deep-Dive: study.unimelb × current-students overlap zones

*Analysis based on: 300-page BFS crawl of study.unimelb.edu.au (June 2026) + 1,161-page faculty current-students crawl (June 2026). Cross-referenced with students.unimelb.edu.au students.unimelb.edu.au data.*

---

## Scope of this analysis

This document maps every topic area where content exists on both `study.unimelb.edu.au` (prospective) and the current-students estate (enrolled), asks whether they serve the same user need or different lifecycle stages, audits cross-linking between the two, and recommends where the enrolment "handoff" boundary should sit.

---

## 1. Topic-by-topic overlap mapping

### 1a. Fees and finance

| Site | Pages | Nature of content |
|---|--:|---|
| study.unimelb | 13 | Tuition fee schedules by level/type, HECS/FEE-HELP explainers, living cost estimates, fee estimator tool |
| Faculty CS (enrolled) | ~12 (scattered across faculties) | Faculty-specific fee variations, invoice payment, HELP debt |
| students.unimelb.edu.au students.unimelb.edu.au | ~5 | HECS/FEE-HELP basics, fees FAQ |

**Are they serving the same user need?** Partially. study.unimelb fees content answers "what will I pay?" before enrolment. The enrolled estate answers "how do I pay my current invoice?" and "what is my HELP debt?" These are adjacent needs but distinct tasks.

**The actual problem:** The boundary is not signalled. The page `/how-to-apply/undergraduate-study/domestic-applications/fees-and-payments` lives on study.unimelb but contains payment process information that enrolled students search for. Its 4 links to students.unimelb suggest it half-acknowledges this but doesn't cleanly hand off. An enrolled student who Googles "University of Melbourne tuition fees" will routinely land on study.unimelb — a prospective-student context — without any "if you're already enrolled, go here instead" signpost.

**Where should the handoff be?** The fee schedule (what courses cost) belongs on study.unimelb and in the Handbook. The payment mechanics (when invoices are issued, how to pay, HELP debt management) belong exclusively on students.unimelb.edu.au. study.unimelb fee pages that currently describe payment process should link directly to `students.unimelb.edu.au/your-finances` and stop at "here are the fees; once enrolled, manage payments here."

---

### 1b. Scholarships

| Site | Pages | Nature of content |
|---|--:|---|
| study.unimelb | ~75 (43 study-scholarships + 32 scholarships cross-tag) | Scholarship search, equity schemes (Access Melbourne, Narrm), scholarship application guides, Narrm Scholar profiles |
| Faculty CS (enrolled) | 141 pages across 9 faculties | Named donor awards, application rounds, T&Cs, Dean's Honours Lists, winner galleries |
| `scholarships.unimelb.edu.au` | Active subdomain (central system) | Award database, application engine — linked from study.unimelb (167 links) |
| students.unimelb.edu.au students.unimelb.edu.au | 0 pages | Nothing |

**Are they serving the same user need?** No — but they should be connected. study.unimelb serves discovery (what scholarships exist, am I eligible, how do I apply before I enrol). Faculty CS serves post-enrolment scholarship management (my named award, when is the next round, Dean's Honours). `scholarships.unimelb.edu.au` sits in between and is the only candidate for a unified through-thread, but it's not surfaced from students.unimelb.edu.au at all.

**The critical missing link:** An enrolled student returning to find new scholarships or check on their Narrm Scholarship status has nowhere to go in the enrolled-student system. study.unimelb's equity scheme pages (Narrm Scholarship Program, Access Melbourne) link to `students.unimelb.edu.au` for ongoing support but the enrolled site has no corresponding scholarship discovery or management section.

**Where should the handoff be?** study.unimelb should remain the entry door for prospective scholarships. On receipt of an offer, or at commencing student orientation, there should be an explicit "Your scholarships once enrolled" path that lands at `students.unimelb.edu.au/your-finances/scholarships` — a page that does not currently exist. That page should surface the `scholarships.unimelb.edu.au` catalogue for enrolled-student-specific searches, and link to the relevant faculty scholarship section for named awards.

---

### 1c. Careers and employability

| Site | Pages | Nature of content |
|---|--:|---|
| study.unimelb | 37 | Employment outcomes, "9 in-demand industries", industry connections by faculty, employer partner showcase |
| Faculty CS (enrolled) | ~80 pages across 8 faculties | Internship programmes, employer events, job boards, career skills workshops, mock interviews |
| careers.unimelb.edu.au | Active platform | Central career services portal (underlinked from faculty CS) |

**Are they serving the same user need?** No. study.unimelb's careers content is **aspiration-framing** — it answers "will this degree lead to a good career?" for someone deciding whether to enrol. Faculty CS careers content is **action-oriented** — it answers "how do I find an internship next semester?" for an enrolled student. The topic tag conflates these.

**Cross-link audit:** study.unimelb careers pages do not link to `careers.unimelb.edu.au` or faculty CS career services. The enrolled-student's career services platform is invisible from the prospective site. This is a **funnel gap**: a prospective student researching careers gets excited about outcomes on study.unimelb but has no path to see what support they'll actually receive once enrolled.

**Where should the handoff be?** A simple addition: study.unimelb careers pages should include a section "Career support once enrolled" linking to `careers.unimelb.edu.au`. This is a marketing and retention argument — showing prospective students what enrolled-student career support looks like is a competitive differentiator.

---

### 1d. International students

| Site | Pages | Nature of content |
|---|--:|---|
| study.unimelb | 55 (international) + 66 (study-international) | Visa applications, OSHC, Moving Guide, agent directory, ELR, country-specific requirements, exchange/study-abroad applications |
| Faculty CS (enrolled) | Scattered — ~15 pages across 4 faculties | Outbound exchange, study abroad, international student support |
| students.unimelb.edu.au students.unimelb.edu.au | Some | Visa compliance (ESOS), OSHC renewal, international student support |

**Are they serving the same user need?** The international topic has the **clearest lifecycle split** of any overlap zone, but the boundary is blurry at the moment of arrival:

- **Pre-enrolment (study.unimelb):** choosing to come, visa application, OSHC purchase, English requirements, agent, country-specific processes
- **Pre-arrival to arrival (study.unimelb + students.unimelb.edu.au gap):** Moving Guide, what to bring, how to settle in, banking, transport
- **Post-arrival enrolled (students.unimelb.edu.au + faculties):** OSHC renewal, visa compliance, ESOS obligations, outbound exchange

The **Moving Guide** (`/support/moving-support/moving-guide` — 8 links to students.unimelb) is the clearest boundary-blurring page. It is a post-offer, pre-arrival guide that explains registered university accommodation, campus orientation, and first-week tasks — but it lives on the prospective site. Newly arrived international students who need it will find it via study.unimelb rather than through the enrolled-student portal.

**Where should the handoff be?** The Moving Guide and all "You've received an offer — here's what to do before you arrive" content should either:
(a) Remain on study.unimelb with a prominent banner: "This page is for students who have already received an offer. If you haven't applied yet, [start here]."
(b) Or be reproduced on `students.unimelb.edu.au` as the canonical post-offer international transition guide, with study.unimelb pointing to it.

Currently the handoff is a link within body copy on a prospective-context page. That is insufficient for the highest-stakes transition in the student journey.

---

### 1e. Graduate Degree Packages (the strongest overlap zone)

| Site | Pages | Nature of content |
|---|--:|---|
| study.unimelb | 14+ pages | Guaranteed undergraduate-to-postgraduate pathways, entry requirements, duration, fee info, by discipline (Engineering, Law, IT, ABPD, Health, Teaching, etc.) |
| Faculty CS (enrolled) | ~0 dedicated pages (scattered references) | None have a dedicated section on how enrolled students can activate their guaranteed pathway |
| students.unimelb.edu.au students.unimelb.edu.au | 0 | Nothing |

**This is the most significant structural gap found in this analysis.** The Graduate Degree Package pages on study.unimelb average 2,000–4,700 words and contain 8–24 links each to `students.unimelb.edu.au`. They describe — in detail — what an enrolled student must do to activate their guaranteed progression to a master's degree: maintain a certain GPA, apply by a certain date, contact a specific person.

An enrolled student in Year 2 or Year 3 of their bachelor's, planning their graduate pathway, will search for this information. Google will typically return the study.unimelb Graduate Degree Package page — which is framed for prospective students ("choose Melbourne because of this pathway") rather than enrolled students ("here's how to activate the pathway you signed up for"). students.unimelb.edu.au has no equivalent, and the faculty CS sections do not have dedicated pathway-management pages.

**Where should the handoff be?** Each Graduate Degree Package page on study.unimelb should include a clear section: "You're already enrolled — here's how to confirm your pathway" with links to the relevant faculty CS section and/or students.unimelb.edu.au's course variation process. The enrolled-student estate should have a mirror of this content framed for managing the progression rather than choosing it.

---

### 1f. Student life and community

| Site | Pages | Nature of content |
|---|--:|---|
| study.unimelb | 47 student-life + 109 study-campus-life | Meet-our-students profiles (51 pages), Melbourne lifestyle, events, sports, clubs overview, accommodation |
| Faculty CS (enrolled) | ~40 pages across multiple faculties | Faculty-specific clubs, mentoring, maker spaces, ambassador programs |
| students.unimelb.edu.au students.unimelb.edu.au | Heavy | UMSU, clubs & societies, events, student support |

**Are they serving the same user need?** Study.unimelb student-life content serves a single need: **reassurance before committing** ("Will I belong here?"). The 51 student profiles are editorial, not transactional. The enrolled estate's student-life content is operational — how to join a club, book a room, find a mentor.

**Low overlap risk**, but one flag: study.unimelb's student-life landing page has 6 links to students.unimelb, suggesting it uses students.unimelb.edu.au as the "once you're enrolled, participate here" pointer. This works but is implicit — a "life as an enrolled student" section could make it explicit.

---

## 2. Cross-link audit

### Does study.unimelb link to students.unimelb?

**Yes — 273 links from 62 pages (21% of the crawled set).** This is a substantial and consistent cross-link pattern. It means study.unimelb has already accepted `students.unimelb.edu.au` as the canonical destination for enrolled-student actions. The cross-linking happens organically (page by page) rather than through a deliberate transition architecture.

**High-cross-link pages:**
- Glossary (44 links) — defining enrolled-student systems for prospective readers
- Graduate Degree Packages (8–24 links each) — enrolled pathway management from a prospective page
- FAQ (16 links) — mixed prospective/enrolled questions on one page
- Transferring courses (12 links) — process for enrolled students, on prospective site

### Does study.unimelb link to faculty current-students sections?

**Rarely.** A scan of outbound hosts found no significant volume of direct links to `eng.unimelb.edu.au/students`, `fbe.unimelb.edu.au/students`, etc. study.unimelb routes to students.unimelb.edu.au (`students.unimelb.edu.au`) but not to the 13 faculty CS sections. This means **the prospective site does not acknowledge that post-enrolment, students will move to faculty-specific sections** — a significant gap for students who want to understand what their faculty's current-student experience looks like before committing.

### Does study.unimelb link to the Handbook?

**25 links to `handbook.unimelb.edu.au`** — moderate volume, concentrated on Graduate Degree Package pages where students need to look up specific subject requirements.

### Does the current-students estate link back to study.unimelb?

From the existing cross-site analysis: **529 outbound links from current-students faculty sections to study.unimelb.edu.au.** This means enrolled students are being directed back to the prospective site — typically for course information that exists on study.unimelb but not on the enrolled-student estate. This is the "reverse funnel" problem: enrolled students using the prospective site as a reference resource.

---

## 3. Where should the "handoff" be?

### Current state

There is no designed handoff. The boundary is de facto set by the URL — once you leave study.unimelb you're on a different site — but users don't experience it that way. The current state is:

- Prospective students exploring → study.unimelb
- Accepted offer, pre-enrolment tasks → study.unimelb links them to students.unimelb as needed
- Enrolled first-year → students.unimelb + faculty CS section
- But: enrolled students searching course info, fees, scholarships, Graduate Degree Packages → Google → study.unimelb → prospective-framed content with enrolled-student links embedded

### Recommended handoff architecture

**1. Create a dedicated post-offer transition section on study.unimelb**

A section at `/study-with-us/you-have-an-offer` or similar that explicitly transitions users:
- "You've received an offer — congratulations. Here's what happens next."
- Enrolment checklist (currently scattered across study.unimelb and students.unimelb)
- Explicit instruction: "From now on, your study information lives at students.unimelb.edu.au. Bookmark it."
- Direct links to: My Enrolled Courses (Handbook), My Finances (students.unimelb.edu.au), My Faculty (faculty CS section), Student Support (students.unimelb.edu.au)

**2. Add audience-disambiguation banners to crossover pages**

The Glossary, FAQ, Graduate Degree Packages, High School Guide, and Transferring Courses pages should carry a banner:
- "Already enrolled? This page has information for enrolled students too. [Go to My Student Portal]"

**3. Add a scholarship through-path at enrolment**

- study.unimelb scholarship discovery → clear "Once you're enrolled, manage your scholarships at [scholarships.unimelb.edu.au → enrolled section]"
- `students.unimelb.edu.au/your-finances/scholarships` (new page needed) that surfaces enrolled-student scholarship opportunities

**4. Faculty CS handback from study.unimelb**

Graduate Degree Package pages should link directly to the relevant faculty CS section's course-planning pages — not just to students.unimelb.edu.au. This would give prospective students a preview of their faculty's enrolled experience and create a direct link from funnel-entry to lifecycle management.

**5. International student pre-arrival transition**

Move or duplicate the Moving Guide as a post-offer page on `students.unimelb.edu.au`, prominently linked from "You've accepted your offer" comms and the Offers & Enrolments page on study.unimelb. The Moving Guide is the highest-stakes page in this analysis — an international student relying on it should not have to orient themselves on a prospective-student website.

---

## 4. Summary verdict

| Overlap zone | Pages (study) | Pages (enrolled) | Verdict |
|---|--:|--:|---|
| Fees / finance | 13 | ~17 | Mostly different stages; signal boundary better |
| Scholarships | ~75 | 141 (faculty) | Connected only via `scholarships.unimelb.edu.au`; students.unimelb.edu.au gap |
| Careers | 37 | ~80 | Different lifecycle needs; add through-link from prospective |
| International | 66–121 | ~15 | Pre-arrival gap; Moving Guide needs dual presence |
| Graduate Degree Packages | 14+ | ~0 | **Enrolled students have no equivalent content; biggest gap** |
| Student life | 47–109 | ~40 | Low duplication; lifestyle vs. operations framing |
| Course planning | 2 | ~50 (faculty CS) | study.unimelb doesn't cover enrolled planning; healthy split |

**The single highest-priority finding:** Enrolled students have no place to go for Graduate Degree Package pathway management. study.unimelb has the content; it's framed wrong; and no enrolled-student resource mirrors it. This is the clearest content gap identified across the entire estate analysis.
