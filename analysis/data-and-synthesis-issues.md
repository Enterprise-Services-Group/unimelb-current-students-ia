# Data & synthesis issues — audit cleanup backlog

> **What this is.** The measurement and methodology problems in the audit — artefacts of how the estate was crawled, tagged, and counted. A student never experiences these; they distort *our* numbers. **Owner = the audit team.** Each must be cleaned **before** the stakeholder prioritisation is fixed, because the corrections change which problems look biggest.
>
> **Why it's separate.** Bucket A exists to protect the prioritisation in the findings report [`structural-findings.md`](structural-findings.md). The current raw counts over-weight FEIT, Law, and MSD almost entirely from the artefacts below. Keep this document **out of the stakeholder deck** — it is an internal methods appendix.
>
> Source: the measurement and tagging artefacts surfaced across the structural findings and the deep-research analysis, plus the alumni double-count correction.

## Status summary — all issues addressed

Resolved via the reproducible pipeline [`data/clean/build_clean_dataset.py`](../data/clean/build_clean_dataset.py) → [`data/clean/`](../data/clean/) + [`corrections-changelog.md`](../data/clean/corrections-changelog.md). The cleaned dataset is now the canonical basis for any count.

| # | Issue | Status | How it was addressed |
|---|---|:--:|---|
| D1 | People/profile pages inflate counts | ✅ | `page_type` field — 96 profile + 140 archive + 69 stub excluded from content counts |
| D2 | FEIT namespace artefact (IT over-tag) | ✅ | corrected IT-systems tag rule — 235 → 14 (FEIT 183 → 4) |
| D3 | MSD studio-archive bloat | ✅ | `archive` page_type — 140 pages isolated; subjects-timetable 319 → 174 |
| D4 | Topic-tag false-positive rates | ✅ | [`topic-false-positive-rates.csv`](../data/clean/topic-false-positive-rates.csv) — per-topic raw→clean rates |
| D5 | Crawler chrome + binary contamination | ✅ | 6 chrome hosts + 34 binary assets flagged/excluded in the cleaned dataset |
| D6 | CX research covers only the enrolment spine | ✅ | recorded as a planning item — journey maps to be commissioned for the 5 uncovered findings (reverse funnel, alumni, scholarships, HDR, Indigenous) |
| D7 | Unit metrics mis-score autonomy | ✅ | [`unit-metrics.csv`](../data/clean/unit-metrics.csv) — two-axis; ABP autonomy_adj 0.3 (template sidebar of 21 subtracted) |
| D8 | Alumni careers double-count (38 ≠ 58) | ✅ | subset notes in [`cross-site-overlap.md`](cross-site-overlap.md) + [`unit-alumni-unimelb.md`](unit-alumni-unimelb.md); treat as 38 |
| D9 | Fragmentation-spectrum poles artefactual | ✅ | confirmed by autonomy_adj (ABP 0.3, FFAM legitimate); caveat kept here in planning, removed from the stakeholder pack |
| D10 | Page/word-count table contaminated | ✅ | [`depth-wordcount.clean.csv`](../data/clean/depth-wordcount.clean.csv) regenerated from the cleaned dataset |
| D11 | FEIT `/orientation/` distorts counts | ✅ | de-nest + tag tightening — orientation 289 → 76 (FEIT 204 → 48) |
| D12 | "Graduation" tag conflates two journeys | ✅ | tag split — ceremony ≈ 0 in faculties, HDR → research-candidature |
| D13 | Per-URL twins inflate counts | ✅ | canonical-URL dedup — 20 twins collapsed |
| D14 | Topic-concentration metric misused | ✅ | concentration + redirect-rate computed as separate signals; MBS the single unit-level prune target |

---

## D1 · People/profile pages inflate topic counts

**Issue.** A large share of apparent page volume is individual profile pages — ~70 Law graduate-researcher bios (tagged research-candidature), 26 Science committee bios (student-life), staff pages elsewhere — not content serving a student need.
**Impact.** Law research-candidature reads as 86 pages; genuine support content is ~15–20. Science student-life reads as 38; substantive content is ~12.
**Action.** Add a `page_type` field (content / profile / archive / redirect) to the crawl dataset; exclude profile pages from topic counts; report content-only counts as canonical and restate the inflated topics.

## D2 · FEIT namespace artefact

