# Compliance-by-Construction Thesis — Handoff Extract
*Prepared 2026-07-21 for use in a separate agent thread. Self-contained; no prior context required.*

## Author context (minimum needed)
Tony Harper — Analytics Director at Meta (8 years), leads a ~30-person London org spanning Data Risk, User Risk, and AI Data Enablement. Prior: 11 years at Humana. This is his own thesis; he writes the prose himself — the assistant's role is scaffolding, pressure-testing, and iteration only. Full publication is escrowed until after he leaves Meta; the conceptual/architectural layer may be advanced now through standards bodies (NIST CAISI consortium, ISO/IEC JTC 1/SC 42 via INCITS, IEEE), ideally by joining Meta's existing delegations. The thesis also functions as his career filter (e.g., Waymo as the purest industrial expression; Datavant, Stripe as compliance-as-product cases) and appears in his LinkedIn About section.

## Working thesis (one line)
The friction model of data governance is failing from both ends at once — practitioners defeat the controls from below, and the rules misdescribe the technology from above — and closing the gap requires moving controls into the substrate **and** rewriting the rules for how models learn. Neither half works without the other.

## Structure: two halves

### Half one — failure from below (controls)
- Current governance = detection + enforcement (retention-violation detection, deletion enforcement, non-compliant-dataset flagging).
- Under time/business pressure, researchers route around all of it: stash data in random filesystems to keep training sets stable, evade detectors, or refuse outright.
- Implication: detection-based governance is partly theater — it works on the already-compliant and is defeated by exactly the population whose behavior matters most.
- Fix: **compliance by construction** — controls baked into datastores and pipeline tooling so the compliant path is the *only* path and the *frictionless* one. A non-compliant dataset cannot be assembled, and compliant researchers aren't slowed.
- Quotable principle: *you can't route around a control that **is** the substrate.*
- Named limit (the seam to half two): only *formalizable* rules compile into the substrate (retention windows, deletion propagation, access control). Judgment-laden rules (purpose limitation, "a use people would reasonably expect") can't be compiled and must be resolved at the level of the rule itself.

### Half two — failure from above (rules)
- Existing regulation is a category error: written for ~2015 user-facing transactional data; does not map onto model training workflows.
- Frontier claim 1: **deletion rights are conceptually broken** against a stable training set or learned weights; machine unlearning does not reliably satisfy the legal right as written.
- Frontier claim 2: **competition rules have no theory of inference.** They were written around data combination (joins, record linkage); a model that infers rather than matches creates a vacuum at the center of the regulatory regime that almost nobody is articulating publicly. This is the most differentiated claim in the thesis.
- A Wall Street reporting anecdote is earmarked as the Meta-specific illustration.

## Open iteration agenda (pressure points identified, not yet worked)
1. **Formalizability boundary needs a theory, not examples.** Candidate criterion: a rule compiles iff its satisfaction is decidable from metadata present at pipeline time. Implication: the boundary may be *movable* (e.g., consent scope becomes formalizable if consent is captured as structured data at ingestion) — a stronger claim than "some rules don't compile."
2. **Name the precedents.** Memory-safe languages vs. static analyzers (Rust made use-after-free inexpressible rather than better-detected), type systems, policy-as-code (OPA, Sentinel), capability-based security, differential privacy as a construction primitive for a formerly judgment-laden concept, and the engineering-safety "hierarchy of controls" (elimination > detection > PPE) as a century-old empirical foundation.
3. **Strongest counterargument = calcification, not difficulty.** Substrate controls encode today's interpretation of a rule at scale; if the rule changes or was encoded wrong, the error is built into everything, whereas detection failures are local. The thesis needs an account of substrate versioning and governance of the constructors themselves ("who audits the compiler?").
4. **The inference vacuum deserves its own act.** Claim 2 is currently thin scaffold; it could carry a third of the piece. Open question: what would a theory of inference in competition law look like — is inferred data "combined" data?
5. **The Humana thread is unused.** Eleven years in healthcare data (the most compliance-saturated data environment in the US) provides a second industry proof point that pre-dates the AI framing, making the argument durable rather than trendy.

## Working norms for any assisting agent
- Tony writes the prose; produce scaffolds, structure, counterarguments, and precedent research — not drafts of his voice.
- Keep implementation-layer Meta specifics out of anything intended for external circulation; the conceptual layer is the shareable layer until exit.
- The two-sided structure (below + above) is the thesis's architecture — do not collapse it back into "construction beats detection."
