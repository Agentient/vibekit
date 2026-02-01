#!/usr/bin/env bash
# Firebase Command Validator - Prevents destructive Firebase CLI operations
# Exit Code 2 blocks execution on dangerous command

set -euo pipefail

# Extract command from tool input (handles JSON input from PreToolUse hook)
COMMAND="${1:-}"

if [ -z "$COMMAND" ]; then
  # No command provided, allow
  exit 0
fi

# Check if this is a Firebase CLI command
if [[ ! "$COMMAND" =~ ^firebase ]]; then
  # Not a Firebase command, allow
  exit 0
fi

# Validation errors array
ERRORS=()

# ========================================================================
# DANGEROUS COMMANDS DENY-LIST
# ========================================================================

# === VALIDATION 1: Prevent project deletion ===
if [[ "$COMMAND" =~ firebase[[:space:]]+(projects:delete|project:delete) ]]; then
  ERRORS+=("❌ BLOCKED: Firebase project deletion is not allowed.")
  ERRORS+=("   Command: $COMMAND")
  ERRORS+=("   This would permanently delete the Firebase project.")
fi

# === VALIDATION 2: Prevent Firestore data deletion ===
if [[ "$COMMAND" =~ firebase[[:space:]]+firestore:delete.*--all-collections ]]; then
  ERRORS+=("❌ BLOCKED: Deleting all Firestore collections is not allowed.")
  ERRORS+=("   Command: $COMMAND")
  ERRORS+=("   This would permanently delete all data in Firestore.")
fi

# === VALIDATION 3: Prevent Storage bucket deletion ===
if [[ "$COMMAND" =~ firebase[[:space:]]+storage:delete.*--recursive ]]; then
  ERRORS+=("❌ BLOCKED: Recursive Storage deletion is not allowed.")
  ERRORS+=("   Command: $COMMAND")
  ERRORS+=("   This would permanently delete all files in Storage.")
fi

# === VALIDATION 4: Warn about force deploy to production ===
if [[ "$COMMAND" =~ firebase[[:space:]]+deploy.*--force ]]; then
  # Check if targeting production project (customize this list)
  if [[ "$COMMAND" =~ -P[[:space:]]+(prod|production|main) ]] || grep -q '"default".*"prod"' .firebaserc 2>/dev/null; then
    ERRORS+=("⚠️  WARNING: Force deploy to production project detected.")
    ERRORS+=("   Command: $COMMAND")
    ERRORS+=("   Recommendation: Deploy without --force flag for safety.")
    ERRORS+=("   Proceeding with caution...")
  fi
fi

# === VALIDATION 5: Prevent deletion of Functions ===
if [[ "$COMMAND" =~ firebase[[:space:]]+functions:delete ]]; then
  ERRORS+=("❌ BLOCKED: Deleting Cloud Functions via CLI is not allowed.")
  ERRORS+=("   Command: $COMMAND")
  ERRORS+=("   Use Firebase Console for function deletion.")
fi

# === VALIDATION 6: Prevent Auth user deletion (bulk) ===
if [[ "$COMMAND" =~ firebase[[:space:]]+auth:import.*--delete ]]; then
  ERRORS+=("❌ BLOCKED: Bulk user deletion is not allowed.")
  ERRORS+=("   Command: $COMMAND")
  ERRORS+=("   This would delete all existing users before import.")
fi

# ========================================================================
# OUTPUT RESULTS
# ========================================================================

if [ ${#ERRORS[@]} -gt 0 ]; then
  echo "" >&2
  echo "════════════════════════════════════════════════════════════" >&2
  echo "  FIREBASE COMMAND VALIDATION FAILED" >&2
  echo "════════════════════════════════════════════════════════════" >&2
  echo "" >&2

  for error in "${ERRORS[@]}"; do
    echo "$error" >&2
  done

  echo "" >&2
  echo "For safety, this command has been blocked." >&2
  echo "If you need to perform this operation:" >&2
  echo "  1. Use the Firebase Console (https://console.firebase.google.com)" >&2
  echo "  2. Or manually run the command in your terminal after review" >&2
  echo "════════════════════════════════════════════════════════════" >&2
  echo "" >&2

  # Exit with code 2 to BLOCK execution
  exit 2
fi

# All validations passed
exit 0
