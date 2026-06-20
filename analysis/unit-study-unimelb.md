# study.unimelb.edu.au — Unit Brief

*Crawled June 2026. 300 pages, BFS from root, cap depth 3.*

---

## Overview: What study.unimelb IS

`study.unimelb.edu.au` is the University of Melbourne's prospective-student and course-discovery site — the top of the enrolment funnel. Its primary audience is people who have **not yet enrolled**: school-leavers choosing a degree, career-changers considering postgraduate study, international students researching Melbourne, and parents/agents advising applicants.

The site is **structurally separate** from the current-students estate (students.unimelb.edu.au and the faculty CS sections). It does not sit inside a faculty; it is a whole-of-university marketing and information platform.

However, this brief establishes that **study.unimelb bleeds meaningfully into current-student territory** in at least five topic areas, and that the handoff from prospective to enrolled is not currently clean for the user.

---

## Scale and depth

| Metric | Value |
|---|---|
| Pages captured | 300 (cap reached; site larger) |
| Max IA depth | 3 |
| Unique content pages | 271 (90%) |
| Link-farm / thin pages | 28 (9%) |
| HTTP/parse 404s | 1 |
| Fetch errors | 0 |
| Top-level sections | 8 (find, how-to-apply, student-life, study-with-us, accommodation, support, connect-with-us, discover) |

The **90% unique rate** is high — this is a content-rich site, not a link directory. The 33 pages under `/__data/` are PDFs (course guides, brochures) which were captured with extremely high word counts because the PDF text is rich.

### Section page distribution

| Section | Pages |
|---|---|
| `/find` | 81 |
| `/student-life` | 51 |
| `/how-to-apply` | 55 |
| `/accommodation` | 25 |
| `/study-with-us` | 39 |
| `/__data` (PDFs) | 33 |
| `/support`, `/connect-with-us`, `/discover` | 16 |

The `/find` section (course browser) and `/student-life` together account for **44%** of pages — the site invests heavily in course discovery and lifestyle reassurance, which are the two primary motivations of a prospective student.

---

## Topic breakdown (top topics by page count)

| Topic tag | Pages | What it covers |
|---|--:|---|
| study-course-info | 224 | Course descriptions, degree packages, Graduate Degree Package pages, PDF brochures, course finders |
| graduation | 121 | Degree pathway pages where "guaranteed progression" language triggers this tag — actually prospective-to-PG funnel content |
| study-campus-life | 109 | Accommodation, student life, Melbourne lifestyle, sport, housing |
| study-how-to-apply | 70 | Application guides, VTAC, online application, offers & enrolments, deadlines |
| study-international | 66 | International applicant content, visa info, OSHC, moving guide, agent finder |
| international | 55 | Cross-tagged: international exchange/study abroad, dual-degree options |
| student-life | 47 | Student community, meet-our-students profiles, Narrm Scholars stories |
| study-scholarships | 43 | Scholarship search, Access Melbourne, equity schemes, Narrm Scholarship |
| careers-employability | 37 | "Why study at Melbourne" employment outcomes, graduate destinations, industry connections |
| scholarships | 32 | Cross-tagged with current-students scholarship topic (overlap zone) |
| study-entry-requirements | 23 | ATAR, selection rank, VCE prerequisites, English language requirements |
| study-fees-costs | 21 | Fee estimators, HECS/FEE-HELP, tuition fee schedules, living cost guides |
| wellbeing-health | 17 | Mental health/wellbeing reassurance content for prospective students |
| fees-finance | 13 | Cross-tagged with current-students fees topic (overlap zone) |

The `graduation` tag count of 121 is an artefact of the **Graduate Degree Package** pages — the University's signature undergraduate-to-postgraduate pathway product. These pages describe how to progress from a bachelor's to a master's, and the tagger fires on "graduate" language throughout. They are genuinely prospective-audience content, but they reference `students.unimelb.edu.au` heavily (average 8–24 links per page) because the enrolment mechanics once a student is accepted live on the hub.

---

## Cross-site overlap findings

**21% of study.unimelb pages (62 of 300) link out to `students.unimelb.edu.au`**, generating 273 outbound links total to the current-students hub. This is the primary structural finding: the prospective site is **actively sending prospective visitors into the enrolled-student system** rather than hand-holding them through an enrolment transition.

### Overlap zone 1: Fees and finance (13 pages)

