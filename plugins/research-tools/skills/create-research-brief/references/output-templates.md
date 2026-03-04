# Output Templates

**Version**: 2.0
**Last validated**: 2026-03-04
**Consumed by**: create-research-brief (brief assembly), consolidate-research (merge prompt + output templates)

This file defines: (1) pattern-specific research brief templates, (2) SINGLE mode guidance, (3) the merge prompt, and (4) the Best Practices output template.

---

## Section 1: Research Brief Templates

Every research brief shares a common structure (Header Block, Prompt Slots, Manifest, Post-Research sections) with pattern-specific middle sections that vary by pattern. Shared blocks are defined once below, then each pattern template references them.

---

### Shared Block: Header

Used by all 9 pattern templates. Fill in bracketed values during brief generation.

````markdown
# Research Brief: [Topic]

**Model Mode**: [DUAL / FULL / SINGLE] ([Model list])
**Research Pattern**: [Pattern Name] (`[pattern_id]`)

## Research Classification

| Dimension | Assessment |
|-----------|------------|
| **Pattern** | [Pattern Name] (`[pattern_id]`) |
| **Key questions** | [3-5 questions from pattern template + user context] |
| **Success criteria** | [What makes this research successful — derived from pattern primary deliverable] |
| **Primary deliverable** | [From Pattern Registry: e.g., "Weighted comparison matrix + decision recommendation with sensitivity analysis"] |

## Topic Risk Assessment

| Risk Factor | Rating | Implication |
|-------------|--------|-------------|
| Recency sensitivity | [H/M/L] | [Impact on findings reliability] |
| Contestation level | [H/M/L] | [Likelihood of conflicting expert views] |
| Source availability | [H/M/L] | [Whether quality primary sources exist] |
| False confidence risk | [H/M/L] | [Risk of models agreeing without evidence] |
| Coverage gap risk | [H/M/L] | [Risk of missing important areas] |

## Context Budget

| Dimension | Estimate |
|-----------|----------|
| **Expected combined output** | [X]K tokens |
| **Context tier** | [Standard / Extended / Chunked] |
| **Chunking strategy** | [N/A / By section / By model — only if Chunked tier] |

## Model Role Assignments

### DUAL Mode

| Model | Base Role | + Redistributed from OpenAI |
|-------|-----------|----------------------------|
| **Claude Opus 4.6** | Deep reasoning + web research + novel synthesis | + [redistributed areas] |
| **Gemini 3.1 Pro Deep** | Structured data + landscape mapping | + [redistributed areas] |

### FULL Mode

| Model | Assigned Role | Rationale |
|-------|---------------|-----------|
| **Claude Opus 4.6** | [Primary researcher: reasoning + web research + novel synthesis] | [Why] |
| **Gemini 3.1 Pro Deep** | [Structured data retrieval + landscape mapping] | [Why] |
| **GPT-5.2 Deep Research** | [Targeted investigation with site restrictions] | [Why] |
| **GPT-5.2 Chat** | [Recency validation + quick sentiment scan] | [Why — if used] |

## Consolidation Strategy

**Recommended mode**: [Mode name] (`[mode_id]`)
**Pattern default**: [Mode name] (`[mode_id]`)
**Override rationale**: [Why recommended differs from default, or "Matches pattern default"]
**Verification priorities**:
1. [Top verification item]
2. [Second verification item]
3. [Third verification item]

## Coverage Matrix

| Coverage Area | Claude | Gemini | GPT-5.2 Deep | GPT-5.2 Chat | Overlap Zone |
|---------------|--------|--------|--------------|--------------|--------------|
| [Area 1] | X | X | | | Yes |
| [Area 2] | | X | X | | Yes |
| [Area 3] | X | | | | No |

**Cross-validation strategy**: [Brief description of how overlapping coverage enables cross-validation]
````

---

### Shared Block: Prompt Slots

Used by all 9 pattern templates. Actual prompt content is generated from `pattern-prompt-templates.md`; these are structural slots in the brief.

````markdown
---

## Ready-to-Execute Prompts

### Prompt 1: Claude Opus 4.6 Research Prompt
<!-- COPY START -->
```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

[Full prompt generated from pattern-prompt-templates.md for Claude's role]
```
<!-- COPY END -->

### Prompt 2: Gemini 3.1 Pro Deep Research Prompt
<!-- COPY START -->
```
[Full prompt generated from pattern-prompt-templates.md for Gemini's role]
```
<!-- COPY END -->

### Prompt 3: GPT-5.2 Deep Research Prompt (FULL mode only)
<!-- COPY START -->
```
[Full prompt generated from pattern-prompt-templates.md for GPT-5.2 Deep's role]

Site restrictions: [list of restricted domains]
```
<!-- COPY END -->

### Prompt 4: GPT-5.2 Chat Prompt (FULL mode, optional)
<!-- COPY START -->
```
[Full prompt generated from pattern-prompt-templates.md for GPT-5.2 Chat's role]
```
<!-- COPY END -->
````

---

### Shared Block: Post-Research

Used by all 9 pattern templates. Appears after the consolidation manifest.

````markdown
---

## Post-Research: Merge Prompt

After executing all prompts, use the merge prompt (see Section 3 of output-templates.md) to consolidate outputs. Paste:
1. The consolidation manifest (from below)
2. All model outputs (unabridged)

into a new Claude Opus 4.6 conversation with the merge prompt.

## Post-Research Verification

| Priority | Verify | Method | Confidence Impact |
|----------|--------|--------|-------------------|
| 1 | [Item from verification_priorities] | [Specific verification method] | [What changes if wrong] |
| 2 | [Item] | [Method] | [Impact] |
| 3 | [Item] | [Method] | [Impact] |

## Freshness Model

| Attribute | Value |
|-----------|-------|
| **Topic volatility** | [critical / high / medium / low / stable] |
| **Confidence half-life** | [1_month / 3_months / 6_months / 12_months / 24_months] |
| **Recommended refresh date** | [YYYY-MM-DD] |
| **Staleness indicators** | [2-5 specific signals that would invalidate findings] |

### Per-Section Volatility (if applicable)

| Section | Volatility | Reason |
|---------|------------|--------|
| [Section name] | [critical/high/medium/low/stable] | [Why this section ages differently] |

## Research Chain

| Attribute | Value |
|-----------|-------|
| **Upstream research** | [research_id or "None — standalone research"] |
| **Upstream pattern** | [pattern_id or "N/A"] |
| **Inherited constraints** | [List of constraints from upstream, or "None"] |
| **Expected downstream** | [research_id + pattern_id, or "None planned"] |

### Constraint Propagation

