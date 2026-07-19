---
title: "Data Access Security for Nest Data Apps: Why We Should Follow the DaiQuery/Bento Model"
date: 2026-03-09
audience: engineers
status: draft
tags: [nest, data-apps, dva, security, privacy, data-access]
---

# Data Access Security for Nest Data Apps

**TLDR:** Nest Data Apps should adopt the DaiQuery/Bento security model — viewer-credentialed queries, no delegated access. Replicating DVA would conflict with current privacy requirements, amplify exposure risk in an AI-generated app ecosystem, and move us in the opposite direction from where privacy infrastructure needs to go. The friction problem is real, but the fix belongs upstream in access provisioning, not at the dashboard layer.

## Context

Nest Data Apps are positioned to succeed Unidash as Meta's primary dashboarding platform. The `@nest/data-apps` library — built on Quartz, the same query backend as Unidash — already supports Presto, M360, Scuba, and ODS data sources. Sevearl Data Engineering teas are building all or many new dashboards in Nest, and I expect that we will see investment move away from Unidash over the course of 2026.

One critical design question remains open: **how should Nest Data Apps handle data access security?**

Today, Nest uses viewer-credentialed queries by default. When a viewer opens a Nest Data App, queries run under the viewer's identity. If the viewer doesn't have access to the underlying table, they don't see the data. This is the same model DaiQuery and Bento use.

The Nest team has acknowledged that a "DVA-like experience" is a top priority. DVA (Dashboard Viewer Access) is Unidash's delegated access model, where the dashboard owner requests data access once for a dashboard-level identity, and all viewers see data through that identity — without needing direct table access themselves.

We should not replicate DVA. Here's why.

## The Case Against DVA on Nest

### 1. DVA conflicts with current privacy requirements

DVA works by decoupling the viewer's identity from the query identity. The dashboard's DVA ACL — not the viewer — is the credentialed actor. This means viewers can see data from tables they have no individual access to.

This was a reasonable design when it was built. But current privacy requirements expect the viewer's own identity to govern data access. A DVA implementation that lets viewers see data they can't directly access conflicts with these requirements. **[TODO: cite specific privacy policy/requirement that prohibits delegated data access without viewer-level authorization.]** And a privacy-compliant version of DVA — one constrained enough to satisfy current requirements — would be so restrictive that its users would reject it, likely requiring diffrential privacy . It would have all the complexity of DVA with none of the convenience.

### 2. AI-generated apps change the threat model

Nest Data Apps can be created via Hatch (an AI app builder) or Claude Code. This is a feature, not a bug — it dramatically lowers the barrier to building data tools. But it also means the number of data apps will grow fast, and many will be built by people who aren't thinking deeply about data access implications.

We've already seen this play out. In February 2026, a "vibe coded" Hatch app called `ai_teamwars_hatch` surfaced AI token usage data company-wide — any employee could look up any manager's token consumption, see leaderboard rankings, and break down usage by tool. The data was supposed to be scoped to "you and your directs." The app's data access was revoked shortly after launch, but not before it demonstrated the pattern.

The root cause went deeper than a missing ACL. There's a known bug in the Nest-to-Quartz pipeline: CAT tokens aren't propagated through the thrift-proxy handoff, so queries execute as `svc:onyx` (a service identity) rather than the authenticated viewer. This means the "viewer-credentialed" model that Nest advertises — "Security by default, automatic authentication with user permissions respected" — has a gap in its actual implementation. Queries may run with service-level permissions regardless of who's viewing the app.

This matters for the DVA question in two ways. First, it shows how quickly AI-generated apps can create exposure — someone built a data-surfacing dashboard with no access control review in what appears to be a few hours. Second, it reveals that Nest's identity propagation isn't fully working yet. Building a delegation model (DVA) on top of an identity chain that already has gaps would compound the problem.

DVA would amplify the broader risk. Without DVA, the table ACL is the last line of defense — if the viewer doesn't have access, they don't see the data. With DVA, that check disappears. A carelessly configured DVA identity on a quickly-spun-up Nest app becomes a hole in the access control surface.

### 3. The direction is zero-trust, not more delegation

