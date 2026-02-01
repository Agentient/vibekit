# Assumption Surfacing Protocol

A systematic approach to identifying, categorizing, and validating assumptions during knowledge elicitation.

---

## Overview

### Why Assumptions Matter

Assumptions are the invisible architecture of knowledge. Unsurfaced assumptions:
- Lead to misaligned understanding
- Create brittle solutions
- Cause downstream failures when conditions change
- Mask the true scope of uncertainty

### The Three Types

| Type | Definition | Visibility | Risk |
|------|------------|------------|------|
| **Explicit** | Directly stated by interviewee | High | Low (already acknowledged) |
| **Implicit** | Unstated beliefs underlying responses | Medium | Medium (can be surfaced) |
| **Structural** | Embedded in the interview framing | Low | High (often invisible) |

---

## 1. Explicit Assumptions

### Definition
Assumptions the interviewee directly states or acknowledges.

### Indicators
- "We're assuming that..."
- "This depends on..."
- "Given that [condition]..."
- "Assuming [X] is true..."
- "If [Y] holds..."

### Examples

**Stated explicitly:**
- "We're assuming budget isn't a constraint for this quarter."
- "This only works if the API remains backward compatible."
- "I'm assuming you want the enterprise version, not the free tier."

### Capture Protocol

1. **Document verbatim** when stated
2. **Confirm scope:** "When you say 'budget isn't a constraint,' does that include headcount as well?"
3. **Test importance:** "What would change if that assumption turned out to be wrong?"
4. **Categorize:** Business / Technical / Temporal / Scope

### Validation

Explicit assumptions should always be validated:
```
"You mentioned we're assuming [X]. Just to confirm:
- Is that assumption documented somewhere?
- Who else shares this assumption?
- What would invalidate it?"
```

---

## 2. Implicit Assumptions

### Definition
Unstated beliefs that underlie what the interviewee says, inferred from word choice, framing, or what's omitted.

### Detection Signals

| Signal | Example | Implicit Assumption |
|--------|---------|---------------------|
| **Certainty language** | "Obviously we need..." | This requirement is universal |
| **Embedded causation** | "Because users want X..." | Users have been asked |
| **Omission** | No mention of mobile | Desktop-first thinking |
| **Jargon without definition** | "We'll use the standard approach" | Shared understanding exists |
| **Time references** | "When this launches..." | Launch will happen |

### Examples

**Implicit (not stated):**
- Response: "We need real-time updates."
  - Implicit: Users check frequently enough to need real-time
  - Implicit: Network conditions support real-time
  - Implicit: Cost of real-time is acceptable

- Response: "The admin handles that."
  - Implicit: Admin is available when needed
  - Implicit: Admin has sufficient permissions
  - Implicit: One admin is enough

### Surfacing Techniques

**Technique 1: "What would have to be true?"**
```
"For that to work, what would have to be true?"
"What conditions are you taking for granted here?"
```

**Technique 2: "Reverse the assumption"**
```
"What if [opposite of implicit assumption]?"
"What if users don't actually want real-time updates?"
```

**Technique 3: "Outsider perspective"**
```
"If someone from a different industry heard this, what would they question?"
"What would a skeptic push back on?"
```

**Technique 4: "Fill in the blank"**
```
"When you say 'standard approach,' you mean...?"
"The 'obvious' solution here is obvious because...?"
```

### Validation

Once surfaced, make it explicit:
```
"It sounds like we're assuming [surfaced assumption].
Is that right? Should we document that as a known assumption?"
```

---

## 3. Structural Assumptions

### Definition
Assumptions embedded in the very framing of the interview—what's in scope, how concepts are defined, which perspectives are included.

### Why They're Dangerous
- Invisible to both interviewer and interviewee
- Shape what questions get asked
- Determine what answers seem relevant
- Often only visible in hindsight

### Detection Signals

| Signal | Structural Assumption |
|--------|----------------------|
| Interview focuses on one user type | Other users don't matter |
| Technical framing only | Organizational factors irrelevant |
| Current state focus | Future evolution not important |
| Success metrics undefined | We agree on what "good" means |
| Stakeholders not listed | We know who matters |

### Examples

**Structural (embedded in framing):**
- We structured the interview around technical dimensions
  - Assumes: Technical factors are primary
  - Missed: Organizational politics, budget constraints, user training

