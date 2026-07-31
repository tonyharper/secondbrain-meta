Source: https://docs.google.com/document/d/1GA2Vs6qcaZ2OTbHbeua2hi16s-xgnN5BDOU1iGaM3Bo/edit?tab=t.avhr0j4vgxp5#heading=h.i1qmd0as0se4

# Ingest — Project Neo: Impact on Growth metrics (Business Overview)

- Date: 2026-07-31
- Author: Thasneem Farzana (xAU source), Neo Program + Central Growth (JAT, Amee), FB App (Justin, Srivatsan, Lily) audience
- Type: google_doc
- Ingested: 2026-07-31 via meta CLI
- Status: Working Draft / Confidential — xAU Focus

## TLDR

Proposes redefining FB xAU (DAU/MAU) to IG parity — attribute time spent to acted-on profile (voice) not acting/admin, include business profiles in xAU — rollout Option B event-driven following product migration (M1 Dec 2026 10% test → M3 Q4 2027 full, phased not step), ceiling +40M DAU / +240M MAU at M3, +43M DAU / +208M MAU upper bound, DAU@2 222K. Option 4 recommended. Three shadow metrics from M1.

## Key Points

- **Metric redefinition — Option 4 (recommended):** acted-on attribution + include business. Cross-app alignment with IG/WA, complete time spent coverage, profile-level explainability. Alt options: #1 maintain current, #2 acting+include biz, #3 acted-on exclude biz (drops -6.3M DAU -3.7M MAU from primary-only-active-on-AP+), #5 Meta Account level (mtid).
- **Rollout timing — Option B recommended (event-driven):** official xAU switches as entities migrate to account status. Correct (factually accurate for DSA), schedule resilient (no recuts if timeline slips), forecasting continuity (shadow previews), experimentation-safe. Option A switch at M1 forward-estimate creates early large step on estimated AP+, Option C keep current + flip after M3 not feasible (can't identify AP+ post-Neo).
- **Shadow metrics from M1:** 1) Growth Understanding — Option 4 applied to ALL AP+ artificially for longitudinal/clean series, 2) Experimentation — non-Neo-impacted users only for historical compares, 3) Actor/acting-account accounting — old definition retained, will NOT be deprecated (Family Accounting, Creator/Biz).
- **Milestones:** Smoke Nov 2026 3 countries, M1 Q1 2027 global (Dec 2026 10% test) new Personal/Creator/Business modes + multi-profile flexible names + FB-FB hardlinks, no AP+ changes. M2 Q2-Q3 2027 large entity profiles → accounts, low-risk & opt-in AP+/Pages migration. M3 Q4 2027 complete Page migration.
- **Impact:** M1 slow organic growth from new creator/business modes — IG proxy 0→1.3M daily secondary creations. M2 onwards steady growth from AP+→account migration. M3 ceiling +40M DAU / +240M MAU phased. SUMA FB-specific pending, IG proxy +31.5M MAU +2.2% Y1. DAU@2 222K.
- **Data team implications:** Extensive warehouse adaptation — logging (acted-on vs acting), experimentation (exposure unchanged event-driven, 3 handling options under evaluation: metrics-level, dimension-level all, dimension-level ad hoc — PoC Roxy Wang), growth understanding (Neo vs non-Neo views + mode decomposition personal/creator/business), forecasting (shadow + rollout plans baked into Central Growth forecasts), Family Accounting (hardlinks, mitigation aligned Alex Schultz A/C Priv), demographics (country/age predictions), extensible work central execution explored.
- **Nomenclature:** Accounts/Profiles used pre-Future3 sense. Acted-on = voice, Acting = admin.
- **Caveat:** Timelines subject to change mid-July 2026 understanding.

## Connection to Tony's Data Risk threads

- **Data Model grain shift:** This doc explains WHY acting_account→voice shift — for xAU metric parity. Links to existing doc 1uFjRAGP (DAU grain voice, dim_all_users→voice, dim_fb_account→acting_account, dim_fb_profile deprecated with shadow macro). Needed for 1L1pXwnjf semantic models update, repo context, evals.
- **XSU / Deletion:** Time spent attribution change affects XSU checker POC putting Biz out-of-scope (per SteerCo), needs hardlink infra. Deletion/retention (Ryan Begley) needs actor vs profile distinction.
- **UIBC / Business Data Classification:** Business profiles inclusion in xAU changes boundary — need Business Data Criteria Decision (Shashwat/Bunmi) Option 1-3. Creator starts in-scope XSU reclassified to business based on activity.
- **Privacy Handling:** Family Accounting hardlinks FB-FB created during migration — detail shared aligned Alex Schultz (A/C Priv) — links to Meta Account PoR Option 1.

## Flags / What to discuss

- Approve redefinition + rollout? Ask to Central Growth + FB App leads — needs decision before M1.
- Forecasting: need Growth Understanding shadow from M1 for model calibration — who builds?
- Experimentation handling — which option chosen? Impacts all FB experiments during 6-month migration (upward angle change not step).
- DSA external reporting — event-driven keeps official metric tied to product reality (good).
- Link to DAP sizing: this doc says +40M DAU ceiling, North Star deck claims +3.8% DAP ceiling — need reconcile with private note 0.7-2.1% grounded.

## Route to

- [x] projects/project_neo/ — overview.md Key Docs + this file
- [ ] areas/data_risk/overview.md if data model implications grow
- [ ] decisions/decision_log.md — when xAU redefinition approved (Option 4 + Option B event-driven)
- [ ] reference/key_docs.md — link + TLDR