study.unimelb has full fee schedule pages:
- `/how-to-apply/fees` — fee overview for all student types
- `/how-to-apply/undergraduate-study/domestic-applications/fees-and-payments` (4 links → students hub)
- `/how-to-apply/graduate-coursework-study/domestic-applications/fees-and-payments` (4 links → students hub)
- HECS-HELP and FEE-HELP explanations

The current-students estate (via the hub and individual faculties) also carries fees content. The split makes partial sense: study.unimelb covers "what will it cost me as an applicant", while the hub covers "how do I pay my invoice as an enrolled student". But the boundary is not marked to users — someone who has enrolled but wants to check their fees will land on study.unimelb from Google and may not realise they're on the prospective site.

**Overlap verdict:** Partially intentional split; audience handoff is not clearly marked.

### Overlap zone 2: Scholarships (32 pages + 43 study-scholarships pages = ~75 pages)

study.unimelb has a large scholarships surface — the equity schemes (Access Melbourne, Narrm Scholarship), the general scholarship search, and fee-based scholarship information. The existing current-students analysis found **141 scholarship pages across 9 faculty CS sections** and **zero** on the central hub.

The three-way situation:
- `scholarships.unimelb.edu.au` exists as a dedicated subdomain (167 outbound links from study.unimelb point here)
- study.unimelb has 75+ pages explaining and directing to scholarships
- Faculty CS sections hold 141 pages of faculty-specific scholarship/prize/awards content
- `students.unimelb.edu.au` holds nothing on scholarships

study.unimelb is the closest thing to a front door for scholarships, but it stops at the apply/discover stage — once enrolled, there is no clear path to check scholarship status, seek new scholarships, or understand ongoing obligations.

**Overlap verdict:** Funnel entry only (study) vs. lifecycle management (faculty CS); no through-path.

### Overlap zone 3: Careers and employability (37 pages)

study.unimelb's careers content is marketing-oriented: graduate employment outcomes, "9 in-demand industries", industry connections by faculty, employer partners. The faculty current-students sections (8 of 9 faculties) have their own careers content, and the existing analysis flagged `careers.unimelb.edu.au` as underlinked from the current-students estate.

The study.unimelb careers content serves a **different lifecycle stage** — it's answering "will this degree get me a job?" rather than "how do I find a job now I'm enrolled". There is low content duplication, but the topic category masks this distinction.

**Overlap verdict:** Different lifecycle stage; minimal duplication, but the same topic label obscures that.

### Overlap zone 4: International students (55 pages)

study.unimelb has extensive international content (second-largest single-tagged topic): visa applications, OSHC, Moving Guide (8 links to students hub), agent finder, English language requirements, country-specific entry requirements, international exchange and study abroad applications.

The current-students estate has scattered international content (particularly for outbound mobility). The inbound international applicant journey lives almost entirely on study.unimelb, and the "I've arrived" handoff point is the Moving Guide → `students.unimelb.edu.au`. The Moving Guide itself (1,400+ words) links to 8 hub pages but does so within a prospective-site context, which may disorient a newly-arrived student who expected to find it on the enrolled-student platform.

**Overlap verdict:** Structural boundary problem — the pre-arrival → post-arrival transition sits awkwardly on the prospective site.

### Overlap zone 5: Graduate Degree Packages (the dual-audience zone)

The `/study-with-us/guaranteed-undergraduate-to-graduate-study-pathways/graduate-degree-packages/` section is a standout overlap zone. These pages explain guaranteed progression pathways from bachelor's to master's for enrolled students who want to plan ahead. They average **12–24 links per page to students.unimelb.edu.au**, have high word counts (2,000–4,700 words), and are tagged with both `study-course-info` and `graduation`.

