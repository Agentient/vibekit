---
name: optimize-prompt
description: >
  Transform prompts into optimized, production-ready versions.
  PROACTIVELY activate for: (1) prompt engineering, (2) prompt improvement,
  (3) making prompts more effective, (4) prompt debugging.
  Triggers: "optimize prompt", "improve prompt", "better prompt", "fix prompt",
  "prompt engineering", "refine prompt", "enhance prompt"
argument-hint: [prompt text or file path]
disable-model-invocation: true
---

# Optimize Prompt

Transform prompts into production-ready versions using prompt engineering best practices.

## When to Use

Use this skill when you need to:
- Improve an existing prompt's effectiveness
- Adapt a prompt for Claude's strengths
- Add structure and clarity to vague prompts
- Debug prompts that aren't working as expected

## Workflow

Invoke the `improve-prompt` skill for analysis and optimization.

### Input

$ARGUMENTS

### Analysis Framework

#### Step 1: Analyze Current Prompt

Evaluate for:
| Dimension | Check |
|-----------|-------|
| Clarity | Is the task unambiguous? |
| Completeness | Is all necessary context provided? |
| Structure | Is it well-organized? |
| Constraints | Are boundaries defined? |
| Examples | Are few-shot examples provided if needed? |
| Output format | Is expected output specified? |

#### Step 2: Identify Issues

Common problems to address:
- Vague instructions → Make specific
- Missing context → Add relevant background
- No output format → Specify structure
- No examples → Add few-shot demonstrations
- No constraints → Add guardrails
- Too long → Consolidate and prioritize

#### Step 3: Apply Claude-Specific Best Practices

**Structure:**
- Use XML tags for clear sections (`<context>`, `<task>`, `<output>`)
- Put important instructions at start AND end (primacy/recency effect)
- Use numbered steps for sequences

**Framing:**
- Use positive framing ("do X" not "don't do Y")
- Be specific about the persona/role if helpful
- Request step-by-step reasoning for complex tasks

**Output Control:**
- Specify exact output format with examples
- Use structured formats (JSON, XML, Markdown) for parsing
- Include edge case handling instructions

#### Step 4: Generate Optimized Prompt

Produce the improved version with:
- Clear structure using XML tags
- Explicit instructions
- Defined output format
- Examples if beneficial

## Output Format

```markdown
## Prompt Analysis

**Original prompt issues:**
1. [Issue 1 with specific example]
2. [Issue 2 with specific example]

**Improvements applied:**
1. [Improvement 1 and rationale]
2. [Improvement 2 and rationale]

---

## Optimized Prompt

[The improved prompt, ready to copy]

---

## Usage Notes

- **Best for**: [model/use case recommendations]
- **Expected output**: [description of what the prompt produces]
- **Variations**: [suggested modifications for different contexts]
```

## Quality Gates

- [ ] All ambiguities in original prompt resolved
- [ ] Output format explicitly specified
- [ ] Appropriate length (not bloated with unnecessary content)
- [ ] Edge cases considered and handled
- [ ] Claude-specific techniques applied where beneficial
- [ ] Prompt is self-contained (doesn't require external context)
