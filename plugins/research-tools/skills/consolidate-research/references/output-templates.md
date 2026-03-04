# Pattern-Specific Consolidated Output Templates

**Version**: 1.0
**Last validated**: 2026-03-04
**Consumed by**: consolidate-research (Step 5: Generate Output)
**Source**: pattern-registry.md (pattern definitions + confidence tiering)

---

## How to Use This File

1. **Identify the research pattern** from the consolidation manifest or infer from research outputs.
2. **Select the matching template** below (1 of 9).
3. **Fill the template** using consolidated findings from Step 4 (Apply Consolidation Mode).
4. **Apply confidence tiering** using the pattern-specific approach described in each template header.
5. **Complete all universal sections** -- every template requires them.

### Universal Sections (present in every template)

Every template contains these sections in order:
- **Executive Summary** (2-3 paragraphs) -- always first
- **Pattern-specific sections** -- the core deliverable, varies per pattern
- **Cross-Domain Synthesis** -- mandatory, never skip
- **Self-Review Results** -- internal consistency audit
- **Coverage Gaps & Verification Status** -- what was missed and what needs checking
- **Quality Metrics** (YAML block) -- quantified assessment
- **For Downstream** -- actionability section with specific target skill/workflow
- **Freshness Model** (YAML block) -- staleness estimates per section
- **Methodology Notes** -- how consolidation was performed

### Confidence Tier Definitions (Universal)

| Tier | Threshold | Meaning |
|------|-----------|---------|
| **Tier 1** | >75% confidence | Cross-source agreement + quality citations + specific/verifiable |
| **Tier 2** | 50-75% confidence | Partial agreement or moderate citations; caveats noted inline |
| **Tier 3** | <50% confidence | Single-source, contested, or poorly cited; requires verification |

Confidence is applied to **pattern-specific artifacts** (see each template header for what gets tiered).

### Contested Areas Format (Universal)

Whenever sources disagree on a substantive claim, use this format:

```
<contested>
**Claude Opus 4.6 view**: [Position + reasoning + web sources]
**Gemini 3.1 Pro view**: [Position + sources]
**GPT-5.2 view**: [Position + site-specific sources]
**Assessment**: [How to interpret; what would resolve it]
</contested>
```

If only 2 models were used (DUAL mode), omit the missing model line.

---

## Template 1: Landscape Mapping

**Pattern ID**: `landscape_mapping`
**Primary Deliverable**: Taxonomy + comprehensive player inventory + white space map
**Default Consolidation Mode**: `breadth_first`
**Confidence Tiering Target**: Category completeness (how thoroughly each category is mapped)

````markdown
# Landscape Map: [TOPIC] in [DOMAIN]

**Research Date**: [DATE]
**Sources**: [MODEL LIST]
**Consolidation Mode**: breadth_first
**Pattern**: landscape_mapping

---

## Executive Summary

[2-3 paragraphs: Total landscape scope, number of categories and players identified, key structural observations, overall confidence in landscape completeness. State the most significant white spaces discovered and the most surprising ecosystem dynamics.]

**Key landscape findings:**
1. **[Finding 1]** -- [One-line summary]
2. **[Finding 2]** -- [One-line summary]
3. **[Finding 3]** -- [One-line summary]

---

## 1. Market/Domain Taxonomy

### 1.1 Taxonomy Overview

<high_confidence>

| Category ID | Category Name | Definition | Player Count | Maturity |
|-------------|---------------|------------|--------------|----------|
| C1 | [Category] | [One-line definition of what belongs here] | [N] | [Emerging / Growing / Mature / Declining] |
| C2 | [Category] | [Definition] | [N] | [Maturity] |
| C3 | [Category] | [Definition] | [N] | [Maturity] |

</high_confidence>

### 1.2 Taxonomy Rationale

**Why these categories, not others:**
- [Rationale for chosen classification axes]
- [Alternative taxonomies considered and why they were rejected]
- [Cross-source agreement on category boundaries]

<moderate_confidence>

**Categories with uncertain boundaries:**
- [Category X]: Boundary with [Category Y] is fuzzy because [reason]. Sources disagree on whether [specific player/approach] belongs in X or Y.

</moderate_confidence>

### 1.3 Taxonomy Confidence Assessment

| Category | Completeness Confidence | Basis |
|----------|------------------------|-------|
| [Category 1] | Tier 1 | Multiple sources enumerate same players; well-established segment |
| [Category 2] | Tier 2 | Players identified but list may be incomplete; emerging segment |
| [Category 3] | Tier 3 | Category suspected from limited signals; player list unverified |

---

## 2. Player Inventory

### 2.1 Category: [Category 1 Name]

**Category completeness**: Tier [1/2/3]

| Player | Description | Founded / Est. | Maturity | Positioning | Funding / Scale | Key Differentiator | Source(s) |
|--------|-------------|----------------|----------|-------------|-----------------|-------------------|-----------|
| [Player A] | [One-line description] | [Year] | [Stage] | [Position summary] | [Funding/revenue/scale indicator] | [What makes them distinct] | [Claude/Gemini/GPT-5.2] |
| [Player B] | [Description] | [Year] | [Stage] | [Position] | [Scale] | [Differentiator] | [Sources] |

<contested>
**Claude Opus 4.6 view**: [Player X] is positioned as [category], based on [evidence].
**Gemini 3.1 Pro view**: [Player X] is better categorized as [different category], because [evidence].
**Assessment**: Classification depends on [factor]. For purposes of this landscape, categorized as [choice] because [reasoning].
</contested>

### 2.2 Category: [Category 2 Name]

**Category completeness**: Tier [1/2/3]

| Player | Description | Founded / Est. | Maturity | Positioning | Funding / Scale | Key Differentiator | Source(s) |
|--------|-------------|----------------|----------|-------------|-----------------|-------------------|-----------|
| [Player] | [Description] | [Year] | [Stage] | [Position] | [Scale] | [Differentiator] | [Sources] |

[Repeat for all categories]

### 2.3 Player Inventory Summary

| Metric | Value |
|--------|-------|
| Total categories | [N] |
| Total players identified | [N] |
| Tier 1 categories (fully mapped) | [N] |
| Tier 2 categories (partially mapped) | [N] |
| Tier 3 categories (suspected/sparse) | [N] |

---

## 3. Market Structure Analysis

### 3.1 Consolidation Trends

<high_confidence>
- [Trend 1: e.g., "Top 3 players hold ~X% of Category A, indicating high concentration"]
- [Trend 2: e.g., "Category B is fragmented with no player exceeding Y% share"]
</high_confidence>

<moderate_confidence>
- [Trend with partial evidence or single-source data]
</moderate_confidence>

### 3.2 Emerging vs. Established Segments

| Segment | Status | Growth Signal | Evidence Quality |
|---------|--------|---------------|-----------------|
| [Segment] | Emerging (< 2 years) | [Signal] | Tier [1/2/3] |
| [Segment] | Established | [Signal] | Tier [1/2/3] |
| [Segment] | Declining | [Signal] | Tier [1/2/3] |

### 3.3 Geographic Distribution

| Region | Concentration | Notable Players | Notes |
|--------|---------------|-----------------|-------|
| [Region] | [High/Medium/Low] | [Key players] | [Context] |

---

## 4. White Space Map

### 4.1 Identified Gaps

| Gap ID | Gap Description | Adjacent Categories | Opportunity Signal | Confidence |
|--------|-----------------|--------------------|--------------------|------------|
| G1 | [Underserved need or missing category] | [Which existing categories border this gap] | [Why this gap matters] | Tier [1/2/3] |
| G2 | [Gap] | [Adjacent] | [Signal] | Tier [1/2/3] |

### 4.2 Underserved Segments

- **[Segment]**: [Description of why it is underserved, evidence, potential]
- **[Segment]**: [Description]

### 4.3 Cross-Domain White Space Patterns

<cross_domain_synthesis>
1. **[Pattern]** (from [adjacent industry/domain]): [How a gap-filling pattern from another domain maps here. Where the analogy holds, where it breaks, and what actionable insight it provides.]
2. **[Pattern]** (from [domain]): [Same structure]

**Emergent gap interactions**: [Gaps that combine to create a larger opportunity not visible from any single gap]
</cross_domain_synthesis>

---

## 5. Ecosystem Relationships

### 5.1 Partnership & Integration Map

| Player A | Player B | Relationship Type | Significance | Source |
|----------|----------|-------------------|-------------|--------|
| [Player] | [Player] | [Integration / Partnership / OEM / Reseller] | [Impact on landscape] | [Source] |

### 5.2 Platform Dynamics

- **Platform players**: [Players creating ecosystem effects through APIs, marketplaces, or developer platforms]
- **Lock-in vectors**: [Where platform dynamics create switching costs]
- **Ecosystem health indicators**: [Developer adoption, partner count, integration breadth]

### 5.3 M&A Activity

| Date | Acquirer | Target | Category Impact | Strategic Signal |
|------|----------|--------|-----------------|-----------------|
| [Date] | [Company] | [Company] | [How this reshapes the category] | [What this signals about market direction] |

---

## Cross-Domain Synthesis

<cross_domain_synthesis>
1. **[Structural pattern]** (from [unrelated domain]): [Mapping to this landscape, where analogy holds/breaks, actionable insight]
2. **[Pattern]** (from [domain]): [Same structure]

**Emergent constraint interactions**: [Non-obvious dynamics from combining multiple landscape observations]
**What conventional framing misses**: [Blind spots in standard landscape analysis of this domain]
**What would need to be true for the consensus view to be wrong**: [Contrarian check]
</cross_domain_synthesis>

---

## Self-Review Results

<self_review>
**Internal contradictions found**: [None / List with resolutions]
**Confidence tier adjustments**: [None / "Category X completeness: Tier Y to Z because..."]
**Reasoning chains that did not survive scrutiny**: [None / List]
**Coverage gaps vs. planned categories**: [None / List with follow-up recommendations]
**Potential biases in landscape construction**: [e.g., US-centric sources, English-language bias, VC-funded player overrepresentation]
</self_review>

---

## Coverage Gaps & Verification Status

| Expected Coverage | Actual Status | Impact | Recommended Action |
|-------------------|---------------|--------|-------------------|
| [Category/area] | [Not covered / Partial / Single-source] | [H/M/L] | [Targeted search / Accept gap / Flag] |

### Verification Checklist

| Priority | Claim to Verify | Method | Status |
|----------|----------------|--------|--------|
| 1 | [Specific claim] | [How to verify] | [Pending] |
| 2 | [Claim] | [Method] | [Pending] |

---

## Quality Metrics

```yaml
quality_metrics:
  pattern: landscape_mapping
  total_categories: [N]
  total_players_identified: [N]
  tier_1_categories: [N]
  tier_2_categories: [N]
  tier_3_categories: [N]
  white_spaces_identified: [N]
  sources_used: [N]
  cross_source_agreement_rate: [0.0-1.0]
  contested_claims: [N]
  coverage_completeness: [0.0-1.0]  # estimated % of real landscape captured
  geographic_coverage: [list of regions covered]
```

---

## For Downstream

**Target**: Comparative Evaluation (shortlist selection)

**Shortlist criteria for evaluation:**
- [Criterion 1 for narrowing to evaluation set]
- [Criterion 2]
- [Criterion 3]

**Recommended evaluation set** (top candidates from landscape):
1. [Player/option] -- selected because [reason]
2. [Player/option] -- selected because [reason]
3. [Player/option] -- selected because [reason]

**Key constraints established:**
- [Constraint from landscape that downstream patterns must respect]
- [Constraint]

**Would change conclusions if:**
- [New major player enters Category X]
- [M&A event consolidates Category Y]

**Recommended refresh trigger**: [Timeframe based on volatility heuristic]

---

## Freshness Model

```yaml
freshness_model:
  pattern: landscape_mapping
  research_date: "[DATE]"
  overall_volatility: "[High/Medium/Low]"
  estimated_shelf_life: "[3/6/12 months]"
  per_section_freshness:
    taxonomy: "[DATE of newest source] -- stable/volatile"
    player_inventory: "[DATE] -- [note: new entrants expected every N months]"
    market_structure: "[DATE] -- [stability note]"
    white_space_map: "[DATE] -- [changes with each new entrant]"
    ecosystem_relationships: "[DATE] -- [M&A activity pace]"
  refresh_triggers:
    - "[Event type that would require re-research]"
    - "[Threshold that indicates staleness]"
```

---

## Methodology Notes

