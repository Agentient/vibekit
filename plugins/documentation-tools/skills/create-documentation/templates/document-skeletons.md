# Document Skeletons

Ready-to-use templates for all four Diátaxis document types. Copy the appropriate skeleton and customize for your content.

---

## Skeleton Selection Guide

| Need | Document Type | Skeleton |
|------|--------------|----------|
| Teach someone how to do something new | Tutorial | [Tutorial Skeleton](#tutorial-skeleton) |
| Help someone accomplish a specific task | How-To | [How-To Skeleton](#how-to-skeleton) |
| Help someone understand a concept | Explanation | [Explanation Skeleton](#explanation-skeleton) |
| Provide lookup information | Reference | [Reference Skeleton](#reference-skeleton) |

### Quick Decision Tree

```
Is the reader trying to LEARN or DO something?
├── LEARN → Is it practical (doing) or theoretical (understanding)?
│   ├── Practical → Tutorial
│   └── Theoretical → Explanation
└── DO → Is it a specific task or looking up info?
    ├── Specific task → How-To
    └── Looking up info → Reference
```

---

## Tutorial Skeleton

**Copy this for:** Learning-oriented documentation where the reader acquires new skills through hands-on steps.

```markdown
# Tutorial: [Verb] [Outcome]

Learn to [what they'll accomplish] by [brief description of approach].

## What You'll Learn

- [Skill 1]
- [Skill 2]
- [Skill 3]

## Prerequisites

- [Software/tool requirement]
- [Knowledge requirement]
- [Account/access requirement]

## Time Required

[X-Y] minutes

---

## Step 1: [First Action]

[1-2 sentences: what we're doing and why]

**Do this:**
```language
[code or action]
```

[Optional: Brief explanation of key elements]

**Verify:** [How to confirm success]

---

## Step 2: [Second Action]

[1-2 sentences: what we're doing and why]

**Do this:**
```language
[code or action]
```

**Verify:** [How to confirm success]

---

## Step 3: [Third Action]

[1-2 sentences: what we're doing and why]

**Do this:**
```language
[code or action]
```

**Verify:** [How to confirm success]

---

[Continue with additional steps as needed]

---

## What You've Learned

In this tutorial, you:

- [Skill/concept 1 they now have]
- [Skill/concept 2 they now have]
- [Skill/concept 3 they now have]

## Try It Yourself

Now apply what you learned to a slightly different scenario:

**Challenge:** [Variation on the tutorial task]

<details>
<summary>Hints</summary>

- [Hint 1]
- [Hint 2]

</details>

<details>
<summary>Solution</summary>

```language
[Solution code or steps]
```

</details>

## Next Steps

Now that you can [core skill], you might want to:

- [Related tutorial]
- [How-to for common task]
- [Explanation for deeper understanding]

## Troubleshooting

### [Common Problem 1]
[Solution]

### [Common Problem 2]
[Solution]
```

### Tutorial Customization Notes

- **Always include verification** after every step
- **Add recovery paths** for steps likely to fail
- **Keep steps atomic** — one concept per step
- **Use progressive complexity** — start simple, add nuance

---

## How-To Skeleton

**Copy this for:** Task-oriented documentation where the reader needs to accomplish a specific goal quickly.

```markdown
# How to [Goal]

[One sentence: what this accomplishes]

**Prerequisites:**
- [Requirement 1]
- [Requirement 2]

---

## Steps

1. **[Action verb] [object]**
   ```language
   [code if needed]
   ```
   [Optional: One-line note]

2. **[Action verb] [object]**
   ```language
   [code if needed]
   ```

3. **[Action verb] [object]**
   ```language
   [code if needed]
   ```

[Continue with additional steps]

---

## Result

When complete, you will have:
- [Outcome 1]
- [Outcome 2]

To verify: [How to confirm success]

---

## Troubleshooting

**[Error message or symptom]**
[Solution]

**[Error message or symptom]**
[Solution]

---

## Related

- [Link to related how-to]
- [Link to explanation for more context]
- [Link to reference for options]
```

### How-To Customization Notes

- **Put prerequisites first** — readers need to know before starting
- **Use imperative verbs** — "Run", "Add", "Configure"
- **Code should be copy-paste ready** — include all context
- **Keep explanations minimal** — link to explanations if needed

---

## Explanation Skeleton

**Copy this for:** Understanding-oriented documentation where the reader wants to comprehend how or why something works.

```markdown
# Understanding [Concept]

[One paragraph: What this is and why it matters to the reader]

---

## Why This Matters

[2-3 paragraphs: Context for why the reader should care. Connect to
their likely situation or problems they're trying to solve.]

---

## What [Concept] Is

[Core definition and description. Be clear and precise.]

### Key Characteristics

- **[Characteristic 1]:** [Brief explanation]
- **[Characteristic 2]:** [Brief explanation]
- **[Characteristic 3]:** [Brief explanation]

---

## How [Concept] Works

[Explain the mechanism or process. This is the "how" of the explanation.]

### [Sub-aspect 1]

[Detailed explanation]

### [Sub-aspect 2]

[Detailed explanation]

---

## Different Perspectives

Understanding [Concept] can be approached in multiple ways:

### The [Mental Model 1] Perspective

[Explain concept through this lens]

### The [Mental Model 2] Perspective

[Explain concept through this lens]

---

## Trade-offs

Every approach involves trade-offs. Here's how [Concept] compares:

| Approach | Advantages | Disadvantages | Best When |
|----------|------------|---------------|-----------|
| [Approach 1] | [Pros] | [Cons] | [Use case] |
| [Approach 2] | [Pros] | [Cons] | [Use case] |

**Our recommendation:** [Approach X] for most use cases because [reasoning].

---

## [Concept] in Practice

[How this applies to real situations. Ground the theory in practical examples.]

**Example scenario:**
[Concrete example showing the concept in action]

---

## Common Misconceptions

| Misconception | Reality |
|---------------|---------|
| [Wrong belief 1] | [Correct understanding] |
| [Wrong belief 2] | [Correct understanding] |

---

## Related Concepts

- **[Related concept 1]:** [How it connects]
- **[Related concept 2]:** [How it connects]
- **[Related concept 3]:** [How it connects]

---

## Further Reading

- [Link to deeper explanation]
- [Link to tutorial for hands-on practice]
- [Link to reference for specifics]
```

### Explanation Customization Notes

- **Start with why** — motivation before mechanics
- **Offer multiple perspectives** — different mental models help different readers
- **Include practical grounding** — abstract concepts need concrete examples
- **Link liberally** — explanations connect to other content

---

## Reference Skeleton

**Copy this for:** Information-oriented documentation for looking up specific facts, parameters, or syntax.

```markdown
# [Category] Reference

[One paragraph: What this reference covers and how it's organized]

---

## Overview

| [Column 1] | [Column 2] | [Column 3] |
|------------|------------|------------|
| [Item 1]   | [Value]    | [Notes]    |
| [Item 2]   | [Value]    | [Notes]    |
| [Item 3]   | [Value]    | [Notes]    |

---

## [Entry 1 Name]

**Type:** [category/type]
**Since:** [version, if applicable]

[One-line description of what this does]

### Syntax

```language
[Usage syntax with placeholders]
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `param1`  | string | Yes | — | [Description] |
| `param2`  | number | No | `10` | [Description] |
| `param3`  | boolean | No | `false` | [Description] |

### Returns

[What this returns or produces]

### Example

```language
[Minimal working example]
```

Output:
```
[Expected output]
```

### See Also

- [Related entry 1]
- [Related entry 2]

---

## [Entry 2 Name]

**Type:** [category/type]

[One-line description]

### Syntax

```language
[Usage syntax]
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|

### Returns

[Description]

### Example

```language
[Example]
```

### See Also

- [Related entries]

---

[Continue for each entry]

---

## Index

### By Name
- [Entry 1](#entry-1-name) — [one-line summary]
- [Entry 2](#entry-2-name) — [one-line summary]

### By Category
**[Category A]**
- [Entry 1](#entry-1-name)

**[Category B]**
- [Entry 2](#entry-2-name)
```

### Reference Customization Notes

- **Consistency is paramount** — every entry must use identical structure
- **Keep entries self-contained** — no required reading order
- **Include comprehensive index** — multiple ways to find entries
- **Examples should be minimal** — just enough to demonstrate usage

---

## Skeleton Adaptation Rules

### By Audience

| Persona | Adaptations |
|---------|-------------|
| Anxious Novice | Add more verification steps, recovery paths, reassurance |
| Pragmatic Practitioner | Strip to essentials, ensure copy-paste ready |
| Curious Explorer | Add "why" sections, more connections, depth options |

### By Reading Level

| Level | Adaptations |
|-------|-------------|
| Grade 8 | Shorter sentences, more examples, define all terms |
| Grade 12 | Standard length, some assumed terms, moderate examples |
| Professional | Dense acceptable, jargon OK, minimal examples |

### By Complexity

| Complexity | Adaptations |
|------------|-------------|
| Low | Single skeleton may be enough |
| Medium | Add troubleshooting, multiple examples |
| High | Add "Background" sections, multiple perspectives, extensive See Also |
