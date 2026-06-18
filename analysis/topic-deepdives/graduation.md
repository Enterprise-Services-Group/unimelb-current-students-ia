# Topic Deep-Dive: Graduation

*Cross-faculty analysis from the full crawl. June 2026.*

**125 graduation-tagged pages** sit across the faculty estate — a mid-sized topic, but the tag is a near-total misnomer. Almost none of it is about the graduation *ceremony* or the transactional spine of *completing* a degree (apply to graduate, eligibility, eStudent, the ceremony itself) — that material lives on the central hub and is barely tagged here. What the tag actually captures is the **end-of-degree lifecycle as faculties experience it**: research-candidature milestones and thesis submission, honours and Dean's-award recognition, graduate-research prizes and travel grants, and graduate-cohort enrichment. It is overwhelmingly **faculty-owned and discipline-bound**, dominated by a single faculty (Arts), with a thin layer of hub-overlapping orientation/enrolment restatements.

## Distribution — who holds it

| Unit | Pages | What dominates |
|---|--:|---|
| Arts | 61 | Graduate-research candidature lifecycle (milestones → thesis → conversion) + UG/PG enrichment |
| Engineering & IT (FEIT) | 21 | Graduate-research scholarships, prizes, travel grants + graduate orientation |
| Architecture, Building & Planning (MSD) | 20 | Dean's Honours Awards, mentoring, sample course plans |
| Medicine, Dentistry & Health Sciences | 11 | Placement conclusion + student-enrichment / mentoring |
| Fine Arts & Music | 8 | Research-student progress reviews, grants, enrolment |
| Business & Economics (FBE) | 2 | Graduate-researcher prizes + Dean's Honours List |
| Education | 1 | Master of Teaching (Early Childhood) |
| Biomedical Sciences (school · MDHS) | 1 | Biomedicine Graduate Pathways |
| **Total** | **125** | |

Arts alone holds **49%** of the topic — almost all of it the graduate-research candidature pathway (`/students/graduate-research/...`). Together Arts and FEIT account for **66%**: this tag is really "graduate-research lifecycle + recognition," concentrated in the two faculties with the deepest research-candidature content.

## Types of Graduation content

1. **Graduate-research candidature lifecycle** — the spine of the topic: commencing, progressing, and completing a higher-degree-by-research. *Arts* is the whole story here — "Milestone reviews" (1,517w), "Candidature variations" (1,254w), "Thesis submission" / "Thesis requirements", "Course conversion" (MA↔PhD), "Manage your candidature", "Commence your candidature". Excerpts confirm these are progression-to-completion pages ("converting from a MA to a PhD and PhD to MA"), not ceremony pages.

2. **Honours & Dean's-list recognition** — completion-with-distinction content. *MSD* "Dean's Honours Awards 2024 / 2023" (1,924w / 1,877w) and "Dean's Honours Awards & Prizes"; *FBE* "Dean's Honours List 2024"; the cross-listed *Arts* "Bachelor of Arts (Degree with Honours)" study-site redirect. This is genuinely end-of-degree, genuinely faculty-specific.

3. **Graduate-research prizes, awards & travel grants** — recognition and funding tied to research completion. *FEIT* dominates: "Graduate Research Prizes", "PhD Write Up Award", "Engineering and IT Conference Travel Grant" (1,739w), "Scholarships for Graduate Researchers", Summer/Winter/Other scholarship rounds; *FBE* "Graduate researcher prizes and awards"; *FFAM* "Grants and internal funding", "Scholarships & Studentships".

4. **Graduate orientation & getting-started** — the bookend at the *other* end of candidature, tagged here because it's graduate-cohort content. *Arts* "Graduate Research Orientation" (appears 3× across path variants), "Graduate Research", "Graduate coursework students"; *FEIT* "Graduate Orientation" (live + a redirect duplicate), "Building access and ID cards — Graduate Researchers", "Graduate research resources".

5. **Research-student progress & supervision** — discipline-specific candidature management. *FFAM* "Progress reviews for research students", "Graduate research seminar (Melbourne Conservatorium of Music)", "Information for research students"; *Arts* "Enriching your graduate research", "Research support", "Facilities and resources".

