# Bias Protection Techniques

Methods for detecting and mitigating cognitive biases during knowledge elicitation.

---

## Overview

### Why Bias Protection Matters

Both interviewer and interviewee bring cognitive biases that distort captured knowledge:
- **Interviewer biases** shape which questions get asked and how answers are interpreted
- **Interviewee biases** shape what information is shared and how it's framed

### Core Techniques

| Technique | Purpose | When to Apply |
|-----------|---------|---------------|
| **Frame Equivalence** | Detect framing effects | Critical claims, emotional topics |
| **Disconfirmation Hunting** | Counter confirmation bias | Confident assertions |
| **Assumption Surfacing** | Make implicit explicit | After substantive answers |
| **Anchoring Detection** | Identify order effects | First-mentioned solutions |
| **Availability Mitigation** | Counter recency bias | Recent/vivid examples |
| **Representativeness Check** | Counter pattern-matching | Generalizations |

---

## 1. Frame Equivalence Testing

### Purpose
Verify that a finding holds regardless of how the question is framed. Findings that only emerge under certain framing are frame-dependent and should be flagged.

### When to Apply
- Emotionally charged topics
- Claims with high stakes
- Situations where interviewer chose the frame
- Answers that seem "too clean"

### Method

**Step 1: Identify the frame**
Original question: "What problems does the current system have?"
Frame: Deficit-focused, assumes problems exist

**Step 2: Construct equivalent opposite frame**
Reframe: "What works well about the current system?"

**Step 3: Ask and compare**
If the "problems" from Q1 appear as absent "strengths" in Q2 → finding is robust
If new information emerges → finding was frame-dependent

### Examples

**Example 1: Problem/Solution Framing**
```
Original: "What would make the onboarding better?"
Reframe: "What would a user lose if onboarding changed?"

Compare: Does the "better" version preserve what users value?
```

**Example 2: Gain/Loss Framing**
```
Original: "What would you gain from implementing this?"
Reframe: "What would you lose by not implementing this?"

Compare: Is the magnitude of gain/loss symmetric?
```

**Example 3: Internal/External Attribution**
```
Original: "Why did the project fail?"
Reframe: "What external factors contributed to the outcome?"

Compare: Does attribution balance internal/external factors?
```

### Documenting Frame Effects

```xml
<finding id="F1" frame_sensitivity="high">
  <statement_positive_frame>Users want faster checkout</statement_positive_frame>
  <statement_negative_frame>Users avoid slow experiences</statement_negative_frame>
  <equivalence_test>
    <result>Partial equivalence - magnitude differs by 2x</result>
    <note>Loss framing produces stronger response</note>
  </equivalence_test>
</finding>
```

---

## 2. Disconfirmation Hunting

### Purpose
Actively seek evidence against current understanding to counter confirmation bias.

### When to Apply
- After confident assertions
- When building consensus feels "too easy"
- On foundational assumptions
- Before closing a dimension

### Method

**Technique 1: Direct Challenge**
```
"What would make you wrong about that?"
"What's the strongest argument against this position?"
"Who disagrees with this view, and why?"
```

**Technique 2: Pre-Mortem**
```
"Imagine we implemented this and it failed spectacularly.
What would the post-mortem reveal?"
```

**Technique 3: Counter-Example Request**
```
"Can you think of a case where this didn't hold true?"
"When has the opposite been true?"
```

**Technique 4: Steel-Man Opposition**
```
"If I were to argue the opposite position as strongly as possible,
what would be my best points?"
```

### Red Flags Indicating Need for Disconfirmation

| Signal | Bias Risk | Disconfirmation Approach |
|--------|-----------|--------------------------|
| "Obviously..." | Anchoring | Challenge the obvious |
| "Everyone agrees..." | False consensus | Find the dissenters |
| "This always works..." | Overgeneralization | Find the exceptions |
| No downsides mentioned | Optimism bias | Force negatives |
| Quick consensus | Groupthink | Introduce friction |

### Documenting Disconfirmation

```yaml
finding: "Feature X is critical"
confidence_before_disconfirmation: 0.90
disconfirmation_hunt:
  challenges_raised:
    - "What if users don't adopt it?"
    - "What evidence suggests users actually need this?"
  counter_evidence_found:
    - "20% of similar features go unused"
    - "No direct user request for this"
  response: "Interviewee acknowledged uncertainty"
confidence_after_disconfirmation: 0.70
```

---

## 3. Assumption Surfacing

### Purpose
Make implicit assumptions explicit so they can be validated or challenged.

### Three Types of Assumptions

