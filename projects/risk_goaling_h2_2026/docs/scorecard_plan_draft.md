# Risk H2 2026 Goal Scorecard — Plan Draft

_Last updated: 2026-07-21_
_Objective: Create repo-native scorecard pulling from overall goal tracker (Tier-1 Metrics sheet) and aggregating to format of goals v3 doc, then build export skills to detailed tracking + summarized v3-style format._

## What we have (source analysis)

### Source A: Overall Goal Tracker Sheet
- URL: https://docs.google.com/spreadsheets/d/1MCTfdFwYLl6VDrVthczHEd1OIQhMp1yRdjA9wY7pGFA
- Local: /tmp/risk_sheet_retry.xlsx 321KB, /tmp/risk_sheet_export.csv 44KB, html zip 560KB
- Tab H2'26 Tier-1 Metrics: 118 rows, 22 columns:
  - 0 Investment Priority (maps to Priority 1-4 + 1 extra: "Meet obligations" 26, "Youth Pressure" 26, "Transform AI" 58, "Unblock AI" 6, "AI adoption" 1)
  - 1 Human language goal (sub-goal, e.g., "1.1: Maintain...", "1.2: Operate inbound...", "Keep SIN within SLO...", "Obligations reach critical milestones faster")
  - 2 Goal Metric Name (individual metric, e.g., ">90% of L1+...", "% SINs under SLO", "Obligation wall time...")
  - 3 Risk Group Name (Youth 33, Risk Review 18, User Risk 13, AI Risk 11, Data Risk 10 etc)
  - 4 Type Existing/New/Ship Goal (New 43 Ship 41 Existing 28)
  - 5 Metric POC Analytics Team Member (Barnaby Cooper, Baris Cem Sal, etc)
  - 6 Goal/Tracking (Goal 106 Tracking 7)
  - 7 Definition / Milestone Description
  - 8 Definition Status (Finalized 56 Pending 23 In progress 13 Blocked 8)
  - 9-10 Will ready By 6/16 + Reason
  - 11 Target / Exit Condition
  - 12 T-Shirt Sizing + Reasons
  - 14 Operationalization Status + 15-16 Will operationalized by 7/16 + Reason
  - 17-18 Will be M360? + Reason
  - 19 M360/Dashboard Link
  - 20 Goal added to scorecard?
  - 21 Comments/Questions

- Other tabs: Consolidation View 901 rows (PA team mapping), North Star Metrics (5 NSMs), Timeline (stale H1 2025), Items to be Completed hidden, etc.

### Source B: Goals v3 Doc [IN PROGRESS]
- URL: https://docs.google.com/document/d/1U9vrVFRO4A_jbi7QhhDbYdWv8n834gq3udR3M1KTjQQ/edit?tab=t.94anu86ip79a
- Local: /tmp/risk_goaling_doc1_full.html 187KB, owner Stephanie Yee, 19 editors, status [IN PROGRESS] To Do numbers by July 15
- Structure: Table with 4 columns:
  - H2 Goal (plain language success by EOY) e.g., "1A. Land Aligned Response Plans and mature inbound response capabilities"
  - Goal Metrics (team-level metrics or milestones, bullet list with M1 M2 M3, often with xx% placeholders, includes specifics like "Ship EU AI Act Aug+Dec 2026", "Develop inquiries tooling 95% in tooling usefulness 70%", youth age assurance U18/U16/U13, Family Center App beta, TMH 100% requests, AI priority launches Hatch/Confidential VM/Wearables ambient, AIR decisions xx% within SLA no increase high residual risk, AI Governance framework, 4A Risk review sustainable Missed Risk <7% SINs under SLO Agentic Review Share xx% etc, 4B AI-native requirements change loop propagates to 2+ downstream, 4C Reduce SEV prevalence double proactive interception agent privacy Harden 90% Tier-1 etc, 4F Standardize AI-native pods AI Fundamentals bar eval quality, 4G Strengthen talent density)
  - Metric Owner (Accountable Group Lead, e.g., Zef RosnBrick, Allison Hartnett, Arash Nikkar, Susan Cooper, Abhishek Gulati, Nathan Davis, Kazuho Ozawa)
  - Risk Group Owner (e.g., All Areas Leads, Area Response Platform, RCP, Various, Youth, AI Risk, User Risk Data Risk Monetization, GRC Agent Oversight, Engineering Analytics & Research)
