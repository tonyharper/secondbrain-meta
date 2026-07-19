# FRAPS Weekly Update | Week of April 6, 2026

**Author:** Anisha Patel
**Source:** https://fb.workplace.com/groups/1948585412696066/permalink/1963028637918410/

## Overall Status: At-Risk

At-Risk, driven mainly by measurement/logging gaps. WS1 still needs a locked definition/taxonomy and a prioritized measurement plan (war room underway; ETA Apr 16). WS4 has significant observability gaps (~54% unobservable) and unresolved agent identity propagation issues (ETA: TBD).

Execution continues to progress: ~20% interruption reduction to date, expanded Meta CLI across major environments, onboarded top internal tools into System 1 with early positive signals, and established an ongoing exec comms and operating cadence.

## Highlights

- DataEx H1'26 DE survey validates agent access friction remains #1 DE pain point and main ceiling on scaling AI efficiency gains. Surfaces growing tool fragmentation (Claude Code vs Analytics Agent vs Datamate vs Devmate).
- v1 FRAPS friction dashboard live.
- ~20% overall friction reduction: 550K to ~450K interrupts/day (~12 to ~10.1 interrupts/user/day). Target: <1 interruption/user/day.
- Meta CLI rolled out across Mac, Linux (alpha), Windows, and Sandcastle.
- Onboarded top 800 highest-friction intern tools into System 1.
- First executive update shipped to Michel Protti and leads (Mar 31); bi-weekly x-org leads sync kicking off this week.

## Key Decisions

- WS2/WS4 initial alignment on permission model (AMP ACLs vs CLI permissions) completed — primary blocker for service users and bots.

## WS1: Identify, Detect & Triage

- v1 dashboard live.
- ~20% reduction in overall interruptions (~550K → ~450K/day), ~12 → ~10.1 interrupts/user/day.
- Security Plugin (agent_security_guardrails): rolling out to Central Security (~500 engineers), plan for phased company-wide rollout.
  - Known issues: deterministic checks only so far; LLM inspection not live; Haiku adds 800-900ms (plan to switch to Avocado 2B <100ms); 45-50% of tool calls may require LLM evaluation.
- Intake/routing: aligned with WS2 on extending Meta CLI intake. Requirements one-pager ETA Apr 8, v1 intake dashboard ETA Apr 15.
- Operating rhythm published.
- **Risk:** No agreed definition/taxonomy, measurement approach, or prioritization framework for "agent friction." War room kicked off (ETA: Apr 16).

## WS2: Meta CLI Security Controls

- Building Meta CLI specific dashboard into v0.5 focusing on Trust layer failures.
- BII scanning of CLI commands underway.
- Migration from hard-coded allowlist to rule-based allowlist in progress.
- Platform coverage: Mac, Linux (alpha), Windows, Sandcastle. Extending to Devmate, Confucius, serverless/FaaS (ETA: TBD).

## WS3: Agent Data Access

- DSS-4 access enablement for Claude progressing per plan.
- AccessMate integration underway.
- WS3 deliverables refined and documented.

## WS4: Intern Tools & Infra

- Closing friction visibility gaps. Two root causes identified:
  - Agent friction mirrors user friction: onboarded top 800 highest-friction intern tools into System 1, expanding to ~18K tools.
  - Broken agent identity propagation: investigating root causes.
- ~54% of agent friction unobservable due to logging gaps (MySQL = ~99% of gap). Daily war rooms on this.
- MSL friction: majority from MSL-owned assets blocked by risk mitigation.
- SIR precision/recall: 9 asset classes shared with AsM for improvement.

## Cross-Workstream Dependencies

1. "Top agents" definition (All WS) — Owner: Tony Harper, ETA: TBD
2. Session vs trace-level metrics alignment (WS3, WS4) — Owners: Hannah Wang, Shane Li, ETA: TBD
3. CLI access rightsizing overlap (WS2, WS4) — Owner: Tola Dalton, ETA: TBD
