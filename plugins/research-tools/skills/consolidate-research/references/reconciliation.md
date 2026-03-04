# Reconciliation Protocol & Agentic Mode Reference

**Version**: 1.0
**Last validated**: 2026-03-04
**Consumed by**: consolidate-research (Step 4: Reconcile)
**Purpose**: Detailed protocols for provenance weighting, citation scoring, deduplication, dependency propagation, confidence tier assignment, structural artifact merging, and autonomous agentic consolidation.

---

## Section 1: Provenance Hierarchy

Every claim extracted during consolidation carries a **provenance channel** derived from the model configuration in the consolidation manifest. The provenance channel determines a weight multiplier applied during confidence tier computation.

### Provenance Weight Table

| Provenance Channel | Weight | Source Condition | Rationale |
|--------------------|--------|------------------|-----------|
| `internal_document` | 1.5x | Gemini `file_search` against uploaded docs | Grounded in proprietary/verified data the user controls |
| `site_restricted` | 1.3x | GPT-5.2 with `site_restrictions` capability | Limited to authoritative domains; reduced noise |
| `web_search` | 1.0x | Any model with open `web_search` | Baseline — open web, standard reliability |
| `quick_validation` | 0.7x | GPT-5.2 chat (no deep research) | Fast check, shallow reasoning, less thorough sourcing |
| `unsourced_assertion` | 0.3x | Any model assertion without citation | May be training data recall; unverifiable provenance |
| `agentic_verification` | 0.9x | Claude Opus 4.6 web search during agentic consolidation | Post-hoc verification; useful but not primary research |
| `agentic_gap_fill` | 0.8x | Claude Opus 4.6 web search filling coverage gaps | Gap-fill context is narrower than primary research |

### Provenance Assignment Rules

```
For each claim C in model output M:
  If M.capabilities includes file_search AND C cites uploaded document:
    C.provenance = internal_document
  Else if M.capabilities includes site_restrictions AND C.source_domain in M.site_restrictions:
    C.provenance = site_restricted
  Else if C has URL citation:
    C.provenance = web_search
  Else if M.role == recency_validator:
    C.provenance = quick_validation
  Else:
    C.provenance = unsourced_assertion
```

### Effective Confidence Score

```
effective_score(claim) = citation_quality_score * provenance_weight * cross_model_modifier
```

Where `cross_model_modifier` is defined in Section 2.

---

## Section 2: Citation Quality Rubric

### Base Score (0-5)

| Score | Source Type | Example |
|-------|------------|---------|
| 5 | Primary source — original data, official record | SEC filing, peer-reviewed paper, RFC, official API docs, benchmark dataset |
| 4 | High-quality secondary — expert analysis of primary data | Gartner/Forrester report, quality journalism with named sources, conference talk by maintainer |
| 3 | General secondary — professional coverage | News article, press release, industry publication, Stack Overflow accepted answer |
| 2 | Tertiary — aggregated/compiled | Wikipedia, tutorial blogs, content aggregators, promotional whitepapers |
| 1 | Unsourced model assertion with reasoning | Model claims "X is best practice" with logical reasoning but no external citation |
| 0 | Unverifiable or hallucination-suspect | Fabricated URL, non-existent paper, citation that doesn't support the claim |

### Cross-Model Citation Modifier

When multiple models address the same claim, apply these modifiers to the combined score:

| Scenario | Modifier | Rationale |
|----------|----------|-----------|
| Same model cites same source twice | +0 (no boost) | Repetition is not corroboration |
| Different models cite same primary source | +1 | Cross-validation of interpretation, but not independent sourcing |
| Different models cite different primary sources, same conclusion | +2 | Genuine independent corroboration — strongest signal |
| Different models, different conclusions from same source | -1 (flag conflict) | Interpretation divergence; requires reconciliation |

### Scoring Procedure

```
For each claim C with citations from models [M1, M2, ...]:
  1. Score each citation individually (0-5)
  2. Compute base_avg = mean(all citation scores)
  3. Run citation deduplication (Section 3)
  4. Apply cross-model modifier based on dedup result
  5. Apply provenance weight (Section 1)
  6. final_score = base_avg * provenance_weight + cross_model_modifier
```

