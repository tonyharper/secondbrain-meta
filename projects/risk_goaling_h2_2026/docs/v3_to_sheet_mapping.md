# Draft Mapping: Goals v3 Doc → Tier-1 Sheet

_Source: Sheet https://docs.google.com/spreadsheets/d/1MCTfdFwYLl6VDrVthczHEd1OIQhMp1yRdjA9wY7pGFA (CSV /tmp/risk_sheet_export.csv 117 rows, 108 non-blank) + v3 Doc https://docs.google.com/document/d/1U9vrVFRO4A_jbi7QhhDbYdWv8n834gq3udR3M1KTjQQ (12 goals)_
_Last updated: 2026-07-21_
_Mapping direction: Sheet (Investment Priority + Human language goal) → v3 Goal ID, per heuristic + manual Data Risk P0-P5 mapping._
_Status: Draft – for review, 76 unique (Investment Priority, Human Goal) combos mapped, 0 TODO unmapped groups after heuristic (but 1C/3C/4G have 0 metrics pending curation)._
_Method: Option 1 – Sheet + Docs human sources of truth feed YAML (scorecard.yaml) preserving manual mappings + values history → exports to clean docs._

## Summary Counts

| v3 Goal | Title | Human Goals Mapped | Metrics Mapped | Example Risk Groups |
|---------|-------|--------------------|----------------|---------------------|
| **P1 1A** | Land Aligned Response Plans and mature inbound response capabilities | 8 | 11 | Areas Response Platform, User Risk, Data Risk, AI Risk, Monetization Risk, Youth |
| **P1 1B** | Mature efficacy of meeting ongoing obligations | 12 | 15 | Data Risk, MTC, GRC Product Platform, Youth |
| **P1 1C** | Improve effectiveness and risk mitigation of high-harm Security/Integrity areas (CSAM) | 0 | 0 | None in sheet yet – TBD, maybe People Data? |
| **P2 2A** | Strengthen age assurance practices and advocacy via improved age classification, minimum age detection, readiness for AV mandates | 5 | 12 | Youth |
| **P2 2B** | Return to growth in Parental Alignment and continue reducing gap to YouTube | 3 | 10 | Youth |
| **P2 2C** | Reduce regulatory pressure by advocating against social media bans + US federal legislation | 2 | 3 | Youth |
| **P2 2D** | Drive toward resolution of key TMH matters | 1 | 1 | Youth |
| **P3 3A** | Unblock Priority AI Roadmap Initiatives (white-glove support) | 2 | 2 | AI Risk, Monetization Risk |
| **P3 3B** | Deliver timely well-calibrated AIR decisions | 1 | 2 | AI Risk |
| **P3 3C** | Ship AI Governance trust & safety launch framework | 0 | 0 | None yet – TBD in sheet |
| **P4 4A** | Scale Risk Review with high quality across all Areas | 26 | 35 | User Risk, Data Risk, Monetization Risk, AI Risk, Agent Oversight, Risk Review Systems, GRC Product Platform |
| **P4 4B** | Ship AI-native requirements across all Risk Areas | 3 | 3 | User Risk, Monetization Risk, [Risk Harness] |
| **P4 4C** | Harden controls and scale platform to keep pace with agent growth | 13 | 18 | User Risk, Data Risk, AI Risk, Monetization Risk, Agent Oversight |
| **P4 4F** | Standardize how AI-native pods operate across Risk | 2 | 2 | [People Process Goals], Areas Response Platform |
| **P4 4G** | Strengthen talent density and AI-native expertise | 0 | 0 | None mapped – iRev + PG cost currently mapped to 4C but could be 4G per description create company value + talent density – needs decision |

**Total combos:** 76 unique (Investment Priority, Human Goal) → 108 non-blank metrics mapped.

## Detailed Mapping: v3 Goal → Sheet Human Goals → Metrics

