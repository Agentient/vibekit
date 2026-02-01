# MECE Decomposition Guide

A comprehensive reference for breaking research questions into Mutually Exclusive, Collectively Exhaustive (MECE) structures optimized for multi-LLM research.

---

## 1. Overview

### What is MECE?

MECE (Mutually Exclusive, Collectively Exhaustive) is a principle for organizing information:

| Property | Definition | Test |
|----------|------------|------|
| **Mutually Exclusive** | Categories don't overlap | No finding belongs to 2+ categories |
| **Collectively Exhaustive** | Categories cover everything | No relevant finding is uncategorized |

### Why MECE for Multi-LLM Research?

1. **Clear Model Assignment** — Each category maps to one primary model
2. **No Redundant Queries** — Avoids duplicate work across models
3. **Complete Coverage** — Ensures no research gaps
4. **Easy Consolidation** — Findings merge cleanly without overlap

### The 4 Standard Patterns

| Pattern | Use Case | Categories |
|---------|----------|------------|
| Market Research | Sizing, dynamics, trends | 5 categories |
| Competitive Intelligence | Company/product analysis | 5 categories |
| Technology Evaluation | Build/buy/adopt decisions | 5 categories |
| Strategic Research | Direction, options, planning | 5 categories |

---

## 2. Pattern 1: Market Research

### Purpose
Understand market size, structure, participants, and trajectory for market entry, expansion, or investment decisions.

### Category Structure

```
┌─────────────────────────────────────────────────────────────┐
│                    MARKET RESEARCH                          │
├─────────────┬─────────────┬─────────────┬─────────────┬─────┤
│   Size &    │  Structure  │   Demand    │  Supply &   │ Evo-│
│  Dynamics   │             │             │ Competition │lution│
│  (Gemini)   │  (Gemini)   │  (Claude)   │  (Gemini)   │(Clau│
│             │             │             │             │ de) │
└─────────────┴─────────────┴─────────────┴─────────────┴─────┘
```

### Category 1: Market Size & Dynamics
**Primary Model:** Gemini Pro 3 (breadth, citations, current data)

| Sub-Question | Focus |
|--------------|-------|
| What is the TAM/SAM/SOM? | Total, serviceable, obtainable market sizes |
| What are historical and projected growth rates? | CAGR, acceleration/deceleration patterns |
| What economic factors drive market size? | GDP correlation, cyclicality, elasticity |
| How is the market distributed geographically? | Regional breakdown, growth hotspots |

**Output Format:**
```xml
<market_size>
  <tam value="" currency="" year="" source="" confidence=""/>
  <sam value="" currency="" methodology=""/>
  <som value="" currency="" assumptions=""/>
  <growth_rate cagr="" period="" drivers=""/>
</market_size>
```

### Category 2: Market Structure
**Primary Model:** Gemini Pro 3 (comprehensive sourcing)

| Sub-Question | Focus |
|--------------|-------|
| How is the market segmented? | By product, customer, geography, channel |
| What does the value chain look like? | Participants, margins, power distribution |
| What are the key market segments and their sizes? | Segment definitions, relative sizes |
| How concentrated is the market? | HHI, top-N share, fragmentation |

**Output Format:**
```xml
<market_structure>
  <segmentation type="" segments=""/>
  <value_chain>
    <stage name="" players="" margin_range="" power=""/>
  </value_chain>
  <concentration hhi="" top_3_share="" trend=""/>
</market_structure>
```

### Category 3: Demand Characteristics
**Primary Model:** Claude Opus 4.5 (judgment, buyer psychology)

| Sub-Question | Focus |
|--------------|-------|
| Who are the primary buyers and decision-makers? | Personas, roles, influence patterns |
| What are the core use cases and jobs-to-be-done? | Functional, emotional, social jobs |
| What criteria do buyers use to evaluate options? | Must-haves, nice-to-haves, deal-breakers |
| How do buyers currently solve this problem? | Incumbent solutions, workarounds, gaps |

**Output Format:**
```xml
<demand>
  <buyer_persona role="" influence="" pain_points=""/>
  <use_cases>
    <use_case name="" frequency="" value="" alternatives=""/>
  </use_cases>
  <evaluation_criteria priority="" weight=""/>
</demand>
```

### Category 4: Supply & Competition
**Primary Model:** Gemini Pro 3 (comprehensive player mapping)

| Sub-Question | Focus |
|--------------|-------|
| Who are the major players and their market shares? | Leaders, challengers, niche players |
| What are barriers to entry? | Capital, technology, regulation, network effects |
| What substitutes and alternatives exist? | Direct, indirect, non-consumption |
| How intense is competitive rivalry? | Price competition, differentiation, switching costs |

