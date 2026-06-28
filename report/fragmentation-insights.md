# Fragmentation, Duplication & the Student Experience
## Insights from the University of Melbourne Web Estate Audit

**June 2026**

---

## Executive Summary

The University of Melbourne's web estate for current students spans **19 separate websites** containing over **36,500 pages**. A student trying to find information about their course, fees, placements, or graduation must navigate a landscape where the same topic appears across 9 to 11 different websites, where there are five different URL conventions for "information for current students", and where the pathway from enrolled student to graduate to alumnus is structurally broken at the web level.

This report synthesises findings from a comprehensive crawl and analysis of the entire estate. It is written for decision-makers who need to understand what a student actually experiences — not the technical architecture, but the fragmentation, duplication, and gaps that shape the day-to-day experience of being a student at Melbourne.

**Key finding:** The fragmentation problem is not primarily between the central hub and faculty sites. It is **faculty-to-faculty** — 65% of content is genuinely unique and discipline-specific, but it is distributed across 13 separate sites with no consistent navigation, labelling, or cross-linking. The real duplication is thin (~120–180 pages) but the **discoverability problem** affects every student, every day.

---

## 1. The Estate at a Glance

The current-student digital experience is delivered across 19 distinct websites:

| Site | Pages | Role |
|------|------:|------|
| students.unimelb.edu.au | 833 | Central hub — academic skills, admin, support |
| study.unimelb.edu.au | 4,048 | Prospective students — course finder, fees, entry requirements |
| 9 faculty sites | 25,568 | Faculty-specific content (largest: mdhs 6,079, law 3,188) |
| 3 school sub-sites | 1,871 | Biomedical, MBS, Dental — independent CS sections |
| scholarships.unimelb.edu.au | 2,226 | Dedicated scholarships domain |
| handbook.unimelb.edu.au | 3,000 | Subject and course handbook |
| services.unimelb.edu.au | 176 | Central services directory |
| alumni (www.unimelb.edu.au/alumni) | 137 | Graduate and alumni community |

A student's experience of this estate is shaped not by its total size but by **where their faculty sits on the fragmentation spectrum** — a continuum from central-dependent to self-contained.

---

## 2. The Five-URL Problem

The single concept "information for current students" is served at five different URL patterns across the university:

| URL Pattern | Faculties Using It |
|-------------|-------------------|
| `/students` | Law, Arts, FEIT, Science, FBE |
| `/current-students` | ABP/MSD, FFAM |
| `/study/current-students` | Education, MDHS |
| `/study/student-resources` | Dental School |
| `/study/current-student-information` | Biomedical Sciences School |

**Impact on the student:** A student transferring between faculties — or simply helping a friend in another faculty — cannot guess where their information lives. The URL convention carries no meaning across the university. This is the most basic discoverability failure in the estate and the easiest to fix.

**Recommendation:** Standardise on a single URL convention. Every faculty should serve its current-student content at `/students`. Redirect existing URLs.

---

## 3. The Fragmentation Spectrum

Not all fragmentation is equal. Faculties fall on a spectrum from "central-dependent link directories" to "self-contained parallel ecosystems":

```
CENTRAL-DEPENDENT ←————————————————————————————————→ SELF-CONTAINED
    ABP     FBE    Education   Arts   Science   MDHS    Law    FFAM    FEIT
```

**At the central-dependent end (ABP, FBE):** The current-student section is primarily a list of links pointing to students.unimelb.edu.au. A student finds most transactional content on the central hub but loses faculty context. Course planning advice, placement information, and discipline-specific support are thin.

**In the middle (Education, Arts, Science):** These faculties maintain a balance — faculty-specific content for discipline needs, with central-redirect for standard transactions. A student gets context-relevant advice without duplicated admin content. This is the closest the estate comes to a working model.

**At the self-contained end (Law, FEIT, FFAM):** These faculties run parallel systems. Law has its own course planning tools, careers services, scholarship listings, and academic skills resources — all on law.unimelb.edu.au, with minimal links to the central hub. FEIT operates a similarly complete parallel universe. An FEIT student and an Arts student have fundamentally different web experiences of the same university.