<methodology>
- **Consolidation mode**: breadth_first -- prioritized completeness over depth
- **Sources processed**: [List each model/source with brief characterization]
- **Lead source for inventory**: [Gemini/Claude/etc.] -- selected for [reason]
- **Key conflicts resolved**: [How major classification disagreements were handled]
- **Remaining uncertainties**: [What could not be resolved with available data]
- **Limitations**: [Coverage biases, language limitations, recency gaps]
</methodology>
````

---

## Template 2: Comparative Evaluation

**Pattern ID**: `comparative_evaluation`
**Primary Deliverable**: Weighted evaluation matrix + decision recommendation with sensitivity
**Default Consolidation Mode**: `confidence_weighted`
**Confidence Tiering Target**: Each criterion score per option (individual cell-level confidence)

````markdown
# Comparative Evaluation: [TOPIC] in [DOMAIN]

**Research Date**: [DATE]
**Sources**: [MODEL LIST]
**Consolidation Mode**: confidence_weighted
**Pattern**: comparative_evaluation

---

## Executive Summary

[2-3 paragraphs: Options evaluated, evaluation methodology, primary recommendation with confidence level, key factors driving the recommendation, and conditions under which the recommendation would change.]

**Key evaluation findings:**
1. **[Finding 1]** -- [One-line summary]
2. **[Finding 2]** -- [One-line summary]
3. **[Finding 3]** -- [One-line summary]

---

## 1. Evaluation Framework

### 1.1 Criteria & Weights

| Criterion | Weight | Rationale | Measurability |
|-----------|--------|-----------|---------------|
| [Criterion 1] | [W1]% | [Why this weight] | [How scored: quantitative metric / qualitative rubric] |
| [Criterion 2] | [W2]% | [Rationale] | [Measurability] |
| [Criterion 3] | [W3]% | [Rationale] | [Measurability] |
| **Total** | **100%** | | |

### 1.2 Scoring Methodology

- **Scale**: [e.g., 1-5 or 1-10]
- **Score basis**: [How each score is determined -- benchmark data, feature checklist, expert assessment]
- **Confidence annotation**: Each cell carries a confidence tier indicating evidence quality for that specific score
- **Source attribution**: Each cell notes which model(s) informed the score

### 1.3 Options Under Evaluation

| Option | Category | Why Included | Source of Nomination |
|--------|----------|--------------|---------------------|
| [Option A] | [Category] | [Why it is a candidate] | [Landscape output / user specification / model recommendation] |
| [Option B] | [Category] | [Reason] | [Source] |

---

## 2. Detailed Comparison Matrix

### 2.1 Full Scoring Matrix

| Criterion (Weight) | [Option A] | [Option B] | [Option C] | [Option D] |
|--------------------|------------|------------|------------|------------|
| [Criterion 1] ([W1]%) | Score: [X] / Conf: Tier [N] / Src: [models] | Score: [X] / Conf: Tier [N] / Src: [models] | Score: [X] / Conf: Tier [N] / Src: [models] | Score: [X] / Conf: Tier [N] / Src: [models] |
| [Criterion 2] ([W2]%) | Score / Conf / Src | Score / Conf / Src | Score / Conf / Src | Score / Conf / Src |
| [Criterion 3] ([W3]%) | Score / Conf / Src | Score / Conf / Src | Score / Conf / Src | Score / Conf / Src |
| **Weighted Total** | **[Total]** | **[Total]** | **[Total]** | **[Total]** |

### 2.2 Confidence-Adjusted Scores

| Option | Raw Weighted Score | Confidence-Adjusted Score | Lowest-Confidence High-Weight Cell | Adjustment Rationale |
|--------|-------------------|--------------------------|-----------------------------------|---------------------|
| [Option A] | [Score] | [Adjusted] | [Criterion X: Tier 3] | [Why adjusted] |
| [Option B] | [Score] | [Adjusted] | [Cell] | [Rationale] |

---

## 3. Per-Option Analysis

### 3.1 [Option A]

<high_confidence>
**Strengths (Tier 1 findings):**
- [Strength with evidence and source attribution]
- [Strength]

**Weaknesses (Tier 1 findings):**
- [Weakness with evidence]
- [Weakness]
</high_confidence>

<moderate_confidence>
**Risks (Tier 2 findings):**
- [Risk with caveats]
- [Risk]
</moderate_confidence>

**Unique differentiators:**
- [What sets this option apart, with cross-domain synthesis if applicable]

**Hidden dependencies / second-order effects:**
- [Effects of choosing this option that are not captured in criteria scoring]

### 3.2 [Option B]

[Same structure as 3.1]

### 3.3 [Option C]

[Same structure as 3.1]

---

## 4. Contested Evaluations

Where models disagreed on scoring:

### 4.1 [Criterion X] for [Option Y]

<contested>
**Claude Opus 4.6 view**: Score [N] because [reasoning + web sources]. Key evidence: [specific citation].
**Gemini 3.1 Pro view**: Score [M] because [reasoning + sources]. Key evidence: [citation].
**GPT-5.2 view**: Score [P] because [reasoning + site-specific sources]. Key evidence: [citation].
**Assessment**: Disagreement stems from [root cause -- e.g., different benchmarks, different timeframes, different weighting of sub-factors]. Consolidated score of [X] reflects [resolution approach]. Would be resolved by [specific verification action].
</contested>

### 4.2 [Next contested area]

[Same structure]

---

## 5. Decision Recommendation

### 5.1 Primary Recommendation

<high_confidence>
**Recommended option**: [Option X]
**Confidence level**: [High/Medium/Low]
**Rationale**: [2-3 sentences on why, grounded in matrix results]
**Best for**: [Use case, team profile, or context where this excels]
</high_confidence>

### 5.2 Runner-Up

**Runner-up option**: [Option Y]
**Conditions under which it becomes preferred**:
- If [criterion weight change] -- e.g., "If cost weight increases from 20% to 35%"
- If [new information] -- e.g., "If Option X's pricing model changes to usage-based"
- If [context change] -- e.g., "If team has existing expertise in Option Y's ecosystem"

### 5.3 Decision Sensitivity Analysis

| Criterion | Current Weight | Weight at Which Recommendation Flips | New Winner |
|-----------|---------------|-------------------------------------|------------|
| [Criterion 1] | [W1]% | [Flip threshold]% | [Option Y] |
| [Criterion 2] | [W2]% | [Flip threshold]% | [Option Z] |

**Key insight**: The recommendation is [robust/fragile] because [explanation of how much weights must change to flip the result].

### 5.4 Migration Cost Assessment

| Scenario | Estimated Switching Cost | Timeframe | Risk |
|----------|------------------------|-----------|------|
| Switch from [Option X] to [Option Y] at 6 months | [Cost/effort] | [Time] | [Risk level] |
| Switch from [Option X] to [Option Z] at 12 months | [Cost/effort] | [Time] | [Risk level] |

---

## Cross-Domain Synthesis

<cross_domain_synthesis>
1. **[Pattern]** (from [domain]): [How evaluation patterns from other domains inform this comparison -- e.g., vendor selection patterns from enterprise IT, technology adoption curves from adjacent markets]
2. **[Pattern]** (from [domain]): [Same structure]

**Emergent constraint interactions**: [Criteria that interact in non-obvious ways -- e.g., choosing Option A for performance creates hidden cost implications]
**What conventional evaluation misses**: [Blind spots in standard comparison approaches]
</cross_domain_synthesis>

---

## Self-Review Results

<self_review>
**Internal contradictions found**: [None / List -- e.g., "Option A scored high on ease-of-use but low on documentation quality, which are typically correlated"]
**Confidence tier adjustments**: [None / "Option B's security score: Tier 1 to Tier 2 because single-benchmark basis"]
**Reasoning chains that did not survive scrutiny**: [None / List]
**Coverage gaps vs. evaluation criteria**: [None / List -- criteria that could not be adequately scored]
**Potential evaluation biases**: [e.g., recency bias toward newer options, familiarity bias toward market leaders]
</self_review>

---

## Coverage Gaps & Verification Status

| Expected Coverage | Actual Status | Impact | Recommended Action |
|-------------------|---------------|--------|-------------------|
| [Criterion/option] | [Status] | [H/M/L] | [Action] |

### Verification Checklist

| Priority | Claim to Verify | Method | Status |
|----------|----------------|--------|--------|
| 1 | [Score for Option X on Criterion Y] | [How to verify] | [Pending] |
| 2 | [Pricing claim] | [Check vendor website] | [Pending] |

---

## Quality Metrics

```yaml
quality_metrics:
  pattern: comparative_evaluation
  options_evaluated: [N]
  criteria_count: [N]
  total_matrix_cells: [N]  # options x criteria
  tier_1_cells: [N]
  tier_2_cells: [N]
  tier_3_cells: [N]
  contested_cells: [N]
  recommendation_confidence: "[High/Medium/Low]"
  sensitivity_robustness: "[Robust/Moderate/Fragile]"
  sources_used: [N]
  cross_source_agreement_rate: [0.0-1.0]
```

---

## For Downstream

**Target**: Implementation Pattern (how to build with the selected option)

**Selection rationale** (for Architecture Decision Record):
- **Context**: [Decision context]
- **Decision**: [Option X selected]
- **Consequences**: [Accepted trade-offs]
- **Alternatives rejected**: [Options and why]

**Implementation considerations from evaluation:**
- [Consideration 1 -- e.g., "Option X requires specific infrastructure setup"]
- [Consideration 2 -- e.g., "Key weakness area requires architectural mitigation"]

**Evaluation criteria as success metrics:**
- [Criterion] >= [threshold] -- measures ongoing success of the selection

**Key constraints established:**
- [Constraint]

**Would change conclusions if:**
- [Key assumption proves false]
- [Market event occurs]

**Recommended refresh trigger**: [Timeframe]

---

## Freshness Model

```yaml
freshness_model:
  pattern: comparative_evaluation
  research_date: "[DATE]"
  overall_volatility: "[High/Medium/Low]"
  estimated_shelf_life: "[3/6/12 months]"
  per_section_freshness:
    evaluation_framework: "[DATE] -- criteria weights stable unless priorities change"
    comparison_matrix: "[DATE] -- [note on score volatility per option]"
    per_option_analysis: "[DATE] -- [version-dependent sections flagged]"
    pricing_data: "[DATE] -- [high volatility note]"
    decision_recommendation: "[DATE] -- valid while criteria weights hold"
  refresh_triggers:
    - "Major version release of any evaluated option"
    - "Pricing model change by any evaluated option"
    - "New entrant that would qualify for evaluation"
```

---

## Methodology Notes

<methodology>
- **Consolidation mode**: confidence_weighted -- evidence quality determines score reliability
- **Sources processed**: [List with characterization]
- **Scoring approach**: [How raw scores were derived and consolidated across sources]
- **Key conflicts resolved**: [How scoring disagreements were reconciled]
- **Remaining uncertainties**: [Cells or criteria with unresolved low confidence]
- **Limitations**: [Evaluation scope limitations, criteria not included, options not evaluated]
</methodology>
````

---

## Template 3: Implementation Pattern

**Pattern ID**: `implementation_pattern`
**Primary Deliverable**: Architecture decision catalog + pattern catalog + anti-pattern register + decision trees
**Default Consolidation Mode**: `depth_first`
**Confidence Tiering Target**: Each architecture decision and pattern recommendation (production-validation level)

````markdown
# Implementation Patterns: [TOPIC] in [DOMAIN]

**Research Date**: [DATE]
**Sources**: [MODEL LIST]
**Consolidation Mode**: depth_first
**Pattern**: implementation_pattern

---

## Executive Summary

[2-3 paragraphs: Architecture approach, number of key decisions documented, most critical patterns identified, most dangerous anti-patterns, and overall implementation confidence. State the decision with the highest impact and the anti-pattern with the highest risk.]

**Key implementation findings:**
1. **[Finding 1]** -- [One-line summary]
2. **[Finding 2]** -- [One-line summary]
3. **[Finding 3]** -- [One-line summary]

---

## 1. Architecture Decisions

Each decision follows the ADR format: Context, Options, Decision, Consequences.

### AD-1: [Decision Title]

**Context**: [What situation or requirement drives this decision]

**Options considered**:

| Option | Pros | Cons | Production Evidence |
|--------|------|------|-------------------|
| [Option A] | [Pros] | [Cons] | [Where this has been validated in production] |
| [Option B] | [Pros] | [Cons] | [Evidence] |
| [Option C] | [Pros] | [Cons] | [Evidence] |