**Output Format:**
```xml
<supply_competition>
  <player name="" share="" positioning="" strengths="" weaknesses=""/>
  <barriers type="" height="" trend=""/>
  <substitutes threat_level="" from=""/>
  <rivalry intensity="" basis=""/>
</supply_competition>
```

### Category 5: Market Evolution
**Primary Model:** Claude Opus 4.5 (synthesis, trend analysis)

| Sub-Question | Focus |
|--------------|-------|
| What macro trends are reshaping the market? | Technology, demographic, social, economic |
| What regulatory changes are emerging or expected? | Current, proposed, likely future |
| What disruptive forces could transform the market? | New entrants, technologies, business models |
| What is the likely market state in 3-5 years? | Consolidation, fragmentation, transformation |

**Output Format:**
```xml
<market_evolution>
  <trend name="" impact="" timeline="" probability=""/>
  <regulation status="" impact="" timeline=""/>
  <disruption source="" probability="" impact_if_occurs=""/>
  <future_state scenario="" probability="" implications=""/>
</market_evolution>
```

---

## 3. Pattern 2: Competitive Intelligence

### Purpose
Analyze specific competitors or competitive landscape for positioning, strategy, or M&A decisions.

### Category Structure

```
┌─────────────────────────────────────────────────────────────┐
│                COMPETITIVE INTELLIGENCE                     │
├─────────────┬─────────────┬─────────────┬─────────────┬─────┤
│  Product &  │ Customers & │ Go-to-Market│Organization │Strat│
│  Offering   │ Positioning │             │& Operations │ egy │
│   (GPT)     │  (Claude)   │  (Gemini)   │  (Gemini)   │(Clau│
│             │             │             │             │ de) │
└─────────────┴─────────────┴─────────────┴─────────────┴─────┘
```

### Category 1: Product & Offering
**Primary Model:** GPT-5.2 Deep (technical detail, exhaustiveness)

| Sub-Question | Focus |
|--------------|-------|
| What products/services do they offer? | SKUs, tiers, bundles, pricing |
| What are key features and capabilities? | Differentiated, parity, gaps |
| What is their technology stack and architecture? | Build vs. buy, patents, technical debt |
| What is their product roadmap (known or inferred)? | Announced, rumored, logical next steps |

### Category 2: Customers & Positioning
**Primary Model:** Claude Opus 4.5 (positioning analysis, win/loss)

| Sub-Question | Focus |
|--------------|-------|
| Who are their target customer segments? | ICP, verticals, company size |
| What is their value proposition and messaging? | Claims, proof points, tone |
| Why do customers choose them (or not)? | Win themes, loss reasons, churn drivers |
| How do they position against competitors? | Direct comparisons, competitive claims |

### Category 3: Go-to-Market
**Primary Model:** Gemini Pro 3 (comprehensive mapping)

| Sub-Question | Focus |
|--------------|-------|
| What is their sales model and motion? | Enterprise, self-serve, hybrid |
| What marketing channels and tactics do they use? | Content, events, paid, partnerships |
| What is their pricing strategy? | Models, levels, discounting patterns |
| What partnerships and integrations do they have? | Strategic, technology, channel |

### Category 4: Organization & Operations
**Primary Model:** Gemini Pro 3 (factual lookup)

| Sub-Question | Focus |
|--------------|-------|
| What is their organizational structure? | Leadership, teams, reporting |
| What is their technology and operations stack? | Tools, vendors, infrastructure |
| What is their cost structure and unit economics? | Fixed/variable, margins, efficiency |
| What recent hires, departures, or reorgs are notable? | Signals about strategy, culture, health |

### Category 5: Strategy & Trajectory
**Primary Model:** Claude Opus 4.5 (synthesis, strategic judgment)

| Sub-Question | Focus |
|--------------|-------|
| What is their stated strategy and vision? | Mission, goals, strategic priorities |
| What investments and bets are they making? | R&D focus, M&A, geographic expansion |
| What are their strengths, weaknesses, opportunities, threats? | SWOT analysis |
| What is their likely strategic direction? | Scenarios, most probable path |

---

## 4. Pattern 3: Technology Evaluation

### Purpose
Assess technologies for build/buy/adopt decisions with comprehensive risk and fit analysis.

### Category Structure

