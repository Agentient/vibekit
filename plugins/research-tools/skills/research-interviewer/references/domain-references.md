# Domain References

Domain-specific vocabulary, MECE patterns, and interview configurations for the research-interviewer skill.

---

## Overview

### Supported Domains

| Domain | Focus | Default MECE | Validation Mode |
|--------|-------|--------------|-----------------|
| **product** | Users, features, market | Market Research | balanced |
| **architecture** | Systems, components, tech | Technology Evaluation | rigorous |
| **research** | Questions, methods, findings | Strategic Research | balanced |
| **requirements** | Jobs, acceptance criteria | Custom | empathetic |
| **custom** | User-defined | User-specified | balanced |
| **none** | Generic | Generic 5-dimension | balanced |

---

## 1. Product Domain

**Purpose:** Product discovery, problem validation, feature elicitation

### Key Concepts

| Concept | Definition | Question Focus |
|---------|------------|----------------|
| **User** | Who uses the product | Personas, segments, behaviors |
| **Feature** | What the product does | Capabilities, gaps, priorities |
| **UX** | How it feels to use | Friction, delight, usability |
| **Roadmap** | Where it's going | Plans, priorities, timeline |
| **Market** | External context | Competition, trends, positioning |

### Default MECE Pattern: Market Research

| Dimension | Sub-Areas | Priority |
|-----------|-----------|----------|
| **User Needs** | Personas, jobs-to-be-done, pain points | Critical |
| **Current Solution** | Features, gaps, workarounds | Critical |
| **Competitive Landscape** | Alternatives, differentiation | Important |
| **Success Metrics** | KPIs, measurement, targets | Important |
| **Constraints** | Technical, business, timeline | Critical |

### Typical Stakeholders
- Product Manager (primary)
- End Users (primary)
- Engineering Lead (secondary)
- Design Lead (secondary)
- Customer Success (secondary)

### Question Patterns

| Type | Product-Specific Pattern |
|------|--------------------------|
| Grand Tour | "Walk me through a typical day when you encounter this problem" |
| Structural | "How does this problem connect to other challenges you face?" |
| Contrast | "How is this different from [similar problem]?" |
| Example | "Can you give me a specific recent example?" |
| Probing | "What happens when [current solution] fails?" |
| Devil's Advocate | "What if this problem just went away—would anything negative happen?" |
| Clarifying | "When you say [term], what specifically do you mean?" |
| Confirming | "So the core issue is [summary]. Did I capture that correctly?" |

### Common Assumptions to Surface
- "Users want more features" (vs. simplicity)
- "Mobile is secondary" (vs. mobile-first)
- "Enterprise is the growth path" (vs. SMB/consumer)
- "Price is the main objection" (vs. value/fit)

### Confidence Traps
- Taking feature requests literally (probe for underlying need)
- Assuming stated priority matches actual behavior
- Conflating "would use" with "would pay"
- Treating vocal users as representative

---

## 2. Architecture Domain

**Purpose:** Technical decision documentation, system understanding, constraint capture

### Key Concepts

| Concept | Definition | Question Focus |
|---------|------------|----------------|
| **System** | Bounded technical unit | Boundaries, responsibilities |
| **Component** | Part of a system | Function, dependencies |
| **Interface** | Connection point | Contracts, protocols |
| **Data** | Information flow | Schema, storage, movement |
| **Infrastructure** | Underlying platform | Deployment, scaling |

### Default MECE Pattern: Technology Evaluation

| Dimension | Sub-Areas | Priority |
|-----------|-----------|----------|
| **Current State** | Architecture, tech stack, patterns | Critical |
| **Capabilities** | What it can do, performance | Critical |
| **Constraints** | Technical debt, limitations | Critical |
| **Integration** | External systems, APIs | Important |
| **Evolution** | Roadmap, migration paths | Important |

### Typical Stakeholders
- Technical Architect (primary)
- Engineering Lead (primary)
- DevOps/SRE (secondary)
- Security Engineer (secondary)
- Product Manager (tertiary)

