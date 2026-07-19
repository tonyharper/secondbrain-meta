# Memory

Version-controlled typed memory. Survives compaction, model changes, migration.

Copy pattern from miles/ exactly.

## Prefixes

- `feedback_*.md` — interaction bug fixes, meta-learning about Cal's mistakes:
  Example: `feedback_meeting_flow.md` — Share background first, wait for thoughts, then write entry

- `project_*.md` — multi-month initiatives that aren't folders yet, or lessons from projects:
  Example: `project_fraps_measurement.md`, `project_data_risk_analytics_lead.md`

- `person_*.md` or `user_*.md` — deep context on frequent collaborators, manager:
  Example: `person_stephanie_yee.md` in memory (different from people/ file — memory is for Cal's behavior tuning, people/ is retrieval)

- `reference_*.md` — runbooks, MCP configs, env setup, tool notes:
  Example: `reference_python_venv.md`, `reference_kubera_mcp.md`, `reference_meta_cli.md`

- `MEMORY.md` — index with descriptions of all memory files

## Rules

- Stored in repo root `memory/` not in `~/.agent/projects/.../memory/` — survives everything
- Created when friction happens: Cal makes mistake -> write feedback_ file
- New preference emerges -> project_ or person_ file
- One file per topic, concise — not brain dump
- MEMORY.md must be updated when new memory file added

## Cal's Role

- CAN draft memory entries from interaction friction
- Must update MEMORY.md index when adding new memory file
- Should read MEMORY.md at session start for context
