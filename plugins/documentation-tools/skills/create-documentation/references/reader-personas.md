# Reader Personas Reference

Three archetypal reader personas that inform all documentation decisions. Every document should be optimized for its primary persona while remaining accessible to others.

## Persona Selection Guide

| Signal | Likely Persona |
|--------|----------------|
| "I'm new to..." / "First time..." | Anxious Novice |
| "How do I quickly..." / "Just need to..." | Developer |
| "What's the business impact..." / "Give me the summary..." | Scanning Executive |
| Expertise: novice | Anxious Novice |
| Expertise: intermediate + task urgency | Developer |
| Expertise: any + strategic decisions | Scanning Executive |

---

## The Anxious Novice

### Profile
- **Expertise:** New to the topic, tool, or domain
- **Emotional state:** Uncertain, worried about breaking things, afraid of looking foolish
- **Goal:** Successfully complete task without disaster
- **Reading behavior:** Reads carefully, follows every step, seeks reassurance

### Core Needs
- Explicit, step-by-step guidance with no assumed knowledge
- Clear "you're in the right place" signals at the start
- Visible success indicators after each action
- Recovery paths when things go wrong
- Permission to proceed ("it's safe to...")

### Documentation Strategies
1. **State prerequisites explicitly** — Never assume they know what's needed
2. **Show expected output** — "You should see..." after every significant step
3. **Provide escape hatches** — "If you see X instead, try Y"
4. **Use reassuring language** — "Don't worry if..." / "This is normal..."
5. **Avoid jargon** — Define terms on first use, even "obvious" ones

### Voice Guidelines
- Reassuring but not condescending
- Patient, willing to over-explain
- Explicit about what will happen
- Acknowledges potential confusion

### Anti-Patterns to Avoid
| Anti-Pattern | Why It Fails | Instead |
|--------------|--------------|---------|
| "Simply do X" | Implies it should be easy; creates shame | "Do X" (neutral) |
| "Obviously..." | Makes them feel stupid if not obvious | Remove entirely |
| "As you know..." | They don't know | Explain it |
| Skipping "trivial" steps | Nothing is trivial to novices | Include all steps |
| Dense paragraphs | Overwhelming | Short paragraphs, lists |

### Example Voice
> "Before we begin, let's make sure you have everything you need. Don't worry if you're missing something — we'll tell you exactly how to get it."

---

## The Developer

### Profile
- **Expertise:** Competent in the domain, knows fundamentals
- **Emotional state:** Focused, possibly time-pressured, task-driven
- **Goal:** Accomplish specific task efficiently
- **Reading behavior:** **Scan pattern** — eyes jump to code blocks, headings, and bold text; reads selectively

### Core Needs
- Goal stated immediately in title/first line
- Prerequisites listed upfront (not buried)
- Steps that can be copy-pasted
- No explanations unless essential
- Quick navigation to different scenarios

### Scan Pattern Optimization

Developers don't read linearly. Optimize for their scan pattern:

```
SCAN ORDER (typical Developer):
1. Title → Does this solve my problem?
2. Code blocks → Can I copy-paste this?
3. Headings → Where's the part I need?
4. Bold text → What's important?
5. Prerequisites → What do I need first?
6. Prose → Only if stuck
```

**Design for scan success:**
- Make code blocks self-contained
- Front-load key info in each section
- Use bold for critical terms
- Headings should be scannable decisions points

### Documentation Strategies
1. **Put goal in title** — "How to X" not "About X"
2. **Prerequisites as a bullet list** — Scannable, at the top
3. **Numbered steps with imperative verbs** — "Run...", "Add...", "Configure..."
4. **Code blocks are copy-paste ready** — Include all necessary context
5. **Troubleshooting at the end** — Not interrupting the flow

### Voice Guidelines
- Direct and efficient
- Respects their time and competence
- No unnecessary pleasantries
- Assumes domain knowledge, not tool knowledge

