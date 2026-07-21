# Data Risk H2 2026 Goal Map — Summary

_Source: https://docs.google.com/document/d/1p5m4E70gaSLc7fCmpZnpDp9GCbCYVPgn8eBNOiFhfDA/edit?tab=t.0#heading=h.nvx5ud8oublf_
_Title: [draft] Data Risk H2 2026 Goal Map_
_Author: Baris Cem Sal (bariscemsal@meta.com), Date June 8 2026, Status Draft – for review_
_Last modified by: Tony Harper June 18 2026, 4 editors, 13+ viewers_
_Local: /tmp/data_risk_goalmapping.html 47KB, /tmp/data_risk_goalmapping.md_

_Ladder: Michel's Risk Org priorities (2026-05-29 WP 4530923387164309, 195 reactions) → Oliver's Data Risk priorities (2026-06-04 WP 1524006602468138, 38 reactions) → DR metrics → roll up to Risk Org North Star Metrics (Stephanie Yee WP 1480755657138590, Risk Leads Dashboard)_

_Parsed: 2026-07-21_

## How it ladders

Michel H2 Priorities: 1 Meet obligations, 2 Step-change Youth pressure, 3 Unblock AI launches, 4 Transform processes for AI. Context: H1 recap – Youth FB Teen Accounts + IG Teen Accounts expansion + TMH trials no sustained parental alignment impact; AI Risk Avocado launch first-ever EU AI Act Systemic Risk Assessment + 225B anonymized FOA tokens + automated compliance; Risk Review 45% minimal intervention +12pts; AI adoption ~95% code AI-generated 25% diffs auto-approved; Compliance 3rd DMA report + Cycle1 4th FTC Assessment high marks.

Oliver Data Risk Draft Priorities: P0 Keep Company Running (fast good risk decisions unblock launches drive value, SIN/Escalation SLA throughput, regulatory/inquiry deadlines, maintain controls KCIs green + SEVs + MAPs – confident on BAU before strategic), P1 Meet all Risks with Robust Global Controls (Ship critical Beehive/DOJ Bulk Data Rule/Cloud; global self-evidencing self-adopting yellow→green; robust to agents embedding requirement awareness guidance into agent workflows), P2 Strengthen Data Risk Positions (7 areas drifted during CS2.0: Restricted Data, RL Wearables, Cloud, Self-preferencing/cross-promotion, Data In, Portability Access, Anonymization), P3 Make Step Change Internal Efficiency (UDI, Competition AMP/ALP/XSU, Deletion/Retention simplify platform reduce oncall, Anonymization self-serve; pods unblocked move fast, project reporting cheap easy, fast lightweight goal change process), P4 Enable AI Transformation Risk Review (Forest, SIN Agent, AI-Assisted Escalations, Shared Facts, sharing Forest components across LaMa/control apps), P5 Improve Company Velocity Value Efficiency deliberately lower (Privacy Wave, federated cost reduction, RR acceleration not in P4 above). Sustainability: do not expect longer hours, no bus factor 1 via cross-training/docs/re-arch, invest in things that compound, be prepared to say no outside priorities.

This doc maps P0-P5 to metrics → NSMs.

## Goal Map Table (P0-P5)

