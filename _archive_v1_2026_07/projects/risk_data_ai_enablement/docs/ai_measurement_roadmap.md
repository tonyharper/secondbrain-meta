<!-- Source: https://docs.google.com/document/d/1l0ZzOslLNLVogWlGCZoEJh3lakMpbZ2nV8ETsaNfsp4/edit -->
<!-- Title: Risk DE AI Measurement Roadmap -->
<!-- Date Accessed: 2026-03-31 -->

# Risk DE AI Measurement Roadmap

QB: Swetha Singiri | Team: Lakshmi Chinta

Ref: WS5: Risk Insights & Governance | AI Data Stack Measurement Strategy

---

## Mission & Context

Our mission is to enable better and faster business outcomes for the Risk DE Org by delivering trusted, reliable, and timely AI-powered responses at scale -- measured through a rigorous, continuously improving evaluation and observability framework.

We are collaborating with the AI Infra & CPP teams to establish a scalable data foundation, which will support various use cases across the Family of Apps (FoA), including those within the Risk organization. The primary objectives of this partnership are to guarantee the consistency and reliability of our metrics and to accelerate development through shared responsibilities across teams. This approach prioritizes flexibility, allowing individual teams and organizations to maintain different goaling strategies tailored to their specific use cases, while still ensuring a common standard for shared themes.

## Out of Scope

- Risk XFN AI measurement use cases are out of scope of this document.

## Objectives

| **Objective** | **Description** | **High-Level Deliverables** | **Success Criteria** |
| --- | --- | --- | --- |
| **O1. Finalize Metrics & Definitions** | Develop canonical measurement and finalize metric definitions. | 1. Measurement plan published (Doc) by 02/18. 2. Definitions finalized across metric themes by 02/28. 3. Measurement alignment with WS4: Monitoring & Oversight by 02/28. | Measurement plan and metric definitions reviewed and adopted. Metrics are comprehensive and aligned. |
| **O2. Data & Logging Foundations** | Build scalable, reusable data foundation; close logging gaps. | 1. Logging gap analysis and remediation plan for P0 metrics by 02/28. 2. For all P0 metrics, initial scalable data foundation delivered in partnership with AI Infra by 03/06. 3. P0 metrics implemented in M360 by 03/06. 4. P1 metrics -- fix logging gaps, build data foundation and define Metrics by 03/30. 5. Support new metrics based on learnings and feedback in Q2. | All critical data gaps closed. Data Foundation supports unified measurement and can easily scale to new use cases. Metrics tracked in M360. |
| **O3. Deliver Dashboards** | Provide dashboards for progress tracking and strategic insights. | 1. Deliver Exec dashboard with P0 metrics by 03/15. 2. Deliver Deep-dive dashboard with P0/P1 metrics by 03/30. 3. Deliver Manager insights dashboard with P0/P1 metrics by 03/30. 4. Enrich dashboards with new metrics based on learnings in Q2. 5. Publish Documentation/user guides by 03/15. | Dashboards live and actionable. Documentation published. |
| **O4. Learn, Iterate & Enrich** | Continuously improve the framework based on feedback and learnings. | 1. Continuous Feedback review sessions. 2. Continuous Improvement backlog prioritization. 3. Continuous -- Enriched foundation, metrics, dashboards. | Feedback incorporated. Prioritized Improvements delivered. Learnings shared across teams. |
| **O5. Org Visibility & Communication** | Ensure clear visibility into progress, trends, and opportunities. | 1. Measurement FAQ. 2. Monthly updates post. 3. End-of-H1 readout. | FAQ and updates published. Communication timely and actionable. |

## Metric Themes

| **Theme** | **Description** |
| --- | --- |
| **M1.0 AI Adoption** | Ensure Risk DEs are using AI to generate at least 75% of diffs. Metric is defined as Percentage of Risk DEs who published diffs with >=75% AI characters in the last 7 days. |
| **M2.0 Eval Quality & Representativeness** | Ensure our evals are comprehensive, testing the right things, and accurately measuring the quality of AI agent responses. |
| **M3.0 Asset Coverage** | Ensure our most critical business assets (tables, dashboards, metrics) are covered by the AI data stack and corresponding evals. |
| **M4.0 Adoption & Impact** | Measure whether users are adopting SM-backed AI agents, if they are retained, and whether the AI is making a difference. |

## H1 Roadmap & Milestones

### Overall Milestones

| **Deliverable** | **Objective** | **Target Date** |
| --- | --- | --- |
| Measurement plan published | O1 | Feb 18 |
| Metric definitions finalized (all themes) | O1 | Feb 28 |
| Logging gap analysis and remediation plan | O2 | Feb 28 |
| Initial P0 data foundation landed (in partnership with AI Infra) | O2 | Mar 06 |
| Logging gaps fixed | O2 | Mar 16 |
| Exec Dashboard live (P0 metrics) | O3 | Mar 16 |
| Dashboard documentation and user guides published | O3 | Mar 20 |
| Deep-dive Dashboard live (P0/P1 metrics) | O3 | Mar 30 |
| Manager Insights Dashboard live (P0/P1 metrics) | O3 | Mar 30 |
| P1 data foundation and metrics implemented | O2 | Mar 30 |

