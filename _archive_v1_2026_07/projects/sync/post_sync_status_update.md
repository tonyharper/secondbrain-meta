# Post-Sync Status Update — Instructions for Cal

_These instructions tell Cal how to refresh project status files after every content sync._

## When to run

After every content sync (daily or as triggered). The sync produces a triage file at `sync/triage/{date}.md` and may update existing docs. This status update process should run after the sync completes and Tony has reviewed/approved triage candidates.

## What to update

### Per-project status files (`{project}/status.md`)

For each active project:

1. **Read the project's CLAUDE.md** for current context
2. **Read all docs in the project's `docs/` folder** — especially anything new since the last status update
3. **Read `tasks.md`** and extract tasks tagged to this project
4. **Read the sync triage file** for new candidates related to this project
5. **Compare against the existing `status.md`** and update:
   - **State**: has anything changed? Did something unblock, stall, or complete?
   - **Open threads**: add new threads from synced docs, remove resolved ones
   - **Stale items**: anything that was in the last status and hasn't moved is now staler. Call it out. Items that were stale last time and still haven't moved deserve stronger language.
   - **Cal's take**: re-evaluate. Don't just append — rewrite this section based on the current picture. What's changed? What new risks or opportunities emerged? What should Tony do differently than last time?
   - **Recommended next actions**: reprioritize based on what's new. Completed actions get removed. New actions get added.
6. **Update the `_Last updated:` date** at the top

### Cross-project summary (`status_{date}.md`)

Write a new dated summary (don't overwrite the old one — they serve as a history). Include:

- Updated heat map with health/urgency/leverage ratings
- Any new cross-project dependencies or conflicts surfaced by the new content
- Revised "this week" priority actions
- Carry forward unresolved structural cleanup suggestions; mark resolved ones as done

## How to approach the "Cal's take" section

This is the most important part. Don't just summarize — form opinions:

- **What's working?** Call it out so Tony can replicate the pattern.
- **What's not working?** Be direct. If a project is stalling, say so and say why.
- **What should Tony be doing that he isn't?** Look for gaps between what the docs say should happen and what tasks.md shows is actually happening.
- **What questions should Tony be asking?** Sometimes the right next action is a question, not a task.
- **What connections is Tony missing?** Look for threads across projects that should be linked but aren't.
- **What's changed since last time?** If Cal flagged something last time and it hasn't moved, escalate the language. If it has moved, acknowledge it.

## Rules

- Always read the current state of every file before updating — don't rely on memory of previous content
- Reference specific documents, tasks, and dates — not generalities
- Don't soften language over time. If something was a problem last update and it's still a problem, say so more directly, not less.
- If a project has had no changes across two consecutive syncs, explicitly flag that in the status — either the project is stable (fine) or it's being neglected (not fine). Say which one.
- Keep the format consistent across all status files — same sections, same structure
- Track patterns: if Tony consistently doesn't complete a certain type of recommended action, note the pattern and ask whether those recommendations are realistic or whether the approach needs to change