---

## Section 3: Citation Deduplication Protocol

When multiple models agree on a claim, determine whether their agreement stems from independent research or shared underlying sources.

### Step-by-Step Process

```
STEP 1: EXTRACT
  For each claim C with multi-model support:
    For each model M citing C:
      Extract: primary_urls[], reference_titles[], author_names[]

STEP 2: NORMALIZE
  For each URL:
    Strip: tracking params (?utm_*, ?ref=*, ?source=*, &fbclid=*, etc.)
    Normalize: www.example.com → example.com
    Normalize: http → https
    Normalize: trailing slashes
    Resolve: URL shorteners to final destination
    Canonicalize: /blog/post-title/ == /blog/post-title

STEP 3: CLUSTER
  Group normalized URLs by domain + path
  Group reference titles by fuzzy match (>80% token overlap)
  Group author names by exact match

STEP 4: COMPUTE OVERLAP
  shared_sources = |intersection of source clusters across models|
  total_sources  = |union of source clusters across models|
  overlap_ratio  = shared_sources / total_sources

STEP 5: CLASSIFY
  If overlap_ratio > 0.50:
    classification = "shared_source"
    modifier = +1 (cross-validation only, not independent)
    note = "Models converge but draw from overlapping source pool"

  If overlap_ratio <= 0.50:
    classification = "independent_corroboration"
    modifier = +2 (genuine independent sourcing)
    note = "Models independently reached same conclusion from different evidence"

  If overlap_ratio == 1.0 AND total_sources == 1:
    classification = "single_source_echo"
    modifier = +0 (no boost — one source repeated)
    note = "All models reference same single source; treat as single-source claim"

STEP 6: ADJUST
  Apply modifier to confidence tier computation (Section 6)
  Record classification in claims matrix for traceability
```

### Edge Cases

| Case | Handling |
|------|----------|
| Model cites a source that cites another source | Trace to root primary source for dedup comparison |
| One model has no citations but agrees with claim | Treat as `unsourced_assertion` provenance; does not count toward dedup |
| Models cite same organization but different publications | Count as partially independent (overlap_ratio += 0.5 per shared org) |

---

## Section 4: Dependency Propagation Algorithm

Claims often depend on other claims. A recommendation built on a Tier 3 factual claim cannot itself be Tier 1. This algorithm walks the dependency graph to enforce consistency.

### Pseudocode

```
FUNCTION propagate_dependencies(claims_matrix):

  # Build dependency graph
  FOR each claim C in claims_matrix:
    C.depends_on = identify_dependencies(C)
    # Dependencies detected via:
    #   - Explicit "because" / "given that" / "building on" language
    #   - Causal chains: C1 → C2 → C3
    #   - Recommendation → factual basis links
    #   - Quantitative claims that derive from other quantitative claims

  # Topological sort to process leaves first
  sorted_claims = topological_sort(claims_matrix)

  # Propagate tier constraints
  FOR each claim C in sorted_claims (leaf-to-root):
    IF C.depends_on is non-empty:

      min_support_tier = MIN(tier(D) for D in C.depends_on)

      # Rule 1: A claim cannot be more confident than its weakest support
      IF C.tier < min_support_tier:   # lower number = higher confidence
        # C.tier is already appropriately cautious; no change
        PASS

      IF C.tier > min_support_tier:
        # This is fine — a claim CAN be less confident than its support
        PASS

      # The key rule: cap at weakest dependency
      IF tier_number(C) < tier_number(min_support_tier):
        old_tier = C.tier
        C.tier = min_support_tier
        LOG: "DOWNGRADE: Claim [{C.id}] '{C.text_summary}'
              moved from Tier {old_tier} → Tier {C.tier}
              due to dependency on [{D.id}] (Tier {min_support_tier})"

      # Rule 2: Flag at-risk recommendations
      IF min_support_tier == 3 AND C.type == "recommendation":
        FLAG: "RECOMMENDATION AT RISK: '{C.text_summary}'
               depends on Tier 3 claim [{D.id}]: '{D.text_summary}'.
               Verify factual basis before acting on this recommendation."

  RETURN claims_matrix, downgrade_log, at_risk_flags
```

