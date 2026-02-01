# Generate Architecture Decision Record (ADR) Command

You are creating an Architecture Decision Record to document a significant technical decision, its context, rationale, and consequences.

## What is an ADR?

An ADR is a lightweight document that captures:
- **What** decision was made
- **Why** it was made (context and drivers)
- **What alternatives** were considered
- **What consequences** (positive and negative) result from the decision

## When to Create an ADR

Create an ADR when making decisions about:
- Technology selection (frameworks, libraries, databases)
- Architectural patterns (Server Components vs Client Components, state management approach)
- API design (REST vs GraphQL vs Server Actions)
- Data modeling approaches
- Security patterns
- Performance optimizations with trade-offs
- Third-party service integrations

## ADR Template

Use this structure:

```markdown
# ADR-[NUMBER]: [Title in Present Tense]

**Date**: YYYY-MM-DD
**Status**: [Proposed | Accepted | Deprecated | Superseded by ADR-XXX]
**Deciders**: [Names of people involved in the decision]

## Context

[What is the issue, problem, or opportunity that is motivating this decision?
What are the forces at play? What constraints exist?]

Include:
- Background information
- Current situation/pain points
- Requirements or goals
- Constraints (technical, business, time)

## Decision

[What is the change we're proposing/implementing?]

Be specific and concrete. Describe the solution in enough detail that someone can implement it.

Example:
"We will use React Server Components as the default rendering strategy for all pages
and components. Client Components (marked with 'use client') will be used only for
interactive features that require state, event handlers, or browser APIs."

## Consequences

### Positive Consequences (Benefits)
- [Benefit 1 - be specific]
- [Benefit 2 - quantify if possible]
- [Benefit 3]

### Negative Consequences (Costs/Drawbacks/Risks)
- [Drawback 1 - be honest about limitations]
- [Drawback 2]
- [Drawback 3]

### Mitigation Strategies
- [How to address Drawback 1]
- [How to address Drawback 2]
- [How to address Drawback 3]

## Alternatives Considered

### Alternative 1: [Name]
- **Description**: [Brief explanation of this option]
- **Pros**:
  - [What's good about this approach]
- **Cons**:
  - [What's bad about this approach]
- **Why Rejected**: [Specific reason this was not chosen]

### Alternative 2: [Name]
- **Description**: [Brief explanation]
- **Pros**: [Advantages]
- **Cons**: [Disadvantages]
- **Why Rejected**: [Specific reason]

[Add more alternatives as needed]

## References

- [Link to relevant documentation]
- [Link to RFC or proposal]
- [Link to related ADRs]
- [Link to benchmark or research]
```

## Execution Instructions

### Step 1: Identify Decision Details

Ask the user:
1. **What decision** are you documenting?
2. **What problem** does it solve?
3. **What alternatives** did you consider?
4. **Who** was involved in the decision?

### Step 2: Number the ADR

Check `docs/adr/` directory for existing ADRs:

```bash
ls docs/adr/
```

Use the next sequential number (e.g., if 003-*.md exists, create 004-*.md).

### Step 3: Create the ADR File

Filename format: `[NUMBER]-[kebab-case-title].md`

Example: `004-adopt-zustand-for-global-state.md`

```bash
# In docs/adr/ directory
touch 004-adopt-zustand-for-global-state.md
```

### Step 4: Fill in the Template

Populate each section thoughtfully:

#### Context Section
- Explain the problem or opportunity clearly
- Provide enough background for someone unfamiliar with the project to understand
- List the forces/constraints influencing the decision

#### Decision Section
- State the decision clearly and definitively
- Use present tense ("We will use...", "We will adopt...")
- Be specific enough for implementation

#### Consequences Section
- Be balanced - list both positive and negative consequences
- Be honest about trade-offs and limitations
- Provide concrete mitigation strategies for negative consequences

#### Alternatives Section
- Show that you considered other options
- Explain why each was rejected
- Demonstrate due diligence in decision-making

### Step 5: Set Status

- **Proposed**: Decision is under discussion
- **Accepted**: Decision has been approved and is being implemented
- **Deprecated**: Decision is no longer valid
- **Superseded by ADR-XXX**: Decision has been replaced by a newer ADR

### Step 6: Review Checklist

Before finalizing, verify:
- [ ] Title clearly states the decision
- [ ] Context explains why the decision is needed
- [ ] Decision is specific and actionable
- [ ] Both positive and negative consequences are listed
- [ ] At least 2 alternatives are considered and rejected
- [ ] References/links are provided
- [ ] Language is clear and concise
- [ ] Status is set appropriately

