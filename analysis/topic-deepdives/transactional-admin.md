# Topic Deep-Dive: Transactional Admin

*Cross-faculty analysis from the full crawl — enrolment, exams & results, special consideration, fees, library. June 2026.*

**227 pages** across the faculty estate carry one of the five transactional tags — enrolment (84), exams & results (78), fees & finance (33), special consideration (25), library (7). This is the cluster the audit thesis bites hardest on. Unlike course-planning (where the volume is genuinely degree-specific) or subjects (where faculties own the content), the transactional spine is **centrally definitive**: the rules for how you enrol, what a grade means, how special consideration is adjudicated, when fees are due, and how the library works are set centrally on `students.unimelb.edu.au` and policy.unimelb.edu.au. The faculty pages here are overwhelmingly **restatements, local-process wrappers, or redirects** — and the crawl proves it: of all 227 pages, only **6 sit on students.unimelb.edu.au domain**, and 4 of those 6 surfaced *because Arts pages deep-link straight into students.unimelb.edu.au's canonical `course-admin/*` pages* (census dates, overloading, cross-institutional study, class timetable) rather than reproduce them. That is the consolidation argument in a single data point — when a faculty does it right, the crawler finds a students.unimelb.edu.au URL, not a faculty one. This is the **single clearest consolidation target in the estate.**

## Distribution — who holds it

| Faculty / unit | Enrol | Exams | Spec con | Fees | Library | **Total** | What dominates |
|---|--:|--:|--:|--:|--:|--:|---|
| Law | 25 | 24 | 3 | 6 | 2 | **60** | JD/MLM enrolment + grading restated per cohort; GRD student-profile false positives |
| Education | 15 | 23 | 13 | 4 | 0 | **55** | Placement/ITE assessment & extension wrappers; one MT FAQ (5,447w) absorbs everything |
| Architecture, Building & Planning (MSD) | 16 | 0 | 6 | 6 | 2 | **30** | Enrolment forms + extension form; studio-archive false positives on fees/library |
| Arts | 10 | 6 | 0 | 4 | 0 | **23** | Census/overloading/cross-institutional — but mostly **links to students.unimelb.edu.au's own pages** |
| Fine Arts & Music | 11 | 8 | 2 | 1 | 0 | **22** | Conservatorium enrolment/exam forms (genuinely local); thin link-farms |
| Medicine, Dentistry & Health Sciences | 3 | 11 | 0 | 3 | 0 | **17** | Placement assessment/conclusion pages tagged as exams; Dental forms |
| Business & Economics (FBE) | 1 | 3 | 0 | 9 | 0 | **13** | Assessment + Exam Viewing FAQ; PhD stipend/fee-remission pages |
| Engineering & IT (FEIT) | 3 | 3 | 1 | 0 | 0 | **7** | Orientation enrolment steps; one good extensions/spec-con page (1,347w) |
| **Total** | **84** | **78** | **25** | **33** | **7** | **227** | |

Two faculties — **Law and Education — hold 115 of 227 pages (51%)**. But this is not ownership in the course-planning sense; it is *volume of restatement*. Law's 60 pages are inflated by ~15 graduate-researcher profile pages (e.g. "Daria Vasilevskaia", "Charlie Hock") that the topic classifier swept in on stray keyword matches; Education's 55 are dominated by a single 5,447-word Master of Teaching FAQ that touches enrolment, assessment, extensions and special consideration all at once. Strip the false positives and what remains is a thin local layer over a centrally-owned spine.

**Domain signal (the headline):** 219 of 227 pages live on faculty/school domains, 6 on `students.unimelb.edu.au`, 2 are course-finder redirects to `study.unimelb.edu.au`. students.unimelb.edu.au *is* the source of truth; the faculty estate is the echo.

## The five sub-topics

