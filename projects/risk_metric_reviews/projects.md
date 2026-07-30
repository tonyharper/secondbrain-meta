# Risk Metric Reviews — Tasks

## Active
- [ ] Link July 27 scorecard — `projects/risk_goaling_h2_2026/docs/july_27_scorecard.csv` — 95 unpacked, 39 numeric should map (only numeric per user, ship goals like Unblock Data Risk Cloud excluded), 12 placeholders xx%/yy% (now 10 OPEN + 2 DONE: Agentic 50% + Quality Bar 80% Anthony), Target column extracted (95%, 70%, 100%, 14 days, ≤2 AAPC, ≤2% PLP, 500k/yr, ≥50% @90% etc), Current_Value blank — map Review ETA table to blocked 6 remaining + Conor 8/13 + TMH hold — due tomorrow 2026-07-28
- [ ] M360 pulls — for 39 numeric metrics add m360_link + populate values[] in scorecard.yaml via meta m360.metric info — reuse generate_risk_scorecard.py (parser fixed 2026-07-27 for single+multi entries) — starter: Parental Alignment 37.4% vs 37.2% goal, Minimal LaMas 25.9% backslid from 45.3%, Cost Compliance $97.1M vs $157M baseline
- [ ] Keep separate from Risk Goaling per user — don't combine yet — shared source scorecard.yaml + july_27_scorecard.csv

## On Hold
- (none)

## Complete
- [x] Scaffold project folder — 2026-07-27
- [x] Ingest founding doc via knowledge_load — https://docs.google.com/document/d/1nyI6Xk_I_IPO-hGSFcWA6h4cdJ0Hh2s57izDVp1hOpM — truncated cache 57KB — TLDR initial
- [x] Fetch full founding doc via meta CLI — `meta google.docs get --id 1nyI6Xk_I_IPO-hGSFcWA6h4cdJ0Hh2s57izDVp1hOpM --format text` — 1,165 lines — done 2026-07-27 — How to fill: 1 metric goals regular trend lightweight table, 2 significant movement commentary, 3 goals metrics pending ETA table, 4 Insights — NOT include ship goal progress — July 2026 Review appendix full narrative with 14 newly filed reg inquiries in June, Youth Parental Alignment 37.4% +0.2pp vs goal, Unblock AI 36% LaMas Heavy 21% escalation 47% SIN, >7bd 33% down from 41%, XFN Red doubled via CAIP, P4 Transform LaMa volume nadir, % minimal 45.3%→25.9% Forest+MonAI RQ20046081, Controls & Verifiers 629 reqs 412 manual 65.5% vs 34.5% self-evidenced 41 ineffective 6.5%, Cost Compliance $97.1M vs $157M baseline $15.7M EOY goal, SEVs 1.12x vs All Meta, Privacy SEVs inflated Agent Oversight 54 interceptions, DPRS/ACH prevention ~74 — see overview.md
- [x] Define cadence — confirmed monthly with Stephanie Yee — Risk Leads Dashboard Monthly Review Owner Risk Analytics — done 2026-07-27 per user
- [x] Define scope — monthly operational review cadence for Risk org goal metrics vs H2 targets — lightweight trend table if flat, commentary if movement, separate ETA table for pending metrics + insights — ship goals out-of-scope per founding doc — done
- [x] Stakeholder list — Risa Kawai (Reg inquiries), Anthony O'Sullivan, Jim Liu (Youth/TMH), Connie Lun (Unblock AI / AI Native Req + 3 blocked targets % SINs SLO + AIR SLA + L1 Rate), Anastasia Gandrik (Scale Risk Review Agentic Share 50% DONE), Conor Frailey (Day 0-14/20 >xx% O18 ETA 8/13), Kaz (Preventable attrition <xx% due tomorrow), Tony Harper (Harden Controls/Standardize + July 27 scorecard owner) — done