### Question Patterns

| Type | Architecture-Specific Pattern |
|------|-------------------------------|
| Grand Tour | "Describe the current system architecture at a high level" |
| Structural | "What are the key dependencies between components?" |
| Contrast | "How does this approach differ from [alternative]?" |
| Example | "Walk me through how a request flows through the system" |
| Probing | "What happens when [component] fails?" |
| Devil's Advocate | "What's the strongest argument for [alternative approach]?" |
| Clarifying | "When you say 'scalable', what specific metrics matter?" |
| Confirming | "So the key constraint is [X]. Is that accurate?" |

### Common Assumptions to Surface
- "The database can scale" (actual limits unknown)
- "Microservices are the solution" (vs. modular monolith)
- "Cloud provider won't change" (vendor lock-in)
- "Current team can maintain this" (skill assumptions)

### Confidence Traps
- Assuming current architecture diagrams are accurate
- Taking "it should scale" without specific numbers
- Conflating "we could" with "we should"
- Missing hidden dependencies

---

## 3. Research Domain

**Purpose:** Research question refinement, methodology design, scope definition

### Key Concepts

| Concept | Definition | Question Focus |
|---------|------------|----------------|
| **Question** | What we want to know | Clarity, scope, answerable |
| **Hypothesis** | Proposed answer | Testable, falsifiable |
| **Method** | How to investigate | Approach, rigor, bias |
| **Finding** | What we discovered | Evidence, confidence |
| **Implication** | What it means | Actions, decisions |

### Default MECE Pattern: Strategic Research

| Dimension | Sub-Areas | Priority |
|-----------|-----------|----------|
| **Research Objective** | Questions, scope, success criteria | Critical |
| **Current Knowledge** | What's known, gaps | Critical |
| **Methodology** | Approach, sources, rigor | Important |
| **Constraints** | Time, resources, access | Important |
| **Stakeholders** | Who needs this, how they'll use it | Critical |

### Typical Stakeholders
- Research Lead (primary)
- Decision Maker (primary)
- Subject Matter Expert (secondary)
- Analyst (secondary)

### Question Patterns

| Type | Research-Specific Pattern |
|------|---------------------------|
| Grand Tour | "What decision are you trying to make with this research?" |
| Structural | "How does this research fit into your broader planning process?" |
| Contrast | "How is this different from research you've done before?" |
| Example | "What would an ideal research output look like?" |
| Probing | "What level of confidence do you need to act?" |
| Devil's Advocate | "What if the research contradicts your current hypothesis?" |
| Clarifying | "When you say 'competitive landscape', which competitors specifically?" |
| Confirming | "So the key output is [X]. Is that correct?" |

### Common Assumptions to Surface
- "The data exists and is accessible"
- "Stakeholders agree on the question"
- "Timeline is realistic"
- "This research will actually change the decision"

### Confidence Traps
- Assuming stakeholders agree on the research question
- Taking stated confidence requirements literally
- Missing that "research" may be cover for delayed decision
- Assuming data access without verification

---

## 4. Requirements Domain

**Purpose:** Requirements gathering, acceptance criteria definition, scope management

### Key Concepts

| Concept | Definition | Question Focus |
|---------|------------|----------------|
| **Job Story** | User need in context | Situation, motivation, outcome |
| **Acceptance Criteria** | Definition of done | Testable conditions |
| **Constraint** | Hard limit | Must respect |
| **NFR** | Quality attribute | Performance, security, etc. |
| **Priority** | Relative importance | Must/should/nice-to-have |

### Default MECE Pattern: Custom

| Dimension | Sub-Areas | Priority |
|-----------|-----------|----------|
| **User Needs** | Job stories, personas | Critical |
| **Functional Requirements** | What it must do | Critical |
| **Non-Functional Requirements** | How well it must do it | Critical |
| **Constraints** | Technical, business, regulatory | Critical |
| **Dependencies** | External systems, teams, data | Important |

