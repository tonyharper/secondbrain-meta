# H2 Risk Org Goals v3 — Summary

_Source: https://docs.google.com/document/d/1U9vrVFRO4A_jbi7QhhDbYdWv8n834gq3udR3M1KTjQQ/edit?tab=t.94anu86ip79a — [IN PROGRESS] v3_
_Owner: Stephanie Yee (sjyee@meta.com), created 2026-06-29, modified 2026-07-21 09:07 UTC_
_Editors: 19, sharing: tonyharper@meta.com writer + 56 others_
_Local: /tmp/risk_goaling_doc1_full.html (187KB), /tmp/doc1_full.md_

_Last parsed: 2026-07-21_

## Status

Title marked `[IN PROGRESS]` — To Do: Will get numbers by July 15. Document contains 3 layers:
- Discussion questions (blue comments)
- Proposed risk org corresponding goals (high level view)
- Same list with goal metrics, owners, groups

Roadmaps linked: https://docs.google.com/document/d/1pt6ljd4slI6mqpdlkIo6zxl7H1xfKaIs7fKpxjqykEE/edit?tab=t.gceuxloe1ns6#heading=h.tql1opjmftr0

## Open Questions (from top of doc)

- ✅ **Goal 1C [for Arash]** – Determine approach to bringing best practices to CI. Currently added as new goal under Priority 1 — "Improve effectiveness and risk mitigation of Integrity & Security for CSAM, etc."
- **[for Abhishek + Risk areas] Goal 4A – Risk review**
  - Discuss resources required for non-forest risk review efforts. Also, neither AI Risk nor Monetization have goals around forest. Should they?
  - Refactored agentic risk review goal to be more explicit about metric ownership + combine product adoption + efficiency/cost goals. Graduated area-level goal around stating/meeting defined performance benchmarks to whole system.
    - Does new structure provide clarity (addressing 'various' owners)?
    - Nathan pointed out we do not include metrics for risk mitigation and instead focus on speed/etc. Should we?
    - Have we raised confidence in ARR being fully rolled out by EOY? Or reframe ARR to partial rollout? (Assuming goals should be 50:50)
- ✅ **[for Nathan] Goal 4B** – Figure out what work requirements require, and discuss staffing. Talk to Kristen Durkin and Jackie Zajac about their groups' requirements-related goals.

Additional open questions from comments section (v2 part):
- Goal 4A(3) Deprecate L1 – refactor in favor of business value-tied goals?
- Goal 4B Requirements – do goals as written provide enough direction? Arash flagged level of effort unknown, architecture/complexity, no excess capacity, needs incremental funding contingent. Should monetization/news requirements be in AI-native req doc?
- Goal 4G Risk strategists – grow pool as "tastemakers" not "labelers"; who owns sharing taste with model? Zef owns grow pool but not taste sharing.
- Are non-forest risk-review efforts fully funded? Only forest appeared on roadmaps.
- How approach teaching CI risk best practices?
- Goal 3(3) – Given MCI SEV followups, should we have goal around tracking RQ updates from AIR decisions?

## Priority Structure (from v3 table)

### PRIORITY 1: Meet our obligations

| Goal | Description | Metrics | Metric Owner | Risk Group Owner |
|------|-------------|---------|--------------|------------------|
| **1A. Land Aligned Response Plans and mature inbound response capabilities** | Land frontier/high-risk positions in priority launch regions (EU, Korea, Vietnam, CA). Ship EU AI Act deliverables Aug+Dec 2026 (AI transparency, content labeling, prohibited practices). Youth: Deliver aligned Response Plans for 100% regs with enforcement Q3-Q1 2027; achieve deploy-ready for 100% regs with enforcement H2. Develop capabilities for deploy-ready in high-risk/high-complexity (social media bans, ADF-model bills, India DPDP). Data Risk: Mature positions & decision making in high priority areas (Restricted Data, RL Wearables, Cloud, Self-preferencing/cross-promotion, Data In, Portability (Access), Anonymization) | varies by effort | Zef RosnBrick (AI), Allison Hartnett (Youth), Arash Nikkar (Data Risk) | All Areas Leads |
| 1A-2: Develop inquiries tooling | Spans whole response, mature inbound response efficiency. Users in Reg Readiness, Legal, Risk Areas rate tools as useful (95% inquiries in tooling; usefulness to 70% bar (Inquiries); 100% legal analysis AI-first with human review; Understand phase to 14 days (Laws)) | | Jackie Zajac | Area Response Platform |
| **1B. Mature efficacy of meeting ongoing obligations** (Meet obligations / Invest in automation / Accelerate existing systems) | Meet obligations: Demonstrate youth compliance via E2E controls library + testing, youth commitment inventory, youth audits (DSA Art 28, TMH), minimizing negative findings. Deliver FTC Assessment 4 Cycle 2 and MAPs >90% on-time audit rate <7% reopen, reduce erroneous testing. Ensure comprehensive control inventory + 100% control testing for Frauds & Scams. Invest: Safeguard Automation 75% auto-detected [MAP-517], auto-tested as they change [MAP-511]; Automate 65% GRC specialized Risk Assessments, decreasing delivery time 70%. Accelerate: Reduce time to onboard & test controls 50%; FTC cycle deadlines met no gaps, reduce Assessor Response time 50%; 100% obligations have status/milestones tracked via central tool. | | Susan Cooper (youth), Arash Nikkar, Jackie Zajac | RCP / GRC, Data Risk, User Risk / Areas Response Platform |
| **1C. Improve effectiveness and risk mitigation of high-harm Security/Integrity areas** | Integrate integrity E2E into Risk for 1 use case (CSAM) | | Arash Nikkar | Various |

