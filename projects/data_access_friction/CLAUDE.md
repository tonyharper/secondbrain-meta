# Data Access Friction

**Project Tag**: `project:data_access_friction`

## Overview

Working with the SPARE (Security & Privacy Access Rebalancing Effort) initiative to reduce Tech FTE data access friction across Meta. The Data Warehouse was historically responsible for ~50% of company-wide friction. The project involves building easier-to-query aggregations and views of friction data from Security DE sources, and preparing analysis for senior leadership review.

## Current Status

**Phase**: Active — building prototype aggs and views of friction data

## Key Deliverables

| Name | Description |
|------|-------------|
| Friction Data Aggs | Easier-to-query aggregations of user friction data from Security DE |
| Leadership Analysis | Friction analysis prepared for senior leadership review |
| Accessmate Integration | TODO — understanding how Accessmate reduces DW friction |

## Key Stakeholders

| Person | Role | Team |
|--------|------|------|
| Tony Harper | Project lead (Risk DE side) | Risk DE |
| Nick Castro | Partner | Security/SPARE |
| Ben Krull | Partner | Security/SPARE |
| Dan May | Partner | Security/SPARE |

## Key Documents

| Name | Description |
|------|-------------|
| [AIDRE & SPARE Impact Post](https://fb.workplace.com/groups/266626206077195/permalink/853367510736392/) | Executive summary of SPARE's impact on DW friction |
| [S587842 - Friction Hours SEV](https://www.internalfb.com/sevmanager/view/587842) | SEV for incorrect Friction Hours and 1+ Day Interruptions due to select_with_budget data |
| [T247302221 - ACL Request](https://thrift.internalfb.com/intern/tasks/?t=247302221) | ACL request for oncall_security_de data access |
| [T234785384 - Friction Table Access](https://thrift.internalfb.com/intern/tasks/?t=234785384) | Permission request for security.fct_iam_user_friction |
| [Data Access Friction Review - Brady Preread (3/3/26)](https://docs.google.com/document/d/13kB1O6D_HQZhZaTcYJ9EEzInXbpEihVcW-QCM0K1wa0/edit) | Preread for Brady review covering 2025 results (33% friction reduction), 2026 YTD regressions (+25%), AI Agent friction analysis, and H1 investment plans |

## Key Data Sources

- `security.fct_iam_user_friction` — Core friction data table
- ACL: `DATA_PROJECT:oncall_security_de`

## Open Tasks

View tasks for this project:
```bash
tasks --agent-enabled search --name $USER --tag "project:data_access_friction"
```

## Project Files

- `docs/` - Project documentation
- `meetings/` - Meeting notes
- `analysis/` - Notebooks and data analysis
- `outputs/` - Deliverables and artifacts
