# Uncertainty Taxonomy

A framework for classifying uncertainties in research findings into three distinct types. Understanding uncertainty type determines whether additional research can help and what actions are appropriate.

---

## Overview

### Purpose
Classify uncertainties to:
- Determine if more research can reduce the uncertainty
- Guide appropriate response strategies
- Set realistic expectations for stakeholders
- Identify which LLM/research approach best addresses each uncertainty

### The Core Insight
Not all uncertainty is the same. Some gaps can be closed with more research (epistemic), some cannot be reduced no matter how much we investigate (aleatory), and some depend on the frameworks we choose to use (model). Conflating these types leads to wasted research effort or false confidence.

### The Three Types at a Glance

| Type | Can Be Reduced? | Action | Example |
|------|-----------------|--------|---------|
| **Epistemic** | YES — with more research | Investigate further | "We don't know their market share" |
| **Aleatory** | NO — inherent randomness | Quantify and accept | "Future stock price movements" |
| **Model** | DEPENDS — on framework choice | Acknowledge assumptions | "Growth depends on TAM definition" |

---

## The Three Types

### Epistemic Uncertainty (Knowledge Gaps)

**Definition:** Uncertainty arising from incomplete information that COULD be reduced through additional research, measurement, or investigation.

**Key Characteristic:** The truth exists and is knowable in principle; we simply haven't found it yet.

**Indicators:**
- "We couldn't find data on..."
- "The source didn't specify..."
- "No public information available about..."
- "Conflicting reports require verification..."

#### Categories of Epistemic Uncertainty

| Category | Description | Research Approach |
|----------|-------------|-------------------|
| **Data Gap** | Information exists but wasn't found | Expand search, use different sources |
| **Access Gap** | Information exists but is restricted | Seek alternative proxies, expert interviews |
| **Measurement Gap** | Phenomenon exists but hasn't been measured | Commission primary research |
| **Verification Gap** | Claims exist but need validation | Cross-reference, triangulate sources |

#### Examples by Domain

**Market Research:**
```
Epistemic: "We don't know Company X's current headcount"
Why: This is a fact that exists (HR knows it)
Action: Check LinkedIn, job postings, press releases, or ask directly
Resolution: Finding the answer reduces uncertainty to zero
```

**Competitive Intelligence:**
```
Epistemic: "Competitor's product roadmap is unclear"
Why: The roadmap exists internally
Action: Monitor job postings, patent filings, conference talks, customer feedback
Resolution: Partial resolution through inference; full resolution if leaked/announced
```

**Technology Evaluation:**
```
Epistemic: "Performance benchmarks for this configuration don't exist"
Why: The performance is measurable
Action: Run benchmarks or find comparable configurations
Resolution: Measurement eliminates uncertainty
```

**User Research:**
```
Epistemic: "We don't know why users abandon at checkout"
Why: Users have reasons (even if unconscious)
Action: User interviews, session recordings, surveys
Resolution: Research reveals the actual reasons
```

#### LLM Strategy for Epistemic Uncertainty
- **Gemini Pro 3:** Best for breadth search across many sources
- **GPT-5.2 Deep:** Best for exhaustive investigation of specific questions
- **Claude Opus 4.5:** Best for synthesizing partial information into likely scenarios

---

### Aleatory Uncertainty (Inherent Randomness)

**Definition:** Uncertainty arising from genuine randomness or variability that CANNOT be reduced through additional research. The outcome is inherently unpredictable.

**Key Characteristic:** Even with perfect information, the outcome would remain uncertain because it hasn't happened yet or is fundamentally stochastic.

**Indicators:**
- Future states of complex systems
- Human behavior at individual level
- Market movements
- Natural phenomena with random components
- Outcomes dependent on free will or emergent behavior

#### Categories of Aleatory Uncertainty

| Category | Description | Approach |
|----------|-------------|----------|
| **Future State** | Outcome hasn't occurred yet | Scenario planning |
| **Stochastic Process** | Genuine randomness in mechanism | Probabilistic modeling |
| **Complex System** | Too many variables to predict | Identify key sensitivities |
| **Behavioral** | Individual human choices | Probability distributions |

#### Examples by Domain

**Market Research:**
```
Aleatory: "Will customers prefer Product A or B?"
Why: Customer decisions haven't been made yet
Action: Survey for preferences, but actual choices may differ
Cannot: Predict with certainty what people will actually do
Response: Report preference distributions, not point estimates
```

