# Skills Factory

AI skills factory with advanced reasoning techniques for research, evaluation, and documentation.

## Quick Reference

- **Generate a skill:** Use cognitive-process-architect skill or `/generate-skill` command
- **Run expert panel:** Use expert-panel-deliberation skill or `/run-expert-panel` command
- **Research workflow:** Use create-research-brief → consolidate-research skills

## Core Libraries

Located in `core/`:
- `technique-taxonomy.yaml` — 200+ reasoning techniques
- `artifact-contracts.yaml` — Standardized I/O schemas
- `scoring-rubrics.yaml` — Evaluation algorithms
- `skill-patterns.yaml` — Workflow patterns

## Available Skills

### Meta
- **cognitive-process-architect** — Generate domain-specific skills from templates

### Evaluation
- **expert-panel-deliberation** — Multi-expert evaluation and consensus
- **generate-ideas** — Structured ideation with tournament ranking

### Research
- **create-research-brief** — Multi-LLM research prompt generation
- **consolidate-research** — Synthesize multi-source findings

### Documentation
- **create-documentation** — Diátaxis-aligned documentation

### Prompts
- **improve-prompt** — Optimize prompts for Claude

## Commands

- `/generate-skill` — Create new skill from templates
- `/run-expert-panel` — Quick expert panel invocation

## Working With This Repo

1. Skills auto-activate based on context
2. Use `/skill-name` for explicit invocation
3. Core libraries loaded on-demand via `@core/filename.yaml`
