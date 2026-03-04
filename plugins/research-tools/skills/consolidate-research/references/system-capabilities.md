# System Capabilities Reference

**Version**: 1.0  |  **Last validated**: 2026-03-04
**Consumed by**: consolidate-research (freshness modeling, chain management, quality reporting)

---

## Section 1: Temporal Confidence Model

### Purpose

Research findings decay in reliability at different rates. This model estimates when
consolidated findings should be refreshed.

### Volatility Classification

| Volatility | Half-Life | Typical Topics | Refresh Cadence |
|------------|-----------|----------------|-----------------|
| **Critical** | 1 month | Pricing, breaking changes, live competitive moves | Weekly monitor, monthly refresh |
| **High** | 3 months | AI/ML tools, startup landscape, emerging regulations | Monthly monitor, quarterly refresh |
| **Medium** | 6 months | Market sizing, competitive positioning, tech adoption | Quarterly monitor, semi-annual refresh |
| **Low** | 12 months | Implementation patterns (mature tech), established practices | Semi-annual monitor, annual refresh |
| **Stable** | 24+ months | Compliance frameworks, architectural principles, stable APIs | Annual monitor, refresh on major event |

### Pattern x Volatility Defaults

| Pattern | Default | Increase If | Decrease If |
|---------|---------|-------------|-------------|
| `landscape_mapping` | High | Startup-heavy / AI-adjacent market | Mature consolidated market; high entry barriers |
| `comparative_evaluation` | High | Options include pre-1.0 or AI tools | All options enterprise-mature with stable APIs |
| `implementation_pattern` | Medium-Low | Framework < 2yr; monthly breaking changes | Framework > 5yr; LTS release track |
| `best_practices` | Medium | Technology < 2yr; community debate on patterns | Technology > 5yr; codified in official guides |
| `competitive_intelligence` | High | VC-funded startups; market disruption | Public companies; stable positioning 2+ yr |
| `market_research` | Medium | Emerging market (AI, crypto, climate) | Established market; stable growth trajectory |
| `user_research` | Medium | Rapidly adopting new technology | Fundamental needs; stable product category |
| `economic_analysis` | High | Usage-based pricing; volatile input costs | Fixed depreciation; stable enterprise licensing |
| `compliance_requirements` | Low-Medium | Active regulatory proceedings | Established framework (SOC2, PCI-DSS) |

### Staleness Indicator Library

Observable signals that findings may no longer be accurate. When any fires, evaluate affected sections.

**Version / Release**

| Indicator | Strength | Example |
|-----------|----------|---------|
| New major version release | High | Framework v2 released; patterns may shift |
| API deprecation announced | High | Vendor deprecates evaluated endpoint |
| Breaking change in dependency | Medium | Upstream library incompatible change |
| End-of-life announcement | High | Evaluated option reaches EOL |

**Market**

| Indicator | Strength | Example |
|-----------|----------|---------|
| Significant M&A activity | High | Key landscape player acquired |
| New funded entrant | Medium | Competitor raises Series A in space |
| Pricing model change | High | Vendor switches per-seat to usage-based |
| Market exit or shutdown | High | Player shuts down; inventory invalid |

**Regulatory**

| Indicator | Strength | Example |
|-----------|----------|---------|
| New regulation enacted | High | EU AI Act enforcement date reached |
| Enforcement action taken | High | Fine sets new data-handling precedent |
| Regulatory guidance issued | Medium | Agency publishes interpretation guidance |

**Technology**

| Indicator | Strength | Example |
|-----------|----------|---------|
| Benchmark breakthrough | High | New architecture obsoletes evaluated approach |
| New platform capability | Medium | Cloud provider launches native replacement |
| Open-source alternative emerges | Medium | OSS reaches production readiness in category |

**Competitive**

| Indicator | Strength | Example |
|-----------|----------|---------|
| Competitor strategic pivot | High | Competitor exits market or changes focus |
| Major feature launch | Medium | Competitor closes identified capability gap |
| Partnership announcement | Medium | Alliance shifts ecosystem dynamics |

### Freshness Model Generation Protocol

