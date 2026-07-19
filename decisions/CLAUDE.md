# Decisions

Decision log — provenance matters. Like deadwax in miles/: where decision came from and why.

## Options

1. Single file `decision_log.md` with dated entries (simple)
2. One file per decision `YYYY_MM_DD_decision_slug.md` (if decision warrants depth)

Start with option 1. Split to option 2 when decision needs its own doc.

## Format for decision_log.md

```markdown
# Decision Log

## YYYY-MM-DD — Decision title

- **Context**: What prompted this
- **Options considered**: including rejected and why
- **Chosen**: what we decided
- **Why**: reasoning, constraints
- **Owner**: who decided
- **Revisit**: when to reconsider, if applicable
- **Sources**: links to docs, meeting notes
```

## Rules

- Date every decision
- Include rejected options and why — provides transparency
- Link to sources, don't copy full content
- Update when decision changes — don't overwrite, add new entry with "Supersedes YYYY-MM-DD"

## Cal's Role

- CAN draft entry from provided context
- CAN link decisions to projects/areas
- Does NOT invent rationale not in source
