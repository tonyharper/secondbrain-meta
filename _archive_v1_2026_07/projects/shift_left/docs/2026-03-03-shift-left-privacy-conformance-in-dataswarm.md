---
title: "Shift Left: Privacy Conformance in the Dataswarm Development Workflow"
date: 2026-03-03
audience: engineers
status: draft
tags: [shift-left, privacy, dataswarm, devmate, data-understanding, proposal]
---

# Shift Left: Privacy Conformance in the Dataswarm Development Workflow

## TLDR

We should integrate privacy conformance directly into the Dataswarm development workflow — so that when an engineer runs `tester`, the system classifies the data being produced, determines which privacy requirements apply, and applies them. The mechanism is DEMate recipes backed by real-time Data Understanding (RTUP) and privacy requirement APIs. This replaces the current model where privacy requirements are discovered and enforced after the fact — through wave tasks, codemods, and agent-driven remediation — at substantial cost and friction.

## Problem

Today, privacy conformance for Dataswarm-produced data assets is reactive. An engineer writes a pipeline, lands a diff, and creates a table. Days or weeks later, the Unified Prediction Pipeline (UPP) runs, classifies the data, and if the table contains user data, triggers privacy wave tasks — Rich Type annotations, Actor labels, Half-Life deletion plans, access controls. The engineer (or an agent acting on their behalf) then has to go back, understand what's needed, and fix things.

This creates several problems:

- **Cost.** Thousands of wave tasks per half. In H1 2025, roughly 9,600 assets triggered privacy tasks — ~8,000 for Half-Life deletion and ~1,400 for Rich Types alone. AI agents now handle much of the remediation work, so the cost is shifting from engineer hours to token spend — but there's still a human cost. Someone has to review what the agent produced, verify it's correct, and land it. That review burden scales with the number of retroactive fixes, and the quality is harder to ensure when the reviewer didn't author the original code.
- **Friction.** Engineers experience privacy as something that happens *to* them after the fact, not something built into how they work. This undermines both the experience and the outcome.
- **Lag.** The gap between table creation and requirement enforcement means data can exist in a non-compliant state for days or weeks. That's risk we don't need to carry.
- **Rework.** When requirements are applied retroactively, the fix is often a codemod or stacked diff that the engineer didn't author and doesn't fully understand. The quality of these fixes is lower than if the engineer had done it at authoring time with full context.

The root cause is architectural: privacy classification and enforcement happen in batch, disconnected from the development workflow where the data asset is actually being built.

## Proposal

Move privacy conformance into the Dataswarm development loop. Specifically:

**When an engineer runs `tester` on a pipeline that produces a new or modified data asset, the system should:**

1. **Classify the data.** Invoke real-time Data Understanding to determine what the output table contains — is this user data? What kinds? (Rich Types, Actor labels, Semantic Types.)
2. **Determine applicable requirements.** Based on the classification, call into privacy systems to identify which requirements apply — retention policies, deletion obligations, access controls, purpose limitations, anonymization requirements.
3. **Apply the requirements.** Modify the pipeline code and UPM Dataset to conform — add Rich Type annotations, set retention policies, configure deletion plans, apply access controls. Where full automation isn't possible, surface clear guidance on what the engineer needs to do manually.

### How It Works

The implementation builds on two things that already exist or are in active development:

**DEMate** is the Data Engineering extension of DevMate. It already provides specialized recipes for Dataswarm development — creating pipelines from SQL, adding data quality checks, running lineage queries, launching test runs. DEMate activates automatically when working in `dataswarm-pipelines/` and has access to MCP tools for linting, testing, and pipeline validation. This is the right vehicle for privacy conformance because it's already where DEs work.

**Real-Time Data Understanding (RTUP)** is a proposed real-time extension of the Unified Prediction Pipeline. It uses Bii Real-Time Enumeration (RTE) to scan newly created tables within hours of creation, then runs the same prediction logic as UPP via XStream to produce Rich Type, Actor, and Semantic Type annotations. For Dataswarm UPM Dataset tables, RTE coverage is already at 88.9%. RTUP can surface predictions back into the engineer's diff as suggested annotations on their UPM Dataset file.

The proposed integration:

```
Engineer writes/modifies pipeline
        │
        ▼
   Runs `tester`
        │
        ▼
   Test table created with test prefix
        │
        ▼
   RTUP scans test table (via Bii RTE)
        │
        ▼
   Data Understanding classifies columns
   (Rich Types, Actor labels, Semantic Types)
        │
        ▼
   Classification result: contains user data?
        │
        ├── No → Done. No privacy requirements apply.
        │
        └── Yes →
                │
                ▼
           Query privacy requirement APIs
           (What retention? What deletion? What access controls?)
                │
                ▼
           DEMate applies requirements to pipeline code:
           - Rich Type annotations on UPM Dataset
           - Actor labels
           - Retention/deletion configuration
           - Access control settings
           - Anonymization where required
                │
                ▼
           Engineer reviews changes
           (Accept, modify, or override with justification)
```

### What DEMate Does Specifically

This would be implemented as one or more DEMate recipes that:

