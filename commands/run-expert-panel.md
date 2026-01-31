---
name: run-expert-panel
description: Quick invocation of expert panel deliberation
---

# Run Expert Panel Command

Quickly run an expert panel analysis.

## Usage
/run-expert-panel [topic or question to analyze]

## What This Does

1. Invokes expert-panel-deliberation skill
2. Auto-selects appropriate experts based on topic
3. Runs standard deliberation protocol
4. Returns consensus findings

## Examples
/run-expert-panel should we migrate to microservices?
/run-expert-panel evaluate our Q2 product roadmap
/run-expert-panel analyze security implications of new auth system

## Arguments

$ARGUMENTS - The topic or question for expert analysis

## Instructions

When invoked:

1. Parse the topic from $ARGUMENTS
2. Identify domain (technical, product, strategy, etc.)
3. Select 5 appropriate experts including 1 challenger
4. Execute standard deliberation (not deep)
5. Output:
   - Panel composition
   - Consensus findings
   - Key disagreements
   - Recommendation

Keep output concise - this is for quick analysis.
