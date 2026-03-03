---
title: Unidash Is Dead
date: 2026-03-02
audience: engineers
status: draft
tags: [unidash, nest-apps, tooling, risk-analytics]
---

# Unidash Is Dead

## TLDR

Unidash was the right tool for a simpler time. But our dashboards aren't dashboards anymore — they're applications with query engines bolted on. Nest apps give us full-stack control, AI-native development, and the ability to build what we actually need instead of fighting what Unidash will let us have. Risk Analytics should start building new work on Nest and migrate our most painful Unidash dashboards over the next two quarters.

## The Problem With Unidash

I want to be fair to Unidash. For the standard use case — pull some Presto data, render a few charts, share a link with your XFN partners — it works. Drag and drop, publish, done. That covers maybe 80% of dashboard needs across Meta.

We are not in the 80%.

Risk Analytics dashboards have 50+ queries with Jinja templating, 60+ widgets, cross-widget event chains, and filter logic that would make a reasonable person cry. When you're operating at that complexity, Unidash stops being a tool and starts being an obstacle. Here's what we hit regularly:

**Performance is painful.** Large dashboards with Unified Filters enabled lag during editing, crash pages, and break grid alignment. The event propagation model — where every selector triggers a full React component tree reprocessing — compounds latency as dashboards grow. Our P90 page loads are nowhere near the team's 5-second target.

**Maintenance is a grind.** A simple logic change that touches multiple queries means clicking through widget after widget, updating each one individually. There's no way to make a coordinated change across a dashboard atomically. In code, this is a find-and-replace. In Unidash, it's an afternoon.

**The ceiling is low.** We can't do real-time data. We can't run LLM inference and render results inline. We can't build multi-step workflows or preserve state across tabs. We can't write custom interactive components. Every quarter, someone on the team has an idea that would genuinely help our partners, and the answer is "Unidash can't do that."

**The Configerator API is dying.** The programmatic API for building dashboards in code — the one thing that made complex dashboards manageable — is being deprecated. Its replacement, Unison, doesn't have feature parity yet. So the path forward for code-driven dashboards in Unidash is, at best, unclear.

None of this is a knock on the Unidash team. They're small, they've been through a reorg, and they're investing heavily in AI features. But the platform was designed for a different class of problem than the one we're solving.

## What Nest Apps Get Right

Nest is Meta's internal platform for building full-stack web apps — think Next.js, but wired into our infrastructure. React frontend, server-side rendering, backend API routes, direct access to XDB, InternGraph, Presto, and auth. You deploy from master and your app is live in minutes.

Here's why it matters for us:

**It's code.** Your dashboard is a codebase. You can refactor it, version it, review it, test it. A change that touches 15 queries is a single diff, not 15 manual widget edits. You get all the benefits of software engineering practices — because it is software engineering.

**The ceiling is gone.** Arbitrary React components. WebSockets for real-time data. LLM inference rendered inline. Multi-step workflows with preserved state. Custom visualizations. If you can build it in React, you can ship it in Nest. No more "the platform doesn't support that."

**It's AI-native.** This is the part I care about most. Nest apps are built on open-source stacks — Next.js, React, TypeScript — that every foundation model understands deeply. You can build a functional Nest app with Claude Code in a day. Teams across Meta are reporting full dashboard rebuilds in under a week. The `@nest/data-apps` library gives you `usePrestoQuery` hooks that handle auth and data fetching out of the box. The development loop is: describe what you want, iterate with the AI, ship it.

**Other teams are already moving.** Instagram rebuilt their Overview Dashboard as a Nest data app in under three weeks with three DEs. Horizon has migrated multiple dashboards. Security and Compliance is actively migrating. There's even a Claude Code skill that automates Unidash-to-Nest migration — extraction, scaffolding, component generation, the whole thing.

## What's Still Rough

I'm not going to pretend Nest is perfect. It's early, and there are real gaps:

**Discoverability.** Your XFN partners live in Unidash. They have bookmarks, muscle memory, and expectations. A Nest app at some `*.nest.x2p.facebook.net` URL doesn't get found. The workaround — embedding Nest apps in Unidash via iframe — works but adds complexity around auth and theming.

**Governance.** Unidash has built-in permissions, Dashboard Viewer Access, centralized controls. Nest has none of that by default. You roll your own with GK and ACLs. For Risk Analytics, where data sensitivity matters, this is something we'd need to solve deliberately.

**Data lineage.** In Unidash, an analyst can right-click a widget and see the underlying query. In Nest, that transparency only exists if you build it in. We should.

**Platform maturity.** Logging, error reporting, e2e testing — still being standardized. Production availability incidents have happened. The package management story is still evolving.

These are real concerns, not blockers. They're the kind of problems that get solved by teams building on the platform and pushing it forward.

## What This Means for Risk Analytics

We build complex, query-heavy, interactive tools for partners who need to understand risk signals, investigate anomalies, and make decisions. That's not a "dashboard" — it's an application. We've been building applications inside a dashboard tool, and it shows.

Nest lets us build what we actually need:

- Coordinated multi-query views with shared state
- Real-time signal monitoring
- Interactive investigation workflows with drill-down paths
- Inline model inference for anomaly explanation
- Custom components that match how our partners actually work

And we can build it faster, because the AI tooling actually works with the stack.

## What We Should Do Next

1. **Pick one high-pain dashboard and migrate it.** Something complex enough to prove the value, visible enough that our partners notice the improvement. Use it to build institutional knowledge and shake out the rough edges.

2. **Default new work to Nest.** Unless the ask is genuinely simple — a few charts, no interactivity, no custom logic — build it in Nest. Stop adding complexity to a platform we're moving away from.

3. **Solve governance early.** Don't wait until we have ten Nest apps to figure out permissions and data access controls. Build the pattern once, document it, reuse it.

4. **Build in data lineage.** Every query backing a component should be inspectable by the end user. Our partners deserve the same transparency they have in Unidash, and more.

5. **Embed in Unidash where it makes sense.** For tools that our XFN partners access through Unidash today, use the iframe embedding pattern to maintain discoverability while we build on Nest underneath.

Unidash served us well. But we've outgrown it, and the replacement is here. Time to move.
