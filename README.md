# University of Melbourne — "Current Students" IA Audit & Unification Strategy

An evidence-based audit of how current-students content is fragmented across the
University of Melbourne's **central hub** (`students.unimelb.edu.au`) and the
**academic-unit sites** (9 faculties + ~35 schools / departments / institutes /
centres, plus any nested program subdomains), and a strategy to unify it.

Plan: `~/.claude/plans/plan-using-the-links-lazy-naur.md`

## Why this exists
Faculty/school sites each run their own "Current Students" sections. Some hold
genuinely unique content (placements, course-planning advice, local services);
many are **"link farms"** that just redirect to the central hub. The result is an
inconsistent, duplicated, gap-ridden student experience. This project inventories
all of it, classifies it, and recommends how to unify it.

## How the data is produced (important constraints)
- `WebFetch` is **WAF-blocked (403)** and Apify is **over its monthly limit**, so
  **all pages are fetched through Claude-in-Chrome** (the user's connected browser).
  Crawling is therefore **sequential** and **resumable across sessions**.
- The crawl writes a **local corpus** (`crawl/`); the multi-agent analysis reads
  those files, never the live site.
- Public pages only. Anything behind student login (`my.unimelb`, LMS/Canvas, SIS)
  is recorded as a gateway, not crawled.

## Folder structure
```
state/    frontier.json · visited.json · progress.md   (resume point)
crawl/    pages.jsonl · raw/<sha1>.txt                  (captured corpus)
data/     url-inventory.csv · unit-registry.csv · top-ia.json ·
          current-students-ia.json · pages-by-topic.csv ·
          unique-vs-linkfarm.csv · students-unimelb-ia.json
analysis/ unit-<slug>.md · service-model-matrix.* · topic-deepdives/*
report/   recommendations.md · report.html → report.pdf
deck/     unimelb-cs-ia.pptx
```

## `pages.jsonl` record
`url, normalizedUrl, unitName, unitLevel(faculty|school|department|institute|centre|program),
faculty, subdomain, domain, section, breadcrumb[], title, depth, navItems[],
wordCountUnique, outboundLinks[{text,href}], destinationsSummary{host:count},
classification(unique|link-farm|mixed|redirect), topicTags[], rawTextFile, capturedAt`

## Classification taxonomy
- **link-farm/hub** — mostly outbound links (esp. → `students.unimelb.edu.au`), low unique prose (≲150 words).
- **unique** — substantive content not on the hub (placements, discipline advice, local forms/contacts).
- **mixed** — some unique content + significant redirection.
- **redirect** — pass-through (meta-refresh / "go to students.unimelb").

## Resuming the crawl
State lives in `state/`. To continue: reload `frontier.json` + `visited.json`,
keep BFS-ing until each unit's frontier is drained. See `state/progress.md` for
the live checkpoint log and per-unit counts.

## Status
Phase 0 (scaffold) ✔ · Phase 1 (unit registry + CS probe) in progress.

## Published Reports
The HTML reports for this project are published via GitHub Pages:
- [Current Student Journey Map](https://redesigned-spork-92nvp2n.pages.github.io/journey/current-student-journey-map.html)
- [Course Planning & Enrolment Journey Map](https://redesigned-spork-92nvp2n.pages.github.io/journey/course-planning-enrolment-journey-map.html)
- [DEAG Findings Pack](https://redesigned-spork-92nvp2n.pages.github.io/report/DEAG-findings-pack.html)
- [Recommendations](https://redesigned-spork-92nvp2n.pages.github.io/report/Recommendations.html)
- [Topic Deep Dives](https://redesigned-spork-92nvp2n.pages.github.io/report/Topic-Deep-Dives.html)
- [Main Report](https://redesigned-spork-92nvp2n.pages.github.io/report/report.html)
- [Presentation Deck](https://redesigned-spork-92nvp2n.pages.github.io/deck/unimelb-cs-ia-deck.html)
