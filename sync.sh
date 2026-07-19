#!/bin/bash
set -e
cd "$(dirname "$0")"

# Like miles/ — low friction git backup + mobile via GitHub web
# Commit message auto-generated from changed top-level folders

# Get changed folders from staged, unstaged, untracked
CHANGED=$(git diff --name-only --diff-filter=AMDR --cached; git diff --name-only --diff-filter=AMDR; git ls-files --others --exclude-standard | cut -d'/' -f1 | sort -u)
# Extract top-level folder names
FOLDERS=$(echo "$CHANGED" | cut -d'/' -f1 | sort -u | grep -v '^\.' | grep -v '^$' | tr '\n' ',' | sed 's/,$//' | sed 's/,/, /g')

if [ -z "$FOLDERS" ]; then
  # Check if anything to commit at all
  if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    echo "No changes to sync."
    exit 0
  fi
  FOLDERS="misc"
fi

echo "Changed folders: $FOLDERS"
echo "Staging all changes..."
git add -A

echo "Committing: Update $FOLDERS"
git commit -m "Update $FOLDERS" || echo "Nothing to commit"

echo "Pulling --rebase..."
git pull --rebase || echo "Pull failed or no upstream"

echo "Pushing..."
git push || echo "Push failed"

echo "Done."
