# Areas

Ongoing responsibilities with no end date — unlike projects. Team brains live here.

## Structure

```
areas/{area_name}/
  overview.md — purpose, stakeholders, rhythms, current priorities
  key_docs.md — link + 1-line summary, not full copies
  rhythm_of_business.md — optional, cadences
  team_brain.md — optional, strategy + reporting notes
```

## Current Areas

- `data_risk/` — Data Risk Analytics Lead role, pod reporting, pod digests
- `user_risk/` — User Risk counterpart (TBD — create when needed)
- `risk_de_org/` — org management, hiring, performance

## Naming

Snake case: `data_risk`, `user_risk`, `risk_de_org`

## Cal's Role

- CAN draft summaries, extract key points from ingested docs
- CAN update overview.md and key_docs.md when new doc ingested
- CAN NOT store A/C priv or user data — link + TLDR only (Tier 2 rule)

## Team Brain Ingestion (Workflow #2)

When Tony says "add to team brain" with a doc URL:

1. Fetch via meta CLI on demand: `meta google.docs get --id <ID>` or `knowledge_load` for Workplace
2. Summarize: what changed, why it matters, flags for discussion
3. Route: if Data Risk strategy / pod report -> `areas/data_risk/`
4. Update `overview.md` + `key_docs.md` with link + 1-line summary
5. If decision emerges -> `decisions/decision_log.md`
6. Do NOT copy full sensitive content into repo.

No auto-sync. Old system failed because sync was a pipeline. Now on-demand only.
