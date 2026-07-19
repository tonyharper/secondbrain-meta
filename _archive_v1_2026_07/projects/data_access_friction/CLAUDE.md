# Data Access Friction / FRAPS

**Project Tag**: `project:data_access_friction`
**Current Name**: FRAPS (Friction Reduction for Agents Privacy & Security)

## Overview

Originally the SPARE (Security & Privacy Access Rebalancing Effort) data access friction project, now expanded and renamed to FRAPS. The scope covers reducing agent and Tech FTE data access friction across Meta, with four workstreams:

- **WS1**: Identify, Detect, and Triage Agent Friction
- **WS2**: Meta CLI Friction Removal and Security Foundation
- **WS3**: Reduce Agent Data Access Friction (Tony's primary workstream)
- **WS4**: Reduce Intern Tools & Other Infra Access Friction

Tony's team owns the measurement and dashboard layer — building a unified FRAPS dashboard that stitches together multiple data pipelines to give leadership a single topline metric (Agent Session Interruption Rate) while enabling per-workstream tracking.

## Current Status

**Phase**: Active — v0.5 FRAPS dashboard is live with F1-F7 taxonomy deployed, producing real numbers (6.2M traces/day, 1.58% interruption rate). Program status is "At-Risk" due to measurement/logging gaps. WS1 war room ran past the Apr 16 target — taxonomy refinements still in progress. Tony leads the weekly FRAPS Measurement sync.

## Key Challenge: The Two-Pipeline Problem

The FRAPS topline requires stitching at least two separate enforcement pipelines:

| Pipeline | Source | Captures | Misses |
|----------|--------|----------|--------|
| Pipeline 1 (Security) | `fct_agent_security_traces` | ASP, ACL, input filtering, FwdProxy | DW table-level access denials, DIPS checks |
| Pipeline 2 (DIPS) | `fct_agent_execution_dpas_requests` | DW permission outcomes, DUA enforcement | Security guardrails, CLI trust checks |

Neither alone gives the full picture. A potential Pipeline 3 (privacy observability, Maharshi Jha) may also need stitching.

## Key Deliverables

| Name | Description |
|------|-------------|
| FRAPS Dashboard v0.5 | Pipeline 1 only, labeled "Security Controls Friction" (shipped) |
| FRAPS Dashboard v1 | Live as of early April — composite view |
| UBAR Metric | Unexpected Blocks to Access Rate — "bad friction" metric distinguishing reducible friction from correct security controls |
| WS3 Metrics | Agent Interruption Rate (DW), AccessMate auto-approval rate, permission wait time |

## Key Stakeholders

| Person | Role | Team |
|--------|------|------|
| Tony Harper | Measurement lead, dashboard owner | Risk DE |
| Anisha Patel | Overall QB / TPM | FRAPS |
| Aaron Morris | Measurement plan author, TPM | FRAPS |
| Wenlong Dong | STO, WS1 | S4AI |
| Can Lin | Co-STO, WS1 | AIDRE |
| Yimo Tao | STO, WS2 | Meta CLI |
| Yanbo Xu | STO, WS3 | DW |
| Hannah Wang | TPM, WS3 | DW |
| Tola Dalton | STO, WS4 | Intern Tools |
| Shane Li | TPM, WS4 | Intern Tools |
| Nick Castro | Partner | Security/SPARE |
| Dan May | Partner | Security/SPARE |
| George Schnabel | Partner | Security |
| Shruti Tyagi | DE, trace coverage analysis | Risk DE |

## Key Documents

| Name | Description |
|------|-------------|
| [FRAPS Measurement Plan](https://docs.google.com/document/d/1iHseo6oWQCXUBlc3B5b6fhUd5U3sVndwCv3Y3m8vgLA/edit) | Cross-workstream measurement framework, dashboard structure, workback plan |
| [FRAPS Measurement Inventory](https://docs.google.com/document/d/1YhSddiEYoDqfVVb52xnjDfZBD226mFlH_TbTBjKW8b4/edit) | Existing artifacts, OKRs, data sources, and gaps |
| [Canonical FRAPS OKRs](https://docs.google.com/document/d/1N5nKaNhcafg4kaxpPZdFNmZBEM5qyzFIPmsNJYs93TQ/edit) | All workstream KRs |
| [AIDRE & SPARE Impact Post](https://fb.workplace.com/groups/266626206077195/permalink/853367510736392/) | Executive summary of SPARE's impact on DW friction |
| [Data Access Friction Review - Brady Preread (3/3/26)](https://docs.google.com/document/d/13kB1O6D_HQZhZaTcYJ9EEzInXbpEihVcW-QCM0K1wa0/edit) | 2025 results (33% friction reduction), 2026 regressions, AI Agent friction, H1 plans |
| [SPARE H1 2026 Dashboard](https://www.internalfb.com/unidash/dashboard/spare/draft_spare_h1_26_goals/overview) | Legacy dashboard, maintenance mode |
| [Agent Data Access Friction Dashboard](https://agent-execution-di.nest.x2p.facebook.net/) | Early DIPS-based DW friction view (Pipeline 2) |
| [DPAS-to-Artillery Trace Coverage Gap Analysis](https://docs.google.com/document/d/1SLkhja9R-5aIRiEemUVjY5U4KFYK4g4aYzXNJ82uxmw/edit) | Shruti Tyagi's analysis (4/1/26) — only 4.5% of DPAS records match security traces. Three gaps: 94% missing artillery_trace_id, 23% with ID but no security trace, FAILED_BY_SERVER drops all trace context |
| [FRAPS Operating Rhythm](https://fb.workplace.com/groups/1948585412696066/permalink/1960331394854801/) | Meeting cadences, communication channels, escalation paths (Anisha Patel, 4/2/26) |
| [FRAPS Execution Tracker](https://docs.google.com/spreadsheets/d/1s4UtvtN9JI5fPHQfsOFM_CmAwnn2bGQG0JnrCfgrKh8/edit) | Sprint-level progress tracking |
| [WS3 Deliverables](https://docs.google.com/document/d/10J4JhD01nu_Fx8hhgMlzolom52yUg_8NQ65fequLbJ0/edit) | WS3 refined deliverables |
| [Claude Friction Dashboard](https://cc_security_sprint_dash.nest.x2p.facebook.net/#tab=prompt_friction) | Claude-specific friction view |
| [v1 FRAPS Dashboard](https://fraps-agent-friction.nest.x2p.facebook.net/) | Live FRAPS friction dashboard |
| [FRAPS Friction Taxonomy](https://docs.google.com/document/d/1tHHY9zQpk6SJo3rX60bvdD6PfleSXXcZRWFawdZThz0/edit) | Wenlong's F1-F7 taxonomy, agent heatmap, chokepoint mapping |
| [Friction Taxonomy Data Mapping](docs/friction_taxonomy_data_mapping.md) | Tony's mapping of F1-F7 to data sources — coverage assessment, attribution rules, gaps |
| [ISE Logging & Enforcement Inventory](https://docs.google.com/document/d/1GGrBevNPMjVFtIHs4nVhjPXHFby465AtlIE35iFLh58/edit?tab=t.o7ppko935rxr#bookmark=kix.31u0fm0ekwi) | ISE's enforcement logging datasets — ~25 sources across chokepoints, with agent/trace attribution status. Key datasets: bpfjailer_enforce, hipster_aclchecker_checks, ai_agent_input_filter |
| [Artillery Coverage Comparison Proposal](docs/artillery_coverage_comparison_proposal.md) | Proposal for two focused comparisons: hipster vs. artillery (F6) and bpfjailer volume (F3) |
| [FRAPS Measurement Team](docs/fraps_measurement_team.md) | Roles, ownership map, gaps, proposed ownership for war room and ongoing measurement |
| [Friction Taxonomy Data Mapping](docs/friction_taxonomy_data_mapping.md) | Tony's F1-F7 to data sources mapping — coverage assessment, attribution rules, gaps. ~50-55% of taxonomy measurable. |

## Key Data Sources

### Pipeline 1 — Security Controls
- `fct_agent_security_traces` (:security) — per-trace security control outcomes
- `fct_agent_security_sessions` (default) — per-session outcomes (V0, replaced by traces)
- `artillery_agent_platform_events` — raw Artillery logging

### Pipeline 2 — Data Access / DIPS
- `datainfra_permission_service_logger_logs` — raw DIPS logs
- `fct_agent_execution_dpas_requests` — agent data access outcomes
- `agg_agent_execution_dpas_metrics` — pre-computed rollups

### Shared
- `d_employee_plus` — employee dimension table
- `meta_cli_audit` (Scuba) — CLI trust pipeline results
- `meta_cli_telemetry` (Scuba) — CLI command telemetry
- `dim_ai_code_security` (:security) — AI-generated diff security analysis

### Legacy
- `security.fct_iam_user_friction` — original SPARE friction data (ACL: `DATA_PROJECT:oncall_security_de`)

## WS3 Key Metrics

| Metric | Baseline | Target |
|--------|----------|--------|
| Agent Interruption Rate (DW) | 4.1% | ≤2% |
| AccessMate auto-approval rate for Claude | TBD | +50% increase |
| Permission request wait time | TBD | Reduce |
| Task completion rate w/o human intervention | TBD | Track and improve |

## Open Tasks

View tasks for this project:
```bash
tasks --agent-enabled search --name $USER --tag "project:data_access_friction"
```

## Project Files

- `docs/` - Project documentation (includes measurement plan and inventory summaries)
- `meetings/` - Meeting notes
- `analysis/` - Notebooks and data analysis
- `outputs/` - Deliverables and artifacts
