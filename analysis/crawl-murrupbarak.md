# murrupbarak.unimelb.edu.au — Crawl Analysis

*The Indigenous student support unit — 37 pages. Well-structured, comprehensive, and completely disconnected from the student hub (19 hub links vs 614 from MSD). Confirms the equity deep-dive: the service exists and is good; the hub just doesn't route to it. June 2026.*

---

## What we found

Murrup Barak is the University's Indigenous student support unit. The equity deep-dive identified it as the most extreme link asymmetry in the estate: the student hub links it 19 times; MSD links it 614 times (a 30:1 ratio). The crawl reveals a **37-page, well-structured site** that provides comprehensive Indigenous student support — confirming the service is real and well-built. The problem is purely routing.

### Structure

| Section | Pages | Content |
|---|---|---|
| `/home/study` | 12 | Indigenous student study resources, pathways, tutoring |
| `/home/about` | 7 | About Murrup Barak, team, history, values |
| `/home/student-experience` | 6 | Student life, community, events, cultural activities |
| `/home/financial-support` | 4 | Scholarships, bursaries, financial assistance |
| `/home/outreach` | 3 | Schools outreach, community engagement |
| `/home/contact-us` | 2 | Contact, locations |
| `/home/accommodation` | 1 | Student accommodation support |

The IA is clean: **study → student-experience → financial-support → accommodation → outreach → contact.** A student landing here can navigate their needs intuitively.

### What the site covers

Sampling titles reveals comprehensive coverage:

- "Murrup Barak" — landing page
- "Study" — academic support
- "Student Accommodation" — housing
- "Careers and Employment" — career support
- "Financial support" — scholarships and aid
- "Application process" — how to engage
- "Contact us" — locations and people

The content spans the full student lifecycle: academic support, financial aid, accommodation, careers, and community. This is everything the equity deep-dive said should exist on the hub — and it does exist, just not on the hub.

### Link analysis

| Outbound destination | Links in 30-page sample | Role |
|---|---|---|
| www.unimelb.edu.au | 242 | Extreme chrome — every page carries ~8 corporate links |
| about.unimelb.edu.au | 132 | Chrome |
| students.unimelb.edu.au | 37 | Hub — thin connection back |
| study.unimelb.edu.au | 31 | Prospective site |
| giving.unimelb.edu.au | 30 | Donations |
| safety.unimelb.edu.au | 30 | Chrome |
| library.unimelb.edu.au | 30 | Chrome |
| staff.unimelb.edu.au | 30 | Chrome |
| forms.your.unimelb.edu.au | 16 | Transactional forms |
| scholarships.unimelb.edu.au | 11 | Scholarships |

The site links BACK to students.unimelb 37 times — but the hub only links to Murrup Barak 19 times. **The connection is directional: Murrup Barak links to the hub; the hub barely reciprocates.**

### Page weight

Extremely consistent: median 142KB, max 159KB, min 134KB. All pages are within a 25KB range — suggesting a uniform template with consistent content depth. One of the most consistent sites in the estate.

---

## What this means

### 1. The service exists and is good — the routing is broken

Murrup Barak is a comprehensive, well-structured Indigenous student support unit. Every journey stage is covered. The 19 hub links vs 614 MSD links is not a content gap — it's a routing failure. **The hub should be the #1 router to Murrup Barak; instead it's #11.**

### 2. The chrome overload is extreme

242 www.unimelb.edu.au links in 30 pages = ~8 corporate chrome links per page. On a 37-page site, every page carries the full corporate footer. This is the same chrome-inflation pattern seen across the estate.

### 3. The www-twin is confirmed

The equity deep-dive noted murrupbarak.unimelb.edu.au vs www.murrupbarak.unimelb.edu.au as one of the 28 www-twins. The crawl confirms the bare domain resolves and has content. The www-twin should 301 to the bare domain (or vice versa).

### 4. One new hub page would close the gap

The fix recommended in the equity deep-dive — a single Indigenous-students landing page on students.unimelb that introduces Murrup Barak and deep-links out — is directly confirmed by the crawl. The content exists. It just needs a front door on the hub.

---

## Recommendations

1. **Create one Indigenous-students landing page on students.unimelb.** Introduce Murrup Barak, link to its key sections (study, financial support, student experience, contact). This closes the 19 vs 614 gap.

2. **Fix the www-twin.** 301 www.murrupbarak.unimelb.edu.au → murrupbarak.unimelb.edu.au.

3. **Wire every faculty's Indigenous content to this hub page.** The 17 domains linking Murrup Barak should point to the new hub landing page, which then routes to murrupbarak.

4. **Reduce chrome overhead.** 8 corporate links per page on a 37-page site is excessive.

---

*Built from: murrupbarak crawl (37 pages), links.json sampling (30 pages), index.json structural analysis, equity-indigenous-journey.md deep-dive. June 2026.*
