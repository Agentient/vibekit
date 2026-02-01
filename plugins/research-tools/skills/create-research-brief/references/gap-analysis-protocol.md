# Gap Analysis Protocol

A two-part protocol for detecting coverage gaps in research findings. Part 1 uses MECE (Mutually Exclusive, Collectively Exhaustive) frameworks to identify expected coverage. Part 2 probes for unknown unknowns that structured analysis might miss.

---

## Overview

### Purpose
Identify what's missing from research findings:
- **Known unknowns:** Expected information that wasn't found (MECE gaps)
- **Unknown unknowns:** Risks and factors not anticipated (probes)

### When to Apply
- Before finalizing research briefs
- When research feels "complete" (danger zone for blind spots)
- After consolidating multi-model research
- Before making recommendations based on findings

### Two-Part Structure

| Part | Focus | Method | Output |
|------|-------|--------|--------|
| **Part 1** | MECE Gap Detection | Compare findings to expected coverage matrix | List of missing expected elements |
| **Part 2** | Unknown Unknowns | 5 structured probes | List of unconsidered factors |

---

## Part 1: MECE Gap Detection

### Concept

MECE analysis ensures research covers all expected dimensions without overlap. For each research type, there's an "expected coverage matrix" of what comprehensive research should include. Gaps are where findings are absent or weak (Evidence Score ≤ 2).

### Expected Coverage Matrices

#### Matrix 1: Market Research

**Research Question Type:** "What is the market opportunity for X?"

| Dimension | Expected Coverage | Sub-Elements |
|-----------|-------------------|--------------|
| **Market Size** | Current and projected size | TAM, SAM, SOM; Growth rates; Historical trend |
| **Market Structure** | How the market is organized | Segmentation; Value chain; Distribution channels |
| **Demand Drivers** | Why customers buy | Use cases; Pain points; Buying criteria |
| **Supply Dynamics** | Who provides solutions | Competitive landscape; Barriers to entry; Substitutes |
| **Market Trends** | Where market is heading | Emerging segments; Technology shifts; Regulatory changes |

**Completeness Checklist:**
```
[ ] Market size: Current value with source (Score ≥ 3)
[ ] Market size: 3-5 year projection with methodology
[ ] Segmentation: At least 2 segmentation schemes identified
[ ] Customer needs: Primary use cases documented
[ ] Competitors: Top 5 competitors identified with market share
[ ] Trends: At least 3 directional trends identified
[ ] Barriers: Entry/exit barriers characterized
```

---

#### Matrix 2: Competitive Intelligence

**Research Question Type:** "How does Competitor X compare to us?"

| Dimension | Expected Coverage | Sub-Elements |
|-----------|-------------------|--------------|
| **Product** | What they offer | Features; Pricing; Positioning; Roadmap |
| **Customers** | Who they serve | Target segments; Win/loss patterns; Retention |
| **Go-to-Market** | How they sell | Channels; Sales motion; Marketing; Partnerships |
| **Operations** | How they deliver | Technology stack; Team structure; Cost structure |
| **Strategy** | Where they're heading | Stated priorities; Investment areas; M&A activity |

**Completeness Checklist:**
```
[ ] Product comparison: Feature-by-feature on key capabilities
[ ] Pricing: Model and approximate price points
[ ] Customer base: Size and key segments
[ ] Recent wins: Named accounts or patterns
[ ] Team size: Total headcount and key hires
[ ] Funding/financials: Revenue or funding stage
[ ] Strategic moves: Recent announcements or pivots
```

---

#### Matrix 3: Technology Evaluation

**Research Question Type:** "Should we adopt Technology X?"

| Dimension | Expected Coverage | Sub-Elements |
|-----------|-------------------|--------------|
| **Capability** | What it does | Core features; Limitations; Performance |
| **Maturity** | How ready it is | Stability; Community; Ecosystem |
| **Fit** | How it matches our needs | Use case alignment; Integration; Migration path |
| **Cost** | Total cost of ownership | Licensing; Infrastructure; Personnel |
| **Risk** | What could go wrong | Vendor risk; Technical risk; Adoption risk |

**Completeness Checklist:**
```
[ ] Core capabilities: Documented with benchmarks
[ ] Limitations: Known constraints identified
[ ] Community health: Contributors, releases, issues
[ ] Integration: Compatibility with our stack
[ ] Learning curve: Team skill gaps assessed
[ ] Licensing: Terms and cost structure clear
[ ] Vendor stability: Company health indicators
[ ] Alternative: At least 1 alternative evaluated
```