```
┌─────────────────────────────────────────────────────────────┐
│                 TECHNOLOGY EVALUATION                       │
├─────────────┬─────────────┬─────────────┬─────────────┬─────┤
│ Capability &│ Maturity &  │    Fit &    │   Cost &    │Risk │
│ Performance │  Ecosystem  │ Integration │ Investment  │& Gov│
│   (GPT)     │  (Gemini)   │  (Claude)   │  (Gemini)   │(Clau│
│             │             │             │             │ de) │
└─────────────┴─────────────┴─────────────┴─────────────┴─────┘
```

### Category 1: Capability & Performance
**Primary Model:** GPT-5.2 Deep (technical depth, benchmarks)

| Sub-Question | Focus |
|--------------|-------|
| What are the core capabilities and features? | Functional coverage, technical specs |
| How does it perform against benchmarks? | Speed, accuracy, scalability, reliability |
| What are the known limitations and edge cases? | Documented gaps, failure modes |
| How does it compare to alternatives technically? | Feature matrix, performance comparison |

### Category 2: Maturity & Ecosystem
**Primary Model:** Gemini Pro 3 (comprehensive sourcing)

| Sub-Question | Focus |
|--------------|-------|
| How mature and stable is the technology? | Version history, breaking changes, roadmap |
| What is the community and ecosystem like? | Contributors, plugins, extensions, support |
| What companies are using it successfully? | Case studies, references, scale achieved |
| What tooling and developer experience exists? | Documentation, SDKs, debugging, monitoring |

### Category 3: Fit & Integration
**Primary Model:** Claude Opus 4.5 (use case alignment, judgment)

| Sub-Question | Focus |
|--------------|-------|
| How well does it fit our specific use cases? | Gap analysis against requirements |
| What integration effort is required? | APIs, data formats, authentication |
| What migration path exists from current state? | Steps, risks, timeline |
| What organizational changes would adoption require? | Skills, processes, culture |

### Category 4: Cost & Investment
**Primary Model:** Gemini Pro 3 (factual research)

| Sub-Question | Focus |
|--------------|-------|
| What is the total cost of ownership? | License, infrastructure, personnel, maintenance |
| What is the licensing model? | Open source, commercial, hybrid |
| What infrastructure requirements exist? | Compute, storage, network, dependencies |
| What hidden costs should we anticipate? | Training, support, customization, scaling |

### Category 5: Risk & Governance
**Primary Model:** Claude Opus 4.5 (risk judgment, nuance)

| Sub-Question | Focus |
|--------------|-------|
| What are the technical risks? | Lock-in, obsolescence, security vulnerabilities |
| What are the vendor risks? | Viability, acquisition, pricing changes |
| What compliance and regulatory considerations apply? | Data privacy, industry regulations, audits |
| What is the reversibility if we need to change? | Exit strategy, data portability, sunk costs |

---

## 5. Pattern 4: Strategic Research

### Purpose
Inform strategic decisions about direction, options, and resource allocation.

### Category Structure

```
┌─────────────────────────────────────────────────────────────┐
│                   STRATEGIC RESEARCH                        │
├─────────────┬─────────────┬─────────────┬─────────────┬─────┤
│   Current   │  External   │  Strategic  │ Stakeholder │Impl-│
│    State    │ Environment │   Options   │Considerations│emen│
│  (Claude)   │  (Gemini)   │  (Claude)   │  (Claude)   │tation│
│             │             │             │             │(GPT)│
└─────────────┴─────────────┴─────────────┴─────────────┴─────┘
```

### Category 1: Current State
**Primary Model:** Claude Opus 4.5 (honest assessment, nuance)

| Sub-Question | Focus |
|--------------|-------|
| What are our core strengths and capabilities? | Distinctive competencies, assets, advantages |
| What are our key weaknesses and gaps? | Limitations, technical debt, talent gaps |
| How do we currently perform vs. objectives? | Metrics, trends, benchmark comparisons |
| What resources and constraints do we have? | Budget, people, time, technology |

### Category 2: External Environment
**Primary Model:** Gemini Pro 3 (comprehensive environmental scan)

| Sub-Question | Focus |
|--------------|-------|
| What industry trends are most relevant? | Technology, business model, competitive dynamics |
| What macro forces are shaping the landscape? | PESTEL factors, megatrends |
| What are competitors doing and planning? | Moves, investments, strategic signals |
| What technological shifts could be disruptive? | Emerging tech, adoption curves, implications |

### Category 3: Strategic Options
**Primary Model:** Claude Opus 4.5 (option generation, trade-offs)

| Sub-Question | Focus |
|--------------|-------|
| What strategic directions are available? | Growth vectors, positioning choices, focus areas |
| What are the trade-offs between options? | Benefits, costs, risks, reversibility |
| What capabilities would each option require? | Build, buy, partner requirements |
| What would success look like for each option? | Metrics, milestones, outcomes |

