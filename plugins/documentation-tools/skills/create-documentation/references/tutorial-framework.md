# Tutorial Framework

Tutorials are **learning-oriented** documentation that takes readers through a series of steps to complete a project. The goal is learning by doing in a safe environment with guaranteed success.

---

## Tutorial Philosophy

### Core Principles

1. **Learning by doing** — Readers learn through hands-on action, not reading about action
2. **Explicit state changes** — Every action produces a visible, verifiable result
3. **Safe to fail** — Mistakes are recoverable; nothing breaks permanently
4. **Guaranteed success** — Following the tutorial exactly will work
5. **No choices** — One path, clearly marked; choices come later

### Tutorial vs. Other Types

| Tutorial | How-To |
|----------|--------|
| "Learn to do X" | "Do X" |
| Teaches transferable skills | Accomplishes specific task |
| Comprehensive path | Minimal steps |
| Explains why | Just tells what |

**Key insight:** A tutorial succeeds when the reader can apply what they learned to a *different* situation. A how-to succeeds when the specific task is complete.

---

## Tutorial Structure

### Required Sections

```markdown
# Tutorial: [Action] + [Outcome]

## What You'll Learn
[Skills/knowledge gained — use bullet list]

## Prerequisites
[What they need before starting]

## Time Required
[Realistic estimate]

---

## Step 1: [First Action]
[Content]

## Step 2: [Second Action]
[Content]

...

---

## What You've Learned
[Summary of skills acquired]

## Next Steps
[Where to go from here]
```

### Section Details

#### Title
Format: "Tutorial: [Verb] + [Outcome]"
- Good: "Tutorial: Build a REST API with Express"
- Bad: "Express Tutorial" (no outcome)
- Bad: "How to Build APIs" (that's a how-to)

#### What You'll Learn
- Use bullet list
- Focus on transferable skills, not tutorial-specific artifacts
- 3-5 items maximum

Example:
```markdown
## What You'll Learn
- Create and configure a basic Express server
- Define routes that handle HTTP methods
- Connect to a database and perform CRUD operations
- Handle errors gracefully
```

#### Prerequisites
- Be specific about versions and requirements
- Link to installation guides
- Include knowledge prerequisites

Example:
```markdown
## Prerequisites
- Node.js v18+ installed ([installation guide](./install-node.md))
- Basic JavaScript knowledge (variables, functions, arrays)
- A code editor (VS Code recommended)
- A terminal/command line
```

#### Time Required
- Provide realistic range
- Account for debugging and confusion
- Format: "30-45 minutes" not "30 minutes"

---

## Step Writing Pattern

Each step follows this structure:

```markdown
## Step N: [Action in Imperative Form]

[1-2 sentences explaining what we're doing and why]

**Do this:**
```language
[code or action]
```

[Optional: Brief explanation of key parts]

**Verify:** [How to confirm it worked]

[Optional: "If you see X instead, try Y"]
```

### Step Principles

1. **One concept per step** — If you're explaining two things, split the step
2. **Imperative title** — "Configure the database" not "Database configuration"
3. **Why before what** — Brief context before the action
4. **Verification mandatory** — Every step needs a way to confirm success
5. **Recovery optional but encouraged** — Include for likely failure points

### Step Example

```markdown
## Step 3: Create the Database Connection

Now we'll connect to our database. This connection will be reused
throughout the application.

**Do this:**
Create a new file called `db.js`:
```javascript
const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/tutorial')
  .then(() => console.log('Connected to database'))
  .catch(err => console.error('Connection failed:', err));

module.exports = mongoose;
```

The `connect` function returns a promise that resolves when the
connection is established.

**Verify:** Run `node db.js`. You should see "Connected to database"
in your terminal.

If you see "Connection failed," make sure MongoDB is running.
On macOS: `brew services start mongodb-community`
```

---

## Worked Example Principles

Tutorials are built around worked examples — complete solutions shown with reasoning.

### The Worked Example Effect

Novices learn better from studying worked examples than from solving problems. This is because:
- Problem-solving consumes cognitive resources that could be used for learning
- Worked examples allow focus on understanding, not flailing
- The reasoning process is visible, not hidden

### Example Progression (Fading)

Move from full scaffolding to independence:

| Stage | What You Show | What Reader Does |
|-------|---------------|------------------|
| 1. Complete | Full code with comments | Read and understand |
| 2. Guided | Code with blanks or prompts | Fill in guided parts |
| 3. Scaffolded | Structure only | Write the code |
| 4. Independent | Nothing | Solve similar problem |

**In tutorials:** Usually stages 1-2. Stage 3-4 comes in exercises or follow-up content.

### Annotation Techniques

When showing worked examples:

```javascript
// 1. First, we import the library
const express = require('express');

// 2. Create an app instance
const app = express();

// 3. Define a route - this is where requests will go
app.get('/', (req, res) => {
  // 4. Send a response back to the client
  res.send('Hello World');
});
```

- Number the steps
- Explain WHY, not just what
- One comment per logical unit
- Keep comments brief

---

## Error Recovery Paths

Tutorials must handle the inevitable: things will go wrong.

### When to Include Recovery

| Situation | Include Recovery? |
|-----------|------------------|
| Common error (>20% hit) | Yes, inline |
| Uncommon but confusing | Yes, in troubleshooting section |
| Rare and obvious fix | No |
| Environment-specific | Yes, for major environments |

### Recovery Format

```markdown
**If you see this error:**
```
Error: Cannot find module 'express'
```

**Try this:**
You need to install the dependency. Run:
```bash
npm install express
```
Then try Step 3 again.
```

### Troubleshooting Section

For more complex tutorials, include at the end:

```markdown
## Troubleshooting

### "Cannot connect to database"
Make sure MongoDB is running. On macOS: `brew services start mongodb-community`

### "Port already in use"
Another process is using port 3000. Either stop that process or change the
port in `server.js` to 3001.
```

---

## Cognitive Load for Tutorials

### Target Profile

| Load Type | Level | Strategy |
|-----------|-------|----------|
| Intrinsic | Managed | One concept per step, careful sequencing |
| Extraneous | Minimal | No tangents, no unnecessary info |
| Germane | Maximum | Worked examples, verification, reflection |

### Load Management Techniques

1. **Sequence by dependency** — Only introduce concept when needed
2. **Immediate verification** — Reduce time between action and feedback
3. **No foreshadowing** — Don't mention future complexity
4. **Repetition is good** — Seeing patterns multiple times aids learning
5. **Concrete before abstract** — Show the code, then explain the principle

---

## Tutorial Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|--------------|--------------|-----|
| Teaching concepts first | Novices don't know where to put abstract info | Show, then explain |
| Too many choices | Decision fatigue; analysis paralysis | One path |
| Skipping steps | Readers get lost and can't recover | Every step, every command |
| "Left as exercise" | Learners need complete examples | Show everything |
| Version mismatches | Code doesn't work | Pin versions, test regularly |
| Assuming tools installed | Stops readers at step 1 | Complete prerequisites |
| Long code blocks | Overwhelming; can't track what's happening | Break into steps |
| No verification | Reader doesn't know if they succeeded | Verify every step |

---

## Tutorial Checklist

Before publishing:

- [ ] Title clearly states what will be built
- [ ] Prerequisites are complete and specific
- [ ] Time estimate is realistic
- [ ] Each step has one concept only
- [ ] Every step has verification
- [ ] Code runs without modification
- [ ] Recovery paths for common errors
- [ ] "What you learned" summarizes skills
- [ ] Next steps point to relevant content
- [ ] Tested end-to-end on clean environment
