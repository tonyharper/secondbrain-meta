---
title: Measuring Controls — What We Report and at What Grain
date: 2026-03-09
audience: analytics leads, tech leads, XFN
status: draft
tags: [controls, requirements, risk-leads-dashboard, measurement]
---

# Measuring Controls: What We Report and at What Grain

## The Decision

The Risk Leads Dashboard reports at the **requirement** level. This is consistent with how every team already reports, and it's the right unit for leadership: requirements map directly to obligations, and obligations are what Michel and other senior leaders care about.

Controls — the mechanisms that enforce requirements — live one level below. They matter for cost and resilience analysis, but they're implementation detail for the purposes of "are we compliant."

This doc defines what we track at each level and why.

## Requirements: "Does It Work" and "How Does It Work"

A requirement is an obligation we must satisfy. Requirements originate from Obligations (regulatory, policy, or internal commitments), and risk reviews evaluate whether existing requirements are being met. Each requirement should have at least one control ensuring it's being followed.

The dashboard answers two questions at the requirement level:

### Does it work?

- **Coverage** — Does this requirement have at least one control?
- **Health** — For requirements with automated controls: is the control working?
- **Status** — Is this requirement currently being met?

A requirement is green when it's covered by a healthy control. It's red when coverage is missing or the control is failing. This is the primary view for leadership.

### How does it work?

- **Control type** — Is the requirement enforced manually or automatically?
- **Control count** — How many controls back this requirement? (A requirement backed by a single manual control has a different risk profile than one backed by three automated controls.)
- **Automation opportunity** — For manually enforced requirements: is there a path to automation?

This is the drill-down view. Leadership sees the summary; the team working on a red requirement needs this detail to understand what's broken and what it would take to fix it.

## Controls: Cost and Resilience

Cost and resilience are properties of controls, not requirements. A requirement doesn't have a setup cost — the control that enforces it does. A requirement isn't brittle — the control underneath it might be.

This means cost and resilience tracking lives at the **control** grain, even though the dashboard's primary view is requirements.

### Cost

- **Setup cost** — What does it take to deploy this control? (engineering effort, waves, AI tokens, etc.)
- **Operating cost** — What does it cost to run on an ongoing basis? (compute, headcount for manual controls, maintenance, friction imposed on product teams)

Tracking cost matters because the dashboard is ultimately about the cost of compliance. Showing that a requirement is covered but not what that coverage costs to operate is half the picture.

### Resilience

- **Failure vectors** — What could cause this control to stop working in ways we haven't accounted for? AI-driven changes to underlying systems are the obvious current example, but there are others: upstream schema changes, shifts in user behavior that invalidate assumptions, platform migrations.
- **Redundancy** — If this control fails, is there a backup, or does the requirement go uncovered?

Tracking resilience matters because "control is working today" doesn't tell you whether it'll be working next quarter. Controls that are brittle to environmental change need to be flagged differently from controls that are robust.

### How This Surfaces to Leadership

Cost and resilience data rolls up to the requirement level for the dashboard. A requirement that's green but backed by a single high-cost, brittle control looks different from one backed by a redundant, low-cost automated control. The specifics of how we surface that distinction — whether it's a risk score, a secondary indicator, or a separate view — are TBD.

## Next Steps

1. **Build the requirement-level view** — Coverage, health, and status across risk domains. This is the primary dashboard deliverable.
2. **Define cost and resilience metrics** — What "cost of a control" means concretely, where we'd source that data, and what the tracking model looks like.
3. **Design the roll-up** — How control-level cost and resilience data surfaces at the requirement level for leadership.
