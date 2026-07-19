<!-- Source: https://fb.workplace.com/groups/1948585412696066/permalink/1960331394854801/ -->
# FRAPS Operating Rhythm: How we Run, Communicate, Escalate

**Author:** Anisha Patel
**Posted:** 2026-04-02

## TL;DR

We launched FRAPS (Friction Reduction for Agents, Privacy & Security) two weeks ago, are working on locking OKRs across all four workstreams, and are already in execution mode. This post covers how we operate: meeting cadences, communication channels, escalation paths, and where to plug in.

## Overview

AI agents are transforming how Meta engineers work — agent platforms grew 10x in 2025, and agent adoption continues to accelerate. But this growth is colliding with security and privacy controls designed for humans, creating friction that blocks agent workflows and drives users toward unsafe bypass configurations. Total access friction hours have climbed to 654K, up 25% from a 523K seasonally-adjusted baseline, with sharp regressions across Data Warehouse (+15%), Intern Tools (+41%), and Other Surfaces (+23%). At least half of this regression is agent-driven.

FRAPS was launched to systematically reduce this friction. It brings together Privacy Infra, AIDRE, Security, and ISE across four workstreams to reduce security and privacy agent friction at scale.

## Workstream Structure

Sub-workstreams of the Friction (WS2, 2a, 2b, 2c), now known as FRAPS, led by Wenlong Dong & Can Lin as STOs, with Anisha Patel serving as the overall QB.

- **STO's:** Accountable for the outcome of their workstreams
- **T/PM:** Responsible for on-time delivery and execution

## Standing Meetings

| Meeting | Who | Cadence | STO | Purpose | Related Artifacts |
|---------|-----|---------|-----|---------|-------------------|
| FRAPS - Execution Sync | All 4 workstream STOs + T/PMs | Weekly, Thurs @ 10:35 am PST | Anisha Patel | Sprint health; risks and blockers; cross-WS dependencies; decisions to track | [FRAPS Execution Tracker](https://docs.google.com/spreadsheets/d/1s4UtvtN9JI5fPHQfsOFM_CmAwnn2bGQG0JnrCfgrKh8/edit) |
| X-org Leads Review | X-org leads + All 4 WS STOs | Bi-weekly (async) | Anisha Patel | Progress against KRs; risks and decisions requiring x-org alignment; strategy updates | |
| Executive Reviews | Org Leads: Arash Nikkar, Bhavesh Mehta | Monthly (async updates), adhoc for specific topics | Anisha Patel, Wenlong Dong | Program health; milestone review; escalations; upcoming priorities | |
| WS1 Core Team Sync | WS1 working team | Weekly, Thurs @ 3:35 pm PST | Anisha Patel | Intake triage; measurement progress; routing decisions; new friction signals | |
| WS2 Meta CLI Trust | WS2 working team | Weekly | Aaron Morris | Meta CLI Trust Layer, triaging access issues for CLI, strategy discussions for authentication | |
| WS3 Agent Data Access | WS3 working team | Weekly | Hannah Wang | DW access friction metrics; AccessMate progress; auto-approval rate; risks | |
| WS4 Execution Sync | WS4 working team | Weekly | Shane Li | WS4 sprint progress; blockers; intern tools friction metrics | |
| FRAPS Measurement | x-WS Measurement team | Weekly | Tony Harper | Cross-workstream DE/DS discussing measurement, overall dashboards, and gaps in data/telemetry | |

## Written Comms

- **Weekly Updates to FRAPS Working Team** (deep dive) — Audience: FRAPS Workplace group. Purpose: detailed weekly progress, risks, x-workstream dependencies. Every Thursday.
- **Bi-weekly X-org Leads Updates** — Audience: Jonathan Bergeron (PI), Komal Mangtani (AIDRE), Simon Jones (Security) + Sushaant Mujoo (TPM Lead) + Alex Ponomarenko (PI Lead) + Can Lin (AIDRE Lead). Executive-ready FRAPS snapshot with leadership asks.
- **Monthly Executive Reviews** — Audience: Arash Nikkar, Bhavesh Mehta. Overall FRAPS health, trendlines, strategic tradeoffs.
- **Quarterly PAI Updates (WS2 only)** — Audience: Michel Protti + Leads.
- **Weekly Exec updates** — Agent Oversight reporting. Concise, high-level summary with status, key deltas, risks/asks.

## Workplace Groups

| Group | Purpose |
|-------|---------|
| [FRAPS: Friction Reduction for Agent - Privacy & Security](https://fb.workplace.com/groups/1948585412696066) | Primary group for discussions and updates |
| [Agent Security and Privacy Friction](https://fb.workplace.com/groups/1852085805453585) | Forum for employees to report agent friction |
| [Coding Agent Friction](https://fb.workplace.com/groups/aifriction) | Forum for coding agent friction reports |
| [Let's Fix Data Access Friction](https://fb.workplace.com/groups/1070155485010136/) | X-sharing with security team |
| [SPARE](https://fb.workplace.com/groups/1226112005649609) | High-signal comms, kick-off, key updates |
| [Privacy Infra FYI](https://fb.workplace.com/groups/privacyinfrafyi) | Hi-signal privacy infra comms |
| [IAM](https://fb.workplace.com/groups/844714393513051) | X-sharing with IAM |

## Key GChats

- [Canonical] FRAPS: STO + Leads Working Group (WS STOs + T/PMs + DS)
- Agent Access Friction Tiger Team
- FRAPS: T/PMs (PM + TPM coordination)

## Escalation Flow

- **L0:** WS STOs
- **L1:** FRAPS STOs + QB (Wenlong Dong, Can Lin, Anisha Patel)
- **L2:** Org Leads (Simon Jones, Jonathan Bergeron, Komal Mangtani, Alex Ponomarenko, Sushaant Mujoo)
- **L3 [TBD]:** Agentic Oversight POD Leads++ (Aleksandar Ilic, Arash Nikkar, Bhavesh Mehta)

## References

- [FRAPS Canonical Doc](https://docs.google.com/document/d/1N5nKaNhcafg4kaxpPZdFNmZBEM5qyzFIPmsNJYs93TQ/edit) — source of truth for strategy, OKRs, and operating details
- [Execution Tracker](https://docs.google.com/spreadsheets/d/1s4UtvtN9JI5fPHQfsOFM_CmAwnn2bGQG0JnrCfgrKh8/edit) — sprint-level progress tracking