**Impact on the student:** The experience of being a "University of Melbourne student" does not exist. You are an Arts student, a Law student, or an FEIT student. The quality, depth, and structure of the web experience is determined entirely by faculty choice, not by university-wide student-experience standards.

**Recommendation:** Set a university-wide minimum standard for current-student content. Every faculty must maintain a current-students section with at minimum: course planning guidance, key contacts, placement information (where applicable), and a clear pathway to central services. Faculties can exceed this standard but not fall below it.

---

## 4. The School-Level Split

In two faculties, the fragmentation extends below the faculty level to individual schools:

**MDHS** is the most fragmented. The faculty site (mdhs.unimelb.edu.au) carries a thin central landing page with four cards. But three schools run their own independent current-student sections on separate subdomains: Biomedical Sciences, Dental School, and the Melbourne School of Population and Global Health. A student in the Medical School gets routed to the faculty page; a Biomedical Sciences student gets a completely separate site.

**FBE** has a similar split: the main faculty site serves BCom and PhD students, while the Melbourne Business School (mbs.unimelb.edu.au) runs an independent section for graduate business programs.

No other faculty has school-level fragmentation. Arts schools, Science schools, FEIT schools — all route through a single faculty page.

**Impact on the student:** An MDHS student's experience depends on which school they belong to — not which faculty. Two students in the same faculty can have entirely different web experiences, different navigation, and different access to information. This is fragmentation within fragmentation.

**Recommendation:** MDHS and FBE should consolidate school-level CS sections into the faculty site. Where schools have genuinely unique content (e.g. Dental School clinical placements), it should be a section within the faculty CS page, not a separate website.

---

## 5. Topic Fragmentation: Every Faculty Has Its Own Version

The most pervasive form of fragmentation is not structural — it is topical. Across the estate, **22 topics** are covered by multiple faculties independently:

| Topic | Pages Across Estate | Faculties Covering It |
|-------|--------------------|---------------------|
| Placements & WIL | 186 | 9 faculty sites |
| Subjects & Timetable | 174 | 11 faculty sites |
| Course Planning | 107 | 10 faculty sites |
| Scholarships | 100 | 9 faculty sites |
| Research Candidature | 96 | 9 faculty sites |
| Orientation | 76 | 10 faculty sites |
| International | 74 | 9 faculty sites |
| Student Life | 68 | 10 faculty sites |
| Careers & Employability | 63 | 9 faculty sites |
| Clubs & Events | 46 | 9 faculty sites |

Every one of these topics is reproduced independently by most faculties. A student cannot compare placement options across faculties, cannot see all scholarship opportunities in one place, and cannot understand what "orientation" means at Melbourne without first knowing which faculty they belong to.

**The fragmentation is not malicious — it is organic.** Each faculty built content for its own students. No mechanism exists to surface that content across faculty boundaries.

**Recommendation:** For each high-fragmentation topic, create a central landing page on students.unimelb.edu.au that aggregates and links to faculty-specific detail. The central page provides the overview, comparison, and navigation; faculties retain ownership of discipline-specific depth.

---

## 6. The Lifecycle Handoff Problem

The University's web estate has three distinct lifecycle phases, and the handoffs between them are broken:

```
PROSPECTIVE           →   CURRENT STUDENT        →   GRADUATE/ALUMNI
study.unimelb.edu.au      students.unimelb +        alumni.unimelb.edu.au
                          13 faculty sites
```

**Prospective → Current Student:** study.unimelb.edu.au contains 4,048 pages — course finders, ATAR tables, the Moving Guide for international students, living cost estimators, and a 6,294-word Glossary that functions as an enrolled-student orientation document. It sends 273 outbound links to students.unimelb.edu.au but has no "you're enrolled: start here" pathway. New students land mid-prospectus, dumped into a site designed for applicants.

**Current Student → Alumni:** This handoff does not exist. Across all 36,500+ pages in the current-student estate, there are **zero links** to alumni.unimelb.edu.au. A graduating student is never told about:
- The global alumni chapter network (12 faculty-specific mentoring streams)
- Graduate benefits (library access, alumni email, career tools, language learning, journal access)
- The "Welcome new alumni" page (1,745 words of content that no graduating student will ever see)
- Alumni awards, council, or community