<high_confidence>
**Decision**: [Chosen approach]
**Rationale**: [Why this option, grounded in evidence]
**Confidence**: Tier 1 -- validated by multiple production deployments
</high_confidence>

**Consequences**:
- Accepted trade-off: [What you give up]
- Architectural commitment: [What becomes harder to change]
- Downstream impact: [How this constrains future decisions]

### AD-2: [Decision Title]

[Same structure]

<moderate_confidence>
**Decision**: [Chosen approach]
**Rationale**: [Reasoning with limited production evidence]
**Confidence**: Tier 2 -- used in production but limited evidence of scale
</moderate_confidence>

### AD-3: [Decision Title]

[Same structure -- Tier 3 for theoretically sound but unvalidated decisions]

### Architecture Decision Summary

| ID | Decision | Confidence | Key Trade-off | Reversibility |
|----|----------|------------|---------------|---------------|
| AD-1 | [Decision] | Tier [N] | [Trade-off] | [High/Medium/Low] |
| AD-2 | [Decision] | Tier [N] | [Trade-off] | [Reversibility] |

---

## 2. Implementation Pattern Catalog

Organized by implementation phase/component.

### Phase: [Phase 1 -- e.g., Foundation / Setup / Core Architecture]

#### Pattern: [Pattern Name]

**Context**: When to use this pattern
**Problem**: What problem it solves
**Solution**: How experienced practitioners implement it
**Trade-offs**: What you gain vs. what you sacrifice
**Confidence**: Tier [1/2/3] -- [basis: multiple production cases / limited evidence / theoretical]

```
[Code example or architecture diagram in ASCII, if sources provided them]
```

**Source(s)**: [Which model(s) identified this pattern, with citations]

#### Pattern: [Pattern Name]

[Same structure]

### Phase: [Phase 2 -- e.g., Data Layer / Integration / API Design]

[Same structure per pattern]

### Phase: [Phase 3 -- e.g., Scaling / Optimization / Production Hardening]

[Same structure per pattern]

---

## 3. Anti-Pattern Register

### AP-1: [Anti-Pattern Name]

**Severity**: [CRITICAL / MAJOR / MINOR]
**What developers do**: [The common mistake -- specific behavior, not vague]
**Why it fails**: [Root cause and mechanism -- at what scale, through what path]
**Detection signals**: [How to spot this in existing code or architecture]
**Correct approach**: [What to do instead, with brief rationale]
**Confidence**: Tier [1/2/3]
**Source(s)**: [Models and citations]

### AP-2: [Anti-Pattern Name]

[Same structure]

### Anti-Pattern Summary

| ID | Name | Severity | Failure Mechanism | Detection Difficulty |
|----|------|----------|-------------------|---------------------|
| AP-1 | [Name] | [CRITICAL/MAJOR/MINOR] | [One-line mechanism] | [Easy/Medium/Hard to detect] |
| AP-2 | [Name] | [Severity] | [Mechanism] | [Difficulty] |

<contested>
**Claude Opus 4.6 view**: [Anti-pattern X] is critical because [reasoning].
**Gemini 3.1 Pro view**: [Anti-pattern X] is only major severity because [reasoning with different evidence].
**Assessment**: Severity depends on [factor]. Classified as [chosen severity] because [resolution]. Teams with [context] should treat as [alternative severity].
</contested>

---

## 4. Decision Trees

### DT-1: [Decision Point -- e.g., "Choosing between sync and async processing"]

```
[Primary condition]?
  |-- Yes --> [Sub-condition]?
  |             |-- Yes --> [Approach A] because [reason]
  |             |           Source: [model(s)]
  |             |-- No  --> [Approach B] because [reason]
  |                         Source: [model(s)]
  |-- No  --> [Sub-condition]?
                |-- Yes --> [Approach C] because [reason]
                |-- No  --> [Approach D] because [reason]
```

**Key decision factors**: [What matters most at each branch point]
**Confidence**: Tier [1/2/3] per branch

### DT-2: [Decision Point]

[Same structure]

---

## 5. Operational Considerations

### 5.1 Deployment Patterns

| Pattern | Use When | Complexity | Risk Level | Source |
|---------|----------|------------|------------|--------|
| [Pattern] | [Context] | [H/M/L] | [H/M/L] | [Model(s)] |

### 5.2 Monitoring Requirements

| What to Monitor | Why | Threshold / Alert | Priority |
|-----------------|-----|-------------------|----------|
| [Metric] | [What it indicates] | [Threshold] | [P1/P2/P3] |

### 5.3 Cost Implications of Architectural Choices

| Decision | Cost Driver | Estimated Impact | Scaling Behavior |
|----------|-------------|-----------------|------------------|
| [AD reference] | [What drives cost] | [Magnitude] | [Linear/Exponential/Step-function] |

---

## Cross-Domain Synthesis

<cross_domain_synthesis>
1. **[Pattern]** (from [domain]): [How implementation patterns from other technology domains inform this architecture -- e.g., event sourcing patterns from financial systems, resilience patterns from distributed systems]
2. **[Pattern]** (from [domain]): [Same structure]

**Emergent constraint interactions**: [Architecture decisions that interact to create non-obvious constraints]
**What conventional implementation misses**: [Aspects that only become visible through cross-domain lens]
</cross_domain_synthesis>

---

## Self-Review Results

<self_review>
**Internal contradictions found**: [None / List -- e.g., "AD-2 recommends async but Pattern X assumes sync processing"]
**Confidence tier adjustments**: [None / Adjustments made during review]
**Reasoning chains that did not survive scrutiny**: [None / List]
**Coverage gaps vs. implementation scope**: [None / Architectural areas not addressed]
**Bias check**: [Whether patterns reflect specific technology ecosystem bias]
</self_review>

---

## Coverage Gaps & Verification Status

| Expected Coverage | Actual Status | Impact | Recommended Action |
|-------------------|---------------|--------|-------------------|
| [Architecture area] | [Status] | [H/M/L] | [Action] |

---

## Quality Metrics

```yaml
quality_metrics:
  pattern: implementation_pattern
  architecture_decisions: [N]
  patterns_cataloged: [N]
  anti_patterns_registered: [N]
  decision_trees: [N]
  tier_1_decisions: [N]
  tier_2_decisions: [N]
  tier_3_decisions: [N]
  critical_anti_patterns: [N]
  code_examples_included: [N]
  sources_used: [N]
  cross_source_agreement_rate: [0.0-1.0]
```

---

## For Downstream

**Target**: Foundry (requirements generation)

**Architecture Decision Log** (ready for Foundry ADR import):
- AD-1: [Decision summary]
- AD-2: [Decision summary]

**Implementation Checklist** (ordered by dependency):
- [ ] [Step 1 -- from AD-1]
- [ ] [Step 2 -- from Pattern X]
- [ ] [Step 3 -- from AD-2]
- [ ] [Validation gate -- from AP-1 detection]

**Anti-pattern acceptance criteria** (negative requirements):
- System MUST NOT exhibit [AP-1 behavior]
- System MUST NOT exhibit [AP-2 behavior]

**Key constraints established:**
- [Architectural constraint from decisions]

**Would change conclusions if:**
- [Technology releases new version with different architecture model]
- [Scale requirements change by order of magnitude]

**Recommended refresh trigger**: [Timeframe]

---

## Freshness Model

```yaml
freshness_model:
  pattern: implementation_pattern
  research_date: "[DATE]"
  overall_volatility: "[High/Medium/Low]"
  estimated_shelf_life: "[3/6/12 months]"
  per_section_freshness:
    architecture_decisions: "[DATE] -- [stability note per decision]"
    pattern_catalog: "[DATE] -- [API/version dependency note]"
    anti_pattern_register: "[DATE] -- [new anti-patterns emerge with adoption]"
    decision_trees: "[DATE] -- [branch conditions may change with releases]"
    operational_considerations: "[DATE] -- [pricing/scaling changes]"
  refresh_triggers:
    - "Major version release of core technology"
    - "Production incident revealing new anti-pattern"
    - "Architecture scale threshold crossed"
```

---

## Methodology Notes

<methodology>
- **Consolidation mode**: depth_first -- prioritized WHY patterns work over WHAT patterns exist
- **Lead source for reasoning**: [Claude/analyst] -- selected for architectural depth
- **Sources processed**: [List]
- **Key conflicts resolved**: [How pattern disagreements were reconciled]
- **Remaining uncertainties**: [Decisions with insufficient production evidence]
- **Limitations**: [Stack-specific constraints, scale assumptions, team-size assumptions]
</methodology>
````

---

## Template 4: Best Practices (8-Dimension)

**Pattern ID**: `best_practices`
**Primary Deliverable**: 8-dimension technology knowledge base + Quick Reference Card
**Default Consolidation Mode**: `gap_driven`
**Confidence Tiering Target**: Per dimension (how thoroughly each dimension is covered)

This template extends the existing 8-dimension structure from create-research-brief with quality metrics, freshness model, source provenance, and downstream sections.

````markdown
# Best Practices Knowledge Base: [TOPIC]

**Research Date**: [DATE]
**Sources**: [MODEL LIST]
**Consolidation Mode**: gap_driven
**Pattern**: best_practices
**Downstream use**: [Claude Code skill / code generation / team reference]

---

## Executive Summary

[2-3 paragraphs: Key takeaways, current state of the technology, most critical things a practitioner must know. Highlight which dimensions are strongest (Tier 1) and which have gaps (Tier 3).]

**Critical practitioner knowledge:**
1. **[Finding 1]** -- [One-line summary]
2. **[Finding 2]** -- [One-line summary]
3. **[Finding 3]** -- [One-line summary]

---

## 1. Environmental Context & Setup

**Dimension confidence**: Tier [1/2/3]
**Source provenance**: [Which models contributed, primary citations]

<high_confidence>
**Runtime**: [Version(s), requirements]
**Project Structure**: [Recommended layout]
**Configuration**:
- [Key config items with recommended values and rationale]
</high_confidence>

<moderate_confidence>
**IAM / Authentication**: [Platform-specific auth patterns]
**Secrets Management**: [How to handle secrets properly]
</moderate_confidence>

**Gap between tutorials and production**:
- [Setup decisions with downstream consequences developers miss]

---

## 2. Idiomatic Patterns

**Dimension confidence**: Tier [1/2/3]
**Source provenance**: [Models and citations]

#### Pattern: [Pattern Name]
**Context**: When to use this pattern
**Implementation**: How experienced practitioners implement it
**Why this way**: The reasoning behind the idiomatic approach (mechanism, not just convention)
**Performance impact**: Measurable difference vs. naive approach
**Source**: [Model(s) + citation]

#### Pattern: [Pattern Name]
[Repeat structure]

<contested>
**Claude Opus 4.6 view**: [Pattern X is idiomatic because...]
**Gemini 3.1 Pro view**: [Pattern Y is preferred by community because...]
**Assessment**: [Resolution or context-dependent guidance]
</contested>

---

## 3. Anti-Patterns & Guardrails

**Dimension confidence**: Tier [1/2/3]
**Source provenance**: [Models and citations]

#### Anti-Pattern: [Name]
**What developers do**: [The common mistake]
**Why it fails**: [Root cause -- at what scale, through what mechanism]
**Correct approach**: [What to do instead]
**Detection**: [How to spot this in existing code]
**Severity**: [CRITICAL / MAJOR / MINOR]
**Source**: [Model(s) + citation]

[Repeat for each anti-pattern]

---

## 4. Testing & Validation

**Dimension confidence**: Tier [1/2/3]
**Source provenance**: [Models and citations]

**Unit Testing**: [Framework, patterns, mocking approach]
**Integration Testing**: [Emulator/service setup, test patterns]
**Pre-Deploy Validation**: [Checks to run before deploying]
**Known Test Gaps**: [What is hard or impossible to test locally]

| Test Type | Tool/Approach | Fidelity | Setup Complexity | CI-Friendly |
|-----------|---------------|----------|------------------|-------------|
| [Type] | [Tool] | [H/M/L] | [H/M/L] | [Yes/No] |

---

## 5. Dependencies & Version Management

**Dimension confidence**: Tier [1/2/3]
**Source provenance**: [Models and citations]

| Package | Recommended Version | Purpose | Notes |
|---------|-------------------|---------|-------|
| [pkg] | [version] | [purpose] | [compatibility notes] |

**Packages to Avoid**: [List with reasons]
**Version Pinning Strategy**: [Approach and rationale]
**Fragility Points**: [Where version mismatches cause silent failures]

---

## 6. Operational Awareness

**Dimension confidence**: Tier [1/2/3]
**Source provenance**: [Models and citations]

