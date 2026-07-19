# Quick Start — Rebuilt Work Brain (2026-07-19)

_This is the file to open tomorrow or Tuesday. Permanent copy of rebuild instructions._

## What changed

- Old system (162 files) archived to `_archive_v1_2026_07/` — dual PARA + projects, context sync pipeline with config.yaml 190 lines + manifest.yaml 300 lines, daily triage that felt like homework, no PMF. Last sync 2026-04-02.
- New system built from `personal_second_brain_analysis.md` principles: folder=domain, CLAUDE.md=contract, typed memory in memory/, sync.sh like miles/, voice protection, retrieval not archive.
- One file lost in rm: `writing/proposals/2026-06-17-user-data-risk-contribution-narrative.md` (untracked, not in Drive). Check Time Machine.
- Writing style guide renamed `writing/style.md` (was `claude.md`) to avoid macOS case collision — folder contract is `writing/CLAUDE.md`.

## Folder map (14 folders)

```
inbox/                meetings/, docs/, notes/ — quick capture, inbox zero
meetings/             YYYY_MM_DD_topic.md with Decisions/Actions
projects/             data_access_friction, shift_left, risk_data_ai_enablement — overview.md + projects.md
areas/                data_risk, user_risk, risk_de_org — team brains
people/               stephanie_yee.md, oliver_pell.md
decisions/            decision_log.md
writing/              essays, proposals, decision-docs, comms, notes — Cal proofreads only
memory/               MEMORY.md + feedback_v1_lessons.md
templates/            meeting.md, project_overview.md, etc.
daily/                YYYY_MM_DD.md morning pull scratch
reference/            key_docs.md (50+ links from old manifest, TLDR only), tool_notes.md, this file
private/              gitignored local-only, never pushed
scripts/              for future generated files
_archive_v1_2026_07/  old system, delete after 30 days
```

## Security — 3 tiers

- **Tier 1 — this repo (private GitHub, git-tracked):** scaffolding, links, summaries, non-sensitive plans, writing drafts with no restricted data. Safe if laptop lost.
- **Tier 2 — Google Drive / Docs / Workplace (enterprise-managed):** anything sensitive, A/C priv, people/performance notes with sensitive context, pod reports with user data, full doc contents. Stored in Drive, fetched on demand via `meta google.docs get --id <ID>` — NOT saved fully in repo, only link + 1-line summary.
- **Tier 3 — private/ (gitignored):** local scratch, never pushed, delete after moving to Tier 2.
- Rule: unsure → Tier 2 (link only).

## Three workflows that must earn keep (PMF test)

### Workflow 1 — Ingestion of meeting notes

```
IRL meeting happens
  -> raw dump: transcript, notes, or Google Doc paste into inbox/meetings/ as YYYY_MM_DD_source_topic.md or .txt
  -> Tell Cal: "process meeting X"
  -> Cal does:
     - read inbox file + relevant area/project CLAUDE.md
     - write meetings/YYYY_MM_DD_topic.md:
       H2 per agenda item, Context, Decisions (owner+date), Actions (owner+date), Open Threads
     - update projects/{project}/overview.md or areas/{area}/overview.md if relevant
     - update people/{person}.md if new context
     - move raw from inbox/meetings/ to processed
     - optionally update decisions/decision_log.md
```

### Workflow 2 — Ingestion of docs + team brains (Data Risk / User Risk)

```
Google Doc, Workplace post, Bento, etc.
  -> drop URL or raw into inbox/docs/ as {date}_{slug}.md with first line Source: <URL>
  -> Tell Cal: "ingest doc" or "add to team brain"
  -> Cal does (on demand, no pre-fetch 50 docs):
     - fetch via meta CLI: meta google.docs get --id <ID> --format text (or knowledge_load for Workplace)
     - summarize, extract key points, stale check
     - route to:
       - areas/data_risk/ or areas/user_risk/ if team strategy / rhythm / pod reporting
       - projects/{project}/ if specific project
       - reference/ if general knowledge
     - update area's overview.md + key_docs.md (link + 1-line summary, not full copy)
     - if decision emerges -> decisions/decision_log.md
```

Old system failed because sync was a data pipeline you triaged daily. Now on-demand only.

### Workflow 3 — Early morning context pull

```
Tell Cal: "morning pull" or "context pull for today"
Cal reads:
  daily/YYYY_MM_DD.md (if exists)
  inbox/ (what's unprocessed)
  meetings/ last 3 + next (calendar skill if available)
  areas/data_risk/overview.md + areas/user_risk/overview.md
  projects/*/overview.md + projects/*/projects.md (checkboxes)
  decisions/decision_log.md recent 7 days
  people/ for anyone in today's meetings
Cal writes daily/YYYY_MM_DD.md if not exists with:
  ## Today, ## Unprocessed, ## Meetings, ## Active threads, ## People to remember
Reports concise summary. No homework — just retrieval.
```

## Where things live now (seeds)

- `areas/data_risk/overview.md` — 11 risk areas, pod model 46 pods 3 RAGs, stakeholders Oliver/Arash/Stephanie/Yiannis, open threads from archive (DM&B dark, Forest measurement, controls takeover, Barnaby signal)
- `areas/data_risk/key_docs.md` — curated links, pod registry, Drive path
- `projects/data_access_friction/` — FRAPS measurement, v0.5 + v1 dashboards, two-pipeline problem, metrics
- `projects/shift_left/` + `risk_data_ai_enablement/` — overview + tasks
- `people/` — stephanie_yee, oliver_pell stubs
- `reference/key_docs.md` — full bibliography of 50+ docs from old sync manifest, link + TLDR only
- `reference/tool_notes.md` — how to fetch docs via meta CLI on demand
- `memory/MEMORY.md` — index, `feedback_v1_lessons.md` explains why v1 died
- `daily/2026_07_19.md` — rebuild day context, next steps checklist

## How to use tomorrow / Tuesday

1. Open this file: `reference/quick_start.md`
2. Say "morning pull" — Cal will generate daily file and surface inbox, meetings, active threads
3. Test workflow: drop a meeting transcript in `inbox/meetings/` -> "process meeting X"
4. Test workflow: drop a Google Doc URL in `inbox/docs/` -> "add to data_risk brain"
5. If folder doesn't serve morning pull after 2 weeks, delete it (miles/ rule)

## Sync

`./sync.sh` — like personal brain: git diff --name-only -> cut -d'/' -f1 dedupe -> commit `Update {folders}` -> add -A -> commit -> pull --rebase -> push. Mobile readable via GitHub web.

No rclone to Google Drive for this repo — Tier 1 only. Tier 2 stays in Drive.

## First 30 days

- Keep `_archive_v1_2026_07/` — reference for old context
- Delete after confirming nothing needed (2026-08-19, see decision_log)
- Decision logged in `decisions/decision_log.md`: archive v1, rebuild minimal, revisit 2026-08-19
