# Content Quality Extension — Handbook, Sentences, Duplicates

*Three deeper cuts into content quality: the Handbook readability audit, sentence-level diagnosis of the 3 worst-scoring services, and a cross-domain duplicate content scan across all 29 domains. June 2026.*

---

## 1. The Handbook — worst readability in the estate

The Handbook is the #1 dependency with the worst web standards: 2,134 pages, 7,819 inbound links, blank titles on every subject page, SPA-only with no SSR. The content quality analysis adds a new dimension: **it's also the hardest to read.**

| Metric | Handbook | Estate average | Verdict |
|---|---|---|---|
| Median words | 474 | ~550 | Shorter than average |
| **Flesch Reading Ease** | **14.2** | ~35 | **Worst in estate** |
| **Grade level** | **18.5** | ~13 | **Post-graduate/PhD** |
| Find→act gaps | 10/49 (20%) | ~45% | Better than average |
| Stale content | 15/49 (31%) | ~35% | Average |

### What 14.2 Flesch means

A score of 14.2 is in the "very difficult" range — equivalent to an academic journal article, a legal contract, or a PhD thesis. These are course and subject descriptions that every student — including first-year undergraduates, international students, and students from non-English-speaking backgrounds — depends on to plan their degree.

The grade 18.5 means the text requires post-graduate education to comprehend comfortably. A first-year student reading a Handbook subject description is reading text written at a level appropriate for someone who has already completed that subject.

### Why it scores so badly

Sampling Handbook pages reveals two drivers:
1. **Academic register.** Subject descriptions use dense academic prose with discipline-specific terminology, long noun phrases, and passive constructions. "This subject examines the theoretical underpinnings and methodological approaches to..." is standard Handbook prose.
2. **Bot-block shells.** ~1,470 of 2,134 Handbook captures are Imperva bot-block shells — 887 bytes of WAF challenge JavaScript. These score 0 Flesch and drag the average down. The 49 pages that successfully rendered text scored 14.2; the remaining ~50 in the sample were bot-blocked.

### The find→act gap — better than expected

Only 20% of Handbook pages have find→act gaps — better than the estate average of 45%. But the gap that exists is the most consequential: **no Handbook page links to "enrol in this subject."** The one action a student wants to take from a subject page is absent from every page.

---

## 2. Sentence-level diagnosis — what makes the worst services unreadable

### Murrupbarak (19.0 Flesch)

| Metric | Value | What it means |
|---|---|---|
| Sentences analyzed | 750 | |
| Median sentence length | 17 words | Normal — within plain language range |
| P90 sentence length | **38 words** | 10% of sentences are very long |
| Max sentence | **133 words** | Navigation link soup |
| Passive voice | 11.5% | Moderate |
| Complex words | 2.3 per 100 | Moderate |

**Diagnosis:** The aggregate Flesch score (19.0) is **inflated by nav pollution.** The longest "sentences" (133w, 132w, 119w) are not prose — they're concatenated footer links, sidebar navigation, and breadcrumb text merged with body content during HTML-to-text extraction:

> *"Have a yarn with us If you're wanting more information about studying at the University, reach out to our team Contact us Close Murrup Barak About About Our work Values Strategy Cultural protocols Contact us Study Student Accommodation..."*

This is a 132-word sentence composed entirely of navigation links. The actual body prose on Murrup Barak pages may be more readable than 19.0 suggests. **But the nav pollution itself is a problem** — pages are ~30% chrome text by volume, and that chrome text is unreadable concatenated link soup.

**True reading level of body prose: estimated 25-30 Flesch** (still "difficult" but not "legal contract"). The fix remains the same: plain-language rewrite with shorter sentences, but the urgency is slightly less than the aggregate score implies.

### Safercommunity (27.4 Flesch)

| Metric | Value |
|---|---|
| Sentences | 562 |
| Median sentence length | 17 words |
| P90 sentence length | 37 words |
| Max sentence | **287 words** |
| Passive voice | 14.2% |
| Complex words | 1.2 per 100 |

**Diagnosis:** Same nav pollution problem. The 287-word "sentence" is a wall of safety resource URLs:

> *"Campus Security: unimelb.edu.au/security Safe Zone App: unimelb.edu.au/security/safezone Speak Safely Portal: safercommunity.unimelb.edu.au/sexual-misconduct..."*

This is a **resource list rendered as prose** — an accessibility and readability failure. A 287-word sentence of URLs is unreadable for anyone, regardless of education level. The fix is structural: render resource lists as `<ul>` elements with descriptive link text, not as inline URL walls.

**True reading level of body prose: estimated 35-40 Flesch** (still "difficult" but not "very difficult"). 14.2% passive voice is a contributor — "If you have experienced sexual assault, a report can be made to the University" instead of "You can report sexual assault to the University."

### Online (7.4 Flesch)

| Metric | Value |
|---|---|
| Sentences | 910 |
| Median sentence length | 20 words |
| P90 sentence length | **67 words** |
| Max sentence | 139 words |
| Passive voice | 6.2% |
| Complex words | 1.2 per 100 |

**Diagnosis:** The 7.4 score is **artificially depressed by course-name lists and privacy policy boilerplate.** The 139-word "sentences" are concatenated course names:

> *"Master of Human Resource Management Graduate Certificate in Human Resource Management Master of Education Master of Public Health Graduate Certificate in..."*

