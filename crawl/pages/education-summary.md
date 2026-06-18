# Education — Current Students crawl summary

- **Faculty:** Education (Faculty of Education)
- **Root:** https://education.unimelb.edu.au/study/current-students
- **Scope prefix (PRE):** `/study/current-students` (in-scope = host `education.unimelb.edu.au` AND pathname === PRE or starts with PRE + `/`)
- **Crawl mode:** Exhaustive in-page `fetch()`-BFS (server-rendered, same-origin), DOMParser extraction
- **Crawled:** 2026-06-15
- **Pages captured:** 47 (0 fetch errors; all HTTP 200; caps 250/depth-6 not hit)
- **IA depth (max):** 4

## Counts

### By classification
| classification | pages |
|----------------|-------|
| unique | 32 |
| mixed | 10 |
| link-farm | 5 |
| redirect/broken | 0 |

### By depth
| depth | pages |
|-------|-------|
| 0 | 1 |
| 1 | 16 |
| 2 | 8 |
| 3 | 18 |
| 4 | 4 |

### By topic tag
| topic | pages |
|-------|-------|
| subjects-timetable | 25 |
| placements-WIL | 24 |
| exams-results | 23 |
| careers-employability | 23 |
| course-planning | 20 |
| enrolment | 15 |
| special-consideration | 13 |
| clubs-events | 7 |
| IT-systems | 5 |
| scholarships | 5 |
| academic-skills | 4 |
| fees-finance | 4 |
| contacts-support | 4 |
| forms-admin | 4 |
| student-life | 3 |
| wellbeing-health | 3 |
| graduation | 1 |
| research-candidature | 1 |

## Key structural finding
Education's Current-Students section is **unusually content-rich and self-hosted** compared with other faculties: 32 of 47 pages are unique prose and there are **no broken/redirect pages**. The depth comes almost entirely from one large, faculty-owned subtree — **Employability in Education → Master of Teaching → Placement Requirements / Placement Details** — which documents the teaching-placement (professional experience) program in detail. This content is inherently faculty-specific (initial teacher education, ITE) and cannot live on the central `students.unimelb.edu.au` hub.

Transactional/administrative tasks are still delegated to central systems: course/subject enrolment, timetable, special consideration, wellbeing and IT pages carry hub links (`students.unimelb.edu.au`, `my.unimelb.edu.au`) and `mixed` classification, but they wrap them in faculty-specific guidance rather than pure redirection.

## Section IA (in-scope tree)
```
/study
  /current-students
    /academic-skills-module
    /career-mentoring
    /course-enrolment
    /education-student-advisory-committee
    /employability-in-education
      /contact-us
      /faculty-of-education-scholarships
      /master-of-teaching
        /early-childhood
        /early-childhood-and-primary
        /faqs
        /permission-to-teach-ptt-information
        /placement-allocation-process
        /placement-details
          /placement-forms
          /placement-policies
        /placement-requirements
          /assessment
          /attendance-and-absences
          /health-and-safety
          /participation
          /placement-seminars
          /placement-structure
          /professional-conduct
          /roles-and-responsibilities
          /unsatisfactory-performance
          /working-with-children-check
        /primary
        /secondary
    /enrich-your-studies
      /graduate-education-ambassador-program
      /peer-mentoring
    /extension-assessment-information-and-policies
      /main-page-links
        /attendance-hurdles
        /foe-assessment-penalties
        /foe-extensions
        /reassessment
        /special-consideration
    /icas
    /international-study-opportunities
    /itea
    /literacy-and-numeracy-test-for-initial-teacher-education-students-lantite
    /resources-and-it
    /subject-enrolment
    /timetable
    /wellbeing-and-support
```

