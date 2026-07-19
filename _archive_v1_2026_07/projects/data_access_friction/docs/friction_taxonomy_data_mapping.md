# FRAPS Friction Taxonomy: Data Mapping & Coverage Assessment

**Date:** 2026-04-06
**Author:** Tony Harper
**Purpose:** Map Wenlong's F1-F7 friction taxonomy to available data sources. Identify what we can measure today, what's partial, and what's a gap. Intended for the WS1 war room (ETA: Apr 16).

**Taxonomy source:** [FRAPS: Problem Framing, Measurement, and Prioritization](https://docs.google.com/document/d/1tHHY9zQpk6SJo3rX60bvdD6PfleSXXcZRWFawdZThz0/edit)

---

## Data Sources

| Source | Table | What It Captures |
|--------|-------|------------------|
| Pipeline 1 — Security (`fct_agent_security_traces`) | `fct_agent_security_traces` (:security) | One row per Artillery trace. Security guardrail outcomes: ASP, ACL, input filtering, CBPC, PrivacyLib, fwdproxy, devproxy. 97M-246M traces/day. |
| Pipeline 2 — DPAS (`fct_agent_execution_dpas_requests`) | `fct_agent_execution_dpas_requests` | DPAS authorization outcomes for agent data access. SUCCESS, DENIED, FAILED_BY_SERVER, FAILED_BY_USER. |
| Claude Telemetry | Claude Friction Dashboard (`cc_security_sprint_dash.nest.x2p.facebook.net`) | Client-side permission prompt volume, bypass rates, prompt types. |

**Critical constraint:** Pipelines 1 and 2 can only be joined on `SUBSTR(artillery_trace_id, 1, 11) = trace_id`, but 94.1% of DPAS records have a NULL `artillery_trace_id`. Effective join rate: 4.5%. See [Shruti's gap analysis](https://docs.google.com/document/d/1SLkhja9R-5aIRiEemUVjY5U4KFYK4g4aYzXNJ82uxmw/edit) for details.

---

## F1: Identity & Auth Propagation (15% of posts)

Agent identity not recognized or propagated correctly across services. dCAT failures, CAT rejection, identity lost on delegation, false agent detection.

### What we can derive

| Signal | Source | Column / Condition | Confidence |
|--------|--------|--------------------|------------|
| ASP identity denials | Pipeline 1 | `is_asp_denial = TRUE` | High — ASP evaluates `agent.id` context. Identity propagation failures surface as ASP denials. |
| twintern fallback denials | Pipeline 1 | `is_acl_denial = TRUE` AND `acl_metadata` contains twintern as calling identity | Medium — requires parsing metadata structs. twintern denials signal the agent fell back to service identity. |
| Unknown/service identity traces with denials | Pipeline 1 | `user_id_entity_type IN ('SERVICE_USER', 'UNKNOWN')` AND `is_security_guardrail_denial = TRUE` | Medium — proxy signal. These traces likely ran under a broken identity chain. |

### What's missing

- **dCAT minting failures** (254K/week) — these happen before Artillery tracing starts. No trace exists to attach them to. This is the highest-volume F1 signal and it's invisible.
- **False agent detection** from environment variables — not a denial event, no structured log.
- **Identity lost on multi-agent delegation** — internal to agent orchestration runtime, not instrumented.
- Cannot distinguish "identity wasn't propagated" from "identity was propagated but lacked permission" without parsing `asp_metadata` denial reasons.

### Coverage: ~40-50%

ASP denials are a clean signal for identity-related friction at the enforcement point. But the highest-volume signal (dCAT minting failures) is upstream of any instrumentation we have. Closing this gap requires instrumenting the dCAT minting path to emit events that can be correlated with agent sessions.

---

## F2: Data Sensitivity Controls (25% of posts)

Data classified as sensitive blocks agent access. DSS-4 denials, DPAS denials, EntPrivacy blanket-deny, AI Input Filtering.

### What we can derive

| Signal | Source | Column / Condition | Confidence |
|--------|--------|--------------------|------------|
| AI Input Filtering blocks | Pipeline 1 | `is_input_denial = TRUE`, `input_filter_metadata` | High — direct signal for content scanning blocks and silent empty results. |
| CBPC denials | Pipeline 1 | `is_cbpc_denial = TRUE`, `is_server_cbpc_denial = TRUE` | High — content-based policy checks. |
| PrivacyLib enforcement | Pipeline 1 | `privacylib_metadata` (non-null), `asset_dss_levels` | Medium — asset access metadata, but records access rather than denial. |
| DPAS authorization denials | Pipeline 2 | `auth_response = 'DENIED'` | High — core DSS-4 denial signal. |
| DPAS server failures | Pipeline 2 | `auth_response = 'FAILED_BY_SERVER'` | High — 100% have null artillery trace (diagnostic for trace propagation bug). |

### What's missing

- **EntPrivacy blanket-deny rules** — unclear if these surface as input filter denials, DPAS denials, or neither. Likely a separate enforcement path not instrumented in either pipeline.
- **UGC retroactive access revocation** — not a real-time denial event, no structured signal.
- **Policy zone blocks** in Metamate/Datamate — internal to agent orchestration, not instrumented.
- **Pipeline 1 and Pipeline 2 can't be combined** into a single F2 number without double-counting risk, because the 4.5% join rate means we can't deduplicate traces that appear in both.

### Coverage: ~60-70% (split across two pipelines that can't be joined)

Input filtering and CBPC are clean from Pipeline 1. DPAS denials are clean from Pipeline 2. But the two populations barely overlap, so the "total F2 friction" number is either a union with unknown duplication or two separate numbers presented side by side. EntPrivacy and policy zone blocks are invisible.

---

## F3: Execution Controls (24% of posts)

Kernel/sandbox blocks. BPFJailer kills, sandbox restrictions, Rule of Two, dangerous mutation guardrails, OS-level sandbox.

### What we can derive

| Signal | Source | Column / Condition | Confidence |
|--------|--------|--------------------|------------|
| Dangerous CLI arguments | Pipeline 1 | `has_dangerous_cli_args = TRUE` | Low — this is a flag indicating the trace involved dangerous arguments, not a denial event. Tells you the agent tried something dangerous, not whether it was blocked. |
| Trace-level errors (speculative) | Pipeline 1 | `status_code = 'ERROR'` + `status_message` parsing | Very low — BPFJailer SIGKILL *might* propagate up to an error status on the trace. Speculative and unreliable. |

### What's missing

- **Everything that matters.** BPFJailer operates at the kernel level and kills processes with SIGKILL. No structured log ties "BPFJailer killed process X" to "agent session Y."
- **Sandbox denials** — OS-level permission errors. May appear in agent stderr but not instrumented into any pipeline.
- **Rule of Two blocks** — agent runtime decision, not instrumented as a security event.
- **Dangerous mutation guardrails** (Meta CLI trust layer) — these are CLI-level blocks. May partially appear in WS2's Meta CLI telemetry (`meta_cli_audit` Scuba), but not in `fct_agent_security_traces`.

### Coverage: ~0%

This is the biggest measurement gap in the taxonomy. 24% of post volume, effectively zero structured signal. Closing this requires kernel/sandbox teams to instrument BPFJailer and sandbox enforcement to emit events with agent session context (at minimum: trace_id, agent_id, process name, kill reason). Until then, F3 is a known blind spot.

---

## F4: Permission Prompts (6% of posts)

Client-side prompts interrupting agent workflow. "Do you want to proceed?", platform-enforced hooks, flag persistence bugs.

### What we can derive

| Signal | Source | Column / Condition | Confidence |
|--------|--------|--------------------|------------|
| Prompt volume and bypass rate | Claude Friction Dashboard | Separate telemetry, not column-level | High — ~550K prompts/day, 85% bypass rate. |

### What's missing from the security traces pipeline

- **Everything.** Permission prompts are client-side events in Claude Code. They don't generate server-side Artillery spans. No representation in `fct_agent_security_traces`.
- **No trace correlation.** Can't say "this trace in Pipeline 1 was interrupted by 3 prompts." The Claude telemetry and the security traces are completely siloed.

### Coverage: ~80% from Claude Friction Dashboard, 0% from Pipeline 1

The data exists — it's just in a separate source with no join path to trace-level data. For the heatmap, we can populate the F4 column for Claude Code from this source. F4 is N/A for most other agents (only Claude Code has client-side permission prompts in this form).

---

## F5: Network Controls (12% of posts)

Network-level blocks. Fwdproxy ACL denials, SAP destination allowlists, API rate limits, domain not allowlisted.

### What we can derive

| Signal | Source | Column / Condition | Confidence |
|--------|--------|--------------------|------------|
| Forward proxy denials | Pipeline 1 | `is_fwdproxy_denial = TRUE`, `num_of_fwdproxy_denials`, `fwdproxy_metadata` | High — denied domain, agent_id, denial reason all available. |
| Dev proxy denials | Pipeline 1 | `is_devproxy_denial = TRUE`, `num_of_devproxy_denials`, `devproxy_metadata` | High — same structure. |
| Internet access flag | Pipeline 1 | `is_internet_access = TRUE` | High — contextual signal for whether the trace accessed the internet at all. |

### What's missing

- **API rate limiting** — rate limit events (HTTP 429) aren't instrumented as security denials. They're application-level responses that may or may not appear in trace metadata.
- **TTLS proxy filtering** — unclear if captured in fwdproxy logs or logged separately.
- **SAP destination policy denials** — may overlap with ASP denials (F1). Need to check if `asp_metadata` captures destination-specific blocks separately from identity-specific blocks.

### Coverage: ~80-90%

Fwdproxy and devproxy are the dominant network enforcement points and both have clean, high-confidence signal. This is one of the two best-instrumented categories. Rate limiting is the gap, but it's lower volume than proxy denials.

---

## F6: ACL Denials (12% of posts)

Service-enforced access denied. InternToolConfig, Ent/TAO/MetaGen denials, service-level ACLs.

### What we can derive

| Signal | Source | Column / Condition | Confidence |
|--------|--------|--------------------|------------|
| ACL denials | Pipeline 1 | `is_acl_denial = TRUE`, `num_of_acl_denials` | High — direct signal. |
| ACL denial details | Pipeline 1 | `acl_metadata` — array of structs | High — can sub-classify by service (TAO, GK, OD, Cathode, etc.), resource, and calling identity. |

### What's missing

- **Denials outside the Artillery boundary** — services that haven't onboarded trace logging don't emit ACL denial events into this pipeline. The table only captures what Artillery sees.
- **InternToolConfig denials** — unclear whether these surface in `acl_metadata` or are logged in a separate system.
- **Overlap with F1** — some ACL denials are really identity propagation failures (twintern denials). Without a rule for attribution, the same event could count in both F1 and F6.

### Coverage: ~70-80%

Core ACL enforcement is well-instrumented. The tail of services that haven't onboarded trace logging is the gap. For the war room, propose a rule for F1/F6 attribution: if the denied identity is twintern or a service user, count it in F1 (identity failure). If the denied identity is the actual user, count it in F6 (ACL denial).

---

## F7: Allowlisting & Gating (6% of posts)

Manual configuration or approval required. GK gates, hardcoded FBID allowlists, AccessMate self-rejection, isolation domain boundaries.

### What we can derive

| Signal | Source | Column / Condition | Confidence |
|--------|--------|--------------------|------------|
| GK/allowlist denials (embedded) | Pipeline 1 | `is_acl_denial = TRUE` or `is_asp_denial = TRUE` where metadata indicates gating | Low — requires parsing metadata for gating-specific patterns. Fragile. |
| AccessMate self-rejection | Pipeline 2 | `data_source = 'dpas_accessmate'` AND `auth_response = 'DENIED'` | Medium — captures AccessMate denials but can't distinguish self-rejection from legitimate denial without additional context. |

### What's missing

- **GK evaluation outcomes** — GK just returns false and the feature is unavailable. No denial event is emitted. The agent silently doesn't have access to the capability.
- **FBID allowlist checks** — config lookups, not enforcement events. The agent gets a permission error, but the root cause ("you're not on the hardcoded list") isn't logged.
- **Isolation domain enforcement** — internal to Metamate's orchestration runtime, not instrumented.
- **No way to distinguish F7 from F6** in most cases — the symptom is the same (access denied), the difference is the root cause (explicit gating vs. standard ACL). That root cause isn't captured.

### Coverage: ~20-30%

Most F7 friction is "the feature just doesn't work for the agent" rather than "the system explicitly denied the agent." The former doesn't generate structured events. This category is inherently hard to measure because gating is designed to be invisible — the gate doesn't announce itself.

---

## Summary

| Category | Post Volume | Pipeline 1 | Pipeline 2 | Other | Total Coverage | Key Gap |
|----------|-------------|------------|------------|-------|----------------|---------|
| F1: Identity & Auth | 15% | 40-50% | — | — | **~40-50%** | dCAT minting failures (254K/week, upstream of tracing) |
| F2: Data Sensitivity | 25% | ~30% | ~40% | — | **~60-70%** | Pipelines can't join (4.5% match); EntPrivacy invisible |
| F3: Execution Controls | 24% | ~0% | — | — | **~0%** | No structured logging for BPFJailer/sandbox |
| F4: Permission Prompts | 6% | 0% | — | Claude Dash ~80% | **~80% (siloed)** | No join path to trace-level data |
| F5: Network Controls | 12% | 80-90% | — | — | **~80-90%** | API rate limiting |
| F6: ACL Denials | 12% | 70-80% | — | — | **~70-80%** | Services outside Artillery boundary |
| F7: Allowlisting & Gating | 6% | 20-30% | ~10% | — | **~20-30%** | Gating is invisible by design |

**Weighted by post volume, roughly 50-55% of the taxonomy is measurable from existing structured data.**

The three actionable takeaways for the war room:

1. **F5 and F6 are ready now.** Clean signal, high confidence. Build the heatmap for these two categories first and show real numbers by agent.

2. **F2 is the biggest category and partially measurable, but the two-pipeline problem is real.** We can show input filtering denials (Pipeline 1) and DPAS denials (Pipeline 2) separately, but presenting them as a single F2 number requires solving the trace stitching gap. Recommend presenting them as two sub-metrics until instrumentation improves.

3. **F3 is the biggest blind spot.** 24% of post volume, zero structured signal. This requires a logging investment — specifically, instrumenting BPFJailer and sandbox enforcement to emit events with Artillery trace context. Until then, we're measuring half the problem and calling it the whole thing.

---

## Proposed Attribution Rules

To avoid double-counting across categories, propose these rules for the war room:

| Condition | Assign to |
|-----------|-----------|
| `is_asp_denial = TRUE` | F1 (Identity) — ASP evaluates identity context |
| `is_acl_denial = TRUE` AND calling identity is twintern/service user | F1 (Identity) — identity propagation failure |
| `is_acl_denial = TRUE` AND calling identity is actual user | F6 (ACL Denial) — standard access control |
| `is_input_denial = TRUE` OR `is_cbpc_denial = TRUE` | F2 (Data Sensitivity) — content/privacy enforcement |
| DPAS `auth_response = 'DENIED'` | F2 (Data Sensitivity) — data access authorization |
| `is_fwdproxy_denial = TRUE` OR `is_devproxy_denial = TRUE` | F5 (Network Controls) |
| Claude permission prompt events | F4 (Permission Prompts) — separate data source |
| `has_dangerous_cli_args = TRUE` AND `status_code = 'ERROR'` | F3 (Execution Controls) — speculative, low confidence |
| ASP/ACL denial with gating-specific metadata patterns | F7 (Allowlisting) — fragile, requires metadata parsing |

These rules are a starting point. They'll need refinement as we see the actual distribution of metadata values.
