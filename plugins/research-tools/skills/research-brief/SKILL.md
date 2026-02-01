---
name: research-brief
description: >
  Generate multi-LLM research design with optimized prompts for each model.
  PROACTIVELY activate for: (1) research planning, (2) competitive analysis,
  (3) market research, (4) technology evaluation, (5) strategic research.
  Triggers: "research brief", "research design", "research plan", "competitive analysis",
  "market research", "multi-model research"
argument-hint: [research question]
---

# Research Brief

Generate a comprehensive research design with model-optimized prompts for multi-LLM research.

## When to Use

Use this skill when you need to:
- Design a research strategy that leverages multiple AI models
- Decompose complex research questions into MECE sub-questions
- Generate prompts optimized for Claude, Gemini, and GPT strengths
- Plan systematic research with risk assessment

## Workflow

Invoke the `create-research-brief` skill Phase 1 for: "$ARGUMENTS"

### Default Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| `research_type` | market | Default; override based on question |
| `risk_depth` | standard | Balanced risk assessment |
| `model_mode` | parallel | Run models simultaneously |
| `multi_hypothesis` | false | Enable for hypothesis-driven research |
| `expert_panel` | false | Enable for strategic decisions |

### Research Types

Select based on the research question:
- **market** - Market sizing, trends, demand analysis
- **competitive** - Competitor analysis, positioning, strategy
- **technology** - Tech evaluation, build vs buy, capabilities
- **strategic** - Strategic planning, scenario analysis, options

### Model Assignment Strategy

| Model | Strength | Best For |
|-------|----------|----------|
| Claude Opus 4.5 | Judgment, synthesis, nuance | Strategic questions, conflict resolution |
| Gemini Pro 3 | Breadth, citations, grounding | Factual lookup, comprehensive sourcing |
| GPT-5.2 Deep | Recency, depth, exhaustiveness | Technical details, edge cases |

### MECE Decomposition

The skill will decompose your research question into 5 categories following the appropriate MECE pattern:

**Market Research:**
1. Market Size & Growth
2. Market Structure & Segmentation
3. Demand Drivers & Customer Needs
4. Supply & Competition
5. Evolution & Trends

**Competitive Intelligence:**
1. Product & Capabilities
2. Customers & Positioning
3. Go-to-Market Strategy
4. Organization & Resources
5. Strategy & Trajectory

**Technology Evaluation:**
1. Capability & Performance
2. Maturity & Ecosystem
3. Fit & Integration
4. Cost & Economics
5. Risk & Governance

**Strategic Research:**
1. Current State Assessment
2. External Environment
3. Strategic Options
4. Stakeholder Considerations
5. Implementation Requirements

## Output Format

The research brief will include:

```xml
<research-brief>
  <header>
    <id>[unique identifier]</id>
    <type>[market|competitive|technology|strategic]</type>
    <objective>[research question]</objective>
  </header>

  <mece-decomposition>
    <category name="[Category 1]">
      <question>[Sub-question 1.1]</question>
      <question>[Sub-question 1.2]</question>
    </category>
    <!-- ... more categories ... -->
  </mece-decomposition>

  <model-prompts>
    <prompt model="claude" category="[assigned categories]">
      [Optimized prompt for Claude]
    </prompt>
    <prompt model="gemini" category="[assigned categories]">
      [Optimized prompt for Gemini]
    </prompt>
    <prompt model="gpt" category="[assigned categories]">
      [Optimized prompt for GPT]
    </prompt>
  </model-prompts>

  <risk-assessment depth="[quick|standard|comprehensive]">
    [Risk factors and mitigations]
  </risk-assessment>

  <next-steps>
    1. Execute prompts in each model
    2. Collect responses
    3. Run /consolidate-research with outputs
  </next-steps>
</research-brief>
```

## Quality Gates

- [ ] Research objective is clear and answerable
- [ ] MECE decomposition has no overlaps or gaps
- [ ] Each sub-question is independently researchable
- [ ] Model assignments match model strengths
- [ ] Prompts are optimized for each model's style
- [ ] Risk assessment appropriate to decision stakes
