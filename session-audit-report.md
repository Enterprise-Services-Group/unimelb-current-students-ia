# Claude Code Session Audit: unimelb-current-students-ia

**Audit date:** 2026-06-28  
**Project:** University of Melbourne Current Students IA Analysis  
**Session ID:** `dfc26550-6b5f-4b84-a072-67520f152ff3`  
**Methodology:** Based on [session-optimization-patterns](~/.hermes/skills/autonomous-ai-agents/claude-code/references/session-optimization-patterns.md)

---

## 1. Session Overview

### Scale & Structure

| Metric | Value |
|---|---|
| Total files | 359 |
| Total disk usage | 57 MB |
| Main session size | 22.0 MB |
| Subagent sessions | 142 (26 direct + 116 workflow-organized) |
| Workflow definitions | 9 |
| Duration | 199.4 hours (June 20–28, 2026) |

### Session Composition

| Component | Size | % of Total |
|---|---|---|
| Main session (`.jsonl`) | 22.0 MB | 39.1% |
| Subagent sessions | 29.4 MB | 52.2% |
| Workflow definitions | 0.9 MB | 1.5% |
| Tool results | 4.0 MB | 7.2% |
| **TOTAL** | **56.2 MB** | |

### Message Volume

| Metric | Count |
|---|---|
| Total messages | 4,388 |
| Assistant messages | 1,992 |
| User messages | 955 |
| System messages | 80 |
| Tool result messages | 1,674 |
| Avg assistant message length | 125 chars |
| Max assistant message length | 8,002 chars |

### Models Used

| Model | Main Session | Subagents | Total |
|---|---|---|---|
| `claude-opus-4-8` | 1,404 msgs | 1,980 msgs | **3,384** (dominant) |
| `claude-sonnet-4-6` | 579 msgs | 219 msgs | 798 |
| `claude-haiku-4-5-20251001` | — | 191 msgs | 191 |
| `<synthetic>` | 9 | 8 | 17 |

**Strategy observation:** Opus for heavyweight analysis and verification; Sonnet for interactive slide-deck work; Haiku reserved for lighter extraction tasks in subagents.

### Continuations (Context Reloads)

| Count | Pattern |
|---|---|
| **14** | Session continuation sprawl — each reloads compressed context summary |

---

## 2. Tool Usage

### Main Session — Top Tools

| Tool | Count | % of Total |
|---|---|---|
| **Bash** | 407 | 48.6% |
| **Edit** | 173 | 20.7% |
| **Read** | 137 | 16.4% |
| **Write** | 39 | 4.7% |
| **Agent** | 27 | 3.2% |
| MCP (Chrome JS) | 18 | 2.2% |
| Workflow | 9 | 1.1% |
| MCP (ccd_session) | 9 | 1.1% |
| Other | 18 | 2.1% |
| **TOTAL** | **837** | |

### Subagents — Top Tools

| Tool | Count |
|---|---|
| **Bash** | 886 |
| **Read** | 301 |
| **StructuredOutput** | 86 |
| MCP (Chrome JS) | 62 |
| **Write** | 37 |
| **Edit** | 12 |

### Combined Tool Totals

| Tool | Main | Subagents | **Grand Total** |
|---|---|---|---|
| Bash | 407 | 886 | **1,293** |
| Read | 137 | 301 | **438** |
| Edit | 173 | 12 | **185** |
| StructuredOutput | — | 86 | **86** |
| Write | 39 | 37 | **76** |
| Agent | 27 | — | **27** |

**Key observation:** `StructuredOutput` (86 calls) in subagents is a best practice — agents return structured JSON improvements rather than narrative. Zero `Grep`/`Glob` calls — all file discovery via Bash. Zero `TodoWrite` calls — tasks managed externally via workflow definitions.

---

## 3. Top 3 Token-Waste Patterns

### 🥇 Pattern 1: Session Continuation Sprawl (est. ~700K tokens)

| Metric | Value |
|---|---|
| Continuations detected | **14** |
| Est. tokens per continuation | ~50,000 |
| **Total waste** | **~700,000 tokens (~$1.75)** |

**Evidence:** Multiple user messages contain "This session is being continued from a previous conversation that ran out of context." The 22MB session was one continuous interactive run over 8 days, with 14 context-window resets. Each `--continue` reloads a compressed summary (~50K tokens) instead of starting fresh.

