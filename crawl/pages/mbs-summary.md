# Melbourne Business School (MBS) — Current Students crawl summary

- **Unit:** mbs (Melbourne Business School — graduate coursework)
- **Parent faculty:** FBE (Business & Economics)
- **Unit level:** school (separate subdomain under FBE)
- **Root:** https://mbs.unimelb.edu.au/students
- **Scope prefix (PRE):** /students  (in-scope = host `mbs.unimelb.edu.au` AND path == `/students` or starts with `/students/`)
- **Pages captured:** 61
- **Max IA depth:** 4
- **Fetch errors:** 0
- **HTTP/parse 404s:** 0
- **Off-host (auth/SSO) redirects:** 0
- **Crawled:** 2026-06-15 (in-page fetch-BFS via connected Chrome; caps 250/depth 6, neither hit)

## Headline finding — MBS runs a genuinely SELF-HOSTED, deep course-planning section, NOT a hub link-farm

MBS is a school under FBE but runs an **entirely separate Current-Students section on its own subdomain** (`mbs.unimelb.edu.au/students`), distinct from FBE's own `fbe.unimelb.edu.au/students`. This crawl documents that fragmentation concretely: a student in an FBE-family graduate program navigates a **completely different CS site** from a BCom or PhD student in the same faculty.

Structurally, the section is **substantive and self-contained, not a directory to the central hub**. All 61 pages are server-rendered MBS-hosted content with healthy prose (word counts 288–2,023, median ~844). The classifier scored **0 link-farms** and **1 mixed** — i.e. MBS barely leans on `students.unimelb.edu.au` at all. This is the opposite of the thin cohort-routing pattern seen on some faculty roots.

The mass of the tree is a **per-program 'course plan' cluster**: **41 individual master's-program course-map pages** under `/students/course-planning/course-plans/masters-programs/` (Management, Finance, Marketing, HR, Supply Chain, Actuarial Science, Econometrics, International Business, Entrepreneurship, Digital Marketing, Indigenous Business Leadership — each in 150/200-point and research-pathway variants). Each is a genuine ~700–1,150-word structured study plan. MBS therefore **duplicates the 'course planning' function** that the central hub and Stop 1 nominally own, maintaining its own program-by-program enrolment guidance.

### Service duplication vs the faculty/central hub

MBS maintains its own copies of services that also exist at FBE / the central hub:

| Service | MBS self-hosted | Also at |
|---------|-----------------|---------|
| Course planning / program maps | `/students/course-planning/course-plans` (40+ program pages) | central hub, Stop 1 |
| Enrolment & timetabling | `/students/course-planning/enrolment` | `my.unimelb`, central hub |
| Assessment guidance | `/students/course-planning/assessment` | FBE `/students/bcom/.../assessment` |
| Student support / wellbeing | `/students/student-support`, `/students/wellbeing` | FBE `/students/wellbeing`, central Counselling |
| Computing spaces / virtual lab | `/students/course-planning/services/computing-spaces`, `/virtual-lab` | FBE `/students/services/*` (near-identical) |
| Orientation | `/students/orientation` | FBE `/students/bcom/orientation`, central |
| **Careers (separate service)** | **`mbs.unimelb.edu.au/career` — 'MBS Career Elevation' (live, 200; NOT under /students)** | central Careers, FBE |

The MBS **careers service is a wholly separate site** at `mbs.unimelb.edu.au/career` ('MBS Career Elevation', HTTP 200, confirmed live). It sits OUTSIDE the `/students` scope (path `/career`, not `/students/...`) so it was **not crawled**, but it is recorded here as a notable outbound: MBS graduate students get an MBS-branded careers service distinct from both the FBE careers touchpoints and central `careers.unimelb.edu.au`.

## Breakdown by classification

- **unique:** 60
- **mixed:** 1

_Signal note: every page cleared the 160-word `unique` threshold; the few low-word pages (Virtual Lab 288w, Services 299w) still carry unique MBS-specific prose rather than hub links, so none scored as link-farms._

## Breakdown by topic tag

- **course-planning:** 58
- **research-candidature:** 13
- **international:** 7
- **fees-finance:** 7
- **wellbeing-health:** 2
- **IT-systems:** 2
- **orientation:** 1
- **exams-results:** 1
- **enrolment:** 1
- **forms-admin:** 1
- **contacts-support:** 1
- **subjects-timetable:** 1
- **student-life:** 1
- **inclusion-equity:** 1

## Depth distribution

- depth 0: 1 pages
- depth 1: 3 pages
- depth 2: 10 pages
- depth 3: 46 pages
- depth 4: 1 pages

## Top outbound destinations (where it sends students)

Other unimelb / external hosts linked from the `/students` subtree, by total link count:

- `handbook.unimelb.edu.au`: 1687
- `www.unimelb.edu.au`: 430
- `about.unimelb.edu.au`: 244
- `students.unimelb.edu.au`: 157
- `www.facebook.com`: 122
- `www.instagram.com`: 122
- `www.linkedin.com`: 122
- `mbs.unimelb.edu.au`: 68
- `fbe.unimelb.edu.au`: 66
- `safety.unimelb.edu.au`: 61
- `services.unimelb.edu.au`: 12  ⚠ auth-gated
- `findanexpert.unimelb.edu.au`: 11
- `ask.unimelb.edu.au`: 9
- `study.unimelb.edu.au`: 7
- `www.hec.ca`: 5
- `umsu.unimelb.edu.au`: 4
- `library.unimelb.edu.au`: 4
- `www.unibocconi.eu`: 3
- `lms.unimelb.edu.au`: 2  ⚠ auth-gated
- `academichonesty.unimelb.edu.au`: 2
- `forms.your.unimelb.edu.au`: 2
- `scholarships.unimelb.edu.au`: 2
- `canvas.lms.unimelb.edu.au`: 1  ⚠ auth-gated
- `headspace.org.au`: 1
- `www.beyondblue.org.au`: 1
- `commercestudentcentre.formstack.com`: 1
- `policy.unimelb.edu.au`: 1
- `my.unimelb.edu.au`: 1  ⚠ auth-gated
- `classregenquiries.app.unimelb.edu.au`: 1
- `www.studentit.unimelb.edu.au`: 1  ⚠ auth-gated

