# Second Brain Analysis — Why This One Actually Gets Used

This document is an analysis of this second brain (`miles/`) as a genuinely useful system, written for another Claude Spark instance building a professional version. Based on full directory inspection July 2026.

## Scale

- 28 top-level folders, 1221 markdown files (2412 files in `health/` alone due to Paprika HTML source + converted MD + daily logs)
- 231M working directory (excluding .git) — includes recipe library, collection CSVs, transcripts, photos
- 116 commits in last 90 days, ~1.3/day. Git log shows `Update travel`, `Update record_collecting,travel` pattern from `sync.sh`. Always a few modified files (currently `deadwax-decode-log.md`, `record_store_visits_2026.md`).
- Actively dirty repo = actively used system.

## What's Working Well — Architectural Principles

### 1. Folder = Domain, CLAUDE.md = Contract

Every domain folder has its own `CLAUDE.md` that defines:
- File naming convention
- Entry format / markdown schema
- Claude's role boundary (can-draft vs proofread-only)
- Tone and voice rules
- Workflow steps

Examples:
- `travel/CLAUDE.md`: H1 = title only, `*italics*` for work titles, `**bold**` for emphasis, `<<placeholder>>` for WIP. Explicit: "Never rewrite or draft prose. Tony writes everything." Trip folders named `{year}_{destination}_{month}`, files `{type}_{destination}_{month}_{year}.md`. Also holds traveler ops data: loyalty numbers (Alaska 260393232), TSA PreCheck.
- `record_collecting/CLAUDE.md`: One MD per year, month headers, city subheaders, visit entries `**M/D/YY - Store Name**`, purchases list introduced by `Purchases:` line, format `- Artist - Album (pressing details)`. Genres, pressing detail importance, blunt opinions allowed. "Do NOT rewrite my descriptions — formatting fixes OK."
- `record_collecting/listening/CLAUDE.md`: Bench listening project (not casual log). Scope Phase 1 = 2026 acquisitions queue, Phase 2 = 514 blank-media-grade backlog. Workflow: pull batch, clean, play front-to-back, play-grade (Goldmine M/NM/VG+/VG/G+/G, media=play grade), visual sleeve grade, transcribe deadwax if needed, log in `sessions_{YEAR}.md`, update Discogs. Multi-copy showdowns in separate `play_grade_queue.md`.
- `dnd/moondance/CLAUDE.md`: 190-line campaign bible. Character, party table, story so far (3 acts), current arc (Shard Globe / Bridge Fort), villains, NPCs at Gauntlet, active plot threads, world reference in `moondance_portal/`, session recap template, transcript processing pipeline: `transcripts/to_process/` -> write recap with 8 sections -> update 4 reference docs (`npcs.md` 60+ by faction, `locations.md`, `plot_threads.md`, `items.md`) -> update `session_numbering_notes.md` -> move to `processed/`.
- `health/CLAUDE.md` + `exercise/` + `food/`: Exercise logs `YYYY_MM_DD.md` with tables. Food has `diet_tracking_handoff.md` (239 lines) — a spec for other Claude instances: daily targets 1700-1900 cal / ~150g protein, weekly weigh-in Mon 5:30AM, meal routines (Chipotle usual = double chicken black beans no rice = 650/78g), historical performance (60g -> 140-160g once breakfast formula), tone guidance.

This local contract pattern is the core innovation. It bounds hallucination and makes the system scale.

### 2. Plain Markdown + Git + VS Code

- Global conventions in root `CLAUDE.md`: Markdown only, `lowercase_with_underscores`, no wiki-links or frontmatter, no over-structuring unless folder's own CLAUDE.md says so.
- `sync.sh`: check for changes, `git diff --name-only` for staged/unstaged/untracked -> `cut -d'/' -f1` -> dedupe -> commit message `Update {folders}`, `add -A`, `commit`, `pull --rebase`, `push`. Low friction daily backup + mobile access via GitHub web.
- Generated files respected: `collection_main_*.md` split from Discogs CSV via `generate_collection.py`, newest `pentrant-collection-*.csv` auto-detected, source-of-truth is Discogs. Fix data there, re-export, regenerate, `git diff` to review. Price research lives in `to_sell_prices.json`, merged during generation.
- `~/.venvs/miles` with fpdf2 for finance PDFs, Kubera MCP for net worth, Python tooling isolated.