- Grouped by Priority headers with topline metric note:
  - PRIORITY 1: Meet our obligations (NSM1 ship goals)
  - PRIORITY 2: Youth pressure | Topline: Parental Alignment IG US +1ppt over H1 exit
  - PRIORITY 3: Unblock AI launches | Topline TBC (white-glove product critical decisions)
  - PRIORITY 4: Transform processes and Org for AI (contains 4A 4B 4C 4F 4G)
- Discussion questions at top (Goal 1C CI best practices Arash, Goal 4A Risk review resources non-forest + agentic refactored clarity + Nathan risk mitigation vs speed + ARR confidence partial vs full, Goal 4B requirements staffing Kristen Durkin Jackie Zajac)
- Data Risk narrative from Olivia Grace comment: 7 priority areas RD, RL Wearables, Cloud, Self-pref/cross-promo, Data In, Portability Access, Anonymization

### Source C: Data Risk Goal Map (bridges tracker ↔ v3)
- URL: https://docs.google.com/document/d/1p5m4E70gaSLc7fCmpZnpDp9GCbCYVPgn8eBNOiFhfDA
- Author Baris Cem Sal June 8 Draft, last modified Tony Harper June 18
- Ladder: Michel Org priorities WP (453092..., 195 react, 4 priorities detailed: Youth obligations at scale, EU enforcement Aug2026, FTC SVT ~945 obligations, Fraud & Scams; Youth step-change Age assurance/Parental alignment/Advocacy; Unblock AI Hatch riskiest confidential compute per-connector + Wearables ambient wiretapping biometrics go/no-go social acceptability + AI-native governance; Transform AI Agentic Risk Review default background agent-to-agent Forest all areas + Agent oversight flywheel autonomous continuous + Compliance automation) → Oliver Data Risk priorities WP (152400..., 38 react, P0-P5 order: 0 Keep Company Running BAU fast good decisions SIN SLA controls green SEVs MAPs, 1 Robust Global Controls Beehive DOJ Cloud yellow→green robust to agents embedding awareness, 2 Positions 7 areas, 3 Internal Efficiency UDI AMP ALP XSU Deletion Anonymization self-serve pod ops fast, 4 AI Transformation Forest SIN Agent AI-Assisted Escalations Shared Facts, 5 Velocity Value Efficiency deliberately lower Privacy Wave federated cost + sustainability no longer hours no bus factor 1 invest compounding say no) → DR metrics (10 Tier-1 metrics + secondary/counter) → NSMs (Stephanie NSM post 148075..., values Parental 37.3% IG US, Minimal 48% May19 goal 90% automatically 2027, Heavy median 11.1d, Missed 5.44%, self-evidenced 29.6%, SEV44, interruptions 1.224%, Cost $3.7B)
- Table P0-P5 with columns Priority/What it is/Topline/Secondary/Counter/Ship goals + NSM roll-up tags inline + Known metric gaps ‡ needs to be built † needs work + Other caveats audit calibration Q3, only Minimal LaMas goaled P4 rest tracking-only due audit calibration, cost undercounts federated, NSM4 large AI launches TBD + Appendix NSM definitions + Sources list including Roadmapping Overview doc 1pt6lj... + Verified Days WP 23390... + Flywheel readiness doc 1hvqh...

### Mapping problem

Flat tracker rows (118) vs hierarchical v3 goals (~12 H2 Goals grouped into 4 priorities). Human language goal in tracker often equals or approximates H2 Goal title in v3, but not 1:1:

Examples:
- Tracker Human goal "1.1: Maintain and strengthen existing critical positions..." ≈ v3 1A "Land Aligned Response Plans..."
- Tracker Human goal "1.2: Operate inbound risk-response and escalation processes within SLA across User Risk" appears with 3 metrics in tracker (>90% L1+ escalations T&C input ≥24h before review, All pending Reg Response triaged 5bd, % SINs under SLO) – but v3 1A second row shows "Develop inquiries tooling that spans whole response..." 95% in tooling etc – mismatch suggests v3 doc is older version or groups metrics differently than tracker.
- Data Risk slice tracker Human goals like "Keep SIN within SLO..." "Maintain controls, address SEVs, deliver MAPs" etc – these map to Baris P0-P5, which themselves map to Michel 1-4.

So we need an explicit mapping layer: tracker row → v3 Goal ID (1A,1B,1C,2A,2B,2C,2D,3-1,3-2,3-3,4A,4B,4C,4F,4G). This cannot be fully automated initially – requires manual curation, but can be stored natively.

