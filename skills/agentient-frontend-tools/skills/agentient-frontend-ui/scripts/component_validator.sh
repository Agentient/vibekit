#!/usr/bin/env bash
# Component Validator - Enforces shadcn/ui and RSC best practices
set -euo pipefail

FILE_PATH="${1:-}"
[ -z "$FILE_PATH" ] && exit 0

ERRORS=()

# Check for 'use client' in page/layout files
if [[ "$FILE_PATH" == *"/page.tsx" ]] || [[ "$FILE_PATH" == *"/layout.tsx" ]]; then
  if [ -f "$FILE_PATH" ] && grep -q "'use client'" "$FILE_PATH" 2>/dev/null; then
    ERRORS+=("⚠️  WARNING: 'use client' in $FILE_PATH")
    ERRORS+=("   Keep page/layout as Server Components. Extract interactive parts to separate Client Components.")
  fi
fi

# Check for hardcoded colors instead of theme variables
if [[ "$FILE_PATH" == *".tsx" ]] && [ -f "$FILE_PATH" ]; then
  if grep -qE "bg-(red|blue|green|yellow|purple|pink|indigo)-[0-9]" "$FILE_PATH" 2>/dev/null; then
    ERRORS+=("⚠️  WARNING: Hardcoded color utilities in $FILE_PATH")
    ERRORS+=("   Use semantic theme variables (bg-primary, text-destructive) instead.")
  fi
fi

if [ ${#ERRORS[@]} -gt 0 ]; then
  echo "" >&2
  echo "════════════════════════════════════════════════" >&2
  echo "  UI COMPONENT VALIDATION WARNINGS" >&2
  echo "════════════════════════════════════════════════" >&2
  for error in "${ERRORS[@]}"; do
    echo "$error" >&2
  done
  echo "════════════════════════════════════════════════" >&2
fi

exit 0