**Competitive Intelligence:**
```
Aleatory: "Will the competitor enter our market segment?"
Why: Their decision depends on factors they haven't resolved
Action: Assess capability and strategic logic
Cannot: Know their internal deliberations
Response: Probability-weighted scenarios
```

**Technology Evaluation:**
```
Aleatory: "Will this technology become the industry standard?"
Why: Depends on adoption patterns, network effects, competitor responses
Action: Identify adoption drivers and barriers
Cannot: Predict winner in standards battles with certainty
Response: Scenario analysis with trigger conditions
```

**Financial/Investment:**
```
Aleatory: "What will the stock price be in 12 months?"
Why: Prices are influenced by unpredictable events
Action: Model based on fundamentals
Cannot: Predict with precision
Response: Range estimates with confidence intervals
```

#### LLM Strategy for Aleatory Uncertainty
- **Claude Opus 4.5:** Best for scenario generation and narrative exploration
- **Gemini Pro 3:** Good for gathering inputs for probabilistic models
- **GPT-5.2 Deep:** Useful for deep analysis of analogous historical situations

#### Key Principle
**Do not treat aleatory uncertainty as a research failure.** The appropriate response is to:
1. Acknowledge the irreducible uncertainty
2. Quantify the range of possibilities
3. Identify early warning indicators
4. Build optionality into recommendations

---

### Model Uncertainty (Framework Dependencies)

**Definition:** Uncertainty arising from the choice of analytical framework, definitions, or assumptions. Different valid models yield different conclusions.

**Key Characteristic:** The "answer" depends on which lens you use to view the question. Multiple defensible approaches exist.

**Indicators:**
- Results change significantly with different definitions
- Analysts using same data reach different conclusions
- Answer depends on scope/boundary choices
- Multiple valid methodologies exist

#### Categories of Model Uncertainty

| Category | Description | Approach |
|----------|-------------|----------|
| **Definitional** | Outcome depends on how terms are defined | Explicitly state definition used |
| **Scope** | Outcome depends on boundaries drawn | Test sensitivity to scope changes |
| **Methodological** | Valid methods give different results | Report range across methods |
| **Assumption** | Results depend on input assumptions | Sensitivity analysis |

#### Examples by Domain

**Market Research:**
```
Model: "What is the Total Addressable Market?"
Why: TAM depends on how you define the market boundaries
  - Narrow definition: $5B (current product category)
  - Medium definition: $15B (adjacent use cases)
  - Broad definition: $50B (all potential applications)
Action: Report all three with explicit boundary definitions
Output: "TAM ranges from $5B to $50B depending on market definition"
```

**Competitive Intelligence:**
```
Model: "Who are our competitors?"
Why: Depends on how you define competition
  - Direct competitors: Same product, same market
  - Indirect competitors: Different product, same job-to-be-done
  - Potential competitors: Adjacent players who could enter
Action: Segment analysis by competition type
Output: "5 direct, 12 indirect, 8 potential competitors identified"
```

**Technology Evaluation:**
```
Model: "Is this technology 'mature'?"
Why: Maturity depends on the framework used
  - Gartner Hype Cycle: Slope of Enlightenment
  - Technology S-Curve: Early majority
  - Adoption metrics: 15% penetration
Action: Report position on multiple frameworks
Output: "Mature by adoption metrics, still emerging by Gartner assessment"
```

**Financial Analysis:**
```
Model: "What is the company worth?"
Why: Valuation depends on methodology
  - DCF: $2.1B (based on growth assumptions)
  - Comparable companies: $1.7B
  - Precedent transactions: $2.4B
Action: Report range with methodology sensitivity
Output: "Valuation range $1.7B-$2.4B depending on methodology"
```

#### LLM Strategy for Model Uncertainty
- **Claude Opus 4.5:** Best for multi-perspective synthesis
- **GPT-5.2 Deep:** Good for exhaustive treatment of single methodology
- **Gemini Pro 3:** Useful for finding alternative frameworks

#### Key Principle
**Make model choices explicit.** Research consumers should know:
1. What framework/definition was used
2. What alternatives exist
3. How sensitive conclusions are to these choices
4. Who uses which frameworks and why

---

## Classification Protocol

### Step-by-Step Decision Process

```
STEP 1: Identify the uncertainty
"What specifically don't we know?"

STEP 2: Ask the closure question
"Could more research definitively answer this?"
├─ YES, definitively → Likely EPISTEMIC
├─ NO, inherently unknowable → Likely ALEATORY
└─ DEPENDS on how we frame it → Likely MODEL

STEP 3: Test with counterfactuals
"If we had unlimited resources and access, could we know?"
├─ YES → EPISTEMIC (it's a solvable knowledge gap)
├─ NO (because it hasn't happened) → ALEATORY
└─ NO (because the answer depends on our choices) → MODEL

STEP 4: Verify classification
Check indicators and examples above
```