## Notable outbound: MBS's own separate services (same subdomain, outside /students)

- `mbs.unimelb.edu.au/career` — **MBS Career Elevation** (live, HTTP 200) — MBS-run careers service, NOT under `/students`, not crawled.
- `mbs.unimelb.edu.au/careers` — 404 (the live path is `/career`).

## Auth-gated / login hosts seen (recorded as outbound only, not crawled)

- `services.unimelb.edu.au`: 12 links
- `lms.unimelb.edu.au`: 2 links
- `canvas.lms.unimelb.edu.au`: 1 links
- `my.unimelb.edu.au`: 1 links
- `www.studentit.unimelb.edu.au`: 1 links
- `studentit.unimelb.edu.au`: 1 links

## Notable unique pages (richest substantive content)

- **Outbound - Dual Degree** (2023w, d3, international/course-planning) — `/students/course-planning/master-of-international-business-dual-degrees/outbound`
- **Assessment** (1213w, d2, exams-results/course-planning) — `/students/course-planning/assessment`
- **Master of Management (Accounting and Finance)** (1152w, d3, fees-finance/course-planning) — `/students/course-planning/course-plans/masters-programs/master-of-management-accounting-finance-200-points`
- **Subject Selection and Advanced Standing** (1098w, d2, course-planning/subjects-timetable) — `/students/course-planning/subject-selection-and-advanced`
- **Enrolment and Timetabling** (1057w, d2, enrolment/course-planning) — `/students/course-planning/enrolment`
- **Master of Management (Accounting) 150 point** (1017w, d3, course-planning) — `/students/course-planning/course-plans/masters-programs/master-of-management-accounting-plan-2`
- **Master of International Business (200 point) - Research Pathway** (990w, d3, research-candidature/international/course-planning) — `/students/course-planning/course-plans/masters-programs/master-of-international-business-200-point-research-pathway`
- **Master of Management (200 point) - Research Pathway** (973w, d3, research-candidature/course-planning) — `/students/course-planning/course-plans/masters-programs/master-of-management-200-point-research-pathway`
- **Master of Management (200 point)** (943w, d3, course-planning) — `/students/course-planning/course-plans/masters-programs/master-of-management`
- **Master of Management (150 point) - Research Pathway** (938w, d3, research-candidature/course-planning) — `/students/course-planning/course-plans/masters-programs/master-of-management-150-point-research-pathway`
- **Student Support** (937w, d2, course-planning) — `/students/course-planning/student-support`
- **Master of Finance (Enhanced) - Research Pathway** (920w, d3, research-candidature/fees-finance/course-planning) — `/students/course-planning/course-plans/masters-programs/master-of-finance-enhanced-research-pathway`
- **Master of Management (150 point)** (919w, d3, course-planning) — `/students/course-planning/course-plans/masters-programs/master-of-management-150-point`
- **Master of Finance (Enhanced)** (918w, d3, fees-finance/course-planning) — `/students/course-planning/course-plans/masters-programs/master-of-finance-enhanced`
- **Master of Commerce (Actuarial Science) - Research Pathway** (891w, d3, research-candidature/course-planning) — `/students/course-planning/course-plans/masters-programs/master-of-commerce-actuarial-science-research-pathway`

## Section IA tree (in-scope URLs)

```
students
  course-planning
    assessment
    changing-courses
    course-plans
      masters-programs
        master-of-actuarial
        master-of-actuarial-science
        master-of-actuarial-science-enhanced
        master-of-applied-econometrics-commenced-prior-to-2022
        master-of-applied-econometrics2
        master-of-commerce-actuarial-science
        master-of-commerce-actuarial-science-research-pathway
        master-of-digital-marketing
        master-of-economics
        master-of-entrepreneurship-commenced-prior-to-2023
        master-of-entrepreneurship-enhanced-new-venture-creation-pathway
        master-of-finance
        master-of-finance-enhanced
        master-of-finance-enhanced-research-pathway
        master-of-finance-research-pathway
        master-of-indigenous-business-leadership
        master-of-international-busines
        master-of-international-business-150-point
        master-of-international-business-150-point-research-pathway
        master-of-international-business-200-point-research-pathway
        master-of-management
        master-of-management-150-point
        master-of-management-150-point-research-pathway
        master-of-management-200-point-research-pathway
        master-of-management-accounting
        master-of-management-accounting-finance-200-points
        master-of-management-accounting-plan-2
        master-of-management-finance-150-point
        master-of-management-finance-200-point
        master-of-management-human-resources
        master-of-management-human-resources-150-point
        master-of-management-human-resources-150-point-research-pathway
        master-of-management-human-resources-200-point-research-pathway
        master-of-management-marketing
        master-of-management-marketing-150
        master-of-management-marketing-150-point-research-pathway
        master-of-management-marketing-200-point-research-pathway
        master-of-management-supply-chain-management-150pt
        master-of-management-supply-chain-management-150pt-research-pathway
        master-of-management-supply-chain-management-200pt
        master-of-management-supply-chain-management-200pt-research-pathway
    enrolment
    master-of-international-business-dual-degrees
      inbound
      outbound
    services
      computing-spaces
      rules
      virtual-lab
    student-administration
    student-support
    subject-selection-and-advanced
  orientation
  wellbeing
    ambassadors
```