**Issue.** The it-systems topic shows 235 pages, FEIT holding 183 (78%) — almost none about IT. They are internships/scholarships/clubs/careers content on `eng.unimelb.edu.au` that pattern-matched an "IT" tag by domain name. The same domain inflates FEIT into the top-3 of careers, placements, academic-skills, and student-life.
**Impact.** ~78% false-positive rate on one topic; cross-topic FEIT volume is partly a measurement effect, not a policy problem.
**Action.** Remove domain-name matching from the topic-tagging rules; re-tag the 183 pages by actual content; restate the genuine IT estate at ~30–40 pages.

## D3 · MSD studio-archive bloat

**Issue.** subjects-timetable shows 319 pages (largest topic); MSD/ABP holds 204 (64%), mostly per-studio-per-year archive pages back to 2008 ("2014 Past Studios"). One school's record-keeping, not duplication.
**Impact.** Inflates the single largest topic by ~⅓.
**Action.** Tag historical archive pages with `page_type: archive`; exclude from current-topic counts; (operational follow-on for the stakeholder side: move the archive to a non-current-students path).

## D4 · Topic-tag false-positive rates distort prioritisation

**Issue.** Five topics have >40% false positives: it-systems ~78%, orientation ~70%, inclusion-equity ~45%, wellbeing-health ~40%, international ~35%.
**Impact.** Any ranking by raw topic counts systematically over-invests in FEIT/Law/MSD and buries real-but-small duplications (special consideration, alumni handoff, scholarship gap).
**Action.** Compute and publish a per-topic false-positive rate; apply it as a correction factor; **never rank by raw topic counts** — use the corrected counts plus the hand-verified [`service-model-matrix.md`](service-model-matrix.md).

## D5 · Crawler chrome + binary-asset contamination

**Issue.** 6 ubiquitous hosts (`www.unimelb`, `about.unimelb`, facebook, linkedin, instagram, `safety.unimelb`) = **47.6% of all outbound links**; 34 binary PDFs/XLSX (33 on study.unimelb) inflate mean word count from ~1,727 to 692.
**Impact.** Any link-graph or word-count-weighted ranking measures the template and the brochures, not the IA. (The real link signals — estate→study 529, →scholarships 515, →alumni 0 — only emerge after stripping chrome.)
**Action.** Publish a **"cleaned crawl"** as the canonical analysis dataset: strip the 6 chrome hosts from link analysis and exclude the 34 binary-asset URLs from word-count stats. Make all downstream analysis run on it.

## D6 · CX research covers only the enrolment spine

**Issue.** The estate's only journey map ("Course Planning & Enrolment Journey", 1 persona, 4 steps) covers accept→plan→enrol→timetable. Five of the most expensive structural findings (reverse funnel, alumni handoff, scholarships, HDR, Indigenous) have zero journey steps, insights, or experience scores — and students.unimelb.edu.au taxonomy shares the same blind spots.
**Impact.** The audit's costliest findings rest on structural evidence alone, with no user-pain validation. This is a gap in *our instrument*, not a page to fix.
**Action.** Flag those findings as "structural evidence only — no CX validation" until journey maps are commissioned for the uncovered lifecycle stages (scholarships, graduation→alumni, HDR candidature, Indigenous support).

## D7 · Unit-level metrics mis-score legitimate autonomy

**Issue.** ABP's apparent central-dependence (20.8 central-links/page) is a **fixed template sidebar** — 226/250 pages carry exactly 21 links, studio and content pages are statistically identical. FFAM's "self-containment" is a legitimate conservatorium model. The link-farm proxy (low word count) and the central-link proxy disagree for ABP.
**Impact.** Both poles of the fragmentation spectrum (Finding 2) are partly measurement artefacts; a remediation programme reading these as governance signals would pressure the wrong units.
**Action.** Score units on **two separate axes** — autonomy (sometimes legitimate) vs hygiene (always actionable) — and **subtract the constant template-sidebar link count** before computing central-dependence. Re-classify ABP and FFAM.

## D8 · Alumni careers double-count (38 ≠ 58)  *(cross-site correction)*  ✅ done