### 3. Voice Protection Boundary

Split defined in root `CLAUDE.md`:

Claude does NOT draft:
- `writing/` — journal, creative writing
- Travel reports in `travel/` — trip reports

Claude proofreads only: flags typos/grammar/unclear phrasing briefly, comments on structure/pacing/imagery as observations, quotes original exactly when discussing, never silently rewrites.

Claude CAN draft:
- Travel plans, packing lists, todos
- `book_collecting/`, `record_collecting/` — formatting and organizing, not rewriting descriptions
- `live_shows/`, `reading/`, `classes/`, `dnd/`, `home/renovation`, `home/maintenance`, `home/storage`, `health/food`, `health/exercise`, `electronics/`, `auto/`

This trust boundary is why actual personal writing lives here. Voice stays owned.

### 4. Version-Controlled Memory (The Real Second Brain)

`memory/` has 25 files indexed by `MEMORY.md`, typed with prefixes:

- `feedback_*` — interaction bug fixes, meta-learning about Claude's mistakes:
  - `feedback_listening_log_flow.md`: Share background in chat first, wait for thoughts, *then* write combined entry to log. Don't dump incomplete background beforehand.
  - `feedback_budget.md`: Recommend best-in-class gear, not best-value; budget not a constraint.
  - `feedback_pressing_lookup.md`: When Tony adds records, lookup Discogs for matrix/stamper details.
  - `feedback_packing_lists.md`: Make them detailed and granular, not high-level.

- `project_*` — multi-month initiatives:
  - `project_deadwax.md`: Pressing provenance, runout decoding, engineer census
  - `project_collecting_plan_2026_2027.md`: Net seller ~100 out rest of 2026, Julian-focused London trips, Tokyo 2027 needs shelf space
  - `project_listening_grading.md`: Bench sessions in `record_collecting/listening/`, Phase 1 haul-first then 514 blank-grade backlog
  - `project_career_insurance_reserve.md`: $600k tiered reserve, AI displacement thesis, 46% tax math
  - `project_duplicate_two_houses.md`: Managing two properties with own collections

- `user_*` — deep personal context:
  - `user_background.md`: Louisville native, Ear X-Tacy formative
  - `user_audio_philosophy.md`: Gear philosophy, listening style
  - `user_intensity_pattern.md`: Bursts are trigger-response (sales, moves, tool shifts), match pace, respect rest after
  - `user_second_scene_julian.md`: Watford prog/jazz shop relationship worth nurturing
  - `user_sw_pt.md`: Steven Wilson deep catalog, no need to recommend basics

- `reference_*`:
  - `reference_kubera_mcp.md`: OAuth MCP, stateless HTTP only
  - `reference_python_venv.md`: Use `~/.venvs/miles`

Stored in repo root `memory/` not in `~/.claude/projects/.../memory/`. This makes memory survive compaction, model changes, and migration from claude.ai -> local. The other Spark instance should copy this typed-memory pattern.

## What Shows It's Genuinely Used

