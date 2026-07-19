# Risk Data AI Enablement — Status

_Last updated: 2026-04-20_

## State

Phase 1 in progress. Execution is producing real results — Chris Ventura's semantic model work is landing measurable quality gains, and Swetha got Risk onboarded to the Benchmark dashboard. But the operational cadence is still broken — no weekly updates since Mar 9 (6 weeks).

## What happened since last update (Mar 31)

### Semantic Models — major progress

- **Chris Ventura hill-climbed 22 semantic models** (Apr 10): 73% reached 90%+ pass rate, 36% reached 100%. Biggest gains: +52pp (video_surface_monetization), +43pp (mcf_notifications_om).
- **6 common fix patterns identified**: table routing decision trees (12 models), anti-patterns (8), terminology disambiguation (6), namespace corrections (3), filter value documentation (5), formula documentation (3).
- **Self-heal V4 shipped** (Apr 10): Integrates SM Quality Grader with self-heal. Batch orchestrator can run across an entire portfolio in one command with configurable concurrency, auto-resume, and batch dashboard.
- **Fuzzy grading** immediately fixed many issues — e.g., mcf_messaging jumped from 60% to 95%.
- **4 of 7 models below 90% are unfixable through SM edits** — the eval datasets themselves have issues.

### Measurement — Benchmark onboarding

- **Swetha got Risk onboarded to Benchmark_v4 dashboard** (Apr 13): Risk pillar pass rate at **86.07%**. Only 15 of ~700 Risk evals qualified for Benchmark V4 (out of 544 total benchmark evals).
- **Bug found and fixed**: Chronos-scheduled runs weren't logging SM details (NULLs). Lei Lin landed D99711513.
- **Eval lifecycle management** being built centrally (Elango): M1 (Domain-Centric Curation) targeted Apr 17, M2 (Measurement & Execution) May 15, M3 (Automation) June 12. Tony, Chris, Sunil cc'd.

### External ecosystem

- **AI Readiness Framework wiki** (Apr 14): MCF DE documented a framework composed from 5 existing Meta frameworks. Key insight: "A domain can score B on traditional dimensions and still score D on AI readiness — without a semantic model, agents can't find or interpret data."
- **BMG AI Native Data initiative**: Wave 1 (30 domain POCs) complete by Apr 3. End of H1 target: all Tier 0 datasets AI-ready with 75% pass rate.

## Stale items

- **Weekly updates stopped Mar 9** — now 6 weeks without an update. This is Tony's program and the cadence is broken.
- **Eval gap analysis** (Mar 13) — 4 actionable gaps identified but no owners assigned.
- **Anastasia / Context Engineering conversation** — no evidence this happened. No specific "context engineering" posts found on Workplace either.
- **Sunil Rathode** is quiet — cc'd on posts but not authoring. Unclear what he's driving.

## Key metrics

| Metric | Current | Target |
|--------|---------|--------|
| Risk Benchmark V4 pass rate | 86.07% | 85% (met) |
| Risk evals in Benchmark V4 | 15 / ~700 | More qualifying |
| Hill-climbed SMs at 90%+ | 73% (16/22) | Higher |
| Hill-climbed SMs at 100% | 36% (8/22) | Higher |