**Logging**: [Platform-specific conventions and structured logging format]
**Cost Model**: [Key cost drivers, optimization strategies, surprises]
**Scaling**: [Behavior under load, concurrency limits, timeout ceilings]
**Cold Start**: [Mitigation strategies -- if applicable]
**Monitoring**: [What to monitor, recommended alerting thresholds]

| Resource | Default Limit | Maximum | Cost Optimization |
|----------|---------------|---------|-------------------|
| [Resource] | [Default] | [Max] | [Tip] |

---

## 7. Decision Trees

**Dimension confidence**: Tier [1/2/3]
**Source provenance**: [Models and citations]

#### Decision: [Decision Name]
```
[Condition A]?
  |-- Yes --> [Approach 1] because [reason]
  |-- No  --> [Condition B]?
               |-- Yes --> [Approach 2] because [reason]
               |-- No  --> [Approach 3] because [reason]
```

**Source(s)**: [Model(s) with citations]

[Repeat for each key architectural decision]

---

## 8. Escape Hatches & Known Issues

**Dimension confidence**: Tier [1/2/3]
**Source provenance**: [Models and citations]

**Staleness warning**: This dimension has the HIGHEST staleness risk. Source dates noted per issue.

#### Issue: [Description]
**Status**: [Open bug / documented limitation / undocumented behavior]
**Workaround**: [Current workaround]
**Expiration**: [When this may be resolved -- version, timeline, or "indefinite"]
**Source**: [Where identified -- GitHub issue link, community report]
**Last confirmed**: [Date]

[Repeat for each known issue]

---

## Integration Patterns

| Paired Service | Pattern | Key Considerations | Source |
|---------------|---------|-------------------|--------|
| [Service A] | [How they connect] | [Considerations] | [Model(s)] |

---

## Quick Reference Card

**Do**:
- [Most critical "do" items -- max 7]

**Do not**:
- [Most critical "don't" items -- max 7]

**Check First**:
- [Items to verify before starting -- max 5]

---

## Cross-Domain Synthesis

<cross_domain_synthesis>
1. **[Pattern]** (from [domain]): [How it maps, where analogy holds/breaks, actionable insight]
2. **[Pattern]** (from [domain]): [Same structure]

**Emergent constraint interactions**: [Non-obvious interactions across dimensions creating implications not in any individual section]
**What conventional framing misses**: [Blind spots in standard thinking about this technology]
</cross_domain_synthesis>

---

## Self-Review Results

<self_review>
**Internal contradictions found**: [None / List with resolutions]
**Confidence tier adjustments**: [None / "Dimension X: Tier Y to Z because..."]
**Reasoning chains that did not survive scrutiny**: [None / List]
**Coverage gaps vs. 8 dimensions**: [None / List with follow-up]
**Dimension weighting appropriateness**: [Whether weights matched technology family profile]
</self_review>

---

## Coverage Gaps & Verification Status

| Dimension | Expected Coverage | Actual Status | Impact | Action |
|-----------|-------------------|---------------|--------|--------|
| [Dim N] | [Expected] | [Actual] | [H/M/L] | [Action] |

---

## Quality Metrics

```yaml
quality_metrics:
  pattern: best_practices
  dimensions_covered: [N] / 8
  tier_1_dimensions: [N]
  tier_2_dimensions: [N]
  tier_3_dimensions: [N]
  patterns_documented: [N]
  anti_patterns_documented: [N]
  decision_trees_documented: [N]
  known_issues_cataloged: [N]
  code_examples_included: [N]
  sources_used: [N]
  cross_source_agreement_rate: [0.0-1.0]
  gap_driven_audit_score: [0.0-1.0]  # coverage vs. expected
```

---

## For Downstream

**Target**: Claude Code skill generation (research-to-rules-transformer)

**Skill-ready knowledge base**:
- Anti-patterns framed as reasoning-based rules ("X causes Y at Z scale")
- Code snippets for idiomatic patterns (copy-ready)
- Decision trees as conditional logic
- Version stamps for skill freshness awareness

**Quick Reference Card** (skill preamble candidate):
- See Quick Reference Card section above

**Key constraints established:**
- [Constraint 1]
- [Constraint 2]

**Would change conclusions if:**
- [New version released with breaking changes]
- [Community consensus shifts on pattern X]

**Recommended refresh trigger**: [Timeframe from technology profile volatility]

---

## Freshness Model

```yaml
freshness_model:
  pattern: best_practices
  research_date: "[DATE]"
  overall_volatility: "[High/Medium/Low]"
  estimated_shelf_life: "[3/6/12 months]"
  per_dimension_freshness:
    environmental_context: "[DATE] -- [stability note]"
    idiomatic_patterns: "[DATE] -- [patterns stable/evolving]"
    anti_patterns: "[DATE] -- [new anti-patterns with adoption growth]"
    testing: "[DATE] -- [testing tooling evolution pace]"
    dependencies: "[DATE] -- HIGH volatility, check monthly"
    operational: "[DATE] -- [pricing/limits change pace]"
    decision_trees: "[DATE] -- [decision criteria stability]"
    escape_hatches: "[DATE] -- HIGHEST volatility, check with each release"
  refresh_triggers:
    - "Major or minor version release"
    - "Community sentiment shift on key pattern"
    - "New escape hatch / critical bug report"
```

---

## Methodology Notes

<methodology>
- **Consolidation mode**: gap_driven -- audited coverage against all 8 dimensions
- **Technology family weighting**: [Which dimensions weighted heavily and why]
- **Sources processed**: [List with characterization]
- **Key conflicts resolved**: [How practice disagreements were reconciled]
- **Remaining uncertainties**: [Dimensions with insufficient coverage]
- **Limitations**: [Version-specific, platform-specific, scale assumptions]
</methodology>
````

---

## Template 5: Competitive Intelligence

**Pattern ID**: `competitive_intelligence`
**Primary Deliverable**: Per-competitor strategic profiles + competitive dynamics + positioning recommendations
**Default Consolidation Mode**: `adversarial`
**Confidence Tiering Target**: Each strategic claim per competitor (evidence quality for strategic assertions)

````markdown
# Competitive Intelligence: [TOPIC] in [DOMAIN]

**Research Date**: [DATE]
**Sources**: [MODEL LIST]
**Consolidation Mode**: adversarial
**Pattern**: competitive_intelligence

---

## Executive Summary

[2-3 paragraphs: Competitive landscape overview, most defensible positions, most vulnerable competitors, key competitive dynamics reshaping the space, and strategic implications for the user. Note where adversarial audit revealed false confidence in comfortable narratives.]

**Key competitive findings:**
1. **[Finding 1]** -- [One-line summary]
2. **[Finding 2]** -- [One-line summary]
3. **[Finding 3]** -- [One-line summary]

---

## 1. Competitive Landscape Overview

### 1.1 Market Positioning Map

```
                    [Axis 1 Label: e.g., Enterprise Focus]
                    ^
                    |
         [Player C] |          [Player A]
                    |
    ----------------+-------------------> [Axis 2 Label: e.g., Platform Breadth]
                    |
         [Player D] |          [Player B]
                    |
```

**Axis rationale**: [Why these axes were chosen as the most differentiating dimensions]
**Positioning confidence**: Tier [1/2/3]

### 1.2 Segment Leaders

| Segment | Leader(s) | Share Estimate | Confidence | Basis |
|---------|-----------|---------------|------------|-------|
| [Segment] | [Player(s)] | [%] | Tier [N] | [Data source] |

---

## 2. Per-Competitor Analysis

### 2.1 [Competitor A]

#### Strategy Assessment
<high_confidence>
**Current strategy**: [Description of strategic direction with evidence]
**Business model**: [Revenue model, pricing approach, GTM motion]
</high_confidence>

#### Moat Analysis

| Moat Dimension | Assessment | Durability | Confidence |
|----------------|------------|------------|------------|
| **Network effects** | [Present/Absent -- evidence] | [Years] | Tier [N] |
| **Switching costs** | [Assessment] | [Durability] | Tier [N] |
| **Brand/trust** | [Assessment] | [Durability] | Tier [N] |
| **Data advantage** | [Assessment] | [Durability] | Tier [N] |
| **Technology IP** | [Assessment] | [Durability] | Tier [N] |
| **Scale economies** | [Assessment] | [Durability] | Tier [N] |

<moderate_confidence>
**Recent strategic moves**: [Actions observed -- product launches, hires, partnerships, with dates and sources]
</moderate_confidence>

#### Strengths, Vulnerabilities, Next Moves

**Strengths** (Tier 1):
- [Strength with evidence]

**Vulnerabilities** (with confidence):
- [Vulnerability -- Tier N] -- [Evidence and mechanism]

**Likely next moves** (12-month horizon):
- [Predicted move -- Tier N] -- [Signal basis: hiring patterns, patent filings, product gaps]

<contested>
**Claude Opus 4.6 view**: [Competitor A] will likely [move] because [reasoning from web research].
**Gemini 3.1 Pro view**: [Competitor A] is more likely to [alternative] because [different evidence].
**GPT-5.2 view**: Recent signals suggest [yet another trajectory] based on [site-specific sources].
**Assessment**: [Resolution or honest uncertainty statement. What would resolve this.]
</contested>

### 2.2 [Competitor B]

[Same structure as 2.1]

### 2.3 [Competitor C]

[Same structure as 2.1]

---

## 3. Feature/Capability Matrix

| Capability | [Competitor A] | [Competitor B] | [Competitor C] | [Our Position] | Conf. |
|------------|---------------|---------------|---------------|----------------|-------|
| [Cap 1] | [Rating + notes] | [Rating] | [Rating] | [Rating] | Tier [N] |
| [Cap 2] | [Rating] | [Rating] | [Rating] | [Rating] | Tier [N] |

**Matrix provenance**: [Which sources informed each column; cells with single-source basis flagged]

---

## 4. Pricing & Business Model Comparison

| Dimension | [Competitor A] | [Competitor B] | [Competitor C] |
|-----------|---------------|---------------|---------------|
| **Model type** | [Subscription/Usage/Freemium/etc.] | [Type] | [Type] |
| **Entry price** | [Price] | [Price] | [Price] |
| **Enterprise price** | [Price/range] | [Price] | [Price] |
| **Hidden costs** | [What customers miss] | [Hidden costs] | [Hidden costs] |
| **Price trend** | [Direction + evidence] | [Trend] | [Trend] |

**Pricing data confidence**: Tier [1/2/3] -- [basis: public pricing pages, analyst reports, customer reports]

---

## 5. Competitive Dynamics

### 5.1 Structural Forces

<high_confidence>
- [Force 1: e.g., "Feature convergence -- top 3 players now offer 80% of the same capabilities"]
- [Force 2: e.g., "Pricing pressure from open-source alternatives"]
</high_confidence>

### 5.2 Potential Disruption Vectors

<moderate_confidence>
- [Disruption vector with evidence and timeline estimate]
- [Vector]
</moderate_confidence>

### 5.3 Cross-Domain Competitive Patterns

<cross_domain_synthesis>
1. **[Pattern]** (from [industry]): [How competitive dynamics from another industry map here -- e.g., platform commoditization from cloud computing, winner-take-all dynamics from social networks]
2. **[Pattern]** (from [industry]): [Same structure]
</cross_domain_synthesis>

### 5.4 Competitive Scenarios (12-month horizon)

| Scenario | Trigger | Likelihood | Impact | Our Response |
|----------|---------|-----------|--------|-------------|
| [Scenario A: e.g., "Competitor A acquires Competitor D"] | [What would trigger this] | [H/M/L] | [Impact description] | [Recommended response] |
| [Scenario B] | [Trigger] | [Likelihood] | [Impact] | [Response] |
| [Scenario C] | [Trigger] | [Likelihood] | [Impact] | [Response] |

---

## Cross-Domain Synthesis

<cross_domain_synthesis>
1. **[Structural pattern]** (from [unrelated domain]): [Mapping, where analogy holds/breaks, actionable insight]
2. **[Pattern]** (from [domain]): [Same structure]

**Emergent competitive dynamics**: [Non-obvious interactions between competitor strategies]
**What the comfortable narrative misses**: [Adversarial audit findings -- where consensus is wrong or overconfident]
**What would need to be true for the consensus view to be wrong**: [Explicit contrarian check]
</cross_domain_synthesis>

---

## Self-Review Results

