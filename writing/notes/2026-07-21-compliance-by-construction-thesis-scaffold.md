---
title: Compliance by Construction — Thesis Scaffold
date: 2026-07-21
audience: general
status: draft
tags: [compliance-by-construction, governance, standards, thesis]
---

# Compliance by Construction — Scaffold (Cal draft, Tony owns prose)

> Source: `writing/proposals/cbc-thesis-handoff.md` — this file is scaffolding only. No voice.

## One-liner
The friction model of data governance is failing from both ends at once — practitioners defeat controls from below, rules misdescribe technology from above — and closing the gap requires moving controls into substrate AND rewriting rules for how models learn.

## Architecture — Do Not Collapse

### Half One — Failure from Below (Controls)
- Current: detection + enforcement (retention-violation detection, deletion enforcement, non-compliant-dataset flagging)
- Observed failure: under time/business pressure, researchers route around — stash data in random filesystems to keep training stable, evade detectors, refuse outright
- Consequence: detection-based governance partly theater — works on already-compliant, defeated by population that matters
- Fix: compliance by construction — controls baked into datastores + pipeline tooling so compliant path is only path and frictionless path
- Principle: "you can't route around a control that is the substrate"
- Limit / seam to Half Two: only formalizable rules compile (retention windows, deletion propagation, ACL). Judgment-laden rules (purpose limitation, reasonable expectation) can't compile — must be resolved at rule level

### Half Two — Failure from Above (Rules)
- Category error: existing regulation written for ~2015 user-facing transactional data; doesn't map to model training
- Frontier Claim 1: deletion rights conceptually broken against stable training set / learned weights; machine unlearning doesn't satisfy right as written
- Frontier Claim 2 [most differentiated]: competition rules have no theory of inference — written around data combination (joins, record linkage); model that infers rather than matches creates vacuum at center of regime almost nobody articulates
- Illustrative (Tier 2): Wall Street reporting anecdote

## Open Iteration Agenda — Pressure Points

### 1. Formalizability boundary — needs theory
- Candidate test: rule compiles iff its satisfaction decidable from metadata present at pipeline time
- Stronger claim: boundary is movable, not fixed
  - Example: consent scope becomes formalizable IF consent captured as structured data at ingestion
- Need to answer: what metadata would need to exist to make purpose limitation decidable? Is that desirable?

### 2. Name the precedents
| Precedent | Why it matters for CbC | Source to find |
|-----------|------------------------|----------------|
| Memory-safe languages (Rust) | Made use-after-free inexpressible vs better-detected | — |
| Type systems | Compliance as type error at construction | — |
| Policy-as-code (OPA, Sentinel) | Prior art for compiling policy to enforcement | — |
| Capability-based security | Rights as unforgeable references, not checks | — |
| Differential privacy | Construction primitive for formerly judgment-laden concept | — |
| Hierarchy of controls (elimination > detection > PPE) | Century-old empirical foundation from safety eng | — |

Action: fill citations, 1-line summary per, avoid turning into literature review.

### 3. Strongest counterargument = calcification
- Substrate controls encode today's interpretation at scale
- If rule changes or encoded wrong, error built into everything — detection failures are local, construction failures are systemic
- Thesis needs:
  - substrate versioning story
  - governance of constructors — "who audits the compiler?"
  - rollback / interpretation change mechanics

### 4. Inference vacuum — deserves own Act
- Currently thin scaffold, could carry 1/3 of piece
- Open question: what would theory of inference in competition law look like — is inferred data "combined" data?
- Research prompts:
  - Has any competition authority addressed ML inference as combination?
  - Datavant, Stripe as compliance-as-product vs inference-as-product tension
  - Waymo as purest industrial expression — why does inference there avoid vacuum?

### 5. Humana thread — unused durability proof
- 11 years healthcare = most compliance-saturated data environment in US, pre-AI
- Provides proof this isn't trendy AI argument — makes thesis durable
- Need 2-3 healthcare analogs where detection-based governance failed and construction-based fix would have mattered

## Proposed Piece Structure (Problem → Constraints → Options → Recommendation for technical sections)

1. Opening — friction model failing from both ends — anecdote from below
2. Half One — controls theater, substrate fix, principle, formalizability limit
3. Seam — judgment-laden rules don't compile — transition
4. Half Two — rules category error, deletion broken, inference vacuum
5. Counterarguments — calcification, versioning, compiler governance
6. Precedents — hierarchy of controls framing
7. Path forward — construction + rule rewrite, standards track, what would need to be true
8. Humana epilogue — durability

## Standards Track Mapping (conceptual layer only)
- NIST CAISI consortium — best fit for inference + deletion-as-construct discussion
- ISO/IEC JTC 1/SC 42 via INCITS — AI governance, formalizability criteria could be contribution
- IEEE — policy-as-code / construction primitives
- Next: identify Meta delegations to join, don't start new delegation

## What Tony writes vs Cal does
- Tony: all prose in `writing/proposals/` or `essays/` — voice protected
- Cal: this scaffold, precedent table filling (links not prose), counterargument pressure-testing, structure checks, task tracking in `projects/compliance_by_construction/`

## Next Steps (from projects.md)
Pick one pressure point to pressure-test next. Suggested order: 2 (precedents) → 1 (formalizability theory) → 3 (calcification) → 4 (inference vacuum) — builds foundation before hardest differentiated claim.
