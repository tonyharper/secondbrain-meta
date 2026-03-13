# Analytics Org Model — Brainstorm

## Problem Statement

Current setup has overlapping scopes, tight coupling, and poor alignment across ~8 product groups. Analytical quality suffers because incentives aren't well aligned.

## Option A: Organize by Userbase

The natural organizing unit is userbase, not product or work type. Every product group maps cleanly to a user type, and the analytical approach is determined by who the product serves.

### Proposed Structure

1. **Core** — Shared systems, shared data, and cross-cutting risk measurement (e.g., overall risk calibration). Stands alone. Everyone depends on it.
2. **User-facing analytics** — Products that touch end users. Risk and engagement measurement.
3. **Internal/operator analytics** — Products serving internal teams. Cost, efficiency, operational measurement. Includes operational risk decisionmaking (helping internal teams make better decisions).
4. **Analytics infrastructure** — Product-building teams serving the analytics practitioner userbase. Works because they deeply understand their own users.

### Why This Works

- **Scope boundaries are natural.** Defined by users, not by product lines that shift when product teams reorg.
- **Analytical quality improves.** Each team concentrates expertise in the measurement paradigm their userbase requires — no context-switching between engagement and cost analysis.
- **Product-building teams fit cleanly.** Not an exception to the model — an instance of it.
- **Risk decisionmaking splits cleanly.** Operational (helping internal decisionmakers) goes in group 3. Calibration (is the risk framework working overall) goes in Core.

### Open Questions

- Does user-facing need to split further if product groups within it have very different risk profiles?
- Core owns infrastructure and evaluates everyone else's effectiveness — needs a leader with technical credibility and organizational trust.
- Does this structure actually fix incentive alignment, or do success metrics also need to change?
- How does Core prioritization work when every other group depends on it?
