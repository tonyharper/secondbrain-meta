# Data Risk Pod Digest — Week of April 13, 2026

_Generated: 2026-04-20_

## Coverage

- **User & Restricted Data**: 21 pod reports submitted (of 22 pods)
- **Competition**: 0 reports (6 pods exist, none submitted)
- **Data Mgmt & Boundaries**: 0 reports (18 pods exist, none submitted)

**24 of 46 pods have no visibility.** Either those RAGs haven't adopted the reporting template or their first reporting week hasn't started. Worth asking Oliver or RAG DRIs.

## URD Leadership Rollup (Apr 20)

Olivia Grace submitted the leadership rollup with execution status across 10 HLGs (5 Restricted Data, 5 Anonymization & PETs).

| HLG | Status | Key Metric |
|-----|--------|------------|
| RD HLG 1: Accelerate product velocity | At Risk | Self-evidencing 43% (goal: 60%) |
| RD HLG 2: Robust controls | On Track | R11 SPN 96% asset reduction, APO precision 1.000 |
| RD HLG 3: Novel RD decisions | At Risk | GenAI labeller recall 51% (goal: >70%) |
| RD HLG 4: London UDI capability | On Track | Cloud Computing pod formalized, Auto Pilot Phase 2 approved |
| RD HLG 5: Must-do compliance | On Track | MAP-450 execution plan finalized, DSA Year 3 on track |
| Anon HLG 1: Seamless risk review | On Track | 100% P0 SLOs targeted |
| Anon HLG 2: Mature controls | On Track | RAND Self-Serve at Beta, PriNER 7t (23 new languages) |
| Anon HLG 3: Novel risks | On Track | Meta AI Voice 2.0 launched, MIKA SDK decoupled |
| Anon HLG 4: Better engineering | On Track | Pod skills v2 shipped (10 diffs) |
| Anon HLG 5: Regulatory response | On Track | Reg Response PRD: 13 jurisdictions, 3 finalized |

## Flags for Discussion (from pods)

- **GenAI labeller quality gap** — 51% recall vs >70% target. Root cause: characteristics vs. activities confusion. Weekly calibration calls running. No XFN working group to resolve edge cases. No dashboards.
- **Ads 3PD MD-134 blocker** — L2 outcome pending as of 4/16, blocks cross-app cohort anon bar against 4/30 target.
- **RD Discovery self-evidencing at 43%** — 17pp gap with 10 weeks remaining. Batch self-evidencing of 15+ semantic types in flight.
- **Safeguards staffing** — 7 goals without DRIs including a P0. raghavgupta transitioning out Apr 20.
- **CTWA User Journey SEV3** (S649039) — device_name causes k-100 failure at 88.1% vs 95%. Fix identified.

## Items Needing Analytics Attention

### Measurement gaps

1. **GenAI labeller recall** — No dashboards, no automated tracking. The biggest risk to H1 GenAI goals is being managed by calibration calls alone.
2. **R2D2 triage CWE measurement** — Current methodology is inaccurate (includes cross-team escalation noise). Task T265285769 created for Karthik to automate. Needs to be fixed before baselining.
3. **PriNER recall 4.3% drop** — Metrics correction revealed real number is lower than reported. Decision needed: adjust target or find compensating improvements.
4. **Reg Response Acceleration AI** — Scored 0/5 vs expert 5/5. Significant quality gap in AI-assisted regulatory response.

### Measurement infrastructure in progress

5. **Risk Review Forest measurement plan** — Approved by DS. Baseline measurement depends on GT labeling completion (~Apr 29). 239 LAMAs scoped. Labeler capacity may be insufficient for two-week target.
6. **UDC Measurements Strategy** (Gasser Abdelhamid) — GT maintenance, DST consistency, SLA alerts. Under review by Harper Ma's team — relevant context for Tony but not his review action.
7. **AI-Native Classification dashboards** — Precision/recall for Semantic Type and Actor are live. UDC Measurements Strategy defines three focus areas.

### Operational

8. **Anonymization RAND/agentic self-serve** — Both at risk in the Infra Automation pod, possible deprioritization.
9. **OneCatalog Ownership Platform** — Lost EM + TL with no replacement. Decision needed.
10. **UDI Cost Reduction** — Shri Shridhar (BII PoC) moving to AAI org, impacts classifier validation for Goals 4-5.

## Pod-by-Pod Summary

### Restricted Data Pods

| Pod | Lead | Status | Headline |
|-----|------|--------|----------|
| RD Decisions (R2D2) | Daniel Chamberlain | On Track | 41 escalations completed H1, first L4 (Wearables Ambient Audio). Triage CWE measurement inaccurate. |
| RD Discovery | Anand Sudhanaboina | Mostly On Track | Self-evidencing 43%/60%. C4 recall 83% (exceeded 70%). GovID verifier blocked. |
| RD GenAI Controls | Nishant Gupta | Mixed | Labeller recall 51%/70%. Ember launch depends on continuous eval pipeline. |
| RD Risk Review | Tal Arbel | On Track | New pod, 6 members, 239 LAMAs scoped. Measurement plan approved. |
| RD Monetization | Chun-Shuo Lin | On Track | UGC Privacy Solution approved. Verifier implementation starting. |
| RD Output Closure | Daniel Ian Jackson | On Track | C27/C31 review Apr 22. HII verifiers hitting production. |
| RD Safeguards (SPN) | James Turner | Mixed | R11 shipped (96% reduction). 7 goals without DRIs. |

### Anonymization Pods

| Pod | Lead | Status | Headline |
|-----|------|--------|----------|
| Anon Decisions | Paul Rotilie | Mixed | Ads 3PD 4/30 target tight, WA EU briefing risk unresolved. |
| Anon AI & Infra | Haozhi Xiong | Mostly On Track | Pod skills v2 shipped. PriNER recall dropped 4.3% from metrics fix. RAND skill at risk. |
| Anon Structured Data | Yuqiong Sun | On Track | RAND Self-Serve at Beta. CTWA SEV3 active. PPQ skills series started. |
| Anon Extractability | — | — | Not summarized (lower priority). |
| Anon Multi-Modal | — | — | Not summarized (lower priority). |
| Anon Text Measurement | — | — | Not summarized (lower priority). |
| Anon Meta-Inaccessible/PETs | — | — | Not summarized (lower priority). |

### Inventory Pods

| Pod | Lead | Status | Headline |
|-----|------|--------|----------|
| OneCatalog (Agent-Driven) | Tanya Makareeva | On Track | Strategy one-pager nearing completion. Ownership Platform lost EM+TL. |
| AI-Native Classification | Sheetal Parade | On Track | GTKeeper approved by PAI. UDC Measurements Strategy under review. |
| Cost Reduction & Classification | Oleksii Aleksandrov | On Track | Deletion FP reduction targeting 70%→50%. DST coverage/precision/recall tracked. |
| Must-Do Compliance | Ozan Kaya | On Track | MAP-450 finalized. TPA auto-classifies ~60% of vendors. |
| BII Classifiers | — | — | Not summarized (lower priority). |
| Cloud Computing | — | — | Not summarized (lower priority). |
| Auto Pilot | — | — | Not summarized (lower priority). |