**Daily habit signals:**
- Git commits almost daily, auto-message shows changed folders — habit is `record_collecting`, `travel`, `live_shows` most frequent.
- Uncommitted changes always present today (`deadwax-decode-log.md`, `record_store_visits_2026.md`).
- `travel/` = 38 trip folders from `2023_candlestick_point_mar` through `2026_uk_italy_jul`. Each trip folder contains: `plan_*.md`, `packing_*.md`, `todo_*.md`, `adjustments_*.md`, `report_*.md`, plus PDFs, HTML research (`iceland_jun_2026.html`), `FlightyExport`, `Your trip confirmation.pdf`. Not notes — operational bundles.
- `record_collecting/record_store_visits_2026.md` 735 lines by July. Personal blunt reviews: "Immediately got a sketchy feeling about this place — it's attached to a vintage clothing shop... tripped on the curb... This was not the well-curated record store that I love. This was more like a flea market. We beat a hasty retreat."
- `record_collecting/listening/sessions_2026.md` bench entry example: transcription of deadwax `CAS 1051A-1U 'BOBIL' GO 1` -> Bob Hill Trident, grading `VG/VG (Side B scratch audible every revolution)`, impressions in Tony's voice: "musically this is fantastic, though I think I like it less than H to He", actions `-> showdown table copy 5; Discogs update pending`. Cross-refs to decode log and queue.
- `health/food/diet_tracking_handoff.md` 239 lines: daily macro targets, itemized meal routines with cal/protein/fiber, Chipotle strategy (double meat, skip rice), David Bar bridge snack, alcohol math (one vs two drinks), exercise routine (Peloton 20-min ~3x/week, Daphne walks 1.5mi), recipe library search guidance, historical weeks 1-3 with calories/protein/drinks and trend analysis.
- `finances/`: `budget.md`, `account_map.md` + PDF, `advisor_summary_2026_06.pdf`, `financial_plan_2026_2034.md`, `tax_analysis_2025.md`, `snapshots/`, `generate_pdf.py` with fpdf2. Real numbers, not templates.
- `wine/`: `cellar.md` inventory by box, `calendar.md` month-by-month by urgency, `subscriptions.md`, `log.md` tasting notes. Workflow: open bottle -> remove from cellar -> add to log -> update calendar.
- `home/renovation/`: `carmelita/` + `nelson_nest/` each with `overview.md` + `projects.md` with checkboxes and Active/On Hold/Complete.
- D&D weekly Sunday Zoom, 40 recaps of 51 sessions, 158 files in `dnd/`, transcripts pipeline actually exercised.

**Evolution from use:**
- `listening_log/` archived 2026-07-14 with explicit superseded notice in root CLAUDE.md — shows system iterates when pattern fails, not just accretes.
- Deadwax project spun out to `record_collecting/deadwax/` with `deadwax-decode-log.md`, `deadwax-lore-seed.md`, `deadwax-project-instructions.md` when runout decoding became its own rabbit hole.
- `health/` split into `food/meal_tracking/` with `day{N}_meal_plan.md` + `recipes/md/` converted from Paprika + `segments/` high-protein indexes.

## How He Uses It — The Loop

1. **IRL event happens**: record store visit, trip, meal, workout, D&D session, opens wine bottle, home project.
2. **Raw dump**: Tony writes blunt impressions in VS Code or dictates to Miles in chat.
3. **Claude formats per local CLAUDE.md**: organizes to required headings/tables, enriches (Discogs pressing lookup via matrix, nutrition estimates from recipe library, loyalty numbers, TSA PreCheck).
4. **Operational use next day**: packing list checked at airport, calendar says urgency bottle to open this month, exercise log informs next session, trip credits surfaced for booking, deadwax transcription decoded later.
5. **Memory capture**: Interaction friction -> `feedback_*.md` file so next session doesn't repeat mistake. New preference -> `user_*.md` or `project_*.md`. Long-term learning lives in git.
6. **Sync**: `./sync.sh` -> GitHub private repo -> backup + mobile readable via GitHub web + version history.

Key workflows:
- **Travel**: Research/planning phase = Claude drafts `plan_*`, `packing_*` (detailed granular per feedback), `todo_*`. Checks `trip_credits/trip_credits.md` proactively, surfaces expiration. Trip happens. Tony writes `report_*` in his voice, Claude proofreads only (quotes original exactly when flagging). Recommendations go to `recommendations_and_preferences/`.
- **Record collecting**: Visit -> Tony impressions -> Claude formats to yearly file with city/region headers -> pressing lookup -> later bench session in `listening/` grades it, transcribes deadwax -> decode log entry -> updates Discogs grade -> if multi-copy, feeds showdown table -> if sell candidate, flags for collecting plan net seller goal.
- **Health**: Meal described -> Claude builds entry with nutrition table, running daily total `| Running Total | ~XXX | ~XXg |` and remaining budget. End of day summary `Day X — Weekday, Date: ~X,XXX cal | XXXg protein`. Wine counted as calories normally. No lecturing on diet.
- **D&D**: New transcript dropped in `transcripts/to_process/` -> Tony says "Process session X" -> Claude reads chunks -> writes `session_recaps/session_XX.md` with template (Date, Recap, Key Events numbered, Combat, NPC Interactions, Character Moments, Discoveries, Open Threads, End State) -> updates 4 ref docs (npcs by faction, locations geographically, plot threads active/resolved/foreshadowed, items) -> updates numbering notes -> moves transcript to processed -> updates root campaign CLAUDE.md only for major story shifts.
- **Home/Wine/Auto/Electronics**: Inventory + maintenance logs + change log — reference that gets updated on action, not aspirational.