### Category 4: Stakeholder Considerations
**Primary Model:** Claude Opus 4.5 (stakeholder analysis, politics)

| Sub-Question | Focus |
|--------------|-------|
| How would customers react to each option? | Retention, acquisition, satisfaction |
| How would competitors likely respond? | Retaliation, imitation, differentiation |
| What internal stakeholder concerns exist? | Executive, board, employee perspectives |
| What external stakeholder reactions matter? | Investors, partners, regulators, public |

### Category 5: Implementation Requirements
**Primary Model:** GPT-5.2 Deep (detailed planning, exhaustiveness)

| Sub-Question | Focus |
|--------------|-------|
| What capabilities must be built or acquired? | Technology, talent, process, infrastructure |
| What investments are required? | Capital, operating, one-time vs. ongoing |
| What is a realistic implementation timeline? | Phases, dependencies, milestones |
| What are the key implementation risks? | Execution challenges, dependencies, unknowns |

---

## 6. Multi-Hypothesis Extension

### When to Add Hypotheses

Add hypothesis framing when the research involves:
- Predictions or forecasts
- Competing theories or explanations
- Binary or multi-way decisions
- High risk of confirmation bias

### Process

1. **Frame as Testable Prediction**
   - Convert research question to specific, falsifiable claim

2. **Generate MECE Hypotheses**
   - Create 2-4 hypotheses covering all plausible outcomes
   - Ensure mutual exclusivity (only one can be true)
   - Ensure collective exhaustiveness (covers all possibilities)

3. **Assign Prior Probabilities**
   - Estimate likelihood of each hypothesis before research
   - Must sum to 100%

4. **Define Evidence Criteria**
   - What would support each hypothesis?
   - What would refute each hypothesis?

### Example: Market Entry Decision

```xml
<hypotheses question="Should we enter the SMB accounting market?">
  <hypothesis id="H1" position="strong_yes" prior="20%">
    <statement>Market opportunity exceeds $50M with clear path to 15% share</statement>
    <supporting_evidence>
      - TAM >$300M and growing >15% CAGR
      - No dominant incumbent (leader <30% share)
      - Our capabilities map to top 3 buyer criteria
    </supporting_evidence>
    <refuting_evidence>
      - TAM <$200M or declining
      - High concentration (top 3 >70%)
      - Major capability gaps vs. requirements
    </refuting_evidence>
  </hypothesis>

  <hypothesis id="H2" position="conditional_yes" prior="35%">
    <statement>Opportunity exists but requires specific conditions</statement>
    <supporting_evidence>
      - TAM $200-300M with moderate growth
      - Underserved segment or geography exists
      - Partnership could fill capability gaps
    </supporting_evidence>
  </hypothesis>

  <hypothesis id="H3" position="no" prior="45%">
    <statement>Market not attractive given our position</statement>
    <supporting_evidence>
      - TAM <$200M or declining
      - Strong incumbents with distribution lock
      - Capability requirements don't match our strengths
    </supporting_evidence>
  </hypothesis>
</hypotheses>
```

---

## 7. Model Assignment Strategy

### Assignment Principles

| Principle | Description |
|-----------|-------------|
| **Strength Matching** | Assign categories to models based on core strengths |
| **Load Balancing** | Distribute roughly evenly (2-3 categories per model) |
| **Critical Path** | Assign highest-stakes categories to best-suited model |
| **Verification** | Cross-model verification for high-confidence claims |

### Model Strengths Reference

| Model | Best For | Avoid For |
|-------|----------|-----------|
| **Claude Opus 4.5** | Strategic judgment, synthesis, nuance, conflict resolution | Raw data gathering, citation-heavy research |
| **Gemini Pro 3** | Breadth, citations, current data, factual lookup | Deep reasoning, novel synthesis |
| **GPT-5.2 Deep** | Technical depth, exhaustive detail, edge cases | High-level synthesis, broad scans |

### Default Assignments by Pattern

| Pattern | Claude | Gemini | GPT |
|---------|--------|--------|-----|
| Market Research | Demand, Evolution | Size, Structure, Supply | — |
| Competitive Intel | Positioning, Strategy | GTM, Organization | Product |
| Technology Eval | Fit, Risk | Maturity, Cost | Capability |
| Strategic Research | State, Options, Stakeholders | Environment | Implementation |

### Override Conditions

Override default assignments when:
- **Domain expertise matters:** Assign to model with strongest domain knowledge
- **Recency critical:** Prefer Gemini for time-sensitive data
- **Technical depth required:** Prefer GPT for deep technical analysis
- **Judgment calls:** Prefer Claude for decisions requiring nuance

