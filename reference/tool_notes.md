# Tool Notes — How to fetch docs on demand

_No daily auto-sync. Fetch when you need it, summarize, link + TLDR only in repo._

## Google Docs

```
meta google.docs get --id <DOC_ID> --format text
# ID from https://docs.google.com/document/d/<ID>/edit
```

For updated check (like old gdocs revisions):
```
# Use revisions command if available via meta CLI — or just re-fetch and diff manually
```

## Workplace Posts

Use `knowledge_load` tool for Workplace URLs:
- Paste URL like `https://fb.workplace.com/groups/<ID>/permalink/<ID>/`
- Or use meta CLI search if needed

## Google Sheets

```
meta google.sheets get --id <SHEET_ID>
```

## Bento / Daiquery / Unidash

- Links only in repo — content in Tier 2
- If needed, use tool to get metadata, but don't need full data in brain

## Calendar (for morning pulls)

Use calendar skill if available — check today's meetings, attendees.

If not available, rely on daily/YYYY_MM_DD.md manual entry + meetings/ last 3.

## Security Reminder

- Don't paste full sensitive doc content into repo files
- Link + 1-line TLDR in reference/key_docs.md or areas/*/key_docs.md
- If doc contains user data, A/C priv, PII — never copy to Tier 1 repo

## Pod Digests (Data Risk)

Old system: Google Drive `~/My Drive/DataRiskPods/` with weekly markdown per pod.

New system: on-demand — when you need to review pods, list files in that Drive folder manually, or ask Cal to read specific ones. Don't auto-digest all 46 weekly.

If you build a regen script: `scripts/generate_pod_digest.py` reading Drive source, writing `areas/data_risk/pod_digest_YYYY_MM_DD.md` marked as `<!-- GENERATED -->`, source-of-truth = Drive. Document in script header.
