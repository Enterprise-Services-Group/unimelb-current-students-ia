# alumni.unimelb.edu.au (redirects to www.unimelb.edu.au/alumni) — Site Analysis

- **Unit:** alumni-unimelb
- **Actual URL:** `https://www.unimelb.edu.au/alumni` (redirects from `alumni.unimelb.edu.au`)
- **Pages captured:** 116
- **Max IA depth:** 5
- **Classification:** 112 unique, 4 link-farm
- **Crawled:** 2026-06-20

---

## Overview: What This Site Is

`alumni.unimelb.edu.au` is the University's alumni engagement portal, formally housed at `www.unimelb.edu.au/alumni`. It serves a community of 500,000+ graduates across 180 countries. Its five primary functions are:

1. **Community connection** — chapters, groups, events, news stories (most-trafficked section)
2. **Career support** — career tools, mentoring programs, online journals, professional development courses
3. **Benefits** — exclusive discounts covering lifestyle, university access, professional development
4. **Giving back** — donations, scholarships, volunteering, mentoring students
5. **University impact** — partnership with faculties to recruit students, support mentoring programs

The alumni site is content-rich (96% of pages classify as "unique" rather than link-farms), with a significant story-telling layer: over 25 named alumni career profiles and news features form the backbone of the `/stay-connected/news-and-stories` section.

---

## Scale and Depth

| Metric | Value |
|---|---|
| Pages captured | 116 |
| Unique content pages | 112 (97%) |
| Thin/link-farm pages | 4 |
| Max IA depth | 5 |
| Depth 0–1 | 6 pages |
| Depth 2 | 16 pages |
| Depth 3 | 69 pages (primary content layer) |
| Depth 4–5 | 25 pages |

The bulk of content lives at depth 3, which is notably deep for a pure marketing/engagement site. This reflects the elaborated mentoring structure (per-faculty mentoring pages) and the Alumni Council member bios (13 individual member pages).

---

## Topic Breakdown

| Topic tag | Page count | Notes |
|---|---|---|
| alumni-community | 116 | All pages — universal baseline tag |
| careers-employability | 38 | **Heaviest overlap zone with current students** |
| student-life | 21 | Community/network language overlaps with students.unimelb framing |
| alumni-benefits | 20 | Unique to alumni (lifestyle discounts, email, library, sports) |
| international | 20 | Global chapters, India network, international student stories |
| alumni-careers-mentoring | 20 | Mentoring programs (faculty-specific) |
| graduation | 18 | Alumni identity framing — "you've graduated, here's what's next" |
| wellbeing-health | 17 | Overlaps with current-student wellbeing language |
| contacts-support | 7 | Contact us, support pages |
| clubs-events | 4 | Alumni events, reunions |
| alumni-giving | 1 | Donate page — low prominence |
| scholarships | 1 | Give-back/scholarships page |

---

## Section IA Structure

```
/alumni                           ← Home (community hub)
  /support-resources              ← Career support, contact, welcome-new-alumni
  /benefits                       ← Benefits hub
    /professional-development     ← Online journals, language, career tools, PD courses
    /lifestyle                    ← Arts, travel, dining, health, financial
    /university-access            ← Library, sports centre, alumni email
  /stay-connected                 ← News, events, groups, council, awards
    /news-and-stories             ← ~15+ career story articles
    /find-an-event
    /find-a-group                 ← Alumni chapters, India/Indonesia networks
    /global-community             ← Notable alumni, chapters by region
    /alumni-council               ← 13+ member bios
    /alumni-awards                ← 2020–2024 winners + nomination
  /get-involved                   ← Volunteer, mentoring, give-back
    /volunteer/mentoring          ← Faculty-specific mentoring programs
    /give-back                    ← Donate, scholarships
  /impact                         ← Partner with university, recruit students
    /become-a-mentor
    /partner-with-the-university  ← Per-faculty partnership pages
    /students                     ← Thiri mentoring story
    /volunteering
```

---

## Cross-Site Overlap Findings

The alumni site shares topic territory with the current-student estate (`students.unimelb.edu.au`) in five zones:

### 1. Careers (38 pages — largest overlap)
Career support is the single largest theme on the alumni site after baseline community identity. The alumni careers section mirrors the structure of the central Careers hub:
- `/alumni/support-resources/career-support` and `/career-support/career-tools` mirror `students.unimelb.edu.au/careers`
- `/alumni/benefits/professional-development/career-tools` (separate from `/support-resources/career-support/career-tools`) creates an internal duplication
- Career story articles frame alumni as career success narratives — an aspirational register that current students can also consume (and likely are directed to from careers pages)
- Faculty-specific mentoring programs exist under `/get-involved/volunteer/mentoring/faculty-specific-mentoring/` for every faculty — identical scope to what Careers hub recommends for career mentoring

