# Epistemic Labeling Guide

A systematic framework for classifying the certainty level of knowledge claims gathered during interviews.

---

## Overview

### The 5-Tier System

| Label | Definition | Confidence | Action |
|-------|------------|------------|--------|
| **FACT** | Verified, documented truth | 95-100% | Use directly |
| **LIKELY** | Strong evidence, high probability | 80-94% | Use with note |
| **PLAUSIBLE** | Reasonable inference, moderate evidence | 60-79% | Validate if critical |
| **ASSUMPTION** | Taken as true without direct evidence | 40-59% | Surface and validate |
| **UNCERTAIN** | Insufficient information to assess | 0-39% | Flag as gap |

### Purpose

Epistemic labeling serves three functions:
1. **Transparency** - Stakeholders know what's proven vs. assumed
2. **Prioritization** - Focus validation effort on critical low-confidence claims
3. **Gap Detection** - UNCERTAIN labels reveal MECE coverage gaps

---

## Knowledge Map Structure

Organize gathered knowledge into four epistemic categories:

```
KNOWN (directly stated)
├── Facts verified by interviewee
└── Explicit claims with high confidence

BELIEVED (strong inference)
├── Patterns from multiple statements
└── Consistent implications

ASSUMED (interviewer interpretation)
├── Context-based inferences
└── Unstated but implied

UNKNOWN (gaps identified)
├── Questions not yet asked
├── Ambiguous responses
└── Explicit uncertainty from interviewee
```

### Mapping Labels to Categories

| Category | Labels | Confidence Range |
|----------|--------|------------------|
| KNOWN | FACT | 95-100% |
| BELIEVED | LIKELY | 80-94% |
| BELIEVED | PLAUSIBLE | 60-79% |
| ASSUMED | ASSUMPTION | 40-59% |
| UNKNOWN | UNCERTAIN | 0-39% |

---

## 1. FACT (95-100%)

### Definition
Information that is verified, documented, or directly observable. The source is authoritative and current.

### Evidence Requirements
- Primary source documentation (official docs, contracts, code)
- Direct observation or measurement
- Multiple independent confirmations
- Recent (within relevance window for domain)

### Examples
```
FACT: "The API rate limit is 1000 requests per minute"
Evidence: Official API documentation, verified 2024-01-15

FACT: "The system uses PostgreSQL 15"
Evidence: Direct inspection of docker-compose.yml

FACT: "The team has 5 engineers"
Evidence: HR records, confirmed by manager
```

### When to Assign
- Interviewee provides documented evidence
- Claim is verifiable and has been verified
- Information comes from authoritative source

---

## 2. LIKELY (80-94%)

### Definition
Strong evidence supports the claim, but it hasn't been independently verified or may have minor gaps.

### Evidence Requirements
- Credible secondary sources
- Consistent with multiple data points
- Subject matter expert testimony
- No contradicting evidence found

### Examples
```
LIKELY: "Most users access the system via mobile"
Evidence: Analytics dashboard shows 72% mobile, PM confirms pattern

LIKELY: "The migration will take 2-3 months"
Evidence: Engineering lead estimate based on similar past projects

LIKELY: "Competitor X is planning to enter our market"
Evidence: Job postings, conference talks, analyst reports align
```

### When to Assign
- Expert opinion with rationale
- Consistent indirect evidence
- Reasonable inference from strong data

---

## 3. PLAUSIBLE (60-79%)

### Definition
Reasonable inference based on available evidence, but significant uncertainty remains.

### Evidence Requirements
- Logical reasoning from known facts
- Partial evidence supports claim
- No strong contradicting evidence
- Expert considers it reasonable

### Examples
```
PLAUSIBLE: "Users abandon checkout due to payment friction"
Evidence: Drop-off data at payment step, some user complaints,
          but no direct user research conducted

PLAUSIBLE: "The legacy system can handle 2x current load"
Evidence: Informal testing suggests yes, but no load testing done

PLAUSIBLE: "Enterprise customers want SSO integration"
Evidence: 3 of 10 prospects mentioned it, industry trend supports
```

### When to Assign
- Reasonable inference but gaps in evidence
- Interviewee expresses moderate confidence
- Supporting evidence is indirect

---

## 4. ASSUMPTION (40-59%)