### P1 1A – Land Aligned Response Plans and mature inbound response capabilities (11 metrics)

| Investment Priority | Human language goal (Sheet) | Metric Name | Risk Group | Type | POC |
|---------------------|-----------------------------|-------------|------------|------|-----|
| 1. Meet our obligation response requirements | Obligations reach critical milestones faster | Obligation wall time: Triage (passage to LSB) and Understand phase (triage to end of GIA) | Areas Response Platform | New | TBD (Risa & Anthony) |
| 1. Meet... | 1.1: Maintain and strengthen existing critical positions, and land aligned response plans before live date for every regulatory obligation that will come into effect in H2 | Land aligned response plans before live date for every H2 regulatory obligation | User Risk | Ship Goal | TBD, Fernando interim |
| 1. Meet... | 1.2: Operate inbound risk-response and escalation processes within SLA across User Risk | >90% of L1+ supported escalations have T&C input filled and aligned ≥24h before review | User Risk | Existing | Barnaby Cooper |
| 1. Meet... | 1.2: Operate inbound... | All pending Reg Response Obligations triaged within 5 business days | User Risk | New | Barnaby Cooper |
| 1. Meet... | 1.2: Operate inbound... | % SINs under SLO | User Risk | Existing | Alice Berthaux |
| 1. Meet... | 1.3 Ship the H2 Critical Path Deliverables the business depends on | Prepare and ship critical notification campaigns and privacy policy updates | User Risk | Ship Goal | Harshpreet Singh |
| 1. Meet... | Mature risk positions that manage internal + external pressure | Aligned positions for the 7 priority areas | Data Risk | Ship Goal | Baris Cem Sal |
| 1. Meet... | Mature AI regulatory response and compliance strategy | TBC - see comment | AI Risk | Ship Goal | Emily Hahn |
| 1. Meet... | Drive AI-native regulatory readiness at scale | Align x-Meta response plans, including PPG goals, in time to meet monetization overall | Monetization Risk | Ship Goal | Liz Keneski |
| 1. Meet... | Comply with new laws especially high risk regulations | Response Plan ready for new regulations | Youth | Ship Goal | Taylor Orner |
| 1. Meet... | Comply with new laws especially high risk regulations | Deploy ready for new regulations | Youth | Ship Goal | Taylor Orner |

**Notes:** 1A includes inbound response efficiency (95% inquiries in tooling, usefulness 70%, Understand phase 14 days Laws per v3 1A-2) – Obligation wall time maps here. Also Youth Response Plan ready / Deploy ready for new regs. Data Risk 7 areas narrative from Olivia Grace.

### P1 1B – Mature efficacy of meeting ongoing obligations (15 metrics)