### Tier Number Convention

| Tier | Number | Meaning |
|------|--------|---------|
| Tier 1 | 1 | High confidence — acts as strong foundation |
| Tier 2 | 2 | Moderate confidence — usable with caveats |
| Tier 3 | 3 | Low confidence — requires verification |

A claim with `tier_number = 1` depending on a claim with `tier_number = 3` must be downgraded to `tier_number = 3`.

### Circular Dependency Handling

```
IF circular dependency detected (A depends on B depends on A):
  BREAK cycle at the claim with lowest citation quality
  FLAG: "Circular dependency detected: [{A.id}] <-> [{B.id}].
         Broken at [{weakest.id}]. Review reasoning chain."
```

---

## Section 5: False Confidence Audit

Run this audit on ALL claims tentatively assigned Tier 1, and on any Tier 2 claim in a high-stakes consolidation. Seven mandatory checks:

### Audit Checklist

```
CHECK 1: Citation Diversity
├─ Do sources cite DIFFERENT primary sources?
├─ Or are all models drawing from the same 2-3 underlying sources?
├─ FAIL → Downgrade to Tier 2; note "shared source pool"
└─ Uses: dedup classification from Section 3

CHECK 2: Specificity Test
├─ Is the claim specific enough to be falsifiable?
├─ "React is popular" → too vague (FAIL)
├─ "React has >40% market share in frontend frameworks as of 2025" → specific (PASS)
└─ FAIL → Downgrade to Tier 2; note "unfalsifiable as stated"

CHECK 3: Recency Check
├─ Could this information have changed since sources were published?
├─ Check: source publication dates vs. claim volatility
├─ Pricing, market share, API details: high volatility (6-month window)
├─ Architecture patterns, compliance frameworks: lower volatility (18-month)
└─ FAIL → Downgrade to Tier 2; note "recency risk — verify current state"

CHECK 4: Contrarian Search
├─ Does credible dissent exist for this claim?
├─ In agentic mode: execute targeted search for counterarguments
├─ In standard mode: note if no contrarian perspective was found
└─ FAIL → Downgrade to Tier 2; note "unexamined contrarian position exists"

CHECK 5: Mechanism Agreement
├─ Do sources explain WHY the claim is true?
├─ Same mechanism cited by all = possible shared training bias
├─ Different mechanisms converging = genuinely high confidence
├─ Example: "Firebase scales well" — do models cite different reasons?
└─ FAIL → Note "mechanism convergence — possible shared bias"

CHECK 6: Provenance Diversity
├─ Do supporting sources use DIFFERENT provenance channels?
├─ site_restricted + web_search converging = stronger signal
├─ Two web_search sources converging = weaker signal
├─ internal_document + web_search converging = strongest signal
├─ SCORING:
│   3+ distinct provenance channels → strong diversity (PASS+)
│   2 distinct provenance channels  → adequate diversity (PASS)
│   1 provenance channel            → weak diversity (WARN)
└─ FAIL → Note "single provenance channel — corroboration may be superficial"

CHECK 7: Model Methodology Diversity
├─ Did models use different REASONING APPROACHES to reach the same claim?
├─ Claude: cross-domain analogy + deep reasoning
├─ Gemini: exhaustive cataloging + benchmark data
├─ GPT-5.2: site-restricted investigation + recency data
├─ STRONG: Different methodologies converging on same conclusion
├─ WEAK: All models appear to have used similar web search → similar results
└─ FAIL → Note "methodology convergence — models may have followed same search path"
```

### Audit Summary Format

