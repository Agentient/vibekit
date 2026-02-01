# Question Taxonomy for Research Interviewing

A comprehensive reference for the 8 question types used in adaptive knowledge elicitation.

---

## Overview

### The 8 Question Types

| # | Type | Purpose | Signal to Use |
|---|------|---------|---------------|
| 1 | Grand Tour | Map the landscape | New dimension, need context |
| 2 | Structural | Understand organization | Need relationships, hierarchy |
| 3 | Contrast | Distinguish concepts | Similar things need differentiation |
| 4 | Example | Ground in concrete | Abstract needs illustration |
| 5 | Probing | Dig deeper | Response was vague |
| 6 | Devil's Advocate | Test assumptions | Challenge conviction |
| 7 | Clarifying | Resolve ambiguity | Meaning unclear |
| 8 | Confirming | Validate understanding | Ready to close dimension |

---

## 1. Grand Tour Questions

### Purpose
Establish the broad landscape of a domain or dimension before diving into specifics.

### When to Use
- Opening a new dimension
- Understanding overall context
- Letting interviewee set the frame

### Formula
```
"Tell me about [topic]."
"Walk me through [process/system]."
"What does [domain] look like from your perspective?"
"Help me understand the big picture of [area]."
```

### Examples

**Good:**
- "Walk me through how your team currently handles authentication."
- "Tell me about the data pipeline from end to end."
- "What does a typical user journey look like?"

**Bad (Too narrow for Grand Tour):**
- "What authentication library do you use?" (too specific)
- "How long does step 3 take?" (requires prior context)

### What to Listen For
- Scope and boundaries
- Key components mentioned
- Terminology used
- Energy/enthusiasm indicators
- What they mention first (priority signal)

---

## 2. Structural Questions

### Purpose
Understand organization, hierarchy, relationships, or how things connect.

### When to Use
- Need to understand how parts relate
- Building a mental model
- Mapping dependencies

### Formula
```
"How is [X] organized?"
"What are the main parts of [Y]?"
"How do [A] and [B] relate to each other?"
"What's the hierarchy of [system]?"
```

### Examples

**Good:**
- "What are the different user roles in your system and how do they relate?"
- "How is the codebase organized? What are the main modules?"
- "What teams are involved and how do they coordinate?"

**Bad:**
- "Is there a hierarchy?" (yes/no, not structural)
- "What's the structure?" (too vague)

### What to Listen For
- Parent-child relationships
- Peer relationships
- Dependencies
- Ownership boundaries
- Gaps in the structure

---

## 3. Contrast Questions

### Purpose
Differentiate between related or similar concepts that might be confused.

### When to Use
- Two things seem similar but might be different
- Need to understand distinctions
- Clarifying boundaries between concepts

### Formula
```
"What's the difference between [X] and [Y]?"
"How do you distinguish [A] from [B]?"
"When would you use [option 1] versus [option 2]?"
```

### Examples

**Good:**
- "How do you differentiate a bug from a feature request in your tracking system?"
- "What's the difference between authentication and authorization in your system?"
- "When would you use the async process versus the sync one?"

**Bad:**
- "What's the difference?" (missing specifics)
- "Which is better?" (evaluation, not contrast)

### What to Listen For
- Distinguishing characteristics
- Decision criteria
- Edge cases where they overlap
- Situations where distinction matters

---

## 4. Example Questions

### Purpose
Ground abstract concepts in concrete, specific instances.

### When to Use
- Concept is abstract or vague
- Need to verify understanding with real data
- Want to understand typical vs. edge cases

### Formula
```
"Can you give me an example of [X]?"
"Walk me through a specific instance of [Y]."
"Think of a recent time when [situation]. What happened?"
"What does that look like in practice?"
```

### Examples

**Good:**
- "Can you describe a recent situation where the current process failed?"
- "Walk me through what happened the last time you onboarded a new user."
- "Give me an example of a 'complex' request you mentioned."

**Bad:**
- "What are some examples?" (too open, gets list not depth)
- "Is there an example?" (yes/no)

### What to Listen For
- Specific details (names, dates, numbers)
- Sequence of events
- Emotional response (frustration, success)
- What made this case memorable
- Deviation from the "standard" path

---

## 5. Probing Questions

### Purpose
Dig deeper into vague, incomplete, or surface-level responses.

### When to Use
- Response lacks specificity
- Feeling like something was glossed over
- Key term was used without definition

### Formula
```
"You mentioned [X]. Can you tell me more about that?"
"What did you mean by [Y]?"
"What specifically makes it [adjective]?"
"Can you unpack that a bit?"
```

### Examples

**Good:**
- "You said it's 'complicated.' What specifically makes it complicated?"
- "You mentioned 'sometimes' issues occur. How often is sometimes?"
- "What do you mean when you say the system is 'slow'?"