| Investment Priority | Human language goal | Metric Name | Risk Group | Type | POC |
|---------------------|---------------------|-------------|------------|------|-----|
| 1. Meet... | Keep SIN within SLO so as to meet regulatory deadlines | % SINs under SLO | Data Risk | Existing | Scott Murani |
| 1. Meet... | Maintain controls, address SEVs, deliver MAPs | % Requirements effective (green+yellow) | Data Risk | Existing | Iva Marinkovic |
| 1. Meet... | Manage risks globally with self-evidencing, self-adopting controls rather than bespoke case-by-case | % Requirements with effective self-evidencing controls (% green) | Data Risk | Existing | Iva Marinkovic |
| 1. Meet... | MSL Researchers have their datasets successfully mitigated end-to-end on the first attempt | First Attempt Dataset Success Rate | MTC | Existing | Swetha Singiri |
| 1. Meet... | Model Training SEVs are detected proactively to minimize unexpected friction for MSL Researchers | SEV Proactive Rate | MTC | Existing | Kevin Bauer |
| 1. Meet... | AI at Meta production traffic is served by a verifiably compliant checkpoint | Checkpoint Compliance Coverage Rate | MTC | New | Ning Lok |
| 1. Meet... | Our FTC cycle deadlines are met with no outstanding compliance gaps | SVT Automation Deadline Met | GRC Product Platform | Ship Goal | Ashirbad Ghosh |
| 1. Meet... | Safeguards are automatically tested on a rolling basis as they change | Automate Safeguard Verification & Testing (SVT) | GRC Product Platform | Ship Goal | Avi Varadarajulu |
| 1. Meet... | Actual risk to Meta are dramatically reduced through our prevention and detection of SEVs before the risk is realized | Reactive Risk SEV Prevalance | GRC Product Platform | New | Shuaimin Kang |
| 1. Meet... | Auto-detect most Safeguard changes | Auto Detection Rate | GRC Product Platform | New | Shuaimin Kang |
| 1. Meet... | Reduce cost to compliance through automation and platformization. | Response plan efficiency | Youth | Ship Goal | Julia van Hoogstraten |
| 1. Meet... | Reduce cost to compliance through automation and platformization. | Deployment Efficiecy | Youth | New | Qifan Wang |
| 1. Meet... | Mature Risk Area: Every Youth risk area is mature and self-sufficient with routine work automated | Youth Area Maturity | Youth | Ship Goal | Julia van Hoogstraten |
| 1. Meet... | Mature Risk Area... | IDP Maintenance efficiency | Youth | Ship Goal | Julia van Hoogstraten |
| 1. Meet... | Mature Risk Area... | IG Youth Risk review maturity | Youth | Ship Goal | Julia van Hoogstraten |

**Notes:** 1B includes Youth compliance via E2E controls library, FTC Assessment 4 Cycle2 MAPs >90% on-time <7% reopen, Frauds & Scams 100% control testing, Safeguard Automation 75% auto-detected MAP-517 auto-tested MAP-511, 65% GRC RAs automated 70% faster, reduce onboarding testing 50% assessor response 50% central tool.

### P2 2A – Strengthen age assurance practices and advocacy (12 metrics)

| Human Goal | Metric | Risk Group | POC | Def Status |
|------------|--------|------------|-----|------------|
| Teen prediction: Deliver step-function improvement in U18 age estimation accuracy | Adult Classifier (U18) Teen recall | Youth | Conor Frailey | Finalized |
| Teen prediction... | Ship Meta AI x WA adult model V2 | Youth | Conor Frailey | Finalized |
| Teen prediction... | Establish U18 Prediction Playbook | Youth | Conor Frailey | Finalized |
| Minimum Age Detection (MADE): Expand proactive detection coverage... | Develop FoA U16 Model Protoptye | Youth | Prastuti Singh | Finalized |
| MADE... | Expand Proactive deteciton of U13 | Youth | Zoe Guo | Finalized |
| MADE... | Underage proactive and reporting detection + checkpoint volume | Youth | Zoe Guo | Finalized |
| MADE... | U13 Review False Positive Rate | Youth | Zoe Guo | Finalized |
| MADE... | FoA U13 Model Protoptye | Youth | Conor Frailey | Finalized |
| Age Analytics: Reliable topline analytics trends... | Analytics Age Model migration | Youth | Conor Frailey | Finalized |
| External Age Signals: Integrate with government mandated... | Deploy ready for App Store age laws | Youth | Conor Frailey | Finalized |
| External Age Signals... | Digital ID Verification | Youth | Conor Frailey | Finalized |
| AV Mandate Readiness: Deploy readiness for AV mandates... | Day 0-14/20 Age Assurance | Youth | Conor Frailey | Finalized |

**Maps to v3 Goal 2A:** U18 FB/IG teen recall/precision, U18 MetaAI WA CBAP V2 >=50% adult recall @90% teen recall, U18 MetaAI playbook, U16/U13 prototypes, proactive detection all tier1 signals, reporting SURF, enforcement 500k/yr US, new user Day0-14/20 hardlink softmatch 3P, UK OSA >xx% O18.