1. Determine `topic_volatility` from Pattern x Volatility Defaults, adjusted by signals.
2. Set `confidence_half_life` from Volatility Classification.
3. Compute `recommended_refresh` = `research_date` + `confidence_half_life`.
4. Select 3-5 staleness indicators most relevant to the topic/pattern.
5. Assess per-section volatility where sections age at different rates.

```yaml
freshness_model:
  research_id: "[from manifest]"
  pattern: "[pattern_id]"
  topic_volatility: "[critical|high|medium|low|stable]"
  confidence_half_life: "[1m|3m|6m|12m|24m]"
  research_date: "YYYY-MM-DD"
  recommended_refresh: "YYYY-MM-DD"
  staleness_indicators:
    - type: "[version_release|market|regulatory|technology|competitive]"
      description: "What specific event to watch for"
      monitoring: "How to detect — e.g., 'check vendor changelog monthly'"
  per_section_volatility:
    - section: "[section_name]"
      volatility: "[may differ from overall]"
      reason: "Why this section ages differently"
```

**Example** (Best Practices on Google ADK):

```yaml
freshness_model:
  research_id: "adk-best-practices-20260301"
  pattern: "best_practices"
  topic_volatility: "high"
  confidence_half_life: "3m"
  research_date: "2026-03-01"
  recommended_refresh: "2026-06-01"
  staleness_indicators:
    - type: "version_release"
      description: "ADK new major version or breaking API change"
      monitoring: "Watch github.com/google/adk-python releases monthly"
    - type: "technology"
      description: "Competing framework achieves feature parity"
      monitoring: "Monitor LangGraph, CrewAI release notes quarterly"
  per_section_volatility:
    - section: "Dependencies & Versions"
      volatility: "critical"
      reason: "ADK pre-1.0; pinning changes each release"
    - section: "Decision Trees"
      volatility: "medium"
      reason: "Architectural decisions more stable than API surface"
```

---

## Section 2: Research Chain Protocol

### Purpose

When research is conducted in sequence (e.g., Landscape -> Comparative ->
Implementation), each consolidation should build on and validate against predecessors.

### Chain Detection

```
Manifest received for consolidation
|
+-- manifest.research_chain.upstream_id exists?
|   |
|   +-- YES --> Request upstream consolidated output
|   |           |
|   |           +-- File available?
|   |               +-- YES --> Ingest as context; run validation; extract constraints
|   |               +-- NO  --> Warn "upstream not found"; proceed; flag chain_integrity
|   |
|   +-- NO  --> Check conversation history for prior consolidations
|               on related topics (same product, overlapping domain)
|               |
|               +-- Found? --> YES: Offer to link as upstream
|               |              NO:  Proceed as standalone consolidation
```

### Chain Validation Rules

**Landscape -> Comparative**

| Check | On Failure |
|-------|-----------|
| All Comparative options appear in Landscape inventory | Flag new options as "emerged after landscape research" |
| Landscape categories inform evaluation criteria | Note if criteria ignore a relevant dimension |
| Market structure findings are consistent | Flag contradictions in dynamics vs. assumptions |

Propagate: taxonomy, player attributes, white space, ecosystem dynamics.

**Comparative -> Implementation**

| Check | On Failure |
|-------|-----------|
| Implementation targets the selected option | If user diverged from recommendation, note explicitly |
| Evaluation criteria map to success metrics | Flag criteria without implementation validation |
| Identified risks appear as watchpoints | Flag unaddressed risks from Comparative |

Propagate: selection rationale, criteria, risks, runner-up options.

**Market -> Competitive**

| Check | On Failure |
|-------|-----------|
| Market segments consistent across both | Reconcile or explain segment mismatches |
| Market sizing bounds share estimates | Flag if shares imply inconsistent market size |

Propagate: segment definitions, sizing, demand drivers, entry barriers.

**Market -> User Research**

| Check | On Failure |
|-------|-----------|
| Target segments define User Research scope | Flag populations outside defined segments |
| Segment sizes calibrate need frequency | Flag inconsistent frequency vs. segment size |

Propagate: segment definitions, sizing, buying criteria.

**Competitive -> Market**

| Check | On Failure |
|-------|-----------|
| Landscape consistent with market structure | Flag contradictory concentration data |
| Aggregate shares bounded by TAM | Flag if shares exceed market sizing |