## What a Professional Version Should Look Like

Preserve all structural principles above. Map domains to work:

### Folder Structure for Professional Second Brain

```
CLAUDE.md — global: lowercase_with_underscores, MD only, no frontmatter, voice (blunt/data-driven/no corporate filler), where Claude can/can't draft, sync via ./sync.sh

work/
  CLAUDE.md — work-specific voice, working hours, communication norms
  meetings/
    CLAUDE.md — file naming YYYY_MM_DD_topic.md or {year}_{project}_{month}/ like travel, H2 per agenda item, Decisions/Actions with owner+date
    2026_projectname_jun/
      plan_projectname_jun_2026.md, notes_*, followups
  projects/
    CLAUDE.md — one folder per active project pattern (reuse carmelita/ pattern)
    projectname/
      overview.md — status, stakeholders, links, key docs
      projects.md — Active/On Hold/Complete with checkboxes - [ ] / - [x]
      decisions.md — or reuse top-level decisions/
  decisions/
    decision_log.md — date, context, options considered, chosen, why, revisit date. Like deadwax — provenance matters.
    Or one file per decision: YYYY_MM_DD_decision.md
  people/
    CLAUDE.md — how to capture: observations not judgments, private notes boundary
    person_name.md — role, team, working style, last 1:1 topics, context (reuse user_* pattern). Not CRM, memory.
  goals/
    goals_2026.md — quarterly goals, metrics
    checkins/
      YYYY_MM_DD.md — weekly check-in (reuse exercise daily log format: date title, table)
  learning/
    log.md + topic files (reuse listening_log -> listening/ evolution)

memory/ — keep typed prefix system exactly:
  feedback_claude_work.md — interaction bug fixes at work
  project_*.md — multi-quarter initiatives, e.g. project_platform_migration.md
  user_*.md or person_*.md — deep context on frequent collaborators, manager, skip-level
  reference_*.md — runbooks, MCP configs, env setup (like reference_python_venv.md)
  MEMORY.md — index with descriptions

templates/
  meeting.md — empty skeleton with Decisions/Actions sections
  project_overview.md
  decision.md
  person.md
  weekly_checkin.md

daily/ (optional, like travel todo pattern)
  YYYY_MM_DD.md — scratch that rolls up to projects, quick capture for other Spark instance

scripts/ or tools/ (like generate_collection.py, kubera_oauth.py)
  generate_status.py — pulls from source of truth (project tracker) and writes MD snapshot for git diff review
  Keep venv notes in reference_*.md
```

### Rules for Professional Version (Copy These)

1. **Local CLAUDE.md everywhere** — Don't rely on one global prompt. Each folder's CLAUDE.md is schema + role. Other instance should create them as first act in each new folder, following `travel/` and `record_collecting/` patterns.

2. **Voice protection** — Define where Claude does NOT rewrite: `work/meetings/` notes might be your voice only, Claude extracts actions. Or performance reviews, sensitive emails — proofread-only boundary builds trust to actually store real thoughts.

3. **Typed memory** — Copy `memory/` exactly: `feedback_`, `project_`, `user_`/`person_`, `reference_` + `MEMORY.md` index. Version-controlled in repo, not in session-local memory. This is how you learn across compaction and device changes.

4. **Plain markdown, git sync** — No Notion dependency day-to-day (he migrated from Notion for this reason). Git gives backup, history, mobile via GitHub web, `git diff` for generated file review. Keep `sync.sh` verbatim — auto-message from folder names is low friction enough for 1.3 commits/day.