## Proposed Native Format (Repo-Friendly)

Goal: git-tracked, markdown-centric, no auto-sync pipeline, on-demand ingest, supports both detailed tracking and summarized v3-style export.

### Option A: YAML Source of Truth (Recommended)

File: `projects/risk_goaling_h2_2026/scorecard.yaml`

Pros: Structured, easy to diff, supports all tracker fields + v3 grouping + NSM roll-up, Python-friendly for generation. Cons: Not markdown, but allowed as project-specific deep dive? Global convention says markdown only, but scripts CLAUDE.md allows generated source-of-truth lives elsewhere, script is formatter – YAML is common for source-of-truth (like miles). Could argue YAML is okay in docs/ or projects/.

Schema draft:

```yaml
metadata:
  last_updated: 2026-07-21
  version: v3.1
  sources:
    tracker_sheet: https://docs.google.com/spreadsheets/d/1MCTfdFwYLl6VDrVthczHEd1OIQhMp1yRdjA9wY7pGFA/edit?gid=1081314132
    tracker_export: /tmp/risk_sheet_retry.xlsx
    v3_doc: https://docs.google.com/document/d/1U9vrVFRO4A_jbi7QhhDbYdWv8n834gq3udR3M1KTjQQ/edit?tab=t.94anu86ip79a
    goal_map: https://docs.google.com/document/d/1p5m4E70gaSLc7fCmpZnpDp9GCbCYVPgn8eBNOiFhfDA
    north_star: https://docs.google.com/document/d/1iSxSzXVE4HI_bi__7r9bADtFNmC8gityFhzyXft2MhY
    roadmapping_overview: https://docs.google.com/document/d/1pt6ljd4slI6mqpdlkIo6zxl7H1xfKaIs7fKpxjqykEE
  priorities_order: [P1, P2, P3, P4]

priorities:
  - id: P1
    name: Meet our obligations
    topline_metric: NSM1 ship goals (% obligations covered by enforcement date – in development)
    nsm_ref: NSM1
    goals:
      - id: "1A"
        title: Land Aligned Response Plans and mature inbound response capabilities
        description: Land frontier/high-risk positions in priority launch regions (EU, Korea, Vietnam, CA), Ship EU AI Act Aug+Dec 2026, Youth 100% Response Plans Q3-Q1 deploy-ready H2, Data Risk mature positions 7 areas RD/Wearables/Cloud/Self-pref/Data In/Access/Anonymization
        risk_group_owner: All Areas Leads
        metric_owner: Zef RosnBrick / Allison Hartnett / Arash Nikkar
        discussion_q: [Goal 1C CI best practices Arash]
        metrics:
          - metric_name: Land aligned response plans before live date for every H2 regulatory obligation
            tracker_index: 3  # row in CSV
            human_language_goal: 1.1: Maintain and strengthen...
            investment_priority: 1. Meet our obligation response requirements
            risk_group: User Risk
            type: Ship Goal
            poc_analytics: TBD, Fernando interim
            goal_tracking: Goal
            definition: "[Accessibility] Maintain position on EAA..."
            definition_status: Pending
            target: 46 known obligations due H2'26
            tshirt: null
            operationalization_status: Pending
            m360_link: null
            added_to_scorecard: null
            nsm_rollup: NSM1
            data_risk_map: P2
          - ...
```

Simplify: store each metric as flat record with added fields v3_priority + v3_goal_id + data_risk_priority (P0-P5) + nsm_rollup.

Example flat per metric:

```yaml
metrics:
  - id: 7
    investment_priority: 1. Meet our obligation response requirements
    human_language_goal: Keep SIN within SLO so as to meet regulatory deadlines
    metric_name: % SINs under SLO
    risk_group: Data Risk
    type: Existing
    poc: Scott Murani
    goal_tracking: Goal
    definition: "% of SINs completed within SLO"
    definition_status: Pending
    target: null
    tshirt: null
    operationalization: Pending
    m360: Yes
    scorecard: Pending
    v3_mapping:
      priority: P1
      goal_id: 1B
      goal_title: Mature efficacy of meeting ongoing obligations
    data_risk_mapping:
      priority: P0
      name: Keep the Company Running
    nsm_mapping: null
```

Then generator can group.

### Option B: Markdown Table Source of Truth with YAML Frontmatter

File: `projects/risk_goaling_h2_2026/scorecard.md` with frontmatter --- yaml --- containing metadata, body contains markdown table for human readability and is itself source? Pros: markdown only, easy retrieval tomorrow morning. Cons: table with 22 columns unwieldy.

