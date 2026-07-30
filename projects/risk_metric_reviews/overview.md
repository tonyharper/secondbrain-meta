# Risk Metric Reviews — Overview

_Last updated: 2026-07-27_

## State

**Active — new project scaffolded 2026-07-27, full doc fetched 2026-07-27 via `meta google.docs get` — 1,165 lines.** Founding doc https://docs.google.com/document/d/1nyI6Xk_I_IPO-hGSFcWA6h4cdJ0Hh2s57izDVp1hOpM is monthly operational review cadence for Risk org goal metrics vs H2 targets. Monthly confirmed with Stephanie Yee per user 2026-07-27. Closely related to Risk Goaling H2 2026 but separate (don't combine yet).

## TLDR — Risk Leads Metrics Review H2 2026 (founding doc)

Source: https://docs.google.com/document/d/1nyI6Xk_I_IPO-hGSFcWA6h4cdJ0Hh2s57izDVp1hOpM/edit?tab=t.0#heading=h.j25w3p3i0ddr
Local cache: `~/.local/share/opencode/tool-output/tool_fb52e0098001eLjvtAaSjX5Q32` (truncated)

- **What:** Monthly review layer on top of H2 goaling (115 metrics raw / 108 non-blank in `scorecard.yaml` / 95 unpacked clauses in `july_27_scorecard.csv` / 39 numeric targets / 12 placeholders `xx%`/`yy%` per July 27). Not weekly, ship goals out-of-scope per founding doc.
- **Format:** Lightweight trend table if flat; commentary if significant movement; separate ETA table for pending metrics + insights section.
- **4 priorities (same as goaling):**
  - P1 Meet our obligations — incl. regulatory inquiries/litigation spike — POC Risa Kawai / Anthony O'Sullivan — link `risk-leads-dashboard.internalmeta.com?tab=macro-view#regulatory-inquiries`
  - P2 Step-change reduction in Youth pressure — POC Jim Liu
  - P3 Unblock AI launches — POC Connie Lun
  - P4 Transform for AI — sub-buckets: Scale Risk Review (Anastasia Gandrik), AI Native Requirements (Connie Lun), Harden Controls (Tony Harper / Connie Lun / Anthony O'Sullivan), Standardize AI Native Pod Operations (Tony Harper)
- **Cadence / Owner:** Monthly, analytics owner Stephanie Yee per `risk_goaling_h2_2026/overview.md` — Risk Leads Dashboard Monthly Review Owner Risk Analytics — Data Risk + User Risk + Youth + AI Risk — all Risk leads.
- **Current gaps (as of July 27):** M360 links TBD, values null — `scorecard.yaml` values history pending `2026-07-21 null` — needs `meta m360.metric info` pulls; 8 blocked targets pending numeric TO DO by July 15 originally (2A(1) TMH blocked, 2A(3) Conor timeline, 3(2)/4A(1)/4A(3) Connie, 4A(2) 50% Anastasia/Jeb, 4F(1) Anthony, 4G(2) Kaz — stubs created l1_rate_reduction_ai_risk_117 + preventable_attrition...118) — now 6 remaining + Conor ETA 8/13 + TMH hold + 2 done (Agentic Share 50% Anastasia/Jeb, Quality Bar Assessment 80% Anthony) — should be tracked in Review doc ETA table.

## Relation to Risk Goaling H2 2026

- **Goaling = source of truth for metric definitions:** Sheet 1MCTfd..., `scorecard.yaml` 115 raw / 110 non-blank, `july_27_scorecard.csv` 95 unpacked clauses (combined Priority - Title, Goal - Title, Target extracted from clause, Current_Value blank, Confidence HIGH/MED/LOW/NONE, Sheet_Mapped_Metric_Name, Sheet_Target, etc) — 39 numeric that should map (per user: only numeric goals should map, ship goals like "Unblock Data Risk Cloud" no metric), 12 placeholders `xx%`/`yy%`.
- **Reviews = consumption/review layer:** Tracks trend vs goal, commentary on movement, ETA for pending metrics, insights. References July 27 scorecard + blocked_targets docs.

## Key Docs (link + TLDR only — Tier 1)

| Name | Description |
|------|-------------|
| [Risk Leads Metrics Review — H2 2026 Working Doc — founding doc](https://docs.google.com/document/d/1nyI6Xk_I_IPO-hGSFcWA6h4cdJ0Hh2s57izDVp1hOpM/edit?tab=t.0#heading=h.j25w3p3i0ddr) | **NEW 2026-07-27** — founding doc — monthly review layer — tabs August 2026 Review (t.0 linked), July 2026 Review, H2 Goals — Format: lightweight trend if flat, commentary if movement, separate ETA table for pending + insights — covers 4 priorities P1-P4 — POCs Risa Kawai, Anthony O'Sullivan, Jim Liu, Connie Lun, Anastasia Gandrik, Tony Harper — analytics owner Stephanie Yee / Dashboard risk-leads-dashboard — gaps M360 TBD values null, 6-8 blocked targets TO DO July 15 (now 6 + Conor ETA 8/13 + TMH hold + 2 done 50%/80%) — Tier 2 via Drive, TLDR only here |
| [July 27 Scorecard — single CSV source](https://github.com/tonyharper/secondbrain-meta/blob/main/projects/risk_goaling_h2_2026/docs/july_27_scorecard.csv) / `projects/risk_goaling_h2_2026/docs/july_27_scorecard.csv` | 95 rows unpacked from v3 doc + mapping confidence — columns Priority combined (P1 - Meet our obligations), Goal combined (1A - Land Aligned Response Plans...), Goal_Metric_Clause, Is_Placeholder_xx YES=12, Has_Numeric_Goal YES=39 should map (ship goals like Unblock Data Risk Cloud excluded per user), Target extracted (95%, 70%, 100%, 14 days, ≤2 AAPC, ≤2% PLP, 500k/yr, ≥50% @90%, xx% etc), Current_Value blank, Confidence HIGH 17/MEDIUM 12/LOW 6/NONE 4, Sheet_Mapped_Metric_Name, Sheet_Target (now 50% Agentic Share DONE + 80% Quality Bar DONE per Anthony 2026-07-27), Sheet_POC |
| [H2 Goals v3 — Risk Goaling](https://docs.google.com/document/d/1U9vrVFRO4A_jbi7QhhDbYdWv8n834gq3udR3M1KTjQQ/edit?tab=t.94anu86ip79a) | v3 doc — authoritative plain-language descriptions — paired with July 27 scorecard |
| [Risk Goaling H2 2026 Overview](https://github.com/tonyharper/secondbrain-meta/blob/main/projects/risk_goaling_h2_2026/overview.md) | Source of truth — 115 metrics raw, 10 sources ingested, native scorecard built — closely related but separate from this project per user |

## Stakeholders

| Person | Role | Context |
|--------|------|---------|
| Tony Harper | Owner / Data Risk | Owner for this Reviews project + H2 goaling + Harden Controls/Standardize (P4 4C/4F/4G), plus July 27 scorecard owner |
| Stephanie Yee | Analytics Owner | Risk Leads Dashboard Monthly Review Owner, analytics for goaling |
| Risa Kawai / Anthony O'Sullivan | P1 Meet obligations | Regulatory inquiries/litigation spike dashboard |
| Jim Liu | P2 Youth | TMH litigation + Youth pressure |
| Connie Lun | P3 Unblock AI + P4 4B AI Native Req | Decision Speed White-Glove within SLA + SINs under SLO + L1 Rate + AI Native Requirements change loop |
| Anastasia Gandrik | P4 4A Scale Risk Review | Agentic Review Share 50% confirmed 2026-07-27 |
| Conor Frailey | P2 2A | Day 0-14/20 Age Assurance >xx% O18 — ETA 8/13 |
| Kaz / Kazuho Ozawa | P4 4G | Preventable attrition <xx% — due tomorrow 2026-07-28 |
| Anthony | P4 4F | Quality Bar Assessment 80% confirmed 2026-07-27 (80% systems pass, 100% critical) |

## Open Threads

- [ ] Ingest full founding doc via meta CLI — `meta google.docs get --id 1nyI6Xk_I_IPO-hGSFcWA6h4cdJ0Hh2s57izDVp1hOpM --format text` — re-parse tabs July + Aug + H2 Goals + fill missing sections — due 2026-08-01 — currently truncated cache
- [ ] Define cadence — confirm monthly with Stephanie Yee, link to Risk Leads Dashboard, document here
- [ ] Link July 27 scorecard — reference `risk_goaling_h2_2026/scorecard.yaml` + `july_27_scorecard.csv` — map Review ETA table to blocked targets 8→6 + Conor 8/13 + TMH hold + 2 DONE (50% Agentic Share, 80% Quality Bar)
- [ ] M360 pulls — for 39 numeric metrics add m360_link + populate values[] via `meta m360.metric info` — reuse `scripts/generate_risk_scorecard.py` logic (now fixed parser for single entry + multi entry)
- [ ] Separate vs combine — closely related to Risk Goaling but don't combine yet per user — keep separate projects with shared source `scorecard.yaml` + `july_27_scorecard.csv`

## Key Metrics (Tier 1 only — link + TLDR)

| Metric | Baseline | Target | Note |
|--------|----------|--------|------|
| H2 Goaling metrics | 115 raw / 110 non-blank / 95 unpacked clauses | 39 numeric that should map + 12 placeholders xx%/yy% | July 27 scorecard single CSV |
| Blocked numeric targets | 8 originally 2026-07-27 | 6 remaining + Conor ETA 8/13 + TMH hold + 2 DONE (Agentic 50% Anastasia/Jeb, Quality Bar 80% Anthony) | Per v3 To Do July 15 |
| July 27 scorecard placeholders | 12 YES | 10 OPEN + 2 DONE | Is_Placeholder_xx YES |
| Risk Metric Reviews cadence | Monthly (not weekly) | Monthly review layer — trend + commentary + ETA table | Founding doc: ship goals out-of-scope |