### P2 2B – Return to growth in Parental Alignment (10 metrics)

| Human Goal | Metric | POC |
|------------|--------|-----|
| Teen Account/Supervision consistency across Meta: Expand Teen Account/Supervision further across FoA; launch standalone Family Center app beta | Launch FCA App | Qifan Wang |
| AI Risk Measurement and Parent Alignment: Mature youth risk measurement and deliver safety features to drive parent alignment. | Ship turn/ conversational-level CYS measurement across text, video, images, voice | Wenjun Sun |
| AI Risk Measurement... | CYS Online VR | Wenjun Sun |
| AI Risk Measurement... | Ship SSI Alert V2 | Taylor Brown |
| AI Risk Measurement... | Launch Parental alerts on new high-sensitivity topics | Platina Liu |
| Continue strengthening our baseline to sustain/expand safe and age appropriate experiences across FoA | Facebook AAPC Exposure per hour | Andreas Ferstad |
| Continue strengthening... | Instagram AAPC Exposure per hour | Anita Mahinpei |
| Continue strengthening... | Facebook PLP 18+ % | Andreas Ferstad |
| Continue strengthening... | Instagram PLP 18+ % | Anita Mahinpei |
| Continue strengthening... | Age-appropriate Content 2nd Line of Defense | Katrina Browne |

**Maps to v3 2B:** Family Center App beta smoke test positive sentiment, sustain teen safety across AI/content experiences 13+ Meta AI chats <=2 AAPC exposures/hr <=2% PLP full AAC LoD FB/IG/AI CYS measurement new modalities Teen Accounts Vibes MAI App.

### P2 2C – Reduce regulatory pressure advocating against social media bans + US federal legislation (3 metrics)

- External Engagement: Increase acceptance of multi-layered age assurance approach and promptly respond to RFIs → Regulatory Acceptance of Multi-Layered Approach (Conor Frailey)
- Reduce regulatory pressure by advocating effectively... → Develop repeatable policy and product playbook (Tian Lan) + Product Support for Policy (Tian Lan)

Maps to v3 2C: Develop repeatable policy and product playbook for social media bans + India DPDP, support for 100% bills meeting trigger criteria.

### P2 2D – Drive toward resolution of TMH matters (1 metric)

- Support TMH response... → Support TMH Negotiations (Jim Liu) → Provide support + deliver positions for TMH litigation pressure 100% requests.

### P3 3A – Unblock Priority AI Roadmap Initiatives (2 metrics)

- Unblock priority AI roadmap initiatives and make cross-org strategic decisions... → TBC - see comment (AI Risk Zef RosnBrick)
- Up-level AI-product MonRisk decisions - Support key x-Meta priorities... → MonRisk is not blocker for Meta priority product outcomes (Monetization Risk Liz Keneski)

Maps to v3 3: Unblock priority AI roadmap initiatives via white-glove support: Hatch Confidential VM Meta AI agentic, TBD Labs models, PAR RL personalization video/multimodal wearables ambient, People Data new risk area, Data Risk MTC deletion/retention Cloud, User Risk Conversational AI Non-invoker Copyright News, Monetization Business AI Bets Meta business agent Subscriptions skills MRS 1PD/3PD organic/ads conversion AI-generated ads Shop Everything, RCP all H2 AI model launch requirements evidenceable prior launch.

### P3 3B – Deliver timely well-calibrated AIR decisions (2 metrics)

- Risk Org Priority #3: Unblock AI launches with informed Risk trade-offs → AI Launch Decision Speed % AIR White-Glove Product Critical Decisions within SLA (Jiaqi Guo) + Decision Risk Trade-Off % AIR L1+ Decisions with high residual risk (Melody/Ian Interim) – maps to v3 3: xx% white-glove product-critical decisions within SLA no increase L1+ high residual risk rate.

### P4 4A – Scale Risk Review with high quality across all Areas (35 metrics)