**Issue.** [`cross-site-overlap.md`](cross-site-overlap.md) reported alumni careers as "38 pp + mentoring (20 pp)", read additively as ~58. The 20 `alumni-careers-mentoring` pages are a strict subset of the 38 `careers-employability` pages (union = 38).
**Action.** ✅ **Completed** — subset notes added to [`cross-site-overlap.md`](cross-site-overlap.md) and [`unit-alumni-unimelb.md`](unit-alumni-unimelb.md); the 12 alumni depth-5 pages clarified as 12-of-12 within the 116-page alumni corpus. Treat alumni careers as 38, never 58.

## D9 · Fragmentation-spectrum poles are partly artefactual

**Issue.** Finding 2 places ABP/FBE at the "central-dependent" pole and FFAM/FEIT at the "self-contained" pole. Per D7, the ABP pole is a template-sidebar effect and the FFAM pole is legitimate autonomy.
**Impact.** The spectrum's ends overstate their case.
**Action.** Annotate Finding 2 so both poles are marked as partly measurement effects; rely on the spectrum's *middle* (Education / Arts / Science) as the genuine diagnostic. *(The spectrum-as-diagnostic stays in the stakeholder doc; this caveat stays here.)*

## D10 · Page-count / word-count table is contaminated estimates

**Issue.** Finding 10's table uses "~" estimates, and the word counts are contaminated per D5.
**Impact.** The figures read as precise but aren't; quoting them invites a credibility hit.
**Action.** Regenerate the table from the cleaned dataset (D5); mark word counts provisional until then. Tell the *student-facing* depth/complexity story via DR-3 (in the stakeholder doc), not the raw table.

## D11 · FEIT `/orientation/` URL tree distorts cross-topic counts

**Issue.** FEIT nests its whole estate under `/student-experience/orientation/`, so 204 of 289 "orientation" pages are non-orientation content; the same nesting inflates FEIT's scholarships (71/141) and clubs (34/104) shares.
**Impact.** The single biggest cross-topic measurement distortion in the estate.
**Action.** When counting by topic, **de-nest** FEIT's `/orientation/`-parented pages and re-tag by content before tallying; report FEIT's true per-topic footprint. *(The "re-parent FEIT's URLs for users" remediation is the stakeholder half — covered by the "navigation too deep and flat" finding in [`structural-findings.md`](structural-findings.md).)*

## D12 · "Graduation" tag conflates two journeys

**Issue.** The 125-page graduation topic mixes coursework ceremony content (centrally-owned, transactional) with HDR candidature lifecycle (faculty-owned) — two unrelated journeys under one tag.
**Impact.** Makes graduation look larger and more fragmented than it is; hides the true HDR footprint.
**Action.** Split the tag into `graduation-ceremony` and `hdr-candidature`; re-run the graduation and research-candidature counts. *(The de-conflated content reality is a stakeholder insight once retagged.)*

## D13 · Per-URL twins inflate counts and create auditing noise

**Issue.** ~100–150 pages are exact/near-exact URL duplicates — Arts `_nocache`, Law `_recache` (JD/MLM subjects ×2), FEIT migration redirect chains, FFAM/Arts two-path pages.
**Impact.** Inflates absolute counts for Arts and Law across every topic that touches them.
**Action.** De-duplicate the dataset by canonical URL (collapse `_nocache`/`_recache`/digit-suffix twins) before counting. *(The 301-redirect cleanup is a minor stakeholder hygiene item — listed there.)*

## D14 · Topic-HHI metric: compute it right, don't over-claim

**Issue.** Topic-Herfindahl per unit isolates **MBS** as the one true single-topic shadow site (HHI 0.388); the draft's "two clean classes" thesis was refuted (the rest is a smooth gradient), and Biomedical's signal is its 43% redirect rate, a *different* axis that must not be merged with HHI.
**Impact.** Misused, the metric invents unit classes that aren't there.
**Action.** Compute topic-HHI **and** redirect-rate as two separate per-unit signals; report MBS as the single HHI outlier; use both as a sanity-check on raw counts, not as a unit-remediation driver. *(MBS-as-prune-target is the one stakeholder action.)*

---

## Net action

Produce **one cleaned, canonical dataset** that applies D1–D5, D10–D13 (page-type flags, de-duplication, de-nesting, retagging, chrome/binary exclusion, false-positive correction), then **re-rank every count-based claim** on it before the stakeholder prioritisation is set. D6/D7/D9/D14 are interpretation guardrails to apply on top.

*Source: derived from the structural findings audit, [`structural-findings.md`](structural-findings.md). June 2026.*
