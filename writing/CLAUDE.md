# Writing

Tony's writing. Voice protection is mandatory.

## Directory Structure (from v1 — keep)

- `essays/` — Personal essays, reflections, blog-style posts
- `proposals/` — Technical proposals and 1-pagers
- `decision-docs/` — Decision documents, option analyses
- `comms/` — Team communications, announcements, meeting materials
- `notes/` — Quick notes, rough thinking, and informal captures
- `style.md` — detailed voice/style guide (migrated from v1 claude.md, renamed to avoid case collision on macOS)

## File Naming

Date-first: `YYYY-MM-DD-title-in-lowercase-kebab-case.md`

## Frontmatter (optional)

```yaml
---
title: The Full Title
date: 2026-02-26
audience: engineers | leadership | general
status: draft | review | published
tags: [relevant, topic, tags]
---
```

## Cal's Role — Proofread Only

**For essays, proposals, decision-docs, comms:**

- Cal flags typos, unclear phrasing briefly
- Quotes original exactly when discussing: "Original: '...' — suggestion: ..."
- Comments on structure/pacing as observations, not rewrites
- **Never silently rewrites prose, never adds corporate filler, no exclamation**

**Cal CAN draft:**

- `notes/` — quick notes, outlines, brainstorming
- Formatting fixes, table structure, link curation

## Voice / Style — Authority is writing/style.md

Detailed guide lives in `writing/style.md` (was claude.md in v1, renamed for macOS case-insensitivity).
Read it before any writing work.

TLDR: direct, conversational-but-professional, contractions natural, warm without soft, plain language, no "leverage/synergies", mix short punchy + longer explanatory, em dashes for asides, Problem → Constraints → Options → Recommendation in tech writing, generous specific credit.

## Security

- No restricted data, PII, or A/C priv details in writing drafts stored in repo — link only
- If draft contains sensitive framing, keep in `private/` or Google Docs (Tier 2/3), not here