- We're interviewing the product manager
  - Assumes: PM has complete knowledge
  - Missed: Engineering constraints, support team insights

- We defined the topic as "authentication"
  - Assumes: Auth is separable from identity management
  - Missed: Authorization, session management, SSO

### Surfacing Techniques

**Technique 1: "Question the frame"**
```
"Why did we frame this as a [X] problem rather than a [Y] problem?"
"What if we defined [topic] differently?"
```

**Technique 2: "Missing voices"**
```
"Whose perspective haven't we heard?"
"Who might see this problem completely differently?"
```

**Technique 3: "Alternative structures"**
```
"If we organized this around [different dimension], what would change?"
"What dimensions did we not include that we could have?"
```

**Technique 4: "Scope the scope"**
```
"Why is [X] out of scope? What if it were in?"
"What did we decide not to ask about?"
```

### Meta-Assumption Check

At end of Phase 5 or during Phase 6:
```
"Stepping back—what assumptions have we made about
this interview itself? What did we choose not to explore?"
```

---

## Assumption Inventory Format

### Per-Assumption Record

```yaml
assumption:
  id: A1
  type: explicit | implicit | structural
  statement: "[The assumption in clear language]"
  source: "[How it was identified]"
  confidence: 0.0-1.0
  validated: true | false | contested
  validator: "[Who confirmed]"
  implications:
    - "[What depends on this assumption]"
    - "[What would change if wrong]"
  conditions_to_invalidate:
    - "[What would make this false]"
```

### Summary Table Format

| ID | Type | Assumption | Validated | Criticality | Dependencies |
|----|------|------------|-----------|-------------|--------------|
| A1 | Explicit | Budget unconstrained | Yes (CFO) | High | Timeline, scope |
| A2 | Implicit | Users want real-time | Partial | Medium | Architecture |
| A3 | Structural | Tech focus appropriate | No | High | Entire analysis |

---

## Validation Protocol

### For Critical Assumptions

1. **State it clearly:** "We're assuming [X]."
2. **Confirm understanding:** "Is that right?"
3. **Test importance:** "What depends on this?"
4. **Check validity:** "How confident are you in this?"
5. **Identify triggers:** "What would cause this to change?"
6. **Document owner:** "Who should we check with to validate?"

### Validation Levels

| Level | Description | When to Use |
|-------|-------------|-------------|
| **Unvalidated** | Just identified | Default state |
| **Self-validated** | Interviewee confirms | Single source |
| **Cross-validated** | Multiple sources agree | Moderate stakes |
| **Documented** | Formal record exists | High stakes |
| **Contested** | Disagreement exists | Flag for resolution |

---

## Integration with Knowledge Map

### Linking Assumptions to Findings

Every finding should reference its assumptions:

```xml
<finding id="F1" confidence="0.85">
  <statement>Users need sub-100ms latency</statement>
  <assumptions>
    <ref assumption_id="A1">Network conditions support this</ref>
    <ref assumption_id="A2">Users notice latency above 100ms</ref>
  </assumptions>
</finding>
```

### Confidence Adjustment

Finding confidence should be capped by assumption confidence:

```
Finding confidence = min(evidence_confidence, critical_assumption_confidence)
```

If a finding depends on an unvalidated assumption, flag it:

```xml
<finding id="F2" confidence="0.70" assumption_risk="high">
  <statement>System can scale to 10K concurrent users</statement>
  <note>Depends on unvalidated assumption A3</note>
</finding>
```

---

## Quick Reference

### Surfacing Questions

| To Surface | Ask |
|-----------|-----|
| Explicit | "What are we taking as given here?" |
| Implicit | "What would have to be true for that to work?" |
| Structural | "What did we choose not to ask about?" |

### Red Flags

| Signal | Suggests |
|--------|----------|
| "Obviously..." | Unexamined assumption |
| "Everyone knows..." | Implicit assumption |
| No mention of [X] | Structural blind spot |
| High confidence, low evidence | Assumption-dependent |

### Validation Priority

1. **Critical + Unvalidated** → Validate immediately
2. **Critical + Contested** → Resolve before proceeding
3. **Non-critical + Unvalidated** → Document, move on
4. **Structural** → Always surface, discuss impact