### Anti-Patterns to Avoid
| Anti-Pattern | Why It Fails | Instead |
|--------------|--------------|---------|
| Long introductions | They'll skip it anyway | One sentence max |
| "First, let's understand..." | They don't want to understand, they want to do | Skip theory, link to it |
| Inline explanations | Interrupts the flow | Footnotes or separate section |
| Non-actionable headings | Can't scan for what they need | Use verb phrases |
| Missing prerequisites | Forces backtracking | Prerequisites section |

### Example Voice
> "Run `npm install`. Add the config to `.env`. Restart the server."

---

## The Scanning Executive

### Profile
- **Expertise:** May be technical or non-technical; has decision-making authority
- **Emotional state:** Time-constrained, needs to form opinions quickly
- **Goal:** Understand implications, risks, and tradeoffs for decision-making
- **Reading behavior:** Asks key questions, seeks executive summary, drills into specifics only when needed

### Core Needs
- Clear answers to "What? So what? Now what?"
- Impact and implications upfront
- Risk and tradeoff analysis
- Confidence levels on recommendations
- Minimal jargon or jargon explained

### Key Questions Framework

Scanning Executives approach documentation with specific questions:

```
KEY QUESTIONS (in order):
1. What is this? (one sentence)
2. Why does it matter to me/us?
3. What are the options?
4. What are the tradeoffs?
5. What's recommended and why?
6. What are the risks?
7. What's the timeline/cost?
```

**Design for question-answering:**
- Ensure each key question is answerable from your doc
- Put answers where an executive would scan for them
- Don't bury critical information in prose

### Documentation Strategies
1. **Lead with impact** — "This reduces deployment time by 40%" not "This is a CI/CD tool"
2. **Use comparison tables** — Executives love side-by-side tradeoff analysis
3. **Quantify when possible** — Numbers are more scannable than prose
4. **Provide recommendations** — Don't make them decide without guidance
5. **Acknowledge uncertainty** — Calibrated confidence builds trust

### Voice Guidelines
- Confident but not arrogant
- Acknowledges complexity without drowning in it
- Provides clear recommendations
- Respects their need for both summary and depth

### Anti-Patterns to Avoid
| Anti-Pattern | Why It Fails | Instead |
|--------------|--------------|---------|
| Starting with implementation details | Wrong level of abstraction | Lead with impact |
| No recommendation | Forces decision without context | Recommend with rationale |
| Hidden risks | Erodes trust when discovered | Surface risks proactively |
| Unexplained jargon | Alienates or confuses | Define or avoid |
| "It depends" without elaboration | Not actionable | Explain what it depends on |

### Example Voice
> "**Recommendation:** Adopt Option B. It costs 20% more but reduces integration risk significantly. Option A is viable if budget is the primary constraint, but expect a 2-week delay for workarounds."

---

## Persona Mapping by Document Type

| Doc Type | Primary Persona | Secondary Persona |
|----------|-----------------|-------------------|
| Tutorial | Anxious Novice | Developer |
| How-To | Developer | Anxious Novice |
| Explanation | Scanning Executive | Developer |
| Reference | Developer | Scanning Executive |

---

## Persona Detection Heuristics

When the persona isn't explicitly stated, infer from:

1. **Explicit signals in request:**
   - "I'm new to..." → Anxious Novice
   - "Quickly..." / "Just need to..." / "How do I..." → Developer
   - "What's the impact..." / "Should we..." / "Compare options..." → Scanning Executive

2. **Stated expertise level:**
   - Novice → Default to Anxious Novice
   - Intermediate → Developer (task-focused) or Anxious Novice (learning)
   - Expert → Developer or Scanning Executive

3. **Document type:**
   - Tutorial → Anxious Novice
   - How-To → Developer
   - Explanation → Scanning Executive (for decisions) or Anxious Novice (for learning)
   - Reference → Developer

4. **Context indicators:**
   - Time pressure + implementation → Developer
   - Decision-making context → Scanning Executive
   - Learning context → Anxious Novice

**Default:** When uncertain, design for Anxious Novice — the others can skim, but novices can't infer missing information.