---

#### Matrix 4: User Research

**Research Question Type:** "What do users need from X?"

| Dimension | Expected Coverage | Sub-Elements |
|-----------|-------------------|--------------|
| **Users** | Who they are | Personas; Segments; Contexts |
| **Jobs** | What they're trying to do | Goals; Tasks; Workflows |
| **Pains** | What frustrates them | Obstacles; Workarounds; Complaints |
| **Gains** | What delights them | Desired outcomes; Upsides; Success metrics |
| **Journey** | How they interact | Touchpoints; Moments of truth; Drop-offs |

**Completeness Checklist:**
```
[ ] User segments: At least 2-3 distinct personas
[ ] Primary jobs: Top 3 jobs-to-be-done identified
[ ] Pain points: Ranked by severity/frequency
[ ] Current solutions: What they do today
[ ] Desired outcomes: Measurable success criteria
[ ] Journey map: Key stages and transitions
[ ] Behavioral data: Quantitative usage patterns
```

---

### Audit Process

#### Step 1: Map Findings to Matrix

For each finding in your research, map it to the appropriate dimension:

```markdown
| Finding | Matrix Dimension | Evidence Score | Notes |
|---------|------------------|----------------|-------|
| Market is $10B | Market Size | 4 | Gartner 2024 |
| Growing 15% YoY | Market Size | 4 | Same source |
| 3 main segments | Market Structure | 3 | Industry report |
| ... | ... | ... | ... |
```

#### Step 2: Identify Missing Dimensions

Check the matrix for dimensions with no findings or only weak evidence:

```markdown
## Gap Identification

| Dimension | Status | Gap Type |
|-----------|--------|----------|
| Market Size | ✓ Covered (Score 4) | — |
| Market Structure | ✓ Covered (Score 3) | — |
| Demand Drivers | ⚠️ Weak (Score 2) | Evidence gap |
| Supply Dynamics | ✓ Covered (Score 4) | — |
| Market Trends | ❌ Missing | Coverage gap |
```

#### Step 3: Classify Gap Severity

| Severity | Criteria | Action |
|----------|----------|--------|
| **Critical** | Core to research question; no coverage or Score 1 | Must address before finalizing |
| **Significant** | Important dimension; Score 2 or single weak source | Should attempt to fill |
| **Minor** | Supporting detail; provides context but not central | Note for future research |

**Severity Decision Tree:**
```
Is this dimension core to answering the research question?
├─ YES → Missing or Score ≤ 2 = CRITICAL
│        Score 3 = SIGNIFICANT
│        Score ≥ 4 = No gap
└─ NO → Missing or Score ≤ 2 = SIGNIFICANT
        Score 3 = MINOR
        Score ≥ 4 = No gap
```

---

### Gap Detection Output Format

```markdown
## MECE Gap Analysis

**Research Type:** [Market/Competitive/Technology/User]
**Question:** [Research question]

### Coverage Summary

| Dimension | Status | Best Evidence | Score | Gap Severity |
|-----------|--------|---------------|-------|--------------|
| [Dim 1] | ✓ Covered | [Source] | 4 | — |
| [Dim 2] | ⚠️ Weak | [Source] | 2 | Significant |
| [Dim 3] | ❌ Missing | — | — | Critical |
| [Dim 4] | ✓ Covered | [Source] | 5 | — |
| [Dim 5] | ✓ Covered | [Source] | 3 | — |

### Critical Gaps
1. **[Dimension]:** [What's missing and why it matters]
   - Suggested source: [Where to look]
   - Fallback: [Alternative approach if primary fails]

### Significant Gaps
1. **[Dimension]:** [What's weak]
   - Current evidence: [What we have]
   - Needed: [What would strengthen]

### Coverage Score
**[X/Y] dimensions covered at Score ≥ 3**
**Overall: [Complete | Mostly Complete | Significant Gaps | Incomplete]**
```

---

## Part 2: Unknown Unknowns Probe

### Concept

MECE analysis catches known unknowns—things we expected to find. But research can miss entire categories of relevant information. The 5 probes below systematically surface factors outside our initial frame.

### The 5 Probes

---

#### Probe 1: Adjacent Domain Analysis

**Purpose:** Identify relevant factors from neighboring domains that might impact findings.

**Questions:**
- What adjacent industries face similar dynamics?
- What analogous situations have played out in other markets?
- What would experts from related fields notice that we missed?
- Are there upstream or downstream dependencies we haven't considered?

