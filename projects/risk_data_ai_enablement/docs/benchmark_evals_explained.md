# Benchmark Evals: What They Are and Why We Need Them

**Date:** 2026-03-13
**Author:** Tony Harper
**Context:** Brady Lauback's [AI Readiness: Calls-to-Action](https://fb.workplace.com/groups/157370374282131/posts/26792033697055770) post (March 10, 2026) and follow-up discussion with Singiri and Sunil

---

## What Benchmark Evals Are

Benchmark evals test the analytics agent — not our team, not our semantic models directly. They measure whether the agent (Analytics Agent, Datamate, etc.) can answer questions correctly when asked about Risk data.

Each eval is a test case with three parts:

1. **A prompt** — a specific question you'd ask the agent
2. **A golden answer** — reference SQL that produces the correct result
3. **A question type** — which determines how the answer gets graded (single value, categorical breakdown, time series, data discovery, or freeform rubric)

A benchmark eval set is a versioned collection of these test cases. CPP's current benchmark (v2.2) has 140 questions. They run it weekly, 5 trials per question, and track pass rates over time. That's what feeds the [AI for Analytics Measurement Dashboard](https://ai4a.nest.x2p.facebook.net/) — the dashboard Brady shared.

## How It Works

The agent gets a prompt, generates SQL, and returns an answer. The system compares that answer to the golden reference. Pass/fail gets reported on the dashboard by domain.

If your pillar hasn't submitted evals that make it into the benchmark set, you're either invisible on the dashboard or showing poor numbers. Brady tagged us directly in the post. This dashboard is going to leadership.

## The Eval Pipeline

1. You write test cases in **AEM** (Analytics Eval Manager) — prompt, SQL, question type, assign 2 SME reviewers
2. Automated checks run — SQL validity, data access, structural completeness
3. SMEs review and approve (Phabricator-like workflow: Draft -> Needs Review -> Endorsed -> Accepted)
4. Accepted evals enter the **Validated Pool**
5. CPP selects a subset for the **Benchmark Set** — that's what gets reported

There's also a "Northstar" track where you submit a published analysis your team already did. CPP reverse-engineers a prompt from it, and you grade the agent's attempt. These are harder, more realistic evals.

## The Five Eval Types

CPP is defining a taxonomy of eval types. Here's how they map:

| Type | Purpose | Who Defines | Tooling |
|------|---------|-------------|---------|
| Unit Test | Basic SM correctness checks during development | SM builders | EvalHawk |
| Hill Climbing | Iterative SM/agent quality improvement | SMEs | Shifting to AEM |
| Benchmarking | Cross-agent comparison against a standard set; feeds Brady's dashboard | SMEs + CPP | AEM |
| Aspirational | Stretch goals (e.g., funnel analysis evals) | CPP | AEM |
| Regression | Catch regressions (definition still unclear) | TBD | TBD |

Our team currently uses EvalHawk for unit testing and hill climbing our semantic models. That doesn't change. The new ask is **benchmarking evals** — test cases that go through AEM and feed the central dashboard.

## EvalHawk vs. AEM

These are not competing tools. AEM is a UI/workflow layer for managing eval test cases. EvalHawk is the storage and execution backend. AEM uses EvalHawk under the hood.

The pain point Singiri raised is real: hill climbing is shifting from EvalHawk to AEM, which means our SMEs now need to work in both tools. Cedric Hourcade [posted about this fragmentation](https://fb.workplace.com/groups/1991251848365266/permalink/2092032574953859/) in February — broad agreement that the tooling needs consolidation. But for now, both tools are in play.

## What Good Evals Look Like

The [Analytics Eval Quick Start Guide](https://docs.google.com/document/d/1A0EQ24cI1eIvks2HEqicwoiYDixGK0_C8-sk2RzgwZk/edit) lays out the quality bar. Key points:

- **Only 17% of submitted evals** currently pass quality checks
- Top rejection reason: prompt-answer misalignment (60% of failures) — the question is vague but the answer is specific
- Prompts must specify product, metric, timeframe, and geography
- SQL must be tested in DaiQuery, use stable date ranges, avoid most recent 1-2 days (backfill lag)
- Two SME reviewers required, cannot self-approve

Where to start:
- **Your team's recurring questions.** What do people ask about Risk data every week?
- **Your dashboards.** For each key metric on Tier 0 dashboards, write an eval asking the agent to reproduce that number.
- **Published analyses.** Submit real investigations via the Northstar track.

Current Usage track takes ~15 min per eval. A focused sprint could produce a meaningful set.

## The Coverage Gap

Worth knowing: an [analysis](https://fb.workplace.com/groups/1991251848365266/permalink/2105100553647061/) showed only 16% of actual user prompts match existing evals. Most evals are metric-specific ("What was X on date Y?") but real users ask exploratory questions. The highest-value evals aren't just number lookups — they're the questions your analysts and PMs actually ask.

## Why We Should Do This

- We get visibility into where the agent fails on Risk data — that tells us where our semantic models have gaps
- We show up on the dashboard that leadership sees
- Pillars with evals get CPP's attention when they prioritize agent improvements; pillars without don't
- The cost is low — a sprint of focused eval writing in AEM

## Related Documents

- [AI Readiness: Calls-to-Action](https://fb.workplace.com/groups/157370374282131/posts/26792033697055770) — Brady's post
- [AI for Analytics Measurement Dashboard](https://ai4a.nest.x2p.facebook.net/) — the benchmarking dashboard
- [Analytics Eval Quick Start Guide](https://docs.google.com/document/d/1A0EQ24cI1eIvks2HEqicwoiYDixGK0_C8-sk2RzgwZk/edit) — how to write and submit evals
- [Analytics Eval Manager (AEM)](https://www.internalfb.com/wiki/CPP_AI_Foundation/Analytics_Eval_Manager_%28AEM%29/) — the submission tool
- [Eval Methodology Gap Analysis](../eval_methodology_gap_analysis.md) — our internal eval method vs. the AI Evaluation Playbook
- [Unifying Evals Execution with EvalHawk](https://fb.workplace.com/groups/1991251848365266/permalink/2092032574953859/) — Cedric's post on tooling consolidation
- [Eval Coverage Gap Analysis](https://fb.workplace.com/groups/1991251848365266/permalink/2105100553647061/) — 84% of user prompts untested
