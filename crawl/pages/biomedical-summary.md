# Biomedical Sciences (School) — Current Student Information crawl summary

- **Unit:** School of Biomedical Sciences (slug: `biomedical`)
- **Parent faculty:** MDHS (Medicine, Dentistry & Health Sciences)
- **Root:** https://biomedicalsciences.unimelb.edu.au/study/current-student-information
- **Scope prefix (PRE):** `/study/current-student-information` (host `biomedicalsciences.unimelb.edu.au`)
- **Crawl mode:** in-page fetch-BFS (same-origin), live-nav fallback for cross-origin redirects; localStorage-persisted queue/visited; corpus POSTed to 127.0.0.1:8117
- **Crawled:** 2026-06-15
- **Pages captured:** 42  (cap 250 / depth 6 — neither hit; BFS converged naturally)

## Key structural finding
The School of Biomedical Sciences runs a **separate, substantive current-students section on its own subdomain** (`biomedicalsciences.unimelb.edu.au`), entirely distinct from the thin MDHS faculty hub (`mdhs.unimelb.edu.au/study/current-students`). This documents **school-level fragmentation within MDHS**: a Biomedicine / Biomedical-Science student must move between the central hub (`students.unimelb.edu.au`), the MDHS faculty hub, AND this school site for different needs.