Propagate: competitor positioning, shares, dynamics, moat-derived barriers.

**Any -> Best Practices**

| Check | On Failure |
|-------|-----------|
| Tech choices from prior research scope practices | Flag coverage of unselected technology |
| Architecture decisions weight dimensions | Note if weighting ignores upstream context |

Propagate: technology selection, architecture decisions, constraints.

### Constraint Propagation

From upstream output, extract four categories:

| Category | Extract | Use Downstream |
|----------|---------|---------------|
| **Decisions** | Selections made ("selected Option B") | Scope downstream; note if findings would change decision |
| **Constraints** | Hard limits ("must support HIPAA") | Apply as filters; flag violations |
| **Assumptions** | Stated beliefs ("market growing at 15%") | Validate; flag contradictions explicitly |
| **Open Questions** | Unresolved ("pricing unconfirmed") | Attempt resolution; report status |

When downstream contradicts upstream, produce a **Chain Conflict Notice**:

```
CHAIN CONFLICT: [finding] contradicts upstream [constraint|assumption]
  Upstream: [statement, research_id]
  Downstream: [finding, evidence]
  Impact: [what changes if downstream is correct]
  Recommendation: [re-validate | accept downstream | flag for decision-maker]
```

### Chain Metadata

```yaml
research_chain:
  chain_id: "[product]-[topic]-chain"
  position: 2
  sequence:
    - research_id: "[upstream_id]"
      pattern: "landscape_mapping"
      status: "consolidated"
      key_decisions: ["Identified 4 categories, shortlisted 5 options"]
      key_constraints: ["Must integrate with existing GCP infrastructure"]
      key_assumptions: ["Market consolidation expected within 18 months"]
      open_questions: ["Pricing for Player X unconfirmed"]
    - research_id: "[this_id]"
      pattern: "comparative_evaluation"
      status: "in_progress"
      inherits: ["5-option shortlist", "GCP constraint", "consolidation assumption"]
  planned_next:
    - pattern: "implementation_pattern"
      trigger: "After selection confirmed by stakeholder"
  chain_conflicts: []
```

---

## Section 3: Quality Metrics Framework

### Purpose

Measurable quality signals for consolidated research. Every consolidation should
produce a quality report. Metrics enable cross-consolidation comparison and process improvement.

### Metric Definitions

#### 1. Coverage Ratio (target: > 90%)

| | |
|---|---|
| **Definition** | Proportion of input claims addressed in output (included, synthesized, or excluded with reason) |
| **Calculation** | `claims_addressed / total_claims_in_inputs` |
| **> 90%** | Comprehensive; minimal information loss |
| **80-90%** | Acceptable; review for unintentional omissions |
| **< 80%** | Significant loss; re-examine normalization for missed claims |
| **< 60%** | Critical; likely skipped entire source sections |
| **Improve** | Check deduplication aggression, section-level skipping, undocumented scope narrowing |

#### 2. Conflict Resolution Rate (target: > 70%)

| | |
|---|---|
| **Definition** | Proportion of source conflicts resolved (preferred with rationale, synthesized, or designated genuine disagreement) |
| **Calculation** | `conflicts_resolved / conflicts_identified` |
| **> 70%** | Most tensions resolved; remaining are genuinely unresolvable |
| **50-70%** | Acceptable if unresolved conflicts are flagged with context |
| **< 50%** | Too many unresolved; consider Agentic consolidation mode |
| **Improve** | Use adversarial mode; distinguish assumption-based vs. evidence-based disagreement |

Note: not all conflicts SHOULD be resolved. Genuine expert disagreement is valid data.

#### 3. Provenance Depth (target: > 60%)

| | |
|---|---|
| **Definition** | % of Tier 1 claims with multi-source corroboration from independent primary sources |
| **Calculation** | `tier1_with_independent_corroboration / total_tier1_claims` |
| **> 60%** | Tier 1 well-corroborated; confidence tiers credible |
| **40-60%** | Some Tier 1 claims may be over-classified |
| **< 40%** | Run citation dedup audit; Tier 1 likely overassigned |
| **Improve** | Use FULL mode for source diversity; dedup citations across models |

#### 4. Actionability Score (target: > 50%)

