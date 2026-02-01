#!/bin/bash
# doc-lint.sh
# Checks documentation for cognitive load and style issues

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
CONTENT=$(echo "$INPUT" | jq -r '.tool_input.content // empty')

# Only check markdown files
if [[ "$FILE_PATH" == *.md ]]; then
  WARNINGS=""

  # Check for "Obviously" or "Simply" language (assumes reader knowledge)
  if echo "$CONTENT" | grep -qi '\bobviously\b'; then
    WARNINGS="${WARNINGS}Found 'Obviously' - avoid assuming reader knowledge. "
  fi

  if echo "$CONTENT" | grep -qi '\bsimply\b'; then
    WARNINGS="${WARNINGS}Found 'Simply' - what's simple to you may not be to the reader. "
  fi

  if echo "$CONTENT" | grep -qi '\bjust\b[[:space:]]\+[a-z]'; then
    WARNINGS="${WARNINGS}Found 'just [verb]' - minimizes complexity for reader. "
  fi

  # Check for passive voice indicators in instructions (should be imperative)
  if echo "$CONTENT" | grep -qi 'should be\|can be\|will be' | head -3 | grep -qi 'should be\|can be\|will be'; then
    WARNINGS="${WARNINGS}Consider using imperative voice in instructions ('Run' not 'should be run'). "
  fi

  # Check for very long code blocks without explanation
  LONG_CODE=$(echo "$CONTENT" | awk '/^```/{p=1;n=0;next} p{n++} /^```/{if(n>30)print "long";p=0}' | head -1)
  if [ "$LONG_CODE" = "long" ]; then
    WARNINGS="${WARNINGS}Found long code block (>30 lines) - consider breaking up with explanations. "
  fi

  # Check for missing headers in long documents
  LINE_COUNT=$(echo "$CONTENT" | wc -l)
  HEADER_COUNT=$(echo "$CONTENT" | grep -c '^#')
  if [ "$LINE_COUNT" -gt 100 ] && [ "$HEADER_COUNT" -lt 3 ]; then
    WARNINGS="${WARNINGS}Long document with few headers - consider adding structure. "
  fi

  if [ -n "$WARNINGS" ]; then
    echo "{\"additionalContext\":\"Documentation lint warnings: ${WARNINGS}\"}"
  fi
fi

exit 0
