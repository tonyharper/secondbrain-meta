<!-- Source: https://docs.google.com/document/d/13kB1O6D_HQZhZaTcYJ9EEzInXbpEihVcW-QCM0K1wa0/edit -->
<!-- Title: Data Access Friction Review - Brady Preread (3/3/26) -->
<!-- Accessed: 2026-03-31 -->

# Data Access Friction Review - 3/3/26

## 0. Summary

### Summary

- Meta reduced company-wide data access friction by 33% in 2025, outpacing growth and expansion.
- H1 2026 focus: maintain friction improvements in Data Warehouse, drive further reductions in Intern Tools and other asset classes, and proactively manage new friction from AI Agent adoption.
- 2026 YTD friction hours have regressed by 25%, driven by new tools, security controls, and AI Agent development.
- AI Agent adoption is rapidly changing access patterns, with ~20% of friction regression attributable to agent development and usage; ongoing measurement and mitigation efforts are in progress.
- Investments underway: expanding AI automation, optimizing review processes, and aggregating common access needs.

### Discussion Points

- Dan May and George Schnabel - Discussion of headwinds and AI Friction strategy
- Can Lin - Update on Claude Code and DSS-4 data (will voice live)
- Tony Harper - We believe Data Warehouse manual human-generated friction has reached a good place (recent SEV aside), and we propose to hold the line on this and focus on agent friction. Do you agree or disagree?
- Tony Harper - How does Brady foresee the evolution of agents accessing tools and data, and are we missing anything significant from his vision / forecast here?
- Tony Harper - We propose quarterly check-ins with this group if all are aligned.

## 1. Recap of 2025 Progress & H1 Plans

### H2'25 Results

