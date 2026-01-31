---
name: create-research-brief
description: >
  Generate structured research prompts optimized for multiple LLMs (Claude Opus 4.5,
  Gemini Pro 3, GPT-5.2). PROACTIVELY activate for: (1) Create research plan,
  (2) Design multi-model research strategy, (3) Generate research prompts,
  (4) Plan market/competitive/user research, (5) Prepare for deep research.
  
  Triggers: "create research brief", "research plan", "multi-model research",
  "research prompts for", "design research strategy", "plan research for"
---

# Create Research Brief

Generate optimized research prompts for multi-LLM research workflows.

## Purpose

Design research strategies that leverage strengths of different models:
- **Claude Opus 4.5:** Nuanced analysis, synthesis, judgment
- **Gemini Pro 3:** Broad coverage, current information, citations
- **GPT-5.2 Deep:** Exhaustive research on narrow topics (when available)

## When to Use

**Ideal for:**
- Market research and sizing
- Competitive analysis
- User research synthesis
- Technology landscape mapping
- Industry trend analysis
- Regulatory research

## Workflow

### Step 1: Define Research Scope

Gather from user:
- **Research domain:** market | industry | competitive | user | technology | regulatory
- **Core question:** What specifically needs to be answered?
- **Geographic scope:** Region or global
- **Time horizon:** Current state or future outlook
- **Depth:** quick (15 min) | standard (1 hr) | deep (multi-hour)

### Step 2: Select Target Models

Default configuration:
- **Primary:** Claude Opus 4.5 + Gemini Pro 3
- **Optional:** GPT-5.2 Deep (requires explicit availability check)

Model strengths:

| Model | Best For | Prompt Optimization |
|-------|----------|---------------------|
| Claude Opus 4.5 | Synthesis, judgment, technical depth | Extended thinking, reasoning chains |
| Gemini Pro 3 | Breadth, current info, citations | Web grounding, citation requests |
| GPT-5.2 Deep | Exhaustive narrow research | Single deep-dive questions |

### Step 3: Generate Model-Specific Prompts

For each target model, create optimized prompt:

**Claude prompt structure:**
<context>
[Research context and constraints]
</context>
<task>
[Specific research task]
</task>
<output_requirements>

Format: [structured format]
Include: [required elements]
Confidence: [request confidence ratings]
</output_requirements>


**Gemini prompt structure:**
Research Task: [Clear task statement]
Requirements:

[Requirement with citation request]
[Requirement with recency emphasis]

Output Format:
[Structured format specification]
Note: Prioritize recent sources (2024-2025) and include citations.

### Step 4: Create Consolidation Guide

Provide instructions for synthesizing results:
- How to reconcile conflicting findings
- Confidence weighting by source
- Gap identification

## Output Format
```markdown
## Research Brief: [Topic]

### Research Question
[Core question being investigated]

### Scope
- **Domain:** [domain]
- **Geography:** [scope]
- **Time horizon:** [horizon]
- **Depth:** [quick/standard/deep]

---

## Prompt 1: Claude Opus 4.5

**Purpose:** [What this prompt will uncover]
```
[Complete prompt ready to copy]

Prompt 2: Gemini Pro 3 Deep Research
Purpose: [What this prompt will uncover]
[Complete prompt ready to copy]

Prompt 3: GPT-5.2 Deep (Optional)
Purpose: [What this prompt will uncover]
Note: Verify availability before using
[Complete prompt ready to copy]

Consolidation Guide
After gathering research outputs:

Reconcile findings: [How to handle conflicts]
Weight confidence: [How to weight by source]
Identify gaps: [What to look for]

Consolidation Prompt
Use this with consolidate-research skill:
[Prompt for synthesis]

## Parameters

| Parameter | Default | Options |
|-----------|---------|---------|
| `research_domain` | - | market, industry, competitive, user, technology, regulatory |
| `target_models` | claude + gemini | claude_opus_4_5, gemini_pro_3, gpt_5_2_deep |
| `depth` | standard | quick, standard, deep |
| `output_format` | prompts_with_consolidation | prompts_only, prompts_with_consolidation, full_workflow |

## Quality Gates

- [ ] Research question is specific and answerable
- [ ] Model selection matches research needs
- [ ] Prompts are model-optimized
- [ ] Consolidation guide included
- [ ] Output format specified in each prompt

## Examples

**Example: Market Research**
User: Create a research brief for AI document automation market size
Research Brief generates:

Claude prompt: Deep analysis of market segments, TAM/SAM/SOM
Gemini prompt: Current market data, recent reports, citations
Consolidation guide: How to reconcile estimates