### PRIORITY 2: Achieve a step-change reduction in Youth pressure | Topline: Parental Alignment (IG, US): +1ppt over H1 exit (TBC mid July)

| Goal | Metrics | Owner | Group |
|------|---------|-------|-------|
| **2A. Strengthen age assurance practices and advocacy via improved age classification, minimum age detection, readiness for age verification mandates** | M1: U18 FB/IG – Deliver +xx% teen recall at xx% teen precision prioritized markets; M2: U18 MetaAI on WA – ≥50% adult recall @90% teen recall via CBAP V2; M3: U18 MetaAI – Establish 18 boundary prediction playbook for Meta AI Apps; M4: U16 FB/IG – Establish measurement + prototype U16 boundary; M5: U13 FB/IG – Establish measurement + prototype U13 US. Expanded min age enforcement: M1 Proactive Detection – expand to all tier1 signals; M2 Reporting – enable scaling proactive + SURF in prioritized geos; M3 Enforcement Targets – increase proactive+reporting detection+checkpoint volume to 500k/yr IG & FB US (Guardrails: NVMI, Review FPR). Readiness for bans with AV mandates: M1 New user signals Day0-14/20 age assurance via hardlink, softmatch, 3P; M2 UK OSA Resolve >xx% new adult users as O18 | Allison Hartnett | Youth |
| **2B. Return to growth in Parental Alignment and continue reducing gap to YouTube** (Family Center App / AI Risk baseline & safety features / Age-appropriate content baseline) | 1. Launch Family Center App to beta (smoke test) with positive sentiment. 2. Sustain and expand teen safety across AI and content experiences – maintain 13+ experience for teens across Meta AI chats; maintain content experience IG/FB ≤2 AAPC exposures/hr, ≤2% PLP; full operational coverage AAC LoD framework FB/IG/AI; scale CYS measurement to new modalities; ship Teen Accounts for Vibes and MAI App. | Allison Hartnett | Youth |
| **2C. Reduce regulatory pressure by advocating effectively against social media bans and landing US federal legislation** | Continue product support for policy advocacy: Develop repeatable policy + product playbook for social media bans + India DPDP; support for 100% bills meeting trigger criteria | Allison Hartnett | Youth |
| **2D. Drive toward resolution of key TMH matters on terms consistent with principles** | Provide support + deliver positions for TMH litigation pressure on 100% requests | | Youth |

### PRIORITY 3: Unblock AI launches with informed Risk trade-offs | Topline TBC

| Goal | Metrics | Owner | Group |
|------|---------|-------|-------|
| **3. Unblock Priority AI Roadmap Initiatives** (Priority AI roadmap initiatives / Well-calibrated timely decisions / AI Governance & launch framework) | Unblock priority AI roadmap initiatives and make cross-org strategic decisions to unlock/protect multiple AI roadmap initiatives via white-glove support: AI Risk – Meta agentic bets (Hatch, Confidential VM, Meta AI agentic); TBD Labs priority model launches; PAR and RL priority launches (personalization video/multimodal, wearables & ambient sensing). People Data – Enable Internal AI launches by standing up new risk area (requirements, controls, implementation review, risk-review governance). Data Risk – MTC (MSL deletion/retention implementation asks), Cloud. User Risk – Conversational AI, Non-invoker controls, Copyright, News. Monetization – Business AI bets (Meta business agent, Subscriptions skills), continued progress MRS 1PD/3PD and organic/ads signal conversion cross-use, AI-generated advertising features, Shop Everything. RCP – All H2 AI model launch requirements completed, documented, evidenceable prior to launch; support all regulatory engagements for AI launches. | Zef RosnBrick, Arash Nikkar (Data Risk), Kristen Durkin, Susan Cooper (RCP) | AI Risk / Data Risk / Monetization / RCP |
| 2. Deliver timely, well-calibrated AIR decisions | xx% white-glove product-critical decisions within SLA, with no increase in L1+ decisions with high (residual) risk rate | Zef RosnBrick | AI Risk |
| 3. Ship AI Governance trust & safety launch framework | | | |

### PRIORITY 4: Transform our processes and Org for AI