<self_review>
**Internal contradictions found**: [None / List]
**Confidence tier adjustments**: [None / Adjustments from adversarial audit]
**False confidence audit results**: [Which comfortable narratives were downgraded]
**Reasoning chains that did not survive scrutiny**: [None / List]
**Coverage gaps vs. competitor set**: [None / Competitors insufficiently analyzed]
**Potential biases**: [Pro-incumbent bias, narrative bias, recency bias]
</self_review>

---

## Coverage Gaps & Verification Status

| Expected Coverage | Actual Status | Impact | Recommended Action |
|-------------------|---------------|--------|-------------------|
| [Competitor/area] | [Status] | [H/M/L] | [Action] |

---

## Quality Metrics

```yaml
quality_metrics:
  pattern: competitive_intelligence
  competitors_analyzed: [N]
  moat_dimensions_assessed: [N per competitor]
  tier_1_strategic_claims: [N]
  tier_2_strategic_claims: [N]
  tier_3_strategic_claims: [N]
  contested_claims: [N]
  false_confidence_downgrades: [N]  # adversarial audit result
  scenarios_developed: [N]
  feature_matrix_cells: [N]
  sources_used: [N]
  cross_source_agreement_rate: [0.0-1.0]
```

---

## For Downstream

**Target**: Ignite (GTM strategy)

**Positioning strategy inputs:**
- Strongest differentiation axes: [List]
- Competitor vulnerabilities to exploit: [List]
- Positioning to avoid (competitor strongholds): [List]

**Differentiation matrix** (ready for Ignite):

| Dimension | Our Position | Strongest Competitor | Gap / Advantage |
|-----------|-------------|---------------------|-----------------|
| [Dimension] | [Position] | [Competitor + position] | [Our advantage or gap] |

**Key constraints established:**
- [Competitive constraint that downstream must respect]

**Would change conclusions if:**
- [M&A event]
- [New entrant with specific capability]

**Recommended refresh trigger**: [Timeframe]

---

## Freshness Model

```yaml
freshness_model:
  pattern: competitive_intelligence
  research_date: "[DATE]"
  overall_volatility: "[High/Medium/Low]"
  estimated_shelf_life: "[3/6/12 months]"
  per_section_freshness:
    positioning_map: "[DATE] -- [repositioning pace]"
    per_competitor_analysis: "[DATE] -- [per-competitor volatility note]"
    feature_matrix: "[DATE] -- [release cadence note]"
    pricing: "[DATE] -- HIGH volatility, check quarterly"
    competitive_dynamics: "[DATE] -- [structural change pace]"
    scenarios: "[DATE] -- scenarios expire with each major market event"
  refresh_triggers:
    - "Competitor funding round or M&A"
    - "Competitor major product launch"
    - "Pricing model change by any competitor"
    - "New market entrant at scale"
```

---

## Methodology Notes

<methodology>
- **Consolidation mode**: adversarial -- stress-tested alignment; applied false confidence audit
- **Sources processed**: [List]
- **Adversarial audit summary**: [How many claims were downgraded, which narratives were challenged]
- **Key conflicts resolved**: [How strategic assessment disagreements were reconciled]
- **Remaining uncertainties**: [Competitor strategies that could not be determined]
- **Limitations**: [Public data only, no insider knowledge, inference-based predictions]
</methodology>
````

---

## Template 6: Market Research

**Pattern ID**: `market_research`
**Primary Deliverable**: Market sizing (TAM/SAM/SOM) + segmentation + dynamics + entry strategy
**Default Consolidation Mode**: `standard`
**Confidence Tiering Target**: Market sizing estimates and segment boundaries (quantitative precision)

````markdown
# Market Research: [TOPIC] in [DOMAIN]

**Research Date**: [DATE]
**Sources**: [MODEL LIST]
**Consolidation Mode**: standard
**Pattern**: market_research

---

## Executive Summary

[2-3 paragraphs: Market size summary with confidence ranges (never point estimates), most attractive segments, key dynamics shaping the market, and strategic implications. State the single most important market insight and the area of greatest uncertainty.]

**Key market findings:**
1. **[Finding 1]** -- [One-line summary]
2. **[Finding 2]** -- [One-line summary]
3. **[Finding 3]** -- [One-line summary]

---

## 1. Market Definition & Sizing

### 1.1 Market Definition

**Market boundaries**: [What is included and excluded from this market definition]
**Definition rationale**: [Why these boundaries, not broader or narrower]
**Definition confidence**: Tier [1/2/3]

### 1.2 TAM / SAM / SOM

| Metric | Low Estimate | Base Estimate | High Estimate | CAGR | Confidence | Source(s) |
|--------|-------------|---------------|---------------|------|------------|-----------|
| **TAM** | $[X]B | $[Y]B | $[Z]B | [N]% | Tier [1/2/3] | [Sources] |
| **SAM** | $[X]B | $[Y]B | $[Z]B | [N]% | Tier [1/2/3] | [Sources] |
| **SOM** | $[X]M | $[Y]M | $[Z]M | [N]% | Tier [1/2/3] | [Sources] |

<high_confidence>
**Sizing rationale**: [Methodology -- top-down from industry reports, bottom-up from unit economics, or both]
</high_confidence>

<contested>
**Claude Opus 4.6 view**: TAM is approximately $[X]B based on [methodology + sources].
**Gemini 3.1 Pro view**: TAM is approximately $[Y]B based on [different methodology + sources].
**GPT-5.2 view**: Recent analyst reports suggest $[Z]B based on [site-specific sources].
**Assessment**: Discrepancy of [N]% stems from [different market definitions / different methodologies / different base years]. Range of $[Low]-$[High]B is the defensible estimate.
</contested>

### 1.3 Sizing Methodology

<methodology>
- **Approach**: [Top-down / Bottom-up / Triangulated]
- **Base year**: [Year]
- **Key assumptions**: [List numbered assumptions]
- **Sensitivity**: [Which assumptions most affect the estimate]
</methodology>

### 1.4 Growth Projections

| Year | Market Size (Base) | Growth Rate | Key Driver |
|------|-------------------|-------------|------------|
| [Current] | $[X] | -- | -- |
| [+1 year] | $[X] | [N]% | [Driver] |
| [+3 years] | $[X] | [N]% CAGR | [Driver] |
| [+5 years] | $[X] | [N]% CAGR | [Driver] |

---

## 2. Market Segmentation

### 2.1 Segment Framework

| Segment | Definition | Size | Growth Rate | Attractiveness | Confidence |
|---------|------------|------|-------------|---------------|------------|
| [Segment A] | [Who/what belongs here] | $[X] | [N]% | [H/M/L] | Tier [N] |
| [Segment B] | [Definition] | $[X] | [N]% | [Attractiveness] | Tier [N] |
| [Segment C] | [Definition] | $[X] | [N]% | [Attractiveness] | Tier [N] |

### 2.2 Segment Attractiveness Ranking

| Rank | Segment | Score | Key Criteria | Rationale |
|------|---------|-------|-------------|-----------|
| 1 | [Segment] | [Score] | [Criteria driving rank] | [Why most attractive] |
| 2 | [Segment] | [Score] | [Criteria] | [Rationale] |

**Attractiveness criteria**: [List the criteria used -- e.g., size, growth, competition intensity, alignment with capabilities, barriers to entry]

### 2.3 Segment Dynamics

For each segment:
- **[Segment A]**: [2-3 sentences on trends, shifts, and emerging dynamics within this segment]
- **[Segment B]**: [Same]

---

## 3. Market Dynamics

### 3.1 Demand Drivers

<high_confidence>
| Driver | Impact | Timeframe | Evidence |
|--------|--------|-----------|----------|
| [Driver 1] | [H/M/L] | [Short/Medium/Long-term] | [Sources and data] |
| [Driver 2] | [Impact] | [Timeframe] | [Evidence] |
</high_confidence>

### 3.2 Demand Inhibitors

| Inhibitor | Impact | Likelihood of Persistence | Mitigation |
|-----------|--------|--------------------------|------------|
| [Inhibitor 1] | [H/M/L] | [Permanent / Temporary / Declining] | [How market actors are addressing] |

### 3.3 Regulatory Factors

<moderate_confidence>
- [Regulatory factor and its market impact]
- [Factor]
</moderate_confidence>

### 3.4 Technology Trends

- [Technology trend affecting market structure or growth]
- [Trend]

---

## 4. Competitive Structure

### 4.1 Market Concentration

| Metric | Value | Interpretation |
|--------|-------|---------------|
| Top 3 market share | [N]% | [Concentrated / Moderate / Fragmented] |
| HHI estimate | [Value] | [Interpretation] |
| Number of viable players | [N] | [Context] |

### 4.2 Barriers to Entry

| Barrier | Height | Durability | Circumvention Path |
|---------|--------|------------|-------------------|
| [Barrier 1] | [H/M/L] | [Permanent / Eroding / Growing] | [How new entrants bypass] |
| [Barrier 2] | [Height] | [Durability] | [Path] |

### 4.3 Leader Dynamics

- **Incumbent advantages**: [What keeps leaders in place]
- **Challenger strategies**: [How challengers are attacking -- niche focus, pricing, technology]
- **Disruption signals**: [Early indicators of market restructuring]

---

## 5. Customer Analysis

### 5.1 Buyer Profiles by Segment

| Segment | Primary Buyer | Decision Process | Typical Deal Size | Sales Cycle |
|---------|--------------|-----------------|-------------------|-------------|
| [Segment A] | [Title/role] | [Process description] | [Range] | [Duration] |
| [Segment B] | [Buyer] | [Process] | [Size] | [Cycle] |

### 5.2 Decision Criteria

| Criterion | Importance by Segment | Evidence |
|-----------|----------------------|----------|
| [Criterion 1] | Seg A: [H/M/L], Seg B: [H/M/L] | [Source] |
| [Criterion 2] | [Importance] | [Source] |

### 5.3 Willingness-to-Pay Signals

<moderate_confidence>
- [WTP signal from customer behavior, pricing experiments, or analyst data]
- [Signal]
</moderate_confidence>

---

## Cross-Domain Synthesis

<cross_domain_synthesis>
1. **[Pattern]** (from [adjacent market]): [How market dynamics from analogous markets inform projections here -- e.g., adoption curves from adjacent technology categories, pricing evolution from similar SaaS markets]
2. **[Pattern]** (from [market]): [Same structure]

**Emergent market interactions**: [Non-obvious dynamics from combining sizing, segmentation, and competitive data]
**What conventional market analysis misses**: [Blind spots in standard frameworks]
</cross_domain_synthesis>

---

## Self-Review Results

<self_review>
**Internal contradictions found**: [None / List -- e.g., "Segment sizes don't sum to TAM"]
**Confidence tier adjustments**: [None / "TAM estimate: Tier 1 to Tier 2 because methodology inconsistency"]
**Reasoning chains that did not survive scrutiny**: [None / List]
**Coverage gaps vs. market scope**: [None / Segments or geographies not covered]
**Precision calibration**: [Whether estimates inappropriately precise for confidence level]
</self_review>

---

## Coverage Gaps & Verification Status

| Expected Coverage | Actual Status | Impact | Recommended Action |
|-------------------|---------------|--------|-------------------|
| [Market area] | [Status] | [H/M/L] | [Action] |

---

## Quality Metrics

```yaml
quality_metrics:
  pattern: market_research
  segments_defined: [N]
  sizing_confidence: "Tier [N] -- [basis]"
  tam_range_width: "[low to high as %]"
  growth_projections_years: [N]
  demand_drivers_identified: [N]
  barriers_analyzed: [N]
  buyer_profiles_created: [N]
  sources_used: [N]
  analyst_reports_cited: [N]
  cross_source_agreement_rate: [0.0-1.0]
  sizing_methodology: "[top-down / bottom-up / triangulated]"
```

---

## For Downstream

**Target**: Spark (ideation) + Ignite (GTM)

**Segment prioritization** (ready for Spark opportunity scoring):
1. [Segment A] -- [Priority rationale and opportunity size]
2. [Segment B] -- [Rationale]
3. [Segment C] -- [Rationale]

**Entry strategy considerations:**
- Best entry segment: [Segment] because [reasoning]
- Go-to-market motion: [Recommended approach for best segment]
- Expansion path: [Segment A] -> [Segment B] -> [Segment C]

**Key constraints established:**
- Market ceiling: [SAM/SOM constraint on business planning]
- Competitive constraint: [Market share realistically capturable]

**Would change conclusions if:**
- [Regulation changes market definition]
- [Technology shift creates new segment or destroys existing one]

**Recommended refresh trigger**: [Timeframe]

---

## Freshness Model