### Enrolment (84) — the largest, and the most restated
students.unimelb.edu.au owns the transactional act of enrolment end-to-end: my.unimelb / the Student Portal, the [census-dates](https://students.unimelb.edu.au/course-admin/census-dates), [overloading](https://students.unimelb.edu.au/course-admin/planning-your-course-and-subjects/study-load/overloading), [cross-institutional study](https://students.unimelb.edu.au/course-admin/cross-institutional-study) and leave-of-absence machinery. What faculties legitimately host is a thin band of **local enrolment process**: form repositories (MSD "List of Forms", FFAM "Conservatorium Subject/Ensemble Enrolment Forms"), accept-your-offer/orientation steps (Law, FEIT), and cohort-specific rules (Law "JD subjects" / "MLM subjects", prerequisite waivers). Everything else is duplication — 22 of these pages are *mixed* (transactional content bolted onto a page about something else), and the four Arts pages that scored highest are literally students.unimelb.edu.au's own `course-admin/*` URLs picked up because Arts links to them. **Verdict: ~70% restatement/redirect, ~30% legitimate local process (forms, offer-acceptance, cohort rules).**

### Exams & Results (78) — grading is a central policy; faculties add penalty/hurdle local rules
The definition of grades, results release, exam timetabling and the Assessment and Results Policy are students.unimelb.edu.au/policy-owned. The genuinely faculty-specific slice is **local assessment rules**: hurdle requirements, attendance hurdles, penalty schedules, reassessment, exam-viewing (FBE "Exam Viewing FAQ", Education "FoE Assessment Penalties" / "Attendance Hurdles" / "Reassessment", Law "Student Achievement and Grading", FFAM "Conservatorium performance examinations"). But this topic is the noisiest: **Law contributes 24 pages of which the majority are graduate-researcher *profile* pages** misclassified by keyword, and MDHS's 11 are placement assessment/conclusion pages. Strip those and exams-results is a small set of real local-rule pages over a centrally-defined grading spine. **Verdict: heavy false-positive inflation; the real content is local assessment rules (legit) over centrally-owned grading definitions (duplicated).**

### Special Consideration (25) — the textbook centrally-owned policy
Special consideration is a **single university process** with one application path, governed centrally. There is nothing degree-specific about its rules. Yet 13 of 25 tagged pages are Education's (the MT FAQ again, plus "FoE Extensions", "Special Consideration", "Attendance and absences"), and the cleanest comparison in the whole topic is between FEIT's "Extensions and Special consideration" (1,347w — a full local restatement) and Law's "Special consideration" (598w — a near-verbatim restatement of the central policy with a local contact). These pages exist almost entirely to **re-explain a students.unimelb.edu.au policy in faculty voice**. The only legitimate faculty content is the *local extension* process where faculties genuinely hold discretion (short extensions, placement attendance), which is distinct from university special consideration. **Verdict: the purest duplication in the cluster — one central process, restated 25 times.**

### Fees & Finance (33) — almost none of this is real faculty fees content
Fees, due dates, payment, financial hardship, fee remission and Commonwealth assistance are entirely students.unimelb.edu.au/Stop-1-owned. The faculty estate has **essentially no legitimate fees content** — and the crawl shows it: of 33 tagged pages, the top hits are MSD travelling-studio and studio-archive pages (false positives on "fee"/"cost" mentions), Law study-overseas and locker-hire pages, and FBE *PhD stipend and fee-remission* scholarship pages (research-funding, not coursework fees). The only arguably-legitimate items are scholarship/grant pages and the Arts travel grant — and those belong under scholarships, not fees. **Verdict: ~90% false-positive or scholarship-adjacent; near-zero genuine faculty fees ownership. Pure consolidation/central-redirect territory.**

### Library (7) — not a faculty topic at all
The Library is a university-wide service (library.unimelb.edu.au) with its own site outside this crawl's faculty scope. The 7 pages tagged here are **noise**: two Arts 404 error pages, an MSD studio-archive pair, a Law "About the Centre and facilities" page (the Legal Academic Skills centre, not the library) and a 19-word link-farm. **Verdict: zero legitimate faculty library content; the topic confirms faculties don't — and shouldn't — host library material.**

## Legitimate vs central-overlapping

| Faculty-owned (cannot be centralised) | central-overlapping (consolidation candidates) |
|---|---|
| Local enrolment *forms* repositories (MSD, FFAM Conservatorium forms) | Generic "how to enrol / re-enrol" restatements |
| Accept-your-offer / orientation enrolment steps (Law, FEIT) | Special consideration policy restated per faculty (≈ the whole 25) |
| Cohort-specific subject rules & prerequisite waivers (Law JD/MLM) | Census dates / overloading / cross-institutional (students.unimelb.edu.au `course-admin/*` pages already canonical) |
| Local assessment rules: hurdles, penalties, reassessment, exam-viewing (FBE, Education, FFAM) | Grade-definition / results-release restatements |
| Faculty-discretion *extensions* (distinct from university spec-con) | All fees content except scholarships (≈ the whole 33) |
| Research-funding stipends & fee-remission (FBE — belongs under scholarships) | All library content (≈ the whole 7) |

The balance here is the inverse of course-planning. There, most content was legitimately faculty-owned. **Here, most of it is central-overlapping.** The legitimately-local residue is narrow: form repositories, offer-acceptance steps, and the genuine local-discretion bands (faculty extensions, assessment hurdles/penalties). Everything else restates a central rule or is a classifier false positive.

## Recommendation (transactional admin under central-and-spoke)

- **Declare students.unimelb.edu.au the single source of truth** for the transactional spine: enrolment mechanics, grading & results, special consideration, fees, and library. These pages already exist and are canonical on `students.unimelb.edu.au` and policy.unimelb.edu.au — the faculty restatements add maintenance cost and version-drift risk, not value.
- **Faculties link, never restate.** Replace every faculty page that re-explains a central process with a one-line signpost to students.unimelb.edu.au canonical page. The Arts pattern (deep-linking to `course-admin/census-dates`, `.../overloading`, `.../cross-institutional-study`) is the model the other faculties should copy — and the proof it works is that those are the only "faculty" pages the crawler resolved to a students.unimelb.edu.au URL.
- **Remove the duplicative pages outright** where there is no local discretion: the ~25 special-consideration restatements (keep only genuine faculty *extension* process), the ~33 fees pages (re-file the handful of scholarship/stipend pages under Scholarships; redirect the rest), and the library tag entirely.
- **Keep the narrow legitimate residue and label it clearly:** local enrolment *forms*, offer-acceptance/orientation steps, and local assessment rules (hurdles, penalties, reassessment, exam-viewing). These are the only pages with content students.unimelb.edu.au cannot hold.
- **Fix the "where to go" signpost.** Each faculty should expose one consistent "Enrolment, results & admin" landing page whose entire job is to (a) link to students.unimelb.edu.au's transactional pages and (b) surface the faculty's genuine local exceptions (forms, hurdles, extensions). One label, one location, across all eight faculties — so a student never has to guess whether enrolment lives centrally or locally. It lives centrally; the faculty page just points there.
- **Clean the classifier signal.** ~15 Law graduate-researcher profile pages and the MSD studio-archive cluster are false positives inflating these topics; excluding them sharpens the (already strong) duplication picture and should be reflected in the final page inventory.

---

## Appendix — all enrolment pages (84)

### Law — 25
- **5424w** — [Legal Research](https://law.unimelb.edu.au/students/jd/studies/enrolment/legal-research)
- **5424w** — [Legal Research](https://law.unimelb.edu.au/students/jd/studies/enrolment/legal-research/_recache)
- **2103w** — [JD subjects](https://law.unimelb.edu.au/students/jd/studies/enrolment/jd-subjects)
- **2103w** — [JD subjects](https://law.unimelb.edu.au/students/jd/studies/enrolment/jd-subjects/_recache)
- **1901w** — [MLM subjects](https://law.unimelb.edu.au/students/masters/studies/enrolment/mlm-subjects)
- **1901w** — [MLM subjects](https://law.unimelb.edu.au/students/masters/studies/enrolment/mlm-subjects/_recache)
- **1823w** · _mixed_ — [Accept Your Offer & Get Started | JD | University of Melbourne](https://law.unimelb.edu.au/students/jd/studies/accept-your-offer-and-get-started)
- **932w** — [Study Abroad at Oxford](https://law.unimelb.edu.au/students/masters/enrichment/global-learning-opportunities/study-abroad-at-oxford)
- **689w** · _mixed_ — [JD course planning and advice](https://law.unimelb.edu.au/students/jd/studies/course-planning)
- **594w** — [Enrolment and Re-Enrolment | Masters | Melbourne Law School](https://law.unimelb.edu.au/students/masters/studies/enrolment)
- **580w** — [Accept Your Offer & Get Started | Masters | Law at Melbourne](https://law.unimelb.edu.au/students/masters/studies/accept-your-offer-and-get-started)
- **516w** — [Enrolment and Re-Enrolment | JD | Melbourne Law School](https://law.unimelb.edu.au/students/jd/studies/enrolment)
- **509w** — [Orientation](https://law.unimelb.edu.au/students/orientation)
- **452w** — [Cross-Institutional Study](https://law.unimelb.edu.au/students/masters/studies/cross-institutional-study)
- **420w** — [Daria Vasilevskaia](https://law.unimelb.edu.au/students/grd/students/daria-vasilevskaia)
- **419w** — [Course Transfers and Early Exit Awards](https://law.unimelb.edu.au/students/masters/studies/course-transfers)
- **408w** — [Admission to Practice](https://law.unimelb.edu.au/students/admission-to-practice)
- **372w** — [Concurrent Diploma option with the JD](https://law.unimelb.edu.au/students/jd/studies/concurrent-diploma)
- **372w** · _mixed_ — [MLM student advising](https://law.unimelb.edu.au/students/masters/studies/student-advising)
- **283w** — [Leave of Absence](https://law.unimelb.edu.au/students/masters/studies/leave-of-absence)
- **248w** — [Prerequisites and Recommended Requirements](https://law.unimelb.edu.au/students/masters/studies/prerequisites-and-recommended-requirements)
- **196w** — [Legal Academic Skills LMS Community](https://law.unimelb.edu.au/students/legal-academic-skills/lms-community)
- **168w** — [Subject Prerequisite Waiver](https://law.unimelb.edu.au/students/jd/studies/waiver-of-subject-prerequisites)
- **149w** · _link-farm_ — [Ian Malkin Centre for Legal Academic Skills](https://law.unimelb.edu.au/students/legal-academic-skills)
- **130w** · _link-farm_ — [Student Published Research Prize](https://law.unimelb.edu.au/students/grd/scholarships-funding-and-prizes/sprp)

### ABP/MSD — 16
- **1239w** · _mixed_ — [Current Students | Melbourne School of Design](https://msd.unimelb.edu.au/current-students)
- **1216w** — [Quota Subjects | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/quota-subjects)
- **1001w** · _mixed_ — [Application for Extension](https://msd.unimelb.edu.au/current-students/enrolment/list-of-forms/application-for-extension)
- **596w** — [Subject Information | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information)
- **514w** · _mixed_ — [Enrolment | Current Students | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/enrolment)
- **417w** — [List of Forms | Current Students | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/enrolment/list-of-forms)
- **376w** — [Practical Experience](https://msd.unimelb.edu.au/current-students/subject-information/practical-experience)
- **356w** — [Subjects with a Travel Component](https://msd.unimelb.edu.au/current-students/subject-information/subjects-with-a-travel-component)
- **343w** — [Sample Course Plans](https://msd.unimelb.edu.au/current-students/course-planning/sample-course-plans)
- **343w** — [Master of Landscape Architecture Studios](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-landscape-architecture)
- **300w** — [Course Planning | Current Students | MSD](https://msd.unimelb.edu.au/current-students/course-planning)
- **297w** — [MSD Studios Archive](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive)
- **291w** — [2014 Studio Archive | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2014)
- **291w** — [2015 Studio Archive | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2015)
- **291w** — [2016 Studio Archive | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2016)
- **0w** · _redirect_ — [Redirecting...](https://msd.unimelb.edu.au/current-students/enrolment/list-of-forms/application-for-extension/extension-application-form)

### Education — 15
- **1482w** — [Roles and responsibilities](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/roles-and-responsibilities)
- **1457w** — [Career Mentoring](https://education.unimelb.edu.au/study/current-students/career-mentoring)
- **1457w** · _mixed_ — [Course Enrolment | Faculty of Education](https://education.unimelb.edu.au/study/current-students/course-enrolment)
- **1142w** — [Introduction to Contemporary Australian Schooling](https://education.unimelb.edu.au/study/current-students/icas)
- **1048w** · _mixed_ — [Student Timetabling | Faculty of Education](https://education.unimelb.edu.au/study/current-students/timetable)
- **927w** — [Education Student Advisory Committee](https://education.unimelb.edu.au/study/current-students/education-student-advisory-committee)
- **875w** — [Permission to Teach (PTT) Information](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/permission-to-teach-ptt-information)
- **795w** · _mixed_ — [Current Students | Faculty of Education](https://education.unimelb.edu.au/study/current-students)
- **641w** — [Literacy and Numeracy Test for Initial Teacher Education Students (LANTITE)](https://education.unimelb.edu.au/study/current-students/literacy-and-numeracy-test-for-initial-teacher-education-students-lantite)
- **524w** · _mixed_ — [Subject Enrolment](https://education.unimelb.edu.au/study/current-students/subject-enrolment)
- **475w** — [Health and safety](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/health-and-safety)
- **409w** · _mixed_ — [International Study | Faculty of Education](https://education.unimelb.edu.au/study/current-students/international-study-opportunities)
- **370w** · _mixed_ — [Student Services and IT](https://education.unimelb.edu.au/study/current-students/resources-and-it)
- **308w** — [Enrich your studies](https://education.unimelb.edu.au/study/current-students/enrich-your-studies)
- **293w** — [Reassessment](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/reassessment)

### FFAM — 11
- **716w** — [Conservatorium Ensemble Enrolment & Participation Forms](https://finearts-music.unimelb.edu.au/current-students/forms/conservatorium-ensemble-enrolment-and-participation-forms)
- **413w** — [Assessment and Program Approval forms](https://finearts-music.unimelb.edu.au/current-students/forms/assessment-program-aproval-forms)
- **409w** · _mixed_ — [Orientation](https://finearts-music.unimelb.edu.au/current-students/starting-out/orientation)
- **307w** — [Conservatorium performance examinations](https://finearts-music.unimelb.edu.au/current-students/assessment-and-exams/conservatorium-performance-timetable-and-examinations)
- **290w** — [Information for research students at the Faculty of Fine Arts & Music](https://finearts-music.unimelb.edu.au/current-students/research-students)
- **265w** — [Conservatorium Subject Enrolment Forms](https://finearts-music.unimelb.edu.au/current-students/forms/conservatorium-subject-enrolment-forms)
- **253w** — [Minor Music Performance](https://finearts-music.unimelb.edu.au/current-students/forms/conservatorium-subject-enrolment-forms/minor-music-performance)
- **191w** — [Conservatorium Special Permission Forms](https://finearts-music.unimelb.edu.au/current-students/forms/Conservatorium-Special-Permission-Forms)
- **131w** · _link-farm_ — [Enrolment for research students](https://finearts-music.unimelb.edu.au/current-students/research-students/enrolment)
- **119w** · _link-farm_ — [Graduate research seminar (Melbourne Conservatorium of Music)](https://finearts-music.unimelb.edu.au/current-students/research-students/graduate-research-seminar-melbourne-conservatorium-of-music)
- **77w** · _link-farm_ — [Fine Arts and Music Enrolment Assistance](https://finearts-music.unimelb.edu.au/current-students/forms/fine-arts-and-music-enrolment-assistance)

### Arts — 10
- **1212w** · _mixed_ — [Diploma in Languages](https://arts.unimelb.edu.au/students/undergraduate/enrich-your-bachelor-of-arts/diploma-in-languages)
- **987w** · _mixed_ — [Check your subject census dates : The University of Melbourne](https://students.unimelb.edu.au/course-admin/census-dates)
- **913w** · _mixed_ — [Course enrolment information](https://arts.unimelb.edu.au/students/graduate-research/commencement/course-enrolment-information)
- **913w** · _mixed_ — [Course enrolment information](https://arts.unimelb.edu.au/students/graduate-research/plan-your-program2/course-enrolment-information)
- **891w** — [Internship: Personal & Career Growth | UniMelb Arts](https://arts.unimelb.edu.au/students/experiential-learning/internship-personal-and-career-growth)
- **804w** — [Journalism Internship | Master of Journalism & International Journalism – UniMelb](https://arts.unimelb.edu.au/students/experiential-learning/journalism-internship-subject)
- **791w** — [EMA Internship Subject | Executive Master of Arts – UniMelb](https://arts.unimelb.edu.au/students/experiential-learning/ema-internship-subject)
- **718w** · _mixed_ — [Overloading | Current students | The University of Melbourne](https://students.unimelb.edu.au/course-admin/planning-your-course-and-subjects/study-load/overloading)
- **629w** · _mixed_ — [SCC Graduate Internship Subjects](https://arts.unimelb.edu.au/students/experiential-learning/scc-graduate-internship-subjects)
- **320w** — [Bachelor of Arts Orientation](https://arts.unimelb.edu.au/students/undergraduate/bachelor-of-arts-orientation)

### FEIT — 3
- **887w** — [Welcome to Melbourne: International Student Webinars](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/finalising-enrolment/enrolment-and-assistance)
- **553w** — [Intro to Uni](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/finalising-enrolment/accepting-offers)
- **474w** · _mixed_ — [Graduate Coursework Students (Domestic)](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/class-registration/enrolling-in-subjects)

### MDHS — 1
- **372w** — [Student Fitness to Practice](https://mdhs.unimelb.edu.au/study/current-students/student-fitness-to-practice)

### MBS (school) — 1
- **1057w** · _mixed_ — [Enrolment and Timetabling](https://mbs.unimelb.edu.au/students/course-planning/enrolment)

### Biomedical (school) — 1
- **836w** · _mixed_ — [Biomedicine Enrolment Advice Day](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/biomedicine-enrolment-advice-day)

### Dental (school) — 1
- **1013w** — [Forms](https://dental.unimelb.edu.au/study/student-resources/Forms)

## Appendix — all exams-results pages (78)

### Law — 24
- **976w** — [Student Achievement and Grading](https://law.unimelb.edu.au/students/jd/studies/student-achievement-and-grading)
- **709w** — [Becoming a Barrister](https://law.unimelb.edu.au/students/career-services/career-pathways/guide-to-becoming-a-barrister-in-victoria)
- **558w** — [Acceleration Guidelines](https://law.unimelb.edu.au/students/jd/studies/acceleration-guidelines)
- **522w** — [JD Rankings](https://law.unimelb.edu.au/students/jd/studies/rankings)
- **420w** — [Andrea Furger](https://law.unimelb.edu.au/students/grd/students/andrea-furger)
- **419w** — [Course Transfers and Early Exit Awards](https://law.unimelb.edu.au/students/masters/studies/course-transfers)
- **408w** — [Admission to Practice](https://law.unimelb.edu.au/students/admission-to-practice)
- **400w** — [Marcus Hickleton](https://law.unimelb.edu.au/students/grd/students/marcus-hickleton)
- **312w** — [Charlie Hock](https://law.unimelb.edu.au/students/grd/students/charlie-hock)
- **306w** — [Lauren Bellamy](https://law.unimelb.edu.au/students/grd/students/lauren-bellamy)
- **304w** — [Aashish Yadav](https://law.unimelb.edu.au/students/grd/students/aashish-yadav)
- **293w** — [Emma Finlay](https://law.unimelb.edu.au/students/grd/students/emma-finlay)
- **283w** — [Jasmine Ali](https://law.unimelb.edu.au/students/grd/students/jasmine-ali)
- **281w** — [Fitria Ratna Wardika](https://law.unimelb.edu.au/students/grd/students/fitria-ratna-wardika)
- **269w** — [Jessica Bridges](https://law.unimelb.edu.au/students/grd/students/jessica-bridges)
- **261w** — [Yanjie (Andrew) Zhu](https://law.unimelb.edu.au/students/grd/students/yanjie-zhu)
- **246w** — [Lydie Schmidt](https://law.unimelb.edu.au/students/grd/students/lydie-schmidt)
- **240w** — [Lilia Anderson](https://law.unimelb.edu.au/students/grd/students/lilia-anderson)
- **235w** — [Elisabeth Lopez Desvars](https://law.unimelb.edu.au/students/grd/students/elisabeth-lopez-desvars)
- **233w** — [Tina Yao](https://law.unimelb.edu.au/students/grd/students/tina-yao)
- **203w** — [Early Academic Guidance for Legal Education](https://law.unimelb.edu.au/students/legal-academic-skills/facilitated-study-groups)
- **197w** — [Haris Jamil](https://law.unimelb.edu.au/students/grd/students/haris-jamil)
- **109w** · _link-farm_ — [Writing for law](https://law.unimelb.edu.au/students/legal-academic-skills/writing-for-law)
- **69w** · _link-farm_ — [Academic skills resources](https://law.unimelb.edu.au/students/legal-academic-skills/academic-skills-resources)

### Education — 23
- **5447w** — [FAQs](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/faqs)
- **1639w** — [Early Childhood and Primary](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/early-childhood-and-primary)
- **1482w** — [Roles and responsibilities](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/roles-and-responsibilities)
- **1277w** · _mixed_ — [Academic Skills module](https://education.unimelb.edu.au/study/current-students/academic-skills-module)
- **982w** — [Primary](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/primary)
- **961w** — [Assessment](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/assessment)
- **950w** — [Secondary](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/secondary)
- **795w** · _mixed_ — [Current Students | Faculty of Education](https://education.unimelb.edu.au/study/current-students)
- **697w** — [Professional Conduct](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/professional-conduct)
- **689w** — [Unsatisfactory performance](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/unsatisfactory-performance)
- **641w** — [Literacy and Numeracy Test for Initial Teacher Education Students (LANTITE)](https://education.unimelb.edu.au/study/current-students/literacy-and-numeracy-test-for-initial-teacher-education-students-lantite)
- **560w** — [Initial Teacher Education Assessment](https://education.unimelb.edu.au/study/current-students/itea)
- **524w** · _mixed_ — [Subject Enrolment](https://education.unimelb.edu.au/study/current-students/subject-enrolment)
- **512w** — [Master of Teaching](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching)
- **479w** — [Attendance and absences](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/attendance-and-absences)
- **402w** — [FoE Assessment Penalties](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/foe-assessment-penalties)
- **370w** · _mixed_ — [Student Services and IT](https://education.unimelb.edu.au/study/current-students/resources-and-it)
- **369w** — [FoE Extensions](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/foe-extensions)
- **309w** — [Participation](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/participation)
- **300w** — [Attendance Hurdles](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/attendance-hurdles)
- **293w** — [Reassessment](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/reassessment)
- **225w** — [Special Consideration](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/special-consideration)
- **182w** — [Assessment, Results and Academic Integrity](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies)

### MDHS — 10
- **925w** · _mixed_ — [Employability in MDHS](https://mdhs.unimelb.edu.au/study/current-students/employability-in-mdhs)
- **740w** — [Working with Children Check](https://mdhs.unimelb.edu.au/study/current-students/placements/students/requirements/non-immunisation-checks/wwcc)
- **468w** — [Emily Sun](https://mdhs.unimelb.edu.au/study/current-students/student-enrichment/mentoring-programs/chancellors-scholars/emily-sun)
- **409w** — [Department of Physiotherapy](https://mdhs.unimelb.edu.au/study/current-students/placements/org/department-of-physiotherapy-resources)
- **402w** — [Conclusion of Placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/dsp/conclusion-of-placement)
- **378w** — [Professional Psychology](https://mdhs.unimelb.edu.au/study/current-students/placements/org/msps/professional-psychology)
- **329w** — [Examples of Concerns](https://mdhs.unimelb.edu.au/study/current-students/student-fitness-to-practice/examples-of-concerns)
- **287w** — [During Placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/mspgh/during-placement)
- **286w** — [Before placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/department-of-social-work-resources/before-placement)
- **244w** — [Conclusion of Placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/mspgh/conclusion-of-placement)

### FFAM — 8
- **831w** — [MCM Director's Writing Up Award](https://finearts-music.unimelb.edu.au/current-students/research-students/grants/mcm-directors-writing-up-award)
- **799w** — [Current student info: Master of Music (Research)](https://finearts-music.unimelb.edu.au/current-students/research-students/master-of-music-research-in-music-performance)
- **792w** — [Conservatorium accompanists](https://finearts-music.unimelb.edu.au/current-students/assessment-and-exams/conservatorium-accompanists)
- **711w** · _mixed_ — [Employability in Fine Arts and Music](https://finearts-music.unimelb.edu.au/current-students/employability-in-fine-arts-and-music)
- **413w** — [Assessment and Program Approval forms](https://finearts-music.unimelb.edu.au/current-students/forms/assessment-program-aproval-forms)
- **307w** — [Conservatorium performance examinations](https://finearts-music.unimelb.edu.au/current-students/assessment-and-exams/conservatorium-performance-timetable-and-examinations)
- **77w** · _link-farm_ — [Fine Arts and Music Enrolment Assistance](https://finearts-music.unimelb.edu.au/current-students/forms/fine-arts-and-music-enrolment-assistance)
- **43w** · _link-farm_ — [Practical Music and Performance Timetable](https://finearts-music.unimelb.edu.au/current-students/bookings-and-timetables/pcme-practical-music-timetable)

### Arts — 6
- **1418w** · _mixed_ — [Cross-institutional study](https://students.unimelb.edu.au/course-admin/cross-institutional-study)
- **718w** · _mixed_ — [Overloading | Current students | The University of Melbourne](https://students.unimelb.edu.au/course-admin/planning-your-course-and-subjects/study-load/overloading)
- **331w** — [Audio/Visual loan equipment](https://arts.unimelb.edu.au/students/audiovisual-loan-equipment)
- **316w** · _mixed_ — [Class timetable | Current students | The University of Melbourne](https://students.unimelb.edu.au/course-admin/class-timetable)
- **306w** — [Industry Project (ARTS30001)](https://arts.unimelb.edu.au/students/experiential-learning/industry-project)
- **100w** · _link-farm_ — [ArtsModules](https://arts.unimelb.edu.au/students/graduate-research/manage-your-research-program/enrichment-activities/artsmodules)

### FEIT — 3
- **697w** — [Not-for-Credit Internships](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/practice-hurdle/internship-no-credit)
- **516w** — [Engineering Practice Hurdle](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/practice-hurdle)
- **469w** — [Skills Towards Employment Program](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/practice-hurdle/step)

### FBE — 2
- **1039w** — [Assessment](https://fbe.unimelb.edu.au/students/bcom/current-students/assessment)
- **735w** — [Exam Viewing FAQ](https://fbe.unimelb.edu.au/students/bcom/current-students/assessment/exam-viewing-faq)

### MBS (school) — 1
- **1213w** — [Assessment](https://mbs.unimelb.edu.au/students/course-planning/assessment)

### Biomedical (school) — 1
- **166w** · _redirect_ — [Biochemistry and Molecular Biology - The University of Melbourne](https://study.unimelb.edu.au/find/courses/major/biochemistry-and-molecular-biology/)

## Appendix — all special-consideration pages (25)

### Education — 13
- **5447w** — [FAQs](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/faqs)
- **1457w** · _mixed_ — [Course Enrolment | Faculty of Education](https://education.unimelb.edu.au/study/current-students/course-enrolment)
- **1048w** · _mixed_ — [Student Timetabling | Faculty of Education](https://education.unimelb.edu.au/study/current-students/timetable)
- **641w** — [Literacy and Numeracy Test for Initial Teacher Education Students (LANTITE)](https://education.unimelb.edu.au/study/current-students/literacy-and-numeracy-test-for-initial-teacher-education-students-lantite)
- **479w** — [Attendance and absences](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/attendance-and-absences)
- **475w** — [Health and safety](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/health-and-safety)
- **435w** · _mixed_ — [Wellbeing and Support | Faculty of Education](https://education.unimelb.edu.au/study/current-students/wellbeing-and-support)
- **402w** — [FoE Assessment Penalties](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/foe-assessment-penalties)
- **369w** — [FoE Extensions](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/foe-extensions)
- **300w** — [Attendance Hurdles](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/attendance-hurdles)
- **293w** — [Reassessment](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/reassessment)
- **225w** — [Special Consideration](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/special-consideration)
- **182w** — [Assessment, Results and Academic Integrity](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies)

### ABP/MSD — 6
- **1239w** · _mixed_ — [Current Students | Melbourne School of Design](https://msd.unimelb.edu.au/current-students)
- **1001w** · _mixed_ — [Application for Extension](https://msd.unimelb.edu.au/current-students/enrolment/list-of-forms/application-for-extension)
- **811w** — [Yern-da-ville](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/c_sm1_2026/yern-da-ville)
- **570w** — [Semester 1 2017 Thesis 1](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/the_2017_SM1-studios/semester-1-2017-thesis-1)
- **514w** · _mixed_ — [Enrolment | Current Students | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/enrolment)
- **0w** · _redirect_ — [Redirecting...](https://msd.unimelb.edu.au/current-students/enrolment/list-of-forms/application-for-extension/extension-application-form)

### Law — 3
- **660w** — [Extensions](https://law.unimelb.edu.au/students/academic-support-and-wellbeing/wellbeing/extensions)
- **598w** — [Special consideration](https://law.unimelb.edu.au/students/academic-support-and-wellbeing/wellbeing/special-consideration)
- **418w** — [Registration for ongoing support](https://law.unimelb.edu.au/students/academic-support-and-wellbeing/wellbeing/registration-for-ongoing-support)

### FFAM — 2
- **413w** — [Assessment and Program Approval forms](https://finearts-music.unimelb.edu.au/current-students/forms/assessment-program-aproval-forms)
- **191w** — [Conservatorium Special Permission Forms](https://finearts-music.unimelb.edu.au/current-students/forms/Conservatorium-Special-Permission-Forms)

### FEIT — 1
- **1347w** — [Extensions and Special consideration](https://eng.unimelb.edu.au/students/coursework/study-resources/extensions-and-special-consideration)

## Appendix — all fees-finance pages (33)

### MBS (school) — 7
- **1152w** — [Master of Management (Accounting and Finance)](https://mbs.unimelb.edu.au/students/course-planning/course-plans/masters-programs/master-of-management-accounting-finance-200-points)
- **920w** — [Master of Finance (Enhanced) - Research Pathway](https://mbs.unimelb.edu.au/students/course-planning/course-plans/masters-programs/master-of-finance-enhanced-research-pathway)
- **918w** — [Master of Finance (Enhanced)](https://mbs.unimelb.edu.au/students/course-planning/course-plans/masters-programs/master-of-finance-enhanced)
- **854w** — [Master of Management (Finance) 200 point](https://mbs.unimelb.edu.au/students/course-planning/course-plans/masters-programs/master-of-management-finance-200-point)
- **846w** — [Master of Finance - Research Pathway](https://mbs.unimelb.edu.au/students/course-planning/course-plans/masters-programs/master-of-finance-research-pathway)
- **844w** — [Master of Finance](https://mbs.unimelb.edu.au/students/course-planning/course-plans/masters-programs/master-of-finance)
- **841w** — [Master of Management (Finance) 150 points](https://mbs.unimelb.edu.au/students/course-planning/course-plans/masters-programs/master-of-management-finance-150-point)

### Law — 6
- **1388w** · _mixed_ — [Study Overseas program](https://law.unimelb.edu.au/students/study-overseas-program)
- **1220w** · _mixed_ — [Non-partner programs](https://law.unimelb.edu.au/students/non-partner-programs)
- **1087w** — [University of Oxford BCL or MLF](https://law.unimelb.edu.au/students/jd/enrichment/global-learning-opportunities/degree-partnerships/oxford)
- **508w** — [Student Cards and Law Students' Study Area](https://law.unimelb.edu.au/students/law-students-study-area)
- **236w** — [Nimna Prematilaka](https://law.unimelb.edu.au/students/grd/students/nimna-prematilaka)
- **190w** — [MLM student locker hire](https://law.unimelb.edu.au/students/masters/studies/locker-hire)

### ABP/MSD — 6
- **1445w** — [2016 Past Studios | Travelling Studios | MSD](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2016)
- **910w** — [Nightingale Night School](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/thesis_sm1_2026/nightingale-night-school)
- **831w** — [Travelling Studios | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios)
- **571w** — [Semester 2 2017 Thesis 5](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/THE-2017_SM2-Studios/thesis-5)
- **557w** — [Semester 2 2017 Studio 9](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-9)
- **494w** — [Studio H: Housing](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/mup-2017_SM1-studios/studio-h)

### Arts — 4
- **987w** · _mixed_ — [Check your subject census dates : The University of Melbourne](https://students.unimelb.edu.au/course-admin/census-dates)
- **580w** · _mixed_ — [Bachelor of Arts (Degree with Honours) - The University of Melbourne](https://study.unimelb.edu.au/find/courses/honours/bachelor-of-arts-degree-with-honours/?referrer=arts_redirect)
- **194w** — [Faculty of Arts Travel Grant](https://arts.unimelb.edu.au/students/overseas-experience/funding/faculty-of-arts-overseas-subject-travel-grant)
- **194w** — [Faculty of Arts Travel Grant](https://arts.unimelb.edu.au/students/graduate-coursework/enrich-your-program/overseas-experience/funding/faculty-of-arts-overseas-subject-travel-grant)

### Education — 4
- **1457w** · _mixed_ — [Course Enrolment | Faculty of Education](https://education.unimelb.edu.au/study/current-students/course-enrolment)
- **391w** · _mixed_ — [Faculty of Education Scholarships](https://education.unimelb.edu.au/study/current-students/employability-in-education/faculty-of-education-scholarships)
- **370w** · _mixed_ — [Student Services and IT](https://education.unimelb.edu.au/study/current-students/resources-and-it)
- **80w** · _link-farm_ — [Placement policies](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-details/placement-policies)

### Dental (school) — 3
- **1013w** — [Forms](https://dental.unimelb.edu.au/study/student-resources/Forms)
- **660w** — [Research](https://dental.unimelb.edu.au/study/student-resources/Research)
- **571w** — [Melbourne Dental School Internal Grants](https://dental.unimelb.edu.au/study/student-resources/Research/mds-internal-grants)

### FBE — 2
- **732w** · _mixed_ — [FBE Doctoral Program Stipend and Tuition (Fee Remission) Scholarships](https://fbe.unimelb.edu.au/students/phd/scholarships-and-grants/stipends-and-fee-remissions/fbe-doctoral-program-stipend-and-tuition-fee-remission-scholarships)
- **642w** — [Stipends and fee remissions](https://fbe.unimelb.edu.au/students/phd/scholarships-and-grants/stipends-and-fee-remissions)

### FFAM — 1
- **305w** — [Instrument Loans | Faculty of Fine Arts & Music | UniMelb](https://finearts-music.unimelb.edu.au/current-students/facilities/conservatorium-instrument-loans)

## Appendix — all library pages (7)

### Arts — 3
- **359w** — [Research support](https://arts.unimelb.edu.au/students/graduate-research/faqs/research-support)
- **105w** · _redirect_ — [404 : Page not found | Error](https://arts.unimelb.edu.au/students/undergraduate/enrich-your-bachelor-of-arts/academic-mentoring/dr-lara-anderson)
- **80w** · _redirect_ — [404 : Page not found | Error](https://arts.unimelb.edu.au/students/experiential-learning-archive)

### Law — 2
- **191w** — [About the Centre and facilities](https://law.unimelb.edu.au/students/legal-academic-skills/about)
- **19w** · _link-farm_ — [Academic Support and Wellbeing](https://law.unimelb.edu.au/students/academic-support-and-wellbeing)

### ABP/MSD — 2
- **1012w** — [Summer 2018 Studio 5](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SUM-Studios/studio-5)
- **749w** — [Domesticity Inside Out](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/d_sm1_2026/domesticity-inside-out)