**Technique:**
1. List 3-5 adjacent domains
2. For each: "What lessons from [domain] apply here?"
3. Check if any identified factors are absent from findings

**Example:**
```
Research: AI-powered legal research tools
Adjacent domains:
- AI in medical diagnosis → Liability concerns, credentialing
- Legal tech generally → Bar association resistance, slow adoption
- Enterprise search → Integration complexity, change management
- Academic research tools → Citation integrity, source verification

Surfaced factors not in original research:
- Bar association regulatory stance (not covered)
- Malpractice insurance implications (not covered)
- Integration with existing case management systems (weak coverage)
```

**Output:**
```markdown
### Adjacent Domain Analysis

| Domain | Relevant Factor | Currently Covered? | Importance |
|--------|-----------------|-------------------|------------|
| [Domain 1] | [Factor] | Yes/Weak/No | High/Med/Low |
| [Domain 2] | [Factor] | Yes/Weak/No | High/Med/Low |
```

---

#### Probe 2: Stakeholder Blind Spot Check

**Purpose:** Identify stakeholders whose perspectives might be missing or underweighted.

**Questions:**
- Whose voice is absent from our sources?
- Who loses if our conclusions are correct?
- Who has incentive to hide information?
- What stakeholders operate "behind the scenes"?
- Whose expertise would challenge our framing?

**Technique:**
1. Map all stakeholders (direct, indirect, hidden)
2. For each: Check if their perspective appears in findings
3. Especially scrutinize those with misaligned incentives

**Stakeholder Categories:**
| Category | Examples | Typical Blind Spots |
|----------|----------|---------------------|
| Direct | Customers, competitors | Well covered |
| Indirect | Regulators, partners, suppliers | Often missed |
| Hidden | Lobbyists, influencers, advisors | Usually missed |
| Opposing | Critics, skeptics, losers | Systematically avoided |

**Example:**
```
Research: Market for electric vehicle charging
Stakeholders:
✓ EV manufacturers (covered)
✓ Charging network operators (covered)
✓ Consumers (covered)
⚠️ Utilities (weak—grid capacity not addressed)
❌ Local governments (permitting not addressed)
❌ Property owners (installation barriers not addressed)
❌ Oil/gas industry (lobbying response not addressed)
```

**Output:**
```markdown
### Stakeholder Blind Spot Analysis

| Stakeholder | Representation | Perspective Gap |
|-------------|---------------|-----------------|
| [Stakeholder 1] | ✓ Well represented | — |
| [Stakeholder 2] | ⚠️ Underweighted | [Missing view] |
| [Stakeholder 3] | ❌ Missing | [Unheard perspective] |
```

---

#### Probe 3: Time Horizon Scan

**Purpose:** Check if relevant past context or future implications are missing.

**Questions:**
- What historical precedents inform this situation?
- What happened last time something similar occurred?
- What are the 2nd and 3rd order effects over time?
- What would this look like in 1 year? 5 years? 10 years?
- What assumptions might not hold over time?

**Time Dimensions:**
| Horizon | Questions |
|---------|-----------|
| **Past** | Historical analogies, previous attempts, lessons learned |
| **Near-term** (1-2 years) | Implementation challenges, adoption curves |
| **Medium-term** (3-5 years) | Market maturation, competitive response |
| **Long-term** (5+ years) | Paradigm shifts, obsolescence risk |

**Example:**
```
Research: Adoption of generative AI in enterprises

Time gaps identified:
- Past: Not examining previous AI hype cycles (2016-2018 chatbot wave)
- Near-term: Covered (implementation challenges)
- Medium-term: Weak on competitive commoditization
- Long-term: Missing discussion of AGI implications, job displacement policy
```

**Output:**
```markdown
### Time Horizon Analysis

| Horizon | Coverage | Gap |
|---------|----------|-----|
| Historical context | [Status] | [What's missing] |
| Near-term (1-2y) | [Status] | [What's missing] |
| Medium-term (3-5y) | [Status] | [What's missing] |
| Long-term (5y+) | [Status] | [What's missing] |
```

---

#### Probe 4: Failure Mode Exploration

**Purpose:** Identify ways conclusions could be wrong or plans could fail.

**Questions:**
- What would have to be true for our conclusions to be wrong?
- What's the strongest counter-argument?
- What could cause the predicted outcome NOT to happen?
- What single point of failure exists?
- What black swan events could invalidate findings?

