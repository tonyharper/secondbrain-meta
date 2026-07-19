# FRAPS Measurement Plan — Cross-Workstream Framework

Author: Aaron Morris | Date: 2026-03-24 | Status: DRAFT

## TLDR

FRAPS needs a unified measurement framework that gives leadership a single topline number while enabling each workstream to track and reduce their own friction. This doc inventories what exists, what's missing, and proposes a workback plan to stand up a FRAPS dashboard.


- Topline — Agent Session Interruption Rate (S4AI's metric, already defined and dashboarded)
- Per-workstream decomposition — each WS owns a subset of the topline with their own targets
- UBAR (Unexpected Blocks to Access Rate) — proposed cross-FRAPS "bad friction" metric to distinguish reducible friction from security controls working correctly

**Metric types**: This plan tracks **outcome metrics** (agent-specific friction measurements that appear on the FRAPS dashboard) and **safety countermetrics** (guardrails to ensure friction removal doesn't create risk).


- Ship goals and process deliverables (e.g., "publish tech strategy," "ship DangerousMutateCommand") are tracked in the program plan


| **WS** | **Metric** | **Type** | **Canonical OKR** | **Baseline** | **Target** | **Data Source** |
| --- | --- | --- | --- | --- | --- | --- |
| **WS1: Identify, Detect, and Triage Agent Friction** (STO: Wenlong Dong / Can Lin; TPM: Anisha Patel, Aaron Morris) |  |  |  |  |  |  |
| WS1 | Agent Session Interruption Rate (topline) | Outcome | O1 / KR1.1 | ~1% (est. 1.8-3.2%) | Baseline per platform by EOQ1 | Composite: `fct_agent_security_traces` + `fct_agent_execution_dpas_requests` |
| WS1 | Hard Interrupt Rate Reduction (program-level) | Outcome | O4 / KR4.2 | TBD (depends on KR1.1) | 20% reduction from baseline by EOH1 | Composite pipeline |
| WS1 | % friction issues auto-detected vs manually reported | Capability | O3 / KR3.3 | 0% (100% manual today) | >50% by EOQ2 | Artillery traces + CLI telemetry + Workplace mining |
| **WS2: Meta CLI Friction Removal and Security Foundation** (STO: Yimo Tao; TPM: Aaron Morris) |  |  |  |  |  |  |
| WS2 | CLI Hard Interruption Rate (trust errors / total commands) | Outcome | O1 / KR1.1 | 0.074% (~64K/month) | <0.01% (<10K/month) | `meta_cli_telemetry` |
| WS2 | PermissionDomain trust failures (Mode 1) | Outcome | O3 / KR3.2 | ~35K/month | ≥80% reduction on confirmed platforms | `meta_cli_audit` |
| WS2 | CLI friction: expected vs unexpected (UBAR) split | Outcome | O1 / KR1.1 | Not separated | Separation live; DSS command inventory complete | `meta_cli_telemetry` + DSS annotations |
| WS2 | Agent-caused SEVs from guarded CLI commands | Counter | Countermetric | 3 known (S602335, S627178, S635106) | 0 | SEV tracker |
| **WS3: Reduce Agent Data Access Friction** (STO: Yanbo Xu; TPM: Hannah Wang) |  |  |  |  |  |  |
| WS3 | Agent Interruption Rate (DW subset) | Outcome | O2 / KR2.1 | 4.1% | ≤2% | `fct_agent_execution_dpas_requests` |
| WS3 | AccessMate auto-decision rate for Claude | Outcome | O2 / KR2.3 | TBD | +30% increase | AccessMate logs |
| WS3 | Permission request wait time | Outcome | O1 / KR1.1 | TBD | Reduce (target TBD) | DIPS / AccessMate |
| WS3 | Task completion rate w/o human intervention (session-level) | Outcome | O1 / KR1.1 | TBD | Track and improve | Session-level agent tracking (TBD) |
| **WS4: Reduce Intern Tools & Other Infra Access Friction** (STO: Tola Dalton; PM: Shane Li) |  |  |  |  |  |  |
| WS4 | Agent access friction on internal tools (% agent sessions interrupted) | Outcome | O1 / KR3 | TBD — measure in Q1 | X% reduction (TBD) | `fct_agent_security_traces` |
| WS4 | Agent access friction on other ACLs (% agent sessions interrupted) | Outcome | O1 / KR4 | TBD | X% reduction or hold steady | `fct_agent_security_traces` |
| WS4 | SIR precision/recall for top 2 asset classes (Hive, Internal Tools) | Capability | O1 / KR1 | Current SIR accuracy | ≥70% / ≥70% | SIR system |
| WS4 | Tech FTE friction hours per Tech FTE (blended human+agent) | Outcome | O2 / KR1 | 13.1 | 6.5 | MSL estimates |


**Note on WS4 Tech FTE Friction**: The 13.1→6.5 target is a blended human+agent metric inherited from SPARE. It is retained as an overall outcome goal but is *not agent-specific*. WS4's O1/KR2 (measure access friction for Tech FTE *usage of agents*) is the prerequisite to establishing a true agent-specific metric. Once agent/human friction is separated, the agent-specific metric should replace this as the primary FRAPS-tracked metric for WS4.


The core challenge: the FRAPS topline cannot come from a single data source. Security logging (fct_agent_security_traces) likely does not capture data warehouse access friction, which flows through DIPS. The topline requires stitching at least two pipelines together.

## What Exists Today

### Measurement Infrastructure

Four measurement efforts are already producing data across two distinct pipelines:


| Effort | Owner | Metric | Data Source | Coverage |
| --- | --- | --- | --- | --- |
| S4AI Observability | S4AI | % agent interactions stopped by security controls | `fct_agent_security_traces` (V1, since Mar 9) | Security friction: ASP, ACL, Input Filtering, FwdProxy |
| RE Guardrail Friction V0 | Peiyi Zhang / RE+CS | % agent sessions with guardrail errors | Artillery traces + error extraction | Security + reliability friction |
| DevInfra Error Rate | DevInfra | Agent error rate | Devmate/Claude Code telemetry | Broader errors, coding-agent focused |
| Agent Data Access Friction | DW / DIPS | Agent data access execution outcomes | `fct_agent_execution_dpas_requests` | DW permission friction (DUA enforcement, table-level access) |


### Dashboards


| Dashboard | What It Shows |
| --- | --- |
| [MVP] Agent Security Topline | 3 topline metrics: interruption rate, diffs flagged, latency. Heat map by platform x control type. |
| Agent Security Friction Deep Dive | Per-control breakdown (ASP, ACL, Input Filtering, FwdProxy). Unified controls with scanner/ACL/rule details. d/d and w/w trends. |
| Agent Data Access Friction | Early view of agent data access executions, based on logs processed by DIPS (DataInfra Permission Service). |


### Key Data Tables

Pipeline 1 — Security Controls:


| Table | Namespace | What It Contains |
| --- | --- | --- |
| `fct_agent_security_traces` | :security | Per-trace security control outcomes (V1, since Mar 9). Boolean flags: `is_asp_denial`, `is_acl_denial`, `is_input_denial`, `is_fwdproxy_denial`. Metadata arrays for ACL, ASP, and input filter details. |
| `fct_agent_security_sessions` | default | Per-session security outcomes (V0, Jan 1 to Mar 8). Replaced by traces table. |
| `artillery_agent_platform_events` | — | Raw Artillery logging. Core logging table for security measurement. |


Pipeline 2 — Data Access / DIPS:


| Table | Namespace | What It Contains |
| --- | --- | --- |
| `datainfra_permission_service_logger_logs` | — | Raw DIPS logs. Records every data access permission check. |
| `fct_agent_execution_dpas_requests` | — | Fact table for agent execution DPAS (Data Permission & Access Service) requests. Agent-specific data access outcomes. |
| `agg_agent_execution_dpas_metrics` | — | Aggregated agent execution DPAS metrics. Pre-computed rollups. |


Shared:


| Table | Namespace | What It Contains |
| --- | --- | --- |
| `d_employee_plus` | — | Employee dimension table. Used by both pipelines for user/agent attribution. |
| `meta_cli_audit` | Scuba | Meta CLI trust pipeline results per invocation. Key fields: `auth_method`, `trust_checks_json`, `dcat_environment`. |
| `meta_cli_telemetry` | Scuba | Meta CLI command telemetry, trust exceptions by platform + exception_type. |
| `dim_ai_code_security` | :security | AI-generated diff security analysis (feeds code review metric). |



## The Two-Pipeline Problem

This is the hardest part of FRAPS measurement and the P0 blocker for Tony's dashboard.

### The Problem

The FRAPS topline needs to capture all agent friction, but friction flows through at least two separate enforcement pipelines:


| Pipeline | What It Captures | What It Misses |
| --- | --- | --- |
| Security (`fct_agent_security_traces`) | ASP guardrails, input filtering, forward proxy, some ACL denials | DW table-level access denials, DIPS permission checks, possibly PAI data |
| DIPS (`fct_agent_execution_dpas_requests`) | DW data access permission outcomes, DUA enforcement | Security guardrails, CLI trust checks, non-DW friction |


Neither pipeline alone gives the full picture. George's topline dashboard uses Pipeline 1 only (1.81M guardrail denials/week, but only 124K warehouse). The Agent Data Access Friction dashboard uses Pipeline 2 only (617K DW denials/week). Combined unique friction is at least 2.3M events/week before deduplication.

### What We Don't Know Yet

1. Overlap — do ACL denials in fct_agent_security_traces (is_acl_denial=true) duplicate what's in fct_agent_execution_dpas_requests, or are they different enforcement points?
2. Join key — can you join on trajectory_session_id or trace_id across both tables, or is it a looser join on user + timestamp?
3. Coverage — what fraction of WS3's 4.1% interruption rate comes from Pipeline 1 vs Pipeline 2? If most DW friction is in DIPS, then Pipeline 1 is effectively missing WS3.
4. Privacy pipeline — does Maharshi Jha's privacy observability represent a third data source that needs stitching?
### Proposed Resolution Path

1. Tony's v0.5 dashboard (EOW) — build from Pipeline 1 (security traces) only. Label it clearly as "Security Controls Friction" not "Total FRAPS Friction."
2. Pipeline 2 investigation (next week) — examine fct_agent_execution_dpas_requests schema, confirm what it captures, check for overlap with Pipeline 1.
3. Stitching design (April) — design the composite query that unions both pipelines with deduplication logic.
4. FRAPS Topline v1 (mid-April) — composite metric live on dashboard.
### Composite Metric Formula (Draft)

`FRAPS Topline = DISTINCT(`

`    Security Interruptions from fct_agent_security_traces`

`    UNION`

`    DW Access Denials from fct_agent_execution_dpas_requests`

`    UNION (if applicable)`

`    Privacy Denials from [Maharshi's pipeline TBD]`

`)`

`/ Total Agent Sessions`


The deduplication is critical — if an agent session gets blocked at both the security layer AND the DIPS layer, it should count once in the topline, not twice.

## What's Missing — Logging Gap Inventory

### Cross-Cutting Gaps


| Gap | Impact | Owner | Status |
| --- | --- | --- | --- |
| 94.8% null `error_category` in fct_agent_security_traces | Cannot classify friction type from the topline table | Security / Artillery | Known gap, no ETA |
| `agent_identity` null rate high | Cannot attribute friction to specific agent types | Security / Artillery | [D97484689](https://www.internalfb.com/diff/D97484689) fixed parent_comms for PHP/OD; Rust thin client pending |
| Hard vs soft interrupt not distinguished | Topline counts all interrupts equally — can't isolate hard stops from HITL prompts | Security | "Not yet available in the logging in all cases" (George FAQ) |
| Claude Code friction under-reported | Missing critical errors/IDs logging | Claude Code team / Artillery | Known — Peiyi V0 flagged this |
| 3P agent platforms not covered | Artillery only covers Claude Code, Metamate, Devmate, Confucius | Artillery | Expansion planned through 2026 |
| CLI guardrails via Bpfjailer incomplete | CLI command blocks not fully captured in traces | RE | Planned for Q2 2026 |
| DW friction missing from security topline | Pipeline 1 likely does not capture DIPS-level DW access denials | Tony / DEs | P0 — the two-pipeline problem |


### WS2-Specific Gaps (Meta CLI)


| Gap | Impact | Status |
| --- | --- | --- |
| DSS command inventory incomplete | Cannot automate good/bad friction classification | In progress |
| No dCAT callers unattributed | 72% of trust exceptions can't be traced to specific agents | Investigation needed |
| Pipeline short-circuit hides downstream failures | `transport_vc` callers may have additional failures we can't see | Will surface as dCAT is adopted |


### WS3-Specific Gaps (Data Warehouse)


| Gap | Impact | Status |
| --- | --- | --- |
| Accessor identity on ACL denials missing for most data | Cannot attribute DW access denials to specific users/agents | IAM needs logging diffs |
| Deciding ACL rule type (redline vs user vs agent permission) not differentiated | Cannot split expected vs unexpected DW friction | IAM needs logging diffs |
| ACL asset information requires digging into asset attribute data | Not surfaced directly in `fct_agent_security_traces` | Structural — needs extraction |
| Agent vs human DW access not cleanly separated | Rachel Lee: "How do we delineate between Tech FTE usage vs agent usage?" | Open question |
| DIPS data not linked to security traces | Cannot create unified view without stitching design | P0 — see two-pipeline problem |


### WS4-Specific Gaps (Intern Tools)


| Gap | Impact | Status |
| --- | --- | --- |
| Agent vs human Tech FTE friction not separated | WS4 uses Tech FTE hours for both — unclear how to isolate agent-specific friction | Open question |
| Comprehensive ACL check logs missing for some asset types | Hive, Scuba, Scribe access checks may not be fully logged | Jiyun Yao investigating |
| UBAR classification infeasible at WS4 scale | Surface area too broad for per-asset expected/unexpected tagging | May need probabilistic approach |


## UBAR Framework — Expected vs Unexpected Friction

UBAR (Unexpected Blocks to Access Rate) is the proposed "bad friction" metric across FRAPS. It is the subset of the topline that represents reducible friction — blocks that shouldn't have happened.

### How UBAR Works Per Workstream


| WS | How to Classify Expected vs Unexpected | Feasibility |
| --- | --- | --- |
| WS2 (Meta CLI) | DSS command inventory: each command tagged with expected trust checks. Exceptions on expected checks = good friction. All others = UBAR. | High — enumerable commands, inventory being built |
| WS3 (Data Warehouse) | ACL denials where agent has valid DUA + appropriate role = UBAR. ACL denials due to missing DUA or redline = expected. Requires ACL rule type logging (currently missing). | Medium — blocked on IAM logging diffs |
| WS4 (Intern Tools) | SIR-predicted access that was denied = UBAR. Denials on assets outside the user's role = expected. Surface area very broad. | Low — may need to defer to overall reduction target |


### Recommendation

- WS2 implements UBAR immediately (data and classification available)
- WS3 targets UBAR after ACL logging gaps are closed (ETA: when IAM lands logging diffs)
- WS4 uses their existing Tech FTE friction target as a proxy until UBAR classification is feasible
- FRAPS dashboard shows UBAR where available, and total interruption rate where not
## Proposed FRAPS Dashboard Structure

### Page 1: FRAPS Topline

- Agent Session Interruption Rate — composite metric from Pipeline 1 + Pipeline 2, trending weekly
- Pipeline contribution — what % of topline comes from security controls vs DW access vs other
- De-averaged by agent platform — Claude Code, Metamate, Devmate, Confucius
- Hard vs soft interrupt split — when logging supports it
- Volume context — total agent sessions as denominator
- d/d and w/w trend indicators

Note: until Pipeline 2 is stitched, Page 1 will show Pipeline 1 only, clearly labeled as "Security Controls Friction."

### Page 2: Workstream Decomposition

**WS2 (Meta CLI)** — sourced from canonical FRAPS OKRs O1-O4:

- **CLI Hard Interruption Rate** — trust errors / total commands, trending w/w (O1/KR1.1). Baseline: 0.074%. Target: <0.01%.
- **PermissionDomain trust failures** — the single largest friction source (~35K/month), from `meta_cli_audit` (O3/KR3.2). Target: ≥80% reduction.
- **UBAR vs Expected split** — DSS command inventory classifies each command's expected trust checks. Exceptions on expected checks = good friction. All others = UBAR.
- **Category breakdown** — no dCAT, corp-net, genuine gap, PermissionDomain
- **Top-10 commands** — by trust failure volume
- **Agent-caused SEVs** (countermetric) — 3 known baseline, target 0
**Key levers** (tracked in program plan, not dashboarded): DangerousMutateCommand migration (O2/KR2.1), command risk classification (O2/KR2.2), RBAC design (O2/KR2.3), Mac/Linux/Sandcastle enablement (O3/KR3.1), server-side ACL enforcement (O4/KR4.3), 3P OAuth pattern (O4/KR4.1).


**WS3 (Data Warehouse)** — sourced from canonical FRAPS OKRs O1-O2, O5:

- **Agent Interruption Rate (DW)** — composite of security traces (ACL denials) + DIPS data (O2/KR2.1). Baseline: 4.1%. Target: ≤2%.
- **AccessMate auto-approval rate for Claude** — % of permission requests auto-approved without human intervention (O2/KR2.3). Baseline: TBD. Target: +50% increase.
- **Permission request wait time** — average time from request to grant for agent-initiated access (O1/KR1.1). Baseline: TBD. Target: reduce.
- **Task completion rate w/o human intervention** — % of agent sessions that complete their data access job without needing a human to intervene (O1/KR1.1). Session-level tracking for Claude. Baseline: TBD.
- **Top friction-generating tables/assets** — when ACL logging gaps are closed
**Key levers** (tracked in program plan): AccessMate for Cloud Code GA (O2/KR2.2), Table Insight + k-anonymity integration for low-risk data access (O2/KR2.4), unified dashboard ship by 4/30 (O1/KR1.2), agent traffic observability improvements (O5).


**WS4 (Intern Tools)** — sourced from canonical FRAPS OKRs O1-O2:

- **Agent access friction on internal tools** — % of agent sessions interrupted on internal tool asset class (O1/KR3). Baseline: TBD (prerequisite: O1/KR2 measurement ship). Target: X% reduction.
- **Agent access friction on other ACLs** — % of agent sessions interrupted on non-internal-tool ACLs (O1/KR4). Baseline: TBD. Target: X% reduction or hold steady.
- **SIR precision/recall for top 2 asset classes** — Hive and Internal Tools (O1/KR1). Baseline: current SIR accuracy. Target: ≥70%/70%.
- **Tech FTE friction hours** — blended human+agent metric from SPARE (O2/KR1). 13.1→6.5. Retained as overall context until agent-specific metric is available.
**Key levers** (tracked in program plan): Measure access friction for Tech FTE usage of agents — ship Q1 (O1/KR2), predictive grants (System 1) and JIT decisions (System 2) for automated agent access, centralized access management for intern tools and non-DW assets.


**Prerequisite for WS4**: O1/KR2 ("Measure access friction for Tech FTE usage of agents") must ship before WS4 can report agent-specific numbers to the FRAPS dashboard. Until then, WS4 metrics are placeholders.

### Page 3: Hotspots and Routing

- Top-N friction events — ranked by frequency across all workstreams
- Owning workstream tag — each hotspot tagged with WS2, WS3, or WS4
- Resolution status — open / in-progress / resolved
### Page 4: Logging Health

- Coverage metrics — % of agent platforms with Artillery logging
- Data quality — null rates for key fields (error_category, agent_identity, accessor_id)
- Pipeline stitching status — which pipelines are integrated into the topline
- Gap closure tracking — over time
## Workback Plan

### Phase 0.5: Tony's v0.5 Dashboard (This Week — March 28)


| Action | Owner | ETA |
| --- | --- | --- |
| Build v0.5 from Pipeline 1 (`fct_agent_security_traces`) only | Tony + DEs | Mar 28 |
| Label as "Security Controls Friction" — not total FRAPS | Tony | Mar 28 |
| WS2 measurement plan published (good/bad friction) | Aaron | Mar 28 |
| Confirm WS3 KR data sources and logging dependencies | Aaron + WS3 leads | Mar 28 |
| Confirm WS4 KR data sources and agent/human separation plan | Aaron + WS4 leads | Mar 28 |
| Reach out to Maharshi Jha on privacy observability pipeline | Aaron | Mar 28 |


### Phase 1: Pipeline 2 Investigation (Early April)


| Action | Owner | ETA |
| --- | --- | --- |
| Examine `fct_agent_execution_dpas_requests` schema and contents | Tony / DEs | Early April |
| Check overlap between Pipeline 1 ACL denials and Pipeline 2 DPAS denials | Tony / DEs | Early April |
| Identify join key across pipelines (`trajectory_session_id`, `trace_id`, or other) | Tony / DEs | Early April |
| Assess Maharshi Jha's privacy observability data for Pipeline 3 | Aaron | Early April |


### Phase 2: Dashboard V0 with Composite Metric (Mid-April)


| Action | Owner | ETA |
| --- | --- | --- |
| Design composite query stitching Pipeline 1 + Pipeline 2 | Tony / DEs | Mid-April |
| FRAPS dashboard Page 1 (composite topline) | DEs | Mid-April |
| FRAPS dashboard Page 2 — WS2 view (`meta_cli_audit` integration) | DEs + Aaron | Mid-April |
| FRAPS dashboard Page 2 — WS3/WS4 views (placeholders with targets) | DEs + WS3/WS4 leads | Mid-April |
| IAM lands logging diffs for ACL rule type differentiation | IAM team | TBD |
| Close Claude Code under-reporting gap | Claude Code team / Artillery | TBD |


### Phase 3: Dashboard V1 + UBAR (May to June)


| Action | Owner | ETA |
| --- | --- | --- |
| WS2 UBAR metric live on dashboard | DEs + Aaron | May |
| WS3 UBAR metric (if ACL logging landed) | DEs + WS3 | June |
| Hard vs soft interrupt split in topline | Security / Artillery | When logging supports it |
| Hotspots and routing view | Aaron + DEs | June |
| Logging health monitoring page | DEs | June |



## Open Questions

1. Two-pipeline overlap — do ACL denials in fct_agent_security_traces duplicate what's in fct_agent_execution_dpas_requests? This is the P0 question for Tony's DEs to answer.
2. Pipeline 3 (privacy) — does Maharshi Jha's privacy observability represent a third data source? If so, what table, and how does it relate to Pipeline 1 and 2?
3. Dashboard tooling — build on George's [MVP] Unidash, or create a separate FRAPS dashboard? Recommendation: separate dashboard that pulls from the same underlying tables, to avoid cluttering the security team's operational view.
4. UBAR adoption across WS3/WS4 — is UBAR the right frame for workstreams with very broad surface area? Alternative: just track total reduction against existing KR targets.
5. Agent vs human separation — Rachel Lee flagged this. How do we cleanly attribute interruptions to agent sessions vs human sessions in WS3/WS4 data?
6. Topline denominator alignment — George uses traces, Peiyi uses sessions/trajectories. Which denominator should the FRAPS dashboard use?
7. 3P agent platforms — current coverage excludes 3P agents. Should the FRAPS topline include or exclude these? Timeline for Artillery coverage?
8. Good friction monitoring — do we need an alert if good friction drops (i.e., security controls are being weakened)? This is the safety counterpart to UBAR reduction.
## References


| Reference | Description |
| --- | --- |
| FRAPS WS2 Measurement Plan | Companion doc — WS2-specific good/bad friction plan |
| MetaCLI Trust Exception RCA | 178K/week trust failures (up 45% WoW), 3 categories |
| Agent Security Topline Dashboard | George's [MVP] topline |
| Agent Security Friction Deep Dive | Granular controls breakdown |
| Agentic Guardrail Friction Rate V0 | Peiyi's V0 — ~1% session friction |
| George's Measurement Plan | Agent Interruption Rate definition + FAQ |
| S4AI ACL Logging Gaps | fct_agent_security_traces gaps for IAM |
| (WIP) FRAPS OKR Doc | All workstream KRs |
| FRAPS Measurement Inventory | Logging gaps, DIPS tables, and data sources |
| Agent Data Access Friction Dashboard | DIPS-based DW friction view (Pipeline 2) |



