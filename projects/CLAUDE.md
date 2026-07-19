# Projects

Active work with deadlines. Each project is a folder with `overview.md` + `projects.md`.

## When to create a project

Only if it has a deadline or ships something. Ongoing responsibilities go in `areas/`, not here.

## Folder Structure per project

```
projects/{project_name}/
  overview.md — status, stakeholders, key docs, links, current threads
  projects.md — Active / On Hold / Complete with - [ ] / - [x] checkboxes
  docs/ — optional, project-specific deep dives (link, don't copy full sensitive docs)
```

## Naming

- Snake case, lowercase: `data_access_friction`, `risk_leads_dashboard`
- No dates in folder name — dates live in file names

## File Conventions

`overview.md` — 1-pager, kept current. H2: State, Stakeholders, Key Docs, Open Threads, Key Metrics if relevant.

`projects.md` — like home/renovation in miles/:
```markdown
## Active
- [ ] task — context — due

## On Hold
- [ ] task

## Complete
- [x] task — done date
```

No root `tasks.md`. Tasks live here.

## Cal's Role

- CAN draft overview structure, stakeholder tables, link curation
- CAN extract actions from meeting notes into projects.md
- Does NOT add corporate filler. Keep direct.

## Current seed projects (migrated from v1)

Start with 2-3, not all 7. Others live in archive and can be revived when active.

- `data_access_friction` — FRAPS measurement
- `shift_left` — privacy in Dataswarm
- `risk_data_ai_enablement` — AI ready data (if still active)

Create others on demand.