**Failure Categories:**
| Category | Description | Example |
|----------|-------------|---------|
| **Assumption failure** | Core assumption proves false | "Customers want this" proves untrue |
| **Execution failure** | Plan fails in implementation | Technology doesn't work at scale |
| **External shock** | Environment changes unexpectedly | Regulation bans approach |
| **Competitive response** | Rivals act in unexpected ways | Incumbent undercuts price to zero |
| **Timing failure** | Right idea, wrong time | Market not ready |

**Pre-Mortem Technique:**
1. Assume the conclusion/recommendation failed spectacularly
2. Work backward: "Why did it fail?"
3. Check if those failure modes appear in risk analysis

**Example:**
```
Research: Recommending entry into autonomous delivery market

Failure modes not addressed:
- Regulatory: City bans sidewalk robots (SF example not cited)
- Technical: Edge cases require human intervention 30% of time
- Economic: Unit economics don't work below $10/delivery
- Competitive: Amazon launches free delivery with Prime
- Social: Public backlash against job displacement
```

**Output:**
```markdown
### Failure Mode Analysis

| Failure Mode | Type | Currently Addressed? | Impact if Missed |
|--------------|------|---------------------|------------------|
| [Mode 1] | [Category] | Yes/No | High/Med/Low |
| [Mode 2] | [Category] | Yes/No | High/Med/Low |

**Pre-Mortem Scenario:**
"The recommendation failed because..." [Narrative of failure]
```

---

#### Probe 5: Second-Order Effects

**Purpose:** Trace downstream consequences that initial analysis might miss.

**Questions:**
- If our finding is true, what else must be true?
- What does this imply for adjacent stakeholders?
- What feedback loops or unintended consequences might emerge?
- How might actors respond to the situation we describe?
- What equilibrium does this disrupt?

**Second-Order Framework:**
```
First-order: [Direct finding]
    └── Second-order: [Implication of finding]
         └── Third-order: [Implication of implication]
```

**Example:**
```
Finding: Remote work will remain at 40% for knowledge workers

Second-order effects not analyzed:
1. Commercial real estate → Office vacancy increases →
   Urban tax base declines → City services affected
2. Talent markets → Location-agnostic hiring →
   Salary arbitrage → Wage pressure in high-cost areas
3. Management practices → Surveillance tools increase →
   Privacy concerns → Regulatory response
4. Social dynamics → Fewer in-person mentorship →
   Junior employee development challenges →
   Skills gap emerges
```

**Output:**
```markdown
### Second-Order Effects Analysis

| Finding | Second-Order Effect | Third-Order Effect | Addressed? |
|---------|---------------------|-------------------|------------|
| [Finding] | [Effect] | [Effect] | Yes/No |

**Causal Chain:**
[Finding] → [2nd order] → [3rd order] → [Implication for research]
```

---

## Integrated Gap Report Format

Combine MECE analysis and Unknown Unknowns probes into a single gap report:

```markdown
# Gap Analysis Report

**Research:** [Research question/brief title]
**Date:** [Analysis date]
**Analyst:** [Who performed analysis]

---

## Part 1: MECE Coverage Assessment

### Coverage Matrix: [Research Type]

| Dimension | Coverage | Evidence Score | Gap Severity |
|-----------|----------|----------------|--------------|
| [Dim 1] | ✓ | 4 | — |
| [Dim 2] | ⚠️ | 2 | Significant |
| [Dim 3] | ❌ | — | Critical |
| [Dim 4] | ✓ | 5 | — |
| [Dim 5] | ✓ | 3 | — |

**Coverage Score:** 3/5 dimensions at Score ≥ 3
**Status:** Significant Gaps

### Critical MECE Gaps

1. **[Dimension]:** [Description]
   - Impact: [Why this matters]
   - Action: [How to fill gap]

### Significant MECE Gaps

1. **[Dimension]:** [Description]
   - Current evidence: [What exists]
   - Needed: [What's missing]

---

## Part 2: Unknown Unknowns Assessment

### Probe Results Summary

| Probe | Findings | Priority Items |
|-------|----------|----------------|
| Adjacent Domains | [Count] factors surfaced | [Top 1-2] |
| Stakeholder Blind Spots | [Count] missing perspectives | [Top 1-2] |
| Time Horizons | [Count] temporal gaps | [Top 1-2] |
| Failure Modes | [Count] unaddressed risks | [Top 1-2] |
| Second-Order Effects | [Count] downstream impacts | [Top 1-2] |

### Priority Unknown Unknowns

1. **[Factor]** (from [Probe])
   - Why missed: [Explanation]
   - Impact: [High/Medium/Low]
   - Action: [Research or acknowledge]

2. **[Factor]** (from [Probe])
   - Why missed: [Explanation]
   - Impact: [High/Medium/Low]
   - Action: [Research or acknowledge]

3. **[Factor]** (from [Probe])
   - Why missed: [Explanation]
   - Impact: [High/Medium/Low]
   - Action: [Research or acknowledge]

---

## Integrated Gap Summary

### By Uncertainty Type

| Gap | Type | Severity | Action |
|-----|------|----------|--------|
| [Gap 1] | Epistemic | Critical | Research: [approach] |
| [Gap 2] | Epistemic | Significant | Research: [approach] |
| [Gap 3] | Aleatory | N/A | Acknowledge in findings |
| [Gap 4] | Model | N/A | Make explicit in output |

### Research Recommendations

**Must address before finalizing:**
1. [Gap] — [Specific research action]

**Should address if time permits:**
1. [Gap] — [Specific research action]

**Acknowledge in limitations:**
1. [Gap] — [How to caveat]

---

## Sign-Off

- [ ] MECE audit complete
- [ ] All 5 probes executed
- [ ] Critical gaps have action plans
- [ ] Limitations documented
- [ ] Ready for consolidation
```

