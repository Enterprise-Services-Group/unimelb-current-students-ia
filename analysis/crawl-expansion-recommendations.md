# Uncrawled Domain Crawl Recommendations — Link-Graph Analysis

*Which sites should be scraped next, ranked by link volume from the 20-domain crawled estate, number of crawled sources, and student-journey relevance. Every domain is tagged by journey, feasibility, and crawl priority. June 2026.*

---

## Method

The 20-domain crawl seeded a forward link graph: every outbound link from every crawled page was recorded, producing `cross-site-flow.csv` with 20 unique source domains linking to 200+ destination domains. This analysis ranks every uncrawled destination by:

1. **Total inbound links from the crawled estate** — raw volume
2. **Source breadth** — how many of the 20 crawled domains link to it (higher = more embedded in the estate)
3. **Student-journey relevance** — which persona journey(s) depend on it
4. **Crawl feasibility** — public vs behind-login, WAF risk, crawl cost

**Limitation:** The link graph is forward-only. We know everything the crawled estate links *to*, but nothing about what uncrawled domains link *back*. The 20 seed domains are the only sources in the graph.

---

## Tier 1 — Must crawl (student-critical, high volume, high breadth)

### 1. gradresearch.unimelb.edu.au — Graduate Research Hub

| Metric | Value |
|---|---|
| Inbound from crawled | **4,123** (rank 2) |
| Crawled sources | **18/20** (rank 2) |
| Top linkers | education 1,972, mdhs 1,882, students 60 |
| Journey | HDR candidate (HIGH severity) |
| Feasibility | ✅ Public, crawlable |
| Why | The canonical owner of the HDR candidature lifecycle. 33 byte-identical pages duplicated across education+mdhs point here. The HDR journey's spine is currently invisible. Crawling this completes the HDR picture and enables deduplication. |

### 2. murrupbarak.unimelb.edu.au — Indigenous Student Support

| Metric | Value |
|---|---|
| Inbound from crawled | **805** (rank 11) |
| Crawled sources | **17/20** (rank 4) |
| Top linkers | msd 614, study 79, mdhs 49, **students 19** |
| Journey | Indigenous student (HIGH severity) |
| Feasibility | ✅ Public, crawlable |
| Why | The hub links Murrup Barak 19 times; MSD links it 614. The most extreme ratio in the estate. Zero Indigenous pages on the hub. Crawling this reveals what Indigenous students actually find when they arrive. |

### 3. ask.unimelb.edu.au — Legacy FAQ Knowledge Base

| Metric | Value |
|---|---|
| Inbound from crawled | **619** (rank 12) |
| Crawled sources | **18/20** (rank 2) |
| Top linkers | **students 444**, education 37, mdhs 28, handbook 25 |
| Journey | Every persona — enrolment, fees, census, visas |
| Feasibility | ⚠ WAF risk (Imperva, same as Handbook). Expect bot-block captures. |
| Why | The hub's #1 outbound destination (444 links). Where the actual answers to enrolment, census, fee, and visa questions live. The hub describes; ask.unimelb answers. Without crawling this, we don't know what the hub defers to. |

### 4. safercommunity.unimelb.edu.au — Safety, Crisis & Sexual Misconduct Support

| Metric | Value |
|---|---|
| Inbound from crawled | **144** (rank 38) |
| Crawled sources | **12/20** (rank 15) |
| Top linkers | students 62, mdhs 30, education 23 |
| Journey | Taylor (wellbeing), Alex (at-risk) — HIGH severity |
| Feasibility | ✅ Public, crawlable |
| Why | The wellbeing audit found counselling branded "Academic Skills Unit." Safer Community — the crisis/safety service — lives on a completely separate domain. Crawling this completes the wellbeing/safety picture. |

### 5. studyos.students.unimelb.edu.au — My Course Planner

| Metric | Value |
|---|---|
| Inbound from crawled | **168** (rank 34) |
| Crawled sources | **6/20** |
| Top linkers | students 79, arts 68, fbe 10, eng 8 |
| Journey | Sam, Jordan — course planning (HIGH severity) |
| Feasibility | ⚠ May require auth for planner tool; public landing pages crawlable |
| Why | Referenced on ~830 hub pages but only 79 direct links from the hub. The subject-planning tool every student depends on. Crawling the public-facing pages reveals what students see before login. |

---

## Tier 2 — Should crawl (student-adjacent, moderate volume, high breadth)

### 6. library.unimelb.edu.au — University Library

| Metric | Value |
|---|---|
| Inbound from crawled | **221** (rank 29) |
| Crawled sources | **13/20** (rank 12) |
| Top linkers | students 60, research 36, education 35 |
| Journey | All personas — core academic service |
| Feasibility | ✅ Public, crawlable |

