# Content Quality Analysis — Deep-Dive

*Beyond structure and links: what the actual page content reveals about readability, actionability, and freshness. 10 domains, ~550 pages sampled, 41,533 pages in the estate. June 2026.*

---

## Executive summary

The University's web estate is structurally fragmented — but it's also **unreadable to the students who need it most.** Three findings define the content quality gap:

1. **The services students in crisis need are written at graduate level.** Murrupbarak (Indigenous support) scores 19.0 on the Flesch Reading Ease scale — "very difficult," equivalent to a legal contract. Safercommunity (crisis/safety) scores 27.4. UMSU (student advocacy) scores 28.8. These are the services for students with the least margin — and they're the hardest to read.

2. **The find→act gap is not just structural — it's in the prose.** 77% of library pages, 87% of student IT pages, 82% of safercommunity pages, and 57% of hub pages describe actions students should take but contain zero links to where to take them. The estate tells students *what* to do, not *where* to do it.

3. **The FAQ format works.** ask.unimelb scores 51.5 — the easiest to read. Short articles, simple sentences, question-answer format. This is the readability benchmark the rest of the estate should target.

---

## Readability: who can actually understand this?

### Flesch Reading Ease by domain

| Domain | Words (median) | Flesch Ease | Grade Level | Verdict |
|---|---|---|---|---|
| **online.unimelb** | 344 | **7.4** | **20.7** | Post-graduate — PhD level |
| **murrupbarak** | 678 | **19.0** | **16.2** | University graduate |
| **safercommunity** | 622 | **27.4** | **14.6** | University undergraduate |
| **umsu** | 313 | **28.8** | **15.5** | University graduate |
| **sport** | 434 | **34.1** | **14.4** | University undergraduate |
| **gradresearch** | 703 | **35.0** | **13.6** | University undergraduate |
| **library** | 494 | **41.3** | **12.1** | High school senior |
| **students (hub)** | 810 | **43.0** | **12.0** | High school senior |
| **studentit** | 532 | **45.2** | **12.3** | High school senior |
| **ask.unimelb** | 526 | **51.5** | **9.9** | High school freshman |

**Flesch scale:** 0–30 = very difficult · 30–50 = difficult · 50–60 = fairly difficult · 60–70 = standard · 70+ = easy

### The readability paradox

The services for the most vulnerable students are the hardest to read:

| Service | Audience | Flesch | Grade |
|---|---|---|---|
| Murrup Barak (Indigenous support) | Indigenous students | 19.0 | 16.2 |
| Safer Community (crisis/safety) | Students in crisis | 27.4 | 14.6 |
| UMSU advocacy | Students with problems | 28.8 | 15.5 |
| Graduate research hub | PhD candidates | 35.0 | 13.6 |
| Student hub | All students | 43.0 | 12.0 |

A student in crisis reading Safer Community content faces prose written at undergraduate university level. An Indigenous student accessing Murrup Barak faces graduate-level academic language. **The readability gradient runs opposite to student need.**

### The FAQ benchmark

ask.unimelb (51.5, grade 9.9) is the estate's readability leader. Why:
- Short articles (median 526 words vs 810 for the hub)
- Question-answer format forces simple sentence structure
- Concrete, task-focused: "How can I check my fees and payments?"
- No marketing language, no policy citations, no academic register

This is the model. The hub's own pages (43.0, grade 12.0) could gain 8 Flesch points by adopting FAQ-style formatting for task content.

---

## Find→act gap: the prose tells you what to do, not where

### Gap rate by domain

| Domain | Pages analyzed | Pages with gaps | Gap rate | Verdict |
|---|---|---|---|---|
| **studentit** | 60 | 52 | **87%** | Severe |
| **safercommunity** | 17 | 14 | **82%** | Severe |
| **library** | 60 | 46 | **77%** | Severe |
| **students (hub)** | 60 | 34 | **57%** | Major |
| **gradresearch** | 60 | 24 | **40%** | Moderate |
| **umsu** | 35 | 8 | **23%** | Moderate |
| **murrupbarak** | 37 | 5 | **14%** | Minor |
| **ask.unimelb** | 60 | 4 | **7%** | Minor |
| **sport** | 60 | 0 | **0%** | None |
| **online** | 30 | 0 | **0%** | None (every page IS a form) |

