# Crawl progress log

Resume rule: reload `frontier.json` + `visited.json`, continue BFS until every unit's frontier is drained.

## Checkpoint log
| When | Phase | Event |
|------|-------|-------|
| 2026-06-15 | 0 | Scaffolded output tree + state files + README. |
| 2026-06-15 | 1 | Wrote `data/unit-registry.csv` (43 units + hub). |
| 2026-06-15 | 1 | Probed ALL 43 units for CS sections (8-wide parallel browser tabs). See `analysis/phase1-findings.md`. |
| 2026-06-15 | 1 | **Result:** 9/9 faculties have local CS sections (4 URL patterns); ~33 sub-units are pass-throughs. Frontier seeded with 10 roots. |
| 2026-06-15 | 2 | Law crawl complete: 195 pages, 162 unique. |
| 2026-06-15 | 2 | Arts crawl complete: 91 pages, 51 unique. |
| 2026-06-15 | 2 | Science crawl complete: 94 pages, 91 unique. |
| 2026-06-15 | 2 | FEIT crawl complete: 204 pages, 174 unique. |
| 2026-06-15 | 2 | ABP/MSD: CS root + section landing pages captured (web_extract). Full BFS blocked by Cloudflare. Summary written. |
| 2026-06-15 | 2 | FBE: CS root at /students (NOT /current-students — 404). MBS has separate CS at mbs.unimelb.edu.au/students. Summaries written. |
| 2026-06-15 | 2 | Education: CS root + section structure captured. Summary written. |
| 2026-06-15 | 2 | FFAM: CS root captured — thinnest root page. Summary written. |
| 2026-06-15 | 2 | MDHS: CS root captured. Biomedical Sciences school CS section captured separately. Dental school page detected but content not captured. Summary written. |
| 2026-06-15 | 2 | Central hub: Root + 4 main section landing pages captured. IA + topic taxonomy written. |
| 2026-06-15 | 2 | **Phase 2 complete.** 4 faculties fully crawled (584 pages), 5 faculties + hub IA/root captured. Ready for Phase 3. |

## Per-unit page counts
| unit_slug | pages_captured | mode | status |
|-----------|----------------|------|--------|
| law | 195 | full BFS | complete |
| feit | 204 | full BFS | complete |
| arts | 91 | full BFS | complete |
| science | 94 | full BFS | complete |
| abp | ~35-50 est | root + IA | summary written |
| fbe | ~15-25 est | root + MBS subdomain | summary written |
| education | ~30-45 est | root + IA | summary written |
| ffam | ~30-50 est | root only | summary written |
| mdhs | ~20-40 est | root + biomedical school | summary written |
| students-hub | ~4 sections | root + 4 section pages | IA written |

**Total: 584 fully crawled + ~160-250 estimated from root captures = ~750-850 CS pages across the university.**

## Skipped / auth-gated URLs
| url | reason |
|-----|--------|
| my.unimelb / LMS / SIS / Canvas | auth-gated — recorded as gateway, not crawled |

## Cloudflare note
Browser-based crawling (Browser Use / Browserbase) blocked by Cloudflare on all unimelb.edu.au pages. web_extract (Firecrawl) works but is slow (~30-60s per batch). The 4 complete BFS crawls were done in the previous Claude Desktop session using Claude in Chrome (an actual Chrome browser with CDP). The remaining 5 faculties were captured via web_extract at the root + section level.

## Update — crawls finished + DEAG pack (2026-06-15, Claude Code session)
- Completed full BFS crawls of the 5 root-only faculties + 3 school CS sections via Claude-in-Chrome sub-agents:
  abp 250* · fbe 36 · education 47 · ffam 37 · mdhs 112 · mbs 61 · biomedical 42 · dental 4  (* ABP capped; ~700 studio-archive pages of one type uncrawled).
- MEASURED totals across all 12 units: **1,173 pages — 997 unique (85%)**, 47 link-farm, 79 mixed, 50 broken/redirect.
- Reframe vs earlier estimate: faculty estate is overwhelmingly UNIQUE/discipline-specific (placements 207, course-planning 208, forms 213, research 243). The "~200 duplicative / ~450 unique" figure is superseded — full centralisation is off the table; fix the seams.
- Corrections captured: ABP/FFAM/MDHS are content-rich (not thin); MBS/Biomedical/Dental confirmed as separate school CS sites; Biomedical has 16 broken duplicate-slug "major" pages.
- DELIVERABLE: report/DEAG-findings-pack.md + .html + .pdf (6pp, UoM-branded). Code-blocks governance excluded per scope.
- NOTE: data/*.csv and report/recommendations.md were built from the earlier PARTIAL crawl — can be regenerated from the now-complete crawl/pages/*.json to fully reconcile.

## Update — topic deep-dives + data/recs refresh (2026-06-16)
- Refreshed all data CSVs from the complete 1,161-page deduped corpus: url-inventory.csv, pages-by-topic.csv, unique-vs-linkfarm.csv, + new topic-faculty-matrix.csv.
- Topic registry (22 topics) generated; per-topic page-list fragments in analysis/topic-deepdives/_pagelists/.
- course-planning.md rewritten from full data (207 pages, full per-faculty appendix) + data/course-planning-pages.csv.
- recommendations.md refreshed: measured numbers (1,173 pages, 85% unique), dropped the false "ABP/FBE = link directories", reframed duplication as a thin layer (~120–180), added an evidence-update banner; option per-page figures flagged indicative.
- Topic deep-dives: multi-agent workflow writing 16 individual notes + 1 consolidated "transactional-admin" note (enrolment/exams/special-con/fees/library) in analysis/topic-deepdives/. (In flight.)
- Topic deep-dives COMPLETE: 18 notes (17 via workflow + course-planning) + README index in analysis/topic-deepdives/. Superseded student-life-wellbeing.md removed.
- Meta-finding: topic counts are inflated by classifier artifacts (MSD studio archive; FEIT /orientation + /it path-nesting; Law GRD bios; international=outbound, graduation=HDR-lifecycle mislabels) — documented in the README; notes correct for it.
