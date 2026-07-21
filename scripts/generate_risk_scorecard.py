#!/usr/bin/env python3
"""
Source: projects/risk_goaling_h2_2026/scorecard.yaml
Generates:
 - projects/risk_goaling_h2_2026/docs/scorecard_detailed.md  (detailed tracking: metric name, human goal, risk group, POC, goal/tracking, value over time, M360)
 - projects/risk_goaling_h2_2026/docs/scorecard_summary.md   (simplified markdown grouped by PRIORITY and H2 Goal ID, paired with goals v3 doc)
 - projects/risk_goaling_h2_2026/docs/scorecard_detailed.csv (for Sheets re-import)
 - projects/risk_goaling_h2_2026/docs/scorecard_summary_ghtml.html (ghtml ready for meta google.docs apply)

Usage:
  python scripts/generate_risk_scorecard.py
  python scripts/generate_risk_scorecard.py --refresh-sheet   # pulls latest Tier-1 sheet via meta CLI and merges into scorecard.yaml preserving manual mappings + values
  python scripts/generate_risk_scorecard.py --format detailed|summary|both   (default both)
  python scripts/generate_risk_scorecard.py --export-gdoc --doc-id 1U9vrVFRO4A_jbi7QhhDbYdWv8n834gq3udR3M1KTjQQ --tab-id t.94anu86ip79a

Venv: uses python3 stdlib only (no yaml/pandas/openpyxl) – parses our custom yaml via simple state machine.

Regen header: each generated file gets <!-- GENERATED from ../scorecard.yaml - do not hand-edit — regen via python scripts/generate_risk_scorecard.py -->
"""

import argparse
import csv
import io
import os
import re
import sys
from collections import defaultdict, OrderedDict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
SCORECARD_YAML = ROOT / "projects" / "risk_goaling_h2_2026" / "scorecard.yaml"
DOCS_OUT = ROOT / "projects" / "risk_goaling_h2_2026" / "docs"
SHEET_URL = "https://docs.google.com/spreadsheets/d/1MCTfdFwYLl6VDrVthczHEd1OIQhMp1yRdjA9wY7pGFA/edit"
SHEET_CSV_TMP = Path("/tmp/risk_sheet_export.csv")
SHEET_XLSX_TMP = Path("/tmp/risk_sheet_retry.xlsx")