```yaml
freshness_model:
  pattern: market_research
  research_date: "[DATE]"
  overall_volatility: "[High/Medium/Low]"
  estimated_shelf_life: "[3/6/12 months]"
  per_section_freshness:
    market_sizing: "[DATE] -- [sizing stability note; analyst report release cycle]"
    segmentation: "[DATE] -- [segment boundary stability]"
    market_dynamics: "[DATE] -- [driver/inhibitor evolution pace]"
    competitive_structure: "[DATE] -- [M&A and entry pace]"
    customer_analysis: "[DATE] -- [buyer behavior shift pace]"
  refresh_triggers:
    - "New analyst report from [key firms]"
    - "Major M&A reshaping market structure"
    - "Regulatory change affecting market definition"
```

---

## Methodology Notes

<methodology>
- **Consolidation mode**: standard -- quantitative findings reconciled across sources
- **Sources processed**: [List]
- **Sizing reconciliation**: [How different sizing estimates were reconciled -- averaging, methodology preference, recency]
- **Key conflicts resolved**: [How segmentation or sizing disagreements were handled]
- **Remaining uncertainties**: [Market areas with insufficient data]
- **Limitations**: [Geographic scope, recency of analyst reports, SMB vs. enterprise coverage]
</methodology>
````

---

## Template 7: User Research

**Pattern ID**: `user_research`
**Primary Deliverable**: Persona profiles + JTBD map + unmet needs hierarchy
**Default Consolidation Mode**: `depth_first`
**Confidence Tiering Target**: Each persona and need claim (behavioral evidence quality)

````markdown
# User Research: [TOPIC] in [DOMAIN]

**Research Date**: [DATE]
**Sources**: [MODEL LIST]
**Consolidation Mode**: depth_first
**Pattern**: user_research

---

## Executive Summary

[2-3 paragraphs: Number of user segments identified, key personas, most important unmet needs, most significant behavioral patterns, and the highest-signal workarounds observed. State which findings are grounded in multi-source evidence vs. inference.]

**Key user research findings:**
1. **[Finding 1]** -- [One-line summary]
2. **[Finding 2]** -- [One-line summary]
3. **[Finding 3]** -- [One-line summary]

---

## 1. User Segmentation

### 1.1 Segment Definitions

| Segment | Definition | Size Estimate | Confidence | Behavioral Profile |
|---------|------------|---------------|------------|-------------------|
| [Segment A] | [Demographic + behavioral definition] | [Est. users/companies] | Tier [N] | [Key behaviors] |
| [Segment B] | [Definition] | [Size] | Tier [N] | [Behaviors] |
| [Segment C] | [Definition] | [Size] | Tier [N] | [Behaviors] |

### 1.2 Segmentation Rationale

**Segmentation axes**: [Behavioral, not just demographic -- e.g., "segmented by current solution sophistication and switching urgency"]
**Why these segments**: [What makes this segmentation actionable vs. alternative approaches]
**Cross-source validation**: [Which sources agreed on segment boundaries]

---

## 2. Persona Profiles

### 2.1 Persona: [Persona Name -- e.g., "The Overwhelmed Ops Lead"]

**Segment**: [Segment A]
**Validation**: [Cross-source agreement level]

| Attribute | Detail | Confidence |
|-----------|--------|------------|
| **Demographics** | [Role, experience level, company size/type] | Tier [N] |
| **Goals** | [What they are trying to achieve -- primary and secondary] | Tier [N] |
| **Frustrations** | [What blocks or slows them -- specific, not generic] | Tier [N] |
| **Current solutions** | [Tools/processes they use today] | Tier [N] |
| **Unmet needs** | [What current solutions fail to address] | Tier [N] |
| **Decision criteria** | [What drives their adoption/switching decisions] | Tier [N] |
| **Information sources** | [Where they learn about new solutions] | Tier [N] |

**Behavioral narrative**: [2-3 sentences describing a typical day/workflow and where pain occurs]

<high_confidence>
**Validated behaviors**: [Behaviors confirmed across multiple sources -- reviews, forums, studies]
</high_confidence>

<moderate_confidence>
**Inferred behaviors**: [Behaviors inferred from single-source data or indirect signals]
</moderate_confidence>

### 2.2 Persona: [Persona Name]

[Same structure as 2.1]

### 2.3 Persona: [Persona Name]

[Same structure as 2.1]

---

## 3. Jobs-to-Be-Done Map

### 3.1 Functional Jobs

| Job ID | Job Statement | Segment(s) | Current Solution | Satisfaction | Confidence |
|--------|--------------|-------------|-----------------|-------------|------------|
| F1 | "When I [situation], I want to [action] so I can [outcome]" | [Segments] | [How solved today] | [Over/Under/Un-served] | Tier [N] |
| F2 | [Job statement] | [Segments] | [Solution] | [Satisfaction] | Tier [N] |

### 3.2 Emotional Jobs

| Job ID | Job Statement | Segment(s) | Current Fulfillment | Gap |
|--------|--------------|-------------|-------------------|-----|
| E1 | "I want to feel [emotion] when [context]" | [Segments] | [How currently fulfilled] | [Gap description] |

### 3.3 Social Jobs

| Job ID | Job Statement | Segment(s) | Current Fulfillment | Gap |
|--------|--------------|-------------|-------------------|-----|
| S1 | "I want to be perceived as [attribute] by [audience]" | [Segments] | [Current fulfillment] | [Gap] |

### 3.4 Satisfaction Gap Summary

```
                Under-served          Appropriately served     Over-served
                (opportunity)         (table stakes)           (potential to simplify)
Functional:     [F1, F3]              [F2, F5]                 [F4]
Emotional:      [E1]                  [E2]                     --
Social:         [S1]                  --                       --
```

---

## 4. Behavioral Patterns

### 4.1 Usage Patterns

<high_confidence>
- **[Pattern 1]**: [Description of observed behavior, frequency, context. Source: reviews, forums, studies]
- **[Pattern 2]**: [Description]
</high_confidence>

### 4.2 Workflow Analysis

| Phase | Activity | Tool(s) Used | Pain Points | Opportunity |
|-------|----------|-------------|-------------|-------------|
| [Phase 1] | [What user does] | [Current tools] | [Where it breaks down] | [What could be improved] |
| [Phase 2] | [Activity] | [Tools] | [Pain] | [Opportunity] |

### 4.3 Workarounds and Hacks (High-Value Signal)

| Workaround | What It Reveals | Segment(s) | Frequency | Source |
|------------|----------------|-------------|-----------|--------|
| [Users do X to work around Y] | [The unmet need this signals] | [Segments] | [How common] | [Source] |

**Workaround insight**: [Meta-analysis of what workaround patterns collectively reveal about product opportunities]

---

## 5. Unmet Needs Hierarchy

### 5.1 Ranked Unmet Needs

| Rank | Need | Frequency | Intensity | Solution Gap | Composite Score | Confidence |
|------|------|-----------|-----------|-------------|----------------|------------|
| 1 | [Need description] | [H/M/L] | [H/M/L] | [H/M/L] | [Score] | Tier [N] |
| 2 | [Need] | [Freq] | [Intensity] | [Gap] | [Score] | Tier [N] |
| 3 | [Need] | [Freq] | [Intensity] | [Gap] | [Score] | Tier [N] |

**Scoring methodology**: Composite = Frequency x Intensity x Solution Gap, normalized to [scale]

### 5.2 Need Clusters

- **Cluster: [Theme]** -- Needs [1, 3, 5] cluster around [common theme]. Solving any one partially addresses the others.
- **Cluster: [Theme]** -- Needs [2, 4] relate to [theme].

### 5.3 Need Validation Status

<high_confidence>
Needs validated by multiple independent sources (reviews, forums, studies): [List]
</high_confidence>

<moderate_confidence>
Needs identified from single-source evidence: [List]
</moderate_confidence>

Needs inferred from behavioral signals without direct user statement: [List -- flag as Tier 3]

---

## Cross-Domain Synthesis

<cross_domain_synthesis>
1. **[Pattern]** (from [adjacent user population]): [How user behavior patterns from analogous domains inform this research -- e.g., enterprise adoption patterns from adjacent SaaS tools, developer workflow patterns from similar dev tools]
2. **[Pattern]** (from [domain]): [Same structure]

**Emergent need interactions**: [Needs that combine to create a larger unmet need not visible from individual needs]
**What conventional user research misses**: [Blind spots -- e.g., non-users, churned users, workaround users]
</cross_domain_synthesis>

---

## Self-Review Results

<self_review>
**Internal contradictions found**: [None / List -- e.g., "Persona A's stated goal conflicts with observed behavior"]
**Confidence tier adjustments**: [None / Adjustments]
**Reasoning chains that did not survive scrutiny**: [None / List]
**Coverage gaps vs. user segments**: [None / Segments under-represented in source data]
**Assumption laundering check**: [Were pre-existing beliefs confirmed too readily? Any contradictory evidence suppressed?]
</self_review>

---

## Coverage Gaps & Verification Status

| Expected Coverage | Actual Status | Impact | Recommended Action |
|-------------------|---------------|--------|-------------------|
| [User group/behavior] | [Status] | [H/M/L] | [Action] |

---

## Quality Metrics

```yaml
quality_metrics:
  pattern: user_research
  segments_defined: [N]
  personas_created: [N]
  jtbd_functional: [N]
  jtbd_emotional: [N]
  jtbd_social: [N]
  unmet_needs_ranked: [N]
  workarounds_identified: [N]
  tier_1_needs: [N]
  tier_2_needs: [N]
  tier_3_needs: [N]
  sources_used: [N]
  cross_source_agreement_rate: [0.0-1.0]
  behavioral_vs_demographic_segmentation: "[behavioral / mixed / demographic]"
```

---

## For Downstream

**Target**: Foundry (requirements) + Spark (ideation)

**Persona cards** (ready for Foundry consumption):
- [Persona 1 name]: [One-line summary + top 3 needs]
- [Persona 2 name]: [Summary + needs]
- [Persona 3 name]: [Summary + needs]

**JTBD map** (ready for Spark opportunity scoring):
- Top underserved jobs: [F1, F3, E1]
- Current solution weaknesses: [List]

**Ranked unmet needs** (ready for feature prioritization):
1. [Need] -- Frequency [H], Intensity [H], Gap [H]
2. [Need] -- [Scores]
3. [Need] -- [Scores]

**Key constraints established:**
- [User constraint that downstream must respect -- e.g., "users will not tolerate setup time > 15 minutes"]
- [Constraint]

**Would change conclusions if:**
- [User behavior shifts with new competing product]
- [Market segment expands to include different user profile]

**Recommended refresh trigger**: [Timeframe]

---

## Freshness Model

```yaml
freshness_model:
  pattern: user_research
  research_date: "[DATE]"
  overall_volatility: "[High/Medium/Low]"
  estimated_shelf_life: "[3/6/12 months]"
  per_section_freshness:
    segmentation: "[DATE] -- [segment stability note]"
    personas: "[DATE] -- [behavioral shift pace]"
    jtbd_map: "[DATE] -- functional jobs stable; emotional/social may shift"
    behavioral_patterns: "[DATE] -- [tool/workflow change pace]"
    unmet_needs: "[DATE] -- [need satisfaction rate changes with new solutions]"
  refresh_triggers:
    - "Major competing product launch"
    - "User base composition change (new segment enters)"
    - "Significant workflow/tool adoption shift"
```

---

## Methodology Notes

<methodology>
- **Consolidation mode**: depth_first -- prioritized behavioral depth over coverage breadth
- **Sources processed**: [List]
- **User evidence sources**: [Reviews, forums, studies, surveys, behavioral data cited]
- **Key conflicts resolved**: [How persona or need disagreements were reconciled]
- **Remaining uncertainties**: [User segments or behaviors with insufficient evidence]
- **Limitations**: [No primary research conducted; relies on secondary sources. Possible survivorship bias in reviews. English-language sources only.]
</methodology>
````

---

## Template 8: Economic Analysis

**Pattern ID**: `economic_analysis`
**Primary Deliverable**: Financial model framework + sensitivity analysis + benchmark comparison
**Default Consolidation Mode**: `confidence_weighted`
**Confidence Tiering Target**: Each cost and value estimate (quantitative evidence quality)

````markdown
# Economic Analysis: [TOPIC] in [DOMAIN]

**Research Date**: [DATE]
**Sources**: [MODEL LIST]
**Consolidation Mode**: confidence_weighted
**Pattern**: economic_analysis

---

## Executive Summary

