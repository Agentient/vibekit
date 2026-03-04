# Research Pattern Registry

**Version**: 1.0
**Last validated**: 2026-03-04
**Consumed by**: create-research-brief (classification + prompt generation), consolidate-research (template selection + reconciliation logic)

---

## Quick Reference

| ID | Pattern | Purpose (one line) | Default Consolidation | Volatility |
|---|---|---|---|---|
| `landscape_mapping` | Landscape Mapping | Discover and categorize the complete universe of players/solutions in a domain | breadth_first | High |
| `comparative_evaluation` | Comparative Evaluation | Compare known options against weighted criteria for a selection decision | confidence_weighted | High |
| `implementation_pattern` | Implementation Pattern | Synthesize how-to knowledge from real-world architecture decisions and production use | depth_first | Medium-Low |
| `best_practices` | Best Practices | Build an 8-dimension technology knowledge base for practitioner use | gap_driven | Medium |
| `competitive_intelligence` | Competitive Intelligence | Analyze strategic positioning, moat sustainability, and competitive dynamics | adversarial | High |
| `market_research` | Market Research | Size, segment, and analyze market dynamics to inform entry strategy | standard | Medium |
| `user_research` | User Research | Map jobs-to-be-done, behavioral patterns, and unmet needs for a target segment | depth_first | Medium |
| `economic_analysis` | Economic Analysis | Model ROI, TCO, cost-benefit, and financial feasibility with sensitivity ranges | confidence_weighted | High |
| `compliance_requirements` | Compliance & Requirements | Catalog regulatory constraints, governance frameworks, and audit requirements | gap_driven | Low-Medium |

---

## Pattern Definitions

---

### 1. Landscape Mapping (`landscape_mapping`)

**Purpose**: Produces a taxonomy and comprehensive inventory of all players, solutions, or approaches in a domain — the map that subsequent patterns navigate.

**Trigger Signals**:
- Explicit: "map the landscape", "who are the players", "what's out there", "survey the space", "catalog all options", "ecosystem overview"
- Implicit: "I need to understand the ecosystem", "what options exist", "before I compare I need to know what to compare", "is there anything I'm missing"

**Key Questions Template**:
1. What are the major categories of [TOPIC] in [DOMAIN], and how should they be classified?
2. Who are all significant players in each category, and what are their key attributes (maturity, funding, positioning)?
3. Where are the white spaces — categories or segments with few or no solutions?
4. What are the ecosystem dynamics — partnerships, integrations, platform effects, M&A trends?
5. How is this landscape likely to evolve over the next 12-18 months?

**Primary Deliverable**: Taxonomy (category definitions) + player inventory (per-category structured table) + white space map.

**Confidence Tiering Approach**: Confidence applies to **category completeness**. Tier 1: category fully mapped with high-confidence player inventory. Tier 2: category identified but player list may be incomplete. Tier 3: category suspected but poorly sourced, or players unverified.

**Default Consolidation Mode**: `breadth_first` — Landscape Mapping prioritizes completeness over depth. Lead with Gemini's comprehensive inventory, enrich with Claude's structural analysis. Missing a player is worse than shallow analysis of a known one.

**Topic Volatility Heuristic**:
- AI/startup landscapes → High (3-month). New entrants, pivots, and funding events reshape weekly.
- Enterprise/regulated landscapes → Medium (6-month). Players change slowly but positioning shifts.
- Mature technology landscapes → Low (12-month). Categories and major players are stable.

