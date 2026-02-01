#!/bin/bash
# validate-xml-output.sh
# Validates XML artifact outputs match expected schemas from artifact-contracts.yaml

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
CONTENT=$(echo "$INPUT" | jq -r '.tool_input.content // empty')

# Only check .xml files
if [[ "$FILE_PATH" == *.xml ]]; then
  WARNINGS=""

  # Check for required artifact contract fields
  if ! echo "$CONTENT" | grep -q '<artifact_id>\|<id>'; then
    WARNINGS="${WARNINGS}Missing artifact_id/id field. "
  fi

  # Check for common research output elements
  if echo "$FILE_PATH" | grep -qi 'research-brief\|consolidated-report\|problem-statement'; then
    if ! echo "$CONTENT" | grep -q '<header>'; then
      WARNINGS="${WARNINGS}Missing <header> element for research artifact. "
    fi
  fi

  # Check for confidence scores in research outputs
  if echo "$CONTENT" | grep -qi 'finding\|recommendation'; then
    if ! echo "$CONTENT" | grep -qi 'confidence\|evidence_score\|epistemic'; then
      WARNINGS="${WARNINGS}Research findings should include confidence/evidence scoring. "
    fi
  fi

  if [ -n "$WARNINGS" ]; then
    echo "{\"additionalContext\":\"XML validation warnings: ${WARNINGS}Consider reviewing artifact-contracts.yaml for required schema fields.\"}"
  fi
fi

exit 0
