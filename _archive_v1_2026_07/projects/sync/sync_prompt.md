# Daily Context Sync

You are running Tony Harper's daily context sync. This pulls in new and updated documents relevant to his projects.

## What to do

### Step 1: Update existing docs

Read `projects/sync/manifest.yaml` to get the list of tracked docs.

For each Google Doc entry (type: google_doc):
1. Run `gdocs revisions DOC_ID` to check for updates since `last_checked`
2. If there are new revisions, re-fetch with `gdocs get DOC_ID --markdown` and overwrite the cached file
3. Update `last_checked` in the manifest

For Google Sheets (type: google_sheet):
1. Re-fetch with `gsheets get SHEET_ID` and compare to existing
2. Update if changed

Skip workplace_post entries — those don't change.

### Step 2: Discover new documents

Read `projects/sync/config.yaml` for tracked authors, keywords, and workplace groups per project.

**New Google Docs:** For each active project, search using `mcp__plugin_meta_mux__knowledge_filtered_search` with:
- `doc_types: ["google_document"]`
- `keywords`: project keywords from config
- `natural_language_query`: a natural description of the project topic
- `start_creation_time`: the date in `last_sync` from config (or yesterday if not set)
- `authors`: tracked author IDs for that project (search separately per author batch if needed)

Also do a broad search for docs by any tracked author across all projects:
- `doc_types: ["google_document"]`
- `authors`: all tracked author IDs
- `start_creation_time`: since last sync

Dedup results against the manifest (match by URL/doc ID). Collect candidates.

**New Workplace Posts:** For each project's workplace groups, search using `mcp__plugin_meta_mux__knowledge_filtered_search` with:
- `doc_types: ["workplace_post"]`
- `keywords`: project keywords
- `start_creation_time`: since last sync

Also search for workplace posts by tracked authors:
- `doc_types: ["workplace_post"]`
- `authors`: tracked author IDs per project
- `start_creation_time`: since last sync

Dedup against manifest. Collect candidates.

### Step 3: Generate triage file

Write a triage file to `projects/sync/triage/YYYY_MM_DD.md` with this format:

```markdown
# Context Sync — YYYY-MM-DD

## Updated Docs
<!-- List docs that were re-fetched due to new revisions -->
- [Title](relative/path/to/file.md) — N new revisions since last sync

## New Candidates

### project_name
| # | Title | Author | Type | URL | Suggested file |
|---|-------|--------|------|-----|----------------|
| 1 | Doc title | Author name | google_doc | url | docs/suggested_name.md |

<!-- Repeat for each project with candidates -->

### Unmatched (no clear project)
<!-- Docs/posts that don't clearly map to a project -->

## Stats
- Docs checked: N
- Docs updated: N
- New candidates found: N
- Last sync: YYYY-MM-DD
```

### Step 4: Update config

Update `last_sync` in config.yaml to today's date.

## Processing triage results

When Tony reviews the triage file and tells you which candidates to accept:
1. Fetch the doc content (gdocs get or knowledge_load)
2. Save to the specified project's docs/ folder with the suggested filename
3. Add a source URL header comment
4. Add the entry to manifest.yaml
5. If a new workplace group appears, add it to the project's config

## Important notes

- Only sync active projects (not _archive/)
- Use snake_case for all filenames
- Add `<!-- Source: URL -->` as the first line of every fetched doc
- Keep the manifest sorted by project
- If a doc fetch fails (access denied, etc.), note it in the triage file and move on
- Workplace posts are one-time fetches; Google Docs should be re-checked for updates