### 2. Community / Student Life (21 pages)
The alumni site uses "community," "network," "peer," and "connect" language extensively — the same vocabulary used on `students.unimelb.edu.au` for student groups and clubs. The boundary is temporal (student = current; alumni = former), but it is **not spatially distinct**: a prospective student browsing alumni community pages would encounter nearly identical community-framing language to what they'd see on the current-students site.

### 3. Events (4 pages)
Alumni events (`/stay-connected/find-an-event`) and current-student events (via the Union, student services, faculty pages) share calendar infrastructure but diverge in audience. However, some events (lectures, panel discussions, networking) are open to both — the sites do not cross-link.

### 4. Wellbeing and Health (17 pages)
`/alumni/benefits/lifestyle/health` and `/benefits/lifestyle/health/health-and-wellbeing-resources` echo the wellbeing framing on students.unimelb. The content is different (alumni health discounts vs student counselling), but the navigation label and page register are similar enough to create confusion for recently-graduated students seeking continuity of support.

### 5. Graduation (18 pages)
Pages tagged "graduation" on the alumni site almost universally frame graduation as the entry point into alumni identity ("you've graduated — here's your community"). This is the transition zone. But there is no explicit handoff link from the current-student graduation pages to the alumni site.

---

## Content Unique to Alumni

Distinct to alumni.unimelb with no equivalent on the current-student estate:

- **Alumni benefits package** — lifestyle discounts, alumni email for life, sports centre rates, library access for life
- **Alumni-specific giving** — donate to UoM, named scholarships, bequest
- **Global chapter network** — 30+ chapters organised by region (Australia, Asia, UK/Europe, Americas, Africa/ME)
- **Alumni awards** — Global Alumni Awards (2020–2024 winners + nomination form)
- **Alumni Council** — 13+ elected member bios and governance representation
- **Notable alumni showcase** — public figures and sector leaders across industries
- **Partner-with-university** — faculty-by-faculty employer partnership / student recruitment pages (unique role that alumni play in university ecology)
- **Alumni mentoring program as mentor** — alumni mentoring students (role reversal from student-seeking-mentor)

---

## Lifecycle Handoff: Graduating Students Entering the Alumni Estate

The alumni site's welcome page (`/alumni/support-resources/welcome-new-alumni`, 1,745 words — the most word-dense page after the India Alumni Network) addresses new graduates directly. It is the clearest handoff page on the site. But the question is whether the path to it is signposted from the current-student side.

### What exists:
- `/alumni/support-resources/welcome-new-alumni` is a rich onboarding page for new alumni
- The homepage (`/alumni`) links to "Welcome new alumni" as one of five top CTAs

### What is missing:
- No evidence of outbound links from the current-student graduation pages to the alumni site
- The `outboundHosts` analysis shows zero links back to `students.unimelb.edu.au` from alumni pages (and vice versa in the crawled data)
- The alumni site does not explain what happens to a student's MyUnimelb account, LMS access, or email alias after graduation — it only states the alumni email is preserved
- There is no "are you a new grad?" redirect or modal on the alumni homepage

### Verdict on lifecycle signposting:
**Weak.** The alumni site assumes the visitor has already found it. The graduating student experience relies on the student knowing to look for `alumni.unimelb.edu.au` (which itself redirects). The transition from current-student estate to alumni estate is implicit, not guided.

---

## Verdict: Distinct Identity or Bleed?

**Partially distinct, with significant bleed in the careers and community zones.**

The alumni site has a coherent identity in its giving, benefits, and council/awards sections — these are genuinely alumni-only. But its career support and community connection language is functionally identical to current-student language, and the two estates do not cross-link. This creates two problems:

1. **For recent graduates:** Career support resources feel duplicated (alumni careers tools vs. central Careers hub), and it is unclear which to use and when.
2. **For the University's IA:** Career content is being authored independently in three places — the central Careers hub, faculty-level careers pages, and the alumni careers section — with no shared vocabulary, no cross-referencing, and no explicit sequencing for users moving through their career lifecycle.

The alumni site works well as a community and benefits portal. It works less well as a career continuity service, because it does not connect to the student-facing career infrastructure it is meant to extend.
