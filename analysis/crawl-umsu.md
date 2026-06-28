# umsu.unimelb.edu.au — Crawl Analysis

*The University of Melbourne Student Union — 800 pages, the second-largest new domain crawled. Independent organization, not UoM CMS. 266 pages are clubs directory. Median 720KB — extraordinarily heavy. Very insular: almost no outbound links to the rest of the unimelb estate. June 2026.*

---

## What we found

UMSU is the independent student union — not part of the University's CMS, not governed by the same web standards. At 800 pages, it's the second-largest new domain (after sport at 444). But it's structurally and operationally separate from the rest of the student estate.

### Structure

| Section | Pages | Content |
|---|---|---|
| `/buddy-up/clubs` | 266 | Clubs directory — by far the largest section |
| `/make-difference/eduacademic` | 67 | Education & academic advocacy |
| `/support/advocacy` | 50 | Student advocacy services |
| `/express-yourself/theatre` | 35 | Theatre & arts |
| `/guide/article` | 33 | Guide articles |
| `/about/secretariat` | 19 | Governance & secretariat |
| `/express-yourself/gallery` | 17 | Photo galleries |
| `/support/welfare` | 14 | Welfare support |
| Other | 299 | Remaining sections |

The IA reflects a student union: clubs, advocacy, arts, welfare, governance. This is not a University service site — it's a student-run organization.

### Content profile

- 266 pages are clubs directory — 33% of the site
- "Login" appears as a top title pattern (10 pages) — suggesting authenticated areas
- Topics: People of Colour, Safe Student Activism, Elections, Academic Misconduct — distinctly student-union content
- 492 of 800 pages have non-empty titles — 308 have empty or generic titles

### Link analysis — extremely insular

| Outbound destination | Links in 19-page sample |
|---|---|
| intl.umsu.unimelb.edu.au | 4 |
| students.unimelb.edu.au | 3 |
| q.surveys.unimelb.edu.au | 1 |

**Only 8 outbound unimelb links across 19 sampled pages.** UMSU is remarkably insular — it barely links to the student hub, library, or any other University service. This is likely by design (independent organization) but means a student on UMSU has almost no path back to the University estate.

### Page weight — catastrophically heavy

| Metric | Value |
|---|---|
| Median | **720KB** |
| Max | **6,365KB (6.4MB)** |
| Min | 114KB |

These are the heaviest pages in the entire estate. The 6.4MB max is the single largest page we've encountered. UMSU is not on the University's CMS and has no page-weight governance.

---

## What this means

### 1. UMSU is a parallel student universe

Clubs, advocacy, welfare, events — UMSU provides a complete parallel student experience. A student who finds UMSU first may never discover the University's own services. The insular linking means there's no path from UMSU to the hub.

### 2. UMSU is the dark matter of the student web estate

800 pages, 6.4MB max, minimal outbound links — UMSU is large, heavy, and disconnected. It's not causing problems for the University estate because it barely interacts with it. But it's a missed opportunity: UMSU reaches students the University doesn't.

### 3. Page weight is a governance gap

The University has no control over UMSU's web standards, but 6.4MB pages harm students on mobile/limited-data connections. This is worth flagging even if the University can't directly fix it.

### 4. UMSU outbound to hub is near-zero

Only 3 links to students.unimelb in 19 pages. Adding even a handful of cross-links (UMSU advocacy → hub special consideration, UMSU welfare → hub financial hardship) would connect two parallel student experiences.

---

## Recommendations

1. **Flag UMSU page weight to the student union.** 720KB median, 6.4MB max — these are accessibility and equity issues even if outside University governance.

2. **Propose cross-links from UMSU to hub services.** UMSU advocacy → special consideration. UMSU welfare → financial hardship. UMSU clubs → student life. Mutual benefit: UMSU routes students to University services; the hub routes students to the union.

3. **Add UMSU to the student hub's "Student life" section.** The hub currently sends 49 links to UMSU. This connection exists and should be strengthened.

---

*Built from: umsu crawl (800 pages), links.json sampling (19 pages), index.json structural analysis. June 2026.*