Srikanth Sastry's recent RFC, ["AI Breaks the Privacy Threat Model"](https://docs.google.com/document/d/1Qh2V8sXLYWCgUG75r1bW0askS1o7ipKFul7Nzf9DqFc/edit), makes a compelling argument that privacy enforcement can't rely on caller intent. AI agents don't have intent — they optimize for task completion. When they hit a privacy enforcement error, they debug it and find a workaround. The doc demonstrates this with concrete examples: an AI forging a PES CAT token to bypass soft-match policy, an AI reading TAO directly to skip Policy Zone enforcement, an AI writing a custom FBLearner operator to bypass Koski PPF.

The common pattern across all three examples: **privacy enforcement lives in an application layer that can be bypassed by going to the storage layer below it.**

DVA adds another application-layer trust relationship. It assumes the dashboard owner will make good decisions about what data to expose. That's an intent-based control — exactly the kind of control that Srikanth's doc argues is a category error in a world with AI agents. The DaiQuery/Bento model doesn't depend on anyone's intent. Your identity is your identity. The system evaluates your permissions at query time. There's no delegation to exploit.

## The Friction Objection

The obvious counter-argument: DVA exists because viewer-credentialed access creates friction. If a dashboard uses restricted data and every viewer needs direct table access, you get N access requests instead of one. This is real friction that affects real people.

But the solution to that friction is upstream, not at the dashboard layer.

The SPARE initiative reduced Data Warehouse friction by 33% in 2025 — not by removing access checks, but by making access easier to get. Streamlined ACL provisioning, better data aggregations, Accessmate integration. The right response to "viewers can't access the data" is to make access provisioning faster and easier, not to create a bypass that lets them see data they don't have permissions for.

If we build DVA into Nest to solve the friction problem, we're treating the symptom. And we're doing it by introducing a delegation surface that's harder to govern, harder to audit, and misaligned with where privacy infrastructure is headed.

## Recommendation

**Nest Data Apps should adopt the DaiQuery/Bento security model: viewer-credentialed queries, no delegated access.** Specifically:

- **Queries run as the viewer.** The viewer's identity governs all data access. Standard ACLs, RBAC, and Policy Zones are evaluated against the viewer's permissions at query time.
- **No DVA-equivalent.** Dashboard authors cannot grant viewers access to data the viewer can't directly access.
- **Invest in upstream friction reduction.** Work with SPARE and Accessmate to make it easier for viewers to get the access they need — not to bypass the access check entirely.
- **Fix identity propagation.** The `svc:onyx` bug — where queries run as a service identity instead of the viewer — needs to be resolved before any security model can be trusted. Viewer-credentialed access only works if the viewer's credentials are actually being used.
- **Surface access control status at build time.** When a developer connects a Nest Data App to a data source, the platform should tell them whether that source has ACLs, whether the app's queries will enforce viewer permissions, and what happens when a viewer doesn't have access. Today, developers find out after deployment — or don't find out at all.

## What This Doesn't Solve

This recommendation doesn't eliminate data access friction. Viewers of Nest dashboards that use restricted data will still need to request access to the underlying tables. That's a real cost.

But it's a cost we can reduce through better tooling (faster provisioning, clearer error messages, self-service access flows) rather than through weaker security. And it avoids introducing a new delegation surface at exactly the moment when the number of data apps — and the ease of creating them — is about to explode.

## Open Questions

- **Certification and governance.** Nest doesn't yet have dashboard ownership, monitoring, or certification at parity with Unidash. Regardless of the security model, these gaps need to close before Nest can fully replace Unidash for restricted data use cases.
- **Data lineage.** Usage from Nest dashboards isn't fully captured in Meta's lineage systems yet. This affects auditability for both security models.
- **Query transparency.** Unidash lets viewers inspect the underlying SQL. Nest should provide this as a standard feature, not leave it to individual app developers.
- **Risk review.** Should we formally challenge DVA's current compliance status through a risk review? If DVA on Unidash is also non-compliant with current privacy requirements, that's a broader conversation — but it strengthens the case for not replicating it on new infrastructure.