## Notable unique pages
- **Master of Teaching FAQs (single largest page, ~5.4k words)** — `/study/current-students/employability-in-education/master-of-teaching/faqs` (5447 words)
- **MTeach placement: roles & responsibilities** — `/study/current-students/employability-in-education/master-of-teaching/placement-requirements/roles-and-responsibilities` (1482 words)
- **Career mentoring program** — `/study/current-students/career-mentoring` (1457 words)
- **ICAS — Introduction to Contemporary Australian Schooling (ITE-specific)** — `/study/current-students/icas` (1142 words)
- **Education Student Advisory Committee** — `/study/current-students/education-student-advisory-committee` (927 words)
- **Permission to Teach (PtT) information** — `/study/current-students/employability-in-education/master-of-teaching/permission-to-teach-ptt-information` (875 words)
- **LANTITE — national literacy/numeracy test for ITE students** — `/study/current-students/literacy-and-numeracy-test-for-initial-teacher-education-students-lantite` (641 words)
- **iTEA — Initial Teacher Education Assessment (ITE-specific)** — `/study/current-students/itea` (560 words)
- `/study/current-students/employability-in-education/master-of-teaching/early-childhood-and-primary` — Early Childhood and Primary (1639 words)
- `/study/current-students/employability-in-education/master-of-teaching/early-childhood` — Early Childhood (1214 words)
- `/study/current-students/employability-in-education/master-of-teaching/primary` — Primary (982 words)
- `/study/current-students/employability-in-education/master-of-teaching/placement-requirements/assessment` — Assessment (961 words)

### ITE-specific content that justifies the subtree (cannot be central-hub content)
- **LANTITE** — `/study/current-students/literacy-and-numeracy-test-for-initial-teacher-education-students-lantite`
- **ICAS** — `/study/current-students/icas` (Introduction to Contemporary Australian Schooling)
- **iTEA** — `/study/current-students/itea` (Initial Teacher Education Assessment)
- **Academic Skills Module** — `/study/current-students/academic-skills-module`
- **Permission to Teach (PtT)** — `/study/current-students/employability-in-education/master-of-teaching/permission-to-teach-ptt-information`
- **Placement Requirements** (assessment, attendance, health & safety, professional conduct, roles & responsibilities, unsatisfactory performance, working-with-children check, etc.) — `/study/current-students/employability-in-education/master-of-teaching/placement-requirements/*`

## Link-farm / index-only pages (5)
Low-prose navigation nodes that exist only to hold child links (not broken — intentional section indexes):
- `/study/current-students/employability-in-education/contact-us`
- `/study/current-students/employability-in-education/master-of-teaching/placement-details`
- `/study/current-students/employability-in-education/master-of-teaching/placement-details/placement-forms`
- `/study/current-students/employability-in-education/master-of-teaching/placement-details/placement-policies`
- `/study/current-students/employability-in-education/master-of-teaching/placement-requirements`

## Outbound destinations (in-scope pages → off-scope hosts)
Link discovery runs over the whole document, so footer/megamenu nav inflates these counts; they indicate where the section points, not per-task redirection.

| host | link count |
|------|-----------|
| www.unimelb.edu.au | 331 |
| about.unimelb.edu.au | 189 |
| education.unimelb.edu.au | 169 |
| students.unimelb.edu.au | 95 |
| safety.unimelb.edu.au | 48 |
| staff.unimelb.edu.au | 47 |
| handbook.unimelb.edu.au | 25 |
| policy.unimelb.edu.au | 22 |
| study.unimelb.edu.au | 11 |
| canvas.lms.unimelb.edu.au | 8 |
| forms.your.unimelb.edu.au | 8 |
| scholarships.unimelb.edu.au | 8 |
| services.unimelb.edu.au | 7 |
| www.vit.vic.edu.au | 7 |

- **Social/footer (sitewide chrome):** www.facebook.com (95), www.instagram.com (94), www.linkedin.com (94), www.youtube.com (48)
- **`students.unimelb.edu.au`** (the central Current-Students hub) appears 95 times — concentrated on the enrolment / timetable / wellbeing / special-consideration pages.

## Auth-gated hosts (recorded as outbound-only; NOT crawled)
- `canvas.lms.unimelb.edu.au` (8 links)
- `services.unimelb.edu.au` (7 links)
- `lms.unimelb.edu.au` (5 links)
- `studentit.unimelb.edu.au` (2 links)
- `my.unimelb.edu.au` (1 links)

These are login-walled student systems (LMS/Canvas, my.unimelb, StudentIT, services) and are correctly treated as outbound references per scope rules.

## Method notes
- Site has **no `<main>` element**; content extracted from `#main-content` / `[role=main]` (falls back to `.uomcontent` → `body`). Topic tags and word counts are computed from this content region to exclude megamenu/footer boilerplate; link discovery and `outboundHosts` use the full document for IA completeness.
- BFS normalized URLs (strip query/hash/trailing slash), deduped, followed redirects, polite sequential fetches.
- Raw corpus: `crawl/pages/_education_raw_crawl.json`; finalized per-page records: `crawl/pages/education.json`.
