# Scholarships — Deep-Dive

*The highest-volume content-quality failure in the estate. 2,151 pages. 94.7% emit identical `<title>` tags. 96% skip a heading level. Every scholarship is indistinguishable in search results, bookmarks, and screen-reader navigation. June 2026.*

---

## Executive summary

Scholarships are a core student need — the catalogue every student searches to fund their degree. The University maintains 2,151 scholarship pages on scholarships.unimelb.edu.au. But two template failures make the entire catalogue near-invisible and inaccessible:

1. **2,038 of 2,151 pages (94.7%) emit the identical `<title>`**: "Find a scholarship | University of Melbourne." Every scholarship detail page has the same browser tab label, the same bookmark text, the same search-result snippet. A student with three scholarship tabs open cannot tell which is which. A screen-reader user navigating by heading cannot distinguish one scholarship from another. Google sees 2,038 pages with the same title.

2. **96% of pages skip a heading level.** The most common heading-skip pattern in the estate, concentrated in one template. Screen-reader users lose document structure.

This is one template fix that touches 2,038 pages at once — the highest-leverage accessibility + findability improvement by volume in the entire register.

---

## The numbers

| Metric | Value |
|---|---|
| Total scholarship pages | 2,151 |
| Pages with identical `<title>` "Find a scholarship \| University of Melbourne" | 2,038 (94.7%) |
| Pages with unique `<title>` | 113 (5.3%) |
| Pages with heading-skip | ~2,065 (96%) |
| Median page weight | 188KB |
| P90 page weight | 190KB (remarkably tight — template is consistent) |
| Faceted-search permutations | ~2,100 — 24% of all URLs are scholarship permutations |
| Hub contextual links to scholarships | Minimal — the hub barely reaches the catalogue |

---

## The title duplication: what it means in practice

### For students
- Open three scholarship tabs → all three browser tabs say "Find a scholarship"
- Bookmark a scholarship → the bookmark text is "Find a scholarship"
- Search browser history → 2,038 entries all read "Find a scholarship"
- Share a scholarship link on social media → the preview card says "Find a scholarship"

### For screen-reader users
- Navigate by page title → every page is "Find a scholarship." No way to distinguish the Rhodes Scholarship from the Access Melbourne bursary without reading the full page body.
- Screen readers announce the title first. 2,038 pages announce identically.

### For search engines
- Google indexes 2,038 pages with the same title. The search result for every scholarship is indistinguishable. A student searching "Melbourne Law School scholarship" sees 12 results all titled "Find a scholarship | University of Melbourne."

### For analytics
- Page-view reports group by title. 2,038 pages collapse into one row. No per-scholarship analytics possible from standard title-based reporting.

---

## The heading-skip: 96% accessibility failure

The scholarship template skips heading levels — typically jumping from `<h1>` (the page title, generic) to `<h3>` (scholarship name) without an intervening `<h2>`. This is the most concentrated heading-skip pattern in the estate: 2,065 of 2,151 pages, all from one template.

Screen readers rely on heading hierarchy to build a document outline. A skip from h1→h3 breaks the outline. WCAG 1.3.1 (Info and Relationships) requires heading levels to be nested without skipping.

---

## The faceted-search bloat

~2,100 of the 2,151 scholarship pages are faceted-search permutations — the same content served under different filter combinations. These are not distinct pages; they're the catalogue filtered by faculty, level, and category. Every permutation emits the identical `<title>` "Find a scholarship" and carries the same template markup.

This means 24% of all crawled URLs in the estate are scholarship permutations — and they're all titled identically and structured identically. The crawl spent meaningful resources capturing the same template 2,100 times.

---

## The findability gap: hub barely reaches the catalogue

The central student hub (students.unimelb.edu.au) sends minimal contextual links to scholarships.unimelb.edu.au. Cross-site-flow.csv shows the hub is not among the top referrers. A student on the hub looking for scholarship information has no prominent path to the catalogue.

The scholarships catalogue itself is well-structured — faceted search by faculty, level, and category. But a student must already know it exists to find it. The hub doesn't route them there.

---

## The page weight — surprisingly tight

At 188KB median and 190KB P90, the scholarship template is one of the most consistent in the estate. The max is 199KB — a range of only 11KB across 2,151 pages. This proves the template is uniform and a single fix will touch every page identically. Unlike the Handbook (SPA + bot-block) or study.unimelb (327KB with 106KB inline sprite), the scholarship pages are structurally simple. The title and heading problems are pure template bugs — easy to fix, impossible to miss once fixed.

---

## Recommendations

### 1. Give each scholarship page a descriptive `<title>` `[HIGH · quick-win]`
Template: "[Scholarship name] — [Faculty/Level] Scholarship | University of Melbourne". Example: "Rhodes Scholarship — Graduate Research Scholarship | University of Melbourne." One template change touches all 2,138 pages. The highest-leverage findability + accessibility fix in the estate by volume.

### 2. Fix the heading-skip at the template layer `[HIGH · medium]`
Insert an `<h2>` between the generic page `<h1>` and the per-scholarship `<h3>`. The `<h2>` should carry the scholarship name, making the document outline: h1="Scholarships at Melbourne" → h2="Rhodes Scholarship" → h3="Eligibility," "How to apply," etc. One template change fixes 96% of heading-skips in this domain.

### 3. Add facet pagination metadata `[MEDIUM · medium]`
Tag faceted-search permutations with `<meta name="robots" content="noindex, follow">` or canonicalise to the unfiltered base page. This prevents 2,100 near-identical pages from diluting search equity while keeping the base catalogue indexable.

### 4. Wire the hub to the scholarships catalogue `[MEDIUM · medium]`
Add prominent "Find a scholarship" links from the hub's fees/finance pages, the "Get Started" sequence, and the student support section. A student on the hub should not need to know the scholarships subdomain exists.

---

## Linked improvements from the register

| § | Improvement | Severity · Effort |
|---|---|---|
| 6.2 | Give each scholarship detail page its own `<title>` | HIGH · quick-win |
| 3.6 | No shared scholarships-catalogue convention — hub barely reaches it | MEDIUM · medium |
| 4.4 | ~2,100 scholarships pages are faceted-search permutations — 24% of all crawled URLs | MEDIUM · medium |
| 6.1 | Fix the shared-CMS heading-skip seam at the template layer | HIGH · medium |

---

*Built from: improvements-register.md (§6.2, §3.6, §4.4, §6.1), page-weight.csv (188KB median, 199KB max), scholarships crawl data (2,151 pages), and cross-site-flow.csv (hub→scholarships links). June 2026.*
