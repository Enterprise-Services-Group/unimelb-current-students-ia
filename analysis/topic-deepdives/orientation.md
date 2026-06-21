# Topic Deep-Dive: Orientation
*Cross-faculty analysis from the full crawl. June 2026.*

**289 orientation-tagged pages** sit across the faculty estate — a deceptively large count that ranks orientation among the bigger topics, but the number is almost entirely a tagging artifact. **FEIT alone holds 204 of the 289 (71%)** because it nests nearly its whole current-students estate (scholarships, clubs, internships, study-overseas) under `/orientation/` URL paths — only 45 of those 204 URLs actually contain `/orientation/` as a content segment, and most of the rest are unrelated. The *genuine* orientation footprint is small, thin, and **legitimately faculty-owned**: per-degree "welcome / orientation week" landing pages and "accept your offer and get started" checklists. The duplication problem here is not cross-faculty overlap — it is one faculty's information architecture flooding the topic.

## Distribution — who holds it

| Unit | Pages | What dominates |
|---|--:|---|
| Engineering & IT (FEIT) | 204 | Whole estate nested under `/orientation/` paths — scholarships, clubs, internships, study-overseas |
| Biomedical Sciences (school · MDHS) | 24 | "Plan your Bachelor of Biomedicine" + per-program orientation landings |
| Arts | 20 | Graduate-research commencement/induction + BA orientation event |
| Medicine, Dentistry & Health Sciences | 14 | Placement "before placement / day one" induction (not real orientation) |
| Law | 12 | JD/MLM orientation + "accept your offer and get started" + GRD profiles |
| Architecture, Building & Planning (MSD) | 6 | Peer mentoring + studio/course-plan pages (mis-tagged) |
| Science | 3 | Per-degree orientation (BSc, BAgr, graduate getting-started) |
| Fine Arts & Music | 3 | One orientation landing + student-guide link-farm |
| Business & Economics (FBE) | 2 | One BCom orientation page |
| Melbourne Business School (school · FBE) | 1 | One orientation landing |
| **Total** | **289** | |

