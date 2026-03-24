---
title: Analytics Agent Quality — We Have Cause to Be Uneasy
date: 2026-03-23
audience: leadership
status: draft
tags: [analytics-agent, ai-quality, evals, risk-data]
---

# Analytics Agent Quality — We Have Cause to Be Uneasy

Usage of analytics AI tools — Analytics Agent, Datamate, and others — is growing fast. Unforunately, these tools aren't yet accurate enough to support the way people are starting to use them.

## The numbers

Central Products+Infra evals for Analytics Agent and Datamate show an overall pass rate of approximately 50%. That's on a set skewed toward straightforward point questions — "what was metric X last week?" — not the higher-level analytical questions that cross-functional partners actually need answered. For those questions, pass rates are closer to 20%.

To put that in context: we're used to operating at 95%-99% accuracy in our Analytics team outputs. A 20%-50% pass rate is not nearly good enough.

## Why this matters now

Risk team members are adopting these tools at an increasing rate. Non-Analytics adoption in Risk stands at 639 WAU, up 50% from the start of Feburary. That adoption is a signal of demand, which is genuinely positive. But at current accuracy levels, it creates a bad tradeoff:

- **Spot-checking overwhelms DS.** If cross-functional partners use Analytics Agent and then ask DS to verify the output, we've added work rather than removed it. In some cases this is already less productive than not using AI at all.
- **Incorrect decisions go unverified.** If cross-functional partners use Analytics Agent and *don't* ask DS to verify, decisions get made on wrong numbers. At our scale, that's a real risk.

Neither outcome is acceptable. The first erodes the productivity gains we're chasing; the second erodes trust in the tools and in the decisions they inform.

## What we're doing about it

We're not waiting for this to resolve itself. The Risk Data AI Enablement effort — including the war room we ran earlier this month — is building semantic models and evals specifically designed to improve accuracy in our domain. We have ~10 models near Beta deployment, with measurement infrastructure standing up alongside them. Planning for the next round of evals and models is underway.

The path forward is clear: better data foundations (semantic models), rigorous measurement (evals that reflect real user workflows), and honest accounting of where the tools fall short until they don't.