### 7. umsu.unimelb.edu.au — Student Union

| Metric | Value |
|---|---|
| Inbound from crawled | **455** (rank 18) |
| Crawled sources | **15/20** (rank 7) |
| Top linkers | mdhs 85, arts 79, education 75, eng 50, students 49 |
| Journey | All personas — student life, advocacy, clubs |
| Feasibility | ✅ Public, crawlable (independent org, not UoM CMS) |

### 8. studentit.unimelb.edu.au — Student IT Support

| Metric | Value |
|---|---|
| Inbound from crawled | **173** (rank 33) |
| Crawled sources | **12/20** (rank 15) |
| Top linkers | students 55, education 33, mdhs 30, eng 24 |
| Journey | All personas — IT help, software, troubleshooting |
| Feasibility | ✅ Public, crawlable |

### 9. gsa.unimelb.edu.au — Graduate Student Association

| Metric | Value |
|---|---|
| Inbound from crawled | **243** (rank 25) |
| Crawled sources | **16/20** (rank 5) |
| Top linkers | mdhs 86, education 80, students 15 |
| Journey | Priya, HDR — graduate students |
| Feasibility | ✅ Public, crawlable |

### 10. my.unimelb.edu.au — Student Information System (SIS)

| Metric | Value |
|---|---|
| Inbound from crawled | **237** (rank 26) |
| Crawled sources | **10/20** |
| Top linkers | **students 187**, law 14, arts 10 |
| Journey | Every persona — enrolment, results, fees, timetable |
| Feasibility | ❌ Behind login. Only splash/login pages crawlable. Limited value. |
| Why | The single most important destination in the estate. But the public landing page is the only crawlable surface. A crawl confirms what students see before login — worth the minimal cost. |

### 11. lms.unimelb.edu.au — Learning Management System

| Metric | Value |
|---|---|
| Inbound from crawled | **148** (rank 35) |
| Crawled sources | **12/20** (rank 15) |
| Top linkers | students 37, msd 36, law 26 |
| Journey | All personas — Canvas/LMS entry point |
| Feasibility | ❌ Behind login. Public landing page only. |

### 12. canvas.lms.unimelb.edu.au — Canvas LMS Direct

| Metric | Value |
|---|---|
| Inbound from crawled | **115** (rank 43) |
| Crawled sources | **15/20** (rank 7) |
| Top linkers | students 27, law 24, finearts 10, mbs 10 |
| Journey | All personas — learning delivery |
| Feasibility | ❌ Behind login. Public landing page only. |

---

## Tier 3 — Consider crawling (niche audiences, lower volume)

### 13. online.unimelb.edu.au — Online Learning Portal

| Metric | Value |
|---|---|
| Inbound from crawled | **51** (rank >50) |
| Crawled sources | **3/20** |
| Top linkers | study 47 |
| Journey | Online/micro-credential learner (MEDIUM severity) |
| Feasibility | ✅ Public, crawlable |
| Why | The online learner is orphaned between estates. The portal may reveal a current-student experience we haven't traced. |

### 14. sport.unimelb.edu.au — Sport & Recreation

| Metric | Value |
|---|---|
| Inbound from crawled | **67** |
| Crawled sources | **12/20** |
| Top linkers | mdhs 14, students 14 |
| Journey | All personas — student life |
| Feasibility | ✅ Public, crawlable |

### 15. orientation.unimelb.edu.au — Orientation

| Metric | Value |
|---|---|
| Inbound from crawled | **1** |
| Crawled sources | **1/20** (biomed only) |
| Journey | Sam — commencing student transition |
| Feasibility | ✅ Public, crawlable |
| Why | Near-zero inbound but the commencing-student transition is a lifecycle seam. May be linked from my.unimelb (behind login) rather than the public estate. Crawl cost is low. |

### 16. exams.unimelb.edu.au — Exams

| Metric | Value |
|---|---|
| Inbound from crawled | **2** |
| Crawled sources | **1/20** (students only) |
| Journey | All personas — exam timetables, results |
| Feasibility | ✅ Public, crawlable |
| Why | Low inbound but high student relevance. May be linked primarily from my.unimelb behind login. |

### 17. breadth.unimelb.edu.au — Breadth Subjects

| Metric | Value |
|---|---|
| Inbound from crawled | **7** |
| Crawled sources | **1/20** (handbook only) |
| Journey | Sam, Jordan — course planning |
| Feasibility | ✅ Public, crawlable |

---

## Tier 4 — Skip (non-student, chrome/utility, or impossible)

### Skip — not student-facing