### Decision Tree

```
                    What is the nature of the uncertainty?
                                    │
            ┌───────────────────────┼───────────────────────┐
            │                       │                       │
     Missing information     Future/random event    Framework-dependent
            │                       │                       │
    Could we find it with    Is the randomness      Would different
    more research effort?    fundamental or         valid approaches
            │                just complexity?       give different
            │                       │               answers?
        ┌───┴───┐              ┌───┴───┐               │
       YES      NO         Fundamental  Complex        │
        │        │             │          │            │
    EPISTEMIC   │          ALEATORY    (mixed)      MODEL
                │                         │
        Check if it's                 May be
        actually MODEL              partially
        uncertainty                 EPISTEMIC
```

### Mixed Uncertainty

Many real situations combine uncertainty types:

**Example: "Will our new product succeed?"**
- **Epistemic component:** What do customers currently need? (researchable)
- **Aleatory component:** How will competitors react? (unpredictable)
- **Model component:** How do we define "success"? (definitional)

**Handling Mixed Uncertainty:**
1. Decompose into components
2. Classify each component
3. Address epistemic components with research
4. Quantify aleatory components with scenarios
5. Make model choices explicit

---

## Diagnostic Questions

Use these questions to classify uncertainty:

### Epistemic Indicators (Knowledge Gaps)

| Question | If YES → Epistemic |
|----------|-------------------|
| Does someone, somewhere know this answer? | ✓ |
| Could we measure or observe this directly? | ✓ |
| Is this information recorded somewhere? | ✓ |
| Would better access/resources resolve this? | ✓ |
| Has this been true in the past in a measurable way? | ✓ |

### Aleatory Indicators (Inherent Randomness)

| Question | If YES → Aleatory |
|----------|------------------|
| Does this depend on events that haven't happened? | ✓ |
| Would knowing everything today still leave uncertainty? | ✓ |
| Is there genuine randomness in the mechanism? | ✓ |
| Do similar past situations have variable outcomes? | ✓ |
| Is this sensitive to initial conditions? | ✓ |

### Model Indicators (Framework Dependencies)

| Question | If YES → Model |
|----------|---------------|
| Would the answer change with different definitions? | ✓ |
| Do experts disagree despite having the same data? | ✓ |
| Are there multiple valid methodologies? | ✓ |
| Does the answer depend on scope/boundary choices? | ✓ |
| Is there ongoing debate about the right framework? | ✓ |

---

## Action Implications

### What to Do for Each Type

| Uncertainty Type | Primary Action | Secondary Action | Do NOT |
|------------------|----------------|------------------|--------|
| **Epistemic** | Invest in research | Prioritize by importance | Accept as permanent |
| **Aleatory** | Quantify range | Build scenarios | Claim false precision |
| **Model** | Make choices explicit | Test sensitivity | Hide assumptions |

### Research Effort Allocation

```
                    HIGH research value
                           │
           ┌───────────────┼───────────────┐
           │               │               │
      EPISTEMIC        Partially       Mixed with
      (pure gap)       resolvable      MODEL choices
           │               │               │
     Maximum ROI      Good ROI        Moderate ROI
     on research      (clarify what   (research +
                      can be known)    acknowledge)
           │               │               │
           └───────────────┼───────────────┘
                           │
                    LOW research value
                           │
           ┌───────────────┼───────────────┐
           │               │               │
       ALEATORY         MODEL          Aleatory +
       (pure random)    (pure choice)   Model mix
           │               │               │
     No ROI on more    No "research"   Acknowledge
     research (already  needed—just     limits, then
     have all info)     make decisions  decide anyway
```

### Stakeholder Communication

| Type | How to Communicate |
|------|-------------------|
| **Epistemic** | "We can find out; recommend additional research on X" |
| **Aleatory** | "This is inherently uncertain; here are the scenarios" |
| **Model** | "The answer is X under our assumptions; other valid views exist" |

---

## Output Format

### Single Finding Classification

```markdown
**Finding:** [Statement]
**Uncertainty Type:** EPISTEMIC | ALEATORY | MODEL
**Confidence:** [Based on evidence strength rubric]
**Classification Rationale:** [1-2 sentences why this type]
**Recommended Action:** [What to do about it]
```

### Research Section Format

