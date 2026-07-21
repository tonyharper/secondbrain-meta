# Flywheel Metrics Readiness + Verified Days — Summary

## Flywheel Metrics Readiness

_Source: https://docs.google.com/document/d/1hvqh8HJPH_OjRFm75rcZYdQa0aUKSW-OSN1JY5uWU8w/edit_
_Title: Flywheel metrics readiness for Risk Areas: what you need to know_
_POC: Fernando Bartolo (fbartolo@meta.com), Last update 2026-01-26_
_Local: /tmp/flywheel_metrics.md 109 lines_
_Full tracker: https://docs.google.com/spreadsheets/d/1BQPgsZ89Q8lEfB4f0baWAK1_v5ogdbEHndWcBtQv47M/edit_

**Purpose:** Provide clarity on metric readiness for Areas roadmapping. Includes most metrics in Goal Map https://docs.google.com/document/d/1zFGsABSryS2dT8KwebAoX1BEropg29VIyRFVmlb7D8o/edit (e.g., does not include Value metrics or Regulatory Response Decisions).

**Definitions:**
- V0 = query based not fully productionized – temporary metric but if listed can be used.
- V1 = in M360 calculated via pipeline fully productionized typically more resilient/reliable.

**Metrics list (from Goal Map):**
- % Assisted Self-Cert as crawl metric for Efficiency until % Regrettable Triage more mature (not before 2026) – No RA attribution, dashboard Risk Review Health https://fburl.com/datainsights/w0kua05q
- EO N/A Rate* Foundations DE Javier Abascal – Tech audit refactoring, updated metric expected week Dec 15, should map to RA (linked to requirement), no Flywheel dashboard, Areas DEs will build metric.
- % Requirements usable in Risk Review [definition https://docs.google.com/document/d/1ZSA6ApGMrnRDfDCgUeZx8yJ7aC5kU9TdfPlq3g-UeT8/edit] – V0 expected Nov 14, All metrics should have clear RA attribution, Temporary Requirements dash https://fburl.com/unidash/s293gwrt
- % Requirements meeting minimum bar [definition same] – V0 expected Nov 14.
- Other V0 expected Nov 14, Expected Nov, Meet 100% SLOs P0 mature requirement tasks Expected Nov, All metrics clear RA attribution, Metric clear RA attribution Areas Optimal Controls dash https://fburl.com/datainsights/8ghxqrh9
- % reviews with evidence duration <1d,5d,10d L28 approved reviews – V0 available, No RA attribution, Risk Review Operational dash https://fburl.com/datainsights/4xj1qcls
- % EO survey respondents reporting top 2 highest effort levels per RA – Timeline TBD, clear RA attribution.
- # MAPs V0 live MAPs dash https://fburl.com/unidash/go9w1v79 (crossed out maybe deprecated)
- # Severity-weighed SEVs V0 live Expected RA mapping SEVs dash https://fburl.com/datainsights/rpsova80
- Evidence Bars for response plan STO TBC
- PA & PAI Control Investment (Eng Year $) TBC, PG Compliance Cost Federated Tasks TBC
- Audit failure rate automated reviews [definition https://docs.google.com/document/d/1mtXG_LLxz4345ImETC2OJTb8xUgNU84kqixLtEafS8M/edit] – V1 live Can be filtered by risk factors map to RAs
- No T&E Rate V0 live (dashboard shows triage rate) No RA attribution Risk Review Process funnel https://fburl.com/unidash/ptszujde
- Canonical deep dive dashboards in production v0, some RA attribution, posts https://fb.workplace.com/groups/1167810663557228/posts/2705281033143509, dashboard https://fburl.com/unidash/33lccwxm
- NMI (Need more information) rate Expected Nov No RA attribution
- SIN metrics 1st version available expect stabilization WIP dashboard https://fburl.com/unidash/z78m7ea3
- Lama-initiated triage completed without escalation Available dashboard https://fburl.com/datainsights/gkp523o3

**Changelog:** Jan 26 Added SIN metrics Triage without Escalation, Dec15 temporary query Triage without Escalation, Dec10 timeline SIN, Dec8 timelines tech audit refactoring + lama initiated triage + Risk ID Recall, Nov25 list updated goal map, Nov10 temporary requirements dashboard, Nov7 multiple new metrics, Nov4 Aggregate Risk Score dashboard + SIN + Triage Completed without Escalation + EO N/A Rate + % EO survey top2 effort, Oct29 % reviews evidence duration, Oct20 % assisted self-cert SPARK post ROI framework, Oct16 links to definition docs, Oct15 ROI framework, Oct14 controls pilot MAPs SEVs, Oct7 Initial version.

**Dashboard plans:**
1. Flywheel executive dashboard – all topline + secondary metrics no dimensions.
2. Areas executive dashboard – version Flywheel with Areas-specific breakdowns TBD format expected used Ops reviews + goal tracking.
3. Deep-dives – each flywheel node one canonical source of truth dashboard.
- Bunnylol paindex for Areas list https://fburl.com/unidash/fmn6p933
- Folder ALL Risk dashboards https://fburl.com/unidash/v4a7avkb
- Still multiple dashboards scattered, cleanup consolidate but priority build metrics, dashboards linked in table are validated source of truth.

**Implications for Data Risk:**
- Many Data Risk P4 metrics (Triage without escalation, EO N/A Rate, No T&E Rate, % Requirements usable/meeting min bar) are V0 or expected Nov – aligns with caveat that only % Minimal LaMas goaled H2 rest tracking-only due audit calibration unreliable.
- SIN metrics WIP – first version available stabilization needed – guardrail for unnecessary SIN work.

---

## Verified Days Metric

_Source: https://fb.workplace.com/groups/815802615497569/permalink/2339010959843386/ — Verifier Effectiveness: % Verified Days Metric_
_Owner: Oliver Kaus, 2026-05-05, 7 reactions_
_Cc: Tony Harper, Baris Bechir, Sebastian, Connie, Melody, tagged Iva Marinkovic_

**TLDR:**
Last year created standardized requirements, controls, verifiers. Lacking metric ensuring verifiers consistently verified. Designed % Verified Days as secondary monitoring Control Maturity https://docs.google.com/document/d/1sZYoTmxQ2nALvg7-ZNHVieHFBackis7rCPYy2l71hO8/edit to ensure verifiers consistently effective every day L28. Enables Risk Areas mitigate verifier issues before become problems optional tool for risk owners manage controls+verifiers.

**Findings (as of 05/02):**
- 27% (61/229) controls and 12% (75/634) verifiers currently <60% Verified Days L28.
- 31% due verifier failures, 69% due monitor failures (missing data – bug in platform runs verifiers, config issue, data >SLA delayed default 5 days – SLA higher than verifier failure, tasks go to one platform oncall triage take longer pile up failures – per Fernando comment + need analysis split reasons Sushil Ojha).
- Six hotspots verifiers <60% Verified Days ordered by non-verified volume:
  - Restricted Data: 20/82 verifiers (7/21 controls)
  - Data Out: 12/95 verifiers (14/36 controls)
  - Cloud: 11/68 verifiers (3/4 controls)
  - T&C: 7/48 verifiers (5/23 controls)
  - 3PD Mon: 5/19 verifiers (3/7 controls)
  - Anti-Scraping: 4/90 verifiers (2/10 controls)
- Goaled in Restricted Data and UDI, tracking in T&C. Recommend monitoring if flagged.

**Definition:**
- Verifier level: # days verifier passed / total days L28. Control/requirement level aggregated: day verified if all associated verifiers passed for that day. Warning statuses if threshold surpassed still considered verified day. Non-Verified day if any verifier failing or data unavailable.
- Requires all verifiers run daily (600+ verifiers daily few exceptions) statuses pass/fail/missing data L28.

**Details:**
- Table Control/Verifier Count per Risk Area Group (sheet https://docs.google.com/spreadsheets/d/1-8lfzfGCK1Wp-LTx50GsCIWkB5aQF7C2Y30fzQ8PSsk/edit?gid=1004493392 + dash https://fburl.com/datainsights/l0wyo2tw)
- Verifier Breakdown table (doc https://docs.google.com/document/d/1N6Pht4NJWlHLLTe_NCokGCOB3g3EF6qIcJYWWToTbOQ/edit + sheet gid 743796671 + dash https://fburl.com/datainsights/cmt4sekp)
- Breakdown Restricted Data missing data pipeline issues examples PRIV-VER-7833, 3125, 2648.

**Next Steps:**
- Publish deep-dive dashboard surface more details verifier gaps (cc Tejal + Shalini)
- Move metric from MVP dash https://www.internalfb.com/intern/unidash/dashboard/risk_verifier_effectiveness/untitled/?edit=1&widget_id=948865057475182&referrer=insights_sharing to Control Maturity Deep Dive dashboard and use new data foundations
- Work with RAG/RA TLs hot spot areas improve % Verified Days

**Thanks:** Tejal + Shalini building data foundations ensuring consistency, Scott + Tejal foundations % Verified Days metric, Yuri guidance refining metric queries.

**Linked posts:** tagged Tony Harper Baris etc.

**Relevance to H2 goaling:**
- P1 topline % Requirements with effective self-evidencing controls (% green) is subset of effectiveness? Yellow+green = effective (per Baris). Verified Days is guardrail verifier effectiveness goaled in RD + UDI – links to NSM4.6 % self-evidenced RQs deemed effective 29.6% and to P1 counter in Data Risk goal map → NSM4-G2.
- Shows real gap: 27% controls <60% verified days – explains why P1 controls hardening needed + oncall heavy.