Graduation is an exit with no destination.

**Impact on the student:** The University operates three separate websites for three phases of what should be a single lifecycle. A student experiences these as disconnected islands. The most expensive acquisition channel (prospective marketing) has no handoff to retention. The most valuable retention outcome (alumni engagement) receives no warm handoff from graduation.

**Recommendation:** Build a single lifecycle navigation element that appears on every page across all three sites: "Prospective → Current → Alumni." Add a graduation pathway page on students.unimelb.edu.au that introduces alumni benefits, the chapter network, and the mentoring pipeline. Add alumni links to every faculty's final-year and graduation content.

---

## 7. Content Quality: Most Faculty Content Is Genuinely Unique

A persistent concern in web consolidation projects is that faculty sites are mostly "link farms" — pages that just redirect to the central hub. The data contradicts this:

| Classification | Pages | % |
|---------------|-------|---|
| Unique (substantive, faculty-specific) | 755 | 65% |
| Mixed (some unique content + some redirection) | 323 | 28% |
| Link-farm (mostly links to central hub) | 70 | 6% |
| Redirect (pass-through only) | 5 | <1% |

**Sixty-five percent of faculty current-student content is genuinely unique.** Placements (186 pages), course planning (107 pages), research candidature (96 pages), and careers (63 pages) represent real, discipline-specific content that a central hub cannot replicate. The remaining 34% (mixed + link-farm) is where consolidation makes sense.

**Impact on the student:** The content is not the problem — the discoverability is. A student cannot find content that exists. The solution is not to centralise everything but to make everything findable from everywhere.

**Recommendation:** Consolidate the 70 link-farm pages into the central hub. For the 755 unique pages, build cross-faculty aggregation pages on the central hub that surface discipline-specific content to students who might benefit from it — regardless of which faculty created it.

---

## 8. The Scholarships Three-Way Split

Scholarships represent the most fragmented single topic in the estate:

| Site | Scholarship Pages |
|------|------------------:|
| scholarships.unimelb.edu.au (dedicated domain) | 2,226 |
| Faculty sites (9 faculties) | 100 |
| study.unimelb.edu.au (prospective) | 75 |
| alumni.unimelb.edu.au (alumni-funded scholarships) | 1 |

A dedicated scholarships domain exists (2,226 pages) but is **not consistently linked** from any of the three sites where students actually look for scholarships. Faculty sites list their own. study.unimelb lists entry scholarships. alumni.unimelb lists alumni-funded opportunities. No page aggregates all four sources into a single student view.

**Impact on the student:** A student must check four different websites to find all scholarships they are eligible for. Some scholarships will be discovered only by accident. The least-privileged students — those least likely to know the system — are the most likely to miss opportunities.

**Recommendation:** Make scholarships.unimelb.edu.au the single canonical source. Every faculty scholarship page, every study.unimelb listing, and every alumni-funded opportunity should link to and be discoverable from one place. The dedicated domain exists — it just needs to be wired into the estate.

---

## 9. The Study Hub Problem: Enrolled Content on a Prospective Site

study.unimelb.edu.au is the University's prospective student site — built for applicants considering Melbourne. But the crawl reveals it contains substantial content that enrolled students actually need:

- **Graduate Degree Packages** (14+ pages, 2,000–4,700 words each): The University's enrolled-student pathway product lives on the prospective site
- **The Moving Guide**: A post-offer, pre-arrival guide for international students — the highest-stakes misplaced content in the estate
- **The Glossary** (6,294 words): Functions as an enrolled-student orientation document
- **Course finder / degree browser** (81 pages): Has no equivalent in the current-student estate
- **Campus life content** (109 pages): Framed as "will I fit in?" not "how do I participate?"

study.unimelb sends 273 outbound links to students.unimelb.edu.au — confirming that enrolled students are already using it. But the site has no awareness that its audience includes enrolled students. A student who lands on study.unimelb to look up their course structure is treated as a prospective applicant.

**Impact on the student:** Enrolled students are using a site designed for prospects, receiving messaging designed for applicants, and finding no pathway back to the enrolled-student experience. The University speaks to its own students in a voice designed for people who haven't yet decided to attend.