The section is genuinely content-rich (21 unique prose pages, 280–1660 words) — not a pass-through. It is organised into **two program subtrees** plus two standalone pages:
- `/plan-your-bachelor-of-biomedicine/*` — Bachelor of Biomedicine planning hub (majors, breadth, first-year subjects, study-plan templates, Deans' Honours, careers, study abroad/exchange, UROP, societies, enrolment advice day, graduate pathways, concurrent diplomas)
- `/master-of-biomedical-science/*` — Master of Biomedical Science (course planning, academic skills, orientation, Deans' Honours, clubs)
- `/quota-subjects` and `/biom30003-biomedical-science-research-project` — standalone, school-specific (capacity-limited lab/field subjects; undergraduate research subject). Content that genuinely could **not** be centralised.

## Counts by classification
- **unique:** 21
- **mixed:** 3
- **link-farm:** 0
- **redirect/broken:** 18

## Counts by depth
- depth 0: 1
- depth 1: 6
- depth 2: 19
- depth 3: 16

- **iaDepthMax:** 3

## Topic tags (page counts; controlled vocab)
- course-planning: 37
- forms-admin: 34
- orientation: 24
- careers-employability: 17
- wellbeing-health: 9
- IT-systems: 5
- clubs-events: 5
- research-candidature: 4
- placements-WIL: 4
- student-life: 2
- subjects-timetable: 2
- academic-skills: 2
- contacts-support: 1
- enrolment: 1
- graduation: 1
- international: 1
- exams-results: 1
> `forms-admin` and `orientation` are inflated by shared page chrome/footer links on every page; **`course-planning` (37) is the dominant genuine theme** — this is overwhelmingly a course-planning section, with secondary careers-employability and (Master) research-candidature content.

## Broken / circular / redirecting links (notable)
**18 of 42 captured URLs are redirect/broken**, splitting into two groups:

1. **Two prominent hub links that misroute / require auth (depth 1):**
   - `/student-portal` → **302 to `sso.unimelb.edu.au` SAML sign-in** (auth-gated; outbound-only, not crawled).
   - `/university-health-hub` → **302 to `mdhs.unimelb.edu.au/about/contact`** (generic MDHS *Contact* page). A link labelled "University Health Hub" landing on a faculty contact page is an effectively **broken/misrouted link**.
2. **Sixteen Bachelor-of-Biomedicine 'major' pages (depth 3)** under `/plan-your-bachelor-of-biomedicine/majors/bachelor-of-biomedicine-majors/*` — each an in-scope URL that **immediately redirects current students OUT to the prospective-student catalogue** `study.unimelb.edu.au/find/courses/major/*` (e.g. `genetics2 → .../major/genetics`). IA-hygiene smell: **14 of 16 slugs carry a `2` suffix** (`biochemistry-and-molecular-biology2`, `neuroscience2`, …) while 2 do not (`infection-and-immunity`, `public-health-and-epidemiology`) — evidence of **duplicate/versioned CMS slugs**.

**Circular self-link (confirmed):** the hub shows a program card **"Bachelor of Science — Access resources to help you plan your Bachelor of Science"** whose link points back to the hub root itself (`/study/current-student-information`). Unlike Biomedicine and Master of Biomedical Science, **Bachelor of Science has no dedicated subtree** — the card is a no-op loop back to the same page.

## Section IA (tree of in-scope URLs)
```
(root) current-student-information  [unique]
  biom30003-biomedical-science-research-project  [unique]
  master-of-biomedical-science  [unique]
    academic-skills  [unique]
    course-planning  [unique]
    deans-honours-list  [unique]
    orientation  [unique]
    student-clubs-and-societies  [unique]
  plan-your-bachelor-of-biomedicine  [unique]
    academic-skills  [unique]
    biomedicine-deans-honours-list  [unique]
    biomedicine-enrolment-advice-day  [mixed]
    biomedicine-graduate-pathways  [unique]
    breadth  [unique]
    concurrent-diplomas  [unique]
    majors  [unique]
        biochemistry-and-molecular-biology2  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/biochemistry-and-molecular-biology]
        bioengineering-systems2  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/biomedical-engineering-systems]
        biotechnology2  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/biotechnology]
        cell-and-developmental-biology2  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/cell-and-developmental-biology]
        genetics2  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/genetics]
        human-nutrition2  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/human-nutrition]
        human-structure-and-function2  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/human-structure-and-function]
        immunology2  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/immunology]
        infection-and-immunity  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/infection-and-immunity]
        microbiology-and-immunology2  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/microbiology]
        neuroscience2  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/neuroscience]
        pathology2  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/pathology]
        pharmacology2  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/pharmacology]
        physiology2  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/physiology]
        psychology2  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/psychology]
        public-health-and-epidemiology  [redirect/broken]  ->[https://study.unimelb.edu.au/find/courses/major/public-health-and-epidemiology]
    orientation  [unique]
    plan-your-first-year-subjects  [mixed]
    student-societies  [unique]
    study-abroad-and-exchange  [unique]
    study-plan-templates  [mixed]
    urop  [unique]
    your-career  [unique]
  quota-subjects  [unique]
  student-portal  [redirect/broken]  ->[https://sso.unimelb.edu.au/app/universityofmelbourne_studentportal_1/.../sso/saml]
  university-health-hub  [redirect/broken]  ->[https://mdhs.unimelb.edu.au/about/contact]
```

## Top outbound destinations (aggregate link counts)
- study.unimelb.edu.au: 298  [prospective catalogue]
- www.unimelb.edu.au: 280
- about.unimelb.edu.au: 192
- handbook.unimelb.edu.au: 94  [handbook]
- biomedicalsciences.unimelb.edu.au: 84
- www.facebook.com: 70
- www.linkedin.com: 64
- www.instagram.com: 64
- safety.unimelb.edu.au: 40
- forms.your.unimelb.edu.au: 34
- www.youtube.com: 26
- students.unimelb.edu.au: 26  [central CS hub]
- vimeo.com: 16
- www.tiktok.com: 16
- mdhs.unimelb.edu.au: 9
> Leans heavily on **`study.unimelb.edu.au` (298)** and **`handbook.unimelb.edu.au` (94)** for canonical course/subject detail, plus social channels (facebook/linkedin/instagram) for community; **`students.unimelb.edu.au` (26)** for central services. The section owns the *planning narrative* but delegates canonical course/subject data outward.

## Notable unique pages (substantive, wc≥700)
- **BIOM30003 Biomedical Science Research Project** (1663 words) — `/study/current-student-information/biom30003-biomedical-science-research-project`
  - This project (BIOM30003) is designed for undergraduate students who have achieved excellent results in the discipline related to the project, to help develop pr
- **Biomedicine Deans' Honours List** (1543 words) — `/study/current-student-information/plan-your-bachelor-of-biomedicine/biomedicine-deans-honours-list`
  - Recognising our highest achieving Bachelor of Biomedicine students The Dean's Honours ListThe Dean's Honours List is an annual award made to the top performing 
- **Breadth** (1459 words) — `/study/current-student-information/plan-your-bachelor-of-biomedicine/breadth`
  - Did you know that your Bachelor of Biomedicine isn’t filled with just ‘Biomedicine’? Did you know you can study management, communication, language or music? Th
- **Quota Subjects** (1452 words) — `/study/current-student-information/quota-subjects`
  - Find out about the laboratory or fieldwork subjects where enrolment capacity is limited by available resources, including how and when to apply. Quota SubjectsS
- **Majors** (1147 words) — `/study/current-student-information/plan-your-bachelor-of-biomedicine/majors`
  - Biochemistry & Molecular Biology Study the structure and function of components of living cells, to understand the biological processes that enable all living t
- **Student Societies** (809 words) — `/study/current-student-information/plan-your-bachelor-of-biomedicine/student-societies`
  - University is more than just completing your studies. Student societies are a way to find and follow any extra curricula interests, a great place to make new fr
- **Study Abroad and Exchange** (740 words) — `/study/current-student-information/plan-your-bachelor-of-biomedicine/study-abroad-and-exchange`
  - Study overseas to enhance your Melbourne Degree, while making friends from around the world. As part of your studies at the University of Melbourne, we encourag
- **Course Planning** (710 words) — `/study/current-student-information/master-of-biomedical-science/course-planning`
  - Congratulations on joining the Master of Biomedical Science cohort! Information on this page will assist you with your course planning decisions. Course Structu

## Auth-gated hosts referenced (outbound-only, NOT crawled per spec)
- my.unimelb.edu.au
- services.unimelb.edu.au
- sso.unimelb.edu.au

## Method notes
- In-page `fetch()`-BFS over the same-origin subtree (DOMParser extraction). Two depth-1 URLs (`student-portal`, `university-health-hub`) failed `fetch()` (`TypeError: Failed to fetch`) because they **302 to cross-origin hosts** (CORS blocks the redirected response); resolved by **live browser navigation** in the agent's own tab to observe the true redirect targets.
- Excerpts for the 24 substantive pages were re-extracted with page chrome (nav/header/footer/megamenu/script/style) removed; redirect/broken pages carry descriptive excerpts. Word counts derive from the original `main` text and were unaffected by chrome — all `unique` pages clear the 160-word threshold on body prose.