
# [Canonical] Agent Friction - Privacy, Infra and Security Alignment Details


**Status: Aligned (as of Mar 16, 2023)**

**STO**: Wenlong Dong, Can Lin

**Quarterback**: Anisha Patel

**Program Stand Up Support**: Haya Al Nmeir, Simon Jones

**x-org Leads**: Jonathan Bergeron(PI)Komal Mangtani(AIDR)Simon Jones(Security)+ Sushaant Mujoo(Agentic Oversight TPM Lead) + Alex Ponomarenko(PI Lead)+ Can Lin(AIDRE Lead)

## Problem


As AI agent adoption accelerates across Meta, **agents are hitting privacy and security walls that slow or block critical workflows** — affecting every major platform: Claude Code, DevMate, Metamate, Confucius, and others. Issues span agent identity, data sensitivity classifications, filesystem permissions, security constraints, and inconsistent access parity.


SPARE drove Tech FTE access friction down 33% in H2'25 — but agent friction introduces new challenges SPARE wasn't designed to address. Total tech access friction hours have risen to 654K (+25% vs. 523K seasonally-adjusted baseline), with regressions across Data Warehouse (+15%), Intern Tools (+41%), and Other Surfaces (+23%). ~30% of Data Warehouse access requests now originate from agentic sessions. At least half of the regression is driven by AI agent adoption and vibe coding: tool proliferation accelerating 83% faster YOY, new ACL types for agentic development, and role expansions during active coding sessions. Early predictions suggest workforce access friction could grow 2–10x due to agent-driven productivity gains if no action is taken.


Building on SPARE's foundation — proven measurement frameworks, existing cross-org partnerships, and the Agent Access Friction Tiger Team work already underway — FRAPS stands up a lightweight x-org structure to tackle agent governance, friction reduction, and policy at scale.

## **Strategy**