def parse_yaml_simple(yaml_path):
    """
    Very small parser for our scorecard.yaml format.
    Returns (metadata dict, goals_definition list, metrics list)
    Does not need pyyaml – works on our known indentation.
    """
    metadata = {}
    goals_def_priorities = []  # list of dicts with id,name,topline,goals
    metrics = []
    current_metric = None
    current_v3 = None
    current_dr = None
    current_values = None
    in_metadata = False
    in_goals_def = False
    in_priorities = False
    in_goals = False
    current_priority = None
    current_goal = None
    # For values nested
    in_values = False
    current_value_entry = None

    with open(yaml_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # State tracking via indent
    # We will do simple line-by-line
    for raw in lines:
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        stripped = line.lstrip()
        indent = len(line) - len(stripped)

        # metadata
        if line.startswith('metadata:'):
            in_metadata = True
            in_goals_def = False
            continue
        if in_metadata:
            if indent == 2 and ':' in stripped:
                # key: value
                k,v = stripped.split(':',1)
                metadata[k.strip()] = v.strip()
                continue
            if indent == 2 and stripped.startswith('sources:'):
                continue
            if indent == 4 and ':' in stripped:
                # sources subkeys
                k,v = stripped.split(':',1)
                # keep nested under sources maybe
                continue
            if indent == 0 and not stripped.startswith(' '):
                in_metadata = False

        if line.startswith('goals_definition:'):
            in_goals_def = True
            in_metadata = False
            continue
        if in_goals_def:
            # priorities:
            if indent == 2 and stripped.startswith('priorities:'):
                in_priorities = True
                continue
            if in_priorities:
                if indent == 4 and stripped.startswith('- id:'):
                    # new priority
                    pid = stripped.split(':',1)[1].strip()
                    current_priority = {'id': pid, 'goals': []}
                    goals_def_priorities.append(current_priority)
                    continue
                if indent == 6 and ':' in stripped and current_priority is not None:
                    # priority fields: name, topline, nsm
                    if stripped.startswith('name:'):
                        current_priority['name'] = stripped.split(':',1)[1].strip()
                    elif stripped.startswith('topline:'):
                        current_priority['topline'] = stripped.split(':',1)[1].strip()
                    elif stripped.startswith('nsm:'):
                        current_priority['nsm'] = stripped.split(':',1)[1].strip()
                    elif stripped.startswith('goals:'):
                        in_goals = True
                        continue
                if in_goals and current_priority:
                    if indent == 8 and stripped.startswith('- id:'):
                        gid = stripped.split(':',1)[1].strip()
                        current_goal = {'id': gid}
                        current_priority['goals'].append(current_goal)
                        continue
                    if indent == 10 and ':' in stripped and current_goal is not None:
                        if stripped.startswith('title:'):
                            current_goal['title'] = stripped.split(':',1)[1].strip()
                        elif stripped.startswith('description:'):
                            current_goal['description'] = stripped.split(':',1)[1].strip()
                        elif stripped.startswith('risk_group_owner:'):
                            current_goal['risk_group_owner'] = stripped.split(':',1)[1].strip()
                        elif stripped.startswith('metric_owner:'):
                            current_goal['metric_owner'] = stripped.split(':',1)[1].strip()
                # exit conditions
            if indent == 0 and stripped.startswith('metrics:'):
                in_goals_def = False
                in_priorities = False
                in_goals = False
                # fall through to metrics parsing

        if line.startswith('metrics:'):
            # start metrics list
            # we will now parse metrics
            # reset vars
            current_metric = None
            in_values = False
            continue

        # metrics parsing – each metric starts with "  - id:"
        if stripped.startswith('- id:') and indent == 2:
            # new metric
            if current_metric:
                # push previous
                if current_v3:
                    current_metric['v3_mapping'] = current_v3
                if current_dr:
                    current_metric['data_risk_mapping'] = current_dr
                if current_values:
                    current_metric['values'] = current_values
                metrics.append(current_metric)
            mid = stripped.split(':',1)[1].strip()
            current_metric = {'id': mid, 'values': []}
            current_v3 = {}
            current_dr = {}
            current_values = []
            current_value_entry = None
            in_values = False
            continue

        if current_metric is None:
            continue

        # Inside a metric
        if indent == 4:
            if stripped.startswith('metric_name:'):
                # value is quoted
                v = stripped.split(':',1)[1].strip()
                # strip surrounding quotes if present
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                current_metric['metric_name'] = v
            elif stripped.startswith('human_goal:'):
                v = stripped.split(':',1)[1].strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                current_metric['human_goal'] = v
            elif stripped.startswith('investment_priority:'):
                v = stripped.split(':',1)[1].strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                current_metric['investment_priority'] = v
            elif stripped.startswith('risk_group:'):
                v = stripped.split(':',1)[1].strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                current_metric['risk_group'] = v
            elif stripped.startswith('type:'):
                v = stripped.split(':',1)[1].strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                current_metric['type'] = v
            elif stripped.startswith('poc_analytics:'):
                v = stripped.split(':',1)[1].strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                current_metric['poc_analytics'] = v
            elif stripped.startswith('goal_tracking:'):
                v = stripped.split(':',1)[1].strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                current_metric['goal_tracking'] = v
            elif stripped.startswith('definition:'):
                v = stripped.split(':',1)[1].strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                current_metric['definition'] = v
            elif stripped.startswith('definition_status:'):
                v = stripped.split(':',1)[1].strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                current_metric['definition_status'] = v
            elif stripped.startswith('target:'):
                v = stripped.split(':',1)[1].strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                current_metric['target'] = v
            elif stripped.startswith('tshirt_lift:'):
                v = stripped.split(':',1)[1].strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                current_metric['tshirt_lift'] = v
            elif stripped.startswith('operationalization_status:'):
                v = stripped.split(':',1)[1].strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                current_metric['operationalization_status'] = v
            elif stripped.startswith('m360_link:'):
                v = stripped.split(':',1)[1].strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                current_metric['m360_link'] = v
            elif stripped.startswith('added_to_scorecard:'):
                v = stripped.split(':',1)[1].strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                current_metric['added_to_scorecard'] = v
            elif stripped.startswith('v3_mapping:'):
                current_v3 = {}
                in_values = False
            elif stripped.startswith('data_risk_mapping:'):
                current_dr = {}
                in_values = False
            elif stripped.startswith('nsm_rollup:'):
                v = stripped.split(':',1)[1].strip()
                current_metric['nsm_rollup'] = v
            elif stripped.startswith('values:'):
                in_values = True
                current_values = []
                current_value_entry = None

        if indent == 6 and not in_values:
            # inside v3_mapping or data_risk_mapping
            if current_v3 is not None and 'priority_id' not in current_v3 or 'goal_id' in stripped or 'priority' in stripped:
                # we are inside v3_mapping if we recently saw v3_mapping
                # Heuristic: check current context by last seen mapping header
                # We have current_v3 and current_dr both, but we need to know which we are in.
                # We will track by seeing if previous line was v3_mapping and we haven't entered data_risk_mapping after
                pass
            # Actually we need better tracking – we will just parse both dicts by key names
            if ':' in stripped:
                k,v = stripped.split(':',1)
                k=k.strip()
                v=v.strip()
                if v.startswith('"') and v.endswith('"'):
                    v=v[1:-1]
                # Try to assign to v3 or dr based on current_metric context
                # If k is priority_id, priority_name, goal_id, goal_title – could be either mapping
                # We'll check if current_dr is expected empty or if we are in dr block – we can use a simple flag: last mapping header
                # Instead, we will just assign to both and later deduplicate – simpler: if we are after data_risk_mapping header most recently, assign to dr, else to v3
                # For this simple parser, we will use a separate state: we track last_mapping = 'v3' or 'dr' when we see those headers
                # Implement via variable last_mapping_header
                pass

        # Detailed sub-parsing for v3_mapping and data_risk_mapping with state
        # We'll need to track last mapping header encountered
        # This is getting messy – we will instead use a second pass with regex on the file for simplicity for values.

    # Push last metric
    if current_metric:
        if current_v3:
            current_metric['v3_mapping'] = current_v3
        if current_dr:
            current_metric['data_risk_mapping'] = current_dr
        if current_values:
            current_metric['values'] = current_values
        metrics.append(current_metric)

    # Now we have metrics but v3_mapping and data_risk_mapping and values may be incomplete due to parser limits.
    # Let's do a second regex pass to fill those from raw yaml text – more reliable for our simple format.

    # Second pass: for each metric block via regex – isolate metrics section only to avoid counting goals_definition priorities
    raw_text_full = open(yaml_path, 'r', encoding='utf-8').read()
    # Find metrics: section
    m_section = re.search(r'\nmetrics:\s*\n(.*)', raw_text_full, flags=re.DOTALL)
    raw_text = m_section.group(1) if m_section else raw_text_full
    # Split metrics
    metric_blocks = re.split(r'\n\s*- id:', raw_text)
    # prepend dash for parser logic – first block after split loses the '- id:' marker, add it back via first line handling
    # Actually metric_blocks[0] is content before first metric (should be empty), rest are metric bodies starting with " <id>\n..."
    # Keep as is
    # first block is header, rest are metrics
    parsed_metrics = []
    for i, block in enumerate(metric_blocks[1:]):  # skip header
        # reconstruct id line
        # block starts with " metric_id\n    metric_name: ..."
        # We'll parse fields via regex
        def get_field(pattern, text, default=''):
            m = re.search(pattern, text, flags=re.MULTILINE)
            if m:
                val = m.group(1).strip()
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                return val
            return default

        m_id = get_field(r'^\s*([^\s]+)\s*\n', block, '')
        # Actually id is first token before newline
        # The block's first line is " <id>\n"
        # So extract first line
        first_line = block.split('\n',1)[0].strip()
        metric_id = first_line

        metric = {
            'id': metric_id,
            'metric_name': get_field(r'metric_name:\s*\"(.*?)\"', block, ''),
            'human_goal': get_field(r'human_goal:\s*\"(.*?)\"', block, ''),
            'investment_priority': get_field(r'investment_priority:\s*\"(.*?)\"', block, ''),
            'risk_group': get_field(r'risk_group:\s*\"(.*?)\"', block, ''),
            'type': get_field(r'type:\s*\"(.*?)\"', block, ''),
            'poc_analytics': get_field(r'poc_analytics:\s*\"(.*?)\"', block, ''),
            'goal_tracking': get_field(r'goal_tracking:\s*\"(.*?)\"', block, ''),
            'definition': get_field(r'definition:\s*\"(.*?)\"', block, ''),
            'definition_status': get_field(r'definition_status:\s*\"(.*?)\"', block, ''),
            'target': get_field(r'target:\s*\"(.*?)\"', block, ''),
            'tshirt_lift': get_field(r'tshirt_lift:\s*\"(.*?)\"', block, ''),
            'operationalization_status': get_field(r'operationalization_status:\s*\"(.*?)\"', block, ''),
            'm360_link': get_field(r'm360_link:\s*\"(.*?)\"', block, ''),
            'added_to_scorecard': get_field(r'added_to_scorecard:\s*\"(.*?)\"', block, ''),
            'nsm_rollup': get_field(r'nsm_rollup:\s*(\S+)', block, ''),
        }
        # v3 mapping
        v3_block = re.search(r'v3_mapping:\s*\n(.*?)\n\s*(data_risk_mapping:|nsm_rollup:|values:)', block, flags=re.DOTALL)
        if v3_block:
            v3_text = v3_block.group(1)
            v3 = {}
            for k in ['priority_id','priority_name','goal_id','goal_title']:
                mv = re.search(rf'{k}:\s*\"?(.*?)\"?\s*$', v3_text, flags=re.MULTILINE)
                if mv:
                    v3[k] = mv.group(1).strip().strip('"')
            metric['v3_mapping'] = v3
        else:
            metric['v3_mapping'] = {}

        dr_block = re.search(r'data_risk_mapping:\s*\n(.*?)\n\s*(nsm_rollup:|values:)', block, flags=re.DOTALL)
        if dr_block:
            dr_text = dr_block.group(1)
            dr = {}
            for k in ['priority_id','priority_name','nsm']:
                mv = re.search(rf'{k}:\s*\"?(.*?)\"?\s*$', dr_text, flags=re.MULTILINE)
                if mv:
                    dr[k] = mv.group(1).strip().strip('"')
            metric['data_risk_mapping'] = dr
        else:
            metric['data_risk_mapping'] = {}

        # values – parse all date entries
        values = []
        # find values block
        vals_match = re.search(r'values:\s*\n(.*)', block, flags=re.DOTALL)
        if vals_match:
            vals_text = vals_match.group(1)
            # each entry starts with "      - date:"
            entries = re.split(r'\n\s*- date:', vals_text)
            # first split part before first date is empty
            for entry in entries[1:]:
                # entry contains ' "2026-07-21"\n        value: null\n...'
                # prepend the date marker we split on
                entry_full = '- date:' + entry
                d_match = re.search(r'date:\s*\"?(.*?)\"?\s*\n', entry_full)
                v_match = re.search(r'value:\s*\"?(.*?)\"?\s*\n', entry_full)
                s_match = re.search(r'status:\s*\"?(.*?)\"?\s*\n', entry_full)
                src_match = re.search(r'source:\s*\"?(.*?)\"?\s*\n', entry_full)
                comm_match = re.search(r'comment:\s*\"?(.*?)\"?\s*\n', entry_full)
                ve = {}
                if d_match:
                    ve['date'] = d_match.group(1).strip().strip('"')
                if v_match:
                    val = v_match.group(1).strip().strip('"')
                    if val == 'null' or val == '':
                        ve['value'] = None
                    else:
                        ve['value'] = val
                if s_match:
                    ve['status'] = s_match.group(1).strip().strip('"')
                if src_match:
                    ve['source'] = src_match.group(1).strip().strip('"')
                if comm_match:
                    ve['comment'] = comm_match.group(1).strip().strip('"')
                values.append(ve)
        metric['values'] = values
        parsed_metrics.append(metric)

    # Use parsed_metrics as final (more accurate)
    metrics = parsed_metrics

    # Parse goals_definition via regex too for simplicity
    # Extract priorities
    # Find goals_definition block
    goals_def_text_match = re.search(r'goals_definition:\s*\n(.*)\nmetrics:', raw_text, flags=re.DOTALL)
    if goals_def_text_match:
        gd_text = goals_def_text_match.group(1)
        # Re-parse priorities via split
        pri_blocks = re.split(r'\n\s*- id:\s*P', gd_text)
        # Actually first pri id includes P1 etc
        # Let's just reuse earlier simple parse for priorities (approx)
        # For now keep goals_def_priorities as earlier parsed (approx)
        pass

    return metadata, goals_def_priorities, metrics


def latest_value(metric):
    vals = metric.get('values', [])
    if not vals:
        return None
    # assume sorted by date ascending, latest last
    # Try to parse date sort
    def sort_key(v):
        return v.get('date','')
    vals_sorted = sorted(vals, key=sort_key)
    return vals_sorted[-1] if vals_sorted else None


def generate_detailed_md(metrics, out_path):
    header = f"<!-- GENERATED from ../scorecard.yaml — do not hand-edit — regen via python {Path(__file__).name} -->\n"
    header += f"# Risk H2 2026 Scorecard — Detailed Tracking\n\n_Last updated: {date.today().isoformat()}_\n_Source: scorecard.yaml ({len(metrics)} metrics)_\n\n"
    header += "Minimal fields per request: metric name, human goal, risk group, POC, goal/tracking, value at specific dates + M360 links (to be populated).\n\n"
    header += "| Metric Name | Human Goal | Risk Group | POC | Goal/Tracking | Latest Value | Target | M360 Link | v3 Goal ID | Data Risk P | NSM | Def Status |\n"
    header += "|-------------|------------|------------|-----|---------------|--------------|--------|-----------|------------|-------------|-----|------------|\n"

    rows = []
    # Filter out blank metric names (5 placeholder rows in sheet)
    filtered_metrics = [mm for mm in metrics if mm.get('metric_name','').strip()]
    for m in sorted(filtered_metrics, key=lambda x: (x.get('v3_mapping',{}).get('priority_id','Z'), x.get('v3_mapping',{}).get('goal_id','Z'), x.get('risk_group',''), x.get('metric_name',''))):
        metric_name = m.get('metric_name','').replace('|','/').replace('\n',' ')
        human_goal = m.get('human_goal','').replace('|','/').replace('\n',' ')[:120]
        risk_group = m.get('risk_group','')
        poc = m.get('poc_analytics','')
        goal_tracking = m.get('goal_tracking','')
        lv = latest_value(m)
        latest_val = ''
        if lv:
            if lv.get('value') is None:
                latest_val = f"{lv.get('status','') or 'TBD'} ({lv.get('date','')})"
            else:
                latest_val = f"{lv.get('value')} ({lv.get('date','')})"
        target = m.get('target','').replace('|','/')[:80]
        m360 = m.get('m360_link','')
        if m360:
            m360_md = f"[link]({m360})"
        else:
            m360_md = "TBD"
        v3_gid = m.get('v3_mapping',{}).get('goal_id','TODO')
        dr_p = m.get('data_risk_mapping',{}).get('priority_id','') or ''
        nsm = m.get('nsm_rollup','') or m.get('data_risk_mapping',{}).get('nsm','') or ''
        def_status = m.get('definition_status','')
        rows.append(f"| {metric_name[:80]} | {human_goal[:100]} | {risk_group} | {poc} | {goal_tracking} | {latest_val} | {target} | {m360_md} | {v3_gid} | {dr_p} | {nsm} | {def_status} |")

    content = header + "\n".join(rows) + "\n\n## Value History Detail\n\nEach metric's value over time is stored in `scorecard.yaml` under `values:` list with date, value, status, source, comment. Example:\n\n```yaml\nvalues:\n  - date: \"2026-07-21\"\n    value: null\n    status: Pending\n    source: tracker_sheet_import\n  - date: \"2026-08-01\"\n    value: \"48%\"\n    source: m360 pull https://...\n```\n\nAdd new dated entries over time; generator will pick latest for table above. Over time provide M360 links and we will add pull logic (Presto/M360 API).\n"
    Path(out_path).write_text(content, encoding='utf-8')
    print(f"Wrote detailed md to {out_path} ({len(rows)} rows)")

def generate_summary_md(metrics, goals_def_priorities, out_path):
    # Filter blank metric names for summary view
    metrics = [mm for mm in metrics if mm.get('metric_name','').strip()]
    header = f"<!-- GENERATED from ../scorecard.yaml — do not hand-edit — regen via python {Path(__file__).name} -->\n"
    header += f"# Risk H2 2026 Scorecard — Summary (paired with Goals v3 Doc)\n\n_Last updated: {date.today().isoformat()}_\n_Source: scorecard.yaml grouped by v3 Priority/Goal – {len(metrics)} metrics_\n\n"
    header += "This simplified markdown is designed to pair with the Goals v3 doc (https://docs.google.com/document/d/1U9vrVFRO4A_jbi7QhhDbYdWv8n834gq3udR3M1KTjQQ) which holds static descriptions. This file holds live values + POCs + Risk Groups + M360 links.\n\n"
    header += "## How to use with v3 doc\n\n- v3 doc = authoritative descriptions which won't change (H2 Goal plain language, Goal Metrics description).\n- This scorecard = live values, owners, status, M360 links, aggregated counts.\n- For regular updates: refresh values in scorecard.yaml (add dated entries), re-run generator, then copy summary table into v3 doc or use as companion for leadership review.\n\n"

    # Group metrics by priority and goal
    grouped = defaultdict(lambda: defaultdict(list))  # priority_id -> goal_id -> metrics
    priority_names = {}
    goal_titles = {}
    # Build mapping from goals_def_priorities for titles
    for p in goals_def_priorities:
        pid = p.get('id','')
        priority_names[pid] = p.get('name','')
        for g in p.get('goals',[]):
            gid = g.get('id','')
            goal_titles[(pid,gid)] = g.get('title','')

    # Also fallback from metrics own v3_mapping
    for m in metrics:
        v3 = m.get('v3_mapping',{})
        pid = v3.get('priority_id','TODO')
        gid = v3.get('goal_id','TODO')
        # priority name fallback
        if pid not in priority_names:
            priority_names[pid] = v3.get('priority_name','') or ''
        # goal title fallback
        key = (pid,gid)
        if key not in goal_titles or not goal_titles[key]:
            goal_titles[key] = v3.get('goal_title','') or m.get('human_goal','')[:80]
        grouped[pid][gid].append(m)

    # Order priorities P1-P4 then TODO
    ordered_pids = ['P1','P2','P3','P4','TODO','P0']  # P0 is actually Data Risk P0 but appears in v3 as P1 etc – keep P1-P4 first
    # add any others not in ordered list
    all_pids = list(grouped.keys())
    for pid in all_pids:
        if pid not in ordered_pids:
            ordered_pids.append(pid)
    # Remove duplicates preserving order
    seen=[]
    for pid in ordered_pids:
        if pid in grouped and pid not in seen:
            seen.append(pid)
    for pid in all_pids:
        if pid not in seen:
            seen.append(pid)
    ordered_pids = seen

    content_parts = [header]

    for pid in ordered_pids:
        if pid not in grouped:
            continue
        pname = priority_names.get(pid,'')
        # Find topline from goals_def
        topline = ''
        for p in goals_def_priorities:
            if p.get('id')==pid:
                topline = p.get('topline','')
                break
        content_parts.append(f"## PRIORITY {pid} – {pname}\n")
        if topline:
            content_parts.append(f"_Topline: {topline}_\n")
        content_parts.append("\n")

        # Goals under this priority
        goals_dict = grouped[pid]
        # order goal ids: 1A 1B 1C 2A etc
        ordered_gids = sorted(goals_dict.keys(), key=lambda x: (str(x)))
        # put TODO last
        if 'TODO' in ordered_gids:
            ordered_gids = [g for g in ordered_gids if g!='TODO'] + ['TODO']

        for gid in ordered_gids:
            g_metrics = goals_dict[gid]
            g_title = goal_titles.get((pid,gid), '') or g_metrics[0].get('human_goal','')[:100]
            # For TODO group, title from human_goal
            if gid=='TODO':
                g_title = f"Unmapped – {len(g_metrics)} metrics need v3 Goal ID curation"

            content_parts.append(f"### {gid} – {g_title}\n\n")
            # Table for metrics under this goal – simplified per request: metric name, human goal, risk group, POC, goal/tracking, value at dates, M360
            content_parts.append("| Metric Name | Human Goal | Risk Group | POC | Goal/Tracking | Latest Value | Target | M360 | Def Status |\n")
            content_parts.append("|-------------|------------|------------|-----|---------------|--------------|--------|------|------------|\n")
            for m in sorted(g_metrics, key=lambda x: x.get('risk_group','')+x.get('metric_name','')):
                metric_name = m.get('metric_name','').replace('|','/')[:80]
                human_goal = m.get('human_goal','').replace('|','/')[:80]
                risk_group = m.get('risk_group','')
                poc = m.get('poc_analytics','')
                goal_tracking = m.get('goal_tracking','')
                lv = latest_value(m)
                latest_val = ''
                if lv:
                    if lv.get('value') is None:
                        latest_val = f"{lv.get('status','') or 'TBD'} ({lv.get('date','')})"
                    else:
                        latest_val = f"{lv.get('value')} ({lv.get('date','')})"
                target = m.get('target','').replace('|','/')[:60]
                m360 = m.get('m360_link','')
                m360_md = f"[link]({m360})" if m360 else "TBD"
                def_status = m.get('definition_status','')
                content_parts.append(f"| {metric_name} | {human_goal} | {risk_group} | {poc} | {goal_tracking} | {latest_val} | {target} | {m360_md} | {def_status} |\n")
            content_parts.append("\n")

            # Value history timeline for this goal (optional detail)
            # List values over time per metric?
            # Keep brief
            content_parts.append(f"**Count:** {len(g_metrics)} metrics | **Risk Groups:** {', '.join(sorted(set([mm.get('risk_group','') for mm in g_metrics if mm.get('risk_group')])))} \n\n")
            content_parts.append("---\n\n")

    # Add section for Data Risk P0-P5 view as secondary
    content_parts.append("## Appendix – Data Risk P0-P5 View (from goal map)\n\n")
    dr_grouped = defaultdict(list)
    for m in metrics:
        dr = m.get('data_risk_mapping',{})
        pid = dr.get('priority_id','')
        if pid:
            dr_grouped[pid].append(m)
    ordered_dr = ['P0','P1','P2','P3','P4','P5','TODO']
    for dr_pid in ordered_dr:
        if dr_pid not in dr_grouped:
            continue
        content_parts.append(f"### {dr_pid} – {dr_grouped[dr_pid][0].get('data_risk_mapping',{}).get('priority_name','') or ''} ({len(dr_grouped[dr_pid])} metrics)\n\n")
        content_parts.append("| Metric | Risk Group | POC | Goal/Tracking | Latest Value | NSM |\n")
        content_parts.append("|--------|------------|-----|---------------|--------------|-----|\n")
        for m in dr_grouped[dr_pid]:
            content_parts.append(f"| {m.get('metric_name','')[:60]} | {m.get('risk_group','')} | {m.get('poc_analytics','')} | {m.get('goal_tracking','')} | { (latest_value(m) or {}).get('value') or (latest_value(m) or {}).get('status') or 'TBD'} | {m.get('nsm_rollup','') or m.get('data_risk_mapping',{}).get('nsm','') or ''} |\n")
        content_parts.append("\n")

    Path(out_path).write_text("".join(content_parts), encoding='utf-8')
    print(f"Wrote summary md to {out_path}")

def generate_csv(metrics, out_path):
    metrics = [mm for mm in metrics if mm.get('metric_name','').strip()]
    header = ['id','metric_name','human_goal','investment_priority','risk_group','type','poc_analytics','goal_tracking','definition','definition_status','target','tshirt_lift','operationalization_status','m360_link','added_to_scorecard','v3_priority_id','v3_goal_id','v3_goal_title','data_risk_priority_id','data_risk_priority_name','nsm_rollup','latest_date','latest_value','latest_status','latest_source']
    with open(out_path,'w',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for m in metrics:
            v3 = m.get('v3_mapping',{})
            dr = m.get('data_risk_mapping',{})
            lv = latest_value(m) or {}
            row = [
                m.get('id',''),
                m.get('metric_name',''),
                m.get('human_goal',''),
                m.get('investment_priority',''),
                m.get('risk_group',''),
                m.get('type',''),
                m.get('poc_analytics',''),
                m.get('goal_tracking',''),
                m.get('definition',''),
                m.get('definition_status',''),
                m.get('target',''),
                m.get('tshirt_lift',''),
                m.get('operationalization_status',''),
                m.get('m360_link',''),
                m.get('added_to_scorecard',''),
                v3.get('priority_id',''),
                v3.get('goal_id',''),
                v3.get('goal_title',''),
                dr.get('priority_id',''),
                dr.get('priority_name',''),
                m.get('nsm_rollup','') or dr.get('nsm',''),
                lv.get('date',''),
                lv.get('value','') if lv.get('value') is not None else '',
                lv.get('status',''),
                lv.get('source',''),
            ]
            writer.writerow(row)
    print(f"Wrote csv to {out_path}")

def generate_ghtml(metrics, goals_def_priorities, out_path):
    metrics = [mm for mm in metrics if mm.get('metric_name','').strip()]
    # Build simple ghtml table matching v3 doc style: Priorities grouped, with row background colors
    # For simplified version: one table with headers H2 Goal | Goal Metrics (with latest value) | Metric Owner | Risk Group Owner
    # Use <table data-col-widths="225,420,111,139">
    html = []
    html.append('<!-- GENERATED from scorecard.yaml — do not hand-edit — regen via python scripts/generate_risk_scorecard.py -->')
    html.append('<html><head><title>Risk H2 2026 Scorecard — Summary GHTML</title></head><body>')
    html.append('<h1>Risk H2 2026 Scorecard — Summary (GHTML for Google Docs)</h1>')
    html.append(f'<p>Last updated: {date.today().isoformat()} — {len(metrics)} metrics — Source: scorecard.yaml</p>')
    html.append('<table data-col-widths="225.75,420,111,139.5" data-pinned-header-rows="1">')
    html.append('<tr style="background-color: #B4A7D6"><th><p><b>H2 Goal</b></p><p><span style="font-size: 9pt">What success looks like by EOY in plain language</span></p></th><th><p><b>Goal Metrics (with latest value)</b></p><p><span style="font-size: 9pt">Team-level metrics or milestones that track progress</span></p></th><th><p><b>Metric Owner</b></p></th><th><p><b>Risk Group Owner</b></p></th></tr>')

    grouped = defaultdict(lambda: defaultdict(list))
    priority_names = {}
    goal_titles = {}
    goal_descs = {}
    goal_risk_owners = {}
    goal_metric_owners = {}
    for p in goals_def_priorities:
        pid = p.get('id','')
        priority_names[pid]=p.get('name','')
        for g in p.get('goals',[]):
            gid = g.get('id','')
            goal_titles[(pid,gid)]=g.get('title','')
            goal_descs[(pid,gid)]=g.get('description','')
            goal_risk_owners[(pid,gid)]=g.get('risk_group_owner','')
            goal_metric_owners[(pid,gid)]=g.get('metric_owner','')

    for m in metrics:
        v3 = m.get('v3_mapping',{})
        pid = v3.get('priority_id','TODO')
        gid = v3.get('goal_id','TODO')
        grouped[pid][gid].append(m)
        if pid not in priority_names:
            priority_names[pid]=v3.get('priority_name','')
        if (pid,gid) not in goal_titles:
            goal_titles[(pid,gid)]=v3.get('goal_title','') or m.get('human_goal','')

    ordered_pids = ['P1','P2','P3','P4']
    for pid in list(grouped.keys()):
        if pid not in ordered_pids:
            ordered_pids.append(pid)
    for pid in ordered_pids:
        if pid not in grouped:
            continue
        # priority header row
        pname = priority_names.get(pid,'')
        html.append(f'<tr style="background-color: #D9D2E9"><td colspan="4"><b>PRIORITY {pid}: {pname}</b></td></tr>')
        goals_dict = grouped[pid]
        for gid in sorted(goals_dict.keys()):
            g_metrics = goals_dict[gid]
            g_title = goal_titles.get((pid,gid),'') or g_metrics[0].get('human_goal','')[:80]
            # Build Goal Metrics cell with bullet list + latest values
            metrics_html = []
            for m in g_metrics:
                lv = latest_value(m)
                val_str = ''
                if lv:
                    if lv.get('value'):
                        val_str = f" – <b>Current: {lv.get('value')} ({lv.get('date')})</b>"
                    else:
                        val_str = f" – Current: {lv.get('status','TBD')} ({lv.get('date','')})"
                metrics_html.append(f"<li>{m.get('metric_name','')} [{m.get('risk_group','')} – {m.get('poc_analytics','')} – {m.get('goal_tracking','')}]{val_str} – Target: {m.get('target','')}</li>")
            metrics_cell = "<ul>" + "".join(metrics_html) + "</ul>"
            risk_owner = goal_risk_owners.get((pid,gid),'') or ', '.join(sorted(set([x.get('risk_group','') for x in g_metrics if x.get('risk_group')])))
            metric_owner = goal_metric_owners.get((pid,gid),'') or ', '.join(sorted(set([x.get('poc_analytics','') for x in g_metrics if x.get('poc_analytics')])))[:120]
            html.append(f'<tr><td>{gid}. <b>{g_title}</b><p>{goal_descs.get((pid,gid),"")[:200]}</p></td><td>{metrics_cell}</td><td>{metric_owner}</td><td>{risk_owner}</td></tr>')

    html.append('</table></body></html>')
    Path(out_path).write_text("\n".join(html), encoding='utf-8')
    print(f"Wrote ghtml to {out_path}")

def refresh_from_sheet(yaml_path):
    """
    Refresh scorecard.yaml from latest sheet export.
    Preserves manual v3_mapping, data_risk_mapping, values, m360_link.
    """
    print("Refreshing from sheet – running meta google.sheets export...")
    os.system(f'meta google.sheets export --url="{SHEET_URL}" --export-as=csv --dest=/tmp/risk_sheet_export_latest.csv')
    csv_path = Path('/tmp/risk_sheet_export_latest.csv')
    if not csv_path.exists():
        print("Failed to export sheet – using existing /tmp/risk_sheet_export.csv")
        csv_path = SHEET_CSV_TMP
    if not csv_path.exists():
        print("No CSV found – aborting refresh")
        return

    # Parse new CSV
    with open(csv_path,'r',encoding='utf-8') as f:
        reader = list(csv.reader(io.StringIO(f.read())))
    if len(reader) < 3:
        print("CSV too short")
        return
    header = reader[1]
    new_data = reader[2:]
    print(f"New data rows: {len(new_data)}")

    # Load existing yaml to preserve mappings
    _, _, existing_metrics = parse_yaml_simple(yaml_path)
    existing_by_name = {m['metric_name']: m for m in existing_metrics}

    # Build new metrics list merging
    merged = []
    for idx, r in enumerate(new_data):
        if len(r) < 22:
            r = r + [''] * (22 - len(r))
        metric_name = r[2].strip()
        if not metric_name:
            continue
        existing = existing_by_name.get(metric_name)
        if existing:
            # preserve manual fields
            # update definition_status, target etc from new sheet? We will update those fields but keep v3_mapping, data_risk_mapping, values, m360_link if manual
            merged_metric = existing.copy()
            # update fields from sheet that are not manual mappings
            merged_metric['human_goal'] = r[1].strip()[:250]
            merged_metric['investment_priority'] = r[0].strip()[:120]
            merged_metric['risk_group'] = r[3].strip()
            merged_metric['type'] = r[4].strip()
            merged_metric['poc_analytics'] = r[5].strip()[:60]
            merged_metric['goal_tracking'] = r[6].strip()
            merged_metric['definition'] = r[7].strip()[:200]
            merged_metric['definition_status'] = r[8].strip()
            merged_metric['target'] = r[11].strip()[:150]
            merged_metric['tshirt_lift'] = r[12].strip()
            merged_metric['operationalization_status'] = r[14].strip()
            # m360_link preserve if existing has non-empty, else take from sheet
            if not merged_metric.get('m360_link'):
                merged_metric['m360_link'] = r[19].strip()[:200]
            merged_metric['added_to_scorecard'] = r[20].strip()
            merged.append(merged_metric)
        else:
            # new metric – create minimal
            slug = re.sub(r'[^a-zA-Z0-9]+','_', metric_name.lower())[:60].strip('_') or f'metric_{idx}'
            new_metric = {
                'id': f'{slug}_{idx}',
                'metric_name': metric_name[:180],
                'human_goal': r[1].strip()[:250],
                'investment_priority': r[0].strip()[:120],
                'risk_group': r[3].strip(),
                'type': r[4].strip(),
                'poc_analytics': r[5].strip()[:60],
                'goal_tracking': r[6].strip(),
                'definition': r[7].strip()[:200],
                'definition_status': r[8].strip(),
                'target': r[11].strip()[:150],
                'tshirt_lift': r[12].strip(),
                'operationalization_status': r[14].strip(),
                'm360_link': r[19].strip()[:200],
                'added_to_scorecard': r[20].strip(),
                'v3_mapping': {'priority_id': 'TODO', 'goal_id': 'TODO', 'goal_title': 'TODO – curate'},
                'data_risk_mapping': {},
                'nsm_rollup': '',
                'values': [{'date': date.today().isoformat(), 'value': None, 'status': r[8].strip() or 'Pending', 'source': 'tracker_sheet_refresh', 'comment': 'New metric from latest sheet'}]
            }
            merged.append(new_metric)

    # Report diff
    existing_names = set(existing_by_name.keys())
    new_names = set([m['metric_name'] for m in merged])
    added = new_names - existing_names
    removed = existing_names - new_names
    print(f"Added metrics: {len(added)}")
    for a in list(added)[:10]:
        print(f"  + {a}")
    print(f"Removed metrics: {len(removed)}")
    for r_ in list(removed)[:10]:
        print(f"  - {r_}")

    # Rewrite yaml – reuse generation logic from earlier script but with merged data
    # For simplicity, re-generate yaml file using same manual formatting as initial script
    # We'll keep goals_definition unchanged from existing yaml file – read raw file and keep that section
    raw = open(yaml_path,'r',encoding='utf-8').read()
    goals_def_match = re.search(r'(goals_definition:.*?\n)metrics:', raw, flags=re.DOTALL)
    goals_def_text = goals_def_match.group(1) if goals_def_match else ''

    out_path = yaml_path
    with open(out_path,'w',encoding='utf-8') as out:
        out.write('# Risk H2 2026 Goal Scorecard — Native YAML Source of Truth\n')
        out.write(f'# Last updated: {date.today().isoformat()} — refreshed from sheet\n')
        out.write('# Generated from Tier-1 Metrics Sheet ...\n')
        out.write('metadata:\n')
        out.write(f'  last_updated: {date.today().isoformat()}\n')
        out.write('  version: v0.1-refreshed\n')
        out.write(f'  total_metrics: {len(merged)}\n')
        out.write('  sources:\n')
        out.write(f'    tracker_sheet: {SHEET_URL}/edit?gid=1081314132\n')
        out.write(f'    tracker_csv: {csv_path}\n')
        out.write('    v3_doc: https://docs.google.com/document/d/1U9vrVFRO4A_jbi7QhhDbYdWv8n834gq3udR3M1KTjQQ/edit?tab=t.94anu86ip79a\n')
        out.write('    goal_map: https://docs.google.com/document/d/1p5m4E70gaSLc7fCmpZnpDp9GCbCYVPgn8eBNOiFhfDA\n')
        out.write('\n')
        out.write(goals_def_text)
        out.write('\nmetrics:\n')
        for m in merged:
            out.write(f'  - id: {m.get("id","")}\n')
            out.write(f'    metric_name: \"{m.get("metric_name","")[:180]}\"\n')
            out.write(f'    human_goal: \"{m.get("human_goal","")[:250]}\"\n')
            out.write(f'    investment_priority: \"{m.get("investment_priority","")[:120]}\"\n')
            out.write(f'    risk_group: \"{m.get("risk_group","")}\"\n')
            out.write(f'    type: \"{m.get("type","")}\"\n')
            out.write(f'    poc_analytics: \"{m.get("poc_analytics","")[:60]}\"\n')
            out.write(f'    goal_tracking: \"{m.get("goal_tracking","")}\"\n')
            out.write(f'    definition: \"{m.get("definition","")[:200]}\"\n')
            out.write(f'    definition_status: \"{m.get("definition_status","")}\"\n')
            out.write(f'    target: \"{m.get("target","")[:150]}\"\n')
            out.write(f'    tshirt_lift: \"{m.get("tshirt_lift","")}\"\n')
            out.write(f'    operationalization_status: \"{m.get("operationalization_status","")}\"\n')
            out.write(f'    m360_link: \"{m.get("m360_link","")[:200]}\"\n')
            out.write(f'    added_to_scorecard: \"{m.get("added_to_scorecard","")}\"\n')
            v3 = m.get('v3_mapping',{})
            if v3:
                out.write(f'    v3_mapping:\n')
                for k in ['priority_id','priority_name','goal_id','goal_title']:
                    if k in v3 and v3[k]:
                        out.write(f'      {k}: \"{v3[k]}\"\n')
            dr = m.get('data_risk_mapping',{})
            if dr:
                out.write(f'    data_risk_mapping:\n')
                for k in ['priority_id','priority_name','nsm']:
                    if k in dr and dr[k]:
                        out.write(f'      {k}: \"{dr[k]}\"\n')
            if m.get('nsm_rollup'):
                out.write(f'    nsm_rollup: {m.get("nsm_rollup")}\n')
            out.write(f'    values:\n')
            for ve in m.get('values',[]):
                out.write(f'      - date: \"{ve.get("date","")}\"\n')
                if ve.get('value') is None:
                    out.write(f'        value: null\n')
                else:
                    out.write(f'        value: \"{ve.get("value","")}\"\n')
                if ve.get('status'):
                    out.write(f'        status: \"{ve.get("status","")}\"\n')
                if ve.get('source'):
                    out.write(f'        source: \"{ve.get("source","")}\"\n')
                if ve.get('comment'):
                    out.write(f'        comment: \"{ve.get("comment","")[:120]}\"\n')
            out.write('\n')
    print(f"Refreshed {yaml_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--refresh-sheet', action='store_true', help='Pull latest sheet and merge into yaml preserving manual mappings')
    parser.add_argument('--format', choices=['detailed','summary','both'], default='both')
    parser.add_argument('--export-gdoc', action='store_true', help='Generate ghtml for Google Doc export')
    parser.add_argument('--doc-id', help='Google Doc ID to export to (optional)')
    parser.add_argument('--tab-id', help='Google Doc Tab ID (optional)')
    args = parser.parse_args()

    if args.refresh_sheet:
        refresh_from_sheet(SCORECARD_YAML)
        # after refresh, continue to generate

    metadata, goals_def_priorities, metrics = parse_yaml_simple(SCORECARD_YAML)
    print(f"Loaded {len(metrics)} metrics, {len(goals_def_priorities)} priorities from {SCORECARD_YAML}")

    DOCS_OUT.mkdir(parents=True, exist_ok=True)

    if args.format in ('detailed','both'):
        generate_detailed_md(metrics, DOCS_OUT / "scorecard_detailed.md")
        generate_csv(metrics, DOCS_OUT / "scorecard_detailed.csv")

    if args.format in ('summary','both'):
        generate_summary_md(metrics, goals_def_priorities, DOCS_OUT / "scorecard_summary.md")

    if args.export_gdoc or args.format in ('summary','both'):
        generate_ghtml(metrics, goals_def_priorities, DOCS_OUT / "scorecard_summary_ghtml.html")
        if args.doc_id:
            # Try to apply to gdoc via meta CLI as suggestion
            base_tmp = "/tmp/scorecard_ghtml.base"
            # need base snapshot
            print(f"Exporting to Google Doc {args.doc_id} tab {args.tab_id}...")
            # get base
            os.system(f'meta google.docs get --id={args.doc_id} --output=ghtml > {base_tmp} 2>&1')
            cmd = f'meta google.docs apply --id={args.doc_id} --from=file://{DOCS_OUT / "scorecard_summary_ghtml.html"} --base=file://{base_tmp} --write-mode=suggest'
            if args.tab_id:
                cmd += f' --tab-id={args.tab_id}'
            print(cmd)
            os.system(cmd)

if __name__ == "__main__":
    main()
