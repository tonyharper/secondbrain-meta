---
title: Risk DE Dashboard Strategy
date: 2026-03-02
audience: engineers
status: draft
tags: [dashboards, nest, unidash, governance, strategy]
---

# Risk DE Dashboard Strategy

Nest is winning. It's easier to build with — especially with AI — it looks better, and adoption across Risk is already outpacing Unidash. We're not going to fight that. We're going to get ahead of it.

The concern isn't the tool shift itself. It's what happens when anyone can spin up a dashboard with Risk data and nobody's checking whether the numbers are right. That's where we're headed if we don't set a clear direction now.

## How We Build

**New dashboards go in Nest.** Stop building new Unidash unless it's both urgent and high-priority, and the Unidash pattern is already well-established. If you're on the fence, ask — but the default answer is Nest.

**Everyone who builds dashboards learns Nest in H1 2026.** Not optional. We'll sort out the right way to support that — pairing, starter projects, dedicated time — but the expectation is clear.

## The Unidash Tail

We're not migrating everything at once. Most of it will get replaced naturally over time.

- **Important dashboards stay maintained.** If it's actively used and drives decisions, keep it working.
- **Don't enhance — rebuild.** If someone asks for significant new work on an existing Unidash dashboard, that's the trigger to build it in Nest instead.
- **Deprecate explicitly.** When a Nest replacement exists, redirect users, communicate the change, sunset the old one. No zombie dashboards.

## Governance

This is the part that matters most.

**Our dashboards set the bar.** Every Risk DE-owned Nest dashboard should:

- Use approved data sources and metric definitions
- Have testing coverage for key metrics
- Be clearly labeled as governed
- Follow naming and structural conventions we'll define together

**XFN dashboards — review the ones that matter.** We're not going to approve every dashboard someone builds. But the ones leadership sees, the ones that drive operational actions — those need a lightweight review. We validate data sources and metric definitions. We flag problems. We give teams a way to earn a "governed" designation.

**Metric consistency is the line.** If a dashboard shows Risk metrics, those metrics match our definitions. Full stop. Doesn't matter who built it or what tool they used.

## Open Questions

- What does "learning Nest" look like in practice — structured training, pairing, learn-by-doing?
- How do we identify which XFN dashboards warrant review?
- What's the right mechanism for the governed designation — a tag, a registry, something else?
- Can governance fold into existing workflows, or do we need to staff it?