1. **Identify, detect, and triage** frictions from different sources
  1. Manual reporting & requests
  2. Detection, measurement, and monitoring: build on top of WS1 ([**Agent Observability**](https://fb.workplace.com/groups/agent.sec.vteam/permalink/4309480679298808/))
    1. WS1 Materials on Observability (Agent Interaction with Security :
      1. [**S4AI Observability Analytics Agent**](https://www.internalfb.com/analytics-agent?recipeID=729126150167126 )** : **Analytics agent with appropriate semantic layer (recipe) 
      2. [**S4AI Observability Canonical Dashboard**](https://fburl.com/unidash/jb3epc2t)
      3. **fct_agent_security_traces:security** 
  3. Prioritize & triage capabilities and frictions
  4. Drive friction / risk reviews to re-establish new usage patterns (e.g. DSS-4, MacOS)
2. **Enable **security and privacy controls and reduce friction for Meta CLI, with quick actions from the PI Tiger Team
  1. Integrate security & privacy with Infra systems
  2. Build controls and allowlisting for different environments (corp, dev, prod)
3. **Reduce **agent data access for Warehouse systems
  1. Optimize agent DW access w/ or w/o human approvals
4. **Reduce** intern tools & other infra access friction
  1. Optimize agent Intern and non-DW access w/ or w/o human approvals
## **Workstreams**


| **#** | **Workstream** | **STO** | **Involved Orgs** | **Roles & Accountabilities** | **Specific deliverables** | **Objectives (WS STO’s to add) (ETA: **Mar 17, 2026**, EOB PT)** | **Key Results  (WS STO’s to add) (ETA: **Mar 17, 2026**, EOB PT)** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **1** | **Identify, detect, and triage **frictions for agents | Wenlong Dong (Privacy Infra) / Can Lin / (AIDRE) | Privacy Infra (Rachel Lee) / AIDRE (Can Lin) / [consulting] Security (Tola Dalton) / Measurement (Tony Harper, Harsh Asher and George Schnabel to identify POCs) / TPM: Anisha Patel (Overall); Aaron Morris (Measurement) | Identify and prioritize frictions / Lightweight intake for <u>all</u> agent friction caused by security & privacy controls / Routes problems to WS2a/b/c /  | Measurement of workflow session interrupts | O1: Overall measurement strategy and prioritization | KR1.1: Establish top-line agent friction metrics, measurement plan, and define agent centric measurement (i.e access, data, security)  |
|  |  |  |  |  |  | O2: Land a coherent tech strategy to reduce agent friction for  security and privacy | KR2: Defined and published tech strategy with established high level frameworks to guide rest of the workstreams |
|  |  |  |  |  | Intake & prioritization for user-reported friction / papercuts / LLM analysis of agent traces to summarize common friction points | O3: Intake / routing of user reported agent friction complaints | KR3:  / Dependency on overall measurement and common set of data sources / *To-do: (i) framework to determine stack ranking and phasing the work, (ii) LLM analysis of agent traces to summarize common friction points* |
|  |  |  |  |  |  | O4: Establish topline goals for agent friction reduction and ensure successful delivery, run the business/FRASP effort (i,e comms etc) | KR4.1: Define and communicate H2 topline friction reduction targets / KR4.2: Achieve X% reduction in overall agent friction score / KR4.3: Drive execution and stakeholder comms  |
|  |  |  |  |  | Drive friction / risk reviews to re-establish new access patterns (e.g. DSS-4) |  O5: Drive risk reviews to re-established new access patterns (e.g DSS-4) |   KR5: TBC |
| **2** | **Enable **security and privacy controls and reduce friction for Meta CLI (WS2a) | Yimo Tao | Privacy Infra (Yimo Tao) / Infrastructure Security Engineering (Eden Zik) / [consulting] Security (Chris Puderbaugh) / DS: Aman Mathur / **TPM:** Aaron Morris | Enable security and privacy controls and reduce friction for Meta CLI | Establish identity flows and trust controls at the command hub / Optimize tool/skill issues (eg. allowlisting safe tools/internet domains) / Optimise non-access constraints (eg. sandboxing) | **O1: **Establish friction measurement for Meta CLI developer and production workflows | **KR 1.1: **Establish baseline friction measurement for CLI developers and production users including separation of expected friction (DSS4 blocking access to sensitive data) / **KR 1.2:** Deploy automated friction discovery pipeline for CLI trust/access errors |
|  |  |  |  |  |  | **O2:** Build [trust framework](https://fb.workplace.com/groups/1546541073105310/permalink/1574630013629749/) and safety guardrails for CLI as agent infrastructure | **KR 2.1**: Standardize destructive operation guardrails across commands  / **KR 2.2: **Inventory and understand [risks of](https://www.internalfb.com/diff/D97233805?entry_point=19)[ Meta CLI](https://www.internalfb.com/diff/D97233805?entry_point=19)[ commands ](https://www.internalfb.com/diff/D97233805?entry_point=19)  / **KR 2.3:** Build role-based access control into CLI service layer / **KR 2.4: **Unify agent guardrails into CLI Trust layer |
|  |  |  |  |  |  | **O3**: Reduce Meta CLI framework-level friction | **KR 3.1: **Enable Meta CLI across [Mac](https://docs.google.com/document/d/1MpZ0rA2f3SXVUGuT8S9PkoWf4M-mU-P--B3mzyOvzxI/edit?tab=t.0#heading=h.4oi7i5x3dhny), Linux, and Sandcastle environments. / **KR 3.2: **Align with Intern Tools permission model to reduce per-platform friction |
|  |  |  |  |  |  | **O4:** Reduce command execution friction | **KR 4.1:** Enable EP team to reach coverage goals with a reusable authentication integrations / **KR 4.2:** Reduce unexpected friction from Privacy guardrails  / **KR4.3: **Replace guardrails with server-side protections (Hack-based control) |
| **3** | **Reduce **Agent Data Access Friction (WS2b) | Yanbo Xu | AIDRE (Yanbo Xu) / [consulting] Security (Tola Dalton) / DS: TBD(?) / **TPM:**  Hannah Wang | Reduce data access friction for agents / *(without regressing risk)* | Implement optimization levers where agent access is approved automatically or by humans  | O1: Establish robust, agent-specific metrics and dashboards to baseline, track, and drive friction and risk reduction across all workstreams. / O2: Reduce agent data access interruptions so agents can complete jobs-to-be-done autonomously without human intervention. / O5: Improve agent traffic observability for friction and risk measurement and mitigation /  | KR1.1: Define and instrument agent friction metrics (interruption rate, permission request wait time, task completion rate w/o human intervention) with **session-level** tracking for Claude, in partnership with FRAPS. / KR1.2: Ship a unified dashboard covering friction, risk, and encryption metrics by 4/30 — Evolve Shruti's current dashboard to include session-level friction data, risk exposure tracking (agents accessing sensitive data without isolation domain), and encryption adoption rates — providing a single source of truth for the program. |
|  |  |  |  |  |  |  | KR2.1: Reduce Claude agent interruption rate from 4.1% to ≤2% through AccessMate integration, PDP enablement for non-DSS-4 data, and policy changes for low-sensitivity access. / KR2.2: Ship AccessMate integration for Cloud Code to GA. Complete alpha on 3/20, iterate on capability, and reach general availability so permission requests can be auto-negotiated without human intervention. / KR2.3: Increase AccessMate auto-approval rate for Claude by 50% through improved business reason quality, policy-aligned automation, and reduced average permission request wait time. / KR2.4: Integrate low risk data access patterns in sample rows, column stats, sql authoring through Table Insight service and k-anonymity  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **4** | **Reduce **Intern Tools & Other Infra Access Friction (WS2c) | Tola Dalton | Security (Jiyun Yao) / Infrastructure Security Engineering (Eden Zik) / [consulting] Privacy Infra (Wenlong Dong) / DS: TBD / **PM: **Shane Li | Reduce agent access friction to intern tools & other infra assets (TAO, etc) / *(without regressing risk)* / Measure & track* human access friction* | Implement optimization levers where agent access is approved by humans (eg. notifications) / Centralize access management for intern tools and non-DW infra assets / Deploy 2 AI systems for automated agent access:  / System 1: Predictive grants for identities / System 2: JIT decisions | O1: Use AI to reduce agent friction on Intern Tools and other high-friction asset classes | KR1: SIR precision/recall for top 2 highest friction asset classes (Hive, Internal Tools) exceeds 70%/70% and the remaining Q2 System 1 set (9 asset classes) exceeds X%/Y%. / KR2: [ship, Q1] Measure access friction for Tech FTE usage of agents — Claude, MetaMate, DevMate / KR3: Achieve X% agent access friction reduction on internal tools through use of AI tooling (% agent sessions interrupted x%->y%) / KR4: Achieve X% agent access friction reduction (or hold steady) on other ACLs through use of AI tooling (% agent sessions interrupted x%->y%) / KR5: Reduce Tech FTE access friction to use top agents (Metamate, Devmate, Claude Code, etc…) by X% /  |
|  |  |  |  |  |  | O2: Measure & reduce impact of access friction on Meta AI product development velocity. | KR1: Reduce MSL estimated friction hours per Tech FTE 13.1->6.5. |