```yaml
false_confidence_audit:
  claim_id: "C-042"
  claim_text: "Firebase Cloud Functions v2 supports Python 3.12+"
  tentative_tier: 1
  checks:
    citation_diversity: PASS     # 3 different sources across 2 models
    specificity: PASS            # Falsifiable, version-specific
    recency: WARN                # API docs change frequently
    contrarian: PASS             # No credible dissent found
    mechanism: PASS              # Different reasoning paths
    provenance_diversity: PASS   # internal_document + web_search
    methodology_diversity: PASS  # file_search + web_search approaches
  audit_result: PASS_WITH_NOTE
  final_tier: 1
  notes: "Recency flag — verify against latest Firebase release notes"
```

---

## Section 6: Confidence Tier Rubric

### Decision Tree for Tier Assignment

```
CLAIM ASSESSMENT
│
├── Cross-model agreement? (2+ models support claim)
│   │
│   ├── YES ──► Run citation deduplication (Section 3)
│   │   │
│   │   ├── Independent sources? (overlap_ratio <= 0.50)
│   │   │   │
│   │   │   ├── YES ──► Citation quality avg >= 4?
│   │   │   │   │
│   │   │   │   ├── YES ──► False confidence audit passes?
│   │   │   │   │   │
│   │   │   │   │   ├── YES ──────────────────────► TIER 1
│   │   │   │   │   │   (High confidence: independent
│   │   │   │   │   │    corroboration, quality sources)
│   │   │   │   │   │
│   │   │   │   │   └── NO (audit flags) ─────────► TIER 2
│   │   │   │   │       (Downgraded: audit concern)
│   │   │   │   │
│   │   │   │   └── NO (avg < 4) ─────────────────► TIER 2
│   │   │   │       (Independent but weaker sources)
│   │   │   │
│   │   │   └── NO (overlap > 0.50, shared sources)
│   │   │       │
│   │   │       ├── Citation quality avg >= 4?
│   │   │       │   │
│   │   │       │   ├── YES ──────────────────────► TIER 2 (upper)
│   │   │       │   │   CAP: shared sources cannot
│   │   │       │   │   reach Tier 1 regardless of
│   │   │       │   │   citation quality
│   │   │       │   │
│   │   │       │   └── NO ───────────────────────► TIER 2 (lower)
│   │   │       │       (Shared sources + weaker quality)
│   │   │       │
│   │   │       └── Single source echo?
│   │   │           │
│   │   │           └── YES ──────────────────────► Treat as SINGLE SOURCE
│   │   │               (below)
│   │   │
│   │   └── [proceed to dependency propagation after assignment]
│   │
│   └── NO (single model only)
│
├── Single source? (only 1 model supports claim)
│   │
│   ├── Citation quality >= 4?
│   │   │
│   │   ├── YES ──► Provenance = site_restricted OR internal_document?
│   │   │   │
│   │   │   ├── YES ──────────────────────────────► TIER 2 (upper)
│   │   │   │   (Strong citation from authoritative channel)
│   │   │   │
│   │   │   └── NO (web_search or other) ─────────► TIER 2 (lower)
│   │   │       (Strong citation but open-web provenance)
│   │   │
│   │   └── NO (quality < 4) ────────────────────► TIER 3
│   │       (Single source, weak citation)
│   │
│   └── [Note: single-source claims should be flagged for gap analysis]
│
└── Contested? (models actively disagree)
    │
    ├── In AGENTIC mode?
    │   │
    │   ├── YES ──► Attempt web search resolution (Section 8)
    │   │   │
    │   │   ├── Resolved ──► Re-enter decision tree with new evidence
    │   │   │
    │   │   └── Unresolved ──────────────────────► TIER 3
    │   │       + present all positions
    │   │       + [Unresolved] annotation
    │   │
    │   └── NO (standard mode)
    │       │
    │       └── ──────────────────────────────────► TIER 3
    │           + present all positions with source attribution
    │           + note: "Sources actively disagree"
    │
    └── [Always run dependency propagation after tier assignment]
```

### Post-Assignment Steps

After initial tier assignment:
1. Run dependency propagation (Section 4)
2. Run false confidence audit on all Tier 1 claims (Section 5)
3. Record final tier with full audit trail