### Typical Stakeholders
- Product Owner (primary)
- End User Representative (primary)
- Technical Lead (secondary)
- QA Lead (secondary)

### Question Patterns

| Type | Requirements-Specific Pattern |
|------|------------------------------|
| Grand Tour | "What problem are we solving with this system?" |
| Structural | "Which requirements depend on others?" |
| Contrast | "What's the difference between must-have and nice-to-have?" |
| Example | "Can you walk through a scenario where this requirement matters?" |
| Probing | "What happens if this requirement isn't met?" |
| Devil's Advocate | "Could we ship without this requirement?" |
| Clarifying | "What does 'fast' mean in terms of response time?" |
| Confirming | "So the acceptance criterion is [X]. Correct?" |

### Common Assumptions to Surface
- "Users will figure it out" (training/onboarding needs)
- "Performance doesn't matter" (latency expectations)
- "Edge cases are rare" (error handling completeness)
- "This is a one-time build" (maintenance/evolution)

### Confidence Traps
- Assuming "must have" actually means must have
- Taking acceptance criteria as complete without edge cases
- Missing implicit non-functional requirements
- Conflating stakeholder wishes with user needs

---

## 5. Custom Domain

### When to Use
- Topic doesn't fit standard domains
- Interviewee specifies custom framing
- Cross-domain investigation

### Configuration

When `domain_reference: custom`, prompt for:

1. **Key concepts** - What are the main terms/ideas?
2. **MECE dimensions** - How should coverage be structured?
3. **Typical stakeholders** - Who knows about this?
4. **Critical assumptions** - What should be surfaced?

### Template

```yaml
custom_domain:
  name: "[Domain Name]"
  concepts:
    - name: "[Concept 1]"
      definition: "[What it means]"
      question_focus: "[What to ask about]"
  mece_dimensions:
    - dimension: "[Dimension 1]"
      sub_areas: ["[Area A]", "[Area B]"]
      priority: critical | important | nice_to_have
  stakeholders:
    primary: ["[Role 1]", "[Role 2]"]
    secondary: ["[Role 3]"]
  assumptions_to_surface:
    - "[Assumption 1]"
    - "[Assumption 2]"
```

---

## 6. None (Generic)

### When to Use
- Quick interview without domain setup
- Exploratory conversation
- Domain unclear at start

### Generic MECE Pattern

| Dimension | Focus | Priority |
|-----------|-------|----------|
| **Context** | Background, situation | Critical |
| **Problem** | What needs to be solved | Critical |
| **Stakeholders** | Who's involved | Important |
| **Constraints** | Limits and boundaries | Important |
| **Success** | What good looks like | Critical |

### Validation Mode
Default to `balanced` - standard verification without domain-specific rigor.

---

## Validation Mode by Domain

| Domain | Default Mode | Rationale |
|--------|--------------|-----------|
| product | balanced | Mix of qualitative and quantitative |
| architecture | rigorous | Technical claims need verification |
| research | balanced | Method matters, but not adversarial |
| requirements | empathetic | Build rapport with stakeholders |
| custom | balanced | Safe default |
| none | balanced | Safe default |

### Mode Override Conditions

**Use empathetic when:**
- Interviewee is senior executive
- Relationship is new/fragile
- Topic is sensitive

**Use rigorous when:**
- High-stakes decision
- Technical claims need verification
- Prior interview had contradictions

---

## Quick Reference

### Domain Selection

| If the topic is about... | Use Domain |
|--------------------------|------------|
| Users, features, product decisions | product |
| Systems, components, technical design | architecture |
| Questions to answer, studies to conduct | research |
| What to build, acceptance criteria | requirements |
| Something else specific | custom |
| Not sure / general | none |

### MECE Pattern Lookup

| Domain | Pattern | Dimensions |
|--------|---------|------------|
| product | Market Research | 5 |
| architecture | Technology Evaluation | 5 |
| research | Strategic Research | 5 |
| requirements | Custom | 5 |
| custom | User-defined | Variable |
| none | Generic | 5 |