```markdown
## [Research Question]

### Findings
[List of findings with evidence scores]

### Uncertainty Analysis

| Finding | Type | Rationale | Action |
|---------|------|-----------|--------|
| [F1] | Epistemic | Data exists but not found | Search [specific sources] |
| [F2] | Aleatory | Future competitor behavior | Scenario analysis |
| [F3] | Model | Depends on market definition | Use [chosen definition] |

### Implications
- **Can resolve:** [List epistemic items worth researching]
- **Must accept:** [List aleatory items with recommended ranges]
- **Depends on choices:** [List model items with chosen framework]
```

### Full Research Brief Uncertainty Summary

```markdown
## Uncertainty Profile

### Classification Summary
| Type | Count | % of Findings | Key Items |
|------|-------|---------------|-----------|
| Epistemic | 5 | 35% | Market share data, pricing info |
| Aleatory | 4 | 28% | Adoption rates, competitor response |
| Model | 5 | 35% | TAM definition, maturity assessment |

### Research Recommendations
**High-value epistemic gaps to close:**
1. [Gap 1] — [Suggested approach]
2. [Gap 2] — [Suggested approach]

**Aleatory factors to monitor:**
1. [Factor 1] — [Early warning indicator]
2. [Factor 2] — [Early warning indicator]

**Model choices made:**
1. [Choice 1] — [Rationale]
2. [Choice 2] — [Alternative considered]
```

---

## Examples by Research Domain

### Market Research Example

**Research Question:** What is the market opportunity for AI-powered legal research tools?

| Finding | Type | Rationale | Action |
|---------|------|-----------|--------|
| Current market size unclear | Epistemic | Different analysts report differently; truth exists | Triangulate major reports |
| Future AI capability improvements | Aleatory | Technology advancement is unpredictable | Scenario planning |
| Definition of "AI-powered" varies | Model | Some include keyword search, others only ML | State explicit definition |
| Lawyer adoption rates by 2027 | Aleatory | Human behavior not predictable | Survey + historical analogies |
| Competitor pipeline products | Epistemic | Products exist but aren't public | Monitor job postings, patents |

### Competitive Intelligence Example

**Research Question:** How will Competitor X respond to our product launch?

| Finding | Type | Rationale | Action |
|---------|------|-----------|--------|
| Their current capabilities | Epistemic | Observable through public products | Product tear-down |
| Their strategic priorities | Mixed | Partially public, partially unknown | Analyst reports + inference |
| Their specific response | Aleatory | Decision not yet made | Scenario planning |
| "Response" definition | Model | Price cut? Feature match? Legal? | Define response categories |
| Response timing | Aleatory | Depends on internal processes | Historical response times |

### Technology Evaluation Example

**Research Question:** Should we adopt GraphQL for our API layer?

| Finding | Type | Rationale | Action |
|---------|------|-----------|--------|
| Performance benchmarks | Epistemic | Measurable; some data exists | Run benchmarks |
| Our specific use case fit | Mixed | Partially knowable, partially judgment | PoC implementation |
| Industry adoption trajectory | Aleatory | Future adoption unpredictable | Monitor trends |
| "Better" API technology | Model | Depends on evaluation criteria | Weight criteria explicitly |
| Migration cost estimate | Epistemic | Our codebase is known | Engineering assessment |

---

## Integration with Evidence Strength

Combine uncertainty type with evidence score:

| Evidence Score | Epistemic | Aleatory | Model |
|----------------|-----------|----------|-------|
| 5 (Primary) | Well-established fact | Rare—aleatory can't be "known" | N/A—model issues aren't evidence |
| 4 (Auth. Secondary) | High-confidence finding | Good scenario inputs | Expert framework choice |
| 3 (Credible) | Medium confidence | Reasonable scenarios | Industry-standard approach |
| 2 (Weak) | Research gap identified | Speculative scenarios | Less common framework |
| 1 (Speculative) | Unknown—needs research | Guess, not scenario | Idiosyncratic definition |

**Key Insight:**
- Epistemic uncertainty with low evidence scores = high-value research targets
- Aleatory uncertainty shouldn't be "researched" more; should be quantified
- Model uncertainty requires explicit choice, not more evidence

---

## Quick Reference

### The One-Line Summary

| Type | Definition | Action |
|------|------------|--------|
| **Epistemic** | We don't know, but COULD | Research it |
| **Aleatory** | Can't know (randomness) | Accept and quantify |
| **Model** | Depends on framework | Choose and state |

### Memory Aid: EAM

- **E**pistemic = **E**liminable (through research)
- **A**leatory = **A**ccept (can't eliminate)
- **M**odel = **M**ake explicit (choose your lens)