---

## Section 7: Structural Artifact Merging Rules

When multiple model outputs contain structured artifacts (tables, decision trees, timelines, matrices), merge them rather than choosing one or flattening to prose.

### Tables

```
MERGE PROCEDURE: Tables
│
├── 1. IDENTIFY shared dimensions
│      Compare row headers and column headers across sources
│      Use fuzzy matching (>80% token overlap) for header equivalence
│
├── 2. UNION all dimensions
│      Combined table = union of all rows × union of all columns
│      Mark new rows/columns with source: "[Source X only]"
│
├── 3. RESOLVE overlapping cells
│      For each cell present in 2+ sources:
│      ├── Values agree (within 10% for numeric) → use consensus value
│      ├── Values disagree:
│      │   ├── Prefer higher-provenance source value as primary
│      │   └── Note: "Alt: [other value] (Source Y)"
│      └── Add source attribution superscript: value^[S1,S2]
│
├── 4. FILL sparse cells
│      Empty cells marked with "—" and footnote: "Not covered by any source"
│
└── 5. ADD provenance row/column
       Final row or column showing which source(s) informed each entry
```

### Decision Trees

```
MERGE PROCEDURE: Decision Trees
│
├── 1. IDENTIFY shared decision points (root and branch nodes)
│      Match by: decision question text (fuzzy match)
│
├── 2. ALIGN common paths
│      Where trees share the same decision → outcome path:
│      merge into single path
│
├── 3. HANDLE divergent paths
│      Where trees branch differently at the same decision point:
│      ├── Present BOTH branches
│      ├── Label: "[Source A path]" / "[Source B path]"
│      └── Add flag: "⚠ Sources disagree at this decision point"
│
├── 4. HANDLE unique subtrees
│      Decision points only one source covers:
│      ├── Include in merged tree
│      └── Label: "[Source X only — not validated by other sources]"
│
└── 5. CONFIDENCE annotations
       Each leaf node gets tier annotation based on path agreement
```

### Timelines

```
MERGE PROCEDURE: Timelines
│
├── 1. NORMALIZE date formats
│      All dates → ISO 8601 (YYYY-MM-DD) or YYYY-MM or YYYY-QN
│
├── 2. INTERLEAVE chronologically
│      Merge all events into single timeline sorted by date
│
├── 3. RESOLVE date conflicts
│      Same event, different dates across sources:
│      ├── Present as range: "YYYY-MM to YYYY-MM [Sources disagree]"
│      └── Prefer source with primary-source citation for date
│
├── 4. FLAG single-source events
│      Events mentioned by only one source:
│      └── Mark: "[Single source: Source X]"
│
└── 5. ADD source column
       Each timeline entry shows: Event | Date | Source(s) | Confidence
```

### Matrices (Comparison / Evaluation)

```
MERGE PROCEDURE: Evaluation Matrices
│
├── 1. UNION evaluation dimensions (rows)
│      Combine all criteria from all sources
│      Normalize similar criteria (e.g., "DX" = "Developer Experience")
│
├── 2. UNION evaluated items (columns)
│      Combine all options/products/items being evaluated
│
├── 3. RESOLVE conflicting scores
│      Same cell scored differently:
│      ├── Show range: "[3.5 — 4.2]" with source labels
│      ├── Compute weighted average using provenance weights
│      └── Note methodology difference: "Source A used benchmarks; Source B used expert survey"
│
├── 4. PRESERVE scoring methodology
│      Footnotes per source explaining their scoring approach
│      This enables the reader to interpret score ranges
│
└── 5. COMPUTE consensus scores (where possible)
       If methodology is compatible → weighted average as primary
       If methodology differs → show range, no false consensus
```

### General Merging Principles

| Principle | Application |
|-----------|-------------|
| Never flatten structure to prose | Merged artifact stays as table/tree/timeline |
| Source attribution is mandatory | Every cell/node/event shows its source(s) |
| Disagreement is signal, not noise | Divergences are highlighted, not hidden |
| Provenance weight breaks ties | Higher-provenance value is primary display |
| Original artifacts preserved in appendix | If consolidation is complex, include originals |