[If upstream exists: list each inherited constraint and how it affects this research's scope or methodology. If standalone: "No upstream constraints."]

## Estimated Effort

| Phase | Time |
|-------|------|
| Execute prompts | [X hours] |
| Merge & review | [X min] |
| Verification | [X min] |
````

---

### Shared Block: Consolidation Manifest

Placed at the very end of the research brief. The YAML block is populated with research-specific values during brief generation. See `consolidation-manifest-schema.md` for full schema documentation.

````markdown
---

## Consolidation Manifest

Paste this manifest alongside your research outputs when running the merge prompt. Update `executed_at` for each model after running its prompt.

```yaml
# consolidation_manifest
consolidation_manifest:

  # Identity
  research_id: [product]-[topic-slug]-[YYYY-MM]
  pattern: [pattern_id]
  topic: "[Human-readable research topic]"
  objective: "[What decision or outcome this research supports]"
  model_mode: [DUAL / FULL / SINGLE]
  created_at: "[ISO 8601 datetime]"

  # Model Configuration
  models:
    - model_id: claude-opus-4-6
      role: primary_researcher
      capabilities: [web_search, adaptive_thinking, thinking_max]
      output_token_estimate: [estimated tokens]
      executed_at: null  # Update after execution

    - model_id: gemini-3.1-pro-deep-research
      role: structured_cataloger
      capabilities: [web_search, thinking_high]
      output_token_estimate: [estimated tokens]
      executed_at: null  # Update after execution

    # FULL mode only:
    # - model_id: gpt-5.2-deep-research
    #   role: targeted_investigator
    #   capabilities: [web_search, site_restrictions]
    #   site_restrictions: [domain list]
    #   output_token_estimate: [estimated tokens]
    #   executed_at: null

  # Pattern-Specific Metadata
  pattern_metadata:
    [Pattern-specific fields — see individual pattern templates below]

  # Coverage Matrix
  coverage_matrix:
    areas:
      - area: "[Coverage area name]"
        assigned_models: [model-ids]
        overlap_zone: [true/false]
    expected_overlap_summary: "[Cross-validation strategy description]"

  # Consolidation Configuration
  consolidation:
    recommended_mode: [mode_id]
    recommended_mode_rationale: "[Why this mode]"
    pattern_default_mode: [mode_id]
    user_override: null
    verification_priorities:
      - "[Priority 1]"
      - "[Priority 2]"
      - "[Priority 3]"

  # Research Chain
  research_chain:
    upstream_id: [id or null]
    upstream_pattern: [pattern or null]
    inherited_constraints: [list or empty]
    downstream_expected:
      research_id: [planned id or null]
      pattern: [planned pattern or null]

  # Freshness Model
  freshness:
    topic_volatility: [critical/high/medium/low/stable]
    confidence_half_life: [duration]
    staleness_indicators:
      - "[Signal 1]"
      - "[Signal 2]"
    recommended_refresh: "[YYYY-MM-DD]"
    per_section_volatility: []
```
````

---

### Pattern Template 1: Landscape Mapping (`landscape_mapping`)

Assembles: Shared Header + Landscape-Specific Sections + Shared Prompt Slots + Shared Manifest + Shared Post-Research.

**Primary Deliverable**: Taxonomy (category definitions) + player inventory (per-category structured table) + white space map.

**Default Consolidation Mode**: `breadth_first`

**Confidence Tiering**: Applies to category completeness. Tier 1: category fully mapped. Tier 2: category identified but player list may be incomplete. Tier 3: category suspected but poorly sourced.

````markdown
<!-- INSERT: Shared Header Block -->

## Landscape Scope

**Domain**: [Bounded domain being mapped]
**Scope boundaries**: [What is explicitly in/out of scope]
**Expected taxonomy categories**:
1. [Category 1]
2. [Category 2]
3. [Category 3]
4. [Category N]

## Taxonomy Hypothesis

| Category | Description | Expected Player Density | Priority |
|----------|-------------|------------------------|----------|
| [Category 1] | [What belongs here] | [High/Medium/Low/Unknown] | [High/Medium/Low] |
| [Category 2] | [Description] | [Density] | [Priority] |

## White Space Hypothesis

Before research execution, note hypothesized gaps in the landscape:
- [Hypothesized gap 1: where we expect few or no solutions]
- [Hypothesized gap 2]

## Player Inventory Scope

| Attribute | Per-Player Data Point |
|-----------|----------------------|
| Identity | Name, URL, founding year |
| Positioning | One-line positioning statement |
| Maturity | Stage (pre-launch / beta / GA / established) |
| Funding/Backing | Funding raised or corporate parent |
| Target Segment | Primary customer segment |
| Key Differentiator | What they claim sets them apart |

## Coverage Areas (Pattern-Specific)

| Coverage Area | Focus |
|---------------|-------|
| Taxonomy completeness | Are all categories identified and populated? |
| Player inventory depth | Per-category player tables with structured attributes |
| White space identification | Gaps, underserved segments, missing categories |
| Ecosystem dynamics | Partnerships, integrations, platform effects, M&A trends |
| Evolution trajectory | How the landscape is likely to change in 12-18 months |

<!-- INSERT: Shared Prompt Slots Block -->

### Manifest: Pattern-Specific Metadata

```yaml
  pattern_metadata:
    taxonomy_categories:
      - "[Category 1]"
      - "[Category 2]"
      - "[Category N]"
    scope_boundaries: "[What is out of scope]"
    key_questions:
      - "[Supplementary question 1]"
      - "[Supplementary question 2]"
```

<!-- INSERT: Shared Consolidation Manifest Block (with pattern_metadata above) -->
<!-- INSERT: Shared Post-Research Block -->
````

---

### Pattern Template 2: Comparative Evaluation (`comparative_evaluation`)

Assembles: Shared Header + Comparative-Specific Sections + Shared Prompt Slots + Shared Manifest + Shared Post-Research.

**Primary Deliverable**: Weighted comparison matrix (options x criteria with scores, confidence per cell, source attribution) + decision recommendation with sensitivity analysis.

**Default Consolidation Mode**: `confidence_weighted`

**Confidence Tiering**: Applies to each criterion score per option. Tier 1: score backed by multiple sources. Tier 2: single source or moderate evidence. Tier 3: estimated or poorly sourced. Overall recommendation confidence is a function of the lowest-confidence criterion with the highest weight.

````markdown
<!-- INSERT: Shared Header Block -->

## Evaluation Context

**Decision to be made**: [What selection this evaluation supports]
**Decision timeline**: [When a decision is needed]
**Decision reversibility**: [High / Medium / Low — cost of switching later]
**Upstream landscape reference**: [research_id of landscape mapping, if any]

## Options Under Evaluation

| # | Option | Source | Why Included |
|---|--------|--------|-------------|
| 1 | [Option A] | [From landscape / user-specified / recommended] | [Brief rationale] |
| 2 | [Option B] | [Source] | [Rationale] |
| 3 | [Option C] | [Source] | [Rationale] |

## Evaluation Criteria

| # | Criterion | Weight | Description | Measurement Approach |
|---|-----------|--------|-------------|---------------------|
| 1 | [Criterion A] | [0.XX] | [What this measures] | [How to evaluate] |
| 2 | [Criterion B] | [0.XX] | [Description] | [Approach] |
| 3 | [Criterion C] | [0.XX] | [Description] | [Approach] |
| | **Total** | **1.00** | | |

## Decision Sensitivity Questions

- Under what conditions does the recommendation change?
- What is the realistic migration cost if the selection proves wrong in 12 months?
- Which criteria weight changes would flip the recommendation?

## Coverage Areas (Pattern-Specific)

| Coverage Area | Focus |
|---------------|-------|
| Per-option feature analysis | Detailed capability assessment per option per criterion |
| Scoring evidence | Source-attributed evidence for each score |
| Sensitivity analysis | How weight changes affect the recommendation |
| Hidden dependencies | Second-order effects of choosing each option |
| Migration cost | Realistic switching costs if selection proves wrong |

<!-- INSERT: Shared Prompt Slots Block -->

### Manifest: Pattern-Specific Metadata

```yaml
  pattern_metadata:
    evaluation_criteria:
      - criterion: "[Criterion A]"
        weight: 0.XX
        description: "[What this measures]"
      - criterion: "[Criterion B]"
        weight: 0.XX
        description: "[Description]"
    options_under_evaluation:
      - "[Option A]"
      - "[Option B]"
      - "[Option C]"
    key_questions:
      - "[Supplementary question 1]"
      - "[Supplementary question 2]"
```

<!-- INSERT: Shared Consolidation Manifest Block (with pattern_metadata above) -->
<!-- INSERT: Shared Post-Research Block -->
````

---

### Pattern Template 3: Implementation Pattern (`implementation_pattern`)

Assembles: Shared Header + Implementation-Specific Sections + Shared Prompt Slots + Shared Manifest + Shared Post-Research.

**Primary Deliverable**: Architecture decision catalog (context -> options -> decision -> consequences) + implementation pattern catalog (by phase/component) + anti-pattern register (failure mode -> root cause -> detection signal).

**Default Consolidation Mode**: `depth_first`

**Confidence Tiering**: Applies to each architecture decision and pattern recommendation. Tier 1: pattern validated by multiple production deployments. Tier 2: used in production but limited scale evidence. Tier 3: theoretically sound or single case.

````markdown
<!-- INSERT: Shared Header Block -->

## Architecture Context

**Current stack**: [Existing technology stack and architecture]
**Target component**: [What is being implemented]
**Integration points**: [How this connects to the existing system]

## Hard Constraints

| # | Constraint | Source | Impact |
|---|-----------|--------|--------|
| 1 | [Constraint A] | [User-specified / inherited from upstream] | [What this eliminates or requires] |
| 2 | [Constraint B] | [Source] | [Impact] |
| 3 | [Constraint C] | [Source] | [Impact] |

## Implementation Scope

**Architecture decisions needed**: [List of decisions to be made — e.g., event-driven vs. request-response, monolith vs. microservices]
**Implementation phases expected**: [High-level phasing if known]
**Target environment**: [Production environment details — cloud, runtime, scale expectations]

## Coverage Areas (Pattern-Specific)

| Coverage Area | Focus |
|---------------|-------|
| Architecture decision catalog | Context, options, decision, consequences for each key decision |
| Implementation pattern catalog | Proven patterns organized by phase/component |
| Anti-pattern register | Failure modes with root cause analysis and detection signals |
| Operational considerations | Monitoring, scaling, cost at production scale |
| Implementation sequence | Realistic build order with common stumbling points |

<!-- INSERT: Shared Prompt Slots Block -->

### Manifest: Pattern-Specific Metadata

```yaml
  pattern_metadata:
    architecture_context: "[Current architecture description]"
    constraint_list:
      - "[Constraint A]"
      - "[Constraint B]"
    key_questions:
      - "[Supplementary question 1]"
      - "[Supplementary question 2]"
```

<!-- INSERT: Shared Consolidation Manifest Block (with pattern_metadata above) -->
<!-- INSERT: Shared Post-Research Block -->
````

---

### Pattern Template 4: Best Practices (`best_practices`)

Assembles: Shared Header + Best Practices-Specific Sections + Shared Prompt Slots + Shared Manifest + Shared Post-Research.

**Primary Deliverable**: 8-dimension knowledge base (Environmental Context, Idiomatic Patterns, Anti-Patterns & Guardrails, Testing & Validation, Dependencies & Versions, Operational Awareness, Decision Trees, Escape Hatches) + Quick Reference Card + Cross-Domain Synthesis.

**Default Consolidation Mode**: `gap_driven`

**Confidence Tiering**: Applies per dimension. Tier 1: dimension thoroughly covered with cross-validated practitioner consensus. Tier 2: covered but limited sources or contested practices. Tier 3: sparse or rapidly changing.

**Output Template**: See Section 4 for the full Best Practices output template used by the merge prompt.

````markdown
<!-- INSERT: Shared Header Block -->

## Technology Context

**Technology**: [Specific technology being studied]
**Technology family**: [serverless / databases / frontend_frameworks / infrastructure_as_code / api_development / ci_cd_pipelines / ai_ml_platforms / mobile / ai_agent_frameworks / unknown]
**Version/runtime**: [Specific version or runtime being targeted]
**Downstream use**: [Claude Code skill / code generation / team reference / other]

## Dimension Weights

| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Environmental Context & Setup | [high/medium/low] | [Why this weight for this technology] |
| Idiomatic Patterns | [high/medium/low] | [Rationale] |
| Anti-Patterns & Guardrails | [high/medium/low] | [Rationale] |
| Testing & Validation | [high/medium/low] | [Rationale] |
| Dependencies & Version Management | [high/medium/low] | [Rationale] |
| Operational Awareness | [high/medium/low] | [Rationale] |
| Decision Trees | [high/medium/low] | [Rationale] |
| Escape Hatches & Known Issues | [high/medium/low] | [Rationale] |

## Coverage Areas (Pattern-Specific)

Coverage maps directly to the 8 dimensions. All models cover all dimensions (full overlap for cross-validation).

| Coverage Area | Focus |
|---------------|-------|
| Environmental Context | Runtime, project structure, config, auth, secrets |
| Idiomatic Patterns | How experienced practitioners do it vs. merely-functional approaches |
| Anti-Patterns | What fails, why, and how to detect it |
| Testing & Validation | Unit, integration, pre-deploy validation, known test gaps |
| Dependencies & Versions | Package recommendations, avoidances, pinning, upgrades |
| Operational Awareness | Logging, cost model, scaling, cold start, monitoring |
| Decision Trees | Key architectural decisions with branching logic |
| Escape Hatches | Bugs, limitations, workarounds, expiration dates |

<!-- INSERT: Shared Prompt Slots Block -->

### Manifest: Pattern-Specific Metadata

```yaml
  pattern_metadata:
    technology_family: [family_enum]
    dimension_weights:
      environmental_context: [high/medium/low]
      idiomatic_patterns: [high/medium/low]
      anti_patterns: [high/medium/low]
      testing_validation: [high/medium/low]
      dependencies_versions: [high/medium/low]
      operational_awareness: [high/medium/low]
      decision_trees: [high/medium/low]
      escape_hatches: [high/medium/low]
    key_questions:
      - "[Supplementary question 1]"
      - "[Supplementary question 2]"
```

<!-- INSERT: Shared Consolidation Manifest Block (with pattern_metadata above) -->
<!-- INSERT: Shared Post-Research Block -->
````

---

### Pattern Template 5: Competitive Intelligence (`competitive_intelligence`)

Assembles: Shared Header + CI-Specific Sections + Shared Prompt Slots + Shared Manifest + Shared Post-Research.

**Primary Deliverable**: Per-competitor strategic profile (moat analysis, strengths/vulnerabilities, likely next moves) + competitive dynamics analysis (forces reshaping the space) + positioning recommendations.

**Default Consolidation Mode**: `adversarial`

**Confidence Tiering**: Applies to each strategic claim per competitor. Tier 1: supported by public evidence (financials, launches, hiring). Tier 2: inferred from patterns with moderate evidence. Tier 3: speculative or based on thin signals.

````markdown
<!-- INSERT: Shared Header Block -->

## Intelligence Scope

**Subject company/product**: [What we are analyzing competitive dynamics for]
**Competitive frame**: [The specific market/segment where competition occurs]
**Strategic question**: [The core strategic question driving this analysis]

## Competitors Under Analysis

| # | Competitor | Category | Why Included |
|---|-----------|----------|-------------|
| 1 | [Competitor A] | [Direct / Indirect / Emerging] | [Rationale] |
| 2 | [Competitor B] | [Category] | [Rationale] |
| 3 | [Competitor C] | [Category] | [Rationale] |

## Analysis Dimensions

| Dimension | Description |
|-----------|-------------|
| Moat durability | How defensible is their position? What structural factors sustain or erode it? |
| Strategic positioning | Where do they claim to play vs. where they actually win? |
| Likely next moves | What are they probably going to do in 6-12 months? |
| Vulnerabilities | Where are they structurally weak? |
| Differentiation substance | Where is differentiation genuine vs. marketing claim? |
| Competitive dynamics | Pricing pressure, feature convergence, ecosystem effects |

## Coverage Areas (Pattern-Specific)

| Coverage Area | Focus |
|---------------|-------|
| Per-competitor strategic profiles | Moat, strengths, vulnerabilities, trajectory |
| Competitive dynamics analysis | Forces reshaping the space |
| Differentiation audit | Genuine vs. claimed differentiation |
| Positioning recommendations | Strategic response options |
| Signal detection | Early warning indicators for competitive shifts |

<!-- INSERT: Shared Prompt Slots Block -->

### Manifest: Pattern-Specific Metadata

```yaml
  pattern_metadata:
    competitors:
      - "[Competitor A]"
      - "[Competitor B]"
      - "[Competitor C]"
    analysis_dimensions:
      - moat
      - positioning
      - pricing
      - features
      - strategy
      - team
    key_questions:
      - "[Supplementary question 1]"
      - "[Supplementary question 2]"
```

<!-- INSERT: Shared Consolidation Manifest Block (with pattern_metadata above) -->
<!-- INSERT: Shared Post-Research Block -->
````

---

### Pattern Template 6: Market Research (`market_research`)

Assembles: Shared Header + Market-Specific Sections + Shared Prompt Slots + Shared Manifest + Shared Post-Research.

**Primary Deliverable**: Market sizing (TAM/SAM/SOM with methodology and confidence) + segmentation framework (definitions, sizes, growth rates, attractiveness ranking) + market dynamics analysis.

**Default Consolidation Mode**: `standard`

**Confidence Tiering**: Applies to market sizing estimates and segment boundaries. Tier 1: from multiple analyst reports or primary data. Tier 2: from single source or extrapolation. Tier 3: estimated by model reasoning without primary sources.

````markdown
<!-- INSERT: Shared Header Block -->

## Market Scope

**Market definition**: [What market is being sized and analyzed]
**Geographic scope**: [Global / Regional / Country-specific]
**Time horizon**: [Current + N-year forecast]
**Sizing methodology preference**: [Top-down / Bottom-up / Both]

## Segmentation Hypothesis

Before research, hypothesize market segments for validation:

| # | Segment | Description | Expected Size Rank |
|---|---------|-------------|-------------------|
| 1 | [Segment A] | [Who is in this segment] | [Largest / Medium / Smallest] |
| 2 | [Segment B] | [Description] | [Rank] |
| 3 | [Segment C] | [Description] | [Rank] |

## Key Sizing Questions

- What is the TAM/SAM/SOM and what methodology yields the most defensible estimate?
- Which segments are growing fastest and why?
- What are the barriers to entry and incumbent advantages?
- What demand drivers and inhibitors are shaping this market?

## Coverage Areas (Pattern-Specific)

| Coverage Area | Focus |
|---------------|-------|
| Market sizing (TAM/SAM/SOM) | Size estimates with methodology and confidence ranges |
| Segmentation framework | Segment definitions, sizes, growth rates, attractiveness |
| Demand dynamics | Drivers, inhibitors, trend lines |
| Entry barriers | Structural advantages, switching costs, regulatory |
| Entry strategy options | Approaches to enter given market structure |

<!-- INSERT: Shared Prompt Slots Block -->

### Manifest: Pattern-Specific Metadata

```yaml
  pattern_metadata:
    key_questions:
      - "[Market sizing question]"
      - "[Segmentation question]"
      - "[Dynamics question]"
```

<!-- INSERT: Shared Consolidation Manifest Block (with pattern_metadata above) -->
<!-- INSERT: Shared Post-Research Block -->
````

---

### Pattern Template 7: User Research (`user_research`)

Assembles: Shared Header + User Research-Specific Sections + Shared Prompt Slots + Shared Manifest + Shared Post-Research.

**Primary Deliverable**: Persona profiles (demographics, goals, frustrations, current solutions, unmet needs) + JTBD map (functional/emotional/social jobs with satisfaction gaps) + ranked unmet needs hierarchy.

**Default Consolidation Mode**: `depth_first`

**Confidence Tiering**: Applies to each persona and need claim. Tier 1: need validated by multiple independent sources. Tier 2: single-source evidence. Tier 3: inferred from behavioral signals without direct validation. Workaround analysis is high-signal.

````markdown
<!-- INSERT: Shared Header Block -->

## User Research Scope

**Target users**: [Who are the users being studied]
**Domain/product context**: [What solutions or product area]
**Research focus**: [Jobs-to-be-done / Pain points / Decision criteria / Behavioral patterns / All]
**Source strategy**: [Reviews, forums, studies, surveys, community discussions]

## Persona Hypothesis

Before research, hypothesize personas for validation:

| # | Persona | Description | Hypothesized Primary Job |
|---|---------|-------------|-------------------------|
| 1 | [Persona A] | [Brief description] | [What they are hiring a solution to do] |
| 2 | [Persona B] | [Description] | [Primary job] |

## JTBD Framework

| Job Type | Description |
|----------|-------------|
| Functional | What task are users trying to accomplish? |
| Emotional | How do users want to feel during and after? |
| Social | How do users want to be perceived by others? |

## Coverage Areas (Pattern-Specific)

| Coverage Area | Focus |
|---------------|-------|
| Persona profiles | Demographics, goals, frustrations, current solutions |
| Jobs-to-be-done mapping | Functional, emotional, social jobs with satisfaction gaps |
| Unmet needs hierarchy | Ranked by frequency x intensity x solution gap |
| Workaround analysis | What users build themselves — reveals what solutions miss |
| Decision criteria | What drives adoption and switching behavior |

<!-- INSERT: Shared Prompt Slots Block -->

### Manifest: Pattern-Specific Metadata

```yaml
  pattern_metadata:
    key_questions:
      - "[JTBD question]"
      - "[Behavioral pattern question]"
      - "[Unmet needs question]"
```

<!-- INSERT: Shared Consolidation Manifest Block (with pattern_metadata above) -->
<!-- INSERT: Shared Post-Research Block -->
````

---

### Pattern Template 8: Economic Analysis (`economic_analysis`)

Assembles: Shared Header + Economic-Specific Sections + Shared Prompt Slots + Shared Manifest + Shared Post-Research.

**Primary Deliverable**: Financial model (cost model + value/revenue model + ROI calculation) + sensitivity analysis (key variable x impact table) + benchmark comparison.

**Default Consolidation Mode**: `confidence_weighted`

**Confidence Tiering**: Applies to each cost and value estimate. Tier 1: from primary data or multiple corroborating sources. Tier 2: single benchmark or extrapolation. Tier 3: modeled assumption without external validation. Sensitivity analysis must identify which Tier 3 assumptions, if wrong, flip the recommendation.

````markdown
<!-- INSERT: Shared Header Block -->

## Economic Analysis Scope

**Decision context**: [What investment or financial decision this analysis supports]
**Analysis type**: [ROI / TCO / Cost-Benefit / Pricing / Break-even / Full business case]
**Time horizon**: [Over what period — 1 year / 3 years / 5 years]
**Comparison baseline**: [What is the current state or alternative being compared against]

## Cost Categories

| Category | Expected Components | Confidence Expectation |
|----------|-------------------|----------------------|
| Direct costs | [License, infrastructure, API usage] | [High — usually well-documented] |
| Implementation costs | [Development, migration, training] | [Medium — varies by context] |
| Hidden costs | [Opportunity cost, maintenance, integration tax] | [Low — require active hunting] |
| Ongoing operational | [Monitoring, support, updates] | [Medium — requires production data] |

## Value/Revenue Drivers

| Driver | Measurement Approach | Confidence Expectation |
|--------|---------------------|----------------------|
| [Value driver 1] | [How to quantify] | [High/Medium/Low] |
| [Value driver 2] | [Approach] | [Confidence] |

## Sensitivity Analysis Framework

Identify the 3-5 assumptions with the largest impact on the financial outcome. For each:
- Base case, optimistic, and pessimistic values
- Impact on overall ROI/TCO when varied independently
- Whether the assumption flips the recommendation

## Coverage Areas (Pattern-Specific)

| Coverage Area | Focus |
|---------------|-------|
| Cost model | Total cost of ownership with hidden cost hunting |
| Value/revenue model | Quantified value drivers with confidence ranges |
| ROI calculation | Payback period, IRR under multiple scenarios |
| Sensitivity analysis | Key variable x impact table |
| Benchmark comparison | Industry benchmarks and comparable implementations |

<!-- INSERT: Shared Prompt Slots Block -->

### Manifest: Pattern-Specific Metadata

```yaml
  pattern_metadata:
    key_questions:
      - "[TCO question]"
      - "[ROI/payback question]"
      - "[Sensitivity question]"
      - "[Benchmark question]"
```

<!-- INSERT: Shared Consolidation Manifest Block (with pattern_metadata above) -->
<!-- INSERT: Shared Post-Research Block -->
````

---

### Pattern Template 9: Compliance & Requirements (`compliance_requirements`)

Assembles: Shared Header + Compliance-Specific Sections + Shared Prompt Slots + Shared Manifest + Shared Post-Research.

**Primary Deliverable**: Requirements register (functional + non-functional requirements from regulatory, each with source regulation, interpretation confidence, implementation notes) + constraint map (technical, organizational, temporal) + governance recommendations.

**Default Consolidation Mode**: `gap_driven`

**Confidence Tiering**: Applies to each regulatory interpretation. Tier 1: based on explicit regulatory text or authoritative guidance. Tier 2: based on industry consensus or case law. Tier 3: ambiguous or jurisdiction-specific with limited precedent. Tier 3 items require legal review -- flag prominently.

````markdown
<!-- INSERT: Shared Header Block -->

## Compliance Scope

**Jurisdictions**: [List of applicable jurisdictions — e.g., US, EU, UK, specific states]
**Data categories**: [What types of data are involved — PII, financial, health, children's]
**User types**: [Consumer, enterprise, government, mixed]
**Regulatory frameworks**: [Known applicable frameworks — GDPR, CCPA, HIPAA, SOC2, PCI-DSS, EU AI Act]
**Compliance objective**: [Minimum viable compliance / Gold standard / Audit readiness]

## Requirements Register Structure

Each requirement entry should capture:

| Field | Description |
|-------|-------------|
| Requirement ID | [REQ-001, REQ-002, ...] |
| Source regulation | [Which regulation imposes this] |
| Requirement text | [Specific requirement, paraphrased] |
| Tier | [Mandatory / Recommended / Industry standard] |
| Interpretation confidence | [Tier 1 / Tier 2 / Tier 3] |
| Implementation notes | [Technical approach to satisfy] |
| Legal review flag | [Yes if Tier 3 — requires human legal review] |

## Constraint Categories

| Category | Description |
|----------|-------------|
| Technical constraints | System architecture requirements imposed by regulation |
| Organizational constraints | Process, role, or governance requirements |
| Temporal constraints | Deadlines, retention periods, response time requirements |

## Coverage Areas (Pattern-Specific)

| Coverage Area | Focus |
|---------------|-------|
| Requirements register | All applicable requirements with source, tier, confidence |
| Technical constraint map | Architecture constraints from regulatory requirements |
| Governance recommendations | Organizational process and oversight requirements |
| Pending regulatory changes | Upcoming changes that could affect compliance posture |
| Audit trail requirements | What evidence and documentation must be maintained |

<!-- INSERT: Shared Prompt Slots Block -->

### Manifest: Pattern-Specific Metadata

```yaml
  pattern_metadata:
    key_questions:
      - "[Regulatory scope question]"
      - "[Constraint identification question]"
      - "[Governance question]"
      - "[Pending changes question]"
```

<!-- INSERT: Shared Consolidation Manifest Block (with pattern_metadata above) -->
<!-- INSERT: Shared Post-Research Block -->
````

---

## Section 2: SINGLE Mode Guidance

SINGLE mode uses only Claude Opus 4.6. Any pattern template above can be adapted for SINGLE mode by applying these modifications:

### Adaptations

1. **Model Mode**: Set to `SINGLE` in the header and manifest.
2. **Model Role Assignments**: Single row — Claude Opus 4.6 covers all roles (primary researcher + structured cataloger + recency validation).
3. **Coverage Matrix**: All areas assigned to `claude-opus-4-6` only. All `overlap_zone` values are `false` (no cross-validation possible).
4. **Prompt Slots**: Only Prompt 1 (Claude) is generated. Remove Prompts 2-4.
5. **Consolidation Strategy**: Set recommended mode to the pattern default but note: "Single-source execution — no cross-validation available. All findings are single-model and should be treated as lower confidence than DUAL/FULL equivalents."
6. **Manifest models list**: Single entry only.
7. **Post-Research: Merge Prompt**: Skip entirely — nothing to merge. Instead, include a self-review directive at the end of the Claude prompt:

```
After completing your analysis, perform a mandatory self-review:
1. Internal contradiction scan
2. Confidence tier audit — were claims stated with more confidence than evidence supports?
3. Reasoning chain validation — do causal claims survive scrutiny?
4. Coverage check — compare actual coverage against the research questions
5. Source diversity check — are you relying on the same few sources repeatedly?
6. Flag all claims that would benefit from cross-validation with a second model
```

8. **Post-Research Verification**: Emphasize verification items more strongly — single-source findings need more human verification.
9. **Freshness Model**: Same as multi-model. Note in staleness indicators that single-source findings decay faster.

### When to Use SINGLE Mode

- Quick, low-stakes research where time matters more than depth
- Topics where Claude's web search provides sufficient coverage alone
- Preliminary research to scope a subsequent DUAL/FULL effort
- Budget-constrained situations

### SINGLE Mode Limitations

- No cross-validation of claims across models
- No structured data breadth from Gemini
- No site-restricted deep dives from GPT-5.2
- Effective confidence ceiling is Tier 2 for all claims (single-source maximum)

---

## Section 3: Merge Prompt

This merge prompt is used after executing all research prompts. The user pastes it into a new Claude Opus 4.6 conversation along with:
1. The consolidation manifest YAML block from the research brief
2. All model research outputs (unabridged)

The merge prompt accepts the consolidation manifest as structured input and uses it to drive pattern-aware, provenance-weighted synthesis.

### Ready-to-Use Merge Prompt

````
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 32000  # Increase up to 128000 for comprehensive reports

You are consolidating research outputs from multiple AI models into a unified,
high-quality report. Your job is to merge, cross-validate, and synthesize --
not just concatenate.

## Step 0: Parse Consolidation Manifest

Look for a fenced YAML block containing `consolidation_manifest:` in the input.

**If manifest found**:
- Parse all fields. Use `pattern` for output template selection. Use
  `consolidation.recommended_mode` (or `user_override` if set) for
  consolidation mode. Use `models[].role` for provenance weighting.
  Use `coverage_matrix` for gap detection. Use `research_chain` for
  constraint propagation.
- Log: "Manifest detected. Pattern: [pattern]. Mode: [mode]."
- Run validation: confirm model_mode matches number of source outputs provided.

**If no manifest found**:
- Operate in standalone mode. Infer pattern from content. Use standard
  consolidation mode. Weight all sources equally. Log: "No manifest found.
  Operating in standalone mode with inferred configuration."

## Step 1: Identify Sources and Assign Provenance Weights

For each research output provided, identify the source model and assign
provenance weights based on the manifest's model configuration:

| Model Role | Weight Boost On | Weight Reduce On |
|------------|----------------|------------------|
| `primary_researcher` | Reasoning chains, causal claims, cross-domain synthesis, strategic insight | Raw data enumeration |
| `structured_cataloger` | Comprehensive listings, structured tables, citation density, breadth | Novel strategic claims |
| `targeted_investigator` | Claims from site-restricted domains, feature verification, repo-level detail | General market claims |
| `recency_validator` | Recent developments, current sentiment, temporal claims | Deep architectural reasoning |
| `deep_recency_investigator` | Extended recency analysis with depth | Historical pattern analysis |

Provenance channel hierarchy (descending trust, per reconciliation.md weights):
1. `internal_document` (1.5x) — claim grounded in uploaded context documents
2. `site_restricted` (1.3x) — claim sourced from restricted authoritative domain
3. `web_search` (1.0x) — claim from general web search with citation
4. `quick_validation` (0.7x) — claim from quick recency check
5. `unsourced_assertion` (0.3x) — claim without attribution

## Step 2: Triage Claims with Provenance Awareness

For every substantive claim across all inputs:

- **Factual assertions**: Require cross-validation across models. Weight by
  provenance channel. Flag discrepancies with source attribution.
- **Causal claims**: Map each model's reasoning chain. Weight
  `primary_researcher` higher. Note where logic diverges.
- **Quantitative data**: Flag discrepancies >10% between models. Favor
  `site_restricted` > `web_search` > `unsourced_assertion` sourced figures.
- **Recommendations**: Tag as model interpretation, not established fact.
  Weight by role appropriateness.
- **Unique insights**: Preserve with source attribution. These are high-value.
  Note the model role and provenance channel.

### Citation Deduplication

When multiple models cite the same underlying source:
- Merge into a single citation entry with the most complete metadata.
- Note which models independently found the source (strengthens confidence).
- Do not double-count as "cross-validation" — same source through multiple
  models is corroboration of source importance, not independent verification.

### Claim Dependency Tracking

Map claim dependencies — claims that build on or assume other claims:
```
Claim A (Tier 1) ← supports ← Claim B (Tier 2) ← supports ← Claim C (Tier 3)
```
If a foundational claim's confidence drops, cascade the impact upward.
Flag dependency chains where a Tier 3 foundation supports Tier 1 conclusions.

## Step 3: Resolve Disagreements with Provenance Weighting

```
Conflict detected between models
├── Can claims coexist? (different scope, time, context)
│   └── Yes → Preserve both with context boundary. Not a true conflict.
│
├── Provenance comparison:
│   ├── One claim site_restricted, other unsourced?
│   │   └── Strongly favor site_restricted source.
│   ├── One claim web_search with citation, other reasoning?
│   │   └── Favor cited claim; preserve reasoning as interpretation.
│   └── Both equivalently sourced?
│       └── Continue to model count...
│
├── Model count agreement:
│   ├── [FULL] 2+ of 3 agree with evidence?
│   │   └── Note majority view; preserve minority with source.
│   ├── [DUAL] Both disagree with comparable evidence?
│   │   └── Flag "contested; verification priority"
│   └── All diverge?
│       └── Flag "unresolved; requires verification"
│
└── Role appropriateness check:
    └── Is the conflicting claim within the model's assigned role strength?
        ├── Yes → Weight that model's view higher for this claim type.
        └── No → Note but weight lower.
```

## Step 4: Audit for False Confidence

For unanimous claims on topics flagged in the manifest's risk assessment:

- **Citation diversity**: Different primary sources, or same source recycled
  through multiple models? Check for citation deduplication results.
- **Specificity**: Verifiable claim or vague assertion?
- **Recency**: Could this have changed since sources were written? Check
  against manifest's `freshness.staleness_indicators`.
- **Contrarian check**: Does credible dissent exist?
- **Mechanism clarity**: Do sources explain WHY, not just WHAT?
- **Provenance depth**: Is confidence grounded in `site_restricted` or
  `web_search` evidence, or just `reasoning`?

## Step 5: Assign Confidence Tiers

Use the pattern-specific confidence tiering approach from the manifest's
pattern type:

- **Tier 1 (>75%)**: Cross-model agreement + quality citations + specific/verifiable
  + appropriate provenance channel
- **Tier 2 (50-75%)**: Partial agreement or moderate citations or single
  high-quality source
- **Tier 3 (<50%)**: Single-source, contested, poorly cited, or `reasoning`-only
  provenance

Apply the pattern's specific tiering lens:
- `landscape_mapping`: Confidence = category completeness
- `comparative_evaluation`: Confidence = per-criterion per-option score quality
- `implementation_pattern`: Confidence = production validation depth
- `best_practices`: Confidence = per-dimension coverage quality
- `competitive_intelligence`: Confidence = evidence vs. speculation ratio
- `market_research`: Confidence = sizing methodology quality
- `user_research`: Confidence = behavioral evidence depth
- `economic_analysis`: Confidence = estimate source quality
- `compliance_requirements`: Confidence = regulatory interpretation authority

## Step 6: Synthesize Cross-Domain Patterns (Mandatory)

After primary merge, perform cross-domain synthesis:
- What structural patterns from unrelated domains map to these findings?
- Where does conventional framing miss something an outsider would catch?
- What emergent properties arise from constraint interactions?
- What would need to be true for the consensus view to be wrong?

This section is mandatory. If no cross-domain patterns are found, explicitly
state why (e.g., "Domain is narrow and technical; cross-domain analogies
would be forced rather than insightful").

## Step 7: Self-Review (Mandatory Before Finalizing)

1. **Internal contradiction scan**: Do claims in one section contradict another?
2. **Confidence tier audit**: Did any claim's confidence shift during writing?
   Update the tier and note the change.
3. **Reasoning chain validation**: Do causal claims survive scrutiny?
4. **Coverage check**: Compare actual coverage against the manifest's
   `coverage_matrix.areas`. Flag any area with no coverage or thin coverage.
5. **Cross-domain synthesis check**: Was Step 6 genuinely attempted?
6. **Constraint propagation check**: If `research_chain.inherited_constraints`
   exist, do any findings contradict them? Flag contradictions prominently.
7. **Claim dependency audit**: Are there Tier 1 conclusions resting on
   Tier 3 foundations? Flag and adjust.

## Step 8: Produce "For Downstream" Section

After consolidation, produce an actionability section formatted for the
pattern's typical next step (from `research_chain.downstream_expected`):

- If downstream is `comparative_evaluation`: format key findings as
  evaluation criteria inputs and shortlist candidates.
- If downstream is `implementation_pattern`: format as architecture
  constraints, technology selections, and scope boundaries.
- If downstream is `best_practices`: format as technology context,
  dimension priorities, and key investigation areas.
- If downstream is `competitive_intelligence`: format as player shortlist
  with initial strategic hypotheses.
- If downstream is `economic_analysis`: format as cost categories,
  value drivers, and sizing inputs.
- If no downstream planned: format as "Key constraints established" +
  "Would change conclusions if" + "Recommended refresh trigger."

## Step 9: Report Quality Metrics

At the end of the consolidated output, include:

```
## Consolidation Quality Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Coverage ratio | [X/Y areas covered] | [Areas from coverage_matrix with actual coverage / total areas] |
| Conflict resolution rate | [X/Y conflicts resolved] | [Resolved vs. flagged-for-verification] |
| Provenance depth | [% claims with web_search or site_restricted sourcing] | [Higher is better] |
| Cross-validation strength | [X overlap zones with agreement / total overlap zones] | [From coverage_matrix overlap_zone areas] |
| Actionability score | [High/Medium/Low] | [Does the "For Downstream" section provide concrete next-step inputs?] |
| Freshness risk | [Low/Medium/High] | [Based on time since execution vs. topic_volatility] |
| Confidence distribution | [Tier 1: X%, Tier 2: Y%, Tier 3: Z%] | [Proportion of claims at each tier] |
```

## Output Format

**Select output template based on manifest `pattern` field**:

- `best_practices` → Use the Best Practices Knowledge Base template
  (Section 4 of output-templates.md): 8-dimension structure with Executive
  Summary, Quick Reference Card, Cross-Domain Synthesis, Self-Review.

- All other patterns → Use this structure:

# Consolidated Research: [Topic]

**Research ID**: [From manifest]
**Pattern**: [Pattern Name] (`[pattern_id]`)
**Model Mode**: [DUAL/FULL] ([Models used])
**Consolidation Mode**: [Mode used]
**Research Period**: [Date range from executed_at timestamps]

## Executive Summary
[2-3 paragraphs: Key findings, strategic implications, overall confidence.]

**Key convergent findings:**
1. **[Finding 1]** (Tier [X]) -- [One-line summary]
2. **[Finding 2]** (Tier [X]) -- [One-line summary]
3. **[Finding 3]** (Tier [X]) -- [One-line summary]

## Part 1: [Major Topic Area 1]

### 1.1 [Subtopic]

<high_confidence>
[Claims with strong cross-model agreement AND quality citations.
Include provenance: "[Model role] via [channel]"]
</high_confidence>

<moderate_confidence>
[Partial agreement or moderate citations. Note caveats inline.]
</moderate_confidence>

<contested>
**[Model A role] view**: [Position + reasoning + sources]
**[Model B role] view**: [Position + sources]
**[Model C role] view**: [Position + context] (if FULL mode)
**Assessment**: [How to interpret; what would resolve it]
**Provenance comparison**: [Which source type is stronger here]
</contested>

[Continue for all Parts...]

## Cross-Cutting Analysis

### Comparison Matrix
| Dimension | [Option A] | [Option B] | Best For |
|-----------|------------|------------|----------|

### Decision Matrix
| Task/Scenario | Optimal Choice | Decisive Factor |
|---------------|----------------|-----------------|

### Cross-Domain Synthesis
<cross_domain_synthesis>
[Patterns from unrelated domains, emergent interactions, blind spots]
</cross_domain_synthesis>

## Self-Review Results
<self_review>
[Contradictions found, tier adjustments, reasoning validation, coverage gaps,
constraint propagation results, claim dependency audit]
</self_review>

## For Downstream
<for_downstream>
**Target**: [downstream_expected.pattern or "standalone"]

**Key constraints established**:
- [Constraint 1]
- [Constraint 2]

**Inputs for next research phase**:
- [Formatted for downstream pattern's needs]

**Would change conclusions if**:
- [Key assumption 1 proves false]
- [Key external change occurs]

**Recommended refresh trigger**: [When to re-run this research]
</for_downstream>

## Consolidation Quality Metrics
[Table from Step 9]

## Appendix A: Methodology
<methodology>
**Research ID**: [From manifest]
**Model mode**: [DUAL/FULL]
**Consolidation mode**: [Mode with rationale]
**Pattern**: [Pattern with confidence tiering approach used]
**Context tier**: [Standard/Extended/Chunked]
**Models and roles**: [List with capabilities]
**Verification priorities**: [From manifest]
**Inherited constraints**: [From research chain]
</methodology>

---

## Research Outputs to Merge

Paste the FULL, unabridged outputs below. Do not pre-summarize.

### Consolidation Manifest
[PASTE MANIFEST YAML BLOCK HERE]

### Claude Opus 4.6 Output
[PASTE HERE]

---

### Gemini 3.1 Pro Deep Research Output
[PASTE HERE]

---

### GPT-5.2 Deep Research Output (if FULL mode)
[PASTE HERE]

---

### GPT-5.2 Chat Output (if FULL mode, if used)
[PASTE HERE]
````

---

## Section 4: Best Practices Output Template

When the pattern is `best_practices`, the merge prompt produces output in this 8-dimension knowledge base structure. This template is well-validated and serves as the primary input for Claude Code skill generation via the `research-to-rules-transformer` pipeline.

````markdown
# Best Practices Knowledge Base: [TECHNOLOGY]

**Research ID**: [From manifest]
**Researched**: [Date]
**Sources**: Claude Opus 4.6 web research + Gemini 3.1 Pro Deep Research [+ GPT-5.2 if FULL]
**Technology Family**: [From manifest pattern_metadata.technology_family]
**Scope**: [Brief scope statement]
**Downstream use**: [Claude Code skill / code generation / team reference]

---

### Executive Summary

[2-3 paragraphs: Key takeaways, current state of the technology, most critical things a developer must know]

---

### 1. Environmental Context & Setup

**Runtime**: [Version(s), requirements]
**Project Structure**: [Recommended layout]
**Configuration**:
- [Key config items with recommended values and rationale]

**IAM / Authentication**: [Platform-specific auth patterns]
**Secrets Management**: [How to handle secrets properly]

**Confidence**: [Tier 1/Tier 2/Tier 3 with basis]

---

### 2. Idiomatic Patterns

#### Pattern: [Pattern Name]
**Context**: When to use this pattern
**Implementation**: How experienced practitioners implement it
**Why this way**: The reasoning behind the idiomatic approach
**Performance impact**: Measurable difference vs. naive approach

[Repeat for each key pattern]

**Confidence**: [Tier 1/Tier 2/Tier 3 with basis]

---

### 3. Anti-Patterns & Guardrails

#### Anti-Pattern: [Name]
**What developers do**: [The common mistake]
**Why it fails**: [Root cause -- at what scale, through what mechanism]
**Correct approach**: [What to do instead]
**Detection**: [How to spot this in existing code]

[Repeat for each anti-pattern]

**Confidence**: [Tier 1/Tier 2/Tier 3 with basis]

---

### 4. Testing & Validation

**Unit Testing**: [Framework, patterns, mocking approach]
**Integration Testing**: [Emulator/service setup, test patterns]
**Pre-Deploy Validation**: [Checks to run before deploying]
**Known Test Gaps**: [What's hard or impossible to test locally]

**Confidence**: [Tier 1/Tier 2/Tier 3 with basis]

---

### 5. Dependencies & Version Management

| Package | Recommended Version | Purpose | Notes |
|---------|-------------------|---------|-------|
| [pkg] | [version] | [purpose] | [compatibility notes] |

**Packages to Avoid**: [List with reasons]
**Version Pinning Strategy**: [Approach and rationale]
**Upgrade Considerations**: [What to watch for]

**Confidence**: [Tier 1/Tier 2/Tier 3 with basis]

---

### 6. Operational Awareness

**Logging**: [Platform-specific conventions and structured logging format]
**Cost Model**: [Key cost drivers, optimization strategies, things that surprise people]
**Scaling**: [Behavior under load, concurrency limits, timeout ceilings]
**Cold Start**: [Mitigation strategies -- if applicable]
**Monitoring**: [What to monitor, recommended alerting thresholds]

**Confidence**: [Tier 1/Tier 2/Tier 3 with basis]

---

### 7. Decision Trees

#### Decision: [Decision Name]
```
[Condition A]?
  |-- Yes -> [Approach 1] because [reason]
  |-- No -> [Condition B]?
        |-- Yes -> [Approach 2] because [reason]
        |-- No -> [Approach 3] because [reason]
```

[Repeat for each key architectural decision]

**Confidence**: [Tier 1/Tier 2/Tier 3 with basis]

---

### 8. Escape Hatches & Known Issues

#### Issue: [Description]
**Status**: [Open bug / documented limitation / undocumented behavior]
**Workaround**: [Current workaround]
**Expiration**: [When this may be resolved -- version, timeline, or "indefinite"]
**Source**: [Where this was identified -- GitHub issue, community report, etc.]

[Repeat for each known issue]

**Confidence**: [Tier 1/Tier 2/Tier 3 with basis]

---

### Integration Patterns

| Paired Service | Pattern | Notes |
|---------------|---------|-------|
| [Service A] | [How they connect] | [Key considerations] |

---

### Quick Reference Card

**Do**:
- [Most critical "do" items -- max 7]

**Don't**:
- [Most critical "don't" items -- max 7]

**Check First**:
- [Items to verify before starting -- max 5]

---

### Cross-Domain Synthesis

<cross_domain_synthesis>
1. **[Pattern]** (from [domain]): [How it maps, where analogy holds/breaks, actionable insight]
2. **[Pattern]** (from [domain]): [Same structure]

**Emergent constraint interactions**: [Non-obvious interactions creating implications not in any individual section]
**What conventional framing misses**: [Blind spots in standard thinking]
</cross_domain_synthesis>

---

### Self-Review Results

<self_review>
**Internal contradictions found**: [None / List with resolutions]
**Confidence tier adjustments**: [None / "Claim X: Tier Y->Z because..."]
**Reasoning chains that didn't survive scrutiny**: [None / List]
**Coverage gaps vs. planned dimensions**: [None / List with follow-up]
**Claim dependency issues**: [None / "Conclusion X rests on Tier 3 assumption Y"]
</self_review>

---

### Coverage Gaps

| Expected Coverage | Status | Impact | Recommended Action |
|-------------------|--------|--------|-------------------|
| [Dimension/Area] | [Not/Partially covered] | [Impact] | [Action] |

### Version Stamps

| Section | Last Validated | Source Recency | Section Volatility |
|---------|---------------|----------------|-------------------|
| [Section name] | [Date] | [Newest source date] | [From per_section_volatility] |

### Freshness Model

| Attribute | Value |
|-----------|-------|
| **Topic volatility** | [From manifest] |
| **Confidence half-life** | [From manifest] |
| **Recommended refresh** | [From manifest] |
| **Staleness indicators** | [From manifest] |

### For Downstream

<for_downstream>
**Target**: [downstream_expected.pattern or "Claude Code skill generation"]

**Key constraints established**:
- [Constraint 1]
- [Constraint 2]

**Skill generation inputs** (if downstream = Claude Code skill):
- Technology: [technology]
- Critical rules: [top 5 rules from anti-patterns + idiomatic patterns]
- Decision trees: [key decisions for skill routing]
- Escape hatches: [active workarounds to encode]

**Would change conclusions if**:
- [Key assumption 1 proves false]
- [New version released with breaking changes]

**Recommended refresh trigger**: [When to re-run this research]
</for_downstream>

### Consolidation Quality Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Coverage ratio | [X/8 dimensions covered] | [Which dimensions thin or missing] |
| Conflict resolution rate | [X/Y conflicts resolved] | |
| Provenance depth | [% claims with web_search or site_restricted sourcing] | |
| Cross-validation strength | [X/8 dimensions with cross-model agreement] | |
| Actionability score | [High/Medium/Low] | [Does the Quick Reference Card + Decision Trees provide actionable guidance?] |
| Freshness risk | [Low/Medium/High] | [Based on topic_volatility and time since execution] |
| Confidence distribution | [Tier 1: X%, Tier 2: Y%, Tier 3: Z%] | [Per-dimension breakdown available in sections] |
````
