# Competition RAGL x ERPL Check-In — March 2026

**Risk Area:** Competition (CPDP, CDU, CP)
**Date:** March 2026
**Source:** [Google Doc](https://docs.google.com/document/d/1sXZHzdJP4UTr13GYhX5IBCM0TUwSh4bmL6E-yDhZnmU/edit)

---

## Updates and Challenges

### AI Progress

- 94.7% AI-First WAU; 93% of diffs AI-assisted, 98.8% of code AI-generated
- ~122 engineering hours saved per month from meeting optimization (~1 extra hour/person/day)

**AI Wins — Fast, good risk decisions:**
- CDU risk agent integrated into analysis-plan review tool — 50% reduction in CDU Legal review effort
- CDU Decision Agent — 50% cost reduction from reviews and decisions
- Competition SIN Agent — 85% accuracy, 95% risk recall (eval-driven gains)
- Improved CPDP DT — WA-Meta SIN volume reduction by 40%
- Launched XARC (Cross-App Risk Checker) — Claude Code plugin surfacing cross-app privacy and competition risks at idea stage

**AI Wins — Mature controls:**
- Automated Audience Management Agent for CDU — higher accuracy reorg detection alerts
- XSU SupportMate integration — 25% of WP group queries handled by SupportMate
- XSU Handoff Agent — 130+ violations remediated via AI automation

### Goals Achieved

- Completed DMA Y3 Compliance report
- CDU DT trigger rate dropped from 94.1% to 10.6% (updated DT)
- More TLs trained for higher volume T&E escalations
- CDU Decision Agent launched — 50% cost reduction

### New Goals for H1'26

- Evolve CDU safeguarding using AI for additional data sources, growth channels, other surfaces
- Extend Automated Audience Management Agent beyond alerts to automate reorg updates
- Consolidate XSU and Hummingbird Ads Infra
- XSU Multiverse Remediation agent — auto-resolve 60-70% of Multiverse violations
- Building ground truth (pending long tail plan)

### Goal Acceleration

Majority of H1 goals now targeted for May completion. Only the following expected in June due to PPG dependency:
- Onboard Threads to XSU
- Complete XSU roll-out for remaining impacted products

### Key Inform Items

- **Cross-Meta Personalization x Competition Risk:** MRS Ads-Organic unification restarting. Competition team re-engaged. Meta AI designation risk re-assessed for EU personalization.
- **CCI/NCLAT (India):** Supreme Court hearing rescheduled to April 13. Compliance starting positions finalized for all products. Compliance Report filed March 16.
- **ANPD (Brazil):** Compliance plan submitted Feb 9 addressing 8 orders and 2 recommendations from WA-Meta Data Sharing investigation. Expect 1-3 months of ANPD negotiations; rollout anticipated July 2026.
- **Staffing pressure:** Team spread thin due to central AI initiatives (Agentifying the Codebase, Forest, Agentic AI Risk, AI4Oncall, PREQ-AI).
- **Reality Labs:** Infra readiness achieved for Position 1.5. Remaining remediation work paused until RL designated under DMA. Clear plan to re-engage within 3 months of designation.
- **Threads:** Deployment lockdown from multiple SEVs. Evaluating push of XSU Phase 2 launch to Q3.

### Org Updates

- Ben moved to Business Messaging; Raza leaving Meta
- Suchita joined as PATL

---

## Standing Topics

### Data and Dashboards

**Topline (as of 3/21/2026):**

| | Overall | CPDP | CDU | CP |
|---|---|---|---|---|
| Control Maturity (Target > 95%) | 92.59% | 90.9% | 100% | 80% |
| Requirement Meeting Min Bar | 100% | 100% | 100% | 100% |
| LaMa Triage w/o Escalation | 54.5% | 54.5% | 100% | N/A |
| Risk Identification Recall | 86.26% | 86.57% | 100% | N/A |

- Risk Identification Recall: Joint audit with PRPM found 71.4% false positives (9/14 wrongly audited, 1 bug)
- LaMa Triage w/o Escalation: Trivial volume (6 over L28)
- CDU Requirements: 100% green
- CPDP: RQ71427 and RQ78187 fixed, improving to 90.9%. RQ71425 (CCSR) fix WIP
- CP: RQ78499 fix WIP

### Internal Pressures

| Product Group | Engagement | Key Context |
|---|---|---|
| Manus | High-touch | CDU risks assessed as Low — calls via Datamate/Analytics Agent with existing safeguards |
| Central Growth | High-touch | F3 announcement moved to late April. Core Linking simplification: two L1 decisions finalized; early testing results very strong |
| Facebook | High-touch | Pages in A/C and consumerizing Pages — not started, anticipate significant compliance work |
| WhatsApp | High-touch | Exploring IAB precedence for WA BizM signal collection (early assessment) |
| Subscriptions | Light-touch | Non-blocking T&E risks identified (A/C linking discount, Tying Risk) |
| MRS/MSL | High-touch | Requires targeted response |
| Threads | Light-touch | Not started |
| FoA | High-touch | Reg response for 3P AI refusal to supply in 4+ markets; fallback planning for Project Ray / TT decision |
| Compliance | High-touch | DMA Y3 Compliance Report submitted March 6, published on Transparency Center |

### External Pressure Shifts

| Pressure Area | Severity | Key Update |
|---|---|---|
| AI x Competition | High | Active injunction/enforcement in multiple geos. Tying (Meta AI on FoA) and Refusal to Supply (WA 3P AI removal). Concurrent investigations in 4+ markets. |
| WhatsApp x Meta | High | Compliance orders from India, Brazil, Nigeria, Italy. Brazil compliance plan submitted. India Supreme Court hearing pending. |
| Marketplace C&D Order | Medium | Strong 3P listing adoption and engagement |
| DMA Competitive Data Use | Medium | Safeguards in build for foundation models data use and employee AI tools |
| DMA Messaging Interop | Medium | EC letter 3/3 requesting additional interop features. 3P rollout going well. |
| DMA Self-Preferencing | Medium | Emerging EC interest on Threads-IG. RFI submitted Dec 10. |
| DMA FRAND | Medium | ADSM Review Board resolved all pending cases. 30 new DMA cases in December. |
| DMA Designation | Medium | Meta AI 40-50% likelihood in 12m. Threads Medium. WA Channels Low-Medium. |
| Gormsen UK Class Action | Active | $4B class action (46M UK FB users). Court-ordered RFI response Jan 12. Trial Sept'27. |

### Requirements Changes

| Requirement | Change | Reason |
|---|---|---|
| RQ78185 | Removed Ads exception from scope | CCI Compliance (NCAT clarification) |
| RQ78187 | Clarified Family Account as C2P for EU/UK | L1 decision |

### AI4C4ER Check-In

**Progress:**
- CDU risk agent fully integrated into analysis-plan review tool — expected 50% reduction in manual audit effort
- Automated Audience Management: Confucius-agent deployed in alerting mode with improved reorg detection (org tags instead of employee names)

**New work — safeguarding AI tools:**
- CDU strategic overhaul prompted by AI tool proliferation invalidating prior assumptions (humans always involved, limited technical skills, concentrated analytical surfaces)
- Building plan for: (1) multi-layered risk detection (prompt, response, system interactions), (2) async AI-native risk assessment and audit minimizing human involvement
- Unlink SLA cost reduction via Diff Agent (flags violations at diff time) and Table Deletion Framework (identifies safe-to-delete violation tables)
- Link Use: Working proof of concept for AI-first control; decision doc in review with legal

**Challenges:**
- New AI surface launches (Manus, Nest) require immediate CDU partnership
- Quality Ground Truth datasets are foundational for quality agents — teams need to plan for increased investment

### Roadmap Progress (off-track and milestone items only)

| Priority | Project | Status | Detail |
|---|---|---|---|
| P0 | AI on WA Response | Back On Track | Completed BR compliance. Aligned EU/IN response strategy. |
| P0 | Generative AI | Back On Track | Partnering with AI Risk on H1 personalization roadmap |
| P0 | Optimize CDU DT audience | Milestone Complete | DT trigger rate 94.1% to 10.6% |
| P0 | Risk Flywheel Metrics | Back On Track | Triage w/o Escalation dropped from 90% to 57%. Aligned with Central to move to tracking (<10 T&Es). |
| P0 | 100% operational verifiers | At Risk | Currently 31% (from 60% in Dec'25) |
| P0 | Internal Audit Findings | Milestone Complete | CDU and CPDP audit findings remediated |
| P0 | CDU Decision Agent | Milestone Complete | 50% cost reduction |
| P0 | XSU Phase 2 (Threads, RL, P1 systems) | At Risk | RL restructuring extended to H2. Threads rollbacks on 99 model types. |

### MAP/Issue Tracker

| Issue | Summary | Deadline | Status |
|---|---|---|---|
| ISSUE-07322 | ADSM process inefficiencies | 3/31/2026 | On Track |
| Unlink IA Obs #1 | Delay in Remediation Task Creation | 2/1/2026 | Milestone Complete |
| Unlink IA Obs #2 | Inconsistent Data Retention Policy | 2/28/2026 | Milestone Complete |
| Unlink IA Obs #3 | Inconsistent Fail-Close Enforcement | 3/31/2026 | Milestone Complete |

---

## Meeting Notes

- Should not invest more in DT optimizations. Should ensure we have global controls.
