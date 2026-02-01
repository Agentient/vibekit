#!/bin/bash
# validate-skill-placement.sh
# Warns when SKILL.md is written outside correct plugin directory structure

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Check if it's a SKILL.md file
if [[ "$FILE_PATH" == *"SKILL.md" ]]; then
  # Check if it's in correct location: plugins/<plugin>/skills/<skill>/SKILL.md
  if [[ ! "$FILE_PATH" =~ plugins/[^/]+/skills/[^/]+/SKILL\.md$ ]]; then
    echo '{"decision":"block","reason":"SKILL.md must be placed in plugins/<plugin>/skills/<skill-name>/SKILL.md for marketplace visibility. Skills outside this structure will not appear in the marketplace."}'
    exit 0
  fi
fi

# All other cases: allow
exit 0
