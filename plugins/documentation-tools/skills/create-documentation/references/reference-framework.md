# Reference Framework

Reference documentation is **information-oriented** — designed for looking up specific facts, not learning or doing. Readers arrive with a question and need a quick, accurate answer.

---

## Reference Philosophy

### Core Principles

1. **Complete coverage** — Every item in the domain is documented
2. **Consistent structure** — Same format for every entry
3. **Standalone entries** — Each entry self-contained, no reading order
4. **Retrieval optimized** — Fast to find, fast to understand
5. **Not pedagogical** — Teaches nothing, informs everything

### Reference vs. Other Types

| Reference | Explanation | How-To | Tutorial |
|-----------|-------------|--------|----------|
| What are the options for X? | How does X work? | How do I do X? | Teach me X |
| Look up facts | Understand concepts | Complete tasks | Learn skills |
| Any order | Logical flow | Sequential steps | Learning path |

---

## Reference Structure

### Document-Level Organization

```markdown
# [Category] Reference

## Overview
[One paragraph describing this reference domain]

---

## [Entry 1]
[Entry content]

---

## [Entry 2]
[Entry content]

---

## Index
[Alphabetical or categorized list with links]
```

### Entry Structure

Every entry follows the same template:

```markdown
## [Entry Name]

**Type:** [category]
**Since:** [version] (if relevant)

[One-line description]

### Syntax
```
[Usage syntax]
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| param1 | string | Yes | — | Description |
| param2 | number | No | 10 | Description |

### Returns
[What it returns/produces]

### Example
```language
[Minimal working example]
```

### See Also
- [Related entry 1]
- [Related entry 2]
```

---

## Writing Reference Entries

### Description

One line that answers: "What does this do?"

```markdown
// Good - clear, complete
Validates user input against the specified schema and returns errors.

// Bad - vague
Handles validation.

// Bad - too long (that's an explanation)
Validates user input by comparing each field against the constraints
defined in the schema object, checking types, required fields, and
custom validators...
```

### Syntax Blocks

Show the complete signature:

```markdown
### Syntax
```typescript
function validate(input: object, schema: Schema, options?: ValidateOptions): ValidationResult
```
```

For flexible APIs, show variations:
```markdown
### Syntax
```typescript
// Basic usage
validate(input, schema)

// With options
validate(input, schema, { strict: true })
```
```

### Parameter Tables

Include all parameters with:
- **Name** — Exact identifier
- **Type** — Data type
- **Required** — Yes/No
- **Default** — What happens if omitted
- **Description** — What it does (brief)

Example:
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| input | object | Yes | — | Data to validate |
| schema | Schema | Yes | — | Validation rules |
| options | ValidateOptions | No | {} | Configuration options |

### Options Objects

For complex option objects, create sub-tables:

```markdown
### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| strict | boolean | false | Fail on unknown fields |
| abortEarly | boolean | false | Stop on first error |
| allowUnknown | boolean | true | Ignore unknown fields |
```

### Examples

Reference examples should be:
- **Minimal** — Only what's needed to demonstrate
- **Complete** — Actually runnable
- **Realistic** — Real-world-ish values, not "foo"

```markdown
### Example
```javascript
const result = validate(
  { email: 'user@example.com', age: 25 },
  { email: 'email', age: 'number|min:0' }
);

if (result.valid) {
  // proceed
}
```
```

### See Also

Link to related entries to enable exploration:

```markdown
### See Also
- [Schema.define](./schema-define.md) — Create validation schemas
- [ValidationResult](./validation-result.md) — Result object structure
- [Custom validators](./custom-validators.md) — Creating custom rules
```

---

## Organizing Reference Documentation

### Entry Ordering

Choose one and be consistent:
- **Alphabetical** — Best for large APIs where users know the name
- **Categorical** — Group related items; good for discovery
- **Conceptual** — Order by concept complexity; good for learning alongside reference

### Index Section

Always include an index for discoverability:

```markdown
## Index

### Functions
- [validate](#validate) — Validate input against schema
- [sanitize](#sanitize) — Clean and normalize input
- [transform](#transform) — Convert between formats

### Types
- [Schema](#schema) — Validation schema definition
- [ValidationResult](#validationresult) — Validation output
```

### Navigation Aids

For large references:
- Table of contents at top
- Quick navigation links
- Search instructions (if platform supports)
- "Jump to" links within long pages

---

## Cognitive Load for References

### Target Profile

| Load Type | Level | Strategy |
|-----------|-------|----------|
| Intrinsic | Minimal per entry | Self-contained, no dependencies |
| Extraneous | Near zero | Consistent format, quick retrieval |
| Germane | N/A | Reference is for retrieval, not learning |

### Consistency Reduces Load

When every entry has the same structure, readers learn the format once and can navigate instantly thereafter.

**Critical:** Never deviate from your entry template. Missing sections should be explicit ("None" or "N/A"), not omitted.

---

## Reference Quality Standards

### Completeness

- [ ] Every public API/feature is documented
- [ ] No entries are "TODO" or "Coming soon"
- [ ] All parameters documented
- [ ] All return values documented
- [ ] All options documented

### Accuracy

- [ ] Signatures match actual implementation
- [ ] Default values are current
- [ ] Version numbers are correct
- [ ] Examples are tested and working

### Consistency

- [ ] Same structure for every entry
- [ ] Same terminology throughout
- [ ] Same formatting conventions
- [ ] Same level of detail per section

---

## Reference Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|--------------|--------------|-----|
| Narrative style | Slow to scan, hard to find info | Structured entries |
| Incomplete entries | Missing info wastes time | Full template always |
| Inconsistent format | Cognitive load on every lookup | Strict template |
| Mixing with explanation | Wrong place for "why" | Link to explanation |
| Outdated examples | Leads to errors | Regular testing |
| Assuming reading order | Entries should be standalone | Self-contained entries |

---

## Reference Checklist

Before publishing:

- [ ] Every entry uses the same template
- [ ] All parameters/options documented
- [ ] Return values specified
- [ ] Examples are minimal and working
- [ ] See Also links to related entries
- [ ] Index is complete and accurate
- [ ] Alphabetical or consistent ordering
- [ ] No narrative or explanatory text in entries
- [ ] Version/deprecation info where relevant