**Bad:**
- "Tell me more." (too vague)
- "Really?" (not a probe)

### What to Listen For
- Underlying root causes
- Specific numbers/metrics
- Hidden complexity
- Emotional weight behind vague terms
- What they were protecting by being vague

---

## 6. Devil's Advocate Questions

### Purpose
Stress-test assumptions, claims, and confident assertions.

### When to Use
- Interviewee seems very certain
- Important assumption hasn't been challenged
- Need to verify conviction vs. habit
- Testing robustness of position

### Formula
```
"What if [counter-scenario]?"
"Someone might argue [opposite position]. How would you respond?"
"What would have to be true for [X] to be wrong?"
"Play devil's advocate with me—why might this approach fail?"
```

### Examples

**Good:**
- "What if we assumed the opposite—that users actually want more friction?"
- "Some teams choose the other approach. Why might they be right?"
- "What would cause this requirement to become unnecessary?"

**Bad:**
- "Are you sure?" (confrontational, not productive)
- "But what about..." (leading, not open)

### What to Listen For
- Strength of conviction (changes position or digs in)
- Underlying reasoning revealed
- Edge cases and exceptions
- Hidden assumptions exposed
- Conditions under which they'd change their mind

### Validation Mode Adjustment
- **Empathetic:** Use sparingly, soften phrasing
- **Balanced:** Use when confidence seems overblown
- **Rigorous:** Use on every significant claim

---

## 7. Clarifying Questions

### Purpose
Resolve ambiguity and ensure shared understanding of terms and concepts.

### When to Use
- Statement has multiple interpretations
- Technical term used without definition
- Pronouns or references unclear
- Scope of claim uncertain

### Formula
```
"When you say [X], do you mean [interpretation A] or [interpretation B]?"
"Just to make sure I understand—by [term], you mean...?"
"Who specifically are you referring to when you say [they/we/the team]?"
"Is that [X] in the narrow sense or the broader sense?"
```

### Examples

**Good:**
- "When you say 'real-time,' do you mean milliseconds or seconds?"
- "By 'users' do you mean all users or just premium users?"
- "When you said 'we decided,' was that your team or leadership?"

**Bad:**
- "What do you mean?" (too open for clarification)
- "Huh?" (not professional)

### What to Listen For
- The correct interpretation
- Nuances you missed
- Scope boundaries
- Precision of their language

---

## 8. Confirming Questions

### Purpose
Validate understanding and explicitly close loops on gathered information.

### When to Use
- Synthesizing understanding of a dimension
- Before moving to new area
- Verifying key findings
- Closing the interview

### Formula
```
"So if I understand correctly, [summary]. Is that accurate?"
"Let me play back what I heard: [synthesis]. Did I get that right?"
"To confirm: the key point is [X] because [Y]. Yes?"
"Am I correct that [statement]?"
```

### Examples

**Good:**
- "So the core requirement is sub-100ms latency for the critical path. Correct?"
- "If I'm understanding right, the main blocker is lack of API documentation, not technical capability. Is that accurate?"
- "To summarize this area: you have three user types, each with different permission levels, and the admin can modify all of them. Did I capture that correctly?"

**Bad:**
- "Right?" (too casual, doesn't show understanding)
- Summarizing without asking for confirmation

### What to Listen For
- Affirmation or correction
- Additions ("Yes, and also...")
- Nuances ("Mostly, but...")
- New information triggered by summary

---

## Question Sequencing

### Typical Flow Within a Dimension

```
1. GRAND TOUR → Establish landscape
   ↓
2. STRUCTURAL → Understand organization
   ↓
3. EXAMPLE → Ground in concrete
   ↓
4. PROBING → Deepen where needed
   ↓
5. CONTRAST → Clarify distinctions
   ↓
6. DEVIL'S ADVOCATE → Test assumptions
   ↓
7. CONFIRMING → Lock in understanding
```

### Adaptive Branching

```
Response vague?
  → PROBING or EXAMPLE

New term introduced?
  → CLARIFYING

Confident claim made?
  → DEVIL'S ADVOCATE

Multiple similar things mentioned?
  → CONTRAST

Ready to move on?
  → CONFIRMING
```

### Anti-Patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| Same type 3x in a row | Feels repetitive | Vary question types |
| Devil's Advocate first | Feels aggressive | Build rapport first |
| Confirming without depth | Surface understanding | Probe before confirming |
| Grand Tour mid-dimension | Loses focus | Save for new dimensions |

---

## Question Quality Checklist

Before asking, verify:

- [ ] **Single focus:** One question at a time
- [ ] **Open-ended:** Can't be answered yes/no (except Confirming)
- [ ] **Non-leading:** Doesn't embed the answer you want
- [ ] **Clear:** No jargon unless already established
- [ ] **Purposeful:** Knows why you're asking this
- [ ] **Sequenced:** Follows logically from last response