[2-3 paragraphs: Overall financial viability assessment, key ROI drivers, most sensitive assumptions, and recommendation confidence. State the bottom line (viable/marginal/non-viable) with confidence ranges, not point estimates. Highlight the single assumption that most affects the outcome.]

**Key economic findings:**
1. **[Finding 1]** -- [One-line summary]
2. **[Finding 2]** -- [One-line summary]
3. **[Finding 3]** -- [One-line summary]

---

## 1. Cost Model

### 1.1 Cost Categories

| Category | Subcategory | Low Estimate | Base Estimate | High Estimate | Confidence | Source(s) |
|----------|------------|-------------|---------------|---------------|------------|-----------|
| **Setup / Initial** | [Item] | $[X] | $[Y] | $[Z] | Tier [N] | [Sources] |
| | [Item] | $[X] | $[Y] | $[Z] | Tier [N] | [Sources] |
| **Recurring** | [Item] | $[X]/mo | $[Y]/mo | $[Z]/mo | Tier [N] | [Sources] |
| | [Item] | $[X]/mo | $[Y]/mo | $[Z]/mo | Tier [N] | [Sources] |
| **Variable** | [Item] | $[X]/unit | $[Y]/unit | $[Z]/unit | Tier [N] | [Sources] |
| **TOTAL (Year 1)** | | $[X] | $[Y] | $[Z] | | |
| **TOTAL (Year 2-3 annual)** | | $[X] | $[Y] | $[Z] | | |

### 1.2 Cost Drivers & Scaling Behavior

| Cost Driver | Scaling Behavior | Inflection Point | Optimization Lever |
|-------------|-----------------|------------------|-------------------|
| [Driver] | [Linear / Step / Exponential] | [At what scale/volume] | [How to optimize] |

### 1.3 Hidden Costs

<cross_domain_synthesis>
**Hidden costs identified through cross-domain analysis:**
- [Hidden cost 1: e.g., "Migration costs consistently underestimated by 2-3x in similar technology transitions"]
- [Hidden cost 2: e.g., "Opportunity cost of team learning curve -- derived from analogous adoption patterns"]
- [Hidden cost 3]
</cross_domain_synthesis>

<contested>
**Claude Opus 4.6 view**: Total hidden costs estimated at $[X] because [reasoning].
**Gemini 3.1 Pro view**: Hidden costs are lower at $[Y] because [different analysis].
**GPT-5.2 view**: Recent implementations suggest $[Z] based on [site-specific case studies].
**Assessment**: Range of $[Low]-$[High] reflects genuine uncertainty. Key variable: [factor].
</contested>

---

## 2. Revenue / Value Model

### 2.1 Value Drivers

| Value Driver | Quantification | Timeframe | Confidence | Basis |
|-------------|---------------|-----------|------------|-------|
| [Driver 1: e.g., "Time savings"] | [$ value or range] | [When realized] | Tier [N] | [How quantified] |
| [Driver 2: e.g., "Revenue increase"] | [$ value] | [Timeframe] | Tier [N] | [Basis] |
| [Driver 3: e.g., "Risk reduction"] | [$ value] | [Timeframe] | Tier [N] | [Basis] |

### 2.2 Revenue/Value Projections

| Scenario | Year 1 | Year 2 | Year 3 | Cumulative (3yr) |
|----------|--------|--------|--------|-------------------|
| **Pessimistic** | $[X] | $[X] | $[X] | $[X] |
| **Base** | $[X] | $[X] | $[X] | $[X] |
| **Optimistic** | $[X] | $[X] | $[X] | $[X] |

**Scenario assumptions**:
- Pessimistic: [Key assumptions]
- Base: [Key assumptions]
- Optimistic: [Key assumptions]

---

## 3. ROI / Cost-Benefit Analysis

### 3.1 Core Metrics

| Metric | Pessimistic | Base | Optimistic | Confidence |
|--------|-------------|------|------------|------------|
| **ROI** | [X]% | [Y]% | [Z]% | Tier [N] |
| **Payback period** | [X] months | [Y] months | [Z] months | Tier [N] |
| **NPV (3yr, [discount rate])** | $[X] | $[Y] | $[Z] | Tier [N] |
| **IRR** | [X]% | [Y]% | [Z]% | Tier [N] |

### 3.2 Confidence Assessment

<high_confidence>
**Well-grounded estimates**: [Which cost/value items have Tier 1 confidence and why]
</high_confidence>

<moderate_confidence>
**Estimates requiring caution**: [Tier 2 items with caveats]
</moderate_confidence>

**Critical Tier 3 assumptions**: [Items that are Tier 3 confidence AND have high impact on the result. These would flip the recommendation if wrong.]

---

## 4. Sensitivity Analysis

### 4.1 Key Variables & Impact

| Variable | Base Value | Range Tested | Impact on ROI | Impact on Payback | Criticality |
|----------|-----------|-------------|---------------|-------------------|-------------|
| [Var 1] | [Base] | [Low - High] | [ROI range] | [Payback range] | [H/M/L] |
| [Var 2] | [Base] | [Range] | [Impact] | [Impact] | [Criticality] |

### 4.2 Break-Even Thresholds

| Variable | Break-Even Value | Current Best Estimate | Margin of Safety |
|----------|-----------------|----------------------|------------------|
| [Variable] | [Value at which ROI = 0] | [Current estimate] | [How far from break-even] |

### 4.3 "What Changes the Answer" Summary

<high_confidence>
**The recommendation holds** as long as:
- [Condition 1 -- the key assumption that must hold]
- [Condition 2]
</high_confidence>

**The recommendation flips if:**
- [Variable X exceeds Y] -- currently estimated at [Z], so margin is [N]%
- [Assumption A proves false] -- probability estimated at [P]%

---

## 5. Benchmark Comparison

### 5.1 Industry Benchmarks

| Metric | Our Estimate | Industry Benchmark | Source | Assessment |
|--------|-------------|-------------------|--------|------------|
| [Metric] | [Our value] | [Benchmark range] | [Source] | [Above/Below/In-line] |

### 5.2 Comparable Implementations

| Comparable | Context | Result | Relevance | Source | Confidence |
|------------|---------|--------|-----------|--------|------------|
| [Company/project] | [Similar context] | [Outcome] | [How comparable] | [Source] | Tier [N] |

---

## Cross-Domain Synthesis

<cross_domain_synthesis>
1. **[Pattern]** (from [industry]): [How economic patterns from other domains inform this analysis -- e.g., TCO underestimation patterns from enterprise IT, adoption-curve revenue patterns from similar SaaS]
2. **[Pattern]** (from [domain]): [Same structure]

**Emergent cost interactions**: [Non-obvious cost interactions -- e.g., choosing cheap compute increases engineering cost]
**What conventional financial analysis misses**: [Hidden costs, second-order effects, option value]
</cross_domain_synthesis>

---

## Self-Review Results

<self_review>
**Internal contradictions found**: [None / List -- e.g., "Cost savings claim in section 2 contradicts cost increase in section 1.3"]
**Confidence tier adjustments**: [None / "Revenue Driver 2: Tier 1 to Tier 2 because single-benchmark basis"]
**Reasoning chains that did not survive scrutiny**: [None / List]
**Precision calibration**: [Were estimates presented with appropriate ranges? Any false precision?]
**Optimism bias check**: [Was the base case genuinely base, or is it skewed optimistic?]
</self_review>

---

## Coverage Gaps & Verification Status

| Expected Coverage | Actual Status | Impact | Recommended Action |
|-------------------|---------------|--------|-------------------|
| [Cost/value area] | [Status] | [H/M/L] | [Action] |

---

## Quality Metrics

```yaml
quality_metrics:
  pattern: economic_analysis
  cost_categories: [N]
  value_drivers: [N]
  scenarios_modeled: [N]
  tier_1_estimates: [N]
  tier_2_estimates: [N]
  tier_3_estimates: [N]
  sensitivity_variables: [N]
  break_even_thresholds: [N]
  benchmarks_cited: [N]
  comparables_analyzed: [N]
  sources_used: [N]
  cross_source_agreement_rate: [0.0-1.0]
  range_width_avg: "[X]%"  # average range as % of base estimate
```

---

## For Downstream

**Target**: Vantage (value engineering)

**Financial model summary** (ready for Vantage):
- Total 3-year cost (base): $[X]
- Total 3-year value (base): $[Y]
- Net ROI (base): [Z]%
- Payback: [N] months

**Key assumptions** (for Vantage sensitivity):
1. [Assumption with value and confidence tier]
2. [Assumption]
3. [Assumption]

**Sensitivity ranges** (for Vantage risk assessment):
- [Variable]: [Range] -- flips recommendation at [threshold]
- [Variable]: [Range]

**Key constraints established:**
- Budget ceiling: $[X] per [period]
- Minimum viable ROI: [X]%

**Would change conclusions if:**
- [Pricing model changes]
- [Scale assumption proves wrong by > [N]%]

**Recommended refresh trigger**: [Timeframe]

---

## Freshness Model

```yaml
freshness_model:
  pattern: economic_analysis
  research_date: "[DATE]"
  overall_volatility: "[High/Medium/Low]"
  estimated_shelf_life: "[3/6/12 months]"
  per_section_freshness:
    cost_model: "[DATE] -- [pricing change pace note]"
    value_model: "[DATE] -- [value driver stability]"
    roi_analysis: "[DATE] -- [dependent on cost + value freshness]"
    sensitivity: "[DATE] -- [variable range stability]"
    benchmarks: "[DATE] -- [benchmark publication cycle]"
  refresh_triggers:
    - "Vendor pricing change"
    - "Scale assumption validated or invalidated by real data"
    - "New comparable implementation data available"
```

---

## Methodology Notes

<methodology>
- **Consolidation mode**: confidence_weighted -- evidence quality drives estimate reliability
- **Sources processed**: [List]
- **Estimation approach**: [How cost/value estimates were derived and reconciled across sources]
- **Discount rate used**: [Rate and justification]
- **Key conflicts resolved**: [How estimate disagreements were reconciled]
- **Remaining uncertainties**: [Estimates with insufficient data]
- **Limitations**: [Public data only, no access to vendor discount pricing, no primary cost data from similar implementations]
</methodology>
````

---

## Template 9: Compliance & Requirements

**Pattern ID**: `compliance_requirements`
**Primary Deliverable**: Requirements register + constraint map + risk matrix + governance recommendations
**Default Consolidation Mode**: `gap_driven`
**Confidence Tiering Target**: Each regulatory interpretation (legal interpretation confidence)

````markdown
# Compliance & Requirements: [TOPIC] in [DOMAIN]

**Research Date**: [DATE]
**Sources**: [MODEL LIST]
**Consolidation Mode**: gap_driven
**Pattern**: compliance_requirements
**Jurisdictions**: [LIST OF APPLICABLE JURISDICTIONS]

---

## Executive Summary

[2-3 paragraphs: Regulatory landscape scope, number of applicable regulations identified, most constraining requirements, highest-risk non-compliance areas, and key governance recommendations. State which requirements are Tier 1 (clear regulatory text) vs. Tier 3 (ambiguous interpretation requiring legal review).]

**Critical compliance findings:**
1. **[Finding 1]** -- [One-line summary]
2. **[Finding 2]** -- [One-line summary]
3. **[Finding 3]** -- [One-line summary]

**IMPORTANT**: This analysis identifies and organizes regulatory requirements. It is NOT legal advice. Tier 3 interpretations and any requirements with significant business impact REQUIRE legal review before implementation.

---

## 1. Regulatory Landscape

### 1.1 Applicable Regulations by Jurisdiction

| Jurisdiction | Regulation | Scope | Effective Date | Enforcement Status | Confidence |
|-------------|-----------|-------|---------------|-------------------|------------|
| [Jurisdiction A] | [Regulation name + citation] | [What it covers] | [Date] | [Active / Pending / Proposed] | Tier [N] |
| [Jurisdiction B] | [Regulation] | [Scope] | [Date] | [Status] | Tier [N] |

### 1.2 Regulatory Body Requirements

| Body | Authority | Key Requirements | Audit Frequency | Penalty Range |
|------|-----------|-----------------|-----------------|---------------|
| [Body] | [What they regulate] | [Core requirements] | [Annual / Continuous / Ad-hoc] | [Penalty range] |

### 1.3 Compliance Tiers

<high_confidence>
**Mandatory** (legal requirement):
- [Requirement with regulatory citation]
- [Requirement]
</high_confidence>

<moderate_confidence>
**Recommended** (industry standard / best practice):
- [Standard with source]
- [Standard]
</moderate_confidence>

