#!/bin/bash
# load-context.sh
# Loads research-tools context at session start

CONTEXT="Research tools available: /research-interview (knowledge elicitation), /research-brief (multi-LLM research design), /consolidate-research (synthesis), /run-research-pipeline (full workflow). Pipeline: elicit → design → execute → synthesize."

echo "{\"additionalContext\":\"${CONTEXT}\"}"
exit 0
