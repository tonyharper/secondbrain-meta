# CLAUDE.md

This file provides context for Claude Code when working in this workspace.

## About Me

**Tony Harper** - Director, Data Engineering at Meta

- **Team**: Risk Product Management
- **Manager**: Stephanie Yee
- **Started**: 2018-05-14
- **Location**: Menlo Park, USA

**Background**: Tony leads Risk Data Engineering, supporting data engineering across Risk domains (Privacy, Integrity, Security). Risk DE is the amalgamation of four organizations, with 6 direct reports spanning teams in Menlo Park, NYC, and London. Prior roles include FB App Data Engineering, Privacy DE, and the Better DE program. Tony writes for two audiences: engineering teams (depth, tradeoffs, concrete artifacts) and senior leadership (context, recommendation, why it matters).

---

## Persistence

This workspace lives on your local machine at `~/secondbrain/para`, synced via Google Drive for Desktop.
Changes are saved automatically. No manual sync needed.

---

## Directory Structure (PARA Method)

```
~/secondbrain/para
├── CLAUDE.md                    # This file (root context)
│
├── 00_inbox/                    # Unsorted items, quick capture
│   ├── meetings/                # Meeting notes
│   ├── notes/                   # Quick notes
│   └── incubator/               # Ideas not ready to start yet
│
├── 01_projects/                 # Active work with deadlines
│
├── 02_areas/                    # Ongoing responsibilities
│   └── hpms/                    # Highlights, Priorities, Me
│
├── 03_resources/                # Reference material
│   └── people/                  # Colleague notes
│
└── 04_archives/                 # Completed/inactive items
```

---

## File Naming Conventions

Conventions optimized for AI agent discoverability and consistency.

| Type            | Convention               | Example                      |
| --------------- | ------------------------ | ---------------------------- |
| PARA folders    | Zero-padded prefix       | `01_projects/`, `02_areas/`  |
| Project folders | Zero-padded prefix       | `01_my_project/`             |
| Files           | `snake_case`             | `sql_queries.md`, `brief.md` |
| Dated files     | `YYYY_MM_DD_description` | `2025_08_12_meeting.md`      |
| HPMs            | `YYYY_MM_DD`             | `2025_08_04.md`              |
| People          | `firstname_lastname`     | `manager_name.md`            |
| Incubator ideas | `YYYY_MM_DD_idea_name/`  | `2026_02_03_runbook_validation/` |
| Standard files  | Reserved names           | `CLAUDE.md`, `brief.md`      |

**Rules:**

- No spaces in filenames (use underscores)
- All lowercase
- Zero-padded numbers for sorting (01, 02, not 1, 2)
- Dates as YYYY_MM_DD (with underscores)
- Each project and PARA folder has a `CLAUDE.md`

---

## Task Management

All tasks are tracked in **Meta Tasks** (source of truth). Use the `tasks` skill for all task operations.

### Tagging Convention

| Tag Type      | Format                            | Example                       |
| ------------- | --------------------------------- | ----------------------------- |
| Project       | `project:{slug}`                  | `project:my-project`          |
| Area          | `area:{name}`                     | `area:career`                 |
| Agent-created | `taskscli-agent-mutation-enabled` | (auto-added)                  |

### Common Operations

```bash
# List my open tasks
tasks --agent-enabled search --name $USER

# Tasks for a specific project
tasks --agent-enabled search --name $USER --tag "project:{slug}"

# Create a task
tasks --agent-enabled create --quick \
  --title "Task title" \
  --tag "project:{slug}" \
  --pri mid

# Close a task
tasks --agent-enabled close T123456
```

---

## Active Projects

| # | Project | Description |
|---|---------|-------------|
| 01 | [risk_data_ai_enablement](01_projects/01_risk_data_ai_enablement/CLAUDE.md) | Making Risk data AI-ready with Semantic Models, Repo Context, and evals |
| 02 | [risk_leads_dashboard](01_projects/02_risk_leads_dashboard/CLAUDE.md) | Risk Leads dashboard for senior leadership |
| 03 | [risk_de_org_management](01_projects/03_risk_de_org_management/CLAUDE.md) | Org structure, performance, hiring, and team leadership |
| 04 | [data_access_friction](01_projects/04_data_access_friction/CLAUDE.md) | Reducing data access friction via SPARE initiative |
| 05 | [shift_left](01_projects/05_shift_left/CLAUDE.md) | Shifting privacy requirements into the Dataswarm development environment via Claude skills |

---

## Completed Projects