**Aspirational** (emerging / competitive advantage):
- [Emerging standard with timeline]

---

## 2. Requirements Register

### 2.1 Functional Requirements (from regulatory analysis)

| Req ID | Requirement | Source Regulation | Compliance Tier | Interpretation Confidence | Implementation Notes |
|--------|------------|------------------|----------------|--------------------------|---------------------|
| FR-1 | [Specific requirement statement] | [Regulation + section] | Mandatory | Tier [1/2/3] | [How to implement; complexity] |
| FR-2 | [Requirement] | [Source] | [Tier] | Tier [N] | [Notes] |

### 2.2 Non-Functional Requirements (security, privacy, audit)

| Req ID | Requirement | Source | Compliance Tier | Interpretation Confidence | Implementation Notes |
|--------|------------|--------|----------------|--------------------------|---------------------|
| NFR-1 | [Security requirement] | [Source regulation or standard] | [Mandatory/Recommended] | Tier [N] | [Notes] |
| NFR-2 | [Privacy requirement] | [Source] | [Tier] | Tier [N] | [Notes] |
| NFR-3 | [Audit requirement] | [Source] | [Tier] | Tier [N] | [Notes] |

### 2.3 Requirements Requiring Legal Review

**The following requirements have Tier 3 interpretation confidence and MUST be reviewed by legal counsel before implementation decisions:**

| Req ID | Requirement | Ambiguity Source | Risk if Misinterpreted | Recommended Legal Question |
|--------|------------|-----------------|----------------------|---------------------------|
| [ID] | [Requirement] | [Why interpretation is uncertain] | [What goes wrong if misread] | [Specific question for legal] |

<contested>
**Claude Opus 4.6 view**: [Regulation X] requires [interpretation A] because [reasoning from regulatory text].
**Gemini 3.1 Pro view**: [Regulation X] is better interpreted as [interpretation B] because [different precedent / guidance].
**GPT-5.2 view**: Recent enforcement actions suggest [interpretation C] based on [site-specific legal sources].
**Assessment**: Interpretation is genuinely ambiguous. [Factor] would resolve it. Flag for legal review with all three interpretations presented.
</contested>

---

## 3. Constraint Map

### 3.1 Technical Constraints

| Constraint ID | Constraint | Source Requirement | Impact on Architecture | Severity |
|--------------|-----------|-------------------|----------------------|----------|
| TC-1 | [Technical constraint -- e.g., "Data must be encrypted at rest and in transit"] | [FR/NFR reference] | [Architecture impact] | [H/M/L] |
| TC-2 | [Constraint] | [Source] | [Impact] | [Severity] |

### 3.2 Organizational Constraints

| Constraint ID | Constraint | Source | Impact on Process | Severity |
|--------------|-----------|--------|------------------|----------|
| OC-1 | [Organizational constraint -- e.g., "Data processing requires DPO approval"] | [Requirement ref] | [Process impact] | [H/M/L] |

### 3.3 Temporal Constraints

| Constraint ID | Constraint | Deadline | Consequence of Missing | Buffer |
|--------------|-----------|----------|----------------------|--------|
| TMP-1 | [Temporal constraint -- e.g., "Compliance required by [date]"] | [Date] | [Consequence] | [Time remaining] |

### 3.4 Constraint Interaction Map

| Constraint A | Constraint B | Interaction | Resolution |
|-------------|-------------|------------|------------|
| [TC-1] | [OC-1] | [How they interact -- e.g., "encryption requirement conflicts with audit access requirement"] | [How to resolve] |

---

## 4. Risk Matrix

### 4.1 Non-Compliance Risks

| Risk ID | Risk Description | Likelihood | Impact | Severity (L x I) | Source Requirement | Mitigation |
|---------|-----------------|-----------|--------|-------------------|-------------------|------------|
| R-1 | [Risk of non-compliance with specific requirement] | [H/M/L] | [H/M/L] | [Critical/High/Medium/Low] | [Req ID] | [Mitigation strategy] |
| R-2 | [Risk] | [L] | [I] | [Severity] | [Req] | [Mitigation] |

### 4.2 Risk Heat Map

```
              Low Impact     Medium Impact    High Impact
High Likeli.  [R-5]          [R-3]            [R-1] <<<
Med Likeli.   [R-6]          [R-4]            [R-2]
Low Likeli.                  [R-7]            [R-8]
```

### 4.3 Emerging Regulatory Risks

<moderate_confidence>
| Emerging Risk | Regulation/Proposal | Timeline | Probability | Preparation Action |
|--------------|--------------------|---------|-----------|--------------------|
| [Risk from pending regulation] | [Proposal name] | [Expected timeline] | [H/M/L] | [How to prepare now] |
</moderate_confidence>

---

## 5. Governance Recommendations

### 5.1 Framework Suggestions

<high_confidence>
| Framework | Applicability | Alignment With Requirements | Implementation Effort |
|-----------|--------------|---------------------------|---------------------|
| [Framework -- e.g., "SOC 2 Type II"] | [Why applicable] | [Which requirements it covers] | [H/M/L] |
| [Framework] | [Applicability] | [Coverage] | [Effort] |
</high_confidence>

### 5.2 Audit & Monitoring Requirements

| Audit Type | Frequency | Scope | Required Evidence | Responsible Role |
|-----------|-----------|-------|-------------------|-----------------|
| [Audit type] | [Frequency] | [What is audited] | [Documentation needed] | [Who is responsible] |

### 5.3 Ongoing Compliance Monitoring

| What to Monitor | Method | Frequency | Alert Threshold |
|-----------------|--------|-----------|----------------|
| [Compliance metric] | [How to monitor] | [How often] | [When to act] |

### 5.4 Regulatory Change Monitoring

- **Regulations to watch**: [List of pending regulations or active rulemaking processes]
- **Monitoring sources**: [Where to track changes -- government registers, legal services, industry bodies]
- **Review cadence**: [How often to re-assess compliance posture]

---

## Cross-Domain Synthesis

<cross_domain_synthesis>
1. **[Pattern]** (from [adjacent regulated domain]): [How compliance patterns from other industries inform this analysis -- e.g., HIPAA compliance lessons for health data, PCI-DSS patterns for payment processing]
2. **[Pattern]** (from [domain]): [Same structure]

**Emergent constraint interactions**: [Requirements from different regulations that interact to create unexpectedly complex constraints]
**What conventional compliance analysis misses**: [Areas that fall between regulatory frameworks or are under-addressed]
</cross_domain_synthesis>

---

## Self-Review Results

<self_review>
**Internal contradictions found**: [None / List -- e.g., "Requirement FR-3 conflicts with constraint TC-2"]
**Confidence tier adjustments**: [None / Adjustments]
**Reasoning chains that did not survive scrutiny**: [None / List]
**Coverage gaps vs. regulatory scope**: [None / Regulations not fully analyzed]
**Interpretation bias check**: [Were ambiguous regulations interpreted conservatively or liberally? Was this appropriate?]
**Legal review flags**: [N] requirements flagged for legal review
</self_review>

---

## Coverage Gaps & Verification Status

| Expected Coverage | Actual Status | Impact | Recommended Action |
|-------------------|---------------|--------|-------------------|
| [Regulation/jurisdiction] | [Status] | [H/M/L] | [Action -- legal review / targeted research / accept gap] |

---

## Quality Metrics

```yaml
quality_metrics:
  pattern: compliance_requirements
  jurisdictions_covered: [N]
  regulations_analyzed: [N]
  functional_requirements: [N]
  non_functional_requirements: [N]
  tier_1_interpretations: [N]
  tier_2_interpretations: [N]
  tier_3_interpretations: [N]  # requires legal review
  risks_identified: [N]
  critical_risks: [N]
  constraints_mapped: [N]
  constraint_interactions: [N]
  legal_review_flags: [N]
  sources_used: [N]
  cross_source_agreement_rate: [0.0-1.0]
  gap_driven_audit_score: [0.0-1.0]  # coverage vs. expected regulatory scope
```

---

## For Downstream

**Target**: Foundry (requirements generation)

**Requirements register** (ready for Foundry import):
- Total requirements: [N]
- Mandatory: [N]
- Recommended: [N]
- All with: source regulation, interpretation confidence, implementation notes

**Constraint map** (ready for Foundry architecture constraints):
- Technical constraints: [N] -- directly constrain architecture decisions
- Organizational constraints: [N] -- constrain process design
- Temporal constraints: [N] -- drive implementation timeline

**Non-compliance risks for Foundry risk register:**
- Critical risks: [List with Req IDs]
- High risks: [List]

**Key constraints established:**
- [Hard constraint from mandatory regulation]
- [Constraint from emerging regulation]

**Would change conclusions if:**
- [Pending regulation is enacted]
- [Enforcement guidance clarifies ambiguous requirement]

**Recommended refresh trigger**: [Timeframe based on regulatory change pace]

---

## Freshness Model

```yaml
freshness_model:
  pattern: compliance_requirements
  research_date: "[DATE]"
  overall_volatility: "[High/Medium/Low]"
  estimated_shelf_life: "[3/6/12 months]"
  per_section_freshness:
    regulatory_landscape: "[DATE] -- [regulatory change pace by jurisdiction]"
    requirements_register: "[DATE] -- [stable unless regulations change]"
    constraint_map: "[DATE] -- [stable unless new regulation or enforcement guidance]"
    risk_matrix: "[DATE] -- [enforcement action frequency]"
    governance_recommendations: "[DATE] -- [framework update cadence]"
  refresh_triggers:
    - "New regulation enacted in covered jurisdictions"
    - "Enforcement action or ruling setting precedent"
    - "Compliance framework version update (e.g., SOC 2 revision)"
    - "Pending regulation advances to final rule stage"
```

---

## Methodology Notes

<methodology>
- **Consolidation mode**: gap_driven -- audited regulatory coverage against all applicable jurisdictions and regulation types
- **Sources processed**: [List]
- **Regulatory text analysis**: [Which regulations were analyzed from primary text vs. secondary interpretation]
- **Key conflicts resolved**: [How regulatory interpretation disagreements were handled]
- **Remaining uncertainties**: [Ambiguous requirements awaiting legal review]
- **Limitations**: [Not legal advice. AI interpretation of regulations. Jurisdictions not covered. Pending regulations may change.]
- **Legal review recommended for**: [List of Tier 3 requirements and high-impact interpretations]
</methodology>
````

---

## Template Selection Quick Reference

| Pattern ID | Template | Primary Artifact | Default Mode | Confidence Target |
|------------|----------|-----------------|-------------|-------------------|
| `landscape_mapping` | Template 1 | Taxonomy + player inventory + white space | breadth_first | Category completeness |
| `comparative_evaluation` | Template 2 | Weighted matrix + recommendation | confidence_weighted | Cell-level scores |
| `implementation_pattern` | Template 3 | ADR catalog + patterns + anti-patterns | depth_first | Decision/pattern validation |
| `best_practices` | Template 4 | 8-dimension knowledge base | gap_driven | Per-dimension coverage |
| `competitive_intelligence` | Template 5 | Competitor profiles + dynamics | adversarial | Strategic claim evidence |
| `market_research` | Template 6 | TAM/SAM/SOM + segmentation | standard | Sizing estimate precision |
| `user_research` | Template 7 | Personas + JTBD + unmet needs | depth_first | Behavioral evidence quality |
| `economic_analysis` | Template 8 | Financial model + sensitivity | confidence_weighted | Estimate evidence quality |
| `compliance_requirements` | Template 9 | Requirements register + constraints | gap_driven | Interpretation confidence |

---

## For Downstream Cross-Reference

| Pattern | Primary Downstream Target | What It Produces for Downstream |
|---------|--------------------------|-------------------------------|
| Landscape Mapping | Comparative Evaluation | Shortlist + evaluation criteria seeds |
| Comparative Evaluation | Implementation Pattern | Selection rationale (ADR) + implementation scope |
| Implementation Pattern | Foundry | ADR log + implementation checklist + anti-pattern acceptance criteria |
| Best Practices | Claude Code Skills | 8-dimension KB + Quick Reference Card for skill generation |
| Competitive Intelligence | Ignite | Positioning strategy + differentiation matrix |
| Market Research | Spark + Ignite | Segment prioritization + entry strategy |
| User Research | Foundry + Spark | Persona cards + JTBD map + ranked unmet needs |
| Economic Analysis | Vantage | Financial model + key assumptions + sensitivity ranges |
| Compliance & Requirements | Foundry | Requirements register + constraint map |
