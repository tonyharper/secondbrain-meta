# Risk Leads Dashboard — Status

_Last updated: 2026-04-20_

## State

Active — dashboard is live and iterating. P0 Exec Dash progress has slowed; only 1 of 5 remaining P0 metrics landed since last update.

## What's on dash

14 P0 Exec Dash metrics live (13 previous + Insufficient Evidence Rate added Apr 9), plus the Risk by PG tab (4 widgets).

## Remaining P0 metrics

| Metric | Status | Owner (DE) | Notes |
|--------|--------|------------|-------|
| Obligations Volume | Data layer built (Apr 17), **not on dashboard yet** | Nanditha Ramadurai | `digest_regulatory_obligations` table and M360 metrics created, still in test prefix. Karen Krieb reviewing. |
| Agent-driven SEVs | No evidence of progress | Claire Jin, Ashish Mangaj, Mateen Saifyan | |
| AI Researcher Friction | No evidence of landing (ETA was 4/17) | Anthony O'Sullivan | |
| Regulatory Inquiries by Risk Area | No evidence of landing (ETA was 4/15) | Karen Krieb | Karen active on Obligations Volume data layer review |

Not tracking: AI Maturity (deprioritized).

## Recent changes

- **Insufficient Evidence Rate landed** (D100042885, Apr 9) — M360 metric ME8991391, shown in Risk Management tab alongside Risk Miss Rate under "Audit Metrics"
- **M360 data integration fixed** (D100713520, Apr 14) — live Risk Miss Rate/Volume KPIs, time period selectors added
- **Vantage dashboard** being built by stephanieltam, referencing risk-leads-dashboard as the reference implementation (D101022150, D101200376)
- **Risk Org Data App launched** (Mateen Saifyan, Apr 9) — centralized Nest hub for all Risk dashboards with standardized components

## From London (Apr 20)

- Katriel: Risk Leads "did not appreciate" the controls deep dive. His read: "this is good, now stop investing here." Suggests pivoting to outcomes measurement.

## Not a concern right now

- **Alerting** — "Not Started" across all metrics. Acceptable for now.
- **P1 Foundation Dashboard** — ~20 metrics, almost all undefined. Not a priority.

## Key links

- [Live dashboard](https://risk-leads-dashboard.nest.x2p.facebook.net/)
- [Status tracker (Google Sheet)](https://docs.google.com/spreadsheets/d/192VbSiB4DlyBIBGPaTyz7RRKP65_JJwNAYrhO82qGHQ/edit?gid=0#gid=0)
- Consumer: Michel Protti (senior leadership)
- TPM: Ford McKinstry