*Source: [SPARE Dec 2025 Executive Review](https://docs.google.com/document/d/119YDl1kmGWeBcbqIDdbLPNWe7IYeRhkz4QvK-kyb0NI/edit?tab=t.0#heading=h.k2nl6bz443dl)*

We exceeded the goal we set to reduce company-wide access friction by 33%, despite 25% organic growth and ~10% workforce expansion:

Results of 12/15/25:

| **Surface** | **1+ Day Interruptions** | **Friction Hours** |
| --- | --- | --- |
| **Data Warehouse** | 40.8k (-57.3% y/y) | 186.4k (-48.5% y/y) |
| **Intern Tools** | 17.4k (-48.9% y/y) | 91.5k (-37.6% y/y) |
| **Other Surfaces** | 26.2k (-24.4% y/y) | 172.4k (-3.0% y/y) |

## 2. 2026 H1 Plan

Having driven significant improvement in friction in 2025, our key focus in H1 is to **hold the line** on Tech FTE friction.

This maintains our H2'25 gains on Data Warehouse while further driving down friction on Intern Tools & other asset classes along with measuring and proactively mitigating growth from AI Agents.

In spite of these plans - **if friction continues to grow at rates exceeding 10% per month, this growth will exceed our ability to drive counterbalancing reductions at current investment levels.**

### 2.1 Emerging Challenges

Several ongoing challenges have led us to evolve our strategy to manage friction going into 2026:

| **Problem** | **How We Are Adapting** |
| --- | --- |
| **Friction is regressing faster than expected** / H2 organic growth 25% (excl DW) versus expected 15% / Driven primarily by new asset & control creation (non-DW) | Guard-rails to maintain friction at current levels and monitor regressions with solutions to limit friction growth |
| **"Other" access friction is higher than 2024 levels** / Most access still not centrally managed | Centralize and optimize through AI and role-mining algorithms |
| **AI adoption is creating new friction patterns** / 40% increase in Daiquery usage, and we estimate AA/Datamate usage to now be 2x Daiquery / Anticipate >30% friction growth in H1 without action / Long-term friction growth from Agents may be much higher | Measure the impact of agent usage and ensure product development velocity is optimized. DW shifts focus to reducing agents' data access friction and risk. |
| **Other forms of friction remain impactful** / Google Drive proportionally more significant as DW+Intern friction decreases | Understand other friction types such as G-Drive (remedial work only after G-Chat migration completed). |

## 3. YTD Progress/Regressions

**Tech Access Friction Hours Total**

*(Chart: Tech Access Friction Hours Total)*

**Tech Access Friction Hours per Person**

*(Chart: Tech Access Friction Hours per Person)*

| **Surface** | **Current Tech Friction Hours** *(2026.02.23)* | **Hold the Line Goal** *(EOY 2025 friction level, Seasonally Adjusted)* |
| --- | --- | --- |
| Data Warehouse | 252k (+15%) | 219k |
| Intern Tools | 137k (+41%) | 97k |
| Other Surfaces | 265k (+23%) | 216k |
| **Overall** | 654k (+25%) | 523k |

We are currently above our hold-the-line target across all surfaces. Investments in addressing friction stemming from the growth of AI usage are our focus for the remainder of the half.

### 3.1 Regression Drivers

| **Surface** |  | **Regression** | **Causes (preliminary)** |
| --- | --- | --- | --- |
| Data Warehouse |  | +33k | **Potentially transient:** Resolved SEV + temporary ACLs |
| Intern Tools |  | +40k | **Proliferation of New Tools:** Rapid growth in friction accessing new internal tools |
| Other Surfaces | Tail ACL Types | +22k (+18%) | **New Security Controls:** Incremental friction where Security has added controls (TAO, MySQL) / **Agent Development:** Substantial friction from new asset types related to AI Agents / **Vibe Coding:** Incremental friction for core infra asset types, esp from non-SWE |
|  | Permission Groups | +16k* (+50%) | **TBD**; *historical data for many Permission Groups begins in March so baselines are not fully trustworthy. Plan to revisit in ~3 weeks. |
|  | Access Management Platform | +3k (+5%) | **N/A** |

### 3.2 Key Investments in H1

[Key Investments](https://docs.google.com/document/d/1YDabIg0ZBgtD42GUe4mAaNIWBahsl6ahQr23A7P1dfs/edit?tab=t.0#heading=h.vm09jsd4k8aw):

1. Expand AI Automation of access configuration and request review to reduce request volume and wait times for review
2. Optimize notifications content, format, and cadence to reduce reviewer non-responsiveness
3. Expand + optimize OSCAR (scaled review) to speed review processes
4. Aggregation & batching of common vibe-coding needs into as few decision-points as possible
5. White-glove access optimizations for MSL + emerging hotspots

The team is currently investigating what additional investments or accelerations could be made to address these regressions. We note that these were not confirmed until holiday seasonality ended earlier this month and had not been root caused until very recently, so we expect further friction optimizations to emerge over the next few weeks.

## 4. Claude Code & DSS-4 update

**Context:** Our AI agents (like Claude Code) are currently blocked from the DSS-4 data they need — including operational logs in Presto and Scuba. This block, triggered by S609546 and S622463, stops us from automating high-value work. To fix this while managing risk under AIR1460: AI Agents Handling DSS-4 Ops Logs, we are moving toward a secure-by-default architecture.

**What We Propose:** We have a three-phase strategy to securely unlock these capabilities:

1. **Immediate (Completed):** With support from Privacy and Security leads, we allowlisted integer user IDs as a temporary measure to keep work moving before the final AI risk decision.
2. **Short-term:** We are partnering with Claude Code, Privacy Infra and Risk to address the privacy and security risk in AIR1460 and moving the proposal to an L2 risk review. If approved, this enables us to use operational logs with temporary safeguards. We are also securing agents data processing based on Metamate Secure Mode.
3. **Mid-term:** We are working with Security, Privacy Infra and Claude Code to build "Sensitive Mode" for Claude Code — a secure environment similar to Metamate Secure Chat. Approved under AIR1459, this adds E2E encryption and strict data retention so agents can handle DSS-4 directly.

This moves us away from manual blocks and toward a system where our agents can safely handle sensitive data at scale.

## 5. AI Agent Friction

The internal Access ecosystem is evolving very quickly as AI Agents change the shape and usage patterns of our internal workforce. We'll need to continuously update our understanding and react, while navigating execution tension between doing this work and managing evolving access risks related to AI Agents.

Note: given that the use of AI tools at Meta is growing and changing quickly, the analysis below is nascent and will evolve.

### 5.1 Human Access Friction Regressions due to AI

**Expected growth:** We expect workforce access friction will grow 2-10x if/as expected AI Agent productivity gains materialize:

1. **Friction scales with incremental activity:**
   - **(Incremental Activity)** Access friction occurs proportionally to the amount of access people *use*. As people are able to get more work done, they will use more access and experience more access friction in proportion to their incremental productivity.

2. **Friction scales with novelty of activity:**
   - **(Role Changes)** People increasingly need access outside of their roles' historical usage patterns, which is often not pre-provisioned and challenging to predict at scale.
   - **(Vibe Coded Assets)** As the cost of creating new assets lowers, we may see a proliferation of new assets with less re-use of each asset. Access is generally configured per asset, so cost per usage event will increase if consistency of access usage declines.

*Timeline TBD.* This growth would occur as AI agent rollout and productivity gains materialize, so the timeline for this growth is unknown and expectations are rapidly evolving. The business will also face risk/friction tradeoff decisions along the way that influence the ultimate friction landing point.

**Observed growth:** Directional data suggests at least half of the ~25% regression YTD is attributable to AI Agents. Acknowledging some uncertainty in attributing causes to friction events, we believe it breaks down roughly as follows:

1. **Vibe Coded Assets:** People are creating more stuff faster, which then creates risk & friction
   - On Internal Tools, currently ~45k friction hours from tools created in the last 6 months vs expected ~15k; new tools make up 33% of internal tools friction vs historical average ~15%.

2. **Development of AI Systems:**
   - On "Other" ACLs, ~50% incremental friction hours YoY related to AI Agent development, mostly from novel AI infrastructure asset types. The rate at which we are standing up new infrastructure classes which then require access optimization is accelerating.

3. **Role Changes / Vibe Coding Users:**
   - ~20k (X incremental) on access to core engineering tech stack + additional ~3k on Tail ACL types likely attributable to vibe coding.

4. **Incremental Activity:** Not yet known. It's not consistently possible today to either show that a specific bit of activity was incremental beyond the above categories or to rule out all other potential causes of a given class of friction.
   - ~30% of Data Warehouse access requests now come directly from agentic sessions.

### 5.2 Establishing AI Agent Observability (E2E and for Access Friction specifically)

Central security's Security 4 AI ("S4AI") v-team is leading the S4AI Agent Observability workstream to enable:

- **Telemetry** to capture the interactions between the Ecosystem of AI Agents at Meta and Meta's system of Security controls
- **Measurement** to capture the risk and friction of associated interactions.

Establishing an **ETA for this effort** is challenging due to its breadth and the dynamic nature of the AI usage so our prioritization is subject to change. Currently, for H1'26 we are prioritizing Telemetry and Measurement for Access Controls in key Agent platform segments:

| **Security Control Type** | **Claude Code (2P)** | **Devmate (1P)** | **Metamate (1P)** | **Manus (1P/3P)** | **C8 (1P)** | **N8N(3P), BloksLab(1P), Bespoke(1P), IntegrityMate (1P), Manus (External)** |
| --- | --- | --- | --- | --- | --- | --- |
| **Access Controls** | P1 / Rolling out currently (~10% of global traffic) / ETA: March 2026 |  |  | P1 / ETA Q2'26 | Live | P2 |
| **Alignment Guardrails** | Live |  |  | P2 | Live | P2 |
| **Boundary Guardrails** | P2 | P2 | P2 | P2 | P2 | P2 |

Our planned **definition of friction for AI Agents** is as follows:

| **Metric Type** | **What is this metric answering?** | **Metric** | **Definition** *(in development)* |
| --- | --- | --- | --- |
| **Friction** *(leading indicator)* | *How much friction is Security adding to Agent usage at Meta?* | **Agent Security Interruption Rate** | % Agent interactions (prompt cycles = turns) impacted by security controls |

We are working with partner teams to ensure the definition is compatible across several efforts (AI4W effort, SPARE, Reliability Engineering tracking). We will be opportunistic in conducting exploratory analyses into other cost classes such as latency, compute, or reduced autonomous task success rate to validate whether stop rate is a sufficient proxy for AI agent costs.

As the measure of Agent friction (and the Access Friction segment specifically) comes online we expect to add the signal into the SPARE effort to enable cross-prioritization of efforts.

### 5.3 Plans for Managing AI Access Friction

*Disclaimer: this is a rapidly evolving space and the plans below are subject to change (e.g. due to emergence of new Agent Platforms and Security solutions)*

In the immediate term, we expect the dominant share of friction for AI agents will be via interactive sessions, which currently inherit (and scale up) the interactive user's access needs and so inherit existing friction challenges. In the middle to long term, we will need to extend solutions increasingly to autonomous agents, with many unknowns to solve for along the way.

We (across several v-team efforts) are currently investing in a mixture of traditional levers, high-confidence bets and rapid cycle pilots to manage risk/friction trade-off associated with AI Agents.

**Traditional levers:**
- Targeted friction reduction campaigns to update standing access

**High-confidence Bets Leveraging AI:**
- Automated evaluation of access requests: AccessMate, which is an AI Agent, helps facilitate smooth and efficient navigation of access blockers where it is integrated
- Automated solutions to configure standing access: LLM based evaluation of Risk/Friction trade-offs to configure the optimal standing access settings and update as usage patterns evolve

**Rapid-cycle piloting to iterate on novel solutions to leading edge problems:**

Examples of frameworks considered as part of planned piloting in Security 4 AI v-team (planned 90 day sprint for Claude-Code):

- Per-session controls ("Agent X is running code downloaded from public internet in session Y, and therefore should not be able to access user data during session Y")
- Super-user access for agents paired with controls on what agents pass back to users
- Agentic supervisors embedded in agent sessions
- etc

As friction data becomes available (and we learn from the planned rapid cycle pilots) we expect to prioritize amongst these (and other) solutions to optimize the Risk/Friction trade-off for AI Agent ecosystem at Meta.

## Appendix

### 1.1 Topline Metrics

| **Tech FTE Access Friction (12/15/25)** | **H2 Seasonal Baseline** | **Current (L28)** | **P90 Goal (33%)** | **P50 Goal (50%)** |
| --- | --- | --- | --- | --- |
| **Interruptions** | 3.88m | **1.36m (-65%)** | Pass | Pass |
| **1+ day interruptions** | 164k | **84.4k (-49%)** | Pass | Near *(L7 > 50%)* |
| **Estimated total friction hours** | 683k | **448.9k (-34%)** | Pass |  |

Baselines are adjusted for seasonality.

### 1.2 Countermetrics

| **Countermetrics** | **EOH1 Baseline** | **12/15** |
| --- | --- | --- |
| **Residual Access Risk** *(Experimental)* | 6.4% | 6.8% |
| **ACL SEVs caused by SPARE** | N/A | 1 |

The change in RAR was within acceptable risk tolerance.

### 1.3 Breakdown Per Surface

As of 12/15/25, L28 friction metrics per surface:

| **Surface** | **1+ Day Interruptions** | **Friction Hours** |
| --- | --- | --- |
| **Data Warehouse** | 40.8k (-57.3% y/y) | 186.4k (-48.5% y/y) |
| **Intern Tools** | 17.4k (-48.9% y/y) | 91.5k (-37.6% y/y) |
| **Other Surfaces** | 26.2k (-24.4% y/y) | 172.4k (-3.0% y/y) |

### 1.4.2 User Sentiment

UXR completed qualitative, semi-structured interviews with tech FTE (DE, DS, SWE) experiencing significant friction (n=15). Interview findings, which should be interpreted directionally, suggest that:

1. **Friction sentiment is trending toward acceptable**, with auto-approvals cited as a key relief valve. Most participants reported increased auto-grants over time and viewed autogrant access favorably and minimally disruptive.
2. **Perceptions of access friction are shaped, in part, by understanding of the context and whether the friction seems appropriate.** Findings suggest a greater tolerance for friction when it was understood as protecting sensitive user/employee data, while friction was viewed more negatively when it felt miscalibrated (e.g., misaligned with role-based work requirements, delayed time-sensitive tasks).
3. **Manual-review delays cause dissatisfaction due to wait time and added resolution effort.** When access friction triggered manual review and approval flows, most participants reported managing this friction in ways that required additional time and effort — including manual follow-up with on-calls or exploring alternative approaches — or abandoning the task.
4. **Friction is more acute during novel or exploratory work** — such as metric development, pipeline debugging, on-call support, and SEV investigations — where access needs are varied, unpredictable, and often urgent.

We will continue to monitor ongoing sentiment developments, detect regressions, and identify remaining "hot spots" of access friction (e.g., via DevEx and DataEx surveys).