## Example ADR

```markdown
# ADR-004: Adopt Zustand for Global Client State Management

**Date**: 2025-10-23
**Status**: Accepted
**Deciders**: Engineering Team, Tech Lead

## Context

Our Next.js 14+ application uses React Server Components as the default rendering
strategy (see ADR-001). However, some features require shared client-side state
across multiple Client Components (e.g., shopping cart, user preferences, theme).

We need a state management solution that:
- Works well with React Server Components architecture
- Has minimal bundle size impact
- Provides TypeScript support
- Is simple to use and maintain
- Doesn't cause unnecessary re-renders

Constraints:
- Must integrate with existing Server Component patterns
- Bundle size budget: < 5KB for state library
- Team has limited time for learning complex APIs

## Decision

We will use **Zustand** (v5.0.2+) as our global client-side state management library.

Zustand stores will be used for:
- Shopping cart state
- User preferences (theme, language)
- UI state that needs to persist across navigation
- Feature flags and toggles

We will NOT use Zustand for:
- Server-fetched data (use Server Components or Server Actions instead)
- Form state (use React Hook Form)
- URL-based state (use searchParams)

## Consequences

### Positive Consequences
- **Tiny Bundle Size**: Zustand is ~1.2KB gzipped (vs 43KB for Redux Toolkit)
- **Simple API**: Minimal learning curve for the team
- **TypeScript Support**: Full type safety with TypeScript
- **No Boilerplate**: No actions, reducers, or providers required
- **Selective Subscriptions**: Components re-render only when their specific state slice changes
- **Server Component Compatible**: Stores are client-only, no hydration issues

### Negative Consequences
- **Less Ecosystem**: Smaller plugin ecosystem compared to Redux
- **No Time-Travel Debugging**: Unlike Redux DevTools (though Zustand has basic devtools)
- **Team Learning**: Team needs to learn Zustand patterns (though API is simple)

### Mitigation Strategies
- Document common Zustand patterns in project wiki
- Create reusable store templates for common use cases
- Use Zustand middleware (persist, devtools) for debugging support
- Establish naming conventions (e.g., useCartStore, useThemeStore)

## Alternatives Considered

### Alternative 1: Redux Toolkit
- **Description**: Industry-standard state management with Redux Toolkit
- **Pros**:
  - Mature ecosystem
  - Excellent DevTools
  - Well-known by most developers
- **Cons**:
  - 43KB bundle size (36x larger than Zustand)
  - More boilerplate (slices, actions, reducers)
  - More complex API
- **Why Rejected**: Bundle size overhead not justified for our use cases. Server Components reduce need for global state, so we need a lightweight solution.

### Alternative 2: React Context + useReducer
- **Description**: Built-in React state management
- **Pros**:
  - No additional dependencies
  - Native to React
  - Zero bundle size cost
- **Cons**:
  - Causes re-renders of all consumers when any context value changes
  - Requires manual optimization (splitting contexts, memo)
  - More verbose to set up
- **Why Rejected**: Performance issues with larger state and multiple consumers. Would require significant optimization work.

### Alternative 3: Jotai
- **Description**: Atomic state management library
- **Pros**:
  - Very small bundle size (~3KB)
  - Atom-based approach prevents unnecessary re-renders
  - Good TypeScript support
- **Cons**:
  - Different mental model (atoms vs stores)
  - Less mature documentation
  - Team unfamiliar with atomic state patterns
- **Why Rejected**: While technically excellent, the atomic model has a steeper learning curve. Zustand's simpler API is better for our team.

## References

- [Zustand Documentation](https://zustand-demo.pmnd.rs/)
- [Zustand GitHub](https://github.com/pmndrs/zustand)
- [Next.js Client Component Patterns](https://nextjs.org/docs/app/building-your-application/rendering/client-components)
- [ADR-001: Adopt Next.js App Router](./001-adopt-nextjs-app-router.md)
```

## After Creating the ADR

1. **Commit the ADR** to version control
2. **Reference the ADR** in code comments where the decision is implemented
3. **Update the ADR** if the decision changes (add Superseded status and create new ADR)
4. **Share the ADR** with the team in Slack/Discord/Email

---

**Ready to document a decision? Provide the decision details and I'll create the ADR.**
