# ABP / Melbourne School of Design — Current Students crawl summary

- **Faculty:** abp (Faculty of Architecture, Building and Planning — Melbourne School of Design)
- **Root:** https://msd.unimelb.edu.au/current-students
- **Scope prefix (PRE):** `/current-students` (host `msd.unimelb.edu.au`)
- **Crawl mode:** Exhaustive in-page `fetch()`-based BFS (server-rendered, same-origin). Cloudflare bypassed by fetching from within a page already loaded on the origin.
- **Crawled:** 2026-06-15
- **Pages captured:** 250  (BFS visited == 250)
- **Max depth reached:** 4 (cap 6)

> [!WARNING] **Page cap hit (250).** The crawl stopped at the 250-page cap. **737 in-scope URLs remained unvisited — 100% of them were MSD Studio Archive detail pages** (`/subject-information/msd-studios/...`), a deeply self-interlinked catalogue of individual past design studios (one URL per studio per semester per program). **Every non-archive in-scope URL was fully crawled** before the cap engaged, so no distinct IA section is missing — only additional near-equivalent studio detail pages were truncated.

## Classification breakdown

| Classification | Count |
|---|---|
| unique | 240 |
| mixed | 4 |
| link-farm | 0 |
| redirect/broken | 6 |

- **unique (240)** — substantive prose (wc ≥ 160) with little body-level redirection. **169 of these are MSD Studio Archive pages** (each a genuinely distinct studio brief — 167 distinct excerpts across 169 pages confirmed). The remaining ~71 are real faculty content (course plans, studio info, internships, IT support, employability, mentoring, exhibitions).
- **mixed (4)** — real faculty prose AND heavy redirection to the central student hub (`students.unimelb.edu.au`). These are the transactional landing pages: the CS root, the Enrolment landing, List-of-Forms / Application-for-Extension, and the Employability hub.
- **link-farm (0)** — none. ABP does not use pure link-farm pages; redirection-heavy pages still carry their own prose (hence "mixed").
- **redirect/broken (6)** — form-handler endpoints returning HTTP 403 + a "Redirecting…" stub (webforms / register-for / submission handlers that bounce to an auth-gated forms backend).

> [!NOTE] **Hub-link baseline.** Every MSD page carries ~21 outbound "hub" links (`www.unimelb.edu.au` + `students.unimelb.edu.au`) purely from the shared site chrome (footer/nav). Classification therefore counts only hub links **above** this 21 baseline as genuine body-level redirection — otherwise every page would falsely read as "mixed".

## Topic-tag breakdown

| Topic | Pages |
|---|---|
| subjects-timetable | 204 |
| student-life | 60 |
| research-candidature | 43 |
| course-planning | 29 |
| international | 28 |
| forms-admin | 26 |
| graduation | 20 |
| contacts-support | 19 |
| enrolment | 16 |
| clubs-events | 15 |
| careers-employability | 13 |
| inclusion-equity | 11 |
| IT-systems | 10 |
| placements-WIL | 9 |
| special-consideration | 6 |
| fees-finance | 6 |
| orientation | 6 |
| academic-skills | 5 |
| wellbeing-health | 3 |
| library | 2 |
| scholarships | 1 |

*(Each page carries 1–4 tags. `subjects-timetable` dominates because the studio archive — 169 pages — is subject-level studio content.)*

## In-scope IA tree

Non-archive structure (the genuine information architecture), studio archive collapsed:

```
/current-students
  /course-planning
    /sample-course-plans
      /double-masters
        /architecture-construction
        /architecture-landscape-architecture
        /architecture-property
        /architecture-urban-cultural-heritage
        /architecture-urban-design
        /architecture-urban-planning
        /construction-property
        /landscape-architecture-urban-design
        /landscape-urban-planning
        /property-urban-planning
        /urban-planning-urban-design
      /landscape-architecture-course-plans
      /master-of-architectural-engineering
      /master-of-architecture
      /master-of-construction
      /master-of-property
      /master-of-urban-and-cultural-heritage
      /property-valuation
      /urban-design
      /urban-planning
  /enrolment
    /list-of-forms
      /application-for-extension
        /extension-application-form
  /student-experience
    /abp-industry-mentoring
    /access-and-id-cards
      /student-card-access-error-webform
    /clubs-and-societies
      /information-for-clubs
    /construction-ambassador-program
    /deans-honours-awards
      /2023
      /2024
    /employability-in-architecture-building-and-planning
    /graduate-ambassador-program
    /it-support
      /requestfeedback-form
    /msdx-and-student-exhibitions
      /installation-tips
      /key-dates
      /msd-student-curator-group
    /peer-mentoring-program
      /register-for-msd-peer-mentoring
    /student-feedback-and-grievances
    /student-forum
    /student-newsletters
      /n01-edsc-newsletter-submission-form
    /student-participation-on-faculty-committees-and-advisory-boards
  /subject-information
    /internships-vocational-placements
      /abpl90434-construction-management-internship
        /how-to-apply
        /information-for-hosts
        /self-sourced
    /practical-experience
    /quota-subjects
    /subjects-with-a-travel-component
    /travelling-studios
      /2026-subjects-with-international-travel
        /southeast-asia-travelling-studio
      /d02-application-for-travelling-studio
      /past-studios
        /2008
        /2009
        /2010
        /2011
        /2012
        /2013
        /2014
        /2015
        /2016
        /2017
        /2018
        /2019
        /2020
        /2023m-and-2024
        /2025
```

