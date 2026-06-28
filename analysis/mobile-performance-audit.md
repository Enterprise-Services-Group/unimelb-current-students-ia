# Mobile & Performance Audit — Deep-Dive

*The heaviest pages in the estate hit the audiences on the most constrained connections. Median page weight is 149–304KB, but max values explode to 1.1–5.0MB within single domains — a 4×–30× gap proving nothing flags a page when it balloons. June 2026.*

---

## Executive summary

Performance at the University of Melbourne is not a technical footnote — it's an equity issue. The study.unimelb course-discovery pages (304KB median) are the heaviest in the estate and the primary surface for international applicants, who access them on offshore mobile connections. The international agent page is ~245KB. The CoE page is ~264KB. Every compliance-critical step in the international journey happens on the heaviest pages.

The problems are not architectural — they're **CMS side-effects** that no editor intended:
- 9 pages shipping >100KB of base64-inlined images (one page: 2,071KB as a single base64 photo)
- 4 law staff profiles at 5MB each — 1,926 identical Cookiebot icon copies per page
- A 106KB icon sprite inlined in every course page, though most icons are never shown
- 18 blocking scripts on course pages with 0% defer/async
- 3 separate font hosts adding DNS+TLS+FOIT cost

The fix is governance, not redesign: a page-weight budget, a CMS publish-time guard against base64 inlining, and one Cookiebot config change that drops 4 law pages from ~5MB to under 200KB instantly.

---

## The weight table

| Domain | Pages | Median KB | P90 KB | Max KB | Primary audience | Audience connection quality |
|---|---|---|---|---|---|---|
| **study.unimelb** | 2,005 | **304** | 416 | 1,132 | International applicants | Offshore mobile — worst |
| finearts-music | 1,257 | 217 | 248 | 2,292 | Mixed | Domestic broadband |
| scholarships | 2,151 | 188 | 190 | 199 | Mixed | Mixed |
| students.unimelb | 833 | 181 | 217 | 1,102 | Enrolled students | Domestic + on-campus |
| fbe | 1,980 | 166 | 188 | 1,415 | Mixed | Mixed |
| medicine | 2,194 | 164 | 184 | 2,516 | Mixed | Mixed |
| msd | 1,560 | 163 | 182 | 1,779 | Mixed | Mixed |
| law | 2,034 | 161 | 178 | **5,056** | Mixed | Mixed |
| eng | 1,759 | 160 | 174 | 452 | Mixed | Mixed |
| arts | 2,032 | 160 | 186 | 1,677 | Mixed | Mixed |
| mdhs | 3,514 | 149 | 160 | **4,730** | Mixed | Mixed |
| handbook | 2,120 | 0¹ | 77 | 180 | All students | Mixed |

¹Handbook median 0KB = Incapsula bot-block shells for ~1,470 of 2,134 crawled captures.

---

## The three weight pathologies

### 1. Base64-inlined hero images crush mobile/limited-data students `[HIGH]`

9 pages in the crawl ship >100KB of base64-encoded images embedded directly in the HTML document:

| Page | Total KB | Base64 KB | Domain |
|---|---|---|---|
| DEI Conference article | 2,704 | 2,501 | mdhs |
| Honours graduate profile photo | 2,292 | 2,071 | finearts-music |
| Urban density news article | 1,779 | 1,617 | msd |
| Diversity grants page | 1,220 | 1,054 | mdhs |
| Law news article | 1,145 | 976 | law |
| CMR contact-us page | 734 | 570 | biomed |

Base64 inlining defeats browser caching, lazy-loading, responsive srcset, and CDN image optimization. Every byte is re-downloaded on every visit, with ~33% encoding overhead. On a 3G connection a 2MB news article is a 10–20 second wait and a real data cost.

### 2. Cookiebot icon duplicated 1,926 times on a single page `[HIGH]`

4 law staff profile pages at 5,007–5,056KB each contain 1,926 identical `<img>` tags — all carrying the same ~400-byte base64 PNG (the Cookiebot "opens in new window" arrow icon). The same string is repeated 1,926 times instead of referenced once. mdhs has the same pathology: 1,924 copies on a research-training page (4,730KB).

Root cause: the Cookiebot consent script re-decorates every external link with the arrow icon per render, and these pages embed external-page link soup. gzip masks the transfer size but the phone still parses 5MB of DOM with 1,938 `<img>` nodes.

### 3. Course template ships ~327KB before a single external file loads `[HIGH]`

