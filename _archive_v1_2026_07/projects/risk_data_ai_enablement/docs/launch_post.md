<!-- Source: https://fb.workplace.com/groups/992063232674504/permalink/1391829086031248/ -->
<!-- Title: Risk Data AI Enablement (Launch Post) -->
<!-- Date Accessed: 2026-03-31 -->
<!-- Published: 2026-02-19 -->

# Risk Data AI Enablement

*Posted by Tony Harper | Collaborators: Sunil Rathode, Chris Ventura*

---

## TLDR

The Risk Data AI Enablement program is making our data "AI-ready" -- structuring and enriching Risk data so AI agents like Analytics Agent, Datamate, and Devmate can understand and interact with it accurately.

**Why this matters:** Initial tests show poor pass rates when AI agents query Risk data out-of-the-box. By adding proper context through Semantic Models and Repo Context, we've seen 10-60% improvements in accuracy across domains that have adopted this approach.

Questions? Reach out to Chris, Sunil, or Tony -- or leave comments on this post.

---

## Call to Action

Are you a Data Engineer or Data Scientist working on Semantic Models or Recipes, or interested in making your data AI ready? Join our program! We're actively onboarding teams and domains to build high-quality context that powers AI tools across Risk.

Get involved:
- Join our office hours for support: https://fburl.com/meeting/j3pkrdb9
- Connect with us in the Semantic Models workplace group: https://fb.workplace.com/groups/1991251848365266
- Review the Semantic Models runbook to get started: https://fburl.com/semantic-models-runbook
- Track our progress in the project repo: https://www.internalfb.com/code/fbsource/fbcode/dataswarm-pipelines/dataswarm_commons/privacy/data_ai_enablement/

---

## Goal

Make all Risk data domains AI-ready, enabling partners and teams to move from manual queries and inconsistent answers to automated insights and reliable self-service.

---

## The Approach: Two Pillars of Context

### Semantic Models

**What It Is:** Structured business knowledge about data -- metrics, definitions, business rules, lineage, join patterns.

**Why It Matters:** Provides AI agents a single source of truth; reduces hallucinations and incorrect answers.

### Repo Context

**What It Is:** Codified knowledge about pipelines -- skills, rules, architecture docs, testing patterns, on-call playbooks.

**Why It Matters:** Enables faster development, easier debugging, and reduced onboarding time for new engineers.

**Current Tooling State:** Semantic Models are now in Beta release with tools like Datamate and Analytics Agent. Repo Context bootstrapping is in progress with a live prototype.

---

## Program Outputs

1. **Evals for Risk Data Domains** -- Comprehensive evaluation sets measuring AI agent performance on Risk-specific queries
2. **Semantic Models for Key Domains** -- High-quality, consistent models covering critical Risk data domains
3. **Repo Context for Core Repos** -- Well-maintained context for our most important data repositories
4. **Use Case Integration** -- Expanded integrations beyond Analytics Agent and Datamate

---

## Timeline & Current Status

- **Phase 1: Foundation** -- Focus: Core engine for context creation and validation. Status: In Progress
- **Phase 2: Scale** -- Focus: Expand to high-priority domains; refine playbooks. Status: Planned
- **Phase 3: Full Adoption** -- Focus: 100% coverage across Risk. Status: Planned

---

## How We Measure Success

- **Eval Pass Rate:** Target 85% on our "Golden Set" of evaluation queries
- **Domain Coverage:** Target 100% of key Risk domains with Semantic Models
- **DE Adoption:** Increased % of AI-generated diffs
- **XFN Self-Service:** Partners confidently using AI tools for data needs

---

## Resources

- Semantic Models Wiki: https://www.internalfb.com/wiki/Semantic_Models_for_Data/
- Getting Started Runbook: https://fburl.com/semantic-models-runbook
- Detailed Project Tracker: https://www.internalfb.com/code/fbsource/fbcode/dataswarm-pipelines/dataswarm_commons/privacy/data_ai_enablement/plans/detailed_project_tracker.md
- Measurement Plan: https://docs.google.com/document/d/1sSi-RoizS0LoDaaFBU_-w8KYmo8NeX00wP-QJrS3f_s/edit?tab=t.xa4zn9uixen9
