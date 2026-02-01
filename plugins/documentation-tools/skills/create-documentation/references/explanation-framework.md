# Explanation Framework

Explanations are **understanding-oriented** documentation that helps readers comprehend how and why something works. The goal is to build mental models, not accomplish tasks.

---

## Explanation Philosophy

### Core Principles

1. **Understanding over action** — "Why" and "how it works" not "how to do it"
2. **Multiple perspectives** — Different mental models serve different readers
3. **Connections matter** — Link to related concepts, history, alternatives
4. **Depth available** — Allow exploration without forcing it
5. **No right answer** — Explanations can present tradeoffs without recommending

### Explanation vs. Other Types

| Explanation | Tutorial | How-To | Reference |
|-------------|----------|--------|-----------|
| Understand X | Learn to do X | Do X | Look up X |
| Theory-oriented | Learning-oriented | Task-oriented | Information-oriented |
| "Why does...?" | "Teach me..." | "How do I...?" | "What is the syntax for...?" |

---

## Explanation Structure

### Flexible Format

Explanations are less rigid than other types. Choose structure based on topic:

#### Concept Explanation
```markdown
# Understanding [Concept]

## Why This Matters
[Context and motivation]

## What [Concept] Is
[Core definition]

## How [Concept] Works
[Mechanism or process]

## [Concept] in Practice
[Application to real situations]

## Related Concepts
[Connections to other ideas]
```

#### Comparison Explanation
```markdown
# [X] vs [Y]: Understanding the Difference

## Overview
[What we're comparing and why]

## [X] Explained
[How X works]

## [Y] Explained
[How Y works]

## Key Differences
[Direct comparison]

## When to Use Each
[Decision guidance]
```

#### Process Explanation
```markdown
# How [Process] Works

## Overview
[What the process accomplishes]

## Step-by-Step Breakdown
### Phase 1: [Name]
[What happens and why]

### Phase 2: [Name]
[What happens and why]

## Why It Works This Way
[Design rationale]

## Common Variations
[Different implementations]
```

---

## Writing Explanations

### Opening Section

Start by establishing:
1. **What** this concept is (brief)
2. **Why** the reader should care
3. **Where** this fits in the bigger picture

Example:
```markdown
# Understanding Database Indexes

Database indexes are data structures that speed up data retrieval.
Without them, queries must scan entire tables — fine for hundreds
of rows, unacceptable for millions.

If you've ever wondered why some queries are fast and others timeout,
or why adding an index "magically" fixed performance, this explanation
will give you the mental model to understand and predict query behavior.
```

### The "Why" Emphasis

Explanations answer "why" questions that tutorials and how-tos skip:

- Why does this approach exist?
- Why is this designed this way?
- Why would I choose this over alternatives?
- Why do problems occur here?

**Technique:** For every statement of "what," ask yourself if adding "because" would help the reader.

```markdown
// Good - includes why
Indexes use B-tree structures because they allow O(log n)
lookups while supporting range queries efficiently.

// Less helpful - what without why
Indexes use B-tree structures.
```

### Multiple Perspectives

Different mental models help different readers. Offer multiple angles:

```markdown
## Understanding Middleware

### The Pipeline Mental Model
Think of middleware as a series of pipes that requests flow through.
Each pipe can inspect, modify, or reject the flow...

### The Wrapper Mental Model
Alternatively, think of middleware as layers wrapping your core logic.
The outer layers handle cross-cutting concerns...

### The Event Handler Mental Model
You can also view middleware as event handlers responding to the
request lifecycle...
```

---

## Explanation Techniques

### Analogies and Metaphors

Good analogies:
- Connect unfamiliar to familiar
- Hold up under examination
- Don't require technical knowledge

Example:
```markdown
Database transactions are like editing a document in Google Docs
with "suggestion mode" on. You make changes, but they don't become
permanent until someone approves them. If you change your mind,
you can reject all suggestions and the document stays unchanged.
```

**Warning:** Explicitly note where analogies break down:
```markdown
Unlike Google Docs suggestions, database transactions don't show
intermediate states to other users — the changes are invisible
until committed.
```

### Compare and Contrast

Comparisons clarify boundaries:

```markdown
| Authentication | Authorization |
|----------------|---------------|
| "Who are you?" | "What can you do?" |
| Happens first | Happens after authentication |
| One-time per session | Checked on each request |
| Example: Login form | Example: Admin-only page |
```

### Historical Context

Why things exist often explains how they work:

```markdown
## Why REST Uses HTTP Verbs

Early web services treated HTTP as a simple transport — every
request was a POST to a single endpoint. REST emerged as a reaction,
arguing that HTTP already had semantics for different operations.

This history explains why REST feels natural on the web but awkward
elsewhere — it was designed specifically for HTTP's features.
```

### Visual Representations

Use diagrams when:
- Relationships between components matter
- Sequence or flow is important
- Spatial arrangement has meaning

```markdown
## Request Lifecycle

```
Client → DNS → Load Balancer → Server → Application → Database
                                ↑                          |
                                └──────────────────────────┘
```
```

---

## Cognitive Load for Explanations

### Target Profile

| Load Type | Level | Strategy |
|-----------|-------|----------|
| Intrinsic | Embraced | Complex topics can handle complexity |
| Extraneous | Minimized | Clear structure, good organization |
| Germane | Maximized | Connections, perspectives, depth |

### Managing Complexity

Explanations often cover complex topics. Manage this by:

1. **Progressive depth** — Start simple, add nuance
2. **Clear sections** — Allow readers to skip to what interests them
3. **Explicit scope** — State what you will and won't cover
4. **Waypoints** — Summarize periodically

Example of progressive depth:
```markdown
## How Garbage Collection Works

### The Simple Model
The garbage collector finds objects no longer referenced and frees
their memory.

### The Realistic Model
Actually, it's more nuanced. Modern collectors use generational
collection, dividing memory into young and old generations...

### Implementation Details
V8's Orinoco collector specifically uses concurrent marking with...
```

---

## Related Concepts Section

Always include connections to:
- Prerequisites (what to learn first)
- Related ideas (what else to explore)
- Applications (where this knowledge applies)

Example:
```markdown
## Related Concepts

- **[Database normalization](./normalization.md)** — Understanding
  indexes requires understanding why tables are structured as they are
- **[Query planning](./query-plans.md)** — See how the database
  decides whether to use your indexes
- **[Performance profiling](./profiling.md)** — Apply index knowledge
  to real-world optimization
```

---

## Explanation Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|--------------|--------------|-----|
| Procedural focus | That's a how-to | Focus on understanding |
| Oversimplification | Unsatisfying, misleading | Embrace complexity |
| No practical grounding | Abstract without application | Include real examples |
| Missing the "why" | Leaves curiosity unfulfilled | Explain reasoning |
| No connections | Knowledge in isolation | Link to related concepts |
| Dismissing alternatives | "This is the only way" | Acknowledge tradeoffs |
| Too much jargon | Alienates readers | Define terms, build vocabulary |

---

## Explanation Checklist

Before publishing:

- [ ] Opens with why reader should care
- [ ] Core concept clearly defined
- [ ] "Why" questions answered
- [ ] Multiple perspectives offered (if complex topic)
- [ ] Analogies check out (and limitations noted)
- [ ] Connected to related concepts
- [ ] Practical implications included
- [ ] Appropriate depth for audience
- [ ] Clear section structure for navigation
- [ ] No procedural instructions (link to how-tos instead)
