<!-- Source: https://docs.google.com/document/d/1YWbJwk-bW3iQlYdqHFAA6jy3pPxxoKjzCDysoSeQDqc/edit?tab=t.8nnafr41xmz4 -->
<!-- Title: Risk Leads Dashboard Definition -->
<!-- Accessed: 2026-03-31 -->

# Risk Leads Dashboard Definition

**Status**: Discussed with Michel, green light to build

---

## Proposal for "Risk Leads" Dashboard

The "Risk-leads" dashboard is intended to augment the Risk Priorities meeting by providing a high-level view into our risk management capabilities, our compliance capabilities, macro trends, and the cost of risk. Most metrics are intended to be stable, though some can be "focus" metrics, which are swapped in or out based on what's in focus for a given half.

It prioritizes providing a holistic view of the system, versus tracking team progress toward goals. In fact, **some of the data on this dashboard are explicitly not goals**. For example, we would never 'goal' on a T&E volume forecast and feature it rather than "% Triage without Escalation". Similarly, for regulatory readiness, we prioritize metrics that reflect the broader regulatory environment over operational productivity.

This dashboard is intentionally high-level. Once we align on its content, we'll address the separate issue of dashboard navigability.

## Risk-leads Dash

*Audience: Risk leads + anyone else who wants a high-level view*

### Risk Management

Risk review is a control that helps us manage risk and enables Meta to make good product decisions. We must do this without being a bottleneck to the company. To understand how this is going, we propose showing the following:

- A funnel-ish visual showing the **current state of the risk review pipeline**
- **LaMa volume over time**, split by level of friction. Specifically:
  - Historical fully-automated, light-touch, and high-touch LaMa volume
  - Forecasted fully-automated, light-touch and high-touch LaMa volume
- The **Requirement-miss rate** (Definition: "The percentage of required risk factors or requirements that were not identified or addressed during intake or review, but were later found during an audit."). This metric has a one-month lag but is more accurate and less volatile.
- The **insufficient evidence rate** would allow us to keep track of how frequently evidence submissions in privacy reviews fail to meet the required standard during audit.
- End-to-end **wall time over time** (median and 95th percentile)

Taken together, these elements provide an approximate representation of both the current and future state of risk review. The risk-review pipeline visualization is designed to show you the entire system as it exists *now*. Historical LaMa volumes help contextualize past and present trends, while the LaMa volume forecast translates company product development trends (such as developer productivity) into implications for the risk-review pipeline. Requirement miss rate lets us check the quality of intake/review and insufficient evidence rate allows us to monitor the quality of evidence PGs are submitting. End-to-end wall time serves as our best (albeit highly imperfect) proxy for assessing the overall 'state' of the system.

There's another view of risk review which is less about the *state* of the system and more about the experience of each PG. This would go into a different place.

### The State of Our Controls

Even if we are outstanding at making good decisions, we need to make sure we're ensuring compliance with those decisions at scale. We need to better understand the state of our controls (e.g. are they in good standing), the frequency with which issues materially slip through despite our controls. (SEVs).

- For the **state of our controls**, metrics do exist, but Stephanie needs to better understand them and ensure they are fully actionable.
- The number of SEVs is also instructive, and there are two metrics on this front:
  - **Severity-Weighted SEVs**
  - **Externally-Reported SEVs**

  Both can help drive accountability by tracking both SEVs over time. Severity-weighted SEVs will also indicate if a SEV should be attributed to a PG vs. the Risk team (e.g. "the deletion framework code broke" versus "PG implementation was poor"). We recommend using the actual number (rather than a proportion of total Meta SEVs) because our controls should be held to a high standard. Even if total company SEVs increased, we'd still be concerned if risk/privacy SEVs increased under any circumstances.

In the spirit of not bottlenecking the company, we also need to be cognizant of the taxes our controls impose on one of Meta's most precious resources: people's time.

- In the AI4C offsite, Privacy Waves Reimagined, Vibe escalations, and Forest were described as the Top 3 important AI4C bets. The **Privacy Waves Reimagined with AI Savings** metric would be a 'focus' (e.g. temporary) metric that shows the progress made by the Privacy Waves effort against the subset of costs targeted by AI. (Progress around Vibe escalations and forest is tracked via recurring demos.)
- Feedback from AI Researchers is that they experience significant friction in their daily workflows owing to Risk-related controls. Given the importance of MSL as a stakeholder and the velocity at which it operates, we need to understand the non-risk-review impact of Risk/Compliance efforts on that team. Thus, we propose tracking **Researcher Friction** as a focus metric.

