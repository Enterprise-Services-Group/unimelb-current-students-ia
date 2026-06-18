# Topic Deep-Dive: IT & Systems

*Cross-faculty analysis from the full crawl. June 2026.*

**235 IT-systems–tagged pages** sit across the faculty estate, but the count is badly misleading: **183 of them (78%) are FEIT**, and most of those are not about IT at all — they are internships, scholarships, clubs, orientation and study-overseas pages swept in because they live under an "Engineering and Information Technology" faculty whose every URL says `eng.unimelb.edu.au`. Strip the noise and the *genuine* IT-and-systems signal is small, faculty-owned where it concerns physical facilities (computing labs, equipment loans, A/V suites), and almost entirely hub-overlapping where it concerns the transactional spine (Student IT helpdesk, software, the LMS, MyTimetable, the student portal/SSO).

## Distribution — who holds it

| Unit | Pages | What dominates |
|---|--:|---|
| Engineering & IT (FEIT) | 183 | Mostly mis-tagged (internships, scholarships, clubs, orientation); thin genuine core (Student IT, software, ID cards) |
| Arts | 11 | A/V loan equipment + video edit suites + hub course-admin pages cross-tagged in |
| Architecture, Building & Planning (MSD) | 10 | One deep "IT Support" page + studio archives + club/forms pages |
| Business & Economics (FBE) | 8 | Computing spaces / facilities rules / virtual lab — each duplicated (BCom + faculty) |
| Education | 5 | "Student Services and IT" (password/helpdesk) + placement-bound pages |
| Biomedical Sciences (school · MDHS) | 5 | Course redirects + the student-portal SSO redirect |
| Law | 4 | Canvas/LMS community + landing pages |
| Medicine, Dentistry & Health Sciences | 4 | Placement IP / clinical pages (tenuously tagged) |
| Fine Arts & Music | 3 | Tech Support & Facilities (3,501w) + instrument loans |
| Melbourne Business School (school · FBE) | 2 | Open-access computing spaces + virtual lab |
| **Total** | **235** | |

FEIT alone accounts for **78%** of the tag — the single most lopsided distribution in the audit — but that is a faculty-namespace artefact, not a real concentration of IT content. The honest topic is roughly 30–40 genuinely IT-flavoured pages spread thinly across the other nine units.

## Types of IT & Systems content

1. **Student computing spaces, labs & facilities rules** — physical/virtual lab provision and the rules governing it. *FBE* "Student Computing Spaces", "FBE computing facilities rules", "FBE virtual lab" (each existing twice — once under `/bcom/` and once under `/services/`); *MBS* "Open Access Student Computing Spaces", "Virtual Lab". Genuinely faculty-owned because the rooms and machines are.

2. **Faculty IT support / helpdesk pages** — discipline-specific support fronts. The richest is *ABP/MSD* "IT Support" (3,247w) — "Computer and software information for BDes and MSD students", including faculty-specific notes such as Adobe Creative Cloud licensing changes; *Education* "Student Services and IT" ("Forgot your password? … Student IT and eLearning Support … using university applications, accessing your email"). The MSD page is legitimately local; the Education page is mostly a restatement of the hub's Student IT service.

3. **Software access & device requirements** — what to install, what hardware to bring. *FEIT* "General Software for UoM Students", "Technology requirements and available resources", "Calculator Policy". Software entitlements are a University-wide service; the calculator policy is the only genuinely faculty-specific item.

4. **Student IT contact & live-chat channels** — how to reach support. *FEIT* "Student IT", "Student IT Contact", "Chat with Student IT". These point at the same central Student IT service the hub already owns; re-fronting it per faculty is pure overlap.

5. **The LMS / Canvas & learning platforms** — course-delivery systems. *Law* "Legal Academic Skills LMS Community" ("automatically enrolled … it will appear on your Canvas dashboard … Log in to the LMS"). The LMS itself is central; the *community content* inside it is faculty-owned.

6. **Equipment, instrument & A/V loans** — bookable kit tied to studio/performance disciplines. *FFAM* "Tech Support and Facilities" (3,501w — the largest IT-tagged page in the estate, covering equipment loans, technical staff, digital printing), "Instrument Loans"; *Arts* "Audio/Visual loan equipment", "Video edit suites" (×2), "Book a room and hire equipment". Strongly faculty-owned — the kit is physical and program-specific.