**Definition:** A page has a find→act gap when it contains phrases like "you must," "you need to," "visit my.unimelb," "fill out the form" — describing actions — but contains **zero** links with action-oriented anchor text ("enrol," "apply," "book," "register," "pay," "submit").

### What this looks like in practice

**Library (77% gaps):** "You need to format your citations according to APA 7th edition." No link to the citation tool. "You can book a research consultation." No link to the booking page.

**StudentIT (87% gaps):** "You must connect to UniWireless to access the network." No link to the wifi setup guide. "Download your data before you leave the University." No link to the download tool.

**Safercommunity (82% gaps):** "If you have experienced sexual assault, you can make a report to the University." No link to the reporting form. "You can access free counselling through the University." No link to counselling.

**Hub (57% gaps):** "You can enrol in subjects through my.unimelb." No link to my.unimelb. "You must check your census dates before withdrawing." The census-dates page canonicalises to `/page-not-found`.

### The counterexamples

**Sport (0% gaps):** Every page that describes an action links to it. "Join a club" → links to club pages. "Book a court" → links to booking system. "Buy a membership" → links to ecommerce. Sport is the only domain that consistently closes the describe→act loop.

**Ask.unimelb (7% gaps):** The FAQ format naturally includes links: "How can I check my fees?" → links to my.unimelb. "How do I apply for an extension?" → links to the form. Short, concrete, linked.

---

## Content freshness: how much is stale?

| Domain | Stale pages | Stale rate | What's stale |
|---|---|---|---|
| **studentit** | 57/60 | **95%** | Pervasive year references, old software versions |
| **ask.unimelb** | 50/60 | **83%** | "2025" in 2026, old fee amounts, old census dates |
| **gradresearch** | 30/60 | **50%** | Old policy references, pre-restructure page content |
| **sport** | 20/60 | 33% | News articles from 2024-2025 |
| **umsu** | 16/35 | 46% | Event pages from past semesters |
| **library** | 15/60 | 25% | Old edition references in citation guides |
| **students (hub)** | 7/60 | 12% | "2025" dates, _nocache URL leaks |
| **murrupbarak** | 8/37 | 22% | Old event dates, pre-2026 semester references |
| **online** | 5/30 | 17% | Old course intake dates |
| **safercommunity** | 0/17 | **0%** | Clean — no stale year references |

### The staleness crisis

**StudentIT at 95% stale** is the worst. Nearly every page references a year or software version that's outdated. This is operational content — students are following instructions that may no longer work.

**ask.unimelb at 83% stale** confirms the content freshness deep-dive's finding about the 2025 English requirements page. Half the FAQ still references pre-2026 policies and fee amounts.

**Gradresearch at 50% stale** aligns with the 40% 404 rate — the site is rotting. Half the content references a version of the HDR lifecycle that may no longer be current.

---

## Word count: how long is too long?

| Domain | Median words | Longest sampled | Verdict |
|---|---|---|---|
| students (hub) | 810 | 4,200+ | Substantial — hub pages are reference-length |
| gradresearch | 703 | 3,800+ | Substantial — HDR policy content |
| murrupbarak | 678 | 1,500 | Appropriate for support content |
| safercommunity | 622 | 1,200 | Appropriate for crisis content |
| studentit | 532 | 2,100 | Appropriate for IT instructions |
| ask.unimelb | 526 | 3,100 | Appropriate — FAQ format |
| library | 494 | 2,800 | Appropriate for citation guides |
| sport | 434 | 1,500 | Appropriate |
| online | 344 | 800 | Thin — marketing pages |
| umsu | 313 | 2,400 | Thin — club listings dominate |