Better: Keep human-readable aggregated table in markdown body (matches v3 format), and structured YAML in frontmatter or in code fence ```yaml.

### Option C: CSV + Mapping CSV

- `scorecard_detailed.csv` – clone of tracker sheet 118 rows plus extra columns: v3_priority, v3_goal_id, data_risk_priority, nsm_rollup, comments.
- `mapping_goals.csv` – defines H2 Goals: goal_id, priority_id, title, description, risk_group_owner, metric_owner, topline_metric.

Pros: Simple, spreadsheet users comfortable, easy to export back to Google Sheets via meta google.sheets import. Cons: CSV not great for nested lists/milestones.

### Recommendation: Option A YAML flat metrics + separate goals definition YAML

Two files:
- `projects/risk_goaling_h2_2026/goals_definition.yaml` – defines priorities and H2 Goals (id, title, description, owners, topline)
- `projects/risk_goaling_h2_2026/metrics.yaml` – 118 metrics flat, each with v3 mapping and data risk mapping and NSM mapping

Combine into `scorecard.yaml` for simplicity initially.

Or single `scorecard.yaml` with both.

Plus generated files (marked GENERATED – do not hand-edit):
- `projects/risk_goaling_h2_2026/docs/scorecard_detailed.md` – detailed tracking format: markdown table close to tracker sheet but local, with all columns + v3 mapping, sorted by priority → goal → risk group.
- `projects/risk_goaling_h2_2026/docs/scorecard_summary.md` – summarized format matching v3 doc table: Priority header, H2 Goal, Goal Metrics (bulleted list pulled from metrics.yaml grouped), Metric Owner, Risk Group Owner.
- Optional exports: `scorecard_detailed.csv` for re-import to Sheets, and `scorecard_summary_ghtml.html` for applying to Google Doc via meta google.docs apply.

## Export Skills / Scripts

### Script: `scripts/generate_risk_scorecard.py`

Header:
```python
# Source: projects/risk_goaling_h2_2026/scorecard.yaml
# Generates:
# - projects/risk_goaling_h2_2026/docs/scorecard_detailed.md
# - projects/risk_goaling_h2_2026/docs/scorecard_summary.md
# - projects/risk_goaling_h2_2026/docs/scorecard_detailed.csv
# - projects/risk_goaling_h2_2026/docs/scorecard_summary_ghtml.html (ghtml for Google Docs)
# Usage:
#   python scripts/generate_risk_scorecard.py --refresh-sheet (optional, pulls latest sheet via meta google.sheets export)
#   python scripts/generate_risk_scorecard.py --format detailed
#   python scripts/generate_risk_scorecard.py --format summary
#   python scripts/generate_risk_scorecard.py --export-gdoc --doc-id <ID> --tab-id t.94anu86ip79a
# Venv: see memory/reference_python_venv.md or use python3 directly for pure yaml/csv (no pandas/openpyxl needed, use stdlib)
```

Functionality:
1. Load scorecard.yaml (pyyaml)
2. Optional --refresh-sheet: run `meta google.sheets export --url=... --export-as=xlsx --dest=/tmp/risk_sheet.xlsx`, parse xlsx/csv via stdlib csv + zipfile XML parsing (avoid pandas dependency) or use csv export we already have, merge into yaml preserving manual v3 mappings (keep existing mapping if tracker row already mapped, add new rows as unmapped with TODO).
3. Generate detailed markdown: table with columns Investment Priority | Human language goal | Metric Name | Risk Group | Type | POC | Goal/Tracking | Definition Status | Target | Operationalization | M360 | NSM | v3 Goal ID | Data Risk P | Comments – sorted by priority.
4. Generate summary markdown: group metrics by v3 priority → goal, produce table similar to v3 doc:
   - Header row H2 Goal (plain language) | Goal Metrics (bulleted list of metric names + definition + target) | Metric Owner | Risk Group Owner
   - Priority section headers with background color via markdown bold + italic for topline metric note (since ghtml supports row-level background via <tr style="background-color">)
5. Generate CSV for detailed tracking (for Sheets import)
6. Generate ghtml: build <html><head><title>...><body><table data-col-widths="..."> with same structure as v3 doc but populated from yaml – ready for `meta google.docs apply --from=file://... --base=file://...base`
7. Add header to each generated file: `<!-- GENERATED from ../projects/risk_goaling_h2_2026/scorecard.yaml — do not hand-edit — regen via python scripts/generate_risk_scorecard.py -->` or for html `<!-- GENERATED -->` inside.

