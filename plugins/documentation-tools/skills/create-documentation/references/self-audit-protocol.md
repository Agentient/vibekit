# Self-Audit Protocol

Final verification protocol ensuring documentation is complete, coherent, and ready for publication. Includes reasoning chain audit, assumption inventory, confidence calibration, MECE verification, orphan concept detection, and readability passes.

---

## Reasoning Chain Audit

Trace the logical flow of the document to ensure each step follows from the previous.

### Purpose

Documentation should present ideas in a logical sequence where each concept builds on established foundations. Broken reasoning chains leave readers confused about how conclusions were reached.

### Audit Process

**Step 1: Extract the Argument Chain**

For each section, identify:
- What claim or instruction is being made?
- What evidence or reasoning supports it?
- What prior knowledge does it depend on?

**Step 2: Verify Each Link**

| Check | Question | If Fails |
|-------|----------|----------|
| Foundation | Is the supporting concept already established? | Add prerequisite or reorder |
| Logic | Does the conclusion follow from the evidence? | Strengthen reasoning or qualify claim |
| Completeness | Are any steps in the reasoning skipped? | Add missing intermediate steps |

**Step 3: Test with "Why?" Chain**

For key claims, ask "Why?" repeatedly:
- "Users should validate input" → Why?
- "To prevent injection attacks" → Why does that help?
- "Because unvalidated input can execute malicious code"

If any "why" leads to a gap, add explanation.

### Reasoning Chain Checklist

- [ ] Each concept builds on previously established knowledge
- [ ] No logical leaps without explanation
- [ ] Cause-effect relationships are explicit
- [ ] Recommendations have stated rationale
- [ ] Conclusions follow from presented evidence

---

## Assumption Inventory

Explicitly catalog all implicit assumptions to prevent reader confusion.

### Purpose

Documentation often assumes knowledge that readers may not have. An assumption inventory makes these explicit so they can be addressed or documented as prerequisites.

### Categories of Assumptions

| Category | Examples | Risk if Wrong |
|----------|----------|---------------|
| **Technical** | "Has Node.js installed", "Knows what an API is" | Steps fail silently |
| **Conceptual** | "Understands REST principles", "Familiar with async/await" | Misinterprets guidance |
| **Environmental** | "Has admin access", "Using macOS" | Instructions don't apply |
| **Experiential** | "Has deployed before", "Has seen error X" | Lacks context for decisions |

### Inventory Process

**Step 1: Read as Adversarial Novice**

Read each section asking: "What would someone need to know to follow this?"

**Step 2: Catalog Each Assumption**

For each assumption found:
```
Assumption: [What is assumed]
Location: [Section where it appears]
Criticality: [HIGH: blocks progress / MED: causes confusion / LOW: minor inconvenience]
Resolution: [Explain | Link | Add prerequisite | Accept and document]
```

**Step 3: Resolve High-Criticality Assumptions**

- If learnable in <2 sentences: explain inline
- If requires more context: link to explanation
- If fundamental: add to prerequisites section

### Assumption Inventory Checklist

- [ ] All technical prerequisites documented
- [ ] Jargon either explained or linked
- [ ] Environmental requirements stated
- [ ] No "magic" steps (unexplained actions)
- [ ] Prior experience requirements explicit

---

## Confidence Calibration

Calibrate certainty levels to avoid overstating or understating claims.

### Purpose

Documentation should accurately represent the certainty of its claims. Overconfident statements mislead; underconfident statements confuse. Proper calibration builds trust.

### Confidence Levels

| Level | Language | Use When |
|-------|----------|----------|
| **Certain** | "X does Y", "Always use Z" | Documented behavior, verified facts |
| **High confidence** | "X typically does Y", "In most cases" | Common behavior with known exceptions |
| **Moderate** | "X may do Y", "Consider using Z" | Multiple valid approaches, depends on context |
| **Low/Speculative** | "X might help", "This could indicate" | Unverified, edge cases, uncertain causation |

### Calibration Process

**Step 1: Flag Certainty Claims**

Identify statements that assert facts or make recommendations:
- "This will work" vs "This should work"
- "Use X" vs "Consider X"
- "X causes Y" vs "X may cause Y"