These pages are **used by both prospective students** (considering whether to commit to a Melbourne bachelor's) **and enrolled students** (planning their progression mid-degree). The enrolled-student audience has no equivalent content on the current-students estate — it would naturally look for this on the faculty CS pages or hub, but it lives on study.unimelb.

**Overlap verdict:** Genuine dual-audience content with no counterpart in the enrolled estate.

---

## Unique to study.unimelb (no counterpart in current-students estate)

These content types exist only on study.unimelb and are correctly prospective-audience-only:

1. **ATAR / selection rank tables** — entry requirements by course, VCE prerequisite checks, interstate and STAT pathways
2. **Application mechanics** — VTAC lodgement, online application walkthrough, Change of Preference guides, how to accept/defer an offer
3. **Living cost estimators** — rent, food, transport cost breakdowns for Melbourne
4. **Course finder / degree browser** — the `/find` section (81 pages) is the course catalogue discovery tool
5. **Open Day** — events for prospective students
6. **Authorised Education Agents** — agent directory for international applicants
7. **High school programs** — University Extension Program, Year 10 Guide, Young Scholars
8. **Narrm Scholar and student-story profiles** — 51 `/student-life/meet-our-students/` pages; editorial content aimed at reassuring prospective students ("will I fit in?")
9. **Accommodation search and application** — `/accommodation` section (25 pages) for residential college/university housing applications
10. **Equity entry schemes** — Access Melbourne, Special Entry Access Scheme (SEAS), mature-age entry pathways

---

## Notable pages

| Page | Words | Why notable |
|---|---|---|
| Glossary \| Future students | 6,294 | 44 links to students.unimelb — defines University terms for prospective students but also describes enrolled-student systems |
| Frequently asked questions \| Future students | 4,812 | 16 links to students.unimelb — FAQ covers both pre- and post-enrolment questions on single page |
| Graduate Degree Packages: Engineering | 4,714 | 8 links to students hub — dual-audience page: pathway planning for enrolled and prospective |
| Accommodation FAQs | 4,356 | Questions about UniLodge/colleges from applicants + newly arrived students |
| Transferring courses | 1,542 | 12 links to students hub — describes process for enrolled students transferring between degrees |
| High school student's guide to university | 1,211 | 12 links to students hub — introduction to enrolled-student systems aimed at pre-enrolment readers |

The Glossary page is particularly revealing: it defines terms like "Academic Advising", "Census Date", "Subject Coordinator", "MyUniMelb" — systems that only matter once enrolled. Its 44 outbound links to students.unimelb suggest it is **de facto a guide to being enrolled, housed on a prospective-student site**.

---

## Outbound destination analysis

| Destination | Links | Signal |
|---|--:|---|
| `www.unimelb.edu.au` | 576 | Tight coupling to main UoM site (about, news, research) |
| `about.unimelb.edu.au` | 448 | University facts, rankings, sustainability |
| `students.unimelb.edu.au` | 273 | Hub-bound: enrolled-student actions |
| `forms.your.unimelb.edu.au` | 255 | Form submissions (applications, enquiries) |
| `scholarships.unimelb.edu.au` | 167 | Dedicated scholarships subdomain |
| Social platforms (Facebook, LinkedIn, Instagram, TikTok, Twitter) | 471 | Heavy social presence |
| `vtac.edu.au` + `delta.vtac.edu.au` | 75 | Victorian Tertiary Admissions Centre |
| `handbook.unimelb.edu.au` | 25 | Cross-links to course handbook |
| `murrupbarak.unimelb.edu.au` | 26 | Indigenous student support |

The 273 links to `students.unimelb.edu.au` confirm that study.unimelb is already **using the hub as its post-enrolment handoff point**, but the handoff is uncoordinated: individual pages link to individual hub pages without an explicit "You've enrolled — here's where to go next" transition experience.

---

## Verdict: Funnel entry or bleed?

study.unimelb is **correctly positioned as a separate prospective-student funnel** for the majority of its content. The course finder, application guides, ATAR tables, living cost estimates, accommodation search, and equity entry schemes are all correctly audience-scoped and have no place in the enrolled-student estate.

However, the site **bleeds into current-student territory** in three structural ways:

1. **The enrolment bridge pages** (Graduate Degree Packages, Glossary, FAQ, High School Guide, Offers & Enrolments) serve enrolled students but live on a prospective site. Enrolled students Google these terms and land in an environment that signals "you're not yet a student here."

2. **The pre-arrival → enrolled transition is invisible.** The Moving Guide and Offers & Enrolments pages are the natural handoff points, but they hand off via hyperlinks rather than an explicit "You're now a student — leave this site and use this one" journey.

3. **The scholarship funnel is broken at enrolment.** study.unimelb handles discovery and application; the enrolled-student estate handles nothing; `scholarships.unimelb.edu.au` handles the database. An enrolled student returning to manage or find new scholarships has no canonical path.

The fix is not to move content — study.unimelb should remain separate. The fix is to **make the handoff visible**: a post-offer section ("You've received an offer — here's what happens next") that explicitly transitions users to `students.unimelb.edu.au` and the relevant faculty CS pages, rather than leaving them to follow internal hyperlinks from within prospective-audience content.
