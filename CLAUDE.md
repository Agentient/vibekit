# Skills Factory Marketplace

AI skills marketplace with advanced reasoning techniques for research, evaluation, and documentation.

## Installation

```bash
# Add the marketplace
/plugin marketplace add owner/skills-factory

# Install individual plugins
/plugin install research-tools@skills-factory
/plugin install evaluation-tools@skills-factory
/plugin install documentation-tools@skills-factory
/plugin install prompt-tools@skills-factory
/plugin install meta-tools@skills-factory
```

## Available Plugins

### research-tools
Research workflow from knowledge elicitation to consolidated findings.

**Skills:**
- `/research-tools:research-interviewer` — Systematic knowledge elicitation with epistemic tracking
- `/research-tools:create-research-brief` — Multi-LLM research design and consolidation
- `/research-tools:consolidate-research` — Synthesize multi-source findings

**Workflow:**
```
research-interviewer → create-research-brief → consolidate-research
     (elicit)              (design)              (synthesize)
```

### evaluation-tools
Multi-expert evaluation patterns for structured analysis.

**Skills:**
- `/evaluation-tools:expert-panel-deliberation` — Multi-expert evaluation and consensus
- `/evaluation-tools:database-schema-evaluator` — 5-perspective database schema analysis
- `/evaluation-tools:generate-ideas` — Structured ideation with tournament ranking

**Commands:**
- `/evaluation-tools:run-expert-panel` — Quick expert panel invocation

### documentation-tools
Diátaxis-aligned documentation generation.

**Skills:**
- `/documentation-tools:create-documentation` — Reader-centered docs with cognitive load management
  - 4 document types: Tutorial, How-To, Explanation, Reference
  - Reader personas: Anxious Novice, Developer, Scanning Executive

### prompt-tools
Prompt engineering and optimization.

**Skills:**
- `/prompt-tools:improve-prompt` — Optimize prompts for Claude

### meta-tools
Skills for creating skills.

**Skills:**
- `/meta-tools:advanced-skill-creator` — Generate domain-specific skills from templates

**Commands:**
- `/meta-tools:generate-skill` — Create new skill from templates

## Core Libraries

Located in `core/` (shared across all plugins via symlinks):
- `technique-taxonomy.yaml` — 200+ reasoning techniques
- `artifact-contracts.yaml` — Standardized I/O schemas
- `scoring-rubrics.yaml` — Evaluation algorithms
- `skill-patterns.yaml` — Workflow patterns

## Repository Structure

```
skills-factory/
├── .claude-plugin/
│   └── marketplace.json      ← Marketplace catalog
├── plugins/
│   ├── research-tools/       ← Research workflow plugin
│   ├── evaluation-tools/     ← Evaluation patterns plugin
│   ├── documentation-tools/  ← Documentation plugin
│   ├── prompt-tools/         ← Prompt optimization plugin
│   └── meta-tools/           ← Skill generation plugin
├── core/                     ← Shared libraries
└── skills/                   ← Development staging area
```

## For Developers

### Local Testing
```bash
/plugin marketplace add ./path/to/skills-factory
/plugin install research-tools@skills-factory
```

### Creating New Skills
1. Create skill directory in appropriate plugin under `plugins/<plugin>/skills/`
2. Add `SKILL.md` with frontmatter (name, description)
3. Add supporting `references/` and `templates/` as needed
4. Test with `/plugin-name:skill-name`
