---
name: generate-skill
description: Generate a new skill using the cognitive-process-architect
---

# Generate Skill Command

Create a new skill from templates.

## Usage
/generate-skill [description of skill needed]

## What This Does

1. Invokes cognitive-process-architect skill
2. Analyzes your requirements
3. Selects appropriate pattern and templates
4. Generates complete SKILL.md

## Examples
/generate-skill evaluation framework for API designs
/generate-skill research workflow for competitive analysis
/generate-skill documentation generator for technical specs

## Arguments

$ARGUMENTS - Description of the skill you want to create

## Instructions

When invoked:

1. Parse the skill description from $ARGUMENTS
2. Identify the task type (evaluation, research, documentation, etc.)
3. Select appropriate pattern from skill-patterns.yaml
4. Configure template parameters
5. Generate complete SKILL.md with:
   - Proper frontmatter (name, description with triggers)
   - Workflow steps
   - Parameters table
   - Output format
   - Quality gates
   - Examples

Output the generated skill and ask if user wants to save it.
