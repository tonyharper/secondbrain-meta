# Risk DE Eval Method vs. AI Evaluation Playbook: Gap Analysis

**Date:** 2026-03-13
**Author:** Tony Harper
**Sources:** Risk DE AI Measurement Roadmap (Swetha Singiri) | AI Evaluation Playbook (Dor Lavi, Michael Marcusa)

---

The Risk DE doc is a measurement plan and metric definition proposal — scoped, practical, and focused on getting eval pass rates tracked for semantic models. The AI Evaluation Playbook is a comprehensive methodology guide covering the full eval lifecycle. They're doing different jobs, so many differences are fine. But there are a few things in the Playbook that represent real gaps in the Risk DE approach.

## Gaps Worth Closing

### 1. Statistical rigor on pass rates

The Risk DE doc defines pass rate as `passed / total` and reports it daily. The Playbook goes much further — Clopper-Pearson confidence intervals, explicit sample size guidance (50 samples = +/-14% CI, 500 = +/-4%), and McNemar's test for version-to-version comparisons.

This matters because some of our semantic models have very small eval sets (11 evals for Age Reconciliation, 18 for Compliance Graph). A pass rate of 100% on 11 evals is not the same as 100% on 500. Without confidence intervals, we can't distinguish signal from noise, and leadership will treat those numbers as more precise than they are. The comments in the doc already flag this — someone asked about confidence intervals and sample size. This is a real gap.

**Recommendation:** Add confidence intervals to reported pass rates, and set minimum eval set sizes per semantic model. The Playbook's sample size table is a good starting point.

### 2. Failure mode categorization

The Risk DE doc tracks pass/fail as a binary. The Playbook does a structured failure taxonomy — discovery pass (open-ended analysis on 50-100 outputs), then prevalence pass (re-annotate against the taxonomy to get failure rates by category). Their root cause taxonomy has four L1 categories: Bad Retrieval, Bad Reasoning, Bad Instructions, Bad Tool Use.

This matters because a 67% pass rate on Compliance Graph tells you nothing about *what's* failing or *where* to invest. Are the failures retrieval problems (the SM isn't surfacing the right tables)? Reasoning problems (the agent has the right context but draws wrong conclusions)? Prompt problems? Without categorization, improvement is guesswork.

**Recommendation:** Add failure mode tagging to eval results. Doesn't need to be the full taxonomy from the Playbook — even a simple L1 categorization (retrieval / reasoning / instructions / tool use) on failed evals would make pass rate drops actionable.

### 3. Ground truth quality and freshness

The Risk DE doc doesn't address how eval ground truth is maintained over time. The Playbook treats ground truth as a living asset — "never done," with scheduled refresh cycles, quality tiers (Gold/Silver/Bronze), and a "5 lives" rule (after 5 uses, an eval set is considered contaminated). They also enforce strict separation between developers and evaluation sets.

This matters because our semantic models will evolve, the underlying data will change, and evals that were hard six months ago become trivial after hill-climbing. If eval sets go stale, pass rates go up but quality doesn't.

**Recommendation:** Define a ground truth refresh cadence (quarterly at minimum). Tag each eval with a quality tier and a creation date. Track eval set age as a health metric.

### 4. Online vs. offline eval distinction

The Risk DE doc focuses entirely on offline scheduled benchmark runs. The Playbook makes a sharp distinction: offline evals are granular (per-component), online evals are holistic (end-to-end with real users). They recommend shadow mode, A/B testing, and continuous monitoring for train-test skew.

The "Test vs Holdout Delta" metric (P1) gestures at this, but it's deferred to later milestones. The Playbook's framing is useful: if end-to-end online metrics drop, drill down into component-level offline metrics to find the root cause. That's the diagnostic flow.

**Recommendation:** When we get to the Holdout Delta metric, adopt the Playbook's framing of online evals as the top-level signal and offline evals as the diagnostic layer. Also consider logging production query distributions so we can detect drift between what evals test and what users actually ask.

## Differences That Are Fine

- **Eval system scope** (EvalHawk only vs. AEM+EvalHawk+EzEval): The decision to standardize on EvalHawk is cleaner. Keep it.
- **Granularity** (per semantic model vs. per agent): Per-SM makes more sense for our use case since we're measuring SM quality, not agent quality.
- **JTBD framework**: The Playbook's 10-JTBD structure is useful as a reference but would be over-engineering for our current scope. We're not building an eval methodology from scratch — we're measuring a specific set of outputs.
- **MCBoost calibration for automated judges**: Interesting but premature for our stage. Worth revisiting if we scale to hundreds of evals and start relying heavily on LLM-as-a-judge grading.
- **Adversarial red teaming, model cards**: The Playbook deprioritizes these themselves. Not relevant for SM evals.

## Bottom Line

The Risk DE method is solid for what it's trying to do — get a clean, trackable pass rate metric stood up with dashboards. The three things to push on are: **confidence intervals** (eval sets are too small to report bare percentages), **failure mode categorization** (makes the metric actionable), and **ground truth freshness** (keeps the metric honest over time). The fourth item (online/offline distinction) is worth internalizing as we build toward the Holdout Delta metric but isn't urgent.