6. **Placement conclusion (professional degrees)** — for accredited MDHS programs, "completion" means closing out clinical placement, not a ceremony. *MDHS* "Conclusion of placement" (recurs across Social Work, Clinical Neuropsychology, MSPGH), "During placement", "Student Placements", "Chancellor's Scholars".

7. **Enrichment, mentoring & cohort programs** — graduate/UG experience content that swept into the tag. *Arts* "Arts Career Mentoring", "Melbourne Peer Mentor Program", "Peer Assisted Study Sessions", "Arts Student Ambassadors", "Job Ready Program"; *MSD* "ABP Industry Mentoring" (1,858w), "MSD Peer Mentoring", "Student Ambassador & Leadership Program".

8. **Mis-tagged course-planning / structural pages** — overlap with the course-planning topic: *MSD* double-masters "Sample Course Plans" and per-degree plans appear here too; *Arts* "Overview of course structure", "Diploma in Languages". These are tagging bleed, not graduation content.

A structural observation across all eight types: the topic is heavy with **link-farms, redirects and path-variant duplicates** (Arts especially — "Graduate Research Orientation" three times, `_nocache` and `plan-your-program2` mirrors, an `eStudent login` 404). The signal-to-noise is low and the genuinely-graduation content (types 1–3) is a minority of the 125.

## Legitimate vs hub-overlapping

| Faculty-owned (cannot be centralised) | Overlaps the hub (consolidation candidate) |
|---|---|
| Research-candidature milestones, thesis submission, conversion (Arts) | Generic graduate orientation / "getting started" (Arts, FEIT) |
| Dean's Honours Awards lists by year (MSD, FBE) | Re-hosted enrolment / class-registration mechanics (FEIT, Arts) |
| Graduate-research prizes, write-up & travel awards (FEIT, FFAM) | Path-variant & `_nocache` duplicates, redirects, link-farms |
| Placement-conclusion for accredited degrees (MDHS) | The actual *graduation ceremony / apply-to-graduate* spine (hub-owned; barely present here) |
| Discipline-specific progress reviews & supervision (FFAM) | Cross-tagged course-structure / sample-plan pages (MSD, Arts) |

The balance tips clearly to **faculty-owned** — candidature lifecycle, honours, and research prizes are intrinsically discipline-bound. But the topic's defining feature is an *absence*: the transactional graduation spine that students most need (eligibility, apply-to-graduate, ceremony logistics, parchment/AHEGS) is a hub responsibility and is almost entirely missing from this tag, while a fog of duplicates and enrichment pages inflate the count.

## Recommendation

- **Hub owns the graduation spine outright:** eligibility to graduate, apply-to-graduate in eStudent, ceremony dates/logistics, parchments and the AHEGS/testamur. This is pure transactional cross-cutting service — it belongs at `students.unimelb.edu.au` as the single source of truth, and the crawl shows faculties are *not* duplicating it (good) but also not linking to it consistently.
- **Faculties keep the discipline-bound completion content:** research-candidature milestones and thesis submission (Arts), Dean's Honours Awards and graduate-research prizes (MSD, FEIT, FBE), placement-conclusion for accredited degrees (MDHS), and progress reviews (FFAM).
- **Split the tag — it conflates two journeys.** "Graduation/completion of a coursework degree" (ceremony, parchment) and "research-candidature lifecycle" (milestones → thesis → examination) are different journeys with different owners. The single `graduation` tag hides both; retag to separate *coursework completion* from *HDR candidature*.
- **Add one hub gateway:** a "Graduating from your course" page that links out to (a) the central apply-to-graduate transaction and (b) each faculty's honours/awards and HDR-completion pages — so the end-of-degree journey is discoverable from the centre, which it currently is not.
- **Highest-value fix:** clean the Arts/FEIT noise. Roughly a third of the 125 are link-farms, redirects, or path-variant duplicates ("Graduate Research Orientation" ×3, `_nocache` mirrors, dead `eStudent login` links). Deduplicating and pruning these would shrink the topic to its real ~80 substantive pages and make the genuine completion content findable.

## Appendix — all graduation pages (125)