Sampling 25 course pages on study.unimelb: median HTML 327KB, of which:
- ~109KB inline SVG (a 106KB icon sprite with 187 `<path>` icons, most unused)
- ~79KB inline JS
- ~43KB inline CSS

~70% of the document is inlined assets, not content. Because it's inlined per-page, a student browsing structure → entry-requirements → fees → how-to-apply re-downloads the same 106KB sprite + JS + CSS on every step. None of it benefits from browser cache.

---

## The script waterfall on course pages

| Metric | Count |
|---|---|
| Median external stylesheets | 10 |
| Median external `<script src>` | 21 |
| Scripts with defer/async | ~13% (3/21) |
| Blocking scripts | ~18 |
| Third-party tag/analytics origins | 7× googletagmanager.com, google-analytics.com, tealiumiq.com, tiqcdn.com, cdn.optimizely.com, cdn1.adoberesources.net |
| Font hosts | 3 (fonts.googleapis/gstatic + typekit) |
| Preconnect/preload hints | ~2 |

Both GTM and Tealium load simultaneously. ~18 scripts block parsing. 3 font hosts add DNS+TLS+FOIT cost. No resource hints. On a throttled 3G connection the course page is a ~30+ second first-load experience.

---

## The deepest nav equals the heaviest nav

58% of study.unimelb pages sit ≥5 levels deep (max 11). Because the full multi-level nav tree plus the 106KB icon sprite is rendered inline in each document, the deep IA directly inflates every page's first-load weight. The deeper the tree, the more nav markup ships per page — paid on every navigation.

Separately, at least one medicine.unimelb page sets `user-scalable=no` + `maximum-scale=1`, blocking pinch-zoom — a WCAG 1.4.4/1.4.10 mobile-accessibility failure.

---

## No page-weight budget exists

The 20-domain page-weight table shows max values 4×–30× above the median within single domains. No CI gate, no CMS publish-time guard, no dashboard. The two worst anti-patterns (base64 hero images and duplicate Cookiebot icons) are silent CMS/plugin side-effects no editor intended — and nothing caught them.

---

## Recommendations

### 1. De-inline the 9 known >100KB base64 image offenders `[HIGH · medium]`
Convert to served image files with width-appropriate srcset, `loading="lazy"`, and WebP/AVIF. One-off sweep with immediate impact.

### 2. Configure Cookiebot to use CSS instead of per-link `<img>` tags `[HIGH · quick-win]`
One config change: reference the external-link-arrow as a shared CSS `::after` background instead of injecting per-link `<img>` tags. Drops 4 law pages from ~5MB to well under 200KB instantly. The cheapest high-impact win in the estate.

### 3. Externalize the course template's shared assets `[HIGH · medium]`
Move the 106KB icon sprite, base CSS, and base JS into cacheable external files. Tree-shake the sprite to icons actually used. Target: cut per-page course document from ~327KB to <120KB, with shared assets cached after the first page.

### 4. Consolidate tag managers and defer scripts `[MEDIUM · medium]`
Single tag manager (GTM or Tealium, not both). Defer/async all non-critical scripts. Move analytics behind requestIdleCallback. Add preconnect hints for the real origins.

### 5. Stand up a page-weight budget and CI gate `[MEDIUM · medium]`
Warn >500KB HTML. Block >1MB HTML. Surface per-domain weight dashboard. Scheduled Lighthouse run on representative templates tracking LCP/INP/CLS.

### 6. Fix the pinch-zoom blocker `[MEDIUM · quick-win]`
Remove `user-scalable=no` + `maximum-scale=1` from the medicine template. One line fix, WCAG compliance, immediate mobile-accessibility win.

---

## Linked improvements from the register

| § | Improvement | Severity · Effort |
|---|---|---|
| 7.1 | De-inline base64 hero images; add CMS guard against data:image >10KB | HIGH · medium |
| 7.2 | Fix Cookiebot duplicate-icon pathology (1,926 copies/page → CSS sprite) | HIGH · quick-win |
| 7.3 | Externalize course template shared assets; tree-shake icon sprite | HIGH · medium |
| 7.4 | Consolidate tag managers; defer/async scripts; add resource hints | MEDIUM · medium |
| 7.5 | Stand up performance governance: weight budget, CI gate, Lighthouse dashboard | MEDIUM · medium |
| 7.6 | Fix pinch-zoom blocker on medicine template | MEDIUM · quick-win |

---

*Built from: page-weight.csv (20-domain weight table), improvements-register.md (§7 Performance & Mobile), cross-site-flow.csv (offshore audience mapping), and direct HTML analysis of the 154 pages >500KB in crawl/. June 2026.*