---

## Section 8: Agentic Consolidation Mode

### When to Use

| Condition | Required? |
|-----------|-----------|
| All research model outputs are available | Yes |
| Consolidation manifest is present | Strongly recommended |
| Topic is well-bounded (not vague or open-ended) | Yes |
| User wants hands-off consolidation | Yes |
| User has used signal phrases | Helpful |

**Signal phrases**: "agentic consolidation", "autonomous merge", "consolidate without intervention", "full auto", "hands-off consolidation"

### When NOT to Use

| Condition | Reason |
|-----------|--------|
| Highly contested or politically sensitive topics | Human judgment needed for framing decisions |
| Extremely novel domains with sparse information | Risk of confident-sounding confabulation |
| User specifically wants to review intermediate steps | Defeats purpose of autonomous mode |
| Manifest absent AND source outputs are unlabeled | Insufficient metadata for reliable autonomous processing |
| Compliance/regulatory research with legal implications | Human review of interpretations is non-negotiable |

### Workflow: 6-Phase Pipeline

```
PHASE 1: INGEST
├── Parse consolidation manifest (YAML front matter)
├── Validate source completeness against manifest.models[]
│   ├── All expected outputs present → proceed
│   └── Missing outputs → warn user, proceed with available
├── Determine context tier:
│   ├── Total input tokens < 200K → Standard context
│   └── Total input tokens < 1M   → Extended context (summarize if needed)
├── Load pattern-specific output template (from manifest.pattern)
└── Initialize quality_metrics accumulator

PHASE 2: AUTONOMOUS CLAIMS PROCESSING
├── Normalize all inputs:
│   ├── Extract structural artifacts (tables, trees, matrices)
│   ├── Decompose prose into atomic claims
│   └── Tag each claim with: source_model, provenance, citations[]
├── Build claims matrix:
│   │   Rows = claims, Columns = models
│   │   Cells = {supported, contradicted, absent, nuanced}
│   │
│   ├── Assign provenance channel per claim (Section 1)
│   └── Score citations per claim (Section 2)
├── Identify dependency chains (Section 4)
├── Classify each claim:
│   ├── convergent  — 2+ models agree, no dissent
│   ├── majority    — most models agree, some silent
│   ├── unique      — single model, others silent
│   └── contested   — models actively disagree
└── Compute preliminary quality metrics

PHASE 3: CONFLICT RESOLUTION WITH WEB SEARCH
├── FOR EACH contested claim (up to search budget):
│   ├── Formulate verification query:
│   │   ├── Extract key factual assertion
│   │   ├── Add specificity: dates, versions, names
│   │   └── Avoid leading the query toward either position
│   ├── Execute web_search tool
│   ├── Evaluate results:
│   │   ├── RESOLVED: authoritative source confirms one position
│   │   │   ├── Update claim tier
│   │   │   ├── Add provenance: agentic_verification
│   │   │   ├── Record resolution source
│   │   │   └── Annotate: [Agentic checkmark]
│   │   └── UNRESOLVED: no clear resolution OR conflicting web results
│   │       ├── Preserve multi-perspective format
│   │       ├── Annotate: [Unresolved]
│   │       └── If 3 search attempts exhausted → stop trying
│   └── Increment search_counter
│
├── FOR EACH coverage gap:
│   ├── Formulate gap-filling query
│   ├── Execute web_search tool
│   ├── Evaluate results:
│   │   ├── FOUND: relevant information located
│   │   │   ├── Add as new claim with provenance: agentic_gap_fill
│   │   │   ├── Score citation quality (usually 3-4 for web search)
│   │   │   ├── Annotate: [Agentic Fill]
│   │   │   └── Note: "This finding was not in primary research outputs"
│   │   └── NOT FOUND:
│   │       └── Document in Coverage Gaps section of output
│   └── Increment search_counter
│
├── Run citation deduplication pass (Section 3)
└── Enforce search budget: MAX 20 searches total

PHASE 4: SYNTHESIS
├── Cross-domain synthesis pass (MANDATORY):
│   ├── Identify patterns that cross domain boundaries
│   ├── Surface analogies from adjacent fields
│   └── Generate novel connections not in any single source
├── Structural artifact merging (Section 7):
│   ├── Merge tables, matrices, decision trees, timelines
│   └── Preserve source attribution in merged artifacts
├── Dependency chain propagation (Section 4):
│   ├── Walk dependency graph
│   ├── Downgrade claims with weak foundations
│   └── Flag at-risk recommendations
├── Generate "For Downstream" actionability section:
│   └── Pattern-specific deliverables for downstream skills
└── Final false confidence audit on all Tier 1 claims (Section 5)

PHASE 5: OUTPUT GENERATION
├── Select pattern-specific template:
│   └── From manifest.pattern → output-templates.md
├── Populate all sections:
│   ├── Executive Summary (2-3 paragraphs)
│   ├── Pattern-specific core sections
│   ├── Cross-Domain Synthesis
│   ├── Coverage Gaps & Verification Status
│   ├── Methodology Notes (including agentic mode disclosure)
│   └── For Downstream
├── Compute final quality metrics (YAML block):
│   ├── Standard metrics: coverage_ratio, confidence_distribution, etc.
│   └── Agentic metrics: agentic_searches_executed,
│       agentic_resolutions, agentic_gap_fills
└── Generate freshness model (YAML block)

PHASE 6: SELF-REVIEW (Enhanced for Agentic Mode)
├── Standard self-review checks (7 checks):
│   ├── 1. Are all Tier 1 claims actually well-supported?
│   ├── 2. Are contested areas presented without false resolution?
│   ├── 3. Are unique insights preserved with proper attribution?
│   ├── 4. Is the confidence distribution realistic (not all Tier 1)?
│   ├── 5. Are coverage gaps honestly documented?
│   ├── 6. Does the executive summary accurately reflect findings?
│   └── 7. Are structural artifacts properly merged, not flattened?
│
├── Agentic-specific checks (3 additional):
│   ├── 8. "Did any web search finding contradict a previously
│   │       resolved claim? If so, re-evaluate that claim."
│   ├── 9. "Are any gap-filling search results of lower quality
│   │       than primary research outputs? If so, tier them lower
│   │       and annotate appropriately."
│   └── 10. "Would the research brief's author likely agree with
│           how I resolved each conflict? Flag anything where
│           the resolution was a close call as [Close Call]."
│
└── Output self-review summary in report
```