### The Macro View (Regulatory/Aggregate)

Ideally, we'd be able to perfectly quantify and map how risk emerges (e.g. from a regulation) all the way through to how it comes to a company's "risk balance sheet." In the absence of that, we propose a distinct section that shows risk inputs and risk 'outputs'.

- **Regulatory inquiries by risk area** will track the volume and nature of inbound regulatory attention, broken down by risk domain (privacy, competition, content, etc.). The idea is that inquiry volume in a particular area is an early signal of where external scrutiny is concentrating and where we may need to proactively strengthen controls or accelerate remediation before inquiries escalate to enforcement actions. It may make sense to zero in on Youth or AI.
- **Aggregate Risk** will provide a single view of Meta's overall product risk posture. While no single number can capture the full complexity of product risk, the idea would be to provide a useful trend line. (e.g. Is our aggregate risk exposure growing or shrinking?)
- **External effective response rate** will track how good we are at demonstrating oversight to regulators.

### Cost of Risk

As responsible stewards of the business, we need to track costs of compliance over time (broken down into different categories). Compliance has quantifiable dollar costs to the business, namely in the form of headcount, federated work, hardware, and operational expenses. The vast majority of this work is people (~90%) and nearly half of those people are outside of risk. **Total Cost of Compliance**, broken down by the categories above and by PG, can be used to track these. In current state we are missing a large amount of federated work, namely due to non-task project work executed by PGs, but this will improve in accuracy over the course of 2026. We recommend tracking this as a focus metric. It should go down precipitously as the company becomes AI Native, and we can consider retiring it once it becomes immaterial.

## Summary of Metrics & Status

**Legend:**

- Ready to ship = Metric exists, and is ready to put on the dashboard
- In progress = Metric work is underway. ETA indicates when it'll be added to the dashboard.
- Under investigation = Metric exists but needs a bit of fine tuning to be actionable
- Focus metric = Metric is on the dashboard given Risk org priorities and will rotate off eventually

### Risk Management

| Metric | Status | Note |
|--------|--------|------|
| Visualization of risk review 'funnel' as it is *today* (e.g. LaMa to Launch) | Shipped to dashboard | Adding non-approved LAMAs to funnel next |
| LaMa volume over time (historical and forecasted) | Historical is shipped; forecasted in progress | |
| End-to-end wall time (median, 95th percentile) | Shipped to Dashboard | |
| Requirement miss rate | In Progress / (ETA March 13) | |

### State of Controls

| Metric | Status | Note |
|--------|--------|------|
| State of controls | Under investigation | Stephanie needs to better understand how we should interpret & action on the existing suite of metrics. |
| Severity-weighted SEVs | Under Investigation | Aligning on metrics definition and adding Youth SEVs |
| Externally-reported SEVs | Under Investigation | Aligning on metrics definition and adding Youth SEVs |
| Privacy Waves Reimagined with AI Savings (Focus) | In progress / (ETA: 3/5) | Blocked by Nest deployment issue on 3/4; hopefully landing 3/5 |
| Researcher Friction (Focus) | In progress / (ETA: March 31) | |

### Regulatory/Macro View

| Metric | Status | Note |
|--------|--------|------|
| Regulatory inquiries by risk area | Under investigation | We need to confirm that inquiries are being accurately tagged with one or more risk areas. |
| Aggregate risk | Under investigation | We are re-thinking how to approach aggregate risk. This is a longer-term, bigger bet. |
| External effective response rate | | |

### Cost of Risk

| Metric | Status | Note |
|--------|--------|------|
| Total Privacy Costs, broken down by category (Focus) | Shipped to dashboard | Currently we have 50% of costs categorized. We will be able to categorize 100% by next year. |

## To Discuss

- End-to-end wall time (see Jackie's comment above)

## Other Dashboards

### Risk Review View by PG

*Audience: Michel (prior to 1:1s or meetings with small group), DRIs that map to a PG*

PG concerns tend to take two forms: (1) questions about a specific escalation and (2) concerns about lack of automation especially when it comes to evidencing. The objective of this dashboard is to contextualize the specific concern at hand. To do so, for each PG, the dashboard would show:

- Open LaMas (by PG)
- % reviews in different buckets of automation (over time)
  - Self cert, auto implement
  - Self cert, manually implement
  - Self cert, requires manual decision loop, manually implemented
  - Very manual / high touch
- For each bucket, p50 and p95 end-to-end duration
  - Note: Need to contextualize this
- List of 'hot' escalations. We need to spend time defining how to identify these.
- Open question: LaMa backlog (# items awaiting review) by PG.