| Type | Definition | Detection Method |
|------|------------|------------------|
| **Explicit** | Stated directly by interviewee | Listen for "I assume" or "I think" |
| **Implicit** | Embedded in statements | Parse for unstated premises |
| **Structural** | Framework/worldview assumptions | Notice framing and categorization |

### When to Apply
- After each substantive answer
- When conclusions seem to rest on unstated premises
- When interviewee's worldview shapes their response
- Before finalizing any high-confidence finding

### Protocol

**Step 1:** After each substantive answer, identify unstated premises

**Step 2:** Ask explicitly:
```
"What assumptions are you making about [X]?"
"What would have to be true for [conclusion] to hold?"
```

**Step 3:** Surface and confirm:
```
"It sounds like you're assuming [Y]. Is that right?"
"You seem to be taking [Z] for granted. Is that intentional?"
```

**Step 4:** Categorize each assumption by type (explicit/implicit/structural)

**Step 5:** Assess impact:
```
"If [assumption] weren't true, would your conclusion change?"
"What depends on this assumption being correct?"
```

### Detection Techniques

**For Explicit Assumptions:**
- Listen for: "I assume...", "I think...", "We're betting on..."
- Document verbatim when stated

**For Implicit Assumptions:**
- Parse statements for hidden premises
- Ask: "What does that depend on?"
- Probe: "For that to work, what would need to be true?"

**For Structural Assumptions:**
- Notice categorization choices
- Question framing: "Why are we looking at it this way?"
- Explore alternatives: "What if we framed this differently?"

### Assumption Inventory Template

```xml
<assumption_inventory>
  <assumption id="A1" type="explicit" impact="high">
    <statement>[Assumption statement]</statement>
    <evidence>Direct statement in turn [N]</evidence>
    <alternative>[What if this weren't true]</alternative>
  </assumption>
  <assumption id="A2" type="implicit" impact="medium">
    <statement>[Assumption statement]</statement>
    <evidence>Inferred from context</evidence>
    <alternative>[Alternative assumption]</alternative>
  </assumption>
  <assumption id="A3" type="structural" impact="high">
    <statement>[Assumption statement]</statement>
    <evidence>Framing of questions/answers</evidence>
    <alternative>[Alternative framework]</alternative>
  </assumption>
</assumption_inventory>
```

### Impact Assessment Matrix

| Impact Level | Definition | Action Required |
|--------------|------------|-----------------|
| **High** | Conclusion invalid if assumption wrong | Must validate |
| **Medium** | Conclusion weakened if assumption wrong | Validate if time permits |
| **Low** | Conclusion still holds regardless | Document only |

### Example

**Interview context:** Discussing mobile app requirements

**Statement:** "Users will update the app regularly to get new features."

**Assumption surfacing:**
- **Implicit assumption:** Users have auto-update enabled
- **Implicit assumption:** Users have sufficient storage for updates
- **Structural assumption:** Features drive user behavior (vs. necessity)

**Probe:** "What if users don't update? How would that change the approach?"

**Response:** "Oh, we'd need to support older versions longer. That changes the architecture significantly."

**Impact:** High - affects architecture decisions

---

## 4. Anchoring Detection

### Purpose
Identify when first-mentioned options or numbers unduly influence subsequent responses.

### When to Apply
- Numerical estimates
- Priority rankings
- Solution comparisons
- After strong first impressions

### Detection Signals

| Signal | Possible Anchoring |
|--------|-------------------|
| First option favored | Order effect |
| Estimate close to example | Number anchoring |
| "That sounds right" | Lazy agreement |
| No consideration of alternatives | Premature closure |

### Method

**Technique 1: Delay First Mention**
Don't introduce numbers or options first. Let interviewee anchor themselves.

**Technique 2: Order Scrambling**
If you must present options, vary the order:
```
"We could do A, B, or C... actually, let me reorder that.
What do you think about B, then C, then A?"
```

**Technique 3: Explicit De-Anchoring**
```
"Setting aside the first option we discussed,
what would you choose if that weren't available?"
```

**Technique 4: Range Expansion**
For numerical anchoring:
```
"You estimated 10K users. What if I told you some similar
systems see 50K or 2K? Would that change your thinking?"
```

### Documenting Anchoring Concerns

```xml
<finding id="F1" anchoring_risk="medium">
  <statement>Estimated load: 10,000 concurrent users</statement>
  <anchor_check>
    <initial_estimate>10,000</initial_estimate>
    <after_range_expansion>5,000-20,000 range acknowledged</after_range_expansion>
    <conclusion>Initial estimate may be anchored to round number</conclusion>
  </anchor_check>
  <recommendation>Validate with actual data before committing</recommendation>
</finding>
```

---

## 5. Availability Bias Mitigation

### Purpose
Counter the tendency to weight recent or vivid examples more heavily than representative ones.

