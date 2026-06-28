# Resume Instructions — Full Domain Crawl Batch

**Status as of 2026-06-27:** Batch COMPLETE. **All 20 units crawled to
`frontierRemaining: 0`.** The final loose end — `handbook.unimelb.edu.au`'s 1,169-URL
tail (mostly `/2026/subjects/<code>` catalog pages) — was drained with the page cap
raised 3000 → 5000, finishing at **4,169 pages**. Nothing left to crawl.

Source of truth for per-unit state is each `crawl/<dir>/index.json`
(`pagesCrawled`, `frontierRemaining`) — not the old batch state. See
`state/frontier.json` for the reconciled snapshot.

## Totals (measured from index.json files)

- **37,162 pages** crawled across 20 real units (27,302 `page.html` files on disk, 5.0 GB).
- 19 units complete (`frontierRemaining: 0`); handbook draining its last tail.
- `crawl/unimelb-edu-au/` is an empty redirect stub (apex → www.); ignore it.

## Completed units (frontierRemaining = 0)

| Unit dir | Domain | Pages |
|----------|--------|------:|
| mdhs-unimelb-edu-au | mdhs.unimelb.edu.au | 6,072 |
| study-unimelb-edu-au | study.unimelb.edu.au | 4,048 |
| medicine-unimelb-edu-au | medicine.unimelb.edu.au | 3,213 |
| law-unimelb-edu-au | law.unimelb.edu.au | 3,188 |
| arts-unimelb-edu-au | arts.unimelb.edu.au | 2,446 |
| msd-unimelb-edu-au | msd.unimelb.edu.au | 2,348 |
| fbe-unimelb-edu-au | fbe.unimelb.edu.au | 2,241 |
| scholarships-unimelb-edu-au | scholarships.unimelb.edu.au | 2,226 |
| eng-unimelb-edu-au | eng.unimelb.edu.au | 1,985 |
| biomedicalsciences-unimelb-edu-au | biomedicalsciences.unimelb.edu.au | 1,584 |
| finearts-music-unimelb-edu-au | finearts-music.unimelb.edu.au | 1,444 |
| education-unimelb-edu-au | education.unimelb.edu.au | 852 |
| students-full | students.unimelb.edu.au | 833 |
| research-full | research.unimelb.edu.au | 662 |
| science-unimelb-edu-au | science.unimelb.edu.au | 420 |
| dental-unimelb-edu-au | dental.unimelb.edu.au | 204 |
| services-unimelb-edu-au | services.unimelb.edu.au | 176 |
| www-unimelb-edu-au-alumni | www.unimelb.edu.au/alumni | 137 |
| mbs-unimelb-edu-au | mbs.unimelb.edu.au | 83 |

| handbook-unimelb-edu-au | handbook.unimelb.edu.au | 4,169 |

**Totals: 38,331 pages across 20 units; 27,348 `page.html` files on disk (5.0 GB).**
No unit has a non-empty frontier.

## Resume / re-run a single unit

The batch runner (`node crawl/crawl_batch.js`) skips any unit whose `index.json`
has an empty frontier, so re-running it only touches handbook. To resume handbook
directly with a raised cap:

```bash
cd ~/Documents/Claude/projects/unimelb-current-students-ia
node crawl/crawl_domain.js handbook.unimelb.edu.au \
  crawl/handbook-unimelb-edu-au 5000
```

`crawl_domain.js` reloads the frontier + visited set from `index.json`, so it
picks up exactly where it left off and checkpoints every 50 pages.

## Notes

- Chrome is launched by `crawl_domain.js` itself (Playwright `launchPersistentContext`
  on the `~/.hermes/chrome-profile` profile) — this is what bypasses Cloudflare.
- The handbook frontier is reference catalog (individual subject pages), not
  student-journey/IA content. Downstream analysis treats the Handbook as an
  external *link target* (3,380 inbound links from current-student pages), not a
  corpus to mirror — so 3,000 pages already over-covers the analytical need;
  draining the rest is for completeness only.
