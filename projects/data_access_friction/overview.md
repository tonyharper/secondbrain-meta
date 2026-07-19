# Data Access Friction / FRAPS — Overview

_Last updated: 2026-07-19_
_Source: _archive_v1_2026_07/projects/data_access_friction/CLAUDE.md_

## State

FRAPS = Friction Reduction for Agents Privacy & Security. Tony = measurement lead, dashboard owner.

v0.5 dashboard live (F1-F7 taxonomy, 6.2M traces/day, 1.58% interruption rate), v1 live early April composite view. Program At-Risk due to measurement/logging gaps.

4 workstreams: WS1 Identify/Detect/Triage, WS2 Meta CLI Friction Removal, WS3 Reduce Agent DW Friction (Tony's primary), WS4 Intern Tools.

## Key Challenge: Two-Pipeline Problem

| Pipeline | Source | Captures | Misses |
|----------|--------|----------|--------|
| Pipeline 1 Security | `fct_agent_security_traces` | ASP, ACL, input filtering, FwdProxy | DW denials, DIPS |
| Pipeline 2 DIPS | `fct_agent_execution_dpas_requests` | DW permission outcomes | Security guardrails |

Neither alone gives full picture. Pipeline 3 (privacy observability, Maharshi Jha) may need stitching.

## Stakeholders

| Person | Role |
|--------|------|
| Tony Harper | Measurement lead |
| Anisha Patel | Overall QB/TPM |
| Aaron Morris | Measurement plan author |
| Wenlong Dong | STO WS1 |
| Yanbo Xu | STO WS3 |
| Shruti Tyagi | DE trace coverage analysis |

## Key Docs (link + TLDR only)

| Name | Description |
|------|-------------|
| [FRAPS Measurement Plan](https://docs.google.com/document/d/1iHseo6oWQCXUBlc3B5b6fhUd5U3sVndwCv3Y3m8vgLA/edit) | Cross-workstream measurement framework |
| [Measurement Inventory](https://docs.google.com/document/d/1YhSddiEYoDqfVVb52xnjDfZBD226mFlH_TbTBjKW8b4/edit) | Existing artifacts, gaps |
| [Canonical OKRs](https://docs.google.com/document/d/1N5nKaNhcafg4kaxpPZdFNmZBEM5qyzFIPmsNJYs93TQ/edit) | All workstream KRs |
| [Friction Taxonomy](https://docs.google.com/document/d/1tHHY9zQpk6SJo3rX60bvdD6PfleSXXcZRWFawdZThz0/edit) | Wenlong F1-F7 taxonomy |
| [v1 FRAPS Dashboard](https://fraps-agent-friction.nest.x2p.facebook.net/) | Live dashboard |
| DPAS Coverage Gap | Only 4.5% DPAS match security traces — 94% missing artillery_trace_id |

Archived deep dives in `_archive_v1_2026_07/projects/data_access_friction/docs/`.

## Key Metrics

| Metric | Baseline | Target |
|--------|----------|--------|
| Agent Interruption Rate (DW) | 4.1% | ≤2% |
| AccessMate auto-approval | TBD | +50% |
