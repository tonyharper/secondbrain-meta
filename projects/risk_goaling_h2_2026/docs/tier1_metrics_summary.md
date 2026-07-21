# H2 2026 Tier-1 Metrics Sheet — Parsed Summary

_Source: https://docs.google.com/spreadsheets/d/1MCTfdFwYLl6VDrVthczHEd1OIQhMp1yRdjA9wY7pGFA/edit_
_Local exports: `/tmp/risk_sheet_retry.xlsx` (329KB), `/tmp/risk_sheet_html.zip` (560KB, 7 tabs), `/tmp/risk_sheet_export.csv` (44KB, first tab)_
_Parsed: 2026-07-21_
_Sheet tabs discovered:_
- H2'26 Tier-1 Metrics (1081314132) — 882 rows x 29 cols, 197 CSV lines -> 118 data rows
- H2'26 Consolidation View (1337312515)
- Risk North Star Metrics (1075425501)
- Metric Development T-Shirt Size Reference [WIP]
- Timeline (hidden)
- Items to be Completed (hidden)
- Product Goaling POC (hidden)

## High-level counts (Tier-1 Metrics tab)

**Total goal rows:** 118 (parsed from CSV, header row = row 1 in file)

**By Investment Priority:**
- 1. Meet our obligation response requirements: 26
- 2. Achieve a step-change reduction in Youth Pressure: 26
- 4. Transform our processes for AI: 58
- 3. Unblock AI launches with informed Risk trade-off: 6
- AI adoption and usefulness on platforms (ARP & GRC): 1

**By Risk Group:**
- Youth: 33
- Risk Review Systems & Platform: 18
- User Risk: 13
- AI Risk: 11
- Data Risk: 10
- Monetization Risk: 10
- GRC Product Platform: 10
- MTC: 3
- Agent Oversight: 3
- Areas Response Platform: 2

**By Type:**
- New: 43
- Ship Goal: 41
- Existing: 28

**By Metric Definition Status:**
- Finalized: 56
- Pending: 23
- In progress: 13
- Blocked: 8

**By Goal/Tracking:**
- Goal: 106
- Tracking: 7

## Data Risk slice (10 rows)

All Data Risk rows from sheet:

| Metric Name | Human language goal | Type | POC | Def Status |
|-------------|---------------------|------|-----|------------|
| % SINs under SLO | Keep SIN within SLO so as to meet regulatory deadlines | Existing | Scott Murani | Pending |
| % Requirements effective (green+yellow) | Maintain controls, address SEVs, deliver MAPs | Existing | Iva Marinkovic Bugarcic | Pending |
| % Requirements with effective self-evidencing controls (% green) | Manage risks globally with self-evidencing, self-adopting controls rather than bespoke case-by-case | Existing | Iva Marinkovic Bugarcic | Pending |
| Aligned positions for the 7 priority areas | Mature risk positions that manage internal + external pressure | Ship Goal | Baris Cem Sal | Pending |
| % controls agentic-ready | Manage risks globally with self-evidencing, self-adopting controls | New | TBD (Baris Cem Sal, interim) | Pending |
| Cost-of-compliance (Direct costs, USD) | Make controls cheaper + more sustainable; make pod operations + reporting cheap | Existing | TBD (Baris Cem Sal, interim) | Pending |
| % "Minimal" LaMas (DR filtered) | Enable AI Risk Review so the company can move fast on novel-risk products | New | Sebastian Poehlmann | Pending |
| Unnecessary SIN rate [TBD] | Enable AI Risk Review | New | Scott Murani | Pending |
| PG compliance cost ($/EY) | Reduce Privacy Wave and other Federated compliance costs. | Existing | TBD (Baris Cem Sal, interim) | Pending |
| Created company value (e.g. iRev) | Create company value where possible and appropriate. | Existing | TBD (Baris Cem Sal, interim) | Pending |

**Observations:**
- 6/10 Data Risk metrics are Pending definition — not yet Finalized.
- Heavy reliance on TBD POC (Baris Cem Sal interim) — suggests ownership still being assigned post-reorg.
- Themes: SIN SLO, self-evidencing controls, agentic-ready controls, cost, LaMa minimal rate.

## North Star Metrics tab (Risk North Star Metrics)

From HTML parse (27 rows):

| H2 Investment Priorities | North Star Metric |
|---------------------------|-------------------|
| 1. Meet our obligations | NSM1: N/A. Use ship goals. |
| 2. Transform our processes for AI | NSM2: % "Minimal" LaMas in Risk Review (auto-decisioned, not requiring manual evidencing). Guardrail |
| 3. Step-change reduction in youth pressure | NSM3: Parental Alignment (IG, US) |
| 4. AI Risk: Enable Hatch & ambient sensing while reducing and streamlining escalations | NSM4: TBD |
| 5. AI-native transformation of the org | NSM5 [Counter Metric]: AI-driven SEV volume. NSM6: [Counter Metric]: Privacy/Security Agent Inter (truncated) |

Nest: https://risk-leads-dashboard.nest.x2p.facebook.net/

## Timeline tab (appears stale — Jan-Mar 2025 dates)

Deliverable | Status | Target | Owners
Finalize level goals and metrics v1 | Complete | Jan 27, 2025 | Connie Lun, Reiko Yoshida, Kevin Bauer
Finalize level goals and metrics v2 | Not Started | Feb 14, 2025 |
Finalized metrics list for v1 dashboard signoff by Tony and Ian | Complete | Jan 27, 2025 | Tony Harper, Ian Ross
Goal targets and measurement defined for each PA team v1 | In Progress | Ongoing | Samantha Peters, Grace Li
Build out of Goals Dashboard | In Progress | Ongoing | Grace Li
Design review for v1 dashboard | Not Started | Feb 21, 2025 | Anastasia Gandrik
Final goal dashboard ready for all PAs | Not Started | Mar 14, 2025 | Grace Li, Anastasia Gandrik, Samantha Peters

**Note:** Timeline appears to be H1 2025 artifact reused — need H2 2026 timeline from foundational docs.

## Other tabs

- **Metric Development T-Shirt Size Reference [WIP]** — LOW/MEDIUM/HIGH sizing with dimensions: DURATION, COMPLEXITY, FOUNDATIONS ESTABLISHED, Definition ambiguities, logging ambiguities. WIP.
- **H2'26 Consolidation View** (899 rows x 30 cols) — not yet parsed, likely maps Tier-1 to PA teams.
- **Items to be Completed** (1001 rows, hidden) — likely backlog.
- **Product Goaling POC** — POC mapping.

## Open questions for goaling

- [ ] Why 58 rows map to "Transform our processes for AI" — is that the AI-native transformation priority? Consolidation view should clarify.
- [ ] Data Risk has 10 metrics, 6 Pending, heavy TBD ownership — needs ownership alignment.
- [ ] How does Data Risk % controls agentic-ready relate to broader Risk Review Systems & Platform 18 metrics?
- [ ] Need to cross-reference foundational docs (1U9v... and 1iSx...) once fetch unblocked — likely contain narrative for priorities 1-5 and H2 timeline.
- [ ] T-shirt sizing reference WIP — need final definition for effort estimation.

## Next steps

- [ ] Parse Consolidation View tab (extract PA team mapping, goal ownership)
- [ ] Retry Docs fetch after fixing `jf auth --skip-legacy-auth-upgrade` flow (docs API requires different token)
- [ ] Summarize foundational docs narrative once available
- [ ] Draft Data Risk H2 goals synthesis linking 10 metrics to team capacity + pod structure
- [ ] Link to `areas/data_risk/overview.md` if Data Risk team brain needs update