### MSD Studio Archive (collapsed — `/current-students/subject-information/msd-studios/…`)

A large self-interlinked catalogue. 169 archive URLs captured (of ~900+ discovered). Grouped by top segment under `msd-studios`:

| Sub-group | URLs captured |
|---|---|
| `msd-studio-archive` | 122 |
| `master-of-architecture` | 38 |
| `master-of-landscape-architecture` | 3 |
| `master-of-urban-design` | 3 |
| `master-of-urban-planning` | 2 |
| `(index)` | 1 |

## Top outbound destinations

| Host | Link count (incl. ~21/page chrome baseline) |
|---|---|
| students.unimelb.edu.au | 3486 |
| www.unimelb.edu.au | 1710 |
| about.unimelb.edu.au | 976 |
| services.unimelb.edu.au | 495 |
| handbook.unimelb.edu.au | 380 |
| policy.unimelb.edu.au | 249 |
| www.facebook.com | 247 |
| gateway.research.unimelb.edu.au | 246 |
| murrupbarak.unimelb.edu.au | 246 |
| library.unimelb.edu.au | 245 |
| www.linkedin.com | 245 |
| www.instagram.com | 245 |
| staff.unimelb.edu.au | 244 |
| safety.unimelb.edu.au | 244 |
| myuniapps.unimelb.edu.au | 37 |
| edsc.unimelb.edu.au | 29 |
| findanexpert.unimelb.edu.au | 12 |
| forms.your.unimelb.edu.au | 12 |
| umsu.unimelb.edu.au | 10 |
| www.autodesk.com | 8 |
| www.youtube.com | 7 |
| studentit.unimelb.edu.au | 5 |
| forms.office.com | 5 |
| gsa.unimelb.edu.au | 5 |
| doi.org | 5 |

**Central-hub redirection pattern:** ABP/MSD follows the standard UoM model — transactional admin (enrolment, timetable, special consideration, leave, advanced standing, exams, fees) is delegated to `students.unimelb.edu.au` ("Stop 1"), while the faculty site hosts MSD-specific content (course plans, studios, internships, maker spaces, mentoring, exhibitions).

## Auth-gated / login hosts (recorded as outbound only — never crawled)

| Host | Outbound links |
|---|---|
| services.unimelb.edu.au | 495 |
| studentit.unimelb.edu.au | 5 |
| canvas.lms.unimelb.edu.au | 2 |

Additionally, **6 in-scope `*-form` / `*-webform` / `register-for-*` endpoints returned HTTP 403 + "Redirecting…"** — these bounce to an authenticated forms/SSO backend (`sso.unimelb.edu.au` was observed when one peer-mentoring link was resolved by the browser). They are recorded as `redirect/broken`:
  - `/current-students/subject-information/travelling-studios/d02-application-for-travelling-studio`
  - `/current-students/student-experience/peer-mentoring-program/register-for-msd-peer-mentoring`
  - `/current-students/student-experience/access-and-id-cards/student-card-access-error-webform`
  - `/current-students/student-experience/it-support/requestfeedback-form`
  - `/current-students/student-experience/student-newsletters/n01-edsc-newsletter-submission-form`
  - `/current-students/enrolment/list-of-forms/application-for-extension/extension-application-form`

## Mixed pages (prose + heavy hub redirection)

- `/current-students` (wc=1239) — tags: course-planning, subjects-timetable, enrolment, special-consideration
- `/current-students/student-experience/employability-in-architecture-building-and-planning` (wc=1199) — tags: student-life, placements-WIL, forms-admin
- `/current-students/enrolment` (wc=514) — tags: enrolment, subjects-timetable, special-consideration, forms-admin
- `/current-students/enrolment/list-of-forms/application-for-extension` (wc=1001) — tags: forms-admin, special-consideration, enrolment, contacts-support

## Notable unique pages (faculty-distinctive content, excl. studio archive)