---

## 8. Quality Checklist

### MECE Validation

| # | Check | Pass Criteria |
|---|-------|---------------|
| 1 | **Mutual Exclusivity** | No sub-question could fit in multiple categories |
| 2 | **Collective Exhaustiveness** | All aspects of research objective are covered |
| 3 | **Appropriate Granularity** | 3-5 categories (not too broad, not too narrow) |
| 4 | **Balanced Depth** | Categories require similar research effort |
| 5 | **Clear Boundaries** | Category scope is unambiguous |

### Sub-Question Quality

| # | Check | Pass Criteria |
|---|-------|---------------|
| 1 | **Researchable** | Can be answered with available sources |
| 2 | **Specific** | Not vague or overly broad |
| 3 | **Relevant** | Directly serves research objective |
| 4 | **Non-overlapping** | Doesn't duplicate other sub-questions |
| 5 | **Actionable** | Answer informs decision or action |

### Model Assignment Quality

| # | Check | Pass Criteria |
|---|-------|---------------|
| 1 | **Strength Match** | Category aligns with model's core strength |
| 2 | **Balanced Load** | No model has >3 or <1 categories |
| 3 | **Critical Coverage** | Highest-stakes categories assigned appropriately |
| 4 | **No Conflicts** | Same data not requested from multiple models |

---

## 9. Examples

### Example 1: Good Decomposition

**Research Objective:** Evaluate the market opportunity for AI-powered contract analysis tools

**Decomposition:**
```
1. Market Size & Dynamics (Gemini)
   - What is the current market size for contract analysis tools?
   - What is the growth rate and projected size in 5 years?
   - How does the AI-powered segment compare to traditional tools?

2. Buyer Landscape (Claude)
   - Who are the primary buyers (legal, procurement, sales)?
   - What pain points drive purchase decisions?
   - What evaluation criteria do buyers prioritize?

3. Competitive Landscape (Gemini)
   - Who are the major players and their positioning?
   - What differentiates AI-native vs. legacy vendors?
   - What partnerships and integrations are common?

4. Technology Trends (GPT)
   - What AI capabilities are table stakes vs. differentiators?
   - What technical challenges remain unsolved?
   - What emerging tech could disrupt the space?

5. Market Entry Requirements (Claude)
   - What capabilities are must-haves for credibility?
   - What go-to-market approaches work in this space?
   - What barriers to entry exist for new entrants?
```

**Why It Works:**
- Categories are mutually exclusive (no overlap between buyer, competitive, technology)
- Collectively exhaustive (covers size, demand, supply, technology, entry)
- Appropriate model assignments (Claude for judgment, Gemini for data, GPT for tech)
- Sub-questions are specific and researchable

### Example 2: Poor Decomposition (with fixes)

**Research Objective:** Understand competitor X

**Poor Decomposition:**
```
1. What do they do? ← Too vague
2. Are they a threat? ← Not researchable, subjective
3. What's their technology? ← Overlaps with products
4. Products and features ← Overlaps with technology
5. Everything else ← Catch-all, not MECE
```

**Fixed Decomposition:**
```
1. Product & Offering (GPT)
   - What products do they sell and at what price points?
   - What are their key differentiating features?
   - What is their product roadmap?

2. Customers & Positioning (Claude)
   - Who are their target customers?
   - How do they position against competitors?
   - What win/loss patterns exist?

3. Go-to-Market (Gemini)
   - What is their sales model?
   - What marketing channels do they use?
   - What partnerships do they have?

4. Organization & Financials (Gemini)
   - How big are they (revenue, employees)?
   - What is their organizational structure?
   - What recent changes are notable?

5. Strategy & Trajectory (Claude)
   - What is their stated strategy?
   - What investments are they making?
   - What is their likely direction?
```

---

## Quick Reference

### Pattern Selection

| If researching... | Use Pattern |
|-------------------|-------------|
| Market size, growth, segments | Market Research |
| Specific company or product | Competitive Intelligence |
| Build/buy/adopt decision | Technology Evaluation |
| Direction, options, planning | Strategic Research |

### Category Count Guidelines

| Scope | Categories | Sub-Questions/Category |
|-------|------------|------------------------|
| Quick research | 3 | 2-3 |
| Standard research | 5 | 3-4 |
| Comprehensive research | 5-7 | 4-5 |

### Model Assignment Defaults

| Category Type | Default Model |
|---------------|---------------|
| Quantitative, factual | Gemini |
| Qualitative, judgment | Claude |
| Technical, detailed | GPT |