7. **Core student systems: portal, SSO, timetable, census** — the transactional spine, cross-tagged in. *Biomedical* "Student portal" (a 302 redirect to SSO/SAML sign-in); *Arts*-surfaced hub pages "Class timetable" ("MyTimetable is the system you use to create and view your class schedule"), "Check your subject census dates", "Cross-institutional study". These are unambiguously hub assets that happen to carry the IT tag.

8. **Building access & ID cards** — the physical-access system. *FEIT* "Building access and ID cards" (two variants, coursework vs graduate-researcher). Card/access systems are University-wide infrastructure with thin faculty-specific instructions.

9. **Tagging noise (not genuinely IT)** — the dominant "type" by raw count. The FEIT bucket is overwhelmingly internships ("Self-sourced internships" 4,864w, "University-sourced internships", the internship FAQ), scholarships and Dean's Honours pages, student clubs, orientation, and study-overseas/international-research programs. They are IT-tagged only because they sit on the `eng.unimelb.edu.au` (Engineering *and IT*) domain — a classifier false-positive, not real IT content.

## Legitimate vs hub-overlapping

| Faculty-owned (cannot be centralised) | Overlaps the hub (consolidation candidate) |
|---|---|
| Computing labs / facilities rules (FBE, MBS) | Faculty "Student IT" / helpdesk / live-chat re-fronts (FEIT, Education) |
| Faculty IT-support specifics — software licensing, studio kit (MSD, FFAM) | General software entitlements for all UoM students (FEIT) |
| Equipment / instrument / A/V loans (FFAM, Arts) | Student portal / SSO, MyTimetable, census dates (cross-tagged hub pages) |
| LMS *community content* — e.g. Legal Academic Skills (Law) | Building access & ID-card system instructions |
| Calculator policy, discipline device rules (FEIT) | Generic "accessing email / resetting password" restatements |

The balance is unusual for this audit: the *legitimate* faculty-owned core is small but real (physical labs, loanable kit, a couple of genuinely local IT-support pages), while the bulk of the tag is either hub-overlapping restatements of the central Student IT spine **or** outright mis-classification. Very little net unique content sits here once the FEIT namespace artefact is removed.

## Recommendation

