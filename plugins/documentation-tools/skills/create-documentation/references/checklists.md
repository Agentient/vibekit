# Documentation Validation Checklists

Comprehensive checklists for validating documentation across three layers: Structure (Layer A), Content (Layer B), and Experience (Layer C), plus the Mode Boundary Reasoning Audit.

---

## Layer A: Structural Validation

Verifies the document's architecture and organization.

### A1. Diátaxis Alignment

- [ ] Document type is explicitly identified (Tutorial / How-To / Explanation / Reference)
- [ ] Document stays within its quadrant (no mixing types)
- [ ] Structure matches the expected skeleton for this type
- [ ] Title accurately reflects the type and content
- [ ] Purpose aligns with reader's expected goal for this type

**Type-specific structure checks:**

| Type | Required Structure Elements |
|------|----------------------------|
| Tutorial | Prerequisites, Steps with verification, What You Learned, Next Steps, **First-Principles Foundation** |
| How-To | Prerequisites, Numbered steps following **Context→Action→Verification**, Result, Troubleshooting |
| Explanation | Why This Matters, Core concept, **Audience Lens** adaptation, Perspectives, Related concepts |
| Reference | Consistent entry format, Parameters table with **Semantic Descriptions**, Examples, Index |

### A1.1 First-Principles Requirement (Tutorials)

Tutorials must establish foundational understanding before procedural steps:

- [ ] Core concept explained before first action
- [ ] "Why this works" reasoning included
- [ ] No steps that are pure magic ("just do this")
- [ ] Reader could adapt approach to similar problems

### A1.2 Context→Action→Verification Framework (How-Tos)

Every how-to step should follow this pattern:

- [ ] **Context**: What state are we in? What are we trying to achieve?
- [ ] **Action**: What exactly do we do? (copy-paste ready)
- [ ] **Verification**: How do we know it worked?

### A1.3 Audience Lens Requirement (Explanations)

Explanations must be calibrated to their audience:

- [ ] Complexity level matches stated audience
- [ ] Jargon appropriate for expertise level
- [ ] Examples resonate with audience's context
- [ ] Analogies use familiar domains for the audience

### A1.4 Semantic Description Requirement (References)

Reference entries must have meaningful descriptions:

- [ ] Descriptions explain *what it does*, not just *what it is*
- [ ] Purpose is clear from description alone
- [ ] When to use (and when not to) is indicated
- [ ] Relationship to related entries is noted

### A2. Navigation and Flow

- [ ] Table of contents present for documents >500 words
- [ ] Headings form a clear hierarchy (H1 > H2 > H3)
- [ ] Headings are scannable and descriptive
- [ ] Section order is logical for the document type
- [ ] Cross-references use descriptive link text (not "click here")
- [ ] All internal links are valid
- [ ] All external links are valid and relevant

### A3. Length and Density

- [ ] Document length appropriate for reading level:
  - Grade 8: Max 1500 words
  - Grade 12: Max 3000 words
  - Professional: As needed, but chunked
- [ ] No section exceeds 300 words without a subheading break
- [ ] No paragraph exceeds 5 sentences
- [ ] Lists are limited to 7 items (chunk if more)

### A4. Visual Structure

- [ ] Adequate white space between sections
- [ ] Code blocks are clearly demarcated
- [ ] Tables are used appropriately for structured data
- [ ] Callouts (Note, Warning, Tip) are not overused (max 3 per page)
- [ ] Formatting is purposeful, not decorative

---

## Layer B: Content Validation

Verifies accuracy, completeness, and clarity of information.

### B1. Technical Accuracy

- [ ] All statements of fact are correct
- [ ] Code examples are syntactically correct
- [ ] Code examples run without modification (when intended to run)
- [ ] Version numbers and compatibility info are current
- [ ] API signatures match actual implementation
- [ ] Default values are accurate
- [ ] Error messages shown match actual system output

### B2. Completeness

