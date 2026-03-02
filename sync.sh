#!/bin/bash
set -e

cd "$(dirname "$0")"

# Check for changes
if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
  echo "Nothing to sync — working tree is clean."
  exit 0
fi

# Build commit message from the diff summary
msg=""

# Deleted files
deleted=$(git diff --name-only --diff-filter=D)
if [ -n "$deleted" ]; then
  msg+="Remove $(echo "$deleted" | wc -l | tr -d ' ') file(s): $(echo "$deleted" | xargs -I{} basename {} | paste -sd ', ' -)"
fi

# Modified files
modified=$(git diff --name-only --diff-filter=M)
if [ -n "$modified" ]; then
  [ -n "$msg" ] && msg+="; "
  msg+="Update $(echo "$modified" | xargs -I{} basename {} | paste -sd ', ' -)"
fi

# New untracked files
added=$(git ls-files --others --exclude-standard)
if [ -n "$added" ]; then
  [ -n "$msg" ] && msg+="; "
  msg+="Add $(echo "$added" | xargs -I{} basename {} | paste -sd ', ' -)"
fi

# Staged but not yet covered (edge case: pre-staged changes)
staged_new=$(git diff --cached --name-only --diff-filter=A 2>/dev/null)
if [ -n "$staged_new" ]; then
  [ -n "$msg" ] && msg+="; "
  msg+="Add $(echo "$staged_new" | xargs -I{} basename {} | paste -sd ', ' -)"
fi

staged_mod=$(git diff --cached --name-only --diff-filter=M 2>/dev/null)
if [ -n "$staged_mod" ]; then
  [ -n "$msg" ] && msg+="; "
  msg+="Update $(echo "$staged_mod" | xargs -I{} basename {} | paste -sd ', ' -)"
fi

# Fallback
if [ -z "$msg" ]; then
  msg="Sync updates"
fi

echo "Commit message: $msg"
echo ""

git add -A
git commit -m "$msg"
git push

echo ""
echo "Synced to GitHub."