**Recommendation:** Move the Moving Guide, Graduate Degree Packages, and Glossary to students.unimelb.edu.au. Add a prominent "Current students: start here" pathway on study.unimelb that recognises enrolled users and routes them appropriately.

---

## 10. The Uneven Experience: Your Faculty Determines Your Web Experience

The 19-site estate creates an experience lottery. The quality and comprehensiveness of a student's web experience is determined by which faculty they join — not by any university-wide standard:

| Faculty | CS Pages | Experience Quality |
|---------|---------:|-------------------|
| FEIT | 1,985 | Rich, self-contained — parallel ecosystem |
| Law | 3,188 | Comprehensive — own course planning, careers, scholarships |
| Medicine | 3,213 | Extensive — deep discipline-specific content |
| Arts | 2,446 | Well-structured — good balance of local + central |
| MDHS | 6,079 | Largest but most fragmented — school-level splits |
| MBS | 83 | Thin — minimal dedicated content |

An FEIT student has access to detailed course planning tools, faculty-specific scholarship listings, discipline-relevant careers advice, and academic skills resources — all within the FEIT site. An MBS student has 83 pages. They are both students at the same university.

**Impact on the student:** The University does not deliver a consistent student experience. The quality of information available to a student is a function of their faculty's web investment, not of any institutional commitment to student support.

**Recommendation:** Establish a university-wide minimum standard for current-student web content. Every faculty must meet a baseline: course planning guidance, key contacts, placement information (where applicable), and clear pathways to central services. Audit annually.

---

## 11. The Gap Analysis: What Students Cannot Find

Several critical pieces of information that students need are either missing or trapped on the wrong site:

| What Students Need | Where It Is | Problem |
|-------------------|-------------|---------|
| All scholarships I'm eligible for | 4 different sites | No single view exists |
| What happens after graduation | alumni.unimelb.edu.au | Zero links from current-student estate |
| How to plan my course | 10 faculty sites, study.unimelb, handbook | No cross-faculty comparison |
| Placement opportunities | 9 faculty sites | Cannot compare across faculties |
| Career pathways after my degree | Faculty sites + alumni mentoring | Two parallel systems, no connection |
| Support services available to me | students.unimelb + faculty sites | Fragmented; faculty-dependent |
| What my faculty offers vs central services | Neither site makes this clear | Student must discover through trial and error |

**Impact on the student:** Students must triangulate information across multiple sites with no guidance about which source is authoritative for which question. The University has not told its students where to look — it expects them to figure it out.

**Recommendation:** For each high-stakes student question (scholarships, placements, course planning, graduation), designate a single canonical starting point and ensure every related page across the estate links to it. The starting point provides overview and navigation; faculty pages provide depth.

---

## 12. Recommendations

### Immediate (this semester)

1. **Standardise the URL convention.** Every faculty CS section at `/students`.
2. **Fix the life cycle navigation.** Add "Prospective → Current → Alumni" navigation element across all sites.
3. **Build the graduation pathway.** A single page on students.unimelb.edu.au introducing alumni benefits, chapters, and mentoring — linked from every faculty's graduation content.

### Short-term (next 6 months)

4. **Consolidate the 70 link-farm pages** into students.unimelb.edu.au.
5. **Wire scholarships.unimelb.edu.au** as the canonical source — link from every faculty and from study.unimelb.
6. **Move the Moving Guide, Graduate Degree Packages, and Glossary** from study.unimelb to students.unimelb.
7. **Consolidate MDHS and FBE school-level CS sections** into faculty sites.
8. **Create cross-faculty topic aggregation pages** on students.unimelb for placements, course planning, careers, and scholarships.

### Medium-term (12 months)

9. **Establish university-wide minimum content standards** for faculty CS sections — audit annually.
10. **Build a "prospective → enrolled" recognition pathway** on study.unimelb that routes enrolled users to students.unimelb.
11. **Create a single signposting framework** — for every high-stakes student question, one canonical starting point that every related page links to.

---

*This report is based on analysis of 36,500+ pages across 19 University of Melbourne websites, crawled in June 2026. The crawl captured full HTML content for every page, with per-page link graphs, topic classification, and cross-site overlap analysis. All findings are evidence-grounded and traceable to specific pages in the corpus.*