1. **Trigger automatically after `tester` completes** — no manual invocation required. When `tester` finishes and output tables exist, the privacy conformance recipe runs.
2. **Call RTUP or equivalent Data Understanding APIs** to get classification results for the test output tables.
3. **Interpret the classification** — map Rich Types and Actor labels to specific privacy requirements using existing policy APIs.
4. **Generate code changes** — modify the UPM Dataset class to add Rich Type annotations, Actor labels, retention policies, and any other required configuration.
5. **Run the linter** to validate the changes are syntactically and semantically correct.
6. **Surface the results to the engineer** — show what was classified, what requirements apply, and what was changed. The engineer accepts, modifies, or overrides.

### What This Replaces

| Today | Proposed |
|-------|----------|
| Engineer lands diff, table created | Same |
| UPP batch runs (daily) | RTUP runs on test table during development |
| Classification lands days later | Classification available before diff lands |
| Wave tasks filed to engineer | Requirements applied in the development workflow |
| Engineer context-switches back, or agent files fix | Engineer reviews and accepts at authoring time |
| Codemod auto-lands if not reviewed in 2 weeks | No codemod needed — requirements applied at source |

## Dependencies

This proposal depends on several things being true or becoming true:

1. **RTUP needs to work on test-prefix tables.** Currently, Bii RTE scans production tables. For this to work at `tester` time, RTE (or an equivalent scanning mechanism) needs to scan test tables created during tester runs. This may require Capella to expose diff ID and test prefix metadata — a known gap flagged in the RTUP design doc.

2. **RTUP prediction quality needs to be sufficient.** UPP Rich Type prediction quality is ~99% and Actor prediction is ~93%. If RTUP matches these numbers, automated application is reasonable for high-confidence predictions. Low-confidence predictions should be surfaced as suggestions, not auto-applied.

3. **Privacy requirement APIs need to be queryable.** There needs to be a way to go from "this table contains [these Rich Types] with [this Actor]" to "these are the specific requirements that apply." This mapping may already exist in policy systems — needs investigation.

4. **DEMate recipe infrastructure supports this pattern.** DEMate recipes can already invoke MCP tools, run linters, and modify code. The new capability is calling external APIs (RTUP, privacy policy) and applying structured changes based on the results. This should be feasible within the existing recipe framework, but needs validation with the DEMate team.

5. **Latency budget.** RTE currently scans within 3 hours. That's too slow for a synchronous `tester` workflow. We either need a faster scanning path, or the privacy conformance step runs asynchronously and surfaces results when ready (e.g., as a comment on the diff or a follow-up DEMate suggestion). This is the biggest open question.

## Open Questions

- **Latency.** Can we get Data Understanding results fast enough to be useful in the dev loop? 3 hours is too slow. Options: (a) call Bii/scanning APIs directly rather than waiting for RTE, (b) use LLM-based classification on the UPM Dataset schema and SQL as a fast heuristic, (c) run asynchronously and surface results before the diff lands rather than during `tester`.
- **Confidence thresholds.** At what confidence level do we auto-apply vs. suggest? UPP uses auto-land for high-confidence codemods today. We should use the same thresholds.
- **Override mechanism.** When an engineer disagrees with a classification or requirement, how do they override? This needs to integrate with the existing Rich Type disagreement workflow.
- **Scope.** Do we start with Rich Types and Actor labels only (where prediction quality is highest), or include retention, deletion, and access controls from the start?
- **Non-Dataswarm tables.** This proposal is scoped to Dataswarm pipelines. Non-Dataswarm Hive tables would continue to use the batch UPP flow. Is that acceptable, or do we need a broader solution?

## Proposed Phasing

**Phase 1: Classification at dev time.** Integrate Data Understanding into the DEMate workflow so engineers see what their output tables contain before landing the diff. Even without automated requirement application, this is valuable — it closes the feedback loop and eliminates surprise wave tasks.

**Phase 2: Requirement identification.** Add the privacy requirement lookup. After classification, surface which requirements apply and what the engineer needs to do. This is the "tell me what I need to fix" step.

**Phase 3: Automated application.** DEMate modifies the pipeline code to apply requirements directly. High-confidence changes are auto-applied and presented for review. Low-confidence changes are surfaced as suggestions.

## Success Metrics

- Reduction in after-creation privacy remediations for Dataswarm-authored tables — whether via waves, tides, projects, or AI agents
- Percentage of new Dataswarm tables that land with correct Rich Types and Actor labels at creation time (currently ~40% for Rich Types)
- Time from table creation to full privacy conformance (target: zero — compliant at landing)
- Engineer satisfaction with privacy workflow (survey)

## Related Work

- **Shift-Left for Data Understanding (H1 2025)** — Existing program that achieved 99% 14-day SLA and 40% creation-time coverage for Rich Types. This proposal extends that work into the development environment.
- **RTUP design doc** — [Real Time Unified Prediction](https://docs.google.com/document/d/15mku2Nu6gqeclzYi1qpK22f3O-FfUHdZkjJSx67Vmvo/) — Architecture for real-time Data Understanding.
- **Colin Glaes's agentic Dataswarm development** — [Making Dataswarm Development Autonomous with Claude](https://fb.workplace.com/groups/803837402998210/permalink/30652942740994282/) — Prototype connecting code, tester, chronos, and presto via Claude skills. This proposal builds on that foundation.
- **DEMate** — The Data Engineering extension of DevMate, with 47 specialized recipes for Dataswarm workflows.
- **Realtime UPP Rich Type Suggestions** — [Investigation doc](https://docs.google.com/document/d/1y0KWZJ_5uE_E4-9FQEmaU5wNG3qG5he5NlKfnr-pcho/) — Analysis of RT UPP suggestion coverage gaps.