| | |
|---|---|
| **Definition** | % of findings connected to a downstream workflow step, tool, or decision |
| **Calculation** | `findings_with_downstream_connection / total_findings` |
| **> 50%** | Research is decision-enabling |
| **30-50%** | Partially actionable; some findings informational-only |
| **< 30%** | Research informational but not actionable |
| **Improve** | Frame research questions as decision-oriented; review pattern downstream connections |

#### 5. Staleness Risk (target: < 20%)

| | |
|---|---|
| **Definition** | % of claims with source dates older than topic volatility threshold |
| **Calculation** | `stale_source_claims / total_dated_claims` (stale = age > half-life) |
| **< 20%** | Predominantly fresh; reliable |
| **20-40%** | Moderate risk; identify affected sections |
| **> 40%** | High risk; run targeted refresh cycle |
| **Improve** | Prioritize recent-data models; use per-section staleness analysis |

#### 6. Dependency Chain Integrity (target: > 80%)

| | |
|---|---|
| **Definition** | % of recommendation chains where all supporting claims are Tier 2+ |
| **Calculation** | `fully_validated_chains / total_recommendation_chains` |
| **> 80%** | Recommendations well-supported; trustworthy |
| **60-80%** | Acceptable; flag recommendations with Tier 3 dependencies |
| **< 60%** | Under-supported; elevated decision risk |
| **Improve** | Targeted verification on Tier 3 claims in recommendation chains |

#### 7. Cross-Domain Synthesis Index (target: >= 2)

| | |
|---|---|
| **Definition** | Count of novel insights connecting findings across distinct domains |
| **Calculation** | Count (not percentage); each must span 2+ domains |
| **>= 2** | Consolidation adds analytical value beyond aggregation |
| **1** | Minimal synthesis; may be too mechanical |
| **0** | Synthesis pass skipped or ineffective |
| **Improve** | Explicit synthesis pass; look for cross-category patterns and contradictions |

### Quality Report Template

```yaml
quality_metrics:
  coverage_ratio:
    value: 0.00
    detail: "X of Y claims addressed"
    excluded_with_reason: 0
    unaddressed: 0
  conflict_resolution_rate:
    value: 0.00
    detail: "X of Y conflicts resolved"
    unresolved: ["topic 1", "topic 2"]
  provenance_depth:
    value: 0.00
    detail: "X of Y Tier 1 claims independently corroborated"
    citation_dedup_needed: false
  actionability_score:
    value: 0.00
    detail: "X of Y findings connected to downstream workflow"
    target_tools: ["tool or skill name"]
  staleness_risk:
    value: 0.00
    detail: "X of Y claims with sources older than [threshold]"
    at_risk_sections: ["section name"]
    undated_claims: 0
  dependency_chain_integrity:
    value: 0.00
    detail: "X of Y recommendation chains fully validated"
    at_risk_recommendations:
      - recommendation: "[text]"
        weakest_link: "[Tier 3 claim]"
  cross_domain_synthesis:
    insights_generated: 0
    examples: ["insight 1", "insight 2"]
  overall_grade: "A"
  # A: All 7 metrics at target
  # B: 1-2 metrics below target
  # C: 3+ metrics below target
  # D: coverage_ratio < 0.60 OR dependency_chain_integrity < 0.60
```

### Grade Calculation

```
IF coverage_ratio < 0.60 OR dependency_chain_integrity < 0.60:
    grade = D
ELSE:
    below_target = count of:
        coverage_ratio < 0.90, conflict_resolution_rate < 0.70,
        provenance_depth < 0.60, actionability_score < 0.50,
        staleness_risk > 0.20, dependency_chain_integrity < 0.80,
        cross_domain_synthesis < 2
    0 below     -> A
    1-2 below   -> B
    3+ below    -> C
```

---

## Cross-Section Integration

1. **Temporal Model -> Quality Metrics**: `confidence_half_life` sets the staleness threshold.
2. **Chain Protocol -> Quality Metrics**: Chain validation failures degrade integrity score.
3. **Quality Metrics -> Temporal Model**: Grade C/D triggers earlier refresh than `recommended_refresh`.
4. **Chain Metadata -> Freshness Model**: Upstream nearing refresh date flags downstream staleness risk.