**Root cause:** The entire project (slide deck editing, graphify extraction, multi-agent audits, improvements register) was done in one monolithic interactive session rather than decomposed into phases.

**Fix:**
```bash
# Phase 1: Slide deck (interactive, 1-2 hrs)
claude "Update slide deck per feedback..."

# Phase 2: Graphify extraction (one-shot)
claude -p "Extract insights from /analysis/ -- structured output" --max-turns 10

# Phase 3: Multi-agent audit (workflow, already well-structured)
# Keep existing Workflow-based approach — just don't intermix with slide deck editing
```

**Savings:** ~700K tokens. ~80% reduction by isolating the interactive slide-deck work from the batch audit work.

---

### 🥈 Pattern 2: Filesystem Exploration in Bash (est. ~610K tokens)

| Metric | Value |
|---|---|
| Bash calls (main session) | **407** |
| Est. tokens per Bash call | ~1,500 |
| **Total waste** | **~610,000 tokens (~$1.53)** |

**Evidence:** 407 Bash calls in the main session alone — predominantly `ls`, `cat`, `find`, `wc -l`, `head`, `grep` exploration patterns. Subagents add another 886 Bash calls. The project has a large corpus (`analysis/`, `crawl/`, `.graphify/`) that gets repeatedly explored.

**Root cause:** No pre-built project overview. The agent re-discovers the file tree each time context resets.

**Fix:**
```bash
# Create project_overview.sh — run once, read many times
cat > .claude/scripts/project_overview.sh << 'EOF'
echo "=== Crawl data ===" && find crawl/ -name "index.json" | head -30
echo "=== Analysis files ===" && ls analysis/full-scrape/*.csv analysis/*.md
echo "=== Recent changes ===" && git diff --stat HEAD~5
EOF
```

**Savings:** ~400K tokens (assumes 2/3 of Bash calls are exploration). The agent reads one script output instead of 270+ individual `ls`/`cat` commands.

---

### 🥉 Pattern 3: Subagent Spawn Overhead (est. ~162K tokens)

| Metric | Value |
|---|---|
| Agent spawns (main session) | **27** |
| Est. tokens per spawn | ~6,000 |
| **Total waste** | **~162,000 tokens (~$0.41)** |

**Evidence:** 27 `Agent` tool calls from the main session, each loading full agent definitions (4-8KB) + task context + prompts into a new subagent context. The subagents themselves are well-structured (the 9 workflows orchestrating 116 workflow subagents), but the 27 direct subagent spawns from the main interactive session add overhead.

**Also notable:** 4 `claude-opus-4-8` agents doing graphify extraction tasks — these cost ~$0.50-2.00 each vs ~$0.05-0.20 if routed to Gemini.

**Fix:**
- Route graphify semantic extraction to Gemini: `export GOOGLE_API_KEY=...`
- Use `claude --agents '{"extractor":{...}}' -p "..."` with pre-configured agents
- The workflow-based subagents (116) are already well-structured — no change needed there

**Savings:** ~100K tokens + $0.50-2.00 per extraction session.

---

### Other Notable Patterns

| Pattern | Count | Est. Waste | Severity |
|---|---|---|---|
| No compaction in 22MB session | N/A | ~50K tokens | Medium — context grew unbounded, 199-hour duration |
| Visual preview overhead | 0 | 0 | ✓ None — good discipline |
| Inline task management | 0 | 0 | ✓ None — using Workflows instead |

### Total Estimated Token Waste

| Pattern | Est. Tokens |
|---|---|
| Session continuation sprawl | 700,000 |
| Filesystem exploration in Bash | 610,500 |
| Subagent spawn overhead | 162,000 |
| No compaction cost | 50,000 |
| **TOTAL** | **~1,522,500 tokens (~$3.81)** |

---

## 4. Recurring Workflow Patterns

### The Multi-Agent Analysis Pipeline (Primary Pattern)

This project discovered and refined a powerful recurring pattern executed across 9 workflows:

```
┌──────────┐    ┌──────────┐    ┌────────────┐    ┌──────────┐
│ ANALYSE  │───→│ VERIFY   │───→│ SYNTHESIZE │───→│ CRITIQUE │
│ (parallel│    │(adversar.│    │ (dedupe +  │    │(gap fill)│
│  agents) │    │ re-check)│    │  merge)    │    │          │
└──────────┘    └──────────┘    └────────────┘    └──────────┘
```