| Domain | Inbound | Why skip |
|---|---|---|
| findanexpert.unimelb.edu.au | 10,518 | Researcher profiles. Highest inbound in estate but zero student-service content. |
| about.unimelb.edu.au | 3,473 | Corporate/about pages. Not student-service. |
| staff.unimelb.edu.au | 1,742 | Staff intranet. Behind login. Students accidentally routed here. |
| pursuit.unimelb.edu.au | 1,603 | Research stories magazine. Public but not service content. |
| policy.unimelb.edu.au | 1,275 | Policy library. Referenced for rules. |
| giving.unimelb.edu.au | 933 | Donations/advancement. Alumni-facing. |
| gateway.research.unimelb.edu.au | 879 | Research gateway. Researcher-facing. |

### Skip — chrome/utility only

| Domain | Inbound | Why skip |
|---|---|---|
| events.unimelb.edu.au | 574 | Event listings. High volume, low analytical value. |
| maps.unimelb.edu.au | 491 | Campus maps. Utility tiles. |
| search.unimelb.edu.au | 431 | Site search. Crawling it yields search results, not content. |
| go.unimelb.edu.au | 175 | URL shortener/redirect. |
| ecommerce.unimelb.edu.au | 191 | Payment gateway. Transactional, not content. |
| q.surveys.unimelb.edu.au | 231 | Survey platform. |

### Skip — duplicate/www-twin

| Domain | Inbound | Why skip |
|---|---|---|
| www.findanexpert.unimelb.edu.au | 1,409 | www-twin of findanexpert. Crawl canonical only. |

---

## Recommended crawl order

| # | Domain | Links | Sources | Journeys served | Feasibility |
|---|---|---|---|---|---|
| 1 | **gradresearch.unimelb.edu.au** | 4,123 | 18/20 | HDR | ✅ Public |
| 2 | **ask.unimelb.edu.au** | 619 | 18/20 | All (enrolment, fees, census, visas) | ⚠ WAF risk |
| 3 | **murrupbarak.unimelb.edu.au** | 805 | 17/20 | Indigenous | ✅ Public |
| 4 | **safercommunity.unimelb.edu.au** | 144 | 12/20 | Wellbeing, crisis | ✅ Public |
| 5 | **studyos.students.unimelb.edu.au** | 168 | 6/20 | Course planning | ⚠ Partial auth |
| 6 | **library.unimelb.edu.au** | 221 | 13/20 | All academic | ✅ Public |
| 7 | **umsu.unimelb.edu.au** | 455 | 15/20 | Student life | ✅ Public |
| 8 | **studentit.unimelb.edu.au** | 173 | 12/20 | IT support | ✅ Public |
| 9 | **gsa.unimelb.edu.au** | 243 | 16/20 | Graduate students | ✅ Public |
| 10 | **online.unimelb.edu.au** | 51 | 3/20 | Online learners | ✅ Public |
| 11 | **sport.unimelb.edu.au** | 67 | 12/20 | Student life | ✅ Public |
| 12 | **my.unimelb.edu.au** | 237 | 10/20 | All (SIS) | ❌ Behind login |
| 13 | **lms.unimelb.edu.au** | 148 | 12/20 | All (Canvas) | ❌ Behind login |
| 14 | **canvas.lms.unimelb.edu.au** | 115 | 15/20 | All (Canvas) | ❌ Behind login |
| 15 | **orientation.unimelb.edu.au** | 1 | 1/20 | Commencing | ✅ Public |
| 16 | **exams.unimelb.edu.au** | 2 | 1/20 | Exam periods | ✅ Public |
| 17 | **breadth.unimelb.edu.au** | 7 | 1/20 | Course planning | ✅ Public |

---

## What crawling these would unlock

| Domain | What it answers |
|---|---|
| gradresearch | Completes the HDR journey picture. Confirms/denies the byte-identical duplication. Reveals the off-estate HDR experience. |
| ask.unimelb | Reveals what the hub's 444 links actually defer to. Identifies which answers can be migrated back to the hub. Maps the legacy FAQ inventory. |
| murrupbarak | Reveals what Indigenous students find. Closes the most extreme link asymmetry in the estate (19 hub vs 614 MSD). |
| safercommunity | Completes the wellbeing/safety picture alongside the services.unimelb counselling audit. |
| studyos | Reveals the My Course Planner public experience. Confirms whether the "two planning tools" problem is visible to students. |
| library, umsu, studentit, gsa | Fills in the core service ecosystem around the hub. |
| online | Reveals the orphaned online-learner experience. |

---

*Built from: cross-site-flow.csv (full forward link graph), page-weight.csv (20 crawled domains), and the 14 existing deep-dives mapping every student journey. June 2026.*
