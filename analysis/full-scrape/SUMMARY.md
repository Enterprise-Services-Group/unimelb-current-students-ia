# Full-scrape link-graph — headline facts

- **21,250 content pages** across 20 UoM domains; 862,489 total outbound links, **261,652 contextual** (chrome stripped).
- **598** global-nav/footer link patterns stripped as chrome.
- **Orphans:** 289 content pages have ZERO contextual inbound links (reachable only via nav/search).
- **Duplicate content:** 0 fingerprints on >1 URL; 0 span >1 domain.

## Orphan pages by domain (findability risk)

| Domain | Orphans | Pages | % |
|---|--:|--:|--:|
| medicine.unimelb.edu.au | 1 | 2182 | 0% |
| arts.unimelb.edu.au | 0 | 2017 | 0% |
| law.unimelb.edu.au | 2 | 1971 | 0% |
| handbook.unimelb.edu.au | 266 | 1920 | 14% |
| study.unimelb.edu.au | 0 | 1819 | 0% |
| fbe.unimelb.edu.au | 1 | 1756 | 0% |
| eng.unimelb.edu.au | 0 | 1663 | 0% |
| msd.unimelb.edu.au | 0 | 1543 | 0% |
| biomedicalsciences.unimelb.edu.au | 1 | 1529 | 0% |
| finearts-music.unimelb.edu.au | 9 | 1123 | 1% |
| education.unimelb.edu.au | 0 | 788 | 0% |
| mdhs.unimelb.edu.au | 6 | 776 | 1% |
| students.unimelb.edu.au | 1 | 679 | 0% |
| research.unimelb.edu.au | 0 | 650 | 0% |
| dental.unimelb.edu.au | 0 | 201 | 0% |
| services.unimelb.edu.au | 0 | 169 | 0% |
| science.unimelb.edu.au | 0 | 143 | 0% |
| www.unimelb.edu.au | 2 | 133 | 2% |
| scholarships.unimelb.edu.au | 0 | 111 | 0% |
| mbs.unimelb.edu.au | 0 | 77 | 0% |

## Top contextual cross-site flows

| From | To | Contextual links |
|---|---|--:|
| msd.unimelb.edu.au | students.unimelb.edu.au | 8069 |
| study.unimelb.edu.au | handbook.unimelb.edu.au | 4391 |
| handbook.unimelb.edu.au | www.unimelb.edu.au | 2964 |
| arts.unimelb.edu.au | findanexpert.unimelb.edu.au | 2845 |
| handbook.unimelb.edu.au | about.unimelb.edu.au | 2479 |
| education.unimelb.edu.au | gradresearch.unimelb.edu.au | 1972 |
| mdhs.unimelb.edu.au | gradresearch.unimelb.edu.au | 1882 |
| medicine.unimelb.edu.au | findanexpert.unimelb.edu.au | 1806 |
| msd.unimelb.edu.au | www.unimelb.edu.au | 1772 |
| study.unimelb.edu.au | forms.your.unimelb.edu.au | 1493 |
| biomedicalsciences.unimelb.edu.au | findanexpert.unimelb.edu.au | 1479 |
| msd.unimelb.edu.au | services.unimelb.edu.au | 1228 |
| handbook.unimelb.edu.au | students.unimelb.edu.au | 1193 |
| law.unimelb.edu.au | handbook.unimelb.edu.au | 1147 |
| medicine.unimelb.edu.au | mdhs.unimelb.edu.au | 1058 |
| biomedicalsciences.unimelb.edu.au | mdhs.unimelb.edu.au | 971 |
| msd.unimelb.edu.au | study.unimelb.edu.au | 928 |
| eng.unimelb.edu.au | findanexpert.unimelb.edu.au | 847 |
| eng.unimelb.edu.au | staff.unimelb.edu.au | 838 |
| eng.unimelb.edu.au | giving.unimelb.edu.au | 835 |
| msd.unimelb.edu.au | research.unimelb.edu.au | 834 |
| research.unimelb.edu.au | pursuit.unimelb.edu.au | 817 |
| research.unimelb.edu.au | findanexpert.unimelb.edu.au | 780 |
| msd.unimelb.edu.au | handbook.unimelb.edu.au | 778 |
| msd.unimelb.edu.au | staff.unimelb.edu.au | 729 |

## Complementary cuts (built alongside the workflow)
- **Dead/404 pages: 499 across 16 domains** (`dead-pages.csv`) — biomedical 153, msd 74, fbe 72, mdhs 53, medicine 51. ~10× the deck's "~50 broken". A concrete link-integrity/governance fix.
- **Thin pages (<8KB HTML): 1,530** (`thin-content.csv`) — 1,456 are handbook subject stubs (expected for a DB site); the rest are faculty thin pages.
- **Template-clone titles: 275** (`template-clones.csv`) — "contact us" on 15 domains, "research" 11, "news" 8, "people" 6, "home" 9 → parallel reinvention of standard sections at estate scale. ("find a scholarship" 2,042 pages = faceted-search bloat; "search"/"page not found" are crawl/error artifacts, not content.)
- **Navigation depth wildly inconsistent** (`nav-depth.csv`) — study.unimelb 58% of pages ≥5 levels deep, medicine 59%, msd 65%; vs handbook/scholarships flat (DB-style). Student content is buried deep on the marketing-led domains.
- **Alumni handoff (corrected):** ~97 CONTEXTUAL inbound links estate-wide after stripping global-nav chrome → alumni is nav-only, no in-content handoff. The deck's "0 links" was wrong (wrong host + host-level data).
