# Documentation Style Guide

Consistent style reduces cognitive load and builds reader trust. This guide establishes writing standards for all documentation produced by this skill.

---

## Voice and Tone

### Voice by Persona

| Persona | Voice | Tone | Example |
|---------|-------|------|---------|
| Anxious Novice | Reassuring | Patient, explicit | "Don't worry if this seems complex — we'll take it step by step." |
| Pragmatic Practitioner | Direct | Efficient, respectful | "Run `npm install` and restart the server." |
| Curious Explorer | Engaging | Intellectually generous | "This approach emerged because early systems had no concept of..." |

### General Voice Principles

1. **Active voice preferred** — "The function returns X" not "X is returned by the function"
2. **Second person for instructions** — "You can configure..." not "Users can configure..."
3. **Present tense for current behavior** — "The API returns JSON" not "The API will return JSON"
4. **Confident but not arrogant** — State facts directly without hedging, but acknowledge uncertainty when it exists

### Words to Avoid

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| Simply | Implies ease; creates shame if difficult | Remove entirely |
| Obviously | Alienates those to whom it's not obvious | Remove entirely |
| Just | Minimizes; suggests it should be easy | Remove entirely |
| Easy/Easily | Creates expectations that may not match reality | Remove or be specific |
| Basically | Vague; adds no meaning | Remove entirely |
| Very, Really | Weak intensifiers | Use specific descriptors |
| Note that | Usually unnecessary preamble | Remove; state the note directly |

---

## Sentence and Paragraph Structure

### Reading Level Guidelines

| Level | Max Words/Sentence | Paragraph Length | Vocabulary |
|-------|-------------------|------------------|------------|
| Grade 8 | 15 | 2-3 sentences | Common words, no jargon |
| Grade 12 | 20 | 3-4 sentences | Some technical terms, defined |
| Professional | 25 | 4-5 sentences | Technical terms expected |

### Sentence Principles

1. **One idea per sentence** — If you use "and" or "but" mid-sentence, consider splitting
2. **Lead with the action** — "Run X" not "In order to accomplish Y, first run X"
3. **Front-load important words** — Put key terms at the start of sentences
4. **Vary sentence length** — Mix short and medium sentences for rhythm

### Paragraph Principles

1. **One topic per paragraph** — If the topic shifts, start a new paragraph
2. **Topic sentence first** — The first sentence should indicate what the paragraph covers
3. **No orphan sentences** — Single-sentence paragraphs are usually too sparse or should be lists
4. **Transitions are optional** — Don't force transitions; white space can signal topic change

---

## Technical Terminology

### First-Use Rule

Every technical term must be defined on first use, even if "everyone knows it."

**Format options:**
- Inline: "The API (Application Programming Interface) provides..."
- Appositive: "Use the CLI — the command-line interface — to..."
- Following sentence: "Open the REPL. This interactive environment lets you..."

### Glossary Requirements

Include a glossary when:
- Document introduces 5+ new terms
- Document is > 2000 words
- Primary persona is Anxious Novice

### Abbreviation Handling

| Usage Count | Approach |
|-------------|----------|
| 1-2 times | Spell out every time |
| 3+ times | Define on first use, abbreviate after |
| Very common (API, URL) | May abbreviate without definition for professional reading level |

### Jargon Translation

For each reading level, translate appropriately:

| Technical Term | Grade 8 | Grade 12 | Professional |
|----------------|---------|----------|--------------|
| Instantiate | Create | Create a new instance of | Instantiate |
| Asynchronous | Happening later | Non-blocking, completes later | Asynchronous |
| Authenticate | Prove who you are | Verify identity | Authenticate |

---

## Code and Examples

### Code Block Formatting

**Inline code:** Use for `file names`, `commands`, `variable names`, and short code snippets.

**Code blocks:** Use for:
- Multi-line code
- Code meant to be copy-pasted
- Code that benefits from syntax highlighting

### Code Block Requirements

1. **Language tag always** — ```javascript, ```bash, etc.
2. **Copy-paste ready** — No ellipses (...) in code meant to be run
3. **Highlight changes** — Use comments or diff formatting to show modifications
4. **Include output when relevant** — Show expected results

### Comment Density

| Audience | Comment Style |
|----------|--------------|
| Novice | Comment every non-obvious line |
| Intermediate | Comment sections, not lines |
| Expert | Minimal; only for surprising code |

### Example Progression

When showing multiple examples:
1. Start simple — Minimal viable example
2. Build complexity — Add real-world considerations
3. Show edge cases — What happens when things go wrong

### Working Example Requirements

All code examples must:
- [ ] Be syntactically correct
- [ ] Run without modification (if runnable)
- [ ] Include necessary imports/setup
- [ ] Show expected output or result

---

## Formatting Conventions

### Headings

- **H1:** Document title only (one per document)
- **H2:** Major sections
- **H3:** Subsections within H2
- **H4:** Rarely used; consider if structure is too deep

**Heading style:**
- Title case for H1: "Getting Started with Authentication"
- Sentence case for H2-H4: "Setting up your environment"
- No periods at end of headings
- Headings should be scannable and descriptive

### Lists

**Use bullet lists when:**
- Items are not sequential
- Order doesn't matter
- Items are short (1-2 lines each)

**Use numbered lists when:**
- Items are steps to follow
- Order matters
- You'll reference items by number

**List formatting:**
- Parallel structure (all items same grammatical form)
- Consistent punctuation (all periods or no periods)
- No more than 7 items per list (chunk if more)

### Callouts

| Type | Use For | Visual Treatment |
|------|---------|------------------|
| Note | Supplementary information | Subtle highlight |
| Tip | Helpful suggestion, not required | Positive indicator |
| Warning | Risk of problems if ignored | Attention-grabbing |
| Danger | Risk of data loss or security issue | Strong alert |

**Callout rules:**
- One callout type per callout
- Keep callouts short (1-3 sentences)
- Don't overuse — more than 3 per page reduces impact

### Cross-References

**Internal links:** Use descriptive text, not "click here"
- Good: "See the [authentication guide](./auth.md) for details"
- Bad: "Click [here](./auth.md) for details"

**External links:** Include context about destination
- Good: "The [OAuth 2.0 specification](https://...) defines the protocol"
- Bad: "See [this link](https://...)"

---

## Common Mistakes

### Curse of Knowledge Indicators

You may have the curse of knowledge if you:
- Skip steps that seem "obvious"
- Use jargon without realizing it
- Assume readers know your mental model
- Write "as we discussed" without linking

**Antidote:** Have someone unfamiliar with the topic read your draft.

### Assumptions Checklist

Before publishing, verify you haven't assumed:
- [ ] Reader knows the domain vocabulary
- [ ] Reader has specific tools installed
- [ ] Reader has seen previous documentation
- [ ] Reader understands why they're doing this
- [ ] Reader can infer missing steps

### Ambiguity Red Flags

| Red Flag | Example | Fix |
|----------|---------|-----|
| Unclear "it" | "Run the script. It will create..." | "Run the script. The script will create..." |
| Vague "this" | "This causes problems" | "Running without admin privileges causes problems" |
| Multiple possible referents | "The user and the admin can both access this" | Clarify which |
| Unclear scope | "Update the config" | "Update `config.json` in the root directory" |

### Consistency Violations

Check for consistency in:
- [ ] Terminology (same word for same concept)
- [ ] Formatting (code style, heading levels)
- [ ] Tone (don't switch between formal and casual)
- [ ] Naming (file names, variable names)
- [ ] Capitalization (product names, technical terms)