### API Configuration

```yaml
# Agentic consolidation mode — Claude API configuration
model: "claude-opus-4-6"
thinking:
  type: "adaptive"            # Let the model decide when extended thinking helps
effort: "max"                  # Maximum reasoning effort for consolidation quality
max_tokens: 32000              # Default; increase to 128000 for comprehensive reports
tools:
  - type: "web_search_20250305"
    name: "web_search"
# Notes:
#   - Extended thinking is critical for dependency propagation and cross-domain synthesis
#   - web_search tool enables conflict resolution and gap filling
#   - For very large consolidations (3+ model outputs, 500K+ tokens input),
#     consider splitting into two passes: claims processing, then synthesis
```

### Guardrails

| Guardrail | Limit | Rationale |
|-----------|-------|-----------|
| Max verification searches per consolidation | 20 | Prevents runaway search loops; forces prioritization |
| Max search attempts per contested claim | 3 | Diminishing returns after 3 attempts; mark unresolved |
| Gap-fill searches count toward total budget | Yes | Same 20-search budget for all search types |
| All agentic findings get explicit provenance | Always | `agentic_verification` or `agentic_gap_fill` — never unmarked |
| Agentic findings cannot exceed Tier 2 alone | Enforced | Web search during consolidation is supplementary, not primary research |
| Self-review must disclose agentic activity | Always | Transparency: "[N] searches, [M] resolutions, [K] gap fills" |
| Circular search detection | Active | If search results keep pointing to same sources, stop and mark unresolved |