This pattern appeared in:
- **`estate-improvements-audit`** (wf_d830263f): 8 analysis dimensions × one agent each → verify → synthesize → critique → round 2 fill
- **`deep-research-ia-estate`** (wf_f7bd6380): 4 miners → triangulate → verify
- **`student-services-fragmentation`** (wf_6b43e276): Profile per service → synthesize cross-service patterns

### Journey Tracing Pattern

```
┌──────────────────────────────────────┐
│  One agent per journey stage         │
│  All stages run in PARALLEL          │
│  Each returns structured profile:    │
│    - structure                       │
│    - friction points                 │
│    - fragmentation                   │
│    - seams & handoffs                │
│    - fix recommendations             │
└──────────────────────────────────────┘
```

Appeared in:
- **`four-journey-deepdives`** (wf_4aa08b39): 4 personas, ~22 agents
- **`international-student-experience`** (wf_4efe170b): 1 persona, ~9 agents
- **`prospective-student-experience`** (wf_95f1cb51): 1 persona, ~8 agents
- **`lifecycle-journeys`** (wf_1c3052da): multiple personas, ~10 agents
- **`four-journeys-batch1`** (wf_b4e63309): 2 personas, ~9 agents

### Key Recurring Tasks

| Task | Frequency | Automated? |
|---|---|---|
| PDF/slide deck editing | 16+ user messages | Interactive (`Edit` tool) |
| Graphify knowledge graph extraction | 5+ `/graphify` commands | Semi (Agent spawn) |
| Data analysis (Python over CSV/crawl) | Every workflow | Bash + Python scripts |
| File reading/exploration | 438 Read calls | ✓ Well-optimized |
| Structured improvement generation | 138 improvements | ✓ StructuredOutput |
| `continue`/`pick up` context resets | 14 | ✗ Major waste source |

---

## 5. Best Practices That Emerged

### ✅ 1. Structured Workflows with Phased Execution
All 9 workflows define explicit phases (Analyse → Verify → Synthesize → Critique). This is the project's strongest practice: it creates repeatable, auditable multi-agent pipelines.

### ✅ 2. Verification-First Culture
Every analysis workflow includes an adversarial verification phase where a separate agent re-checks findings against raw data. Journal entries show verifiers correcting inflated numbers (e.g., "83 graduation pages" → actually "35"), dropping unsupported claims, and adding "Corrections made in-place" annotations. This is excellent scientific rigor applied to AI-assisted analysis.

### ✅ 3. Structured Output Convention
Subagents return `StructuredOutput` with typed `improvements[]` arrays (category, title, severity, effort). 138 concrete, categorized improvements across 5 dimensions (technical 42, content 38, governance 29, service 15, UX 14). This makes results machine-readable and mergeable.

### ✅ 4. Journal-Based Result Tracking
Each workflow has a `journal.jsonl` tracking `started` and `result` events with agent IDs and result keys. Paired with `.meta.json` files per agent, this creates a full audit trail of which agent produced which improvements.

### ✅ 5. Multi-Model Strategy
- **Opus** (3,384 msgs): Heavy analysis, verification, synthesis
- **Sonnet** (798 msgs): Interactive slide-deck editing, faster turnaround
- **Haiku** (191 msgs): Lightweight extraction in subagents

This is cost-aware and task-appropriate.

### ✅ 6. Artifact Persistence
39 `Write` calls in main session + 37 in subagents. Outputs go to disk (`analysis/`, `.graphify/`), not ephemeral context. The final improvements register survives session boundaries.

### ✅ 7. Zero Preview/Visual Waste
0 preview calls — no browser automation overhead. Slide-deck visuals verified manually by the user.

### ✅ 8. Workflow Scripts with Shared Context
Workflow `.js` scripts define `SHARED[]` context arrays pre-loaded with project paths, data references, and recurring fault patterns. This avoids repeating the same context across all agents.

---

## 6. Automation Opportunities

### 🔧 1. Session Decomposition (HIGH IMPACT)

**Problem:** 199-hour monolithic session with 14 context resets.