---

## Full Worked Example

### Research Context
**Question:** Should we enter the AI-powered customer service market?

### Part 1: MECE Analysis (Market Research Matrix)

| Dimension | Coverage | Score | Gap |
|-----------|----------|-------|-----|
| Market Size | ✓ Covered | 4 | — |
| Market Structure | ✓ Covered | 3 | — |
| Demand Drivers | ⚠️ Weak | 2 | Significant—only enterprise view |
| Supply Dynamics | ✓ Covered | 4 | — |
| Market Trends | ⚠️ Weak | 2 | Significant—tech trends only |

**Critical Gaps:** None
**Significant Gaps:**
- Demand drivers for SMB segment
- Non-technology trends (workforce, regulatory)

### Part 2: Unknown Unknowns Probes

**Probe 1 (Adjacent Domains):**
- Healthcare AI chatbots → Liability concerns when AI gives wrong info
- Gap: No coverage of liability/accuracy requirements

**Probe 2 (Stakeholders):**
- Missing: Customer service agents (job displacement view)
- Missing: Customer advocates (consumer protection perspective)

**Probe 3 (Time Horizons):**
- Missing historical context: Previous chatbot failures (2016-2018)
- Weak long-term: No AGI/superintelligence scenario

**Probe 4 (Failure Modes):**
- Not addressed: AI confidently gives wrong answers → brand damage
- Not addressed: Regulatory ban on AI in certain contexts

**Probe 5 (Second-Order):**
- Finding: "AI reduces support costs 40%"
- 2nd order: Mass layoffs in CS industry
- 3rd order: Political backlash, potential regulation
- Status: Not addressed

### Integrated Summary

**Must address:**
1. Liability/accuracy requirements (Epistemic—researchable)
2. Regulatory landscape, especially consumer protection (Epistemic)

**Should address:**
3. SMB demand drivers (Epistemic)
4. Historical chatbot failures as cautionary context (Epistemic)

**Acknowledge in limitations:**
5. Long-term AGI implications (Aleatory—can't predict)
6. Political/regulatory response to job displacement (Aleatory)

---

## Quick Reference

### MECE Audit Checklist

```
[ ] Select appropriate coverage matrix
[ ] Map every finding to a dimension
[ ] Identify dimensions with no/weak coverage
[ ] Classify gap severity (Critical/Significant/Minor)
[ ] Document action plans for critical gaps
```

### Unknown Unknowns Probe Checklist

```
[ ] Probe 1: List 3+ adjacent domains, extract applicable factors
[ ] Probe 2: Map all stakeholders, identify missing voices
[ ] Probe 3: Check past/near/medium/long time horizons
[ ] Probe 4: Pre-mortem—identify failure modes
[ ] Probe 5: Trace 2nd and 3rd order effects
[ ] Prioritize top 3 unknown unknowns for action
```

### Gap Severity Quick Guide

| | Core to question | Supporting detail |
|-|------------------|-------------------|
| **Missing** | Critical | Significant |
| **Score 1-2** | Critical | Significant |
| **Score 3** | Significant | Minor |
| **Score 4-5** | No gap | No gap |
