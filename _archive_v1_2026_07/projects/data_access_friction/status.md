# Data Access Friction (FRAPS) — Status

_Last updated: 2026-04-20_

## State

Active, At-Risk. v0.5 dashboard is live with F1-F7 taxonomy deployed. ~20% friction reduction achieved (550K to ~450K interrupts/day, ~12 to ~10.1 interrupts/user/day). Target: <1/user/day. Program still flagged "At-Risk" due to measurement/logging gaps.

## What happened since last update (Apr 6)

- **v0.5 FRAPS dashboard producing real numbers**: 6.2M agent traces/day, 97.44K security interruptions, 1.58% interruption rate. ACL denials (F6) are the largest friction source at 0.74%, followed by data sensitivity (F2a, 0.33%) and allowlisting/gating (F7, 0.33%).
- **F3 reads 0%** due to an Artillery sampling SEV (S643755), not because there's no friction.
- **Taxonomy NOT locked by Apr 16 deadline.** F1-F7 categories are deployed but refinements are still in progress: F1 subcategories (F1A/F1B), F2C (policy zones), F6/F2 MECE validation, F7/GK classification, and ~16.8K daily warehouse auth denials still uncategorized.
- **New metrics from Aaron Morris HPM**: UBAR (Unexpected Blocks to Access Rate) at ~1.83%, Trust Exception Rate at 2.51% (target <1%).
- **WS3 code complete**: Isolation domain integration for Claude Code Sensitive Mode on Linux.
- **WS2 Rules Engine shipped**: Trust framework using operation type, mutation risk, max output sensitivity, and Agent Roles.
- **Pipeline join still blocked**: 95% of DPAS records lack an artillery trace ID.
- **Weekly update cadence may have slipped** — no update posted for weeks of Apr 13 or Apr 20.
- **Apr 18 deadline** for committed ETAs from dependent teams (Artillery, MySQL logging, trace_id propagation) — no public confirmation it landed.

## Key open questions Tony needs to shape

1. **Taxonomy refinements** — F1 subcategories, F2C policy zones, F7/GK distinction, and ~16.8K daily warehouse auth denials still need resolution. The war room ran past the Apr 16 target.

2. **F3 SEV masking** — S643755 means F3 (execution controls, 24% of post volume) shows 0% on the dashboard. When this SEV resolves, the numbers will shift. Need to understand the fix timeline.

3. **Weekly update cadence** — No update for two consecutive weeks. Is this an intentional change or drift?

4. **Apr 18 ETAs** — Did dependent teams (Artillery, MySQL logging) commit to timelines? No public confirmation.

5. **"Top agents" definition** — Still listed as Tony's open action item in the Apr 6 weekly update cross-workstream dependencies. Previously marked done in tasks.md — may need re-communication.

## Risks

- **WS4 observability**: ~54% of agent friction unobservable due to logging gaps (MySQL accounts for ~99% of the gap)
- **Security Plugin latency**: Haiku adds 800-900ms, blocking default-on. Avocado 2B replacement (<100ms) not ready yet
- **Trace stitching**: Near-zero overlap between DPAS and security traces (4.5% match rate)
- **F3 blind spot**: Largest measurement gap — 24% of post volume, zero structured signal, now masked by S643755

## Key metrics

| Metric | Current | Target |
|--------|---------|--------|
| Total interruptions/day | ~450K | Much lower |
| Interruptions/user/day | ~10.1 | <1 |
| Overall friction reduction | ~20% | Continuing |
| Dashboard interruption rate | 1.58% | Lower |
| UBAR | ~1.83% | Lower |
| Trust Exception Rate | 2.51% | <1% |
| DPAS-to-security trace match rate | 4.5% | Needs instrumentation |
