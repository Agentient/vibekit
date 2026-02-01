# Cognitive Load Theory for Documentation

Cognitive load theory explains how working memory limitations affect learning. Documentation that ignores cognitive load overwhelms readers; documentation that manages it enables understanding.

## Working Memory Fundamentals

Human working memory can hold approximately 7 (+/- 2) items simultaneously. New information must be processed through working memory before it can be stored in long-term memory. When working memory is overloaded, learning stops.

**Key insight:** Documentation is not just about presenting information — it's about managing the reader's cognitive resources so they can actually absorb what's presented.

---

## Three Types of Cognitive Load

### 1. Intrinsic Load

**Definition:** The inherent complexity of the material being learned. Determined by the content itself and the reader's prior knowledge.

**Characteristics:**
- Cannot be eliminated, only managed
- Higher for complex topics with many interacting elements
- Lower for readers with relevant prior knowledge (chunking)
- Reducible through sequencing and prerequisite building

**Documentation Strategies:**

| Strategy | Implementation | Example |
|----------|----------------|---------|
| Sequencing | Present simpler concepts before complex ones | Teach variables before functions |
| Chunking | Group related items into meaningful units | "The three config options for auth..." |
| Scaffolding | Provide temporary supports that can be removed | Annotated examples before bare code |
| Prerequisite mapping | Explicit "you should know X before Y" | Prerequisites section |

**Assessment Questions:**
- How many new concepts does this introduce simultaneously?
- What prior knowledge does this assume?
- Can complex concepts be broken into simpler sub-concepts?
- Is there a natural dependency sequence?

---

### 2. Extraneous Load

**Definition:** Unnecessary cognitive effort caused by poor presentation, not the content itself. This is waste — it consumes mental resources without contributing to learning.

**Common Sources in Documentation:**

| Source | Description | Fix |
|--------|-------------|-----|
| Poor organization | Reader must mentally reorganize | Logical structure, clear headings |
| Inconsistent terminology | Reader tracks multiple terms for same concept | Glossary, consistent usage |
| Missing context | Reader must infer or look up | Explicit context statements |
| Visual noise | Competing attention demands | Clean layout, purposeful formatting |
| Irrelevant detail | Non-essential information mixed with essential | Separate or remove |
| Split attention | Information needed together is physically separate | Co-locate related info |
| Redundant explanation | Same thing explained multiple ways without purpose | Single clear explanation |

**Elimination Techniques:**

1. **Ruthless editing** — Remove anything that doesn't directly serve understanding
2. **Consistent terminology** — One term per concept, defined on first use
3. **Integrated formats** — Labels on diagrams, not in separate legends
4. **Purposeful formatting** — Every visual distinction has meaning
5. **Signposting** — Tell readers where they are and where they're going

**Assessment Questions:**
- Is any information here that doesn't serve the reader's goal?
- Could the same information be presented more simply?
- Is the reader forced to hold things in memory that could be visible?
- Are related items physically close together?

---

### 3. Germane Load

**Definition:** Cognitive effort that directly contributes to learning — the "good" load. This is the work of building mental schemas and connecting new knowledge to existing knowledge.

**Characteristics:**
- Desirable and should be maximized
- Increases retention and transfer
- Requires intrinsic and extraneous load to be manageable
- Active engagement, not passive reading

**Documentation Strategies:**

| Strategy | Implementation | Example |
|----------|----------------|---------|
| Worked examples | Show complete solution with reasoning | Step-by-step code walkthrough |
| Example fading | Gradually remove scaffolding | Full example → partial → exercise |
| Self-explanation prompts | Ask reader to explain why | "Why do we need X here?" |
| Retrieval practice | Require recall before providing answer | "Before reading on, predict what happens if..." |
| Elaboration | Connect to other knowledge | "This is similar to X, which you may know from..." |
| Variation | Show same concept in different contexts | Multiple examples, different domains |

**Assessment Questions:**
- Does this documentation ask the reader to think, or just read?
- Are there opportunities for the reader to predict, then verify?
- Does this connect to knowledge the reader already has?
- Will the reader be able to apply this to new situations?

---

## Load Management by Document Type

### Tutorial (Learning-Oriented)
| Load Type | Target | Strategy |
|-----------|--------|----------|
| Intrinsic | Managed | Sequence carefully, introduce one concept at a time |
| Extraneous | Minimal | Remove all non-essential information |
| Germane | Maximized | Worked examples, verification steps, reflection points |

**Tutorial-specific guidance:**
- Each step should introduce at most one new concept
- Provide verification after every action ("You should see...")
- Include "what we learned" summaries
- Worked examples should show the thinking, not just the code

### How-To (Task-Oriented)
| Load Type | Target | Strategy |
|-----------|--------|----------|
| Intrinsic | Minimized | Assume competence, link to explanations |
| Extraneous | Eliminated | Only what's needed to complete task |
| Germane | Optional | For those who want it, via links |

**How-to-specific guidance:**
- Assume domain knowledge; don't explain concepts
- Copy-paste ready (no mental translation needed)
- No digressions — every sentence serves the goal
- Troubleshooting separate from main flow

### Explanation (Understanding-Oriented)
| Load Type | Target | Strategy |
|-----------|--------|----------|
| Intrinsic | Embraced | Complex topics can handle higher load |
| Extraneous | Minimized | Clear structure, logical flow |
| Germane | Maximized | Connections, multiple perspectives, depth |

**Explanation-specific guidance:**
- Build mental models, not just facts
- Show how concepts relate to each other
- Multiple perspectives increase understanding
- "Why" is more important than "what"

### Reference (Information-Oriented)
| Load Type | Target | Strategy |
|-----------|--------|----------|
| Intrinsic | Minimal per entry | Each entry self-contained |
| Extraneous | Near-zero | Consistent format, quick retrieval |
| Germane | N/A | Reference is for lookup, not learning |

**Reference-specific guidance:**
- Optimize for scanning and retrieval
- Consistent structure reduces load for repeated lookups
- Complete but not pedagogical
- Cross-references for related entries

---

## Cognitive Load Estimation Checklist

Before writing, assess:

**Intrinsic Load Assessment:**
- [ ] How many new concepts are introduced?
- [ ] How interdependent are these concepts?
- [ ] What prior knowledge is assumed?
- [ ] Can the sequence be simplified?

**Extraneous Load Audit:**
- [ ] Is any content unnecessary for the goal?
- [ ] Is terminology consistent?
- [ ] Are related items co-located?
- [ ] Is formatting purposeful (not decorative)?
- [ ] Is the structure logical and scannable?

**Germane Load Opportunities:**
- [ ] Are there worked examples?
- [ ] Does the reader predict or engage?
- [ ] Are connections to prior knowledge explicit?
- [ ] Will the reader be able to transfer this knowledge?

---

## Cognitive Load Red Flags

When reviewing documentation, watch for:

| Red Flag | Indicates | Fix |
|----------|-----------|-----|
| Long paragraphs (>5 sentences) | High extraneous | Break up, use lists |
| Multiple concepts per sentence | High intrinsic | One concept per sentence |
| "As we discussed earlier..." | Split attention | Repeat or link |
| Undefined jargon | High extraneous | Define on first use |
| Wall of code | High intrinsic | Annotate, break into chunks |
| "It's complicated, but..." | Unmanaged intrinsic | Better sequencing |
| Passive voice throughout | Unnecessary processing | Active voice |
| No examples | Low germane | Add worked examples |