### Arts — 61
- **1517w** — [Milestone reviews](https://arts.unimelb.edu.au/students/graduate-research/manage-your-research-program/milestone-reviews)
- **1489w** — [Arts Student Advisory Council](https://arts.unimelb.edu.au/students/arts-student-advisory-council)
- **1369w** · _mixed_ — [Overview of course structure](https://arts.unimelb.edu.au/students/graduate-research/plan-your-program2/overview-of-course-structure)
- **1316w** — [Arts Career Mentoring](https://arts.unimelb.edu.au/students/career-mentoring)
- **1254w** — [Candidature variations](https://arts.unimelb.edu.au/students/graduate-research/manage-your-research-program/candidature-variation)
- **1212w** · _mixed_ — [Diploma in Languages](https://arts.unimelb.edu.au/students/undergraduate/enrich-your-bachelor-of-arts/diploma-in-languages)
- **1140w** · _mixed_ — [Faculty of Arts Internship Grants](https://scholarships.unimelb.edu.au/awards/faculty-of-arts-internship-grants)
- **991w** — [Arts Student Ambassadors](https://arts.unimelb.edu.au/students/graduate-coursework/enrichment/arts-student-ambassadors)
- **913w** · _mixed_ — [Course enrolment information](https://arts.unimelb.edu.au/students/graduate-research/plan-your-program2/course-enrolment-information)
- **893w** · _mixed_ — [Overseas experience](https://arts.unimelb.edu.au/students/overseas-experience)
- **893w** · _mixed_ — [Overseas experience](https://arts.unimelb.edu.au/students/graduate-coursework/enrich-your-program/overseas-experience)
- **871w** — [Job Ready Program](https://arts.unimelb.edu.au/students/experiential-learning/job-ready-program)
- **720w** — [Melbourne Peer Mentor Program](https://arts.unimelb.edu.au/students/undergraduate/enrich-your-bachelor-of-arts/melbourne-peer-mentor-program)
- **717w** — [Course conversion](https://arts.unimelb.edu.au/students/graduate-research/manage-your-research-program/conversion-and-transfer)
- **684w** · _mixed_ — [Current students | Faculty of Arts](https://arts.unimelb.edu.au/students)
- **676w** · _mixed_ — [Undergraduate students](https://arts.unimelb.edu.au/students/undergraduate)
- **667w** — [Invitation to host an intern](https://arts.unimelb.edu.au/students/experiential-learning/internship-personal-and-career-growth/invitation-to-host-an-intern)
- **629w** · _mixed_ — [SCC Graduate Internship Subjects](https://arts.unimelb.edu.au/students/experiential-learning/scc-graduate-internship-subjects)
- **605w** — [Faculty of Arts Graduate Coursework Conference Grants](https://scholarships.unimelb.edu.au/awards/faculty-of-arts-graduate-coursework-conference-grants)
- **580w** · _mixed_ — [Bachelor of Arts (Degree with Honours) - The University of Melbourne](https://study.unimelb.edu.au/find/courses/honours/bachelor-of-arts-degree-with-honours/?referrer=arts_redirect)
- **550w** · _mixed_ — [Graduate coursework students](https://arts.unimelb.edu.au/students/graduate-coursework)
- **456w** · _mixed_ — [Diploma in Languages](https://arts.unimelb.edu.au/students/graduate-coursework/enrichment/diploma-in-languages)
- **453w** — [Peer Assisted Study Sessions](https://arts.unimelb.edu.au/students/undergraduate/enrich-your-bachelor-of-arts/peer-assisted-study-sessions)
- **450w** — [Professor Tim Parkin](https://arts.unimelb.edu.au/students/undergraduate/enrich-your-bachelor-of-arts/academic-mentoring/professor-tim-parkin)
- **426w** — [Dr Delia Lin](https://arts.unimelb.edu.au/students/undergraduate/enrich-your-bachelor-of-arts/academic-mentoring/dr-delia-lin)
- **393w** — [Academic resources](https://arts.unimelb.edu.au/students/undergraduate/resources-and-support/academic-resources)
- **367w** — [Language placement tests](https://arts.unimelb.edu.au/students/undergraduate/resources-and-support/language-placement-tests)
- **359w** — [Research support](https://arts.unimelb.edu.au/students/graduate-research/faqs/research-support)
- **358w** — [Enrichment](https://arts.unimelb.edu.au/students/undergraduate/enrich-your-bachelor-of-arts)
- **353w** — [Graduate research](https://arts.unimelb.edu.au/students/graduate-research)
- **353w** — [Graduate Research Orientation](https://arts.unimelb.edu.au/students/graduate-research/commencement/orientation-and-induction)
- **353w** — [Graduate Research Orientation](https://arts.unimelb.edu.au/students/graduate-research/commencement/orientation-and-induction/_nocache)
- **353w** — [Graduate Research Orientation](https://arts.unimelb.edu.au/students/graduate-research/plan-your-program2/orientation-and-induction)
- **346w** — [Academic Mentoring](https://arts.unimelb.edu.au/students/undergraduate/enrich-your-bachelor-of-arts/academic-mentoring)
- **344w** — [Video edit suites](https://arts.unimelb.edu.au/students/graduate-coursework/resources-and-support/video-edit-suites)
- **344w** — [Video edit suites](https://arts.unimelb.edu.au/students/graduate-coursework/enrich-your-program/video-edit-suites)
- **338w** — [Thesis submission](https://arts.unimelb.edu.au/students/graduate-research/manage-your-research-program/thesis-requirements)
- **320w** — [Bachelor of Arts Orientation](https://arts.unimelb.edu.au/students/undergraduate/bachelor-of-arts-orientation)
- **316w** · _mixed_ — [Class timetable | Current students | The University of Melbourne](https://students.unimelb.edu.au/course-admin/class-timetable)
- **316w** — [Campus experience](https://arts.unimelb.edu.au/students/undergraduate/enrich-your-bachelor-of-arts/campus-experience)
- **311w** — [GSHSS Academic Culture and English Tutorials](https://arts.unimelb.edu.au/students/graduate-coursework/enrichment/gshss-academic-culture-and-english-tutorials)
- **234w** — [Enriching your graduate research](https://arts.unimelb.edu.au/students/graduate-research/manage-your-research-program/enrichment-activities)
- **224w** — [Enrichment](https://arts.unimelb.edu.au/students/graduate-coursework/enrichment)
- **197w** — [Facilities and resources](https://arts.unimelb.edu.au/students/graduate-research/faqs/resources)
- **157w** · _link-farm_ — [Commence your candidature](https://arts.unimelb.edu.au/students/graduate-research/commencement)
- **157w** · _link-farm_ — [Commence your candidature](https://arts.unimelb.edu.au/students/graduate-research/plan-your-program2)
- **156w** · _link-farm_ — [Melbourne Mobility Awards](https://arts.unimelb.edu.au/students/overseas-experience/funding/melbourne-mobility-awards)
- **156w** · _link-farm_ — [Melbourne Mobility Awards](https://arts.unimelb.edu.au/students/graduate-coursework/enrich-your-program/overseas-experience/funding/melbourne-mobility-awards)
- **155w** · _redirect_ — [Page not found](https://arts.unimelb.edu.au/students/graduate-research/manage-your-research-program/eStudent%20login)
- **141w** · _link-farm_ — [Resources and support](https://arts.unimelb.edu.au/students/graduate-coursework/resources-and-support)
- **120w** · _link-farm_ — [Arts Global Languages Scholarship](https://arts.unimelb.edu.au/students/overseas-experience/funding/melbourne-global-language-scholarship)
- **120w** · _link-farm_ — [Arts Global Languages Scholarship](https://arts.unimelb.edu.au/students/graduate-coursework/enrich-your-program/overseas-experience/funding/melbourne-global-language-scholarship)
- **105w** · _redirect_ — [404 : Page not found | Error](https://arts.unimelb.edu.au/students/undergraduate/enrich-your-bachelor-of-arts/academic-mentoring/dr-lara-anderson)
- **102w** · _link-farm_ — [Support for your research](https://arts.unimelb.edu.au/students/graduate-research/faqs)
- **100w** · _link-farm_ — [ArtsModules](https://arts.unimelb.edu.au/students/graduate-research/manage-your-research-program/enrichment-activities/artsmodules)
- **92w** · _link-farm_ — [Manage your candidature](https://arts.unimelb.edu.au/students/graduate-research/manage-your-research-program)
- **80w** · _redirect_ — [404 : Page not found | Error](https://arts.unimelb.edu.au/students/experiential-learning-archive)
- **68w** · _link-farm_ — [Graduate researcher profiles](https://arts.unimelb.edu.au/students/graduate-research/meet-our-graduate-researchers)
- **54w** · _link-farm_ — [Resources and support](https://arts.unimelb.edu.au/students/undergraduate/resources-and-support)
- **38w** · _link-farm_ — [Research support funding](https://arts.unimelb.edu.au/students/graduate-research/faqs/gr-research-support-funding)
- **0w** · _mixed_ — [(untitled)](https://arts.unimelb.edu.au/students/graduate-coursework/manage-your-course)

### FEIT — 21
- **3201w** — [Meet our graduate researchers](https://eng.unimelb.edu.au/students/research/life-at-feit/student-profile)
- **1739w** — [Engineering and IT Conference Travel Grant](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students/scholarships/scholarships/travel)
- **800w** — [Graduate Coursework and Research Students](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/feit-students-study-abroad-and-exchange/graduate-coursework-and-research-students)
- **750w** — [Summer Round, 2026](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students/scholarships/summer-round)
- **728w** — [Scholarships for Graduate Researchers](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students/scholarships)
- **692w** — [Building access and ID cards - Graduate Researchers - Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/research/getting-started/building-access)
- **654w** — [Undergraduate Students](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/undergraduate)
- **569w** — [Engineering and IT undergraduate scholarships, The University of Melbourne](https://eng.unimelb.edu.au/students/eng-and-it-community/scholarships)
- **523w** · _mixed_ — [Graduate Coursework Students (International)](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/class-registration/mytimetable)
- **522w** — [Other Scholarships](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students/scholarships/other-scholarships,-2023)
- **494w** · _redirect_ — [Graduate Orientation](https://eng.unimelb.edu.au/students/coursework/orientation)
- **494w** — [Graduate Orientation](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation)
- **494w** — [PhD Write Up Award: Engineering and IT students, The University of Melbourne](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students/scholarships/scholarships/phd-write-up-award)
- **474w** · _mixed_ — [Graduate Coursework Students (Domestic)](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/class-registration/enrolling-in-subjects)
- **471w** — [Graduate research resources](https://eng.unimelb.edu.au/students/research/study-resources)
- **460w** — [Winter Round, 2026](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students/scholarships/winter-round)
- **433w** — [Undergraduate Prizes](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/undergraduate/subject-prizes-1)
- **428w** — [Graduate Research Prizes](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students/graduate-research-awards)
- **391w** — [Get in touch - Graduate Researchers – Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/research/get-in-touch)
- **373w** — [Graduate Researchers](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students)
- **365w** — [Graduate Researchers - Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/research)

### ABP/MSD — 20
- **1924w** — [Dean's Honours Awards 2024](https://msd.unimelb.edu.au/current-students/student-experience/deans-honours-awards/2024)
- **1877w** — [Dean's Honours Awards 2023](https://msd.unimelb.edu.au/current-students/student-experience/deans-honours-awards/2023)
- **1858w** — [ABP Industry Mentoring](https://msd.unimelb.edu.au/current-students/student-experience/abp-industry-mentoring)
- **960w** — [Master of Construction/Master of Property](https://msd.unimelb.edu.au/current-students/course-planning/sample-course-plans/double-masters/construction-property)
- **954w** — [Master of Architecture/Master of Construction](https://msd.unimelb.edu.au/current-students/course-planning/sample-course-plans/double-masters/architecture-construction)
- **946w** — [Bower Studio (Studio 30)](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-30)
- **916w** — [Double Masters Degrees](https://msd.unimelb.edu.au/current-students/course-planning/sample-course-plans/double-masters)
- **786w** — [Master of Architecture/Master of Landscape Architecture](https://msd.unimelb.edu.au/current-students/course-planning/sample-course-plans/double-masters/architecture-landscape-architecture)
- **723w** — [Master of Property/Master of Urban Planning](https://msd.unimelb.edu.au/current-students/course-planning/sample-course-plans/double-masters/property-urban-planning)
- **697w** — [ABPL90434 Construction Management Internship](https://msd.unimelb.edu.au/current-students/subject-information/internships-vocational-placements/abpl90434-construction-management-internship)
- **670w** — [Semester 2 2017 Studio 7](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-7)
- **657w** — [Student Ambassador & Leadership Program](https://msd.unimelb.edu.au/current-students/student-experience/graduate-ambassador-program)
- **651w** — [Semester 1 2017 Studio 7](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-7)
- **647w** — [Master of Architecture/Master of Property](https://msd.unimelb.edu.au/current-students/course-planning/sample-course-plans/double-masters/architecture-property)
- **582w** — [Master of Architectural Engineering](https://msd.unimelb.edu.au/current-students/course-planning/sample-course-plans/master-of-architectural-engineering)
- **549w** — [MSD Peer Mentoring Program](https://msd.unimelb.edu.au/current-students/student-experience/peer-mentoring-program)
- **528w** — [Dean's Honours Awards & Prizes](https://msd.unimelb.edu.au/current-students/student-experience/deans-honours-awards)
- **461w** — [Student Forum | Current Students | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/student-experience/student-forum)
- **365w** — [Graduate Diploma in Property Valuation Sample Course Plans](https://msd.unimelb.edu.au/current-students/course-planning/sample-course-plans/property-valuation)
- **343w** — [Sample Course Plans](https://msd.unimelb.edu.au/current-students/course-planning/sample-course-plans)

### MDHS — 11
- **668w** — [During placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/department-of-nursing/during-placement)
- **523w** — [Conclusion of placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/msps/clinical-neuropsychology/conclusion-of-placement)
- **482w** — [Chat Fest](https://mdhs.unimelb.edu.au/study/current-students/student-enrichment/chat-fest)
- **409w** — [Department of Physiotherapy](https://mdhs.unimelb.edu.au/study/current-students/placements/org/department-of-physiotherapy-resources)
- **358w** — [Student Placements](https://mdhs.unimelb.edu.au/study/current-students/placements)
- **349w** — [Department of Nursing](https://mdhs.unimelb.edu.au/study/current-students/placements/org/department-of-nursing)
- **337w** — [Department of Speech Pathology](https://mdhs.unimelb.edu.au/study/current-students/placements/org/dsp)
- **310w** — [Chancellor’s Scholars](https://mdhs.unimelb.edu.au/study/current-students/student-enrichment/mentoring-programs/chancellors-scholars)
- **297w** — [During placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/department-of-social-work-resources/during-placement)
- **253w** — [Research Pathways Advising](https://mdhs.unimelb.edu.au/study/current-students/student-enrichment/research-pathways-advising)
- **244w** — [Conclusion of Placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/mspgh/conclusion-of-placement)

### FFAM — 8
- **1002w** — [Grants and internal funding at the Faculty](https://finearts-music.unimelb.edu.au/current-students/research-students/grants)
- **792w** — [Conservatorium accompanists](https://finearts-music.unimelb.edu.au/current-students/assessment-and-exams/conservatorium-accompanists)
- **726w** — [Student Services | Graduate Students | FFAM](https://finearts-music.unimelb.edu.au/current-students/research-students/university-student-services)
- **393w** — [Scholarships & Studentships | Graduate Students | FFAM](https://finearts-music.unimelb.edu.au/current-students/research-students/scholarships-and-studentships)
- **391w** — [Progress reviews for research students](https://finearts-music.unimelb.edu.au/current-students/research-students/progress-reviews)
- **290w** — [Information for research students at the Faculty of Fine Arts & Music](https://finearts-music.unimelb.edu.au/current-students/research-students)
- **131w** · _link-farm_ — [Enrolment for research students](https://finearts-music.unimelb.edu.au/current-students/research-students/enrolment)
- **119w** · _link-farm_ — [Graduate research seminar (Melbourne Conservatorium of Music)](https://finearts-music.unimelb.edu.au/current-students/research-students/graduate-research-seminar-melbourne-conservatorium-of-music)

### FBE — 2
- **873w** — [Graduate researcher prizes and awards](https://fbe.unimelb.edu.au/students/phd/scholarships-and-grants/prizes-and-awards)
- **627w** — [Dean's Honours List 2024](https://fbe.unimelb.edu.au/students/bcom/current-students/deans-honours-list-2020)

### Education — 1
- **1214w** — [Early Childhood](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/early-childhood)

### Biomedical (school) — 1
- **546w** — [Biomedicine Graduate Pathways](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/biomedicine-graduate-pathways)
