# Meetings

Processed meeting notes. Retrieval focus: tomorrow's follow-ups must require yesterday's note.

## File Naming

`YYYY_MM_DD_topic.md` — lowercase, underscores. Topic = short slug of meeting purpose, not attendees.

Examples:
- `2026_07_15_fraps_measurement_sync.md`
- `2026_07_10_oliver_pell_1_1.md`

If multiple meetings same day, add suffix: `2026_07_15_fraps_measurement_sync.md`, `2026_07_15_stephanie_yee_1_1.md`

## Format

```markdown
# YYYY-MM-DD - Topic

Attendees: names
Source: inbox/meetings/raw_file.md or Google Doc link

## Context
Why this meeting happened, what was at stake.

## Agenda Items (H2 per item)
### Item name
Notes, discussion points.

## Decisions
- [ ] Decision — Owner — Date — Context/link

## Actions
- [ ] Action — Owner — Due — Context

## Open Threads
- Unresolved questions, things to follow up.
```

## Cal's Role

- CAN draft formatting, extract decisions/actions with owner+date
- CAN update projects/*/overview.md, areas/*/overview.md, people/*.md if relevant
- Does NOT invent decisions not in source — if unclear, mark as `Open Threads`

## Retrieval

Used by morning pull: last 3 meetings + any with Actions assigned to Tony.