- **Hub owns the IT spine outright:** Student IT helpdesk + live chat, software/device entitlements, password/account/email, the LMS (Canvas), MyTimetable, student portal/SSO, and building access/ID cards. These are single-source-of-truth services; faculties should link, never restate.
- **Faculties keep only what is physically theirs:** computing labs and their rules, studio/A-V/instrument loan systems, and genuinely local IT-support notes (e.g. MSD's Adobe licensing, FFAM tech support). These cannot be centralised.
- **Stop re-fronting Student IT:** retire the FEIT "Student IT / Student IT Contact / Chat with Student IT" trio and Education's helpdesk restatement in favour of one deep-link to the hub Student IT page.
- **De-duplicate within FBE:** the computing-spaces / rules / virtual-lab set exists twice (`/bcom/` and `/services/`); collapse to one canonical copy each.
- **Highest-value fix — fix the tag, not the content:** the FEIT `eng.unimelb.edu.au` namespace is poisoning this topic (183 of 235 pages, ~78%, mostly non-IT). Re-classify the internship/scholarship/club/orientation pages to their true topics so the IT-systems inventory reflects the ~30–40 genuinely IT pages — without that, every metric on this topic is distorted.

## Appendix — all IT-systems pages (235)

### FEIT — 183
- **4864w** · _mixed_ — [Self-sourced internships](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/self-sourced)
- **4609w** · _mixed_ — [International internships](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/self-sourced-international)
- **4456w** · _mixed_ — [University-sourced internships](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/university-sourced-internships)
- **3201w** — [Meet our graduate researchers](https://eng.unimelb.edu.au/students/research/life-at-feit/student-profile)
- **3148w** — [Frequently Asked Questions](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/faq)
- **2516w** · _redirect_ — [Intercultural Career Mentoring Program](https://eng.unimelb.edu.au/students/coursework/student-experience/international-opportunities/ICMP)
- **2516w** — [Intercultural Career Mentoring Program](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/ICMP)
- **2512w** · _mixed_ — [How to plan your course?](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/further-support/how-to-plan-your-course)
- **2177w** — [FEIT Hackathon Festival](https://eng.unimelb.edu.au/students/coursework/student-experience/industry-series/feit-hackathon-festival)
- **2125w** — [Technical Skills Series](https://eng.unimelb.edu.au/students/coursework/student-experience/technical-skills)
- **2057w** — [My Course Planner](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/further-support/my-course-planner)
- **1990w** — [Global Challenges in Engineering – Jakarta](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/global-challenges-in-engineering-jakarta)
- **1859w** — [Reviewing your progress](https://eng.unimelb.edu.au/students/research/study-resources/progress-review)
- **1614w** — [Peer Connect Program](https://eng.unimelb.edu.au/students/coursework/student-experience/mentoring-volunteering/peer-connect-program)
- **1600w** · _mixed_ — [Scholarship FAQ](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/scholarship-faq)
- **1549w** — [Korea Advanced Institute of Science and Technology (KAIST), Daejeon, South Korea](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/feit-students-study-abroad-and-exchange/international-research/kaist-visiting-student-researcher-program)
- **1461w** — [Pohang University of Science and Technology (POSTECH)](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/feit-students-study-abroad-and-exchange/international-research/kaist-visiting-student-researcher-program2)
- **1347w** — [Extensions and Special consideration](https://eng.unimelb.edu.au/students/coursework/study-resources/extensions-and-special-consideration)
- **1285w** — [Commerce/Engineering pathway](https://eng.unimelb.edu.au/students/eng-and-it-community/commerce-pathway)
- **1281w** · _mixed_ — [Employability in Engineering and Information Technology](https://eng.unimelb.edu.au/students/employability-in-engineering-and-information-technology)
- **1278w** — [Our Clubs](https://eng.unimelb.edu.au/students/clubs/our-clubs)
- **1270w** · _mixed_ — [Faculty Course Planning Resources](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/further-support/faculty-course-planning-resources)
- **1255w** — [Engineering and IT Community](https://eng.unimelb.edu.au/students/eng-and-it-community)
- **1236w** — [Health and Wellbeing Resources](https://eng.unimelb.edu.au/students/coursework/study-resources/wellbeing)
- **1187w** — [Catholic University of Louvain Summer Research Program (Summer: Nov - Feb)](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/feit-students-study-abroad-and-exchange/international-research/catholic-university-of-louvain-summer-research-program-summer-nov-feb)
- **1151w** — [Kyoto University Short-Term Academic Research (KU-STAR) Summer Research Program (Summer: Nov - Feb)](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/feit-students-study-abroad-and-exchange/international-research/ku-star)
- **1151w** — [University of Twente Summer Research Program (Summer: Nov - Feb)](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/feit-students-study-abroad-and-exchange/international-research/university-of-twente-summer-research-program-summer-nov-feb)
- **1116w** · _mixed_ — [Arrival and commencement checklist](https://eng.unimelb.edu.au/students/research/getting-started/arrival-checklist)
- **1092w** — [Academic Communication Skills Series](https://eng.unimelb.edu.au/students/coursework/student-experience/academic-communication-skills-series)
- **1063w** — [Engineering & IT Orientation Program](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/program)
- **1049w** — [Upcoming Opportunities](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/feit-students-study-abroad-and-exchange/international-coursework-opportunities/upcoming-short-term-coursework-opportunities)
- **1038w** — [Nominate for the Community Awards](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/spotlight-celebrations/community-awards/nominate)
- **1000w** — [Building access and ID cards – Coursework Students – Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/coursework/study-resources/building-access-and-id-cards)
- **946w** — [Submitting your thesis and beyond](https://eng.unimelb.edu.au/students/research/study-resources/submitting-your-thesis)
- **933w** — [Engineering & IT Coursework Scholarship Terms and Conditions](https://eng.unimelb.edu.au/students/coursework/progress-your-career/sap/scholarships/terms/engineering-and-it-coursework-scholarship-terms-and-conditions)
- **929w** — [Engineering & IT Coursework Scholarship Terms and Conditions](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships/terms/engineering-and-it-coursework-scholarship-terms-and-conditions)
- **887w** — [Welcome to Melbourne: International Student Webinars](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/finalising-enrolment/enrolment-and-assistance)
- **880w** — [2023 Dean’s Honours List](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/deans-honours-award/2023)
- **849w** — [2022 Dean’s Honours List](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/deans-honours-award/school-of-computing-and-information-systems-1)
- **823w** — [Course requirements](https://eng.unimelb.edu.au/students/research/study-resources/course-requirements)
- **820w** — [2024 Dean's Honours List](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/deans-honours-award/2024)
- **809w** — [Scholarships, Prizes and Awards Recipients](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/scholarships,-prizes-and-awards-recipients)
- **797w** — [Stephen Ho Accelerator Grant](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships/scholarships/stephen-ho-accelerator-grant)
- **789w** — [International Research Opportunities](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/feit-students-study-abroad-and-exchange/international-research)
- **788w** — [Current students](https://eng.unimelb.edu.au/students)
- **787w** — [Scholarships - Coursework Students - Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/whats-next/coursework-students/scholarships)
- **783w** — [Scholarships - Coursework Students - Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships)
- **774w** — [Coursework students | Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/coursework)
- **756w** · _mixed_ — [New Student Checklist (International Students)](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/plan-to-attend-melbourne-orientation/new-student-checklist-international-students)
- **734w** — [FAQs](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/deans-honours-award/faqs)
- **728w** · _redirect_ — [Internships - Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/coursework/progress-your-career/internship/internship-subjects)
- **728w** — [Internships - Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/internship-subjects)
- **726w** — [Student Ambassador Leadership Program](https://eng.unimelb.edu.au/students/coursework/student-experience/mentoring-volunteering/salp)
- **715w** — [Student IT](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/technology-requirements-and-available-resources/student-it)
- **707w** — [Engineering & IT Commencing Scholarship Terms and Conditions](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships/terms/engineering-and-it-commencing-scholarship-terms-and-conditions)
- **698w** — [Student Experience](https://eng.unimelb.edu.au/students/coursework/student-experience)
- **697w** — [Not-for-Credit Internships](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/practice-hurdle/internship-no-credit)
- **694w** — [Not-for-Credit Internships](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/internship-no-credit)
- **692w** — [Building access and ID cards - Graduate Researchers - Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/research/getting-started/building-access)
- **670w** — [Indigenous Student Experience](https://eng.unimelb.edu.au/students/indigenous-student-experience)
- **670w** · _redirect_ — [Indigenous Student Experience](https://eng.unimelb.edu.au/students/feit-indigenous-student-experience2)
- **669w** — [Design/Engineering pathway](https://eng.unimelb.edu.au/students/eng-and-it-community/design-pathway)
- **669w** · _mixed_ — [New Student Checklist (Domestic Students)](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/plan-to-attend-melbourne-orientation/new-student-checklist-domestic-students)
- **667w** — [Academic English Tutorials](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/improve-your-english,-communication-and-academic-skills/academic-english-tutorials)
- **654w** — [Undergraduate Students](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/undergraduate)
- **648w** — [ENG & IT Express Newsletter](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/keep-in-touch/newsletter)
- **644w** — [ENG & IT Express Newsletter](https://eng.unimelb.edu.au/students/coursework/study-resources/newsletter)
- **636w** — [FEIT Student Exchange Funding and Scholarships](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/feit-students-study-abroad-and-exchange/saex-funding-and-scholarships)
- **631w** — [Coursework Prizes](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/whats-next/coursework-students/coursework-prizes)
- **627w** — [Coursework Prizes](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/coursework-prizes)
- **617w** — [Event Funding and Invoicing](https://eng.unimelb.edu.au/students/clubs/event-funding-and-invoicing)
- **601w** — [Science/Engineering pathway](https://eng.unimelb.edu.au/students/eng-and-it-community/science-pathway)
- **601w** · _redirect_ — [Internships - Coursework Students - Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/coursework/industry-engagement/internship)
- **601w** — [Internships - Coursework Students - Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/coursework/student-experience/internship)
- **601w** · _redirect_ — [Internships - Coursework Students - Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/coursework/progress-your-career/internship)
- **600w** — [Melbourne Talks](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/explore-university-platforms-and-systems/melbourne-talks)
- **594w** · _redirect_ — [Professional Skills Series](https://eng.unimelb.edu.au/students/coursework/student-experience/professional-skills)
- **594w** — [Professional Skills Series](https://eng.unimelb.edu.au/students/coursework/student-experience/professional-skills-series)
- **594w** · _redirect_ — [Professional Skills Series](https://eng.unimelb.edu.au/students/coursework/progress-your-career/mse-experience-series/professional-skills)
- **592w** — [Scholarships, Prizes and Awards - FEIT](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards)
- **587w** — [How Does It Work?](https://eng.unimelb.edu.au/students/coursework/student-experience/industry-series/diversity-and-inclusion-case-competition/how-does-it-work)
- **583w** · _mixed_ — [International Student Support](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/explore-university-platforms-and-systems/international-student-support)
- **581w** — [Biomedicine/Engineering pathway](https://eng.unimelb.edu.au/students/eng-and-it-community/biomedicine-pathway)
- **574w** — [Round 1 Scholarships](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/whats-next/coursework-students/scholarships/round-one)
- **570w** — [Round 1 Scholarships](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships/round-one)
- **567w** — [Services, support and activities](https://eng.unimelb.edu.au/students/research/study-resources/services-support-activities)
- **556w** — [Other Scholarships](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/whats-next/coursework-students/scholarships/other-scholarships)
- **553w** — [Intro to Uni](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/finalising-enrolment/accepting-offers)
- **552w** — [Other Scholarships](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships/other-scholarships)
- **546w** — [Diversity & Inclusion Case Competition](https://eng.unimelb.edu.au/students/coursework/student-experience/industry-series/diversity-and-inclusion-case-competition)
- **543w** — [Study abroad and exchange](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/feit-students-study-abroad-and-exchange)
- **542w** — [Professional Associations](https://eng.unimelb.edu.au/students/coursework/career-resources/professional-associations)
- **540w** — [Global Skills Series](https://eng.unimelb.edu.au/students/coursework/student-experience/global-skills-series)
- **540w** — [Information for committee members](https://eng.unimelb.edu.au/students/clubs/committee)
- **539w** — [Student Resources & Services](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/whats-next/student-resources-and-services)
- **539w** — [Stephen Ho Innovation Awards](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships/scholarships/stephen-ho-innovation-awards)
- **537w** — [Study Resources](https://eng.unimelb.edu.au/students/coursework/study-resources)
- **535w** — [Before Orientation](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation)
- **533w** — [Career resources](https://eng.unimelb.edu.au/students/coursework/career-resources)
- **522w** — [Acusensus Scholarship for Women in STEM](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships/scholarships/acusensus-scholarship-for-women-in-engineering)
- **519w** — [Industry Series](https://eng.unimelb.edu.au/students/coursework/student-experience/industry-series)
- **516w** — [Engineering Practice Hurdle](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/practice-hurdle)
- **510w** — [Promote an Upcoming Event](https://eng.unimelb.edu.au/students/clubs/feature-in-the-feit-express-newsletter)
- **507w** — [Academic Skills](https://eng.unimelb.edu.au/students/coursework/study-resources/academic-skills)
- **506w** — [FEIT award winners 2023](https://eng.unimelb.edu.au/students/research/life-at-feit/award-winners)
- **502w** — [Student IT Contact](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/technology-requirements-and-available-resources/student-it-contact)
- **498w** — [John Balfour Memorial Scholarship](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships/scholarships/john-balfour)
- **494w** · _redirect_ — [Graduate Orientation](https://eng.unimelb.edu.au/students/coursework/orientation)
- **494w** — [Graduate Orientation](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation)
- **493w** — [Melbourne University Geomatics Society (MUGS)](https://eng.unimelb.edu.au/students/clubs/our-clubs/melbourne-university-geomatics-society-mugs)
- **489w** — [Community Awards](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/spotlight-celebrations/community-awards)
- **481w** — [Round 4 Scholarships](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/keep-in-touch/eng-and-it-calendar/upcoming-events/round-4-scholarships)
- **478w** — [Internships - Graduate Researchers - Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/research/life-at-feit/internships)
- **475w** — [Eligibility and selection criteria](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/deans-honours-award/eligibility-and-selection-criteria)
- **473w** — [Student Clubs and Societies](https://eng.unimelb.edu.au/students/clubs)
- **473w** — [Round 4 Scholarships](https://eng.unimelb.edu.au/students/eng-and-it-calendar/upcoming-events/round-4-scholarships)
- **471w** — [Graduate research resources](https://eng.unimelb.edu.au/students/research/study-resources)
- **469w** — [Skills Towards Employment Program](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/practice-hurdle/step)
- **464w** — [Round 3 Scholarships](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/whats-next/coursework-students/scholarships/round-two)
- **460w** — [Round 3 Scholarships](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships/round-two)
- **459w** — [Coursework Students](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/whats-next/coursework-students)
- **458w** · _redirect_ — [Global Experience](https://eng.unimelb.edu.au/students/coursework/student-experience/international-opportunities)
- **458w** — [Global Experience](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas)
- **455w** — [Coursework Students](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students)
- **454w** · _redirect_ — [~ Page not found](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/preparing-for-and-securing-an-internship)
- **451w** — [General Software for UoM Students](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/technology-requirements-and-available-resources/general-software-for-uom-students)
- **445w** — [Student clubs and societies](https://eng.unimelb.edu.au/students/research/life-at-feit/student-clubs)
- **442w** — [Round 3 Scholarships](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/keep-in-touch/eng-and-it-calendar/upcoming-events/round-3-scholarships)
- **441w** · _redirect_ — [~ Page not found](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/Peter%20Hall%20Building)
- **441w** · _redirect_ — [~ Page not found](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/Melbourne%20Connect%20Building)
- **438w** — [Spotlight Celebrations](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/spotlight-celebrations)
- **434w** — [Round 3 Scholarships](https://eng.unimelb.edu.au/students/eng-and-it-calendar/upcoming-events/round-3-scholarships)
- **433w** · _redirect_ — [~ Page not found](https://eng.unimelb.edu.au/students/coursework/orientation/after-orientation/whats-next/sap/scholarships/scholarships/m.k.n.-johansen-scholarship-for-the-advancement-of-municipal-engineering)
- **424w** — [Industry Events](https://eng.unimelb.edu.au/students/coursework/student-experience/industry-series/all-industry-events)
- **421w** — [Wellbeing Series](https://eng.unimelb.edu.au/students/coursework/student-experience/wellbeing-series)
- **418w** — [Engineering and IT Scholarship Terms and Conditions](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships/terms)
- **412w** — [Melbourne University Civil and Structural Society](https://eng.unimelb.edu.au/students/clubs/our-clubs/melbourne-university-civil-and-structural-society)
- **403w** — [Round 2 Scholarships](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/whats-next/coursework-students/scholarships/round-1a-scholarships)
- **401w** — [Drone Aviation and Racing Engineering Society](https://eng.unimelb.edu.au/students/clubs/our-clubs/drone-aviation-and-racing-engineering-society)
- **399w** — [Round 2 Scholarships](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships/round-1a-scholarships)
- **397w** — [Mechanical Engineering Student Society](https://eng.unimelb.edu.au/students/clubs/our-clubs/mechanical-engineering-student-society-mess)
- **396w** — [Eligibility](https://eng.unimelb.edu.au/students/coursework/student-experience/industry-series/diversity-and-inclusion-case-competition/who-can-participate)
- **391w** — [Get in touch - Graduate Researchers – Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/research/get-in-touch)
- **382w** — [Deep Dive Sessions](https://eng.unimelb.edu.au/students/eng-and-it-community/deep-dive-sessions)
- **382w** — [Lens Stevens Scholarship](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/keep-in-touch/eng-and-it-calendar/upcoming-events/lens-stevens-scholarship)
- **375w** — [Community image gallery](https://eng.unimelb.edu.au/students/eng-and-it-community/community-image-gallery)
- **375w** · _redirect_ — [Mentoring & Volunteering](https://eng.unimelb.edu.au/students/coursework/student-experience/professional-skills-series/technical-skills-series)
- **375w** — [Mentoring & Volunteering](https://eng.unimelb.edu.au/students/coursework/student-experience/mentoring-volunteering)
- **374w** — [Lens Stevens Scholarship](https://eng.unimelb.edu.au/students/eng-and-it-calendar/upcoming-events/lens-stevens-scholarship)
- **373w** — [Chat with Student IT](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/technology-requirements-and-available-resources/chat-with-student-it)
- **368w** — [Life at FEIT](https://eng.unimelb.edu.au/students/research/life-at-feit)
- **368w** — [FEIT Student Event Calendar](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/keep-in-touch/eng-and-it-calendar)
- **365w** — [Graduate Researchers - Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/research)
- **365w** — [Calculator Policy](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/technology-requirements-and-available-resources/calculator-policy)
- **360w** — [FEIT Student Event Calendar](https://eng.unimelb.edu.au/students/eng-and-it-calendar)
- **353w** — [Dean’s Honours List](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/whats-next/coursework-students/deans-honours-award)
- **352w** — [Ian Alexander Scholarship Round 2](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/keep-in-touch/eng-and-it-calendar/upcoming-events/ian-alexander-scholarship-round-2)
- **352w** — [2023 winners](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/spotlight-celebrations/community-awards/winners/2023-winners)
- **349w** — [Dean’s Honours List](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/deans-honours-award)
- **349w** — [2022 winners](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/spotlight-celebrations/community-awards/winners/2022-winners)
- **348w** — [Getting started](https://eng.unimelb.edu.au/students/research/getting-started)
- **344w** — [Ian Alexander Scholarship Round 2](https://eng.unimelb.edu.au/students/eng-and-it-calendar/upcoming-events/ian-alexander-scholarship-round-2)
- **344w** — [2024 winners](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/spotlight-celebrations/community-awards/winners/2024-winners)
- **342w** — [Upcoming events](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/keep-in-touch/eng-and-it-calendar/upcoming-events)
- **335w** — [Domestic Internships](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/domestic-internship-opportunities)
- **334w** — [Upcoming events](https://eng.unimelb.edu.au/students/eng-and-it-calendar/upcoming-events)
- **332w** — [Orientation feedback survey](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/your-feedback/feedback)
- **328w** — [2025 winners](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/spotlight-celebrations/community-awards/winners/2025-winners)
- **323w** — [Previous Community Awards winners](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/spotlight-celebrations/community-awards/winners)
- **312w** — [After Orientation](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation)
- **312w** — [Honour roll](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/deans-honours-award/honour-roll)
- **312w** — [International Student Resources](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/explore-university-platforms-and-systems/international-student-resources)
- **308w** — [Book a room for your event](https://eng.unimelb.edu.au/students/clubs/book-a-room-for-your-event)
- **307w** — [Image galleries](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/spotlight-celebrations/image-galleries)
- **306w** — [Academic Skills](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/improve-your-english,-communication-and-academic-skills/academic-skills)
- **302w** — [2025 Spotlight Celebration Image Gallery](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/spotlight-celebrations/2025-spotlight-celebration-image-gallery)
- **296w** — [2025 Hackathon Festival Image Gallery](https://eng.unimelb.edu.au/students/coursework/student-experience/industry-series/feit-hackathon-festival/2025-hackathon-festival-image-gallery)
- **293w** — [2022 Spotlight Celebration Image Gallery](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/spotlight-celebrations/2022-spotlight-celebration-image-gallery)
- **293w** — [2023 Spotlight Celebration Image Gallery](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/spotlight-celebrations/2023-spotlight-celebration-image-gallery)
- **293w** — [2024 Spotlight Celebration Image Gallery](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/spotlight-celebrations/2024-spotlight-celebration-image-gallery)
- **291w** — [COVID-19 Student Support](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/further-support/covid-19-student-support)
- **291w** — [Manage your Course](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/further-support/manage-your-course)
- **287w** — [Frequently Asked Questions](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/frequently-asked-questions)

### Arts — 11
- **1770w** · _mixed_ — [Experiential Learning](https://arts.unimelb.edu.au/students/experiential-learning)
- **1418w** · _mixed_ — [Cross-institutional study](https://students.unimelb.edu.au/course-admin/cross-institutional-study)
- **1212w** · _mixed_ — [Diploma in Languages](https://arts.unimelb.edu.au/students/undergraduate/enrich-your-bachelor-of-arts/diploma-in-languages)
- **987w** · _mixed_ — [Check your subject census dates : The University of Melbourne](https://students.unimelb.edu.au/course-admin/census-dates)
- **393w** — [Academic resources](https://arts.unimelb.edu.au/students/undergraduate/resources-and-support/academic-resources)
- **386w** — [Book a room and hire equipment](https://arts.unimelb.edu.au/contact-us/book-a-room-or-equipment)
- **344w** — [Video edit suites](https://arts.unimelb.edu.au/students/graduate-coursework/resources-and-support/video-edit-suites)
- **344w** — [Video edit suites](https://arts.unimelb.edu.au/students/graduate-coursework/enrich-your-program/video-edit-suites)
- **316w** · _mixed_ — [Class timetable | Current students | The University of Melbourne](https://students.unimelb.edu.au/course-admin/class-timetable)
- **155w** · _redirect_ — [Page not found](https://arts.unimelb.edu.au/students/graduate-research/manage-your-research-program/eStudent%20login)
- **105w** · _redirect_ — [404 : Page not found | Error](https://arts.unimelb.edu.au/students/undergraduate/enrich-your-bachelor-of-arts/academic-mentoring/dr-lara-anderson)

### ABP/MSD — 10
- **3247w** — [IT Support | Current Students | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/student-experience/it-support)
- **1641w** — [Information for clubs](https://msd.unimelb.edu.au/current-students/student-experience/clubs-and-societies/information-for-clubs)
- **1071w** — [Semester 2 2017 Thesis 7](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/THE-2017_SM2-Studios/thesis-7)
- **984w** — [Semester 2 2017 Studio 15](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-15)
- **791w** — [Caretaker Studio](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/c_sm1_2026/caretaker-studio)
- **729w** — [Studio 12](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-12)
- **704w** — [Semester 2 2017 Studio 19](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-19)
- **678w** — [Summer 2018 Studio 19](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SUM-Studios/studio-19)
- **417w** — [List of Forms | Current Students | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/enrolment/list-of-forms)
- **0w** · _redirect_ — [Redirecting...](https://msd.unimelb.edu.au/current-students/student-experience/it-support/requestfeedback-form)

### FBE — 8
- **553w** — [Student Computing Spaces](https://fbe.unimelb.edu.au/students/bcom/current-students/services/computing-spaces)
- **550w** — [Student Computing Spaces](https://fbe.unimelb.edu.au/students/services/computing-spaces)
- **493w** — [FBE computing facilities rules](https://fbe.unimelb.edu.au/students/bcom/current-students/services/rules)
- **490w** — [FBE computing facilities rules](https://fbe.unimelb.edu.au/students/services/rules)
- **323w** — [FBE virtual lab](https://fbe.unimelb.edu.au/students/bcom/current-students/services/virtual-lab)
- **320w** — [FBE virtual lab](https://fbe.unimelb.edu.au/students/services/virtual-lab)
- **0w** · _redirect_ — [Sign In (SSO redirect)](https://fbe.unimelb.edu.au/students/bcom/first-semester-guide/week-1/connect-with-your-peer-mentor)
- **0w** · _redirect_ — [Sign In (SSO redirect)](https://fbe.unimelb.edu.au/students/bcom/first-semester-guide/week-2-3/fbe-engagement-planner)

### Education — 5
- **1457w** — [Career Mentoring](https://education.unimelb.edu.au/study/current-students/career-mentoring)
- **580w** — [Placement structure](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/placement-structure)
- **369w** — [FoE Extensions](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/foe-extensions)
- **219w** — [Working with Children Check](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/working-with-children-check)
- **67w** · _link-farm_ — [Placement forms](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-details/placement-forms)

### Biomedical (school) — 5
- **166w** · _redirect_ — [Biochemistry and Molecular Biology - The University of Melbourne](https://study.unimelb.edu.au/find/courses/major/biochemistry-and-molecular-biology/)
- **155w** · _redirect_ — [Neuroscience - The University of Melbourne](https://study.unimelb.edu.au/find/courses/major/neuroscience/)
- **137w** · _redirect_ — [Genetics - The University of Melbourne](https://study.unimelb.edu.au/find/courses/major/genetics/)
- **132w** · _redirect_ — [Biotechnology - The University of Melbourne](https://study.unimelb.edu.au/find/courses/major/biotechnology/)
- **0w** · _redirect_ — [Student portal (redirects to SSO/SAML login)](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/student-portal)

### Law — 4
- **937w** · _mixed_ — [JD Students](https://law.unimelb.edu.au/students/jd)
- **894w** · _mixed_ — [MLM Students](https://law.unimelb.edu.au/students/masters)
- **283w** — [Leave of Absence](https://law.unimelb.edu.au/students/masters/studies/leave-of-absence)
- **196w** — [Legal Academic Skills LMS Community](https://law.unimelb.edu.au/students/legal-academic-skills/lms-community)

### MDHS — 4
- **566w** — [Personal information & Intellectual Property](https://mdhs.unimelb.edu.au/study/current-students/placements/students/personal-information-and-intellectual-property)
- **369w** — [Melbourne Medical School](https://mdhs.unimelb.edu.au/study/current-students/placements/org/melbourne-medical-school)
- **356w** — [How to provide remote placements for clinical audiology students](https://mdhs.unimelb.edu.au/study/current-students/placements/org/clinicalaudiology/before/remote-placements-for-students)
- **282w** — [Hand Hygiene](https://mdhs.unimelb.edu.au/study/current-students/placements/students/requirements/course-specific-checks/hand-hygiene)

### FFAM — 3
- **3501w** — [Tech Support and Facilities](https://finearts-music.unimelb.edu.au/current-students/assets/links/tech-support-and-facilities)
- **305w** — [Instrument Loans | Faculty of Fine Arts & Music | UniMelb](https://finearts-music.unimelb.edu.au/current-students/facilities/conservatorium-instrument-loans)
- **275w** — [Information for current students at the Faculty of Fine Arts and Music](https://finearts-music.unimelb.edu.au/current-students)

### MBS (school) — 2
- **641w** — [Open Access Student Computing Spaces](https://mbs.unimelb.edu.au/students/course-planning/services/computing-spaces)
- **288w** — [Virtual Lab](https://mbs.unimelb.edu.au/students/course-planning/services/virtual-lab)