### Metric Specific Milestones

| **Metric Theme** | **Metric** | **DE POC** | **Tier** | **M1 -- Mar 6th** | **M2 -- Mar 16** | **M3 -- Mar 30** | **M4 -- Apr-Jun 30** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **M1.0 AI Adoption** | eWAU@75 | Lakshmi | P0 | Definition finalized. Data foundation landed. Baseline established. | Dashboard live. | Improvement plan. | Improvement plan. |
| | eWAU@75 Dimensional analysis | Lakshmi | P0 | Data foundation landed. | Dashboard live. | Improvement plan. | Improvement plan. |
| | eWAU@75 Manager Insights | Lakshmi | P0 | Data foundation landed. | Dashboard live. | Improvement plan. | Improvement plan. |
| **M2.0 Eval Quality & Representativeness** | Eval Pass Rate | Swetha S | P0 | Definition finalized. Data foundation landed. | Dashboard live. | Baseline established. Improvement plan. | Improvement plan. |
| | Eval Distribution (JTBD, difficulty level) | Swetha S | P0 | Definition finalized. Data foundation landed. | Dashboard live. | Improvement plan. | Improvement plan. |
| | Eval Coverage (offline vs online Evals) | Swetha S | P0 | Definition finalized. Data foundation landed. | Dashboard live. | Improvement plan. | Improvement plan. |
| | Test vs Holdout Delta | Swetha S | P1 | -- | -- | Definition finalized. Data foundation landed. Baseline established. | Improvement plan. |
| | Eval Distribution (by semantic model, by domains) | Swetha S | P1 | -- | -- | Data foundation landed. Dashboard live. Improvement plan. | Improvement plan. |
| | Empty Response Rate | Swetha S | P1 | -- | -- | Definition finalized. Data foundation landed. Baseline established. | Improvement plan. |
| | Baseline vs SM Delta | Swetha S | P1 | -- | -- | Definition finalized. Data foundation landed. Baseline established. | Improvement plan. |
| | Avg. Response Time (Latency) | Swetha S | P1 | -- | -- | Definition finalized. Data foundation landed. Dashboard live. | Improvement plan. |
| | Cross-Tool Consistency | Swetha S | P1 | Definition finalized. Logging approach scoped. | -- | Data foundation landed. Dashboard live. | Improvement plan. |
| **M3.0 Asset Coverage** | Tier 0/1 Dashboard Coverage | Swetha S | P0 | Definition finalized. Data foundation landed. | Dashboard live. | Improvement plan. | Improvement plan. |
| | Critical Table Coverage | Swetha S | P0 | Definition finalized. Data foundation landed. | Dashboard live. | Improvement plan. | Improvement plan. |
| | M360 Metrics Coverage | Swetha S | P0 | Definition finalized. Data foundation landed. | Dashboard live. | Improvement plan. | Improvement plan. |
| **M4.0 Adoption & Impact** | Agentic DAU/WAU/MAU | Swetha S | P0 | Definition finalized. Data foundation landed. | Dashboard live. | Improvement plan. | Improvement plan. |

### Continuous Improvement & Communication Milestones

| **Deliverable** | **Objective** | **POC** | **Cadence / Target Date** |
| --- | --- | --- | --- |
| Measurement FAQ published | O5 | Swetha S | Mar 15; updated each milestone |
| Progress update post | O5 | Swetha S | Monthly throughout H1 |
| Feedback review session | O4 | Swetha S / Lakshmi | Throughout H1 |
| Improvement backlog prioritization | O4 | Swetha S / Lakshmi | Throughout H1 |
| Enriched metrics and dashboards based on learnings | O4 | Swetha S / Lakshmi | Throughout H1. Deliver all priorities by May 30 for end of half readout |
| End-of-H1 goal readout | O5 | Swetha S | Jun 30 |

### List of Domains Onboarded

| **#** | **Domain** | **Use Case** | **POC** | **Status** |
| --- | --- | --- | --- | --- |
| 1 | Age Reconciliation | | Swetha Singiri | Landed |
| 2 | MADE | | Sainath | In Progress |
| 3 | Age Modeling | | Trevina | In Progress |
| 4 | Cross-Age Measurement | | Ashish Mangaj | In Progress |
| 5 | Compliance Graph | | | |
| 6 | Cost of Compliance | | Sunil Rathode | Landed |
| 7 | FlyWheel | | | |
| 8 | Risk Review | | | |
| 9 | Accessibility | | | |

### Other Workstreams

1. Context Engineering Pod -- Metrics Framework
2. [RFC] LLM-Based Prompt Classification for Semantic Model Coverage Assessment