**Human goals (26 categories) grouped:**

- 2.3 Run Risk Review and Compliance Operations through Agentic Workflows with Continuous Evals → Decrease vendor spending News labelling to AI (Mike Derksen) + 90% L1+ escalation risk options labelled (Barnaby Cooper) + others
- Enable AI Risk Review so company can move fast on novel-risk products... → % Minimal LaMas DR filtered (Sebastian Poehlmann) + Unnecessary SIN rate [TBD] (Scott Murani) – only goaled P4 metric per goal map, rest tracking-only due audit calibration
- Accelerate and Scale Risk Decisions: Leverage AI & automation faster calibrated risk decisions... → Risk Review velocity p80 + avg (Monetization Risk Hamish Russell) + Evolve MonRisk Knowledge Base (Sarah Sosiak) actually maps to 4B but kept here for 4A velocity
- Ship MonRisk Forest (DT replacement) → Expand MonRisk Forest (Daniel Harvey)
- Make AI Risk Review agentic + Automate AI Risk decision engine → TBC see comment (Zef RosnBrick)
- Agentic review handles majority of launches → Agentic Review Share (Mateen Saifyan) – in sheet 58 rows for Transform processes AI
- Classic LaMa is retired → Ship (Risk Review Systems)
- Product teams say experience faster clearer less taxing than Classic LaMa → TBD (Risk Review Systems)
- Product teams experience fewer defects and need less support AI answers most questions → Agentic AI Resolution Rate, Agentic Review Defect Rate (Paul Matsiras)
- The most sensitive and important launches move swiftly thanks to process and operational excellence → TBD (Paul Matsiras)
- POs rarely need to answer questions because agents gather and structure product facts automatically → Zero Question Review Rate, Questions per Review p90 (Melvin Smith Sam Bruce)
- POs rarely submit evidence manually and insufficient evidence is rare because agents do it for them → Insufficient Evidence Rate, Manual Evidence rate (Rishabh Sharma DS)
- The orchestrator works reliably end-to-end Many reviews triggered automatically → Agentic %MAD, Automatic Review Trigger Rate (Paul Matsiras, Yunyan Zhang)
- Humans spend significantly less time finding facts and drafting docs for SINs and escalations thanks to AI → In prep + in review wall-time (Karen Krieb)
- We've reimagined escalations: Risk Strategists leveraging AI to drive Escalations at fraction of time → TBD (Karen Krieb)
- Internal and external parties trust our audits to find and fix gaps Every audit feeds agent improvements → Audit relabeling rate, Audit Completion Rate within SLA (Rishabh Sharma DS)
- Unnecessary manual reviews and missed risks are rare because assessment agents highly accurate → Agentic SIN Rate ratio (Jonathan Zhao) + Missed Risk Rate (Rishabh Sharma DS)
- A majority of GRC specialized Risk Assessments are handled via automation → Specialized Risk Assessment Delivery Time (Ashirbad Ghosh)
- Most of work required to respond to Assessor request is automated → Assessor Response Time (Ashirbad Ghosh)
- Manual remediation removed for ~79% PZM Tasks → Task Eng Hours Savings Rate (Alex Irish)
- Incident & Issue management is mostly automated → Issue Closure Time (Shuaimin Kang)
- Most AI systems pass AI Fundamentals quality bar → Quality Bar Assessment (Avi Varadarajulu)
- etc.

**Maps to v3 4A:** Risk review sustainable Missed Risk Rate <7% and xx% SINs under SLO, Agentic Review Share xx% every rollout meets perf benchmarks p90 Questions per Review <yy% User cSAT +xx%, Risk experts handle novel faster L1 Rate reduced xx% Youth AI agents deployed 75-100%, plus from comments: Zero Question Review Rate decreases xx%, SIN Rate decreases xx%, Youth/Risk Review agents meet uptime SLA no outage undetected >2 BD.