### Budget Allocation Heuristic

```
Given B = 20 total searches:
  contested_claims = count(claims where classification == contested)
  coverage_gaps    = count(identified coverage gaps)

  IF contested_claims + coverage_gaps <= B:
    Allocate 1 search each, remainder for retries
  ELSE:
    Priority order:
      1. Contested claims affecting recommendations (up to 3 attempts each)
      2. Contested factual claims (up to 2 attempts each)
      3. Coverage gaps in high-weight dimensions (1 attempt each)
      4. Remaining coverage gaps (1 attempt each, budget permitting)
```

### Output Annotations

All agentic consolidation outputs must clearly mark the origin of each finding:

| Annotation | Meaning | When Applied |
|------------|---------|--------------|
| `[Agentic ✓]` | Claim resolved via agentic web search | A contested claim where web search confirmed one position |
| `[Agentic Fill]` | Gap filled via agentic search | New information not in any primary research output |
| `[Unresolved]` | Claim resisted resolution despite search attempts | Contested claim where 3 search attempts failed to resolve |
| `[Close Call]` | Resolution was made but with low confidence in the judgment | Self-review Phase 6 check 10 flagged this |

### Agentic Quality Metrics Block

```yaml
# Appended to standard quality_metrics in agentic mode
agentic_metrics:
  mode: agentic
  searches_executed: 14          # out of 20 budget
  searches_for_conflicts: 9      # contested claim resolution
  searches_for_gaps: 5           # coverage gap filling
  conflicts_resolved: 6          # successfully resolved via search
  conflicts_unresolved: 3        # marked [Unresolved]
  gaps_filled: 3                 # new claims added via search
  gaps_unfilled: 2               # documented in Coverage Gaps
  close_calls: 1                 # flagged during self-review
  agentic_claims_tier_distribution:
    tier_2: 8                    # agentic findings capped at Tier 2
    tier_3: 1                    # weak search results
```

### Agentic Mode Self-Review Disclosure Template

```markdown
## Methodology Notes

This consolidation was produced in **agentic mode**. Claude Opus 4.6
performed autonomous conflict resolution and gap filling using web search.

- **Verification searches executed**: [N] of 20 budget
- **Contested claims resolved via search**: [M] (annotated [Agentic ✓])
- **Coverage gaps filled via search**: [K] (annotated [Agentic Fill])
- **Unresolved despite search**: [J] (annotated [Unresolved])
- **Close-call resolutions**: [L] (annotated [Close Call])

All agentic findings are capped at Tier 2 confidence. Primary research
model outputs remain the foundation of Tier 1 claims. Agentic search
findings carry provenance `agentic_verification` or `agentic_gap_fill`
and are explicitly annotated throughout the report.
```

---

## Quick Reference: Section Cross-Dependencies

```
Section 1 (Provenance)
    │
    ├──► Section 2 (Citation Quality) — uses provenance weights
    │       │
    │       ├──► Section 3 (Dedup) — feeds cross-model modifier
    │       │       │
    │       │       └──► Section 6 (Tier Rubric) — uses dedup classification
    │       │
    │       └──► Section 5 (False Confidence Audit) — validates Tier 1 claims
    │               │
    │               └──► Section 6 (Tier Rubric) — audit can downgrade tier
    │
    └──► Section 4 (Dependency Propagation) — post-tier-assignment pass
            │
            └──► Section 6 (Tier Rubric) — propagation can downgrade tier

Section 7 (Artifact Merging) — independent, runs during synthesis

Section 8 (Agentic Mode) — orchestrates Sections 1-7 autonomously
    └── Uses web_search to resolve contested claims (Section 6 re-entry)
    └── Budget-constrained (20 searches max)
    └── Self-review includes agentic-specific checks
```

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-04 | Initial creation: Sections 1-8. Provenance hierarchy, citation rubric, dedup protocol, dependency propagation, false confidence audit, tier rubric, artifact merging, agentic mode. |
