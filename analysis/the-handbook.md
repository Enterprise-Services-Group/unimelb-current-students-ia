# The Handbook — Deep-Dive

*The biggest single dependency in the University's web estate, and the one governed to the lowest web standard. 7,819 contextual inbound links from across 15+ domains — more than any other system — but SPA-only with no server-rendered fallback, blank titles on every page, and no "enrol" action. June 2026.*

---

## Executive summary

The Handbook (handbook.unimelb.edu.au) is the system that defines course structure, subject prerequisites, points, and entry requirements for every degree the University offers. It is the **#1 dependency in the estate**:

- **7,819 contextual inbound links** from 15+ domains — more than my.unimelb (187), ask.unimelb (396), or Careers Online (115) combined
- **8,323 outbound links** — the Handbook is the estate's second-most prolific linker after study.unimelb
- Referenced on **~830 hub enrolment pages** (195 direct links from the course-planning toolchain alone)
- **2,134 pages** — 161 subjects, 105 courses, plus structure and search pages

But the Handbook is governed to a visibly lower web standard than the rest of the estate. It's built on a different platform, operates as a single-page application with **no server-rendered fallback**, has **blank `<title>` tags on every subject and course page**, carries **non-descriptive anchor text** at scale, and provides **no "Enrol in this subject" action** — the single most important task a student would want to perform from a subject page. For ~1,470 of 2,134 crawled captures, the page delivered to the crawler is an 887-byte Imperva bot-block shell — meaning search engines, social-media link previews, and non-JS users see nothing at all.

The fix is not a rebuild. It's SSR, metadata templates, browsable indexes, and one enrol action per subject page. Get this right and the entire estate's planning toolchain — the 7-system obstacle course Jordan and Sam navigate — gets its foundation.

---

## The Handbook by the numbers

| Metric | Value |
|---|---|
| Total pages | 2,134 (crawled) |
| Genuine content pages | ~664 (after filtering ~1,470 bot-block shells) |
| Subjects | 161 (orphaned — no inbound links) |
| Courses | 105 (orphaned — no inbound links) |
| Contextual inbound links (estate-wide) | **7,819** |
| Contextual outbound links | **8,323** |
| Median page weight | 0KB (bot-block artifact) |
| Max page weight | 180KB |
| Blank `<title>` tags | All subject/course pages |

---

## The inbound dependency: who relies on the Handbook

| Source | Contextual links | What for |
|---|---|---|
| study.unimelb.edu.au | **4,391** | Course discovery — every /find/courses/ page links handbook for structure, entry requirements, subjects |
| law.unimelb.edu.au | 1,147 | Law course/subject detail |
| msd.unimelb.edu.au | 778 | Architecture/building course structure |
| finearts-music.unimelb.edu.au | 374 | VCA/MCM course detail |
| arts.unimelb.edu.au | 315 | Arts course/subject detail |
| students.unimelb.edu.au | 179 | Hub enrolment guidance → handbook course structure |
| education.unimelb.edu.au | 146 | Education course detail |
| biomedicalsciences.unimelb.edu.au | 145 | Biomedical course structure |
| fbe.unimelb.edu.au | 131 | Business/economics course detail |
| medicine.unimelb.edu.au | 95 | Medicine course structure |
| eng.unimelb.edu.au | 60 | Engineering course detail |

The Handbook is the **single most-linked-to system after www.unimelb.edu.au and about.unimelb.edu.au** — and unlike those, it's the operational backbone. When a student clicks "course structure" on any faculty site, they land on the Handbook.

---

## The outbound dependency: where the Handbook sends students

| Destination | Contextual links | What for |
|---|---|---|
| www.unimelb.edu.au | 2,964 | Generic University links |
| about.unimelb.edu.au | 2,479 | Policy/administrative links |
| students.unimelb.edu.au | **1,193** | Current student hub — the most important destination |
| safety.unimelb.edu.au | 493 | Safety links (bulk chrome) |
| archive.handbook.unimelb.edu.au | 489 | Archive cross-links |
| study.unimelb.edu.au | 223 | Course discovery |
| forms.your.unimelb.edu.au | 48 | Enrolment variation forms |
| policy.unimelb.edu.au | 41 | University policy |
| ask.unimelb.edu.au | 25 | Legacy FAQ |

The Handbook sends 1,193 links to students.unimelb — the most important handoff. But those links are generic (bare URLs, "current students" labels). None say "Enrol in this subject."

---

## The three failures

### 1. SPA-only with no server-rendered fallback `[HIGH]`

The Handbook is a single-page application. When a search engine, social-media crawler, or non-JS user-agent requests a subject or course page, the server returns JavaScript that must be executed to render content. The Imperva WAF adds a second layer: ~1,470 of 2,134 crawled captures are 887-byte bot-block shells — the WAF challenged the crawler and the crawler couldn't execute JS to pass the challenge.