**FEIT is not "the orientation faculty" — it is a measurement distortion.** Its `/student-experience/orientation/` tree is a deep navigational spine that parents content far beyond orientation (internships at 4,800+ words, scholarship rounds, Dean's Honours lists), so the crawler tagged the whole subtree. Strip FEIT's noise and the real estate is ~85 pages, of which only a handful per faculty are true orientation pages.

## Types of Orientation content

1. **Per-degree orientation / welcome landings** — the genuine core: a dated welcome event for a named cohort. *Law* "Orientation" ("JD Orientation 4–5 February 2026, Melbourne Law School"); *Science* "Bachelor of Science Orientation", "Bachelor of Agriculture Orientation"; *Arts* "Bachelor of Arts Orientation" ("Welcome to the BA! … Monday 20 July 2026, Forum Theatre"); *Biomedical* "Biomedicine Orientation" ("2026 Orientation Events … 23–27 February"); *FBE* / *MBS* / *FFAM* each a single "Orientation" page.
2. **"Accept your offer and get started" / new-student checklists** — the pre-arrival transactional step, faculty-flavoured. *Law* "Accept Your Offer & Get Started | JD" (1,823w) and the Masters equivalent; *FEIT* "New Student Checklist (International Students)", "New Student Checklist (Domestic Students)", "Intro to Uni" (accepting offers).
3. **Graduate-research commencement & induction** — a distinct orientation track for HDR candidates. *Arts* "Graduate Research Orientation", "Commence your candidature", "Commencement form checklist", "Course enrolment information"; *FEIT* "Arrival and commencement checklist" (research).
4. **Orientation-program structure (before / during / after)** — multi-page programs, almost exclusively FEIT. *FEIT* "Engineering & IT Orientation Program", "Before Orientation", "After Orientation", "Graduate Orientation", "Orientation feedback survey", plus "Welcome to Melbourne: International Student Webinars" and "Melbourne Talks".
5. **Pre-arrival IT, software & systems setup** — onboarding into University platforms, all under FEIT's orientation tree. *FEIT* "Student IT", "Chat with Student IT", "General Software for UoM Students", "Calculator Policy", "International Student Resources", "Explore University Platforms and Systems".
6. **Placement induction mis-tagged as orientation** — MDHS's "before placement / day one of placement" pages are clinical-placement onboarding, not course orientation. *MDHS* "Before placement" (×8 across audiology, nursing, social work, psychology, dental), "Day one of placement", "Insurance".
7. **Peer mentoring & first-cohort community** — the social side of starting out. *FEIT* "Peer Connect Program", "Student Ambassador Leadership Program"; *MSD* "MSD Peer Mentoring Program"; *Biomedical* "Student Societies".
8. **FEIT estate swept in by URL path (noise)** — not orientation at all, but tagged because of `/orientation/` parentage: scholarship rounds and terms, Dean's Honours lists, clubs/societies, self-sourced & international internships, study-overseas research programs, skills series. This is the bulk of the 204 and the single biggest data-quality issue in the topic.

## Legitimate vs central-overlapping

| Faculty-owned (cannot be centralised) | Overlaps students.unimelb.edu.au (consolidation candidate) |
|---|---|
| Per-degree orientation event landings (dates, venues, cohort) — Law, Science, Arts, Biomedical, FBE | Generic "what is Orientation week" / University-wide welcome framing |
| Faculty "accept your offer and get started" checklists | Pre-arrival IT/software/systems setup (FEIT) — University-wide, owned by students.unimelb.edu.au |
| Graduate-research commencement & induction (Arts, FEIT) | "Welcome to Melbourne" international webinars / Melbourne Talks |
| Discipline peer-mentoring & society intros | "New student checklist" generic steps students.unimelb.edu.au already owns |
| Placement induction (MDHS) — belongs to placements, not orientation | |

The balance is the inverse of most topics: the *genuinely* orientation-specific content (the dated welcome event per degree) is small and rightly faculty-owned, while a large share of what is *tagged* orientation — IT setup, welcome webinars, generic checklists — is University-wide and should sit on students.unimelb.edu.au. The MDHS placement pages and FEIT's swept-in estate are simply mis-tagged.

## Recommendation
- **students.unimelb.edu.au owns the welcome spine:** a single canonical "Orientation" students.unimelb.edu.au page — University-wide Orientation week dates, the pre-arrival checklist, IT/software/systems setup, and "Welcome to Melbourne" international onboarding — so faculties stop each restating it (FEIT's whole `before-orientation` IT tree is students.unimelb.edu.au material).
- **Faculties keep the dated event:** each faculty owns one "[Degree] Orientation" page with its cohort's date/venue/schedule and a peer-mentoring link — this is the only part that cannot be centralised, and it is exactly what students need from a faculty.
- **Add one students.unimelb.edu.au gateway:** `students.unimelb.edu.au/new-students/orientation` linking to every faculty's orientation-event page, so a commencing student finds their faculty's welcome from the centre (currently each faculty publishes in isolation).
- **Fix the tagging — the highest-value action:** FEIT's `/student-experience/orientation/` URL tree should not parent scholarships, clubs, and internships; re-home them so the orientation topic stops absorbing ~160 unrelated pages, and re-tag MDHS "before placement" pages under placements, not orientation.
- **Standardise the entry pattern:** retire faculty "accept your offer and get started" checklist duplicates in favour of linking students.unimelb.edu.au checklist, keeping only genuinely faculty-specific commencement steps (e.g. Law JD enrolment, Arts HDR commencement forms).

## Appendix — all orientation pages (289)

### FEIT — 204
- **4864w** · _mixed_ — [Self-sourced internships](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/self-sourced)
- **4609w** · _mixed_ — [International internships](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/self-sourced-international)
- **4456w** · _mixed_ — [University-sourced internships](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/university-sourced-internships)
- **3201w** — [Meet our graduate researchers](https://eng.unimelb.edu.au/students/research/life-at-feit/student-profile)
- **3148w** · _redirect_ — [Frequently Asked Questions](https://eng.unimelb.edu.au/students/coursework/progress-your-career/internship/faq)
- **3148w** — [Frequently Asked Questions](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/faq)
- **2516w** · _redirect_ — [Intercultural Career Mentoring Program](https://eng.unimelb.edu.au/students/coursework/student-experience/international-opportunities/ICMP)
- **2516w** — [Intercultural Career Mentoring Program](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/ICMP)
- **2512w** · _mixed_ — [How to plan your course?](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/further-support/how-to-plan-your-course)
- **2177w** — [FEIT Hackathon Festival](https://eng.unimelb.edu.au/students/coursework/student-experience/industry-series/feit-hackathon-festival)
- **2125w** — [Technical Skills Series](https://eng.unimelb.edu.au/students/coursework/student-experience/technical-skills)
- **2057w** — [My Course Planner](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/further-support/my-course-planner)
- **1990w** — [Global Challenges in Engineering – Jakarta](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/global-challenges-in-engineering-jakarta)
- **1859w** — [Reviewing your progress](https://eng.unimelb.edu.au/students/research/study-resources/progress-review)
- **1739w** — [Engineering and IT Conference Travel Grant](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students/scholarships/scholarships/travel)
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
- **873w** — [Community Awards FAQs](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/spotlight-celebrations/community-awards/faqs)
- **849w** — [2022 Dean’s Honours List](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/deans-honours-award/school-of-computing-and-information-systems-1)
- **823w** — [Course requirements](https://eng.unimelb.edu.au/students/research/study-resources/course-requirements)
- **820w** — [2024 Dean's Honours List](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/deans-honours-award/2024)
- **809w** — [Scholarships, Prizes and Awards Recipients](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/scholarships,-prizes-and-awards-recipients)
- **800w** — [Graduate Coursework and Research Students](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/feit-students-study-abroad-and-exchange/graduate-coursework-and-research-students)
- **797w** — [Stephen Ho Accelerator Grant](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships/scholarships/stephen-ho-accelerator-grant)
- **789w** — [International Research Opportunities](https://eng.unimelb.edu.au/students/coursework/student-experience/study-overseas/feit-students-study-abroad-and-exchange/international-research)
- **788w** — [Current students](https://eng.unimelb.edu.au/students)
- **787w** — [Scholarships - Coursework Students - Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/whats-next/coursework-students/scholarships)
- **783w** — [Scholarships - Coursework Students - Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships)
- **774w** — [Coursework students | Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/coursework)
- **756w** · _mixed_ — [New Student Checklist (International Students)](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/plan-to-attend-melbourne-orientation/new-student-checklist-international-students)
- **750w** — [Summer Round, 2026](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students/scholarships/summer-round)
- **734w** — [FAQs](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/deans-honours-award/faqs)
- **728w** · _redirect_ — [Internships - Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/coursework/progress-your-career/internship/internship-subjects)
- **728w** — [Scholarships for Graduate Researchers](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students/scholarships)
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
- **636w** · _redirect_ — [FEIT Student Exchange Funding and Scholarships](https://eng.unimelb.edu.au/students/coursework/progress-your-career/feit-students-study-abroad-and-exchange/saex-funding-and-scholarships)
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
- **572w** — [Thesis writing events](https://eng.unimelb.edu.au/students/research/life-at-feit/thesis-writing-events)
- **570w** — [Round 1 Scholarships](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships/round-one)
- **569w** — [Engineering and IT undergraduate scholarships, The University of Melbourne](https://eng.unimelb.edu.au/students/eng-and-it-community/scholarships)
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
- **523w** · _mixed_ — [Graduate Coursework Students (International)](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/class-registration/mytimetable)
- **522w** — [Acusensus Scholarship for Women in STEM](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships/scholarships/acusensus-scholarship-for-women-in-engineering)
- **522w** — [Other Scholarships](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students/scholarships/other-scholarships,-2023)
- **519w** — [Industry Series](https://eng.unimelb.edu.au/students/coursework/student-experience/industry-series)
- **516w** — [Engineering Practice Hurdle](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/practice-hurdle)
- **510w** — [Promote an Upcoming Event](https://eng.unimelb.edu.au/students/clubs/feature-in-the-feit-express-newsletter)
- **507w** — [Academic Skills](https://eng.unimelb.edu.au/students/coursework/study-resources/academic-skills)
- **506w** — [FEIT award winners 2023](https://eng.unimelb.edu.au/students/research/life-at-feit/award-winners)
- **502w** — [Student IT Contact](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/technology-requirements-and-available-resources/student-it-contact)
- **498w** — [John Balfour Memorial Scholarship](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/scholarships/scholarships/john-balfour)
- **494w** · _redirect_ — [Graduate Orientation](https://eng.unimelb.edu.au/students/coursework/orientation)
- **494w** — [Graduate Orientation](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation)
- **494w** — [PhD Write Up Award: Engineering and IT students, The University of Melbourne](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students/scholarships/scholarships/phd-write-up-award)
- **493w** — [Melbourne University Geomatics Society (MUGS)](https://eng.unimelb.edu.au/students/clubs/our-clubs/melbourne-university-geomatics-society-mugs)
- **489w** — [Community Awards](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/spotlight-celebrations/community-awards)
- **481w** — [Round 4 Scholarships](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/keep-in-touch/eng-and-it-calendar/upcoming-events/round-4-scholarships)
- **478w** — [Internships - Graduate Researchers - Current Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/research/life-at-feit/internships)
- **475w** — [Eligibility and selection criteria](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/coursework-students/deans-honours-award/eligibility-and-selection-criteria)
- **474w** · _mixed_ — [Graduate Coursework Students (Domestic)](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/class-registration/enrolling-in-subjects)
- **473w** — [Student Clubs and Societies](https://eng.unimelb.edu.au/students/clubs)
- **473w** — [Round 4 Scholarships](https://eng.unimelb.edu.au/students/eng-and-it-calendar/upcoming-events/round-4-scholarships)
- **473w** · _redirect_ — [Student Clubs and Societies](https://eng.unimelb.edu.au/students/coursework/progress-your-career/well-being-series/clubs)
- **471w** — [Graduate research resources](https://eng.unimelb.edu.au/students/research/study-resources)
- **469w** — [Skills Towards Employment Program](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/practice-hurdle/step)
- **464w** — [Round 3 Scholarships](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/whats-next/coursework-students/scholarships/round-two)
- **460w** — [Winter Round, 2026](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students/scholarships/winter-round)
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
- **433w** — [Undergraduate Prizes](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/undergraduate/subject-prizes-1)
- **433w** · _redirect_ — [~ Page not found](https://eng.unimelb.edu.au/students/coursework/orientation/after-orientation/whats-next/sap/scholarships/scholarships/m.k.n.-johansen-scholarship-for-the-advancement-of-municipal-engineering)
- **428w** — [Graduate Research Prizes](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students/graduate-research-awards)
- **428w** — [Prizes](https://eng.unimelb.edu.au/students/coursework/student-experience/industry-series/diversity-and-inclusion-case-competition/prizes)
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
- **374w** — [Intercultural Career Mentoring Program](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/keep-in-touch/eng-and-it-calendar/upcoming-events/2026/international-skills-series/intercultural-career-mentoring-program)
- **373w** — [Graduate Researchers](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/graduate-research-students)
- **373w** — [Chat with Student IT](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/technology-requirements-and-available-resources/chat-with-student-it)
- **368w** — [Life at FEIT](https://eng.unimelb.edu.au/students/research/life-at-feit)
- **368w** — [FEIT Student Event Calendar](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/after-orientation/keep-in-touch/eng-and-it-calendar)
- **366w** — [Intercultural Career Mentoring Program](https://eng.unimelb.edu.au/students/eng-and-it-calendar/upcoming-events/2026/international-skills-series/intercultural-career-mentoring-program)
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

### Biomedical (school) — 24
- **1663w** — [BIOM30003 Biomedical Science Research Project](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/biom30003-biomedical-science-research-project)
- **1543w** — [Biomedicine Deans' Honours List](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/biomedicine-deans-honours-list)
- **1459w** — [Breadth](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/breadth)
- **1459w** · _mixed_ — [Plan Your Course](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/study-plan-templates)
- **1452w** — [Quota Subjects](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/quota-subjects)
- **1184w** · _mixed_ — [Plan your First Year Subjects](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/plan-your-first-year-subjects)
- **1147w** — [Majors](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/majors)
- **836w** · _mixed_ — [Biomedicine Enrolment Advice Day](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/biomedicine-enrolment-advice-day)
- **809w** — [Student Societies](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/student-societies)
- **740w** — [Study Abroad and Exchange](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/study-abroad-and-exchange)
- **710w** — [Course Planning](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/master-of-biomedical-science/course-planning)
- **546w** — [Biomedicine Graduate Pathways](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/biomedicine-graduate-pathways)
- **532w** — [Concurrent Diplomas](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/concurrent-diplomas)
- **507w** — [Academic Skills](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/master-of-biomedical-science/academic-skills)
- **478w** — [Shape your biomedical sciences experience](https://biomedicalsciences.unimelb.edu.au/study/current-student-information)
- **449w** — [UROP](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/urop)
- **448w** — [Bachelor of Biomedicine at-a-glance](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine)
- **437w** — [Biomedicine Orientation](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/orientation)
- **420w** — [Academic Skills](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/academic-skills)
- **417w** — [Master of Biomedical Science](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/master-of-biomedical-science)
- **393w** — [Deans' Honours List](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/master-of-biomedical-science/deans-honours-list)
- **390w** — [Student Clubs and Societies](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/master-of-biomedical-science/student-clubs-and-societies)
- **362w** — [Your career](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/your-career)
- **281w** — [Orientation](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/master-of-biomedical-science/orientation)

### Arts — 20
- **1517w** — [Milestone reviews](https://arts.unimelb.edu.au/students/graduate-research/manage-your-research-program/milestone-reviews)
- **1369w** · _mixed_ — [Overview of course structure](https://arts.unimelb.edu.au/students/graduate-research/commencement/overview-of-course-structure)
- **1369w** · _mixed_ — [Overview of course structure](https://arts.unimelb.edu.au/students/graduate-research/commencement/overview-of-course-structure/_nocache)
- **913w** · _mixed_ — [Course enrolment information](https://arts.unimelb.edu.au/students/graduate-research/commencement/course-enrolment-information)
- **717w** — [Course conversion](https://arts.unimelb.edu.au/students/graduate-research/manage-your-research-program/conversion-and-transfer)
- **684w** · _mixed_ — [Current students | Faculty of Arts](https://arts.unimelb.edu.au/students)
- **676w** · _mixed_ — [Undergraduate students](https://arts.unimelb.edu.au/students/undergraduate)
- **550w** · _mixed_ — [Graduate coursework students](https://arts.unimelb.edu.au/students/graduate-coursework)
- **353w** — [Graduate research](https://arts.unimelb.edu.au/students/graduate-research)
- **353w** — [Graduate Research Orientation](https://arts.unimelb.edu.au/students/graduate-research/commencement/orientation-and-induction)
- **353w** — [Graduate Research Orientation](https://arts.unimelb.edu.au/students/graduate-research/commencement/orientation-and-induction/_nocache)
- **353w** — [Graduate Research Orientation](https://arts.unimelb.edu.au/students/graduate-research/plan-your-program2/orientation-and-induction)
- **338w** — [Thesis submission](https://arts.unimelb.edu.au/students/graduate-research/manage-your-research-program/thesis-requirements)
- **320w** — [Commencement form checklist](https://arts.unimelb.edu.au/students/graduate-research/commencement/commencement-checklist)
- **320w** — [Bachelor of Arts Orientation](https://arts.unimelb.edu.au/students/undergraduate/bachelor-of-arts-orientation)
- **320w** — [Commencement form checklist](https://arts.unimelb.edu.au/students/graduate-research/plan-your-program2/commencement-checklist)
- **197w** — [Facilities and resources](https://arts.unimelb.edu.au/students/graduate-research/faqs/resources)
- **157w** · _link-farm_ — [Commence your candidature](https://arts.unimelb.edu.au/students/graduate-research/commencement)
- **157w** · _link-farm_ — [Commence your candidature](https://arts.unimelb.edu.au/students/graduate-research/plan-your-program2)
- **102w** · _link-farm_ — [Support for your research](https://arts.unimelb.edu.au/students/graduate-research/faqs)

### MDHS — 14
- **662w** — [Before placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/melbourne-dental-school/before-placement)
- **496w** — [Before Placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/clinicalaudiology/before)
- **492w** — [Before Placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/mspgh/before-placement)
- **480w** — [During placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/clinicalaudiology/during-placement)
- **477w** — [Before placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/msps/professional-psychology/before-placement)
- **471w** — [Before placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/msps/clinical-psychology/before-placement)
- **431w** — [Before placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/msps/clinical-neuropsychology/before-placement)
- **394w** — [Day one of placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/mspgh/day-one-of-placement)
- **380w** — [Insurance](https://mdhs.unimelb.edu.au/study/current-students/placements/students/insurance)
- **372w** — [Before placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/department-of-nursing/before-placement)
- **353w** — [Before Placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/dsp/before-placement)
- **317w** — [Department of Clinical Audiology](https://mdhs.unimelb.edu.au/study/current-students/placements/org/clinicalaudiology)
- **304w** — [Day one of Placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/dsp/day-one-of-placement)
- **276w** — [Department of Social Work](https://mdhs.unimelb.edu.au/study/current-students/placements/org/department-of-social-work-resources)

### Law — 12
- **1823w** · _mixed_ — [Accept Your Offer & Get Started | JD | University of Melbourne](https://law.unimelb.edu.au/students/jd/studies/accept-your-offer-and-get-started)
- **594w** — [Enrolment and Re-Enrolment | Masters | Melbourne Law School](https://law.unimelb.edu.au/students/masters/studies/enrolment)
- **580w** — [Accept Your Offer & Get Started | Masters | Law at Melbourne](https://law.unimelb.edu.au/students/masters/studies/accept-your-offer-and-get-started)
- **516w** — [Enrolment and Re-Enrolment | JD | Melbourne Law School](https://law.unimelb.edu.au/students/jd/studies/enrolment)
- **509w** — [Orientation](https://law.unimelb.edu.au/students/orientation)
- **457w** — [Hossain Mohammad Reza](https://law.unimelb.edu.au/students/grd/students/hossain-mohammad-reza)
- **443w** — [Melbourne Law Masters](https://law.unimelb.edu.au/students/orientation/mlm-students)
- **338w** — [Jiacheng Gong](https://law.unimelb.edu.au/students/grd/students/jiacheng-gong)
- **319w** — [Ishika Chatterjee](https://law.unimelb.edu.au/students/grd/students/ishika-chatterjee)
- **271w** — [Rebekah Markey-Towler](https://law.unimelb.edu.au/students/grd/students/rebekah-markey-towler)
- **265w** — [Debaranjan Goswami](https://law.unimelb.edu.au/students/grd/students/debaranjan-goswami)
- **222w** — [Enrichment | Masters (Law) | Melbourne Law School](https://law.unimelb.edu.au/students/masters/enrichment)

### ABP/MSD — 6
- **582w** — [Master of Architectural Engineering](https://msd.unimelb.edu.au/current-students/course-planning/sample-course-plans/master-of-architectural-engineering)
- **558w** — [Semester 2 2017 Studio 27](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-27)
- **549w** — [MSD Peer Mentoring Program](https://msd.unimelb.edu.au/current-students/student-experience/peer-mentoring-program)
- **487w** — [Master of Architecture Studios](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture)
- **376w** — [Practical Experience](https://msd.unimelb.edu.au/current-students/subject-information/practical-experience)
- **365w** — [Graduate Diploma in Property Valuation Sample Course Plans](https://msd.unimelb.edu.au/current-students/course-planning/sample-course-plans/property-valuation)

### Science — 3
- **855w** — [Bachelor of Agriculture Orientation](https://science.unimelb.edu.au/students/course-guide-bachelor-of-agriculture/bag-orientation)
- **626w** — [Bachelor of Science Orientation](https://science.unimelb.edu.au/students/course-guide-bachelor-of-science/bsc-orientation)
- **578w** — [Getting started in your graduate science degree](https://science.unimelb.edu.au/students/course-guide-graduate-coursework-degrees/graduate-getting-started)

### FFAM — 3
- **409w** · _mixed_ — [Orientation](https://finearts-music.unimelb.edu.au/current-students/starting-out/orientation)
- **275w** — [Information for current students at the Faculty of Fine Arts and Music](https://finearts-music.unimelb.edu.au/current-students)
- **62w** · _link-farm_ — [Bachelor of Music student guide](https://finearts-music.unimelb.edu.au/current-students/starting-out/bachelor-of-music-student-guides)

### FBE — 2
- **576w** — [Orientation](https://fbe.unimelb.edu.au/students/bcom/orientation)
- **0w** · _redirect_ — [Sign In (SSO redirect)](https://fbe.unimelb.edu.au/students/bcom/first-semester-guide/week-1/connect-with-your-peer-mentor)

### MBS (school) — 1
- **591w** — [Orientation](https://mbs.unimelb.edu.au/students/orientation)