- [ ] All topics promised in introduction are covered
- [ ] Prerequisites are stated explicitly
- [ ] No concepts are used before being introduced
- [ ] Success criteria are defined (reader knows when they're done)
- [ ] Next steps or further reading are provided
- [ ] Required context is included (not assumed)

**Type-specific completeness:**

| Type | Completeness Requirements |
|------|--------------------------|
| Tutorial | Every step for success, verification at each step, recovery paths |
| How-To | All steps to complete task, result verification, common troubleshooting |
| Explanation | Why, what, how, implications, related concepts |
| Reference | All public API/features, all parameters, all options |

### B3. Example Quality

- [ ] Examples are relevant to the topic
- [ ] Examples use realistic values (not "foo", "bar")
- [ ] Examples progress from simple to complex (if multiple)
- [ ] Examples are copy-paste ready (when appropriate)
- [ ] Expected output is shown (when relevant)
- [ ] Edge cases are covered (when important)

### B4. Clarity and Precision

- [ ] No ambiguous pronouns ("it", "this") without clear referent
- [ ] Technical terms are defined on first use
- [ ] Abbreviations are expanded on first use
- [ ] No contradictions or inconsistencies
- [ ] No dead-end references to undefined concepts
- [ ] Scope limitations are explicit ("this guide does not cover...")

---

## Layer C: Experience Validation

Verifies the document serves readers well from their perspective.

### C1. Persona Alignment

**Anxious Novice:**
- [ ] Reassurance present ("Don't worry if...")
- [ ] No assumed knowledge
- [ ] Every step explicitly stated
- [ ] Recovery paths for mistakes
- [ ] Success indicators visible

**Pragmatic Practitioner:**
- [ ] Scannable structure
- [ ] Goal in title/first line
- [ ] Copy-paste ready content
- [ ] Prerequisites upfront
- [ ] No unnecessary explanation

**Curious Explorer:**
- [ ] "Why" explained alongside "what"
- [ ] Connections to related concepts
- [ ] Depth available (links, expandable)
- [ ] Multiple perspectives offered
- [ ] Historical/design context (if relevant)

### C2. Cognitive Load Assessment

- [ ] Chunking is appropriate for topic complexity
- [ ] One concept per sentence/step
- [ ] Related information is co-located
- [ ] Extraneous information removed
- [ ] Visual hierarchy aids scanning
- [ ] Working examples support understanding (tutorials/explanations)

### C3. Entry and Exit Points

- [ ] Document has clear starting point
- [ ] Reader knows within 30 seconds if they're in right place
- [ ] Success criteria are explicit
- [ ] End state is clear
- [ ] "What's next" pathways provided
- [ ] Return paths to broader content exist

---

## Mode Boundary Reasoning Audit

**Purpose:** Detect implicit transitions between documentation modes that can confuse or lose readers. When documentation shifts from explaining to instructing (or vice versa) without warning, readers become disoriented.

### What Is a Mode?

A "mode" is the type of engagement the reader is in:
- **Learning mode** — Building understanding (tutorials, explanations)
- **Doing mode** — Completing a task (how-tos)
- **Looking up mode** — Finding specific info (reference)
- **High-expertise mode** — Assuming domain knowledge
- **Low-expertise mode** — Assuming novice understanding

### Mode Transition Audit

**Step 1: Map Each Section's Mode**

Read through the document and label each section:

| Section | Primary Mode | Expertise Level |
|---------|--------------|-----------------|
| Intro | Explaining | Intermediate |
| Setup | Instructing | Novice |
| Step 1 | Instructing | Novice |
| "Why This Works" aside | Explaining | Expert |
| ... | ... | ... |

**Step 2: Identify All Transitions**

Mark every point where:
- [ ] Mode changes (explaining ↔ instructing ↔ referencing)
- [ ] Expertise level changes (novice ↔ intermediate ↔ expert)
- [ ] Document type shifts (tutorial content in a how-to, etc.)

**Step 3: Verify Transition Markers**

For each transition, check:
- [ ] Transition is explicit (new section, clear signal)
- [ ] Reader is prepared for the shift
- [ ] No jarring jumps in assumed knowledge

### Mode Transition Red Flags

| Red Flag | Example | Fix |
|----------|---------|-----|
| Sudden jargon increase | "Configure the API" then "Set up OAuth2 PKCE flow with JWKS endpoints" | Define terms or link to explanation |
| Unexplained prerequisites mid-doc | Step 5 assumes setup from different guide | Link to prerequisite or include setup |
| "Obviously" or "Simply" | "Simply configure the cache" | Remove or add detail |
| "As you know" | "As you know, REST uses HTTP verbs" | Either assume they know (skip) or explain |
| Explanation in how-to | Theory paragraph between steps | Move to aside or link |
| Instructions in explanation | "Now run this command to see..." | Link to how-to instead |

### Mode Boundary Verification Process

1. **Fresh eyes read** — Read as if unfamiliar; note confusion points
2. **Section mode mapping** — Label each section's mode
3. **Transition identification** — List all mode changes
4. **Marker verification** — Ensure each transition is signaled
5. **Expertise tracking** — Check for implicit expertise jumps

### Boundary Markers to Use

When mode transitions are necessary, use explicit markers:

**Before explaining in a how-to:**
```markdown
**Background:** (optional reading)
[Explanation content]
```

**Before advanced content:**
```markdown
**Note:** This section assumes familiarity with X.
New to X? See the [introduction to X](./intro-x.md).
```

**Before instructions in an explanation:**
```markdown
**Try it:** If you want to see this in action, follow
these quick steps:
[Brief how-to content]
```

---

## Pre-Publication Final Checklist

Run after all three layers pass.

### Completeness

- [ ] All Layer A checks pass
- [ ] All Layer B checks pass
- [ ] All Layer C checks (for primary persona) pass
- [ ] Mode Boundary Reasoning Audit completed
- [ ] MECE verification completed (see self-audit-protocol.md)

### Technical Verification

- [ ] All code examples tested
- [ ] All links verified
- [ ] Screenshots current (if present)
- [ ] Version numbers accurate

### Editorial

- [ ] Spell check completed
- [ ] Formatting consistent throughout
- [ ] Style guide compliance verified
- [ ] No placeholder text remains

### Metadata

- [ ] Document type correctly specified
- [ ] Audience/persona identified
- [ ] Reading level appropriate
- [ ] Title is accurate and descriptive

---

## Quick Reference: Which Checklist When

| Situation | Required Checklists |
|-----------|-------------------|
| New documentation | All layers + MECE |
| Minor update | Layer B (accuracy) only |
| Structural change | Layer A + B |
| Audience change | Layer C + Mode Audit |
| Pre-publication | All layers + Final |