**Step 2: Verify Calibration**

For each flagged statement:
- Is the certainty level appropriate for the evidence?
- Would an expert agree with this confidence level?
- Are exceptions acknowledged when they exist?

**Step 3: Adjust Language**

| Over-confident | Calibrated |
|----------------|------------|
| "This always works" | "This works in standard configurations" |
| "Never use X" | "Avoid X unless [specific case]" |
| "X is the best approach" | "X is often effective for [use case]" |

| Under-confident | Calibrated |
|-----------------|------------|
| "You might want to maybe consider..." | "Consider..." |
| "This could possibly help" | "This helps when [condition]" |

### Confidence Calibration Checklist

- [ ] Certainty language matches evidence strength
- [ ] Known exceptions are acknowledged
- [ ] Recommendations include context for when they apply
- [ ] No false precision (e.g., "87% of users" without data)
- [ ] Uncertainty is explicit, not hidden

---

## MECE Verification Protocol

MECE (Mutually Exclusive, Collectively Exhaustive) ensures documentation is organized without gaps or overlaps.

### Mutually Exclusive Check

No two sections should cover the same content.

**Process:**
1. List all sections/topics covered
2. For each pair of sections, verify no overlap
3. If overlap found, either merge or clearly delineate boundaries

**Overlap Detection:**

| Symptom | Indicates | Resolution |
|---------|-----------|------------|
| Same concept explained twice | Content overlap | Merge into one location, link |
| Same example in multiple places | Example overlap | Single location, cross-reference |
| "See also [section]" that covers same thing | Section overlap | Consolidate |
| Reader could learn X from section A or B | Ambiguous placement | Choose one, reference from other |

**Verification Questions:**
- [ ] Does each section have a unique, non-overlapping purpose?
- [ ] Could any two sections be merged without loss?
- [ ] Is the same information repeated (without intentional reinforcement)?
- [ ] Are boundaries between sections clear?

### Collectively Exhaustive Check

Together, all sections should cover the complete scope.

**Process:**
1. Define the complete scope (what should be covered)
2. List all sections that exist
3. Map sections to scope
4. Identify uncovered areas (gaps)

**Gap Detection by Document Type:**

| Type | Exhaustive Means | Gap Example |
|------|------------------|-------------|
| Tutorial | All steps needed to reach outcome | Missing step causes failure |
| How-To | All paths to accomplish goal | Alternative method not covered |
| Explanation | All perspectives for understanding | Missing "why" or connection |
| Reference | All items in domain | Undocumented parameter |

**Verification Questions:**
- [ ] Have we defined what "complete" means for this document?
- [ ] Can a reader achieve the goal with only this document?
- [ ] Are any obvious questions left unanswered?
- [ ] Would an expert find anything missing?

### MECE Application by Document Type

**Tutorial MECE:**
- ME: Each step teaches one thing
- CE: All steps lead to promised outcome

**How-To MECE:**
- ME: Each step is one action
- CE: All actions needed to complete task

**Explanation MECE:**
- ME: Each section covers distinct aspect
- CE: Understanding is complete after reading all

**Reference MECE:**
- ME: Each entry documents one item
- CE: All items in domain are documented

---

## Orphan Concept Detection

An orphan concept is mentioned but never explained, leaving readers stranded.

### What Makes a Concept Orphaned

| Status | Description | Action Needed |
|--------|-------------|---------------|
| Introduced and explained | Term defined when first used | None |
| Assumed known | Common term for audience level | None |
| Mentioned, not explained | Term used without definition | Fix |
| Referenced, link broken | Points to explanation that doesn't exist | Fix link or add explanation |

### Detection Process

**Step 1: Extract All Technical Terms**

Read through and list every:
- Technical term
- Acronym or abbreviation
- Product/feature name
- Concept name

**Step 2: Check Each Term**

For each term, verify one of:
- [ ] Defined on first use in this document
- [ ] Linked to definition elsewhere
- [ ] Legitimately assumed for audience level

**Step 3: Fix Orphans**

For orphaned concepts:

| Option | When to Use |
|--------|-------------|
| Add definition | Core concept for this document |
| Add link | Explained elsewhere in docs |
| Remove mention | Not actually needed |
| Add prerequisite | Reader should learn first |

### Common Orphan Patterns

| Pattern | Example | Fix |
|---------|---------|-----|
| Jargon assumed | "Configure the CDN" | Define CDN or link |
| Acronym undefined | "Update the CORS settings" | Expand on first use |
| Implicit prerequisite | "Add the hook to your component" (assumes React knowledge) | Add to prerequisites or explain |
| Forward reference | "We'll use this later in the auth flow" | Ensure "auth flow" is covered later |
| Dead-end reference | "See the migration guide" (doesn't exist) | Create it or remove reference |

---

## Promise Verification

Ensures everything promised is delivered.

### Explicit Promises

Check every commitment made:

| Promise Type | Example | Verify |
|--------------|---------|--------|
| Title promises | "How to Configure Auth" | Auth configuration is covered |
| Intro promises | "You'll learn X, Y, and Z" | X, Y, and Z are all taught |
| Section promises | "In this section, we'll..." | Section delivers |
| Example promises | "Let's look at an example" | Example follows |

### Implicit Promises

Readers expect certain things based on document type:

| Type | Implicit Promise | Verify |
|------|-----------------|--------|
| Tutorial | Following steps leads to success | Success is achievable |
| How-To | Task will be completed | Task completable with these steps |
| Explanation | Understanding will be gained | Reader will understand |
| Reference | Information is accurate | All info verified |

### Promise Verification Checklist

- [ ] Title accurately describes content
- [ ] All "What You'll Learn" items are taught
- [ ] All sections promised in intro exist
- [ ] All examples promised are provided
- [ ] Outcome stated in introduction is achievable

---

## Final Readability Pass

Last check before publication, focused on reader experience.

### Read-Aloud Test

Read sections aloud. Mark any place where:
- [ ] You stumble (sentence too long or complex)
- [ ] You lose track (too many clauses)
- [ ] You'd need to re-read (confusing structure)

**Common fixes:**
- Split long sentences
- Replace passive voice
- Remove unnecessary words
- Add transitional phrases

### Heading Scan Test

Read only the headings, in order:
- [ ] Does the structure make sense from headings alone?
- [ ] Could someone navigate using headings only?
- [ ] Are heading levels consistent and logical?
- [ ] Do headings use parallel structure?

### "Can I Find X?" Test

Pick 3-5 specific pieces of information. For each:
- [ ] Can you find it in under 10 seconds using only structure?
- [ ] Is it where you expected?
- [ ] Is the answer clear once found?

### Paragraph Length Audit

- [ ] No paragraph exceeds 5 sentences
- [ ] Average paragraph is 2-3 sentences
- [ ] No single-sentence paragraphs (unless intentional emphasis)

### White Space Check

- [ ] Adequate spacing between sections
- [ ] Code blocks have breathing room
- [ ] Lists aren't cramped
- [ ] Page doesn't feel "wall of text"

---

## Self-Audit Checklist Summary

### Before Declaring "Done"

**MECE Verification:**
- [ ] Mutually Exclusive: No overlapping content
- [ ] Collectively Exhaustive: No gaps in coverage

**Orphan Detection:**
- [ ] All technical terms defined or linked
- [ ] No broken references
- [ ] No assumed knowledge beyond prerequisites

**Promise Verification:**
- [ ] Title delivers what it promises
- [ ] All stated learning outcomes achievable
- [ ] All referenced content exists

**Final Readability:**
- [ ] Read-aloud test passed
- [ ] Heading scan makes sense
- [ ] Information is findable
- [ ] Formatting is consistent

---

## When to Run Each Audit

| Audit | When | Time Investment |
|-------|------|-----------------|
| MECE Verification | After structural changes | 10-15 min |
| Orphan Detection | After content is "complete" | 5-10 min |
| Promise Verification | Before final review | 5 min |
| Final Readability | Last step before publish | 10-15 min |
| Full Self-Audit | New documents, major revisions | 30-45 min |