**Solution:** Split into separate Claude Code sessions or `claude -p` phases:

```bash
# Session 1: Slide deck (interactive, 2-3 hrs)
claude "Work on Current-Students-EndToEnd-Discussion slide deck"

# Session 2: Graphify extraction (batch, 1 hr)
for f in analysis/*.md; do
  claude -p "Graphify extract insights from $f" --max-turns 5 >> graphify_insights.md
done

# Session 3: Multi-agent audit (workflow, 4-6 hrs)
claude -p "Run estate-improvements-audit workflow" --max-turns 30
```

**Expected savings:** ~700K tokens, eliminates 14 context reloads.

### 🔧 2. Project Overview Script (HIGH IMPACT)

**Problem:** 1,293 Bash calls across main + subagents, many exploratory.

**Solution:** Pre-build and maintain a project overview:

```bash
# .claude/scripts/project_overview.sh — updated once, read many times
```

**Expected savings:** ~400K tokens by replacing 270+ exploratory Bash calls.

### 🔧 3. Graphify → Gemini Routing (MEDIUM IMPACT)

**Problem:** 4+ Opus agents doing graphify extraction at Opus prices.

**Solution:** Set `GOOGLE_API_KEY` so graphify routes extraction to Gemini.

```bash
export GOOGLE_API_KEY="..."  # in ~/.claude/.env
```

**Expected savings:** ~$0.50-2.00 per extraction session, ~$5-10 across this project.

### 🔧 4. Auto-Compaction Hook (MEDIUM IMPACT)

**Problem:** 22MB session with no compaction — context grew unbounded over 199 hours.

**Solution:** Add context guard hook:

```json
// ~/.claude/settings.json
{"hooks": {"Stop": [{"hooks": [{
  "type": "command", 
  "command": "python3 ~/.claude/scripts/context_guard.py"
}]}]}}
```

**Expected savings:** 50K+ tokens per long session, avoids forced restarts.

### 🔧 5. Reusable Analysis Pipeline Script (PROCESS IMPROVEMENT)

**Problem:** The Analyse→Verify→Synthesize→Critique pattern was manually orchestrated each time.

**Solution:** Codify as a reusable workflow template:

```javascript
// ~/.claude/workflows/analysis-pipeline.js
export const meta = {
  name: 'analysis-pipeline',
  phases: [
    { title: 'Analyse', detail: 'one analyst per dimension' },
    { title: 'Verify', detail: 'adversarial re-check' },
    { title: 'Synthesize', detail: 'dedupe + prioritize' },
    { title: 'Critique', detail: 'completeness gap analysis' },
  ],
}
```

### 🔧 6. Persistent Bash Session (LOW-MEDIUM IMPACT)

**Problem:** Subagents each explore the same file tree from scratch.

**Solution:** Use Hermes `persistent_shell: true` or an MCP filesystem server to share file-system state across agents.

---

## 7. Summary Dashboard

| Area | Rating | Key Metric |
|---|---|---|
| **Workflow structure** | ⭐⭐⭐⭐⭐ | 9 well-defined phased workflows |
| **Output quality** | ⭐⭐⭐⭐⭐ | 138 categorized improvements, adversarial verification |
| **Model strategy** | ⭐⭐⭐⭐ | Opus/Sonnet/Haiku mix, task-appropriate |
| **Session efficiency** | ⭐⭐ | 14 continuations, 199 hrs, 22MB main session |
| **Artifact persistence** | ⭐⭐⭐⭐ | Disk-persisted outputs, journal tracking |
| **Automation readiness** | ⭐⭐⭐ | Good patterns but not yet codified as templates |
| **Cost efficiency** | ⭐⭐ | ~1.5M tokens waste, graphify on Opus not Gemini |

### Bottom Line

This session produced **exceptional output** — 138 data-grounded, verified improvements across 5 dimensions. The workflow design (parallel analysis → adversarial verify → synthesize) is a **model pattern** that should be templated for reuse. The primary optimization opportunities are **structural** (session decomposition, project overview scripts) rather than behavioral — the actual agent behavior within subagents is already efficient. Fixing the 3 main waste patterns would save ~1.5M tokens (~$3.81) and eliminate the need for 14 context resets in a comparable future project.

---

*Generated from 359 files (57MB) across 199.4 hours of Claude Code sessions.*