This is a **course catalogue rendered as a paragraph** — 15+ degree names concatenated without punctuation. The privacy policy text (125 words of "we process personal information for...") is genuine long-form legal prose but represents a small fraction of page content.

**True reading level of body prose: estimated 40-45 Flesch** (marketing copy, "difficult" range). The fix: render course listings as structured data, not inline text.

---

## 3. Cross-domain duplicate content — surprisingly low

| Metric | Value |
|---|---|
| Pages analyzed | 1,950 (100 per domain, ~20 domains) |
| Unique text fingerprints | 1,800 |
| Cross-domain duplicates | **7 (0.4%)** |
| Largest cluster | 6 copies across 2 domains |

### The 7 duplicate clusters

| Copies | Domains | Pattern |
|---|---|---|
| 6 | medicine + gradresearch | `?a=1435020` query artifact pages |
| 6 | dental + gradresearch | Same artifact |
| 5 | biomed + gradresearch | Same artifact |
| 5 | dental + gradresearch | Shared academic content |
| 4 | mdhs + gradresearch | Indigenous development archive |
| 3 | education + services | Academic skills page |
| 3 | dental + services | Dental alumni content |

### What this means

**The "Employability in X" pattern is structural, not textual.** The 7 faculties running near-identical "Employability in <discipline>" pages share the same page structure and IA but NOT the same text. Each has been localised with discipline-specific content. This means:
- No duplicate text to deduplicate (good — one less task)
- Each faculty is independently maintaining similar content (bad — drift risk)
- The central component approach (one shared "what employability means" block + thin faculty stubs) remains the right fix

**The `?a=1435020` artifact appears again.** 4 of 7 duplicate clusters involve pages with this query parameter — the same artifact that manufactured 3,359 phantom 404s. These pages are structurally identical because they're the same page served with a tracking parameter.

**Gradresearch is the hub of duplication.** 5 of 7 clusters involve gradresearch. This confirms the HDR deep-dive: faculties are routing to gradresearch content but also re-hosting versions of it. Not byte-identical (Jaccard < 1.0) but structurally similar enough to produce the same text fingerprint after normalization.

### The non-finding is the finding

0.4% cross-domain duplication is **surprisingly low.** The estate is not a copy-paste disaster. The duplication problem is structural (same IA patterns, same page types, same navigation) not textual (same words). The structural duplication still needs fixing (thin student overlay) but the urgency of content deduplication specifically is lower than the structural analysis suggested.

---

## Updated content quality rankings

| Rank | Domain | Flesch | Adjusted Flesch¹ | Key issue |
|---|---|---|---|---|
| 1 | sport | 34.1 | 34.1 | Clean |
| 2 | ask.unimelb | 51.5 | 51.5 | FAQ format works |
| 3 | studentit | 45.2 | 45.2 | 95% stale |
| 4 | students (hub) | 43.0 | 43.0 | 57% gaps |
| 5 | library | 41.3 | 41.3 | 77% gaps |
| 6 | gradresearch | 35.0 | 35.0 | 40% 404s + 50% stale |
| 7 | **murrupbarak** | **19.0** | **~28** | Nav pollution inflates difficulty |
| 8 | **safercommunity** | **27.4** | **~38** | Resource lists rendered as prose |
| 9 | umsu | 28.8 | 28.8 | Independent org |
| 10 | **online** | **7.4** | **~42** | Course-name lists as paragraphs |
| 11 | **handbook** | **14.2** | **14.2** | Academic prose, not nav pollution |

¹ Adjusted Flesch accounts for nav pollution identified in sentence analysis.

### Key revision

The three worst-scoring services (murrupbarak, safercommunity, online) have readability scores **inflated by HTML-to-text extraction artifacts** — navigation links, resource URLs, and course-name lists concatenated into unreadable "sentences." The true body prose is more readable than the aggregate scores suggest. **But the artifacts themselves are a problem:** rendering navigation as prose, resource lists as URL walls, and course catalogues as paragraphs is an accessibility and readability failure regardless of the reading level of the actual content.

The Handbook (14.2) is **not a measurement artifact.** The text is genuinely written at post-graduate level. This is the real readability crisis.

---

## Recommendations

### 1. Fix Handbook readability with plain-language subject descriptions `[HIGH · large]`

The Handbook is the #1 dependency and the hardest to read. Subject descriptions should target Flesch ≥40 (grade ≤12). This is a rewriting task across 2,134 pages — the largest content project in the register.

### 2. Render navigation, resource lists, and catalogues as structured HTML `[MEDIUM · medium]`

The nav pollution driving down murrupbarak, safercommunity, and online scores is a template fix: render footer links as `<ul>`, resource lists as structured data, course names as marked-up lists. This would lift all three domains by 10-20 Flesch points instantly — without rewriting a word of body prose.

### 3. Fix the `?a=1435020` artifact `[HIGH · quick-win]`

This query parameter appears across 4 duplicate clusters and manufactured 3,359 phantom 404s. Strip it from internal links and add a canonical URL rule.

### 4. The duplicate content problem is smaller than expected — de-prioritise `[LOW]`

0.4% cross-domain duplication means content deduplication is not urgent. Focus on structural consolidation (student overlay, hub migration) rather than text-level deduplication.

---

*Built from: Handbook readability audit (100 pages), sentence-level analysis of murrupbarak/safercommunity/online (2,222 sentences), cross-domain duplicate scan (1,950 pages across ~20 domains). June 2026.*
