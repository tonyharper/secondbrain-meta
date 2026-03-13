# Evolving the Analytics Champions Model

**Author:** Tony Harper
**Date:** March 2026
**Audience:** Analytics Champions

---

## What Changed

The Analytics/DI collaboration model was designed in 2024 around a specific problem: Analytics teams needed a structured way to advocate for their data infrastructure needs, and DI needed organized feedback from the people using their products. We built a tiered system — Steerco, Champions, SME Program Leads, SME Group Leads, SMEs — across seven domain groups.

Two years later, AI has fundamentally changed the landscape:

- **The consumption layer is collapsing.** The primary interface to data is increasingly an AI agent, not a dashboard or query tool. The boundaries between Data Consumption, Data Processing, and Metric Trust blur when a user just asks a question and expects an answer.
- **The SME role has shifted.** The high-value activity is no longer dogfooding features and filing papercuts. It's teaching AI how to work with our data — semantic models, repo context, evals. The expertise is the same, but the output is different.
- **"AI for Analytics" can't be a separate domain.** AI is the delivery mechanism for everything now. It cuts across all the other domains rather than sitting alongside them.
- **The advocacy model has less surface area.** With fewer active domain groups and more of the work shifting to AI enablement, the original Champions mandate — represent your pillar's needs to DI — covers less ground than it used to.

The Steerco has gone dormant. Several SME groups are inactive or low-activity. The model served us well, but it's time to evolve it.

---

## Proposed: Restructure the SME Groups

Regardless of what we do with the Champions role, the SME groups need to be right-sized to where the work actually is.

### Keep (3)

| Group | Rationale |
|-------|-----------|
| **Data Visualization (rename from Data Consumption)** | Nest is the new consumption platform. It's early enough that it genuinely needs hands-on SME input from people building dashboards. Traditional product feedback collaboration still works here. |
| **Semantic Models & Evals** | New group (or reorg of existing). This is where AI enablement lives — building the structured context that makes AI agents accurate on our data. Semantic models, eval sets, agent accuracy measurement. This is the most important collaboration surface right now. |
| **Data Processing / Warehouse Internals** | Presto, Dataswarm, capacity management. The plumbing still matters. Keep if it's still producing value; revisit if activity has dropped off. |

### Pause / Disband

| Group | Rationale |
|-------|-----------|
| **Privacy & Security** | Privacy requirements are increasingly handled through shift-left approaches — embedding them directly in the development environment rather than through a standing collaboration group. |
| **Metric Trust & Data Governance** | The governance function for AI is semantic models. M360 as source of truth feeds directly into the Semantic Models & Evals group. This work gets absorbed there. |
| **Experimentation** | Open question. Is there still enough cross-org collaboration need here to justify a standing group? Or is the experimentation platform mature enough that it doesn't need one? Propose we ask the current SMEs. |
| **Machine Learning** | Already on hold. Formally close. |

---

## Options: What Should Champions Become?

The SME group changes above are relatively straightforward. The harder question is what the Champions role should be going forward. Four options:

### Option A: Status Quo

Keep the current model. Champions advocate for their Analytics pillar's needs to DI. Tiered accountability. Semi-annual summits. Quarterly updates.

**For:** Continuity. Known process. Clear mandate.
**Against:** The mandate has shrunk. Fewer domain groups means less to coordinate. The advocacy-to-DI function is less relevant when the collaboration is increasingly peer-to-peer. Risk of maintaining structure for structure's sake.

### Option B: DE-to-DE Peer Network

Champions becomes a peer forum for Data Engineering leads across pillars. The purpose shifts from "represent Analytics to DI" to "keep each other sharp." Share what's working, coordinate on shared problems, stay current on platform changes and AI adoption. Still attend QBRs and provide DI feedback there, but that's a periodic input rather than the core function.

**For:** Reflects how the group already operates in practice. Lower overhead. Directly useful to participants. Flexible enough to tackle whatever matters in a given half.
**Against:** Risk of becoming a talking shop without a clear mandate or deliverables. Harder to justify people's time if there's no defined output. May drift without structure.

### Option C: AI Enablement Focus

Champions reorients around a specific mission: accelerating AI adoption across Analytics. Instead of organizing by pillar needs, organize around a shared challenge — how do we make AI work for our data? The group becomes the cross-org body for sharing semantic model patterns, eval approaches, agent adoption playbooks, and lessons learned.

**For:** Clear mission. High urgency. Directly tied to the most important work happening right now. Creates accountability for AI adoption progress.
**Against:** Narrower than the original mandate — doesn't naturally cover the Nest/visualization work or warehouse internals, which aren't primarily AI problems. Could become redundant with existing AI enablement efforts within pillars.

### Option D: Wind It Down

With 2-3 SME groups instead of 7, the coordination layer may not be needed. The remaining groups can run themselves. QBR feedback can happen directly. Champions was justified when there were seven domains and a complex prioritization problem. That's simplified. Free up people's time for the actual work.

**For:** Honest about the reduced coordination need. Frees up time. Avoids maintaining a structure that's outgrown its purpose.
**Against:** Loses the cross-pillar visibility that Champions provides. Harder to restart if the need comes back. QBR feedback without a coordinating body may be less effective.

---

## Discussion

A few things worth noting:

1. **B and C aren't mutually exclusive.** You could run a DE peer network whose primary agenda is AI enablement, but that also serves as the connective tissue for the remaining SME groups. That might be the practical answer — a peer group with a focused default topic but flexibility to cover other ground.

2. **Whatever we choose, we should move fast.** The current model is already drifting. Letting it continue without a deliberate decision is worse than any of these options.

3. **This doesn't need to be permanent.** We can pick a direction, run it for a half, and reassess. The point is to be intentional about what we're doing and why, rather than letting the old structure coast.

---

## Next Steps

- [ ] Align on SME group changes with current SME Group Leads and Program Leads
- [ ] Decide on Champions direction at next biweekly
- [ ] Communicate changes to broader Analytics/DI community
- [ ] Update the collaboration charter to reflect the new model
