# FRAPS Weekly Update | Week of March 26, 2026

Source: [Google Doc](https://docs.google.com/document/d/1Srade6Bh7KEJ4-QmDC3tEfdR5Us4j2Jxiq8ww8iEyoQ/edit)

With - STOs + T/PMs + TBD

### Overall Status: On-Watch

Execution underway; measurement infrastructure (top-line metrics, Warehouse, Intern Tools) in progress.

### Highlights

- Kicked off FRAPS effort; initial operating rhythm established across all 4 workstreams
- Claude permissions tiger team achieved ~20% overall friction reduction (~30% bash)
- Shipped dimension based annotation system for all Meta CLI commands

Key Decisions Made

- Expanding Claude Code CLI Allowlist — Approved relaxing CLI allowlist (including phps, python3, meta CLI) to reduce friction from 12 to <1 bash interrupt/user/day (Risk already accepted under AIR1309).

## Workstream Snapshot

### WS1: Identify, Detect & Triage (On-Watch)

Owners: Wenlong Dong / Can Lin (STO) | Anisha Patel / Aaron Morris (TPM)

- Measurement: Planned working session with AIDRE on Mar 27, 2026 to align on the measurement plan.
- Claude friction reduction:
  - ~20% overall reduction so far, driven by ~30% reduction in bash friction
  - Expanded allowlist to include meta cli, phps, shell builtin like test, command -v, timeout and read only commands. We are seeing the friction trend down
  - Built metrics and [dashboard](https://cc_security_sprint_dash.nest.x2p.facebook.net/#tab=prompt_friction) to monitor friction
- Risk:
  - Potential gaps in baseline S4AI interruption count for all surfaces (eg DW has separate DIPS logs which identify permission blocks which are not in session traces).
    - Mitigation Plan: Planned deep-dives to identify gaps (Owner: Aaron Morris, Tony Harper)

### WS2: Meta CLI Security Controls (On Track)

Owners: Yimo Tao (STO) | Aaron Morris (TPM)

- Friction measurement for CLI developers and production users in-progress. Early [WS2 measurement](https://docs.google.com/document/d/1ug-skX_cbw6kGjBglxegt53cbgHfGq9ABJoBAK7AECA/edit?tab=t.0#heading=h.axffltj583dq) plan
- Shipped dimension-based [annotation system](https://docs.google.com/document/d/1MYFE9YpIP9OLds2JOnI5Dw98pjhHYHNR5VrU7AhHr9k/edit?tab=t.0) for all Meta CLI commands & [secure service users](https://docs.google.com/document/d/17DwqMneVXMC8ON7MbDbsWmTixlgx-K2gXvQlNQIfDnA/edit?tab=t.0#heading=h.c18dxrtj2cza) in sandcastle
- Upcoming:
  - [Two week sprint](https://docs.google.com/document/d/1LTYkCW3gGTOeRqVXMMTM1VGvRQWoOa2VifSa8Y1h8us/edit?tab=t.998704blzq77) to build an MVP for role-based access controls into the CLI layer

### WS3: Agent Data Access (On Track)

Owners: Yanbo Xu (STO) | Hannah Wang (TPM)

- Enable DSS-4 for Claude is on track (ETA: 3/31)
- Enable DSS-4 for Nest app: Prototyping a DVA-like solution for Nest Apps is in-progress (ETA: 4/30)
- Upcoming: Finalize friction baseline and targets for tracking and reporting purposes. Execution is ongoing in parallel

### WS4: Intern Tools & Infra (On-Watch)

Owners: Tola Dalton (STO) | Shane Li (TPM)

- System 1 and 2 rollout are on track and that's expected to reduce agent friction and we're driving forward while figuring out the metrics.
- Risk: Lack of comprehensive logging data to understand what assets agents are attempting to access and whether those requests were granted or denied. Mitigation plan: Daily war rooms to drive to clarity (ETA: Apr 9)
- MSL friction: The majority of MSL Tech FTE friction stems from highly sensitive assets currently undergoing risk reduction work. We've shared a proposal to address the highest-friction assets that fall outside the risk reduction scope and are awaiting feedback.

## Cross-Workstream Dependencies & Alignment Needed

1. **"Top agents" definition** (All workstreams) (Owner: Tony Harper)
   - Action: Establish priority agents for friction reduction focus (ETA: TBD)
2. **Session vs. trace-level metrics alignment** (WS3, WS4) (Owners: Hannah Wang, Shane Li)
   - Action: Unify measurement approach (ETA: Mar 31)
3. **CLI access rightsizing overlap** (WS2, WS4) (Owner: Tola Dalton)
   - Action: Sync on permission model (ETA: Mar 31)
4. **Intake/routing operationalization** (WS1, WS2) (Owners: Aaron Morris to work w/ Kyle, Tony)
   - Action: Discuss dedup of efforts and combining forces across 2 workstreams (ETA: TBD)

## Key Meetings & Reference Links

- [FRAPS Execution Tracker](https://docs.google.com/spreadsheets/d/1s4UtvtN9JI5fPHQfsOFM_CmAwnn2bGQG0JnrCfgrKh8/edit?gid=0#gid=0)
- [FRAPS OKRs & Workstreams](https://docs.google.com/document/d/1N5nKaNhcafg4kaxpPZdFNmZBEM5qyzFIPmsNJYs93TQ/edit?tab=t.0)
- [Claude Friction Dashboard](https://cc_security_sprint_dash.nest.x2p.facebook.net/#tab=prompt_friction)
