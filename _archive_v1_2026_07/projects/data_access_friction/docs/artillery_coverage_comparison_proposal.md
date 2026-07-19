# Artillery Coverage Comparison: Proposal for Two Focused Tests

**Date:** 2026-04-06
**Author:** Tony Harper
**For:** WS1 War Room (ETA Apr 16)
**Depends on:** [Friction Taxonomy Data Mapping](friction_taxonomy_data_mapping.md), ISE Logging & Enforcement Taxonomy (Tab 2 of shared mapping doc)

---

## Problem

The friction taxonomy data mapping estimates that ~50-55% of the F1-F7 taxonomy is measurable from existing structured data, primarily `fct_agent_security_traces` (Pipeline 1) and `fct_agent_execution_dpas_requests` (Pipeline 2). But that estimate is based on column availability, not empirical validation. We don't actually know:

1. **How much enforcement activity happens outside Artillery's boundary.** Pipeline 1 only captures what Artillery-instrumented services emit. Services that haven't onboarded trace logging are invisible. We say F6 coverage is "70-80%" but the denominator is unknown.

2. **Whether F3's "0% coverage" is actually zero, or just zero in our pipeline.** BPFJailer kills processes at the kernel level. Those events exist somewhere — they're just not in `fct_agent_security_traces`. If we can quantify them from the source, we turn a hand-wave into a number.

ISE's enforcement logging inventory (added to the shared taxonomy doc) identifies ~25 datasets across enforcement chokepoints. Several have agent or trace attribution that could let us empirically measure what Artillery misses.

## Proposal: Two Focused Comparisons

Rather than attempt a comprehensive cross-dataset audit, run two bounded comparisons — one for each of the two weakest points in the taxonomy mapping.

### Comparison 1: hipster_aclchecker_checks vs. Artillery ACL Denials (F6)

**Why this one.** hipster_aclchecker_checks is the only ISE dataset with both `agent_id` (via `accessor_contextual_attributes`) and `trace_id`. That means we can do a real event-level join to `fct_agent_security_traces`, not just an aggregate volume comparison.

**What it tests.** F6 (ACL Denials) is estimated at 70-80% coverage in Pipeline 1. The known gap is "services outside the Artillery boundary." hipster is Ent's ACL checker — it sees ACL evaluations that may or may not appear in Artillery traces. Comparing the two tells us:
- How many hipster ACL denials have a matching artillery trace with `is_acl_denial = TRUE`?
- How many hipster ACL denials have no corresponding artillery trace at all?
- What services, resources, or agent types appear in the hipster gap?

**Join approach.** Both datasets have trace_id. Join on trace_id for a single day. Left join from hipster (the potentially broader source) to artillery (the pipeline we're assessing).

**Expected output.** A single number: "X% of ACL denial events visible in hipster are also visible in Artillery." If it's 90%+, our 70-80% estimate holds. If it's 50%, we have a much bigger F6 gap than we thought, and we know which services to target for onboarding.

**POC:** Fland Pan (hipster_aclchecker_checks owner)

**Effort:** 1-2 days in a notebook. One day to understand hipster's schema and write the join query, one day to analyze the results.

---

### Comparison 2: bpfjailer_enforce Volume by Agent (F3)

**Why this one.** F3 (Execution Controls) is 24% of friction post volume and has ~0% structured coverage in any pipeline we use today. BPFJailer is the primary enforcement mechanism. The `bpfjailer_enforce` Scuba dataset captures kill events. If we can slice by agent, we get the first concrete number for F3.

**What it tests.** Not a join — bpfjailer_enforce has no trace_id and no clean agent_id field. But it does have `ancestor_json`, which contains the process tree. Per Liam Wisehart (POC), regex search on this field for known agent process names is the best current approach for agent attribution.

**Join approach.** No join to artillery. This is a standalone volume analysis:
- Total BPFJailer kills per day
- Kills attributable to agent processes (claude_code, metamate, devmate, etc.) via ancestor_json regex
- Kill reasons and process types for agent-attributed events

**Expected output.** A daily volume number: "BPFJailer kills X agent processes per day, affecting Y distinct agents." This gives us the F3 denominator we currently don't have. Even a rough order-of-magnitude (hundreds? thousands? tens of thousands?) changes the conversation.

**Constraint:** Agent attribution via regex is fragile and will undercount. The result is a lower bound, not a census. Liam wants to add proper agent_id attribution — this comparison would also serve as motivation for that investment.

**POC:** Liam Wisehart (bpfjailer_enforce owner)

**Effort:** 1 day. The query is straightforward (Scuba, not Hive). The hard part is validating the regex patterns against known agent process names.

---

## What This Doesn't Cover

- **Pipeline 2 (DPAS) gaps.** Shruti's trace coverage analysis already quantifies this (4.5% join rate, 94.1% NULL artillery_trace_id). The instrumentation fix is identified — it's a code change in the `dpas_others` path. A comparison wouldn't add new information.

- **Datasets without agent attribution.** Several ISE datasets (some asset_access_logs variants, dpas_authorization_checks) lack agent_id entirely. They can't tell us about agent friction until they're instrumented. Worth flagging as future instrumentation requests, but not worth running comparisons on today.

- **Claude Friction Dashboard vs. Artillery.** These are fundamentally different systems (client-side vs. server-side) with no join path. The gap is architectural, not empirical.

## Sequencing

| Step | What | When |
|------|------|------|
| 1 | Reach out to Fland Pan and Liam Wisehart for schema access and validation | Week of Apr 7 |
| 2 | Run Comparison 1 (hipster vs. artillery) | Week of Apr 7-14 |
| 3 | Run Comparison 2 (bpfjailer volume) | Week of Apr 7-14 (parallel) |
| 4 | Incorporate results into taxonomy mapping doc | Before war room (Apr 16) |
| 5 | Present at war room: "here's what we know, here's what we're missing, here's the empirical evidence" | Apr 16 |

## Success Criteria

After these two comparisons, we should be able to say:

1. "Artillery captures X% of ACL enforcement events. The remaining Y% come from services Z1, Z2, Z3 that haven't onboarded trace logging." (Replaces the current hand-wave of "70-80%.")

2. "BPFJailer kills approximately N agent processes per day. This is the F3 signal that is currently invisible in our measurement." (Replaces "~0% coverage, 24% of post volume" with an actual number.)

Both results strengthen the war room presentation. Instead of "we think we're measuring about half the problem," we can say "we measured the gaps, and here's exactly what's missing."