### P4 4B – Ship AI-native requirements across all Risk Areas (3 metrics)

- 2.1 Convert Risk Requirements into machine-readable, AI-native form → Accelerate move to AI-native Requirements (Alice Berthaux) – User Risk
- Improve MonRisk Requirement quality → Requirements min bar (Guillaume Aubert) – Monetization Risk
- Improve Requirements Coverage with Legal → Potential requirement gaps evaluated (Liz Keneski, Dave Viner, Guillaume Aubert) – Monetization Risk
- [Risk Harness Goal] Nathan Davis – also 4B

Maps to v3 4B: AI-native Requirements change loop proven requirement change propagates automatically to at least 2 downstream use cases Applicability SIN verification closed feedback loop cyclically.

### P4 4C – Harden controls and scale platform to keep pace with agent growth (18 metrics)

| Human Goal | Metric | Risk Group | POC |
|------------|--------|------------|-----|
| 2.2 Achieve broad coverage by automated, self-evidencing controls and risk identification | 90% of T&C requirements covered by self-evidencing controls | User Risk | Liz Keneski |
| 2.2... | % of reviews that would be “minimal” but for T&C requirements | User Risk | Alice Berthaux |
| 2.2... | T&C Forest rollout to 100% | User Risk | Barnaby Cooper |
| 1.3 Ship the H2 Critical Path Deliverables the business depends on | Ship critical partner commitments | User Risk | Alice Berthaux |
| Reduce time required to maintain T&C Controls, Safeguards, and deliver non-negotiable partner requests | # eng days per month for these activities | User Risk | TBD |
| Manage risks globally with self-evidencing, self-adopting controls rather than bespoke case-by-case. | % controls agentic-ready | Data Risk | TBD (Baris interim) |
| Make controls cheaper + more sustainable; make pod operations + reporting cheap and easy. | Cost-of-compliance (Direct costs, USD) | Data Risk | TBD (Baris interim) |
| Reduce Privacy Wave and other Federated compliance costs. | PG compliance cost ($/EY) | Data Risk | TBD (Baris interim) |
| Create company value where possible and appropriate. | Created company value (e.g. iRev) | Data Risk | TBD (Baris interim) |
| Mature risk solutions and controls | Mature Controls: risk solution progression metrics | AI Risk | Kevin Bauer |
| Mature risk solutions and controls | Mature Controls - AI Risk Control Effectiveness: % Requirement Instances | AI Risk | Kevin Bauer |
| Mature risk solutions and controls | Mature Controls - Minimal MSL Friction: % Model Training Risk Reviews | AI Risk | Kevin Bauer |
| Mature risk solutions and controls | [New] [Ship] Leading metric for BioID requirement | AI Risk | Jiaqi Guo |
| Mature risk solutions and controls (Mature Metrics) | [New] [Ship] Checkpoint Compliance tracking metric | AI Risk | Ning Lok |
| Ship MonRisk controls/verifiers | Deliver remaining controls/verifiers in FTCO scope | Monetization Risk | Dave Viner |
| Automate 3PP Manual Control Reviews | 3PP control automation | Monetization Risk | Garrett Reid |
| Hold the line on Control Intervention for AI Agent Sessions: Prevent regression | Agent Interruptions | Agent Oversight | Aman Mathur |
| Proactive Agent Privacy Detection & Prevention: Close loop | Interception Rate | Agent Oversight | Qinyue Jiang |

Maps to v3 4C: Reduce Risk SEV prevalence agentic+non-agentic double proactive interception Agent-related privacy violations includes SEVs, Harden 90% Tier-1 reqs known SEV patterns, Reduce friction cost agentic workflows observability >=90% reduce top agent interventions auth sensitive data ACL tool networking Diff Phabricator improve precision AO actions hook diff AURA auto-mitigation orchestrate privacy signals in Phabricator, Reduce time/cost maintain Controls Safeguards partner requests 50% where possible create company value e.g., increase iRev.