### Custom Slash Commands / Skills (future)

Per root CLAUDE.md custom slash commands to build later:
- `/export-scorecard` – runs generate_risk_scorecard.py with both formats
- `/refresh-tracker` – pulls latest sheet, merges into scorecard.yaml, reports diff
- `/publish-goals-v3` – exports summary ghtml and applies to v3 doc as suggestion (meta google.docs apply --write-mode=suggest)

Implementation steps:
1. Build minimal version of script without Google Docs publish first – just generate markdowns.
2. Manually curate v3_mapping for Data Risk 10 rows (we already have P0-P5 + NSM mapping from goal map) as pilot, then extend to other risk groups by asking POCs or inferring from Human language goal prefixes (1.1,1.2 etc).
3. Validate summary output matches v3 doc structure side-by-side.
4. Add export-gdoc capability.

## Questions for Tony (to decide before implementation)

1. **Native format preference:** YAML flat metrics + goals definition (Option A) vs CSV + mapping CSV (Option C) vs hybrid markdown with YAML frontmatter (Option B)? My recommendation YAML because it preserves all 22 tracker columns + manual mappings + comments, easy diff, and scripts can generate both markdown tables.

2. **Source of truth:** Should `scorecard.yaml` be the sole source after initial import, or do you want to keep Google Sheet as source and have script always refresh from sheet (bidirectional sync vs sheet → yaml one-way with manual overrides preserved)? I recommend sheet → yaml one-way with manual v3_mapping preserved (script merges, doesn't overwrite manual fields).

3. **Scope:** Risk-wide scorecard (all 118 metrics, 4 priorities) or start with Data Risk slice only (10 metrics + P0-P5) as pilot for `areas/data_risk/`? Starting with Data Risk slice allows faster iteration and then expand to full Risk.

4. **Detailed format columns:** Should detailed tracking include all 22 tracker columns or subset (e.g., Investment Priority, Human goal, Metric Name, Risk Group, Type, POC, Goal/Tracking, Def Status, Target, T-Shirt, Operationalization, M360 Link, Scorecard?, v3 Goal ID, Data Risk P, NSM)?

5. **Summarized format fidelity:** Should summary exactly replicate v3 doc table structure (Priority header rows with rowspan, bullet lists in Goal Metrics column, owners) or simplified markdown table (one row per metric but grouped with priority/goal headers) for easier git diff? Exact replica requires ghtml generation with rowspan/colspan; simplified version is markdown-friendly but diverges from v3 doc visual.

6. **Export targets:** For summarized format, do you want ghtml output ready to apply to v3 doc (https://docs.google.com/document/d/1U9vrVFRO4A_jbi7QhhDbYdWv8n834gq3udR3M1KTjQQ) as tracked suggestions, or just local markdown for review first?

7. **Automation vs manual:** Should script handle fetching linked docs (roadmapping overview, flywheel etc) and updating overview.md, or keep scorecard generation isolated?

8. **Where to store:** `projects/risk_goaling_h2_2026/scorecard.yaml` vs `projects/risk_goaling_h2_2026/docs/scorecard.yaml` vs root `reference/`? Per projects CLAUDE.md, docs/ optional for deep dives – I suggest root of project folder for source, docs/ for generated.

## Proposed Next Steps (after you pick format)

- Step 1: Create `scorecard.yaml` skeleton from Tier-1 CSV (118 rows) with v3_mapping empty for most rows, but filled for Data Risk 10 rows using goal map P0-P5 + NSM tags (since we have that mapping)
- Step 2: Manually curate v3 goal definitions into `goals_definition.yaml` or inline in scorecard.yaml (12 goals: 1A 1B 1C 2A 2B 2C 2D 3-1 3-2 3-3 4A 4B 4C 4F 4G) from v3 doc
- Step 3: Build `scripts/generate_risk_scorecard.py` minimal version (no external deps) generating detailed md + summary md
- Step 4: Test generation and compare summary md side-by-side with v3 doc ghtml (use meta google.docs diff)
- Step 5: Add ghtml export and optional --export-gdoc suggest mode
- Step 6: Document in `projects/risk_goaling_h2_2026/overview.md` + `scripts/CLAUDE.md` regen command + add slash command stub

Let me know which option you prefer and I'll start building the skeleton.