5. **Generated files discipline** — Like `collection_main_*.md` from Discogs CSV, professional version can have generated status snapshots or meeting exports. Rule: mark as generated, never hand-edit, source-of-truth lives elsewhere, regen script documented in CLAUDE.md.

6. **Design for retrieval, not collection** — This second brain works because packing lists must be checked at airport, wine calendar says bottle to open this month, deadwax codes searched next purchase, D&D NPC list checked weekly Sunday, protein totals needed at next meal. Professional version fails if it's an archive. It must earn keep daily: tomorrow's meeting prep must require it, weekly update must require it, decision recall must require it. If a folder doesn't have a "must check tomorrow" use case, delete it.

7. **Operational loops** — Copy wine pattern: `cellar.md` (inventory) + `calendar.md` (by urgency) + `log.md` (history). For work: `backlog.md` + `sprint.md` + `log.md`, or `pipeline.md` + `runbook.md` + `incidents.md`. Closed loops, not docs.

8. **Evolution allowed** — `listening_log/` archived 2026-07-14 when workflow outgrew it. Professional version will have dead folders too. Root CLAUDE.md keeps list of archived superseded paths. Don't over-structure upfront — create folders as needed (global CLAUDE.md says this explicitly). Don't start with `tasks.md` at root, it dies (his did — real todos live in project folders).

9. **No lectures** — Health CLAUDE.md says "no unsolicited advice about diet or training." Work version same: track what was decided/done, not advice on what should have been done. Facts over coaching unless asked.

### What to Hand Another Spark Instance

Give it:
- Root `CLAUDE.md` pattern (copy Global Conventions + Claude's Role split)
- One example folder CLAUDE.md (use `travel/CLAUDE.md` structure + role + file naming + formatting)
- `memory/` typed pattern + `MEMORY.md` index format + two example feedback files showing meta-learning
- `sync.sh` script verbatim
- Directive: "Create sub-project CLAUDE.md files as new folders take shape, following patterns already established"

Then let it interview the user for 3-4 core daily workflows that must earn keep tomorrow — those become first folders. Not "set up second brain" — "what will you need to recall at 9am tomorrow that you decided today?"

## Context on This Specific Brain

- Owner: Tony Harper, Director of Risk Data Engineering at Meta, San Carlos CA + second home Hyden KY (childhood home of wife Anastasia)
- Interests: writing, history/western classics, travel, vinyl (classic rock/prog/metal/jazz — 2026 heavy acquisition year, now net seller), D&D 5e 2024 rules Paladin Edric in Moondance campaign, audio gear
- Personal: dog Daphne (1.5mi walks), F-150 at SDF for KY trips, protein shakes with Infinite Nutrition mix + Fairlife 2% milk
- Named this Claude instance Miles (D&D character + Miles Davis nod) — librarian/scribe role
- Migrating from Notion, edits in VS Code, lives as Markdown

## Files to Study for Professional Adaptation

If you want to steal patterns, read these in order:

1. `CLAUDE.md` root — global conventions, tone, role split, memory location
2. `travel/CLAUDE.md` — best example of trip folder layout + travel ops (loyalty, credits, TSA) + formatting rules + placeholders
3. `record_collecting/CLAUDE.md` + `record_collecting/listening/CLAUDE.md` — generated vs hand-written discipline + bench workflow + grading conventions + deadwax cross-ref pattern
4. `memory/MEMORY.md` + any `feedback_*.md` — meta-learning structure
5. `health/food/CLAUDE.md` + `diet_tracking_handoff.md` — operational spec for other Claudes, meal tracking table format, recipe segmentation
6. `dnd/moondance/CLAUDE.md` — example of deep campaign knowledge base + transcript processing pipeline that actually runs weekly
7. `wine/CLAUDE.md` — best example of 4-file closed loop (inventory + plan + log)
8. `sync.sh` — sync pattern
9. `record_collecting/deadwax/` — example of project spinning out to own subfolder when rabbit hole emerges