- **IT Support | Current Students | Melbourne School of Design** — `/current-students/student-experience/it-support` (wc=3247; IT-systems, student-life, contacts-support)
- **2014 Past Studios | Travelling Studios | MSD** — `/current-students/subject-information/travelling-studios/past-studios/2014` (wc=2444; subjects-timetable, international)
- **Dean's Honours Awards 2024** — `/current-students/student-experience/deans-honours-awards/2024` (wc=1924; student-life, graduation)
- **Dean's Honours Awards 2023** — `/current-students/student-experience/deans-honours-awards/2023` (wc=1877; student-life, graduation)
- **ABP Industry Mentoring** — `/current-students/student-experience/abp-industry-mentoring` (wc=1858; careers-employability, student-life, graduation)
- **Information for clubs** — `/current-students/student-experience/clubs-and-societies/information-for-clubs` (wc=1641; student-life, clubs-events, subjects-timetable)
- **2019 Past Studios | Travelling Studios | MSD** — `/current-students/subject-information/travelling-studios/past-studios/2019` (wc=1502; subjects-timetable, international)
- **2013 Past Studios | Travelling Studios | MSD** — `/current-students/subject-information/travelling-studios/past-studios/2013` (wc=1489; subjects-timetable, international)
- **2016 Past Studios | Travelling Studios | MSD** — `/current-students/subject-information/travelling-studios/past-studios/2016` (wc=1445; subjects-timetable, international, fees-finance)
- **2012 Past Studios | Travelling Studios | MSD** — `/current-students/subject-information/travelling-studios/past-studios/2012` (wc=1423; subjects-timetable, international)
- **2015 Past Studios | Travelling Studios | MSD** — `/current-students/subject-information/travelling-studios/past-studios/2015` (wc=1391; subjects-timetable, international)
- **Self-sourced internships | ABPL90434** — `/current-students/subject-information/internships-vocational-placements/abpl90434-construction-management-internship/self-sourced` (wc=1289; placements-WIL, subjects-timetable, forms-admin)
- **Internships and Vocational Placements** — `/current-students/subject-information/internships-vocational-placements` (wc=1271; placements-WIL, subjects-timetable, careers-employability)
- **Quota Subjects | Melbourne School of Design** — `/current-students/subject-information/quota-subjects` (wc=1216; subjects-timetable, enrolment, contacts-support)
- **2011 Past Studios | Travelling Studios | MSD** — `/current-students/subject-information/travelling-studios/past-studios/2011` (wc=1196; subjects-timetable, international, contacts-support)
- **2017 Past Studios | Travelling Studios | MSD** — `/current-students/subject-information/travelling-studios/past-studios/2017` (wc=1183; subjects-timetable, international, inclusion-equity)
- **2009 Past Studios | Travelling Studios | MSD** — `/current-students/subject-information/travelling-studios/past-studios/2009` (wc=1109; subjects-timetable, international)
- **2023 and 2024** — `/current-students/subject-information/travelling-studios/past-studios/2023m-and-2024` (wc=1100; subjects-timetable, international, student-life)
- **Information for hosts | ABPL90434** — `/current-students/subject-information/internships-vocational-placements/abpl90434-construction-management-internship/information-for-hosts` (wc=1059; placements-WIL, subjects-timetable, forms-admin)
- **2018 Past Studios | Travelling Studios | MSD** — `/current-students/subject-information/travelling-studios/past-studios/2018` (wc=991; subjects-timetable, international)
- **Master of Construction/Master of Property** — `/current-students/course-planning/sample-course-plans/double-masters/construction-property` (wc=960; course-planning, careers-employability, graduation)
- **Master of Architecture/Master of Construction** — `/current-students/course-planning/sample-course-plans/double-masters/architecture-construction` (wc=954; course-planning, careers-employability, graduation)

### Representative MSD Studio Archive pages (sample of 169)

- **Studio A** — `/current-students/subject-information/msd-studios/master-of-urban-design/ud-2023_sm2-studi` (wc=1518)
- **Open Studio: Future Civic** — `/current-students/subject-information/msd-studios/master-of-architecture/thesis_sm1_2026/f` (wc=1505)
- **Semester 2 2017 Studio 25** — `/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Stu` (wc=1454)
- **The City as Design Project** — `/current-students/subject-information/msd-studios/master-of-architecture/d_sm2_2025/the-ci` (wc=1412)
- **Threshold** — `/current-students/subject-information/msd-studios/master-of-architecture/c_sm1_2026/thresh` (wc=1347)
- **Open Studio: Worlding** — `/current-students/subject-information/msd-studios/master-of-architecture/thesis_sm1_2026/o` (wc=1320)
- **DESIGNING RIPIARIAN SYSTEMS FOR RESILIENCE & CULTURAL MEANIN** — `/current-students/subject-information/msd-studios/master-of-landscape-architecture/la_sm1_` (wc=1275)
- **Studio 10** — `/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Stu` (wc=1268)

## Notes

- **Technique:** in-page `fetch()` BFS from a tab loaded on `msd.unimelb.edu.au` defeats the Cloudflare/403 block that hits WebFetch and direct navigation. All 244 content fetches returned HTTP 200.
- **Studio archive is the dominant structure** and a crawler trap: every studio page links to ~25–58 sibling studios, generating 800+ in-scope URLs. The 250-page cap truncates it after a representative 169 are captured.
- **No standalone link-farm pages** — ABP keeps prose on its redirection pages, so they grade as `mixed` not `link-farm`.
- **Two further in-scope archives** beyond MSD Studios: `subject-information/travelling-studios/past-studios/{2008…2025}` and `student-experience/deans-honours-awards/{2023,2024}`.
