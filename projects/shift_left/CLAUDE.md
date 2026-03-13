# Shift Left

**Project Tag**: `project:shift-left`

## Overview

Shift privacy into the Dataswarm development environment. Rather than applying privacy requirements reactively (after data assets are created and flagged), this project integrates Data Understanding, requirement applicability checks, and requirement application directly into the DE development workflow — triggered when `tester` is run. The mechanism is Claude skills (or similar) that hook into the development environment to surface and apply privacy requirements at authoring time.

This builds on two existing efforts:
1. The existing Shift-Left for Data Understanding program (Rich Types, UPM DataSets, privacy metadata at creation time)
2. Colin Glaes's prototype for agentic Dataswarm development with Claude (connecting code, tester, chronos, and presto)

## Current Status

**Phase**: Discovery

## Key Deliverables

| Name | Description |
|------|-------------|
| Development environment integration | Privacy checks that run as part of the `tester` workflow |
| Data Understanding at dev time | Surface what a data asset contains and what it means during development |
| Requirement applicability | Automatically determine which privacy requirements apply to each data asset |
| Requirement application | Apply applicable requirements (or guide the DE to apply them) during development |
| Claude skills / hooks | Skills or similar mechanism to power the above within Claude Code / Dataswarm |

## Key Stakeholders

| Person | Role | Team |
|--------|------|------|
| Tony Harper | Co-lead | Risk DE |
| Colin Glaes | Co-lead, Dataswarm agentic development | TODO |
| Oliver Pell | Stakeholder | TODO |
| Yiannis Papagiannis | Stakeholder | TODO |
| Alexander Ilic | Stakeholder | TODO |
| Colin Greene | Stakeholder | TODO |
| Stephanie Yee | Stakeholder | Risk PM |

## Key Documents

| Name | Description |
|------|-------------|
| [RTUP — Real Time Unified Prediction](https://docs.google.com/document/d/15mku2Nu6gqeclzYi1qpK22f3O-FfUHdZkjJSx67Vmvo/) | Design doc for Real Time UPP — entry points (Dataswarm diff time, table creation), prediction implementation strategies (SQL vs Python), application methods (code patch, codemod, agentic), and coexistence with batch UPP |
| [Realtime UPP Rich Type Suggestions](https://docs.google.com/document/d/1y0KWZJ_5uE_E4-9FQEmaU5wNG3qG5he5NlKfnr-pcho/) | Investigation into RT UPP Rich Type suggestions — only 192 suggestions (0.9% of predictions) as of 10/29, with analysis of gaps (66% already covered, infra bugs, unsupported APIs, ~27% tester coverage) and improvement opportunities |
| ["Shift-Left" for Data Understanding H1'2025](https://fb.workplace.com/groups/1380785639188244/permalink/1737163660217105/) | Existing Shift-Left program results — 99% 14-day SLA, 40% creation-time coverage for Rich Types, UPM DataSets covering 80% of Hive assets |
| [Making Dataswarm Development Autonomous with Claude](https://fb.workplace.com/groups/803837402998210/permalink/30652942740994282/) | Colin Glaes's post on agentic Dataswarm dev — connecting code, tester, chronos, presto via Claude skills |

## Open Questions

- What is the right UX for surfacing privacy requirements during development?
- How deep should the integration go — linter warnings, blocking checks, or automated fixes?
- How do we handle requirements that need human judgment vs. those that can be fully automated?
- What's the relationship to existing linter checks (e.g., Rich Types STB linter)?
- Goals and success metrics TBD

## Open Tasks

View tasks for this project:
```bash
tasks --agent-enabled search --name $USER --tag "project:shift-left"
```

## Project Files

- `docs/` - Project documentation
- `meetings/` - Meeting notes
- `analysis/` - Notebooks and data analysis
- `outputs/` - Deliverables and artifacts
