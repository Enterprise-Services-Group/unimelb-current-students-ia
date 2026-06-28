# Uncrawled Domains Worth Scraping

*The 20-domain crawl covered the core student estate. But the link graph reveals 200+ uncrawled `*.unimelb.edu.au` hosts. These are the highest-value ones worth adding to a future crawl, ranked by inbound link volume and student impact. June 2026.*

---

## Executive summary

The 20-domain crawl captured the core current-student web estate: the hub, 12 faculty domains, study.unimelb, the Handbook, services, scholarships, and research. But the cross-site-flow.csv reveals **over 200 additional `*.unimelb.edu.au` hosts** that appear in the contextual link graph. Most are single-lab research microsites or archive hosts with negligible inbound links. But several are student-critical services currently invisible to the link-graph analysis because they were never crawled.

This audit identifies the highest-value uncrawled domains, ranked by inbound link volume and student-journey relevance.

---

## Priority tier 1 — student-critical, high inbound links

| Domain | Inbound links | What it is | Why it matters |
|---|---|---|---|
| **gradresearch.unimelb.edu.au** | 4,123 | Graduate Research Hub — HDR candidate lifecycle | The canonical owner of the HDR journey. Currently off-estate; byte-identical faculty clones link here. Crawling this completes the HDR picture. |
| **murrupbarak.unimelb.edu.au** | 805 | Indigenous student support unit | Zero presence on the hub. 19 hub links vs 614 from MSD. Crawling this reveals what Indigenous students actually find. |
| **ask.unimelb.edu.au** | 619 | Legacy FAQ knowledge base | The hub's #1 outbound destination (444 links). Where the actual answers to enrolment, census, fee, and visa questions live. Crawling this reveals what the hub defers to. |
| **my.unimelb.edu.au** | 237 | Student Information System (SIS) | Behind login — cannot be crawled. But the public-facing landing pages may be reachable and would reveal the logged-out experience students hit before authenticating. |
| **safercommunity.unimelb.edu.au** | 144 | Safety, crisis, sexual misconduct support | Separate uncrawled domain. The wellbeing journey audit flagged the off-brand counselling host; this is the safety equivalent. |
| **safety.unimelb.edu.au** | 516 | General safety & emergency | Linked 493 times from the Handbook alone. High inbound volume, student-relevant. |

## Priority tier 2 — student-adjacent, moderate inbound

| Domain | Inbound links | What it is | Why it matters |
|---|---|---|---|
| **library.unimelb.edu.au** | 221 | University library | Core student service. Hub sends 60 links. |
| **umsu.unimelb.edu.au** | 455 | Student union | Independent student organisation. Hub sends 49 links. |
| **studyos.students.unimelb.edu.au** | 168 | My Course Planner | The subject-planning tool. Referenced on ~830 hub pages but only 79 direct links from the hub; the rest are from other domains. |
| **studentit.unimelb.edu.au** | 173 | Student IT support | IT help, troubleshooting, software. Hub sends 55 links. |
| **gsa.unimelb.edu.au** | 243 | Graduate Student Association | Graduate student union. |
| **lms.unimelb.edu.au** | 148 | Learning Management System | Canvas/LMS entry point. Behind login but public landing pages may be reachable. |
| **canvas.lms.unimelb.edu.au** | 115 | Canvas LMS direct | Alternate LMS entry. |
| **online.unimelb.edu.au** | 51 | Online learning | Online/distance education portal. |
| **sport.unimelb.edu.au** | 67 | Sport & recreation | Student gym, sport clubs. |
| **events.unimelb.edu.au** | 574 | Events calendar | High-volume but chrome-level — mostly event listings, not service content. |
| **maps.unimelb.edu.au** | 491 | Campus maps | High-volume but utility — map tiles, not content. |

## Priority tier 3 — high inbound but non-student

| Domain | Inbound links | What it is | Note |
|---|---|---|---|
| findanexpert.unimelb.edu.au | 10,518 | Researcher profiles | Highest inbound in the estate. But researcher-facing, not student-facing. Large crawl cost, low student value. |
| about.unimelb.edu.au | 3,473 | University about pages | Mostly corporate/policy content. |
| staff.unimelb.edu.au | 1,742 | Staff intranet | Behind login. Students accidentally routed here (838 links from eng, 729 from msd). Not student content. |
| pursuit.unimelb.edu.au | 1,603 | Research stories / magazine | Public-facing but not student-service content. |
| policy.unimelb.edu.au | 1,275 | Policy library | Referenced for rules but not a student service. |
| giving.unimelb.edu.au | 933 | Donations / advancement | Alumni/donor-facing. |
| gateway.research.unimelb.edu.au | 879 | Research gateway | Researcher-facing. |

---

## Recommended crawl expansion

**Do crawl (tier 1):**
1. **gradresearch.unimelb.edu.au** — completes the HDR picture, closes the byte-identical duplication story
2. **murrupbarak.unimelb.edu.au** — reveals what Indigenous students actually find, closes the zero-hub-presence gap
3. **ask.unimelb.edu.au** — reveals the legacy FAQ content the hub defers to on 444 links
4. **safercommunity.unimelb.edu.au** — completes the wellbeing/safety picture

**Consider crawling (tier 2):**
5. **studyos.students.unimelb.edu.au** — My Course Planner, core planning tool
6. **library.unimelb.edu.au** — core student service, moderate inbound
7. **umsu.unimelb.edu.au** — student union, high inbound

**Skip:**
- my.unimelb (behind login, crawl will fail)
- findanexpert, about, staff, pursuit, policy, giving, gateway.research (not student-service content)
- events, maps (high-volume but chrome/utility, low analytical value)

---

## Crawl caveats

- **my.unimelb.edu.au** is behind authentication — a crawl will capture only the public login/splash pages, not the SIS content. Limited value.
- **ask.unimelb.edu.au** uses the same Imperva WAF as the Handbook — expect bot-block shells for a portion of captures. The SSR/WAF gap documented in the Handbook deep-dive applies here too.
- **studyos.students.unimelb.edu.au** (My Course Planner) may require authentication for the actual planning tool, but the public landing/support pages should be crawlable.
- All uncrawled domains should be checked for the same patterns found in the crawled estate: parallel URL trees, _nocache variants, sandbox leakage, blank titles.

---

*Built from: cross-site-flow.csv (full uncrawled domain inventory), page-weight.csv (crawled domain list), and improvements-register.md (subdomain registry recommendation). June 2026.*