**Sequencing Relationships**:
- Common predecessors: `market_research` (segments define landscape scope)
- Common successors: `comparative_evaluation` (shortlist from landscape), `competitive_intelligence` (deep-dive on key players)
- Constraint inheritance from predecessors: Market Research defines target segments → Landscape scope limited to those segments. Market sizing bounds → calibrates player scale expectations.
- Example chain: `market_research` → `landscape_mapping` → `comparative_evaluation` (size the market, map who's in it, select from it)

**Downstream Connections**:
- **Spark**: White space map feeds opportunity identification
- **Prism**: Landscape becomes reference dataset for ongoing monitoring
- **Ignite**: Player inventory informs competitive positioning in GTM
- **Foundry**: Taxonomy categories inform product categorization decisions
- Claude Code skills: landscape data feeds competitive monitoring agents

**Anti-Patterns**:
- **Confused with Competitive Intelligence**: Landscape *discovers the universe*; Competitive Intelligence *analyzes known players' strategic positions*. If the user already knows who the competitors are, they want CI, not landscape.
- **Confused with Comparative Evaluation**: Landscape is wide and shallow (who exists); Comparative is narrow and deep (which is best for us). If the user says "compare X and Y", they've already done the landscape implicitly.
- **Over-scoping**: "Map everything in AI" → too broad. Landscape needs a bounded domain. Push for specificity: "Map AI-powered product acceleration tools targeting startup founders."

---

### 2. Comparative Evaluation (`comparative_evaluation`)

**Purpose**: Produces a weighted decision matrix comparing known options, with a defensible recommendation grounded in evidence quality — the analysis that supports a selection decision.

**Trigger Signals**:
- Explicit: "compare X vs Y vs Z", "which should I choose", "evaluate the options", "selection criteria", "decision matrix", "trade-off analysis"
- Implicit: "should I go with X or Y", "which is better for our use case", "help me decide between", "what are the trade-offs"

**Key Questions Template**:
1. How do [OPTIONS] compare against [CRITERIA] with [WEIGHTS] applied?
2. What are the hidden dependencies or second-order effects of choosing each option?
3. Where does the recommendation change if criteria weights shift — what is the decision sensitivity?
4. What would make the runner-up the better choice — under what conditions does the recommendation flip?
5. What is the realistic migration cost if the selection proves wrong in 12 months?

**Primary Deliverable**: Weighted comparison matrix (options × criteria with scores, confidence per cell, source attribution) + decision recommendation with sensitivity analysis.

**Confidence Tiering Approach**: Confidence applies to **each criterion score per option**. Tier 1: score backed by multiple sources with quality citations. Tier 2: score from single source or moderate evidence. Tier 3: score estimated or poorly sourced. Overall recommendation confidence is a function of the lowest-confidence criterion with the highest weight.

**Default Consolidation Mode**: `confidence_weighted` — Selection decisions demand evidence quality. Weigh findings by citation quality and source authority. A well-sourced minority finding should override a poorly-sourced majority.

**Topic Volatility Heuristic**:
- AI frameworks, dev tools → High (3-month). Feature sets change rapidly; today's gap is next month's release.
- Enterprise platforms, infrastructure → Medium (6-month). Core capabilities are stable; pricing and integration change.
- Commodity technologies, mature standards → Low (12-month). Comparison is durable.

**Sequencing Relationships**:
- Common predecessors: `landscape_mapping` (provides the shortlist to evaluate)
- Common successors: `implementation_pattern` (how to implement the selected option), `best_practices` (deep knowledge base for the selection), `economic_analysis` (financial feasibility of the selection)
- Constraint inheritance: Landscape provides the evaluation set → adding options not in the landscape requires justification. Landscape categories → inform evaluation criteria grouping.
- Example chain: `landscape_mapping` → `comparative_evaluation` → `implementation_pattern` (find options, select one, learn to build with it)

**Downstream Connections**:
- **Foundry**: Selection rationale becomes architecture decision record (ADR). Criteria → acceptance criteria for requirements.
- **Vantage**: Decision sensitivity feeds value engineering — which criteria have highest ROI impact.
- **Spark**: Runner-up options remain on radar for pivot scenarios.
- Claude Code skills: comparison matrix feeds vendor assessment templates

**Anti-Patterns**:
- **Confused with Landscape Mapping**: If the user doesn't know what options exist, they need a landscape first. "Compare the vendors in this space" is a landscape + comparative sequence, not pure comparative.
- **Missing criteria weights**: Comparison without weights produces analysis, not decisions. Push for explicit weights or derive from user's stated priorities.
- **Too many options**: >5 options dilutes depth. If >5, recommend a landscape → shortlist → comparative sequence.

---

### 3. Implementation Pattern (`implementation_pattern`)

**Purpose**: Produces architecture decisions with rationale, implementation patterns with trade-offs, and anti-patterns with root cause analysis — the knowledge needed to build correctly, not just to build.

**Trigger Signals**:
- Explicit: "how do I implement", "architecture patterns for", "implementation guide", "what's the right approach to build", "reference architecture"
- Implicit: "we've decided to use X, now how", "migration path from A to B", "production-ready patterns for", "what worked for others"

**Key Questions Template**:
1. What are the proven architecture patterns for [TOPIC] in [DOMAIN], and what are the trade-offs of each?
2. What decisions must be made before implementation, and what factors determine the right choice?
3. What anti-patterns have caused production failures, and what are their root causes?
4. What operational considerations (monitoring, scaling, cost) emerge only at production scale?
5. What does a realistic implementation sequence look like, and what are the common stumbling points?

**Primary Deliverable**: Architecture decision catalog (context → options → decision → consequences) + implementation pattern catalog (organized by phase/component) + anti-pattern register (failure mode → root cause → detection signal).

**Confidence Tiering Approach**: Confidence applies to **each architecture decision and pattern recommendation**. Tier 1: pattern validated by multiple production deployments with evidence. Tier 2: pattern used in production but limited evidence of scale. Tier 3: pattern theoretically sound or documented in a single case.

**Default Consolidation Mode**: `depth_first` — Implementation research needs the deepest reasoning on *why* patterns work, not just *what* patterns exist. Lead with Claude's analytical reasoning about trade-offs, validate with Gemini's catalog of reference implementations.

**Topic Volatility Heuristic**:
- Rapidly evolving frameworks (ADK, LangGraph) → High (3-month). APIs change, patterns shift.
- Established frameworks (React, PostgreSQL) → Low (12-month). Core patterns are stable.
- Infrastructure patterns (K8s, Terraform) → Medium (6-month). Best practices evolve with versions.

**Sequencing Relationships**:
- Common predecessors: `comparative_evaluation` (selected option determines implementation scope), `best_practices` (established patterns constrain implementation)
- Common successors: `best_practices` (deep-dive KB for the implementation), `economic_analysis` (implementation cost modeling)
- Constraint inheritance: Comparative Evaluation's selection → scopes implementation to chosen technology. Evaluation criteria → become implementation success metrics. Risks identified → become implementation watchpoints.
- Example chain: `comparative_evaluation` → `implementation_pattern` → `best_practices` (select ADK, learn architecture patterns, build deep knowledge base)

**Downstream Connections**:
- **Foundry**: Architecture decisions → ADRs. Implementation patterns → technical requirements. Anti-patterns → acceptance criteria (system must NOT exhibit X).
- **Academy**: Implementation sequence → tutorial structure. Decision trees → learning paths.
- Claude Code skills: implementation patterns are the primary input for skill generation (research-to-rules-transformer)

**Anti-Patterns**:
- **Confused with Best Practices**: Implementation Pattern asks "how do I architect this?" Best Practices asks "what do expert practitioners know about this technology across 8 dimensions?" Implementation is narrower (specific architecture) and deeper (decision rationale). Best Practices is broader (all operational knowledge).
- **Confused with Comparative Evaluation**: If the user hasn't decided what to implement, they need comparative first. "How should I implement an orchestration framework" presupposes a selection.
- **Skipping constraints**: Implementation without architecture context produces generic patterns. Push for: what's the current stack, what are the hard constraints?

---

### 4. Best Practices (`best_practices`)

**Purpose**: Produces an 8-dimension technology knowledge base (Environmental Context, Idiomatic Patterns, Anti-Patterns, Testing, Dependencies, Operational Awareness, Decision Trees, Escape Hatches) — the comprehensive practitioner reference that goes beyond documentation.

**Trigger Signals**:
- Explicit: "best practices for", "how should I use [TECHNOLOGY]", "what do experienced developers know about", "patterns and anti-patterns"
- Implicit: "I'm starting a project with [TECH]", "idiomatic way to", "what are the gotchas", "what would a senior engineer do differently"

**Key Questions Template**:
1. What does the expert practitioner know about [TOPIC] that isn't in the official documentation?
2. What are the idiomatic patterns vs. merely-functional approaches for [TOPIC]?
3. What fails at production scale, and what are the root causes?
4. What are the critical decision points, and what factors determine the right choice?
5. What are the known issues, workarounds, and escape hatches for [TOPIC]?

**Primary Deliverable**: 8-dimension knowledge base organized by: Environmental Context, Idiomatic Patterns, Anti-Patterns & Guardrails, Testing & Validation, Dependencies & Versions, Operational Awareness, Decision Trees, Escape Hatches. Includes Quick Reference Card and Cross-Domain Synthesis section.

**Confidence Tiering Approach**: Confidence applies **per dimension**. Tier 1: dimension thoroughly covered with cross-validated practitioner consensus. Tier 2: dimension covered but from limited sources or with some contested practices. Tier 3: dimension sparse or rapidly changing (common for Escape Hatches on new tech).

**Default Consolidation Mode**: `gap_driven` — The 8-dimension framework defines expected coverage explicitly. Gap-Driven mode audits actual coverage against all 8 dimensions, identifies missing areas, and prioritizes completeness. This is the only pattern with a pre-defined coverage checklist.

**Topic Volatility Heuristic**:
- New/rapidly evolving tech (Firebase v2, ADK) → High (3-month). Best practices shift with releases.
- Established tech (PostgreSQL, React) → Low (12-month). Core practices stable.
- Apply `technology-profiles.md` family heuristics for technology-specific estimation.
- **Per-dimension volatility varies**: Dependencies/Versions and Escape Hatches are almost always higher volatility than Idiomatic Patterns and Decision Trees.

**Sequencing Relationships**:
- Common predecessors: `comparative_evaluation` (selection determines which technology to deep-dive), `implementation_pattern` (architecture decisions scope which practices matter)
- Common successors: rarely has successors — it's typically the terminal research in a chain
- Constraint inheritance: Comparative Evaluation's selection → scopes to specific technology. Implementation Pattern's architecture decisions → scope which dimensions to weight heavily.
- Example chain: `comparative_evaluation` → `implementation_pattern` → `best_practices` (select tech, learn architecture, build knowledge base)

**Downstream Connections**:
- **Academy**: 8-dimension structure maps directly to educational chapter organization
- **Foundry**: Decision Trees → acceptance criteria. Anti-Patterns → negative requirements ("system must not…").
- Claude Code skills: **Primary input for skill generation**. Best Practices KB is consumed by `research-to-rules-transformer` to produce Claude Code skill assets (SKILL.md, rules, hooks).
- Flow: Knowledge base becomes persistent context document

**Anti-Patterns**:
- **Confused with Implementation Pattern**: Best Practices is technology-wide knowledge; Implementation Pattern is project-specific architecture. "Best practices for Firebase Cloud Functions" covers all 8 dimensions broadly. "How to implement event-driven architecture on Firebase Cloud Functions for Agentient" is an implementation pattern.
- **Skipping technology family**: Best Practices requires loading `technology-profiles.md` for dimension weighting. Without it, all 8 dimensions get equal weight, producing unbalanced coverage.
- **Treating as documentation**: Best Practices captures what's NOT in the docs — practitioner knowledge, failure modes, workarounds. If the answer is in the official docs, it's not a best practice finding.

---

### 5. Competitive Intelligence (`competitive_intelligence`)

**Purpose**: Produces strategic positioning analysis — moat durability, differentiation sustainability, and competitive dynamics for known players — the intelligence needed for strategic response, not just awareness.

**Trigger Signals**:
- Explicit: "competitive analysis", "analyze our competitors", "competitive moat", "how defensible is their position", "competitive dynamics"
- Implicit: "what are they doing that we're not", "can we differentiate against X", "are they a real threat", "what would make them pivot"

**Key Questions Template**:
1. How defensible is each competitor's position in [DOMAIN], and what structural factors sustain or erode their moat?
2. What are each competitor's likely strategic moves in the next 6-12 months based on their trajectory?
3. Where is [TOPIC/COMPANY] genuinely differentiated vs. where are they claiming differentiation without substance?
4. What competitive dynamics (pricing pressure, feature convergence, ecosystem effects) are reshaping the space?
5. Under what conditions would a competitor pivot to directly compete with us?

**Primary Deliverable**: Per-competitor strategic profile (moat analysis, strengths/vulnerabilities, likely next moves) + competitive dynamics analysis (forces reshaping the space) + positioning recommendations.

**Confidence Tiering Approach**: Confidence applies to **each strategic claim per competitor**. Tier 1: claim supported by public evidence (financial data, product launches, hiring patterns). Tier 2: claim inferred from patterns with moderate evidence. Tier 3: claim is speculative or based on thin signals.

**Default Consolidation Mode**: `adversarial` — Competitive Intelligence risks confirmation bias. Models may align on a narrative that fits expectations rather than evidence. Adversarial mode stress-tests alignment, applies false confidence audit, and identifies where the comfortable narrative breaks down.

**Topic Volatility Heuristic**:
- Startup/AI competitors → High (3-month). Strategy shifts with each funding round or pivot.
- Enterprise competitors → Medium (6-month). Strategy shifts quarterly; execution takes longer.
- Established market leaders → Low-Medium (6-12 months). Positioning is stable; watch for disruption signals.

**Sequencing Relationships**:
- Common predecessors: `landscape_mapping` (identifies who to analyze), `market_research` (market structure informs competitive dynamics)
- Common successors: `economic_analysis` (competitive pricing informs financial modeling), `user_research` (competitive gaps identify unmet needs to exploit)
- Constraint inheritance: Landscape provides the player set → CI analyzes a subset deeply. Market structure → informs competitive dynamics (consolidation trends, entry barriers).
- Example chain: `market_research` → `landscape_mapping` → `competitive_intelligence` (understand market, map players, analyze key threats)

**Downstream Connections**:
- **Ignite**: Positioning recommendations → GTM strategy. Differentiation matrix → sales messaging.
- **Spark**: Competitor vulnerabilities → opportunity identification for new features.
- **Vantage**: Competitive pricing data → value engineering inputs.
- **Foundry**: Competitive feature gaps → feature requirements.

**Anti-Patterns**:
- **Confused with Landscape Mapping**: CI assumes you know WHO the competitors are. If the user is still discovering options, they need a landscape first.
- **Confused with Comparative Evaluation**: CI analyzes *competitors' strategies* (their moats, their moves). Comparative Evaluation compares *options for your decision* (which tool should we use). CI is about them; Comparative is about us.
- **Feature fixation**: CI that catalogs features without analyzing strategic implications is just a feature matrix. Push for: "why does this feature exist, what does it signal about their strategy?"

---

### 6. Market Research (`market_research`)

**Purpose**: Produces market sizing (TAM/SAM/SOM), segmentation, demand dynamics, and entry strategy analysis — the quantitative foundation for business decisions about where to play.

**Trigger Signals**:
- Explicit: "market size", "TAM SAM SOM", "market segmentation", "market dynamics", "entry strategy", "market opportunity"
- Implicit: "is this a big enough market", "who would buy this", "how fast is this growing", "what's the addressable opportunity"

**Key Questions Template**:
1. What is the total, serviceable, and obtainable market size for [TOPIC] in [DOMAIN]?
2. How should this market be segmented, and which segments are most attractive?
3. What are the demand drivers and inhibitors — what forces are growing or shrinking this market?
4. What are the barriers to entry, and what structural advantages do incumbents hold?
5. What entry strategy optimizes for [OBJECTIVE] given the market structure?

**Primary Deliverable**: Market sizing (TAM/SAM/SOM with methodology and confidence) + segmentation framework (definitions, sizes, growth rates, attractiveness ranking) + market dynamics analysis.

**Confidence Tiering Approach**: Confidence applies to **market sizing estimates and segment boundaries**. Tier 1: sizing from multiple analyst reports or primary data, with consistent methodology. Tier 2: sizing from single source or extrapolated from adjacent data. Tier 3: sizing estimated by model reasoning without primary sources.

**Default Consolidation Mode**: `standard` — Market Research benefits from straightforward synthesis. Most findings are quantitative and reconcilable. Standard mode with confidence tiering handles the typical case of slightly different sizing estimates across sources.

**Topic Volatility Heuristic**:
- Emerging markets (AI tools, crypto) → High (3-month). Size and segments shifting rapidly.
- Established markets (SaaS, enterprise software) → Medium (6-month). Sizing is stable; growth rates shift.
- Mature markets (office supplies, commodity infra) → Low (12-month). Sizing is well-established.

**Sequencing Relationships**:
- Common predecessors: rarely has predecessors — often the first research in a chain
- Common successors: `landscape_mapping` (segments define landscape scope), `competitive_intelligence` (market structure informs competitive dynamics), `user_research` (segments define user populations)
- Constraint inheritance: N/A (typically first in chain)
- Example chain: `market_research` → `landscape_mapping` → `competitive_intelligence` (understand market, map it, analyze threats)

**Downstream Connections**:
- **Spark**: Market sizing validates opportunity size for ideation. Segments identify underserved niches.
- **Vantage**: TAM/SAM/SOM feeds business case and financial models.
- **Ignite**: Segment attractiveness → GTM targeting. Entry strategy → launch planning.
- **Foundry**: Segment definitions → persona foundations for requirements.

**Anti-Patterns**:
- **Confused with Landscape Mapping**: Market Research sizes and segments the market. Landscape Mapping catalogs who's in it. "How big is the market" = market research. "Who's in the market" = landscape.
- **Precision fallacy**: TAM/SAM/SOM estimates carry wide confidence intervals. Present ranges, not point estimates. A "$2.4B market" is really a "$1.8-3.2B market" with stated methodology.
- **Segment proliferation**: >6 segments reduces actionability. Push for 3-5 segments with clear differentiation criteria.

---

### 7. User Research (`user_research`)

**Purpose**: Produces persona profiles, jobs-to-be-done maps, behavioral pattern analysis, and ranked unmet needs — the human insight that grounds product decisions in actual user behavior, not assumptions.

**Trigger Signals**:
- Explicit: "user research", "persona development", "jobs to be done", "JTBD", "user needs", "pain points", "user behavior"
- Implicit: "who are our users really", "what do they actually need", "why do people use X instead of Y", "what frustrates users about"

**Key Questions Template**:
1. What are the primary jobs [USERS] are hiring [SOLUTIONS] to do in [DOMAIN] — functional, emotional, and social?
2. What are the behavioral patterns — how do users currently solve this problem, and where do existing solutions fail?
3. What are the unmet needs, ranked by frequency × intensity × solution gap?
4. What workarounds have users developed — and what do those workarounds reveal about what solutions miss?
5. What decision criteria drive adoption and switching behavior?

**Primary Deliverable**: Persona profiles (demographics, goals, frustrations, current solutions, unmet needs) + JTBD map (functional/emotional/social jobs with satisfaction gaps) + ranked unmet needs hierarchy.

**Confidence Tiering Approach**: Confidence applies to **each persona and need claim**. Tier 1: need validated by multiple independent sources (reviews, forums, studies). Tier 2: need identified from single-source evidence. Tier 3: need inferred from behavioral signals without direct validation. Workaround analysis is high-signal — users building workarounds is strong evidence of unmet need.

**Default Consolidation Mode**: `depth_first` — User Research requires the deepest reasoning about behavioral drivers and unmet needs. Surface-level need catalogs are low-value; the insight is in WHY users behave as they do. Lead with Claude's analytical depth.

**Topic Volatility Heuristic**:
- Rapidly adopting technologies → High (3-month). User behaviors shift as tools evolve.
- Established product categories → Medium (6-month). Core needs stable; expectations shift.
- Fundamental human needs → Low (12-month). JTBD at the functional level is durable.

**Sequencing Relationships**:
- Common predecessors: `market_research` (segments define user populations)
- Common successors: `comparative_evaluation` (user needs define evaluation criteria), `economic_analysis` (willingness-to-pay by segment)
- Constraint inheritance: Market Research segments → define which user populations to study. Market sizing → calibrates how many users experience each need.
- Example chain: `market_research` → `user_research` → `comparative_evaluation` (understand segments, understand needs, evaluate solutions against needs)

**Downstream Connections**:
- **Foundry**: Persona cards + JTBD maps → user stories, acceptance criteria, feature requirements
- **Spark**: Unmet needs hierarchy → opportunity scoring for ideation
- **Ignite**: Persona profiles → targeting and messaging in GTM
- **Academy**: User mental models → learning path design
- **Vantage**: Willingness-to-pay → pricing model inputs

**Anti-Patterns**:
- **Confused with Market Research**: Market Research asks "how big is the opportunity and how is it segmented?" User Research asks "what do people in those segments actually need?" Market is quantitative/structural; User is qualitative/behavioral.
- **Demographic fixation**: Personas defined only by demographics (age, title, company size) miss behavioral segmentation. Push for behavioral attributes: goals, frustrations, current solutions, decision criteria.
- **Assumption laundering**: Research that confirms pre-existing beliefs without surfacing contradictory evidence. Adversarial mode override recommended when user has strong priors about their users.

---

### 8. Economic Analysis (`economic_analysis`)

**Purpose**: Produces financial models (ROI, TCO, cost-benefit) with sensitivity analysis and confidence ranges — the quantitative business case that connects technical decisions to financial outcomes.

**Trigger Signals**:
- Explicit: "ROI analysis", "total cost of ownership", "cost-benefit", "financial model", "business case", "pricing analysis", "break-even"
- Implicit: "is this worth it", "how much will this cost us", "what's the payback period", "can we afford this", "justify the investment"

**Key Questions Template**:
1. What is the total cost of ownership for [TOPIC] over [TIMEFRAME], including hidden costs?
2. What are the quantifiable value drivers, and what confidence do we have in each estimate?
3. What is the ROI / payback period / IRR under base, optimistic, and pessimistic scenarios?
4. Which assumptions have the largest impact on the financial outcome — what's the sensitivity?
5. How does this compare to industry benchmarks and comparable implementations?

**Primary Deliverable**: Financial model (cost model + value/revenue model + ROI calculation) + sensitivity analysis (key variable × impact table) + benchmark comparison.

**Confidence Tiering Approach**: Confidence applies to **each cost and value estimate**. Tier 1: estimate from primary data or multiple corroborating sources. Tier 2: estimate from single benchmark or extrapolation. Tier 3: estimate is a modeled assumption without external validation. Sensitivity analysis must identify which Tier 3 assumptions, if wrong, flip the recommendation.

**Default Consolidation Mode**: `confidence_weighted` — Financial decisions require evidence quality. A single well-sourced cost figure outweighs three poorly-sourced ones. Citation quality scoring directly impacts the financial model's credibility.

**Topic Volatility Heuristic**:
- Cloud/SaaS pricing → High (3-month). Pricing changes quarterly; usage-based costs shift with architecture.
- Enterprise software TCO → Medium (6-month). License costs stable; implementation costs vary.
- Capital expenditure / infrastructure → Low (12-month). Hardware costs and depreciation are predictable.

**Sequencing Relationships**:
- Common predecessors: `comparative_evaluation` (selected option determines cost scope), `implementation_pattern` (architecture decisions determine cost drivers), `competitive_intelligence` (competitive pricing constrains pricing strategy)
- Common successors: rarely has successors — typically terminal in a chain, feeding into business decisions
- Constraint inheritance: Comparative Evaluation → scopes financial analysis to selected option. Implementation Pattern → identifies cost drivers. Competitive Intelligence → bounds pricing strategy.
- Example chain: `comparative_evaluation` → `implementation_pattern` → `economic_analysis` (select option, understand architecture, model the financials)

**Downstream Connections**:
- **Vantage**: **Primary consumer.** Financial model → Vantage's value engineering framework. Sensitivity analysis → risk assessment inputs.
- **Foundry**: Cost constraints → non-functional requirements (budget ceilings, performance-per-dollar).
- **Ignite**: Pricing analysis → GTM pricing strategy.
- **Spark**: ROI thresholds → feature prioritization by value.

**Anti-Patterns**:
- **Confused with Market Research**: Market Research sizes the market opportunity. Economic Analysis models the cost/benefit of a specific decision. TAM ≠ ROI.
- **False precision**: Presenting $1,247,832 when the confidence interval is ±40%. Present ranges, not point estimates. Include sensitivity tables showing what changes the answer.
- **Missing hidden costs**: Migration costs, training costs, opportunity costs, and integration maintenance are consistently underestimated. Economic Analysis should actively hunt for hidden costs through cross-domain pattern import.

---

### 9. Compliance & Requirements (`compliance_requirements`)

**Purpose**: Produces a regulatory requirements register, constraint map, and governance recommendations — the compliance foundation that prevents downstream rework and legal risk.

**Trigger Signals**:
- Explicit: "compliance requirements", "regulatory constraints", "data privacy", "governance framework", "audit requirements", "GDPR/HIPAA/SOC2"
- Implicit: "what are we legally required to do", "can we do X with user data", "what will auditors look for", "regulatory risk"

**Key Questions Template**:
1. What regulations apply to [TOPIC] in [JURISDICTIONS], and what are the specific requirements?
2. What are the compliance tiers — mandatory requirements vs. recommended practices vs. industry standards?
3. What technical and organizational constraints do these regulations impose?
4. What governance framework and audit trail requirements must the system satisfy?
5. What pending regulatory changes could affect our compliance posture in the next 12 months?

**Primary Deliverable**: Requirements register (functional + non-functional requirements from regulatory, each with source regulation, interpretation confidence, implementation notes) + constraint map (technical, organizational, temporal) + governance recommendations.

**Confidence Tiering Approach**: Confidence applies to **each regulatory interpretation**. Tier 1: interpretation based on explicit regulatory text or authoritative guidance. Tier 2: interpretation based on industry consensus or case law. Tier 3: interpretation is ambiguous or jurisdiction-specific with limited precedent. For compliance, Tier 3 items require legal review — flag prominently.

**Default Consolidation Mode**: `gap_driven` — Compliance research has an identifiable expected coverage (all applicable regulations, all required controls). Gap-Driven mode ensures nothing is missed. Missing a requirement is far worse than shallow analysis of a known one.

**Topic Volatility Heuristic**:
- AI regulation (EU AI Act, emerging US frameworks) → High (3-month). Rapidly evolving.
- Data privacy (GDPR, CCPA) → Medium (6-month). Framework stable; enforcement evolves.
- Established compliance (SOC2, ISO27001, PCI-DSS) → Low (12-month). Standards stable.

**Sequencing Relationships**:
- Common predecessors: `market_research` (target jurisdictions determine applicable regulations)
- Common successors: `implementation_pattern` (compliance requirements constrain architecture), `economic_analysis` (compliance costs feed financial model)
- Constraint inheritance: Market Research → target markets determine jurisdictions. Compliance requirements → constrain ALL subsequent technical decisions.
- Example chain: `market_research` → `compliance_requirements` → `implementation_pattern` (understand markets, understand regulatory constraints, architect within constraints)

**Downstream Connections**:
- **Foundry**: **Primary consumer.** Requirements register → functional and non-functional requirements. Constraint map → architecture constraints.
- **Vantage**: Compliance costs → TCO components in value engineering.
- **Academy**: Compliance requirements → training content for team enablement.
- **Flow**: Regulatory change monitoring → context updates.

**Anti-Patterns**:
- **Confused with Implementation Pattern**: Compliance tells you WHAT the constraints are. Implementation tells you HOW to build within them. "GDPR requires data portability" = compliance. "Here's how to implement data portability on Firebase" = implementation.
- **Jurisdiction ambiguity**: "We need to be compliant" without specifying jurisdictions produces generic guidance. Push for: which markets, which user types, which data categories.
- **Over-reliance on AI interpretation**: Compliance findings with Tier 3 confidence should include explicit "requires legal review" flags. AI can catalog and organize regulatory requirements; it cannot provide legal advice.

---

## Pattern Detection Decision Tree

```
User input received
│
├── Contains explicit comparison? ("compare X vs Y", "which is better",
│   "evaluate options", "trade-offs between")
│   └── Are the options already identified?
│       ├── YES (≥2 named options) ──────────── → comparative_evaluation
│       └── NO ("compare the options in this space")
│           └── Recommend sequence: landscape_mapping → comparative_evaluation
│
├── Asks about market size/opportunity? ("how big", "TAM", "market size",
│   "segments", "addressable market", "entry strategy")
│   └── ──────────────────────────────────────── → market_research
│
├── Asks about users/needs? ("user needs", "JTBD", "persona", "pain points",
│   "what do users want", "behavioral patterns")
│   └── ──────────────────────────────────────── → user_research
│
├── Asks about competitors strategically? ("competitive moat", "defensible",
│   "competitive dynamics", "positioning analysis", "what are they doing")
│   └── Are the competitors already identified?
│       ├── YES ─────────────────────────────── → competitive_intelligence
│       └── NO ("who are we competing against")
│           └── Recommend sequence: landscape_mapping → competitive_intelligence
│
├── Asks about financial feasibility? ("ROI", "TCO", "cost-benefit",
│   "business case", "worth the investment", "payback")
│   └── ──────────────────────────────────────── → economic_analysis
│
├── Asks about compliance/regulation? ("GDPR", "compliance", "regulatory",
│   "audit requirements", "data privacy", "governance")
│   └── ──────────────────────────────────────── → compliance_requirements
│
├── Asks about "who's out there" / ecosystem? ("map the landscape",
│   "ecosystem overview", "what options exist", "survey the space")
│   └── ──────────────────────────────────────── → landscape_mapping
│
├── Asks about how to build/implement? ("how do I implement", "architecture
│   for", "reference architecture", "implementation guide", "migration path")
│   └── Is the technology/option already selected?
│       ├── YES ─────────────────────────────── → implementation_pattern
│       └── NO ("how should I implement an orchestration framework")
│           └── Recommend sequence: comparative_evaluation → implementation_pattern
│
├── Asks about technology knowledge / practices? ("best practices for",
│   "idiomatic patterns", "gotchas", "what do experts know", "anti-patterns",
│   "patterns and practices for [TECHNOLOGY]")
│   └── Scope = specific technology? (not architecture/project)
│       ├── YES ─────────────────────────────── → best_practices
│       └── NO (project-specific architecture)
│           └── ──────────────────────────────── → implementation_pattern
│
└── Ambiguous / doesn't match above
    └── Check for compound intent:
        ├── "I'm entering a new market" → market_research (start) → landscape_mapping
        ├── "Should we build X?" → economic_analysis + implementation_pattern
        ├── "I need to understand everything about Y" → Ask: "Would you like
        │   to start with a landscape map, or do you already know the
        │   specific area to focus on?"
        └── Still unclear → Ask one clarifying question:
            "Are you trying to: (a) discover what exists, (b) choose between
             options, (c) learn how to build something, (d) understand the
             market opportunity, or (e) something else?"
```

### Compound Intent Resolution

| User Statement | Detected Intent | Recommended Action |
|---|---|---|
| "Compare the vendors in this space" | landscape + comparative | Sequence: `landscape_mapping` → `comparative_evaluation` |
| "Is this worth building?" | economic + implementation | Parallel: `economic_analysis` (feasibility) + `implementation_pattern` (complexity) |
| "How should we enter this market?" | market + landscape + competitive | Sequence: `market_research` → `landscape_mapping` → `competitive_intelligence` |
| "Help me build with X the right way" | implementation + best practices | Sequence: `implementation_pattern` → `best_practices` |
| "What are users doing and how can we win?" | user + competitive | Parallel: `user_research` + `competitive_intelligence` |
| "Is this compliant and financially viable?" | compliance + economic | Parallel: `compliance_requirements` + `economic_analysis` |

---

## Pattern Interrelationship Matrix

Reading: row pattern's relationship TO column pattern. Example: `market_research` PRECEDES `landscape_mapping`.

| | landscape | comparative | implementation | best_practices | competitive | market | user | economic | compliance |
|---|---|---|---|---|---|---|---|---|---|
| **landscape** | — | PRECEDES | — | — | PRECEDES | ENRICHES | — | — | — |
| **comparative** | — | — | PRECEDES | PRECEDES | ENRICHES | — | — | PRECEDES | — |
| **implementation** | — | — | — | PRECEDES | — | — | — | PRECEDES | — |
| **best_practices** | — | ENRICHES | ENRICHES | — | — | — | — | — | — |
| **competitive** | ENRICHES | ENRICHES | — | — | — | ENRICHES | ENRICHES | PRECEDES | — |
| **market** | PRECEDES | — | — | — | PRECEDES | — | PRECEDES | PRECEDES | PRECEDES |
| **user** | — | ENRICHES | — | — | ENRICHES | ENRICHES | — | ENRICHES | — |
| **economic** | — | — | — | — | — | — | — | — | — |
| **compliance** | — | CONSTRAINS | CONSTRAINS | CONSTRAINS | — | — | CONSTRAINS | PRECEDES | — |

### Key Relationships

| Relationship | Meaning | Example |
|---|---|---|
| **PRECEDES** | Pattern A's output is typically required before Pattern B can execute effectively | Market Research → Landscape Mapping: segments define landscape scope |
| **CONSTRAINS** | Pattern A's findings limit Pattern B's solution space | Compliance → Implementation: regulatory requirements eliminate architecture options |
| **ENRICHES** | Pattern A's output adds depth to Pattern B but is not required | Competitive Intelligence → Comparative Evaluation: competitor strategy context improves evaluation |
| **INDEPENDENT** | (blank cell) No typical relationship | Economic Analysis → Landscape Mapping: financial feasibility doesn't affect ecosystem mapping |

---

## Pattern × Consolidation Mode Defaults

| Pattern | Default Mode | Why Default | Override Trigger |
|---|---|---|---|
| `landscape_mapping` | breadth_first | Completeness over depth; missing a player costs more than shallow analysis | User says "deep-dive on key players" → depth_first |
| `comparative_evaluation` | confidence_weighted | Selection decisions demand evidence quality over source volume | User says "quick comparison" → standard |
| `implementation_pattern` | depth_first | WHY patterns work matters more than WHAT patterns exist | User says "comprehensive pattern catalog" → breadth_first |
| `best_practices` | gap_driven | 8-dimension framework defines expected coverage explicitly | User says "focus on anti-patterns only" → depth_first |
| `competitive_intelligence` | adversarial | Competitive analysis risks confirmation bias | User says "just the facts, skip analysis" → standard |
| `market_research` | standard | Quantitative findings are generally reconcilable across sources | User says "high-stakes investment decision" → confidence_weighted |
| `user_research` | depth_first | Behavioral insight requires deep reasoning about WHY | User says "broad needs survey" → breadth_first |
| `economic_analysis` | confidence_weighted | Financial decisions require evidence quality | User says "rough estimate is fine" → standard |
| `compliance_requirements` | gap_driven | Missing a requirement is worse than shallow analysis | User says "focus on highest-risk areas" → depth_first |

---

## Common Research Chains

### Product Development Chain (Agentient primary)
```
market_research → landscape_mapping → competitive_intelligence → comparative_evaluation → implementation_pattern → best_practices
```
Full chain: understand market → map players → analyze threats → select technology → learn architecture → build knowledge base.

### Technology Selection Chain
```
landscape_mapping → comparative_evaluation → economic_analysis → implementation_pattern
```
Find options → evaluate them → validate financially → learn how to build.

### Compliance-Gated Implementation
```
market_research → compliance_requirements → comparative_evaluation → implementation_pattern
```
Understand markets → establish constraints → evaluate within constraints → build within constraints.

### User-Driven Feature Development
```
user_research → comparative_evaluation → implementation_pattern → best_practices
```
Understand needs → evaluate solutions → architect implementation → build expertise.

### Market Entry Strategy
```
market_research → user_research → competitive_intelligence → economic_analysis
```
Size opportunity → understand users → assess competition → model financials.