The result:
- **Search engines see blank pages with no content.** Every handbook page is effectively invisible to Google.
- **Social media link previews show nothing.** Share a handbook subject link on Slack/Teams/LinkedIn — no title, no description, no image.
- **Screen readers and accessibility tools fail.** No server-rendered content = no accessible DOM.
- **266 pages are "orphans"** (161 subjects + 105 courses) — but this is an artifact of the bot-block. The pages exist; the crawler couldn't see who links to them.

### 2. Blank `<title>` on every subject and course page `[HIGH]`

Every subject page and course page in the Handbook has an empty or generic `<title>` tag. This is the single most impactful accessibility + SEO + findability failure in the estate by volume. When a student bookmarks a subject, the bookmark reads nothing. When they search their browser history, nothing appears. When Google indexes the page (if it can), the search result has no title.

### 3. No "Enrol in this subject" action `[HIGH]`

A student looking at a subject page in the Handbook wants to do one thing: enrol in it. The Handbook describes the subject — points, prerequisites, assessment, timetable — but provides **zero path to enrol**. The "describe but don't transact" pattern that defines the estate's worst faults is most acute here: the page a student lands on to decide *whether* to enrol has no way to *actually* enrol. §6.7 of the improvements register calls for exactly this action.

---

## Anchor text: non-descriptive at scale

The Handbook carries thousands of links, but anchor text is generic — "current students," "handbook," bare URLs. This is the #2 findability finding in §2.6. Every link from the Handbook to the student hub should say what it does: "Enrol in subjects," "Check census dates," "Manage your timetable." Instead they're chrome-level labels.

---

## The orphan problem — mostly an artifact

266 handbook pages appear as orphans (no inbound links). 161 are subjects, 105 are courses. But this is substantially a **crawl artifact**: the WAF blocked the crawler from seeing the full link graph. The pages are linked — just not visible through the bot-block. However, the artifact itself is the problem: if the crawler can't see inbound links, neither can Google.

---

## Recommendations

### 1. Add server-rendered fallback for every subject and course page `[HIGH · large]`
Implement SSR so every /subjects/* and /courses/* page delivers a complete HTML document with title, h1, meta description, prerequisite list, points, and assessment structure — before any JavaScript executes. This fixes search engine visibility, link previews, accessibility, and the bot-block problem in one change.

### 2. Give every subject and course page a descriptive `<title>` `[HIGH · medium]`
Template: "MULT10001 Introduction to Life Sciences — Handbook | University of Melbourne". One template change touches all 2,134 pages. The highest-impact accessibility + SEO fix in the estate.

### 3. Add one "Enrol in this subject → my.unimelb" action to every subject page `[HIGH · medium]`
The action students want, on the page they use to decide. One CTA, one destination (my.unimelb enrolment), one template change.

### 4. Build browsable indexes — stop being search-only `[HIGH · medium]`
Subjects and courses are currently discoverable only via the Handbook's internal search. Add browsable A-Z indexes, by-faculty listings, and by-level groupings. These are the pages that search engines and students can navigate.

### 5. Fix non-descriptive anchor text `[MEDIUM · medium]`
Replace generic link labels ("current students," "handbook") with action-oriented labels ("Enrol in subjects," "Check prerequisites," "View course structure").

### 6. Confirm the bot-block serves a real HTML fallback to legitimate non-JS user agents `[MEDIUM · medium]`
The Imperva challenge should not block screen readers, accessibility tools, or link-preview bots. Configure WAF to serve SSR'd content to known-good non-JS user agents.

---

## Linked improvements from the register

| § | Improvement | Severity · Effort |
|---|---|---|
| 2.2 | Surface live 2026 handbook subjects/courses via browsable indexes + give them a `<title>` | HIGH · medium |
| 5.3 | Bring the Handbook up to the estate's web-standards baseline | HIGH · medium |
| 6.6 | Treat handbook subject/course pages as JS-only — provide a server-rendered fallback | MEDIUM · large |
| 6.7 | Wire an "Enrol in this subject" action onto every handbook subject & course page | HIGH · medium |
| 2.6 | Fix non-descriptive anchor text on the Handbook | MEDIUM · quick-win |
| 5.7 | Annotate the handbook crawl artifact so a false "14% orphaned" doesn't reach the deck | LOW · quick-win |

---

*Built from: cross-site-flow.csv (7,819 inbound / 8,323 outbound links), orphans.csv (266 handbook orphans), page-weight.csv (0KB median = bot-block artifact), improvements-register.md (§2.2, §5.3, §6.6, §6.7, §2.6), and crawl/handbook/ (2,134 captures). June 2026.*
