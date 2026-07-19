# Risk Data AI Enablement

**Project Tag**: `project:risk_data_ai_enablement`

## Overview

Making Risk data "AI-ready" by structuring and enriching it so AI agents (Analytics Agent, Datamate, Devmate) can understand and interact with it accurately. Initial tests showed poor pass rates when AI agents query Risk data out-of-the-box. By adding context through Semantic Models and Repo Context, we've seen 10-60% improvements in accuracy across adopting domains.

## Current Status

**Phase**: Phase 1 (Foundation) — In Progress. Phase 2 (Scale) and Phase 3 (Full Adoption) planned.

## Key Deliverables

| Name | Description |
|------|-------------|
| Semantic Models | Structured business knowledge — metrics, definitions, business rules, lineage, join patterns — providing AI agents a single source of truth |
| Repo Context | Codified pipeline knowledge — skills, rules, architecture docs, testing patterns, on-call playbooks |
| Evals | Comprehensive evaluation sets measuring AI agent performance on Risk-specific queries. Target: 85% pass rate on "Golden Set" |
| Domain Coverage | Target 100% of key Risk domains with Semantic Models |
| Use Case Integration | Expanded integrations beyond Analytics Agent and Datamate |

## Key Stakeholders

| Person | Role | Team |
|--------|------|------|
| Tony Harper | Program sponsor | Risk DE |
| Chris Ventura | AI Readiness lead | Risk DE |
| Sunil Rathode | Program lead | Risk DE |
| Swetha Singiri | Coverage measurement | Risk DE |
| Stephanie Yee | Manager | Risk PM |

## Key Documents

| Name | Description |
|------|-------------|
| [Launch Post](https://fb.workplace.com/groups/992063232674504/permalink/1391829086031248/) | Risk Data AI Enablement program announcement (Feb 2026) |
| [Project Repo](https://www.internalfb.com/code/fbsource/fbcode/dataswarm-pipelines/dataswarm_commons/privacy/data_ai_enablement/) | Code and plans for the program |
| [Detailed Project Tracker](https://www.internalfb.com/code/fbsource/fbcode/dataswarm-pipelines/dataswarm_commons/privacy/data_ai_enablement/plans/detailed_project_tracker.md) | Detailed tracker |
| [Measurement Plan](https://docs.google.com/document/d/1sSi-RoizS0LoDaaFBU_-w8KYmo8NeX00wP-QJrS3f_s/edit?tab=t.xa4zn9uixen9) | How we measure success |
| [Semantic Models Runbook](https://fburl.com/semantic-models-runbook) | Getting started guide |
| [Semantic Models Wiki](https://www.internalfb.com/wiki/Semantic_Models_for_Data/) | Wiki documentation |
| [Semantic Models WP Group](https://fb.workplace.com/groups/1991251848365266) | Workplace group |
| [Office Hours](https://fburl.com/meeting/j3pkrdb9) | Regular support sessions |
| [AI Measurement Roadmap](https://docs.google.com/document/d/1l0ZzOslLNLVogWlGCZoEJh3lakMpbZ2nV8ETsaNfsp4/edit) | Swetha's measurement roadmap — metric themes (AI Adoption, Eval Quality, Asset Coverage, Adoption & Impact), H1 milestones, eWAU@75 dashboard plan, domain onboarding status, and semantic model eval results |

## Success Metrics

- **Eval Pass Rate**: Target 85% on Golden Set
- **Domain Coverage**: Target 100% of key Risk domains
- **DE Adoption**: Increased % of AI-generated diffs
- **XFN Self-Service**: Partners confidently using AI tools for data needs

## Open Tasks

View tasks for this project:
```bash
tasks --agent-enabled search --name $USER --tag "project:risk_data_ai_enablement"
```

## Project Files

- `docs/` - Project documentation
- `meetings/` - Meeting notes
- `analysis/` - Notebooks and data analysis
- `outputs/` - Deliverables and artifacts
