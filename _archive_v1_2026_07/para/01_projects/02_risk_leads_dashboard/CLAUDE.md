# Risk Leads Dashboard

**Project Tag**: `project:risk_leads_dashboard`

## Overview

Building a dashboard to provide a clean breakdown of the cost of compliance by type (Headcount, Opex, Hardware, Federated, Non-Federated) and by cost category (Direct/Indirect), with the goal of enabling senior leadership (Michel) to understand and manage privacy compliance costs. The prototype pipeline aggregates daily compliance costs from multiple cost signal tables into a single fact table.

## Current Status

**Phase**: Prototyping — initial pipeline built via Claude Code, now being rebuilt using Semantic Models via Analytics Agent.

## Key Deliverables

| Name | Description |
|------|-------------|
| fct_compliance_cost_category_breakdown | Fact table aggregating daily compliance costs by category and type |
| Cost of Compliance Dashboard | "The Michel dash" — leadership view of privacy compliance costs |

## Key Stakeholders

| Person | Role | Team |
|--------|------|------|
| Tony Harper | Project lead | Risk DE |
| Sunil Rathode | DE support, Semantic Model for cost data | Risk DE |
| TODO | Michel (senior leadership consumer) | TODO |

## Key Documents

| Name | Description |
|------|-------------|
| [D93808202](https://www.internalfb.com/diff/D93808202) | Initial diff adding tonyharper to privacy_cost_de (Feb 2026) |
| [D93810914](https://www.internalfb.com/diff/D93810914) | Pipeline diff for fct_compliance_cost_category_breakdown (Feb 2026, abandoned in favor of D93888192) |
| [Risk Health Dashboard RFC](https://drive.google.com/a/meta.com/open?id=1xZbox7sqf5OtuVyE0vmWdk2UPquJ3shJ6d_Y-WF5cTU) | RFC for the Risk Health / Risk Leads dashboard |
| [Risk Leads Dashboard Proposal](https://drive.google.com/a/meta.com/open?id=1fuvaDL0KaxzWkQsAw9UKa1s1pD1Ugt4WvdE6zPjkUoc) | Initial proposal for Risk Leads dashboard |
| [Analytics Agent Validation](https://fburl.com/aa/121jtwpa) | Semantic Model-based replication of cost queries |
| [Risk Leads Dashboard Definition](https://docs.google.com/document/d/1YWbJwk-bW3iQlYdqHFAA6jy3pPxxoKjzCDysoSeQDqc/edit?tab=t.8nnafr41xmz4) | Dashboard definition doc |
| [Risk Leads Dashboard](https://risk-leads-dashboard.nest.x2p.facebook.net/) | Live dashboard |
| [Control Maturity Updates](https://docs.google.com/presentation/d/1cIaJhzsbEJkTZpgr8vReHqpfnZWqRYHt/edit?slide=id.p1#slide=id.p1) | Control maturity update slides |

## Data Sources

- `dim_privacy_fte_headcount_signal` + `dim_privacy_fte_headcount_costs_signal` — Headcount (PCP + PG Funded)
- `fct_privacy_opex_signal` — Opex
- `fct_privacy_hardware_cost_signal` — Hardware (Direct + Indirect)
- `fct_privacy_task_cost_signal` — Federated
- `fct_privacy_non_federated_privacy_review_signal` — Non Federated (Privacy Review)
- `fct_privacy_non_federated_privacy_program_signal` — Non Federated (Global Privacy Program)

## Open Tasks

View tasks for this project:
```bash
tasks --agent-enabled search --name $USER --tag "project:risk_leads_dashboard"
```

## Project Files

- `docs/` - Project documentation
- `meetings/` - Meeting notes
- `analysis/` - Notebooks and data analysis
- `outputs/` - Deliverables and artifacts
