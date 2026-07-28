# Blocked Numeric Targets — H2 Goals — 2026-07-27 (updated 2026-07-27 PM)

_Source: User provided list + v3 doc t.94anu86ip79a + scorecard.yaml (115 metrics, 110 non-blank)_
_Last updated: 2026-07-27 PM — 1 confirmed, 6 extended to tomorrow, 1 hold_

This tracks the 8 metrics in v3 doc still needing numeric targets per To Do "Will get numbers by July 15" @tonyharper.

## Summary

| # | v3 Goal | Metric (current name in YAML or v3 placeholder) | Status | POC / Owner | Next Step | Exists in Sheet/YAML? |
|---|---------|--------------------------------------------------|--------|-------------|-----------|----------------------|
| 1 | 2A(1) Teen recall/precision | Adult Classifier (U18) Teen recall — "+xx% teen recall @ xx% teen precision" | Blocked on TMH settlement | Waiting on settlement (Youth) | Hold — TMH — no ETA | Yes — target empty |
| 2 | 2A(3) UK OSA readiness | Day 0-14/20 Age Assurance — ">xx% new adult users resolved as O18" | Youth setting targets — extended | Conor Frailey | Follow up tomorrow 2026-07-28 | Yes — target empty, P2 2A |
| 3 | 3(2) AIR decision timeliness | AI Launch - Decision Speed - % AIR White-Glove Product Critical Decisions within SLA — "xx% within SLA" | Metric & target in dev — extended | Connie | Follow up tomorrow 2026-07-28 | Yes — target empty, P3 3B |
| 4 | 4A(1) Risk review sustainability | % SINs under SLO — "x% SINs under SLO" | Following up — extended | Connie + Scott Murani + Alice Berthaux | Follow up tomorrow 2026-07-28 | Yes — duplicate (Data Risk Scott, User Risk Alice) target empty |
| 5 | 4A(2) Agentic Review adoption | Agentic Review Share — "→ 50%" — **CONFIRMED** | Finalized 50% aligned per Anastasia/Jeb | Anastasia / Jeb — CONFIRMED today + POC Mateen Saifyan | **DONE — target set 50% in YAML 2026-07-27** | Yes — target now "50%", P4 4A — regen done |
| 6 | 4A(3) L1 rate reduction | L1 Rate reduced by xx% (AI Risk) — NEW stub l1_rate_reduction_ai_risk_117 | AI Risk setting target — extended | Connie | Follow up tomorrow 2026-07-28 — stub exists | Yes — added 2026-07-27 stub, previously No |
| 7 | 4F(1) AI Fundamentals quality bar | Quality Bar Assessment — "xx% AI systems pass quality bar, 100% critical" | Pending — extended | Anthony + Arash / Avi Varadarajulu | Follow up tomorrow 2026-07-28 | Yes — target empty, P4 4A→4F, POC Avi |
| 8 | 4G(2) Preventable attrition | <xx% preventable attrition — NEW stub preventable_attrition_lt_xx_percent_118 | Pending — extended | Kaz / Kazuho Ozawa | Follow up tomorrow 2026-07-28 — stub exists | Yes — added 2026-07-27 stub, previously No — 4G now 1 metric |

## Details from v3 Doc

- **2A**: M1 U18 FB/IG +xx% teen recall @ xx% precision; M2 UK OSA >xx% O18
- **3(2)**: 2. Deliver timely, well-calibrated AIR decisions — xx% white-glove within SLA, no increase high residual
- **4A**: 1. Risk review sustainable — Missed Risk <7% and xx% SINs under SLO; 2. Agentic Review Share xx% + p90 Questions per Review <yy% + cSAT +xx%; Risk experts L1 Rate reduced by xx%
- **4F**: xx% AI systems, 100% critical, pass AI Fundamentals bar
- **4G**: <xx% preventable attrition

## Action Items (updated — as of 2026-07-27 PM)

- [ ] Conor Frailey — get timeline on 2A(3) UK OSA target — **extended to tomorrow 2026-07-28**
- [x] Anastasia / Jeb — confirm 50% for 4A(2) Agentic Review Share — **DONE 50% aligned 2026-07-27 — target set in YAML**
- [ ] Anthony — follow up on 4F(1) AI Fundamentals target — **extended to tomorrow 2026-07-28**
- [ ] Kaz — follow up on 4G(2) attrition target — **extended to tomorrow 2026-07-28** — stub created preventable_attrition_lt_xx_percent_118
- [ ] Connie — get targets for 3(2) AIR timeliness, 4A(1) SINs under SLO, 4A(3) L1 reduction — **extended to tomorrow 2026-07-28** — stub created l1_rate_reduction_ai_risk_117 for 4A(3)

## How to apply once you have numbers

1. Edit `projects/risk_goaling_h2_2026/scorecard.yaml`:
   ```yaml
   - id: <metric_id>
     target: "95% under SLO" # or "50% Agentic Share" etc
     values:
       - date: "2026-07-27"
         value: null
         status: "Blocked" -> "Finalized" when unblocked
         source: "owner: <name> ETA"
   ```
2. For NEW metrics (4A(3) L1 reduction, 4G(2) attrition) — add new block in scorecard.yaml under metrics: with id generated, v3_mapping priority_id/goal_id (P4 4A, P4 4G), risk_group, poc_analytics.
3. Run `python scripts/generate_risk_scorecard.py` → regen docs/scorecard_detailed.md + summary.md + csv + ghtml
4. Review `docs/scorecard_summary.md` grouped tables — latest value bold — then publish ghtml suggestion to v3 doc 1U9vr... tab t.94anu86ip79a via `meta google.docs apply --write-mode=suggest`

## Files

- Summary: `docs/scorecard_summary.md` (26KB)
- Detailed: `docs/scorecard_detailed.md` (22KB)
- Source: `scorecard.yaml` (108 metrics, 112 missing targets, see todo list /tmp/todo_targets.md)
- Mapping: `docs/v3_to_sheet_mapping.md` (0 TODO unmapped groups after heuristic, but 4G/1C/3C have 0 metrics — gap noted)
- v3 Doc: https://docs.google.com/document/d/1U9vrVFRO4A_jbi7QhhDbYdWv8n834gq3udR3M1KTjQQ/edit?tab=t.94anu86ip79a
- Tier-1 Sheet: https://docs.google.com/spreadsheets/d/1MCTfdFwYLl6VDrVthczHEd1OIQhMp1yRdjA9wY7pGFA/edit