### Definition
Taken as true for purposes of the interview/project, but lacks direct evidence. Often embedded in how questions are framed.

### Evidence Requirements
- No direct evidence required (that's the point)
- Should be explicitly stated
- May be based on convention or past experience
- Often revealed through probing

### Examples
```
ASSUMPTION: "Users prefer simplicity over features"
Evidence: None - this is how we've framed product decisions

ASSUMPTION: "Budget will be approved for Q2"
Evidence: Manager mentioned it's likely, no formal approval

ASSUMPTION: "The current architecture can be extended"
Evidence: Architects believe so, but no formal assessment
```

### When to Assign
- Interviewee says "we assume..." or "we're betting on..."
- Implicit belief underlying other claims
- No validation has occurred
- Would significantly change conclusions if wrong

### Surfacing Techniques
- "What would have to be true for that to work?"
- "What are you taking for granted here?"
- "Has that been validated?"

---

## 5. UNCERTAIN (0-39%)

### Definition
Insufficient information to make any assessment. Represents a knowledge gap.

### Evidence Requirements
- Cannot assess due to missing information
- Contradictory evidence with no resolution
- Outside interviewee's knowledge domain
- Requires research or investigation

### Examples
```
UNCERTAIN: "How many concurrent users the system can handle"
Evidence: No load testing done, no monitoring in place

UNCERTAIN: "Whether competitors have patents in this space"
Evidence: No patent search conducted

UNCERTAIN: "What the regulatory requirements will be in 2025"
Evidence: Regulation still being drafted
```

### When to Assign
- Interviewee says "I don't know"
- Question is outside their expertise
- Conflicting information can't be resolved
- Required data doesn't exist

### Action Required
- Flag as MECE gap
- Determine if gap is critical
- Identify how to resolve (research, different interviewee, etc.)

---

## Classification Decision Tree

```
START: Evaluate claim
│
├─ Is there documented, verifiable evidence?
│  ├─ YES → Is the source authoritative and current?
│  │         ├─ YES → FACT (95-100%)
│  │         └─ NO → LIKELY (80-94%)
│  │
│  └─ NO → Is there strong indirect evidence?
│          ├─ YES → Is the inference strong?
│          │         ├─ YES → LIKELY (80-94%)
│          │         └─ NO → PLAUSIBLE (60-79%)
│          │
│          └─ NO → Is there any basis for the claim?
│                   ├─ YES → ASSUMPTION (40-59%)
│                   └─ NO → UNCERTAIN (0-39%)
```

---

## Evidence Quality Markers

### Strong Evidence (+confidence)
- Primary source documentation
- Multiple independent confirmations
- Direct measurement or observation
- Expert with domain authority
- Recent and relevant timeframe

### Weak Evidence (-confidence)
- Single source, unverified
- Hearsay or secondhand
- Outdated information
- Outside expertise domain
- Contradicted by other evidence

---

## Confidence Calculation Formula

### Weighted Confidence Score

```
Overall Confidence = Σ(Claim Confidence × Claim Weight) / Σ(Claim Weight)
```

### Claim Weights by Priority

| Priority | Weight | Rationale |
|----------|--------|-----------|
| Critical | 3 | Must-have for valid output |
| Important | 2 | Significantly affects conclusions |
| Supporting | 1 | Adds context but not essential |

### Example Calculation

| Claim | Confidence | Priority | Weight | Weighted |
|-------|------------|----------|--------|----------|
| C1 | 0.95 | Critical | 3 | 2.85 |
| C2 | 0.80 | Important | 2 | 1.60 |
| C3 | 0.70 | Supporting | 1 | 0.70 |
| C4 | 0.85 | Critical | 3 | 2.55 |
| **Total** | | | **9** | **7.70** |

**Overall Confidence = 7.70 / 9 = 0.856 (86%)**

---

## Upgrade and Downgrade Triggers

### Upgrade Triggers (increase confidence)
| From | To | Trigger |
|------|-----|---------|
| UNCERTAIN | ASSUMPTION | Interviewee provides reasoning |
| ASSUMPTION | PLAUSIBLE | Supporting evidence found |
| PLAUSIBLE | LIKELY | Multiple confirmations |
| LIKELY | FACT | Primary source verified |

### Downgrade Triggers (decrease confidence)
| From | To | Trigger |
|------|-----|---------|
| FACT | LIKELY | Source recency questioned |
| LIKELY | PLAUSIBLE | Contradicting evidence found |
| PLAUSIBLE | ASSUMPTION | Key evidence invalidated |
| ASSUMPTION | UNCERTAIN | Interviewee retracts |

---

## Integration with MECE Gap Detection

### Coverage Status by Label

| Label | Coverage Status | Action |
|-------|-----------------|--------|
| FACT | Fully covered | None needed |
| LIKELY | Covered with caveat | Note in output |
| PLAUSIBLE | Partially covered | Validate if critical |
| ASSUMPTION | Coverage at risk | Must surface and validate |
| UNCERTAIN | **GAP** | Close gap or document |

### Gap Detection Protocol

Every 4-6 questions, scan Knowledge Map for:
1. Dimensions with no FACT or LIKELY findings
2. Critical dimensions with only ASSUMPTION/UNCERTAIN
3. UNCERTAIN findings in must-have areas

Flag dimensions below threshold:
- Critical dimensions: Need ≥1 FACT or LIKELY
- Important dimensions: Need ≥1 PLAUSIBLE or better
- Nice-to-have: ASSUMPTION acceptable

---

## Output Format

### Per-Finding Label

```xml
<finding id="F1" epistemic_label="LIKELY" confidence="0.85">
  <statement>Users primarily access via mobile devices</statement>
  <evidence_basis>Analytics data, PM confirmation</evidence_basis>
  <evidence_quality>Strong indirect - multiple sources align</evidence_quality>
  <upgrade_path>Direct user survey would confirm</upgrade_path>
</finding>
```

### Summary Statistics

```xml
<epistemic_summary>
  <distribution>
    <tier label="FACT" count="5" percentage="20%"/>
    <tier label="LIKELY" count="8" percentage="32%"/>
    <tier label="PLAUSIBLE" count="6" percentage="24%"/>
    <tier label="ASSUMPTION" count="4" percentage="16%"/>
    <tier label="UNCERTAIN" count="2" percentage="8%"/>
  </distribution>
  <critical_gaps>
    <gap dimension="scalability" current_label="UNCERTAIN"/>
  </critical_gaps>
  <validation_needed>
    <finding ref="F7" reason="Critical assumption"/>
    <finding ref="F12" reason="Contradicting evidence"/>
  </validation_needed>
</epistemic_summary>
```

---

## Confidence Calibration Questions

Use these questions to calibrate interviewee's self-assessed confidence:

### The Three Calibration Questions

1. **Completeness Check:**
   "On a scale of 1-10, how confident are you that we've captured the complete picture of [topic]?"

2. **Gap Surfacing:**
   "Is there anything important we haven't discussed that I should know?"

3. **Action Readiness:**
   "If I had to act on this information tomorrow, would you be comfortable with that?"

### Interpreting Responses

| Response Pattern | Interpretation | Action |
|------------------|----------------|--------|
| High on all three | Interview complete | Proceed to synthesis |
| Low on completeness | Coverage gaps | Return to Phase 3 |
| Yes to gap question | Unknown unknowns surfaced | Explore new area |
| No to action readiness | Quality concerns | Identify specific doubts |

### Calibration Integration

Record calibration in final output:

```xml
<interviewee_calibration>
  <completeness_score>8</completeness_score>
  <gaps_surfaced>None mentioned</gaps_surfaced>
  <action_ready>Yes, with caveat about timeline assumptions</action_ready>
</interviewee_calibration>
```

---

## Quick Reference

### Label Selection

| If interviewee says... | Assign |
|------------------------|--------|
| "It's documented in..." | FACT |
| "I'm confident that..." | LIKELY |
| "I think..." / "Probably..." | PLAUSIBLE |
| "We assume..." / "We're betting..." | ASSUMPTION |
| "I don't know" / "Not sure" | UNCERTAIN |

### Confidence Shortcuts

| Evidence Type | Typical Range |
|---------------|---------------|
| Primary documentation | 95-100% (FACT) |
| Expert + rationale | 80-90% (LIKELY) |
| Logical inference | 65-79% (PLAUSIBLE) |
| Stated assumption | 45-59% (ASSUMPTION) |
| No basis | 0-39% (UNCERTAIN) |