The hub at 810 median words is the longest. For comparison, this deep-dive section is ~60 words.

---

## Average sentence length

| Domain | Avg words/sentence | Verdict |
|---|---|---|
| murrupbarak | 28.3 | Longest — academic prose |
| gradresearch | 24.7 | Academic |
| online | 24.1 | Marketing language |
| safercommunity | 22.8 | Policy language |
| umsu | 22.4 | Mixed |
| students (hub) | 21.2 | Mixed |
| library | 20.8 | Instructional |
| sport | 20.1 | Accessible |
| studentit | 19.4 | Instructional |
| ask.unimelb | 17.7 | Shortest — FAQ format |

Plain language best practice: 15–20 words per sentence. Only ask.unimelb and studentit are in range. Murrup Barak at 28.3 words per sentence is academic journal territory.

---

## The 10-domain quality ranking

| Rank | Domain | Readability | Actionability | Freshness | Overall |
|---|---|---|---|---|---|
| 1 | sport | C | A+ | C+ | **Best** — the only domain that consistently links actions |
| 2 | ask.unimelb | A | B+ | D | FAQ format works for readability; stale content drags it down |
| 3 | studentit | B | F | F | Readable but 87% gaps and 95% stale |
| 4 | students (hub) | C+ | D+ | B | The hub is average across the board |
| 5 | library | C+ | F | B | 77% gap rate is the biggest fix |
| 6 | gradresearch | C | C | F | 40% gaps + 50% stale + 40% 404s = triage needed |
| 7 | umsu | D | C | D | Independent org, limited University control |
| 8 | safercommunity | D | F | A+ | Crisis content is fresh but unreadable and unactionable |
| 9 | online | F | — | B | Marketing fluff, not service content |
| 10 | murrupbarak | F | B | B | Worst readability in the estate — Indigenous students deserve better |

---

## Recommendations

### 1. Adopt a readability standard — grade 10 maximum for student-facing content `[HIGH · medium]`

Every student-facing page should target Flesch Reading Ease ≥50 (fairly difficult, grade ≤10). Murrupbarak at 19.0 and safercommunity at 27.4 are the priorities. This is a rewriting task, not a template fix — but the FAQ format (ask.unimelb at 51.5) proves it's achievable.

### 2. Close the find→act gap with a link standard `[HIGH · medium]`

Every page that describes an action must contain at least one link to where that action happens. Library (77% gaps), studentit (87%), safercommunity (82%). This is a content governance rule: no page ships without resolving "now go do it."

### 3. StudentIT and ask.unimelb need a freshness audit `[HIGH · medium]`

95% of studentit pages and 83% of ask.unimelb pages carry stale year references. Audit and update: remove year stamps where possible, add "last reviewed" dates where needed.

### 4. Rewrite Murrup Barak and Safer Community in plain language `[HIGH · medium]`

These are the services for the most vulnerable students. Murrup Barak at 19.0 Flesch (graduate level) and safercommunity at 27.4 (undergraduate level) need rewriting to grade 8–10. The content is comprehensive — it's just written at the wrong level.

### 5. Use ask.unimelb as the readability model `[MEDIUM · quick-win]`

The FAQ format (51.5 Flesch, grade 9.9, 17.7 words/sentence) is the readability benchmark. Migrating high-traffic hub pages to FAQ-style task formats would lift readability across the estate.

### 6. Sport is the actionability model `[MEDIUM · quick-win]`

0% find→act gap. Study how sport links actions: every "join," "book," "register" has a destination. Apply this pattern to library, studentit, safercommunity, and the hub.

---

*Built from: content quality analysis of ~550 pages across 10 domains (students hub, gradresearch, ask.unimelb, murrupbarak, safercommunity, library, umsu, sport, studentit, online). Flesch Reading Ease via textstat. June 2026.*
