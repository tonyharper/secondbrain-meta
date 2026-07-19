# Quickstart — points to reference/quick_start.md

This file exists so you can find instructions tomorrow or Tuesday without remembering folder structure.

**Open `reference/quick_start.md` for full rebuild instructions, 3 workflows, security model, and folder map.**

TLDR:

- 3 workflows: meeting notes ingestion, doc + team brain ingestion, morning pull
- Say "morning pull" tomorrow — Cal reads inbox/, meetings/ last 3, areas/data_risk, projects/*/overview.md, decisions/, people/
- Inbox: `inbox/meetings/` raw dumps -> "process meeting X" -> writes `meetings/YYYY_MM_DD_topic.md`
- Docs: `inbox/docs/` URL with Source header -> "add to team brain" -> fetches on demand via meta CLI, routes to areas/data_risk or projects
- Security: Tier 1 repo = links/summaries only, Tier 2 Drive/Docs = sensitive content on demand, Tier 3 private/ = local-only gitignored

Full details: `reference/quick_start.md`
