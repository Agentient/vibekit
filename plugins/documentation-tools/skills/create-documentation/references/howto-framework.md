# How-To Guide Framework

How-to guides are **task-oriented** documentation that provides steps to accomplish a specific goal. The reader already knows what they want to do — they just need to know how.

---

## How-To Philosophy

### Core Principles

1. **Assume competence** — Reader knows the domain, not necessarily this specific task
2. **Goal-oriented** — Every element serves task completion
3. **Minimal context** — Only what's needed to do the task
4. **Respect time** — Reader is probably in the middle of work

### How-To vs. Tutorial

| How-To | Tutorial |
|--------|----------|
| Accomplish task X | Learn skill Y |
| Reader knows what they want | Reader discovers what's possible |
| Minimal explanation | Rich explanation |
| Multiple valid paths OK | One clear path |
| Result matters | Learning matters |

---

## How-To Structure

### Standard Format

```markdown
# How to [Goal]

**Prerequisites:** [Brief list or links]

---

## Steps

1. [Imperative action]
   ```
   [code if needed]
   ```

2. [Imperative action]

3. [Imperative action]

---

## Result
[What success looks like]

## Troubleshooting (optional)
[Common issues and fixes]
```

### Section Details

#### Title
Format: "How to [Verb] [Object]"
- Good: "How to reset a user's password"
- Good: "How to configure CORS for your API"
- Bad: "Password reset" (noun, not action)
- Bad: "Learn to configure CORS" (that's a tutorial)

#### Prerequisites
- Brief, scannable list
- Link to setup guides, don't explain here
- Include version requirements if relevant

Example:
```markdown
**Prerequisites:**
- Admin access to the dashboard
- User's email address
- MFA device (if user has MFA enabled)
```

#### Steps
- Numbered, imperative verbs
- One action per step
- Code blocks copy-paste ready
- No explanations unless critical

---

## Step Writing Guidelines

### The Imperative Rule

Every step starts with a verb:
- "Run..."
- "Navigate to..."
- "Click..."
- "Add..."
- "Configure..."

**Not:**
- "You should run..." (wordy)
- "The next step is to..." (wordy)
- "Now we..." (tutorial voice)

### One Action Per Step

```markdown
// Bad - two actions
1. Open the config file and add the API key

// Good - one action each
1. Open `config.json`
2. Add your API key:
   ```json
   { "apiKey": "your-key-here" }
   ```
```

### Code Block Requirements

Every code block must be:
- **Copy-paste ready** — No ... or [your value here] in runnable code
- **Self-contained** — Include necessary imports/context
- **Syntax highlighted** — Specify language
- **Brief** — Only what's needed for this step

```markdown
// Bad
```
// ... other config ...
db: { host: "localhost" }
```

// Good
```json
{
  "db": {
    "host": "localhost",
    "port": 5432
  }
}
```
```

### Expected Result

Include expected result when:
- Result is not obvious
- Confirmation prevents later problems
- The action could silently fail

Format:
```markdown
3. Run the migration:
   ```bash
   npm run migrate
   ```
   Output: "Migration complete: 3 tables created"
```

---

## Cognitive Load for How-Tos

### Target Profile

| Load Type | Level | Strategy |
|-----------|-------|----------|
| Intrinsic | Minimal | Assume competence, link to explanations |
| Extraneous | Zero | Only what's needed |
| Germane | Optional | Available via links for the curious |

### What to Exclude

- Theory (link to explanation instead)
- History or rationale
- Alternative approaches (unless critical)
- Related but unnecessary information
- Reassurance or encouragement

### What to Include

- Prerequisites
- Exact steps
- Expected results
- Common failure recovery
- Links to deeper content

---

## When to Cross-Reference

### Link to Tutorials When:
- The task requires skills the reader may not have
- Setup is complex enough to warrant learning

```markdown
**Prerequisites:**
- Completed the [authentication setup tutorial](./auth-tutorial.md)
```

### Link to Explanations When:
- The "why" matters for future decisions
- Behavior might seem surprising

```markdown
3. Add the middleware *before* your routes.
   [Why order matters](./middleware-explanation.md)
```

### Link to References When:
- Multiple options exist
- Reader may want to customize

```markdown
5. Configure the options:
   ```json
   { "timeout": 5000 }
   ```
   See the [full options reference](./options-reference.md)
```

---

## Multiple Paths

Unlike tutorials, how-tos can show alternatives:

```markdown
## Steps

### Option A: Using the CLI
1. Run `app reset-password --email user@example.com`

### Option B: Using the Dashboard
1. Navigate to Users > Find User
2. Click "Reset Password"
```

Use when:
- Paths are genuinely equivalent
- Reader preference matters (CLI vs GUI)
- Different environments need different approaches

Avoid when:
- One path is clearly better
- Differences require explanation (use explanation doc)

---

## Troubleshooting Section

Include when common issues exist. Format:

```markdown
## Troubleshooting

**"Permission denied" error**
You need admin privileges. Run with `sudo` or contact your system admin.

**"User not found" error**
Check the email address is correct. Emails are case-sensitive.
```

### Troubleshooting Principles

- Problem as heading (what they see)
- Solution as body (what to do)
- One issue per entry
- Most common issues first
- Keep solutions actionable

---

## How-To Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|--------------|--------------|-----|
| Long introduction | Reader skips it; wastes space | 1 sentence max |
| Explaining concepts | They came to do, not learn | Link to explanation |
| Tutorial voice ("Let's...") | Wrong tone; wastes words | Imperative verbs |
| Multiple actions per step | Confusing, error-prone | Split steps |
| Assuming context | Readers arrive from search | Self-contained |
| Missing prerequisites | Forces backtracking | List upfront |

---

## How-To Checklist

Before publishing:

- [ ] Title is "How to [verb] [object]"
- [ ] Prerequisites listed at top
- [ ] Each step starts with imperative verb
- [ ] One action per step
- [ ] Code blocks are copy-paste ready
- [ ] Result/verification is clear
- [ ] No unnecessary explanation
- [ ] Troubleshooting for common issues
- [ ] Tested on clean environment
