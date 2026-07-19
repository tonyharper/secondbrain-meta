# FRAPS Measurement Team: Roles & Ownership

**Date:** 2026-04-06
**Author:** Tony Harper
**Purpose:** Define who does what on the FRAPS measurement effort — current state and proposed ownership going forward.

---

## Team by Workstream

Each FRAPS workstream has a DE lead and DS lead. Tony Harper leads the cross-cutting measurement effort that stitches their outputs together.

| Workstream | DE Lead | DS Lead | STO |
|------------|---------|---------|-----|
| WS1: Identify, Detect, Triage | Tony Gonzalez | Aman Mathur (confirming) | Wenlong Dong / Can Lin |
| WS2: Meta CLI Friction | — | Aman Mathur | Yimo Tao |
| WS3: Data Access Friction | Shruti Tyagi | Maggie Mu | Yanbo Xu |
| WS4: Infra Access Friction | Harsh Asher | Dipra Malhotra | Tola Dalton |
| Cross-cutting Measurement | Tony Harper | — | — |

**TPMs:** Aaron Morris (measurement plan), Anisha Patel (overall FRAPS QB)

---

## Current Ownership Map

| Work Item | Owner | Status |
|-----------|-------|--------|
| Weekly FRAPS Measurement sync | Tony Harper | Running |
| Measurement plan (doc) | Aaron Morris | Written, iterating |
| v1 FRAPS dashboard | Tony Gonzalez | Live, continuing to own |
| Friction taxonomy (F1-F7 definition) | Wenlong Dong | Drafted, war room will finalize |
| Taxonomy-to-data mapping | Tony Harper | Drafted, iterating |
| DPAS trace coverage gap analysis | Shruti Tyagi | Complete |
| Observability solution | Harsh Asher | Scope unclear — need to confirm if this extends beyond WS4 |
| Artillery coverage comparison (hipster, bpfjailer) | **Unowned** | Proposed |
| "Top agents" definition | **Unowned** | Open question |
| Bounded controls taxonomy | **Unowned** | Open question |
| Maggie Mu's current FRAPS work | **Unknown** | Need to find out |
| Dipra Malhotra's current FRAPS work | **Unknown** | Need to find out |

---

## Observations

**What's working.** The workstream structure gives each WS a DE and DS. Tony Gonzalez on WS1 is the right person to own the dashboard since WS1 is the "identify, detect, triage" workstream — that's exactly what the dashboard does.

**What's missing.** The cross-cutting measurement layer — the part that stitches workstream metrics into a coherent topline — is currently just Tony Harper. That's fine for writing the taxonomy mapping and leading the sync, but the actual analytical work (running comparisons, validating coverage, building the empirical case for gaps) needs hands. Specifically:

1. **No one owns the empirical validation work.** The taxonomy data mapping says "F6 is 70-80% covered" and "F3 is ~0%." Those are estimates based on column inspection. The artillery coverage comparisons would turn them into real numbers. This is notebook work — someone needs to write queries and analyze results.

2. **The DS leads are allocated to workstreams, not to cross-cutting measurement.** Aman (WS2), Maggie (WS3), Dipra (WS4) are presumably doing analysis within their workstream scope. It's not clear if any of them are contributing to the cross-workstream friction picture.

3. **Harsh's observability work might be the bridge — or might not.** If his observability solution covers instrumentation gaps across all workstreams (F3 BPFJailer logging, F1 dCAT minting, etc.), that's the engineering side of closing the measurement gaps. But if it's scoped to WS4 only, those gaps stay open. Need to clarify.

---

## Open Questions

1. **What are Maggie Mu and Dipra Malhotra currently working on?** Their workstream DS roles are defined, but I don't know their concrete deliverables or whether any of it feeds the cross-cutting measurement effort.

2. **Does Harsh Asher's observability work extend beyond WS4?** The biggest instrumentation gaps (F3 BPFJailer, F1 dCAT) aren't WS4 problems. If Harsh is only scoped to WS4 infra access, who owns instrumentation for the other gaps?

3. **Who should own the artillery coverage comparisons?** Two candidates:
   - **Tony Gonzalez** — he's on WS1 and owns the dashboard. The comparison results would directly inform what the dashboard can and can't show. But he may be fully loaded on dashboard work.
   - **Shruti Tyagi** — she did the DPAS gap analysis, which is the same kind of "measure the gap empirically" work. But she's WS3 DE lead and may be focused on DW access metrics.

4. **WS1 DS.** Aman Mathur is expected to help with WS1 in addition to WS2. Meeting on 2026-04-07 to confirm scope and availability.

---

## Proposed Ownership (Draft)

### War Room Prep (Now → Apr 16)

| Deliverable | Proposed Owner | Rationale |
|-------------|---------------|-----------|
| Taxonomy data mapping (final) | Tony Harper | Already drafted |
| Artillery vs. hipster comparison (F6) | Tony Gonzalez? | WS1 DE, results inform dashboard |
| BPFJailer volume analysis (F3) | Tony Gonzalez? | Same rationale |
| Trace coverage gap presentation | Shruti Tyagi | She did the analysis |
| Dashboard updates for war room | Tony Gonzalez | Owns the dashboard |
| Topline metric proposal | Tony Harper + Aaron Morris | Measurement sync output |

### Ongoing Measurement

| Area | Proposed Owner | Notes |
|------|---------------|-------|
| FRAPS dashboard | Tony Gonzalez | Continuing |
| Topline metric (UBAR / interruption rate) | Tony Harper + Aaron Morris | Core measurement sync output |
| Cross-workstream data stitching | Tony Harper | Pipeline 1 + 2 + future sources |
| Instrumentation gap closure | Harsh Asher (if scope extends) | F3, F1 gaps need engineering |
| WS3 metrics (interruption rate, AccessMate) | Shruti Tyagi + Maggie Mu | Within their WS3 scope |
| WS4 metrics | Harsh Asher + Dipra Malhotra | Within their WS4 scope |
| WS2 metrics | Aman Mathur | Within WS2 scope |
| ISE data source expansion | **Unowned** | Ongoing as ISE adds attribution |