| Goal | Metrics | Owner | Group |
|------|---------|-------|-------|
| **4A. Scale Risk Review with high quality across all Areas** (Risk review is sustainable / Agents make things faster/easier / Risk experts handle more novel cases, faster) | 1. Risk review runs sustainably: Missed Risk Rate maintained below 7% and xx% SINs under SLO. 2. Most product teams adopt Agentic Risk Review because faster/easier than LaMa: Agentic Review Share increases to xx% and every roll out meets pre-defined performance benchmarks. p90 avg Questions per Review maintained below yy% and User cSAT increases by xx%. [From comments: Risk Review/User Risk/Data Risk – Zero Question Review Rate decreases by xx%, SIN Rate decreases by xx%, Youth/Risk Review agents meet uptime SLA, no outage undetected >2 BD] | Abhishek Gulati + Risk area leaders, Arash Nikkar, Jackie Zajac, Allison Hartnett, Zef RosnBrick | User Risk, Data Risk, Monetization, AI Risk, Youth, Risk Review |
| Risk experts handle more novel cases, faster | User Risk/Data Risk/AI Risk: L1 Rate reduced by xx%; Youth: AI agents deployed across all critical escalation phases with meaningful adoption 75%-100% | | |
| **4B. Ship AI-native requirements across all Risk Areas (Requirements)** (AI Native requirements / Requirement change tooling) | AI-native Requirements change loop proven: requirement change propagates automatically to at least 2 downstream use cases (e.g., Applicability, SIN, verification), and closed feedback loop runs cyclically (Change → eval → fix requirement or distillation → redeployed to use case). | Nathan Davis | |
| **4C. Harden controls and scale our platform to keep pace with agent growth (Controls & Scale)** (Reduce Risk SEV prevalence / Harden and scale controls / Reduce friction & cost) | 1. Reduce Risk SEV prevalence for agentic + non-agentic: Double proactive interception rate for Agent-related privacy violations (includes SEVs). 2. Harden and scale controls: Harden Controls for 90% Tier-1 requirements & known SEV patterns. 3. Reduce friction & cost: Agentic workflows – Observability ≥90%, reduce top agent interventions (auth, sensitive data, ACL, tool/networking). Diff/Phabricator workflows – improve precision AO actions (hook, diff, AURA, auto-mitigation), orchestrate privacy signals in Phabricator. Reduce time/cost to maintain Controls, Safeguards, partner requests by 50%, where possible create company value (e.g., increase iRev). | Arash Nikkar | GRC, Agent Oversight / Data Risk / Agent Oversight, Data Risk, GRC |
| **4F. Standardize how AI-native pods operate across Risk with shared goals, consistent infra, clear expectations for human oversight** (AI in PREQ / Evals) | 1. Ensure critical AI systems — majority of all AI systems — meet AI Fundamentals quality bar: xx% AI systems, 100% critical systems, pass bar. 2. Eval Quality: All top-priority AI launches backed by rigorous evals, SMEs embedded in key pods, ≥1 pod runs rigorous eval E2E using only CoE resources (playbooks, office hours, tooling) without direct coaching | Arash Nikkar, Stephanie Yee | Engineering / Analytics & Research |
| **4G. Strengthen talent density and AI-native expertise across Risk Org** (Scale judgement & expertise / Near-zero preventable attrition) | 1. Scale Judgement & Expertise: Establish and execute plan to scale key talent pools by EOH – Risk strategists [Zef] (Grow pool with skills, tools, make job more efficient), Eval/ML SMEs [Stephanie], Domain experts [Varies by Risk Group Lead], Auditors [Abhishek]. 2. <xx% preventable attrition: Minimize cases where lack awareness or fail timely effective action by tracking awareness + prevention metrics | Kazuho Ozawa + various | |

## Data Risk Specifics (from Priority 1A + 4A + 4C)

- **Data Risk priority narrative (from Olivia Grace comment, incorporated):** "Maintaining clear risk positions that manage intersection of internal/external pressure is core to Data Risk's mission, but drifted amid CS2.0. This half, proactively invest in decision-making and partner with product groups to mature positions, focus: Restricted Data, RL Wearables, Cloud, Self-preferencing/cross-promotion, Data In, Portability (Access), Anonymization."

- **Data Risk appears in:**
  - 1A: Mature positions & decision making in 7 high priority areas (RD, RL Wearables, Cloud, Self-preferencing, Data In, Access, Anonymization) – Owner Arash Nikkar
  - 1B: GRC, Data Risk, User Risk involved in automation/acceleration
  - 3: MTC deletion/retention asks, Cloud
  - 4A: Scale Risk Review for Data Risk + others – Missed Risk Rate <7%, SINs under SLO, Agentic Review Share, Questions per Review, cSAT, L1 Rate reduction
  - 4C: Harden controls for 90% Tier-1 reqs, reduce cost 50%, agentic workflows observability

- **Links to Tier-1 Metrics sheet:** Data Risk 10 metrics (see tier1_metrics_summary.md) align to 1B, 4A, 4C, 3, etc.

## Next steps for synthesis

- [ ] Extract numbers by July 15 per To Do (Stephanie comment @tonyharper – update when you see fit)
- [ ] Clarify Goal 1C scope (CSAM + People Data?)
- [ ] Resolve Goal 4A resource discussion (non-forest risk review)
- [ ] Confirm ownership of agentic risk review metric and product adoption vs efficiency split
- [ ] Link this doc's priority metrics to sheet's 118 rows – ensure consistency