| Priority | What it is | Topline | Secondary | Counter / Guardrail | Ship Goals |
|----------|------------|---------|-----------|---------------------|------------|
| **P0 — Keep the Company Running** | BAU floor: fast good risk decisions; SIN/escalation SLAs + regulatory deadlines; maintain controls KCIs green + address SEVs; deliver MAPs. Confident BAU before strategic work. | • % SINs under SLO • % Requirements effective (green+yellow) | — | — | • MAPs on track (→NSM1) • Regulatory response decisions on time (→NSM1) • Unblock AI Launches with informed Risk trade-offs (→NSM3) |
| **P1 — Meet all our Risks with Robust, Global Controls** | Manage risks globally with self-evidencing, self-adopting controls rather than bespoke case-by-case. Ship critical controls; move requirements yellow→green; make controls robust to agents. | • % controls agentic-ready‡ • % Requirements with effective self-evidencing controls (% green) (→NSM4-G2 → actually NSM4.6 in v0.1, mapped as NSM4-G2 in draft) | — | • % Verified Days (verifier effectiveness; goaled in RD + UDI) (→NSM4-G2/NSM4.6) • Agent-caused SEVs (→NSM5) • Agent interruptions / friction per session (→NSM6) | • Beehive (→NSM1) • DOJ Bulk Data Rule (→NSM1) • Cloud controls (→NSM1) |
| **P2 — Strengthen Data Risk Positions** | Mature risk positions that manage internal+external pressure (drifted during CS2.0): Restricted Data, RL Wearables, Cloud, Self-preferencing, Data In, Access, Anonymization. | • [Ship] Aligned positions for 7 priority areas | • Position maturity‡ | — | — |
| **P3 — Step Change in Internal Efficiency** | Smaller teams → big productivity jump. Make controls cheaper + more sustainable (UDI, Competition, Deletion/Retention, Anonymization self-serve); make pod operations + reporting cheap and easy. | • Cost-of-compliance (Direct costs*, USD) (→NSM7 Cost $3.7B) *FTEs, CWs, Infra, OPEX, Tokens | • Oncall efficiency‡ (SWE + DE, e.g., Deletion heavy, metrics: # alerts, MTTR, FP rate per Yiannis Papagiannis, Devini's prior oncall understand work) | — | — |
| **P4 — Enable the AI Transformation of Risk Review** | Enable AI Risk Review so company can move fast on novel-risk products and requirements without global controls: Forest, SIN Agent, AI-Assisted Escalations, Shared Facts. | • % "Minimal" LaMas (DR filtered)‡ (→NSM4.1 48% org level) – auto-decisioned not requiring manual evidencing (per Tony Harper comment) • [TBD] Metric on unnecessary SIN (reduce # SINs / unnecessary SINs – regrettable triage discussion, needs alignment) | • Triage completed without escalation† [tracking] (→NSM4.1) (vs regrettable triage concept from foundations) • EO N/A Rate† [tracking] (→NSM4.1) | • Missed Risk Rate† [tracking] (→NSM4-G1 → NSM4.5 5.44%) (based on PRPM audits/SC audit audit recall gaps, not fit per Scott Murani / Meghana, needs evals-based metrics horizontal evals workstream) • Risk Identification Recall† [tracking] (PRPM audits? needs evals) • Forest precision/recall [tracking] • Requirement Overapplication Rate‡ [tracking] (false positive rate, over-attached requirement met unnecessarily, sampling alignment ongoing, Forest measurement will enable FP rate – per Scott Murani) | — |
| **P5 — Improve Company Velocity, Value, Efficiency (deliberately lower this half)** | Deliberate choice to place lower, creating space for structural work above that lets DR scale itself. Privacy Wave, federated cost reduction, RR acceleration not in P4. | • PG compliance cost ($/EY) [tracking] (→NSM7) $3.7B total (Risk cost vs PG cost distinction – per Baris: Risk org cost budget vs PG cost wave/friction, Meghana Q: is cost best vs controllable lever iterations/retries/clicks/% automation/time) • Created company value (e.g., iRev) (tokens, iRev discussion Tony + Baris) | • 1+ day interruptions and friction hours • Agent interruptions / friction per session (→NSM6 1.224% – per Tony: choose agent friction metric + one human friction metric probably 1+ day interruptions, last year's human friction metrics useful) | — | — |

Legend: † needs work · ‡ needs to be built (no mark = we have it). * Direct costs FTEs, CWs, Infra, OPEX, Tokens.

## Known Metric Gaps (from doc)

- **Agentic-enabled controls – % controls agentic-ready (P1 topline):** Two aspects – (1) whether control still works when primary actor is AI agent, (2) requirements covered by agentic compliance. Tony Q: in plain language what measuring? Baris: agentic compliance + controls not overrideable by agents. Needs definition leading measure upstream of Agent-caused SEVs (laggy).
- **Position maturity – quantitative measure for P2 beyond position/evidence-bar count.** Cantlin Ashrowan comment: positions don't really exist as first-order construct tracked atomic in compliance graph – consider if reqs? Scott asked context, Oliver said concept talked but not tracked atomic. Feedback from Oliver leads group: revise to "number of aligned positions" each needs review meeting + alignment reached (Tony). Currently ship goal for reviews not queryable.
- **% "Minimal" LaMas – org level metric, need DR contribution version.** Defined as auto-decisioned not requiring manual evidencing. Filtered down version (DR filtered) – 48% org level per Potentially version. To be defined for DR filter (open per Meghana). Discussion on optimizing for SIN then hold precision/recall guardrail (Tony: my instinct reduce # SINs implying reduce unnecessary SINs).
- **Oncall efficiency – including SWE and DE oncalls where appropriate.** Need standard measures across oncalls (e.g., # alerts received, alert MTTR, alert FP rate etc per Yiannis). Build on Devini's oncall understand work. Tony: include DE oncalls too some heavy. Shared in Deletion heavy.

## Other Caveats / Notes

- **Audit calibration** – reliability of audit-derived metrics still not on par with expectations (Missed Risk Rate, Recall). Analytics undertaking Q3 to understand + improve metrics/processes.
- **% "Minimal" LaMas is only goaled P4 metric.** Supporting metrics Triage without escalation, EO N/A Rate, Missed Risk Rate, Risk Identification Recall are tracking-only this half: all depend on self-cert audits whose calibration not yet reliable.
- **Cost-of-compliance currently undercounts federated PG work** – read as directional, improving over 2026.
- **NSM4 (large AI launches) – org-level metric still to be defined.**
- **SEV guardrail needed?** Tony suggested SEV guardrail for P3 cost reduction (could remove deletion system reduce cost but cause SEVs). Baris: hard to find which SEVs caused by reduced invest – leave out maybe SEV understand workstream.
- **Friction vs cost distinction:** Tony: should have both cost (dollars EY compute/storage) and friction (non-dollars interruptions human+agent). Cost = direct EY etc, friction = interruptions. Existing metrics: NSM5 agent friction, last year's human friction 1+ day interruptions + friction hours – useful, should choose agent friction + one human friction probably 1+ day interruptions.
- **Tokens, iRev:** Tony Q on PG compliance cost – are we missing tokens, iRev? Baris initially said tokens part of P3, added * to explain direct costs including tokens. iRev added to last goal P5.

## Appendix — NSMs Mapping (from doc, synced with Stephanie Yee V0.1 post)

| NSM | What it measures | DR coverage |
|-----|------------------|-------------|
| **NSM1** | Meet our obligations – ship goals this half ("% obligations covered by enforcement date" in development) | P0 + P1 ship goals (MAPs, Beehive, DOJ Bulk Data Rule, Cloud controls) |
| **NSM2** | Parental Alignment IG US 37.3% (Youth) | — (Youth/UR) |
| **NSM3** | Unblock AI launches with informed Risk trade-offs – white-glove product critical decisions (in development) | P0 ship goal (e.g., MTC, Unblock AI Launches) |
| **NSM4.1** | % "Minimal" volume in Risk Review auto-decisioned 48% (as of May 19) – mapped to 2027 goal "90% compliance happens automatically" | P4 topline DR filtered |
| **NSM4.2** | Median E2E duration Heavy reviews 11.1 days | DR candidate not yet goaled |
| **NSM4.3/4.4** | Adoption / utility of key tooling (in development) | — |
| **NSM4.5** | Guardrail: Missed Risk Rate 5.44% (as of May 7) – holds identification quality steady optimizing speed | P4 tracking |
| **NSM4.6** | Guardrail: % self-evidenced RQs deemed effective 29.6% (as of Jun 2) – control-maturity check | P1 topline % green + % Verified Days |
| **NSM5** counter | Residual AI/agent privacy risk interim AI-driven SEV volume 44 (L28D Jun2) SEVs where AI caused/contributed production Privacy incident | P1 Agent-caused SEVs |
| **NSM6** counter | Privacy/Security agent interruptions per session 1.224% (L28 Jun1) times agent trace interrupted by privacy/security control per agent session | P1 + P5 agent interruptions/friction |
| **NSM7** counter | Cost of Compliance $3.7B (as of Apr17) ~90% people nearly half outside Risk federated coverage improving through 2026 | P3 Direct costs, P5 PG compliance cost |
| **NSM8** | Intercepted issues SEVs tasks issues in development | — (future detection candidate) |

## Sources Referenced in Doc

- Oliver Pell – H2 2026 Data Risk Priorities: https://fb.workplace.com/groups/1482448799957252/permalink/1524006602468138/ (fetched – summary in inbox)
- Michel Protti – H2 2026 Risk Org Priorities: https://fb.workplace.com/groups/2468134800109855/permalink/4530923387164309/ (fetched – 195 reactions, summary in inbox)
- Risk Org North Star Metrics one-pager: https://fb.workplace.com/groups/992063232674504/posts/1480755657138590 (fetched – summary in inbox + north_star_discussion.md)
- H2 Risk Goals & Roadmapping Overview: https://docs.google.com/document/d/1pt6ljd4slI6mqpdlkIo6zxl7H1xfKaIs7fKpxjqykEE/edit (PENDING FETCH – referenced as main roadmapping doc)
- % Verified Days metric: https://fb.workplace.com/groups/815802615497569/permalink/2339010959843386/ (PENDING FETCH)
- Flywheel metrics readiness for Areas: https://docs.google.com/document/d/1hvqh8HJPH_OjRFm75rcZYdQa0aUKSW-OSN1JY5uWU8w/edit (PENDING FETCH)
- Risk Org Goals tracker: https://docs.google.com/spreadsheets/d/1MCTfdFwYLl6VDrVthczHEd1OIQhMp1yRdjA9wY7pGFA/edit?gid=1081314132 – already fetched, tier1_metrics_summary.md

## Implications for H2 Goaling

- **P0-P5 ladder clearly shows Data Risk intentional stacking order:** Must deliver BAU (SINs under SLO + Requirements effective) before P1-P5 strategic work. Decisions pods → P2 + P4, Controls pods → P1 + P3.
- **P1-P2-P3 chain:** P1 robust global controls self-evidencing self-adopting yellow→green + agentic-ready → NSM4.6 + NSM5/6 counter; P2 positions 7 areas ship aligned positions (review meetings alignment reached, not just count) → addresses defensibility/resilience from North Star doc; P3 internal efficiency cost USD * → NSM7 $3.7B baseline + oncall efficiency → sustainability (no bus factor 1, no extra hours, invest compounding).
- **P4 AI transformation:** Only % Minimal LaMas goaled H2, rest tracking-only due audit calibration – important for goaling realism. Need to reduce unnecessary SINs (regrettable triage) optimize for SIN count while holding Forest precision/recall guardrail + Missed Risk + Risk ID Recall + Requirement Overapplication Rate false positive.
- **P5 deliberately lower:** PG compliance cost $/EY + iRev, friction metrics – but Tony flagged should include both cost (EY/compute/storage) + friction (1+ day interruptions + agent interruptions). Tokens included via * note.
- **Sustainability note from Oliver:** Critical for team health – no longer hours to compensate reduced staffing, no bus factors of 1 via cross-training/docs/re-arch, invest in things compounding, say no outside priorities raise with DRI escalate quickly.

## Next Steps for Synthesis

- [ ] Fetch remaining 3 linked docs/posts: H2 Risk Goals & Roadmapping Overview (1pt6lj...), % Verified Days (81580...), Flywheel metrics readiness (1hvqh...)
- [ ] Confirm with Baris: agentic-ready definition (control works when primary actor AI agent + requirements covered agentic compliance) – upstream lead measure before SEVs
- [ ] Define Position maturity beyond ship count – number of aligned positions each needs review meeting alignment reached per Oliver leads feedback
- [ ] Align on oncall efficiency standard: # alerts, MTTR, FP rate + include DE oncalls (per Tony + Yiannis + Devini)
- [ ] For P4: finalize unnecessary SIN metric – reduce # SINs vs time vs unnecessary SINs – mapping to regrettable triage + Forest measurement
- [ ] For P3/P5: ensure cost captures tokens + PG federated work (undercounts currently directional) + iRev created company value
- [ ] Draft Data Risk team goals tying P0-P5 to pod structure (46 pods) + team capacity (reduced staffing) + sustainability principles