### When to Apply
- After dramatic/memorable examples
- When recent events dominate
- When generalizing from specific cases

### Detection Signals

| Signal | Suggests Availability Bias |
|--------|---------------------------|
| "Just last week..." | Recency weighting |
| Dramatic story dominates | Vividness weighting |
| One case used as proof | Sample size of 1 |
| Emotional response | Memory salience |

### Method

**Technique 1: Frequency Probe**
```
"Is that typical or exceptional?"
"How often does that actually happen?"
"Was that a representative case or an outlier?"
```

**Technique 2: Base Rate Request**
```
"Before that incident, what was the normal pattern?"
"Across all cases, what's the distribution?"
```

**Technique 3: Counter-Vividness**
```
"Can you think of a boring, normal case?
What happened there?"
```

**Technique 4: Time Distance**
```
"What was your view before that recent event?"
"A year ago, would you have said the same thing?"
```

### Documenting Availability Concerns

```xml
<finding id="F1" availability_risk="high">
  <statement>System crashes are a major problem</statement>
  <evidence_source>Recent high-profile crash</evidence_source>
  <availability_check>
    <recency_factor>Incident was 2 weeks ago</recency_factor>
    <base_rate_check>
      <question>How many crashes in the past year?</question>
      <response>Actually, just 3 total</response>
    </base_rate_check>
    <revised_assessment>Crashes rare but impactful when occur</revised_assessment>
  </availability_check>
</finding>
```

---

## 6. Representativeness Check

### Purpose
Counter the tendency to assume instances match prototypes or patterns without verification.

### When to Apply
- Generalizations ("Users always...")
- Pattern claims ("This is just like...")
- Stereotype-based reasoning

### Detection Signals

| Signal | Representativeness Risk |
|--------|------------------------|
| "Users are like..." | Stereotype |
| "This is the same as..." | False analogy |
| "Obviously that means..." | Pattern matching |
| Single example → universal claim | Overgeneralization |

### Method

**Technique 1: Variation Probe**
```
"What types of users don't fit that pattern?"
"When does that generalization break down?"
```

**Technique 2: Base Rate Comparison**
```
"What percentage of cases actually match that pattern?"
"How often is the exception rather than the rule?"
```

**Technique 3: Analogy Challenge**
```
"That seems similar to [X]. But how is it different?"
"What doesn't transfer from that analogy?"
```

---

## Validation Mode Calibration

### How Validation Mode Affects Bias Protection

| Technique | Empathetic | Balanced | Rigorous |
|-----------|------------|----------|----------|
| Frame Equivalence | Rare, soft | Strategic | Systematic |
| Disconfirmation | Minimal | Targeted | Every claim |
| Anchoring Detection | Passive | Active for estimates | Aggressive |
| Availability Mitigation | Gentle probes | Frequency checks | Base rates required |
| Representativeness | Accept generalizations | Spot-check | Challenge all |

### Empathetic Mode Adjustments
- Frame checks only on clearly emotional topics
- Disconfirmation as "exploring alternatives"
- Soft language: "I wonder if..." vs "What if you're wrong?"

### Rigorous Mode Additions
- Every confident claim gets disconfirmation hunt
- All estimates checked for anchoring
- Frame equivalence on all major findings
- No generalization accepted without counter-examples

---

## Integration Checklist

### Before Closing a Dimension

- [ ] High-confidence claims disconfirmation-hunted?
- [ ] Critical findings frame-equivalence tested?
- [ ] Estimates checked for anchoring?
- [ ] Vivid examples checked against base rates?
- [ ] Generalizations verified with counter-examples?

### Flagging in Output

Use bias risk flags in knowledge artifacts:

```xml
<finding id="F1" confidence="0.85"
         bias_flags="availability:low,anchoring:none,frame:tested">
  <statement>...</statement>
  <bias_protection_applied>
    <frame_equivalence result="passed"/>
    <disconfirmation result="no counter-evidence found"/>
  </bias_protection_applied>
</finding>
```

---

## Quick Reference

### Bias Detection Questions

| Bias | Detection Question |
|------|-------------------|
| **Framing** | "Would this hold if we asked differently?" |
| **Confirmation** | "What would prove this wrong?" |
| **Anchoring** | "What if the first number was different?" |
| **Availability** | "Is that typical or just memorable?" |
| **Representativeness** | "What doesn't fit the pattern?" |

### Red Flag Phrases

| Phrase | Likely Bias |
|--------|-------------|
| "Obviously..." | Anchoring, Confirmation |
| "Just recently..." | Availability |
| "Users always..." | Representativeness |
| "Everyone knows..." | False consensus |
| "That's exactly like..." | Representativeness |