### P4 4F – Standardize how AI-native pods operate (2 metrics)

- [People Process Goals for AI Transformation] -> People Process Goals (to be curated)
- Users adopt ARP&GRC AI tooling and find them useful for getting their jobs done. → Users adopt ARP&GRC AI tooling useful (Areas Response Platform Risa & Anthony)

Maps to v3 4F: Ensure critical AI systems majority meet AI Fundamentals quality bar xx% systems 100% critical pass bar, Eval Quality all top-priority AI launches rigorous evals SMEs embedded >=1 pod runs rigorous eval E2E using only CoE resources without direct coaching.

### P4 4G – Strengthen talent density (0 metrics currently – needs decision)

- Created company value iRev and PG compliance cost $/EY could be mapped to 4G per description Strengthen talent density? But v3 4C already mentions iRev. Currently mapped to 4C. 4G has no metrics in sheet yet – may need new metrics for talent pools growth (Zef, Stephanie, Varies, Abhishek, Kazuho Ozawa) and preventable attrition.

## Export Plan (per Q1-Q7 decisions)

**Native:** YAML at `projects/risk_goaling_h2_2026/scorecard.yaml` – source_of_truth_direction: Sheet+Docs → YAML augmented preserves manual mappings + values history → exports to clean docs – Option 1.

**Detailed export:** `docs/scorecard_detailed.md` – columns Metric Name | Human Goal | Risk Group | POC | Goal/Tracking | Latest Value | Target | M360 Link | v3 Goal ID | Data Risk P | NSM | Def Status – 108 rows – plus CSV for Sheets re-import – values over time tracked in YAML `values:` list with date, value, status, source, comment – future M360 pull via `meta m360.metric` or `meta unidash.dashboard view` when links provided.

**Summary export:** `docs/scorecard_summary.md` – simplified markdown grouped by PRIORITY (P1-P4) → Goal ID (1A 1B 2A etc) – each group table with minimal fields Metric Name Human Goal Risk Group POC Goal/Tracking Latest Value Target M360 Def Status + Count + Risk Groups – designed to pair with v3 doc static descriptions which won't change.

**GHTML export:** `docs/scorecard_summary_ghtml.html` – same summary as ghtml table with data-col-widths row background colors ready for `meta google.docs apply --from=file://... --base=file://...base --write-mode=suggest` to v3 doc tab t.94anu86ip79a (or new tab for live values).

**Refresh flow:** `python scripts/generate_risk_scorecard.py --refresh-sheet` pulls latest CSV via meta CLI export, merges preserving manual v3_mapping + data_risk_mapping + values + m360_link, reports added/removed metrics for curation.

**Next steps for curation:**
- [ ] Review P1 1A vs 1B split – Keep SIN within SLO mapped to 1B but also appears in 4A sustainable – may need dual mapping or decide primary is 4A? Currently 1B for Data Risk, 1A for User Risk same metric name % SINs under SLO appears twice (Data Risk Scott Murani + User Risk Alice Berthaux) – both mapped 1B and 1A respectively – may want both map to 4A or keep as is with comment.
- [ ] Confirm 1C – 0 metrics – should high-harm Security/Integrity CSAM have metrics? Add if needed.
- [ ] Confirm 3C – 0 metrics – Ship AI Governance framework – add ship goals if any in sheet marked Ship Goal but not yet mapped.
- [ ] Confirm 4F (2 metrics) and 4G (0 metrics) – People Process Goals and ARP&GRC tooling currently in 4F per heuristic but could be 4G or separate – need decision with Baris + Nathan.
- [ ] Add M360 links over time – you will provide – we will then add pull logic (Presto/Hive or M360 API) to populate values at specific dates – generator will show latest value.
- [ ] Finalize target values currently empty for many rows – sheet column Goal Target / Exit Condition – we truncated to 150 chars – should pull full target into YAML for detailed tracking.

