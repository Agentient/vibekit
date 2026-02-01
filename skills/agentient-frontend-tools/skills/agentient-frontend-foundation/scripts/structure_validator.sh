#!/usr/bin/env bash
# Structure Validator Hook for Next.js 14+ Projects
# Validates Next.js project structure adheres to conventions
# Exit Code 2 blocks execution on violation

set -euo pipefail

# Extract file path from tool input (handles JSON input from PreToolUse hook)
FILE_PATH="${1:-}"

if [ -z "$FILE_PATH" ]; then
  # No file path provided, skip validation
  exit 0
fi

# Check if we're in a Next.js project (has package.json with next dependency)
if [ ! -f "package.json" ]; then
  # Not a Next.js project, skip validation
  exit 0
fi

if ! grep -q '"next"' package.json 2>/dev/null; then
  # No Next.js dependency found, skip validation
  exit 0
fi

# Validation errors array
ERRORS=()

# === VALIDATION 1: Prevent /pages directory (legacy Pages Router) ===
if [[ "$FILE_PATH" == *"/pages/"* ]] && [[ "$FILE_PATH" != *"/node_modules/"* ]]; then
  ERRORS+=("❌ BLOCKED: Using legacy /pages directory is not allowed.")
  ERRORS+=("   Next.js 14+ projects must use the App Router (/app directory).")
  ERRORS+=("   File: $FILE_PATH")
  ERRORS+=("   Solution: Move this file to the /app directory structure.")
fi

# === VALIDATION 2: Ensure App Router files are in /app (not /src/pages) ===
if [[ "$FILE_PATH" == *"/src/pages/"* ]]; then
  ERRORS+=("❌ BLOCKED: Files should be in /src/app, not /src/pages.")
  ERRORS+=("   File: $FILE_PATH")
  ERRORS+=("   Solution: Move to /src/app directory.")
fi

# === VALIDATION 3: Check for legacy data fetching methods ===
if [[ "$FILE_PATH" == *".tsx" ]] || [[ "$FILE_PATH" == *".ts" ]]; then
  if [ -f "$FILE_PATH" ]; then
    if grep -q "getStaticProps\|getServerSideProps\|getInitialProps" "$FILE_PATH" 2>/dev/null; then
      ERRORS+=("❌ BLOCKED: Legacy data fetching methods detected in $FILE_PATH")
      ERRORS+=("   Methods like getStaticProps, getServerSideProps, getInitialProps are not allowed in App Router.")
      ERRORS+=("   Solution: Use async Server Components for data fetching.")
    fi
  fi
fi

# === VALIDATION 4: Warn about 'use client' in page.tsx or layout.tsx ===
if [[ "$FILE_PATH" == *"/page.tsx" ]] || [[ "$FILE_PATH" == *"/layout.tsx" ]]; then
  if [ -f "$FILE_PATH" ]; then
    if grep -q "'use client'" "$FILE_PATH" 2>/dev/null; then
      ERRORS+=("⚠️  WARNING: 'use client' found in $FILE_PATH")
      ERRORS+=("   This forces the entire route to be client-rendered.")
      ERRORS+=("   Recommendation: Keep page/layout as Server Component and create separate Client Components for interactive parts.")
    fi
  fi
fi

# === VALIDATION 5: Check tsconfig.json has strict mode (if being written) ===
if [[ "$FILE_PATH" == *"tsconfig.json" ]]; then
  if [ -f "$FILE_PATH" ]; then
    if ! grep -q '"strict":\s*true' "$FILE_PATH" 2>/dev/null; then
      ERRORS+=("❌ BLOCKED: tsconfig.json must have \"strict\": true")
      ERRORS+=("   File: $FILE_PATH")
      ERRORS+=("   Solution: Add \"strict\": true to compilerOptions in tsconfig.json")
    fi
  fi
fi

# === OUTPUT RESULTS ===

if [ ${#ERRORS[@]} -gt 0 ]; then
  echo "" >&2
  echo "════════════════════════════════════════════════════════════" >&2
  echo "  NEXT.JS 14+ PROJECT STRUCTURE VALIDATION FAILED" >&2
  echo "════════════════════════════════════════════════════════════" >&2
  echo "" >&2

  for error in "${ERRORS[@]}"; do
    echo "$error" >&2
  done

  echo "" >&2
  echo "Fix the issues above before proceeding." >&2
  echo "For project structure guidelines, see the nextjs-project-scaffolding skill." >&2
  echo "════════════════════════════════════════════════════════════" >&2
  echo "" >&2

  # Exit with code 2 to BLOCK execution
  exit 2
fi

# All validations passed
exit 0