| # | Project | Description |
|---|---------|-------------|
| 01 | [ogre_migration](04_archives/01_ogre_migration/CLAUDE.md) | Migration from Compliance Graph to OGRE |
| 02 | [dashboard_quality](04_archives/02_dashboard_quality/CLAUDE.md) | Raising the bar for Risk DE dashboards |
| 03 | [rid_adoption](04_archives/03_rid_adoption/CLAUDE.md) | RID adoption for Half-Life privacy compliance |
| 04 | [risk_data_sevs](04_archives/04_risk_data_sevs/CLAUDE.md) | SEV process and IMOC rotation for Risk data |
| 05 | [risk_review_dashboards](04_archives/05_risk_review_dashboards/CLAUDE.md) | Risk Review Health and Operational dashboards |

---

## Custom Slash Commands

- `/capture-idea` - Capture a project idea for incubation. Creates a date-prefixed folder in `00_inbox/incubator/` with CLAUDE.md. Use `/add-context` to accumulate more context over time, then `/start-project` when ready.
- `/start-project` - Start a new project. Gathers context via brain dump, runs deep research for related resources, creates project folder structure with CLAUDE.md, and updates root.
- `/generate-hpm` - Generate HPM using deep research to discover your recent work (posts, docs, diffs, notebooks). Auto-detects time window from last HPM, shows discovered content for review, generates single version with iteration.
- `/prepare-meeting` - Research a person/team/project using deep research, link to your active projects, and generate a focused 30-min meeting agenda with private background notes.
- `/add-context` - Universal context ingestion. Paste any URL (Google Doc, Workplace post, Diff, Task, Bento, Chats) or text (meeting notes, decisions) and it routes to the right project, updating the appropriate CLAUDE.md sections.
- `/archive-project` - Archive a completed project. Runs deep research to find related docs/posts, updates CLAUDE.md files, and moves folder to archives.
- `/recap` - Generate weekly work recap for PSC. Searches for diffs, posts, tasks closed, and thanks received, then saves to weekly_recaps folder. REQUIRED: Run `/eng-psc-writer` afterward to update PSC draft.
- `/post-to-workplace` - Post messages to Workplace groups via bot. Resolves group names to IDs automatically. Requires `workplace-posts` skill.

---

## Available Skills

Skills are specialized capabilities bundled with the PARA workspace plugin. Invoke with the Skill tool.

| Skill                | Description                                                                 | When to Use                                                                                                                                                        |
| -------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `tasks`              | Comprehensive Meta Tasks management including viewing, searching, creating, updating, and closing tasks | **Use for ALL task operations.** Source of truth for task tracking. Create tasks with project tags, close when complete, search by project.                        |
| `deep-research`      | Advanced multi-agent research system for Meta's codebase and infrastructure | **Use for any complex research request.** Spawns multiple subagents for comprehensive analysis across code patterns, diffs, build systems, or data infrastructure. |
| `calendar`           | Query Meta's internal calendar for meetings and events                      | When checking schedule, meetings, availability, or preparing for meetings.                                                                                         |
| `google-docs`        | Read and write Google Docs                                                  | When exporting markdown/text to Google Docs format or reading Google Doc contents.                                                                                 |
| `google-sheets`      | Read and write Google Sheets                                                | When working with spreadsheet data, creating or updating Google Sheets.                                                                                            |
| `gchat` (optional)   | Read and send Google Chat messages                                          | When using `/add-context` with Google Chat thread URLs. Requires separate installation.                                                                            |
| `workplace-posts` (optional) | Post messages to Workplace groups via bot                            | When using `/post-to-workplace` to share updates with Workplace groups. Requires separate installation.                                                           |

**Important:** When you ask for "deep research" or comprehensive investigation across the codebase, Claude should use the `deep-research` skill which spawns specialized subagents for thorough multi-perspective analysis.

---

## AI Agent Instructions

- Be direct and concise. Avoid unnecessary words.
- Ask clarifying questions before making assumptions.
- Be proactive. Suggest improvements and anticipate needs.
- No flattery or excessive agreement. Challenge flawed ideas.
- When working on a project, read the project-level CLAUDE.md first.
- When linking documents, posts, or notebooks, use a table with two columns:
  - **Name**: Markdown link format `[name](url)`
  - **Description**: Brief description of contents so agents know whether to open the link
- Files in this workspace are saved directly to Google Drive — no manual sync needed.

### Task Management Behaviors

- **At session start**: Fetch open tasks using the `tasks` skill and present a summary
- **When action items are identified**: Propose creating tasks but wait for user confirmation before creating
- **When closing tasks**: Add a brief completion comment explaining what was done
- **Use project tags consistently**: Always use `project:{project-slug}` format for project-related tasks
