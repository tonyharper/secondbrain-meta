# Data Risk — Overview

_Last updated: 2026-07-19_
_Source: migrated from _archive_v1_2026_07/projects/data_risk_analytics_lead/CLAUDE.md + status.md_

## Purpose

Primary analytics owner and point person for Data Risk group within Risk org. Cross-functional role — leads DEs and DSs for analytics/insights across Data Risk areas. Coordination, day-to-day decisions, escalation.

Covers 11 risk areas: Restricted Data, User Data Inventory, Anonymization, Data Access & Portability, Data Deletion & Retention, Anti-Scraping, Data In/Out, Purpose Limitation, Cross-Product Data Practices, Competitive Data Use, Cross-Promotion.

## Stakeholders

| Person | Role | Context |
|--------|------|---------|
| Oliver Pell | DRI, Data Risk | Primary stakeholder, strategy + execution |
| Arash Nikkar | Accountable Lead, Data Risk | Accountable to Michel for Data Risk outcomes |
| Stephanie Yee | Analytics & Research Lead | Tony's leadership chain on analytics |
| Yiannis Papagiannis | Dir, SWE, DM+DB | Sole DRI for all DM+DB decisions, drove pod restructuring Apr 2026 |
| Lucy Baker | PM POC | XFN POC Data Risk |
| Akanksha Julka | TPM POC | XFN POC |
| Baris Cem Sal | DS POC | XFN POC |

## Rhythm

TBD — was learning rhythms when system stalled. Pods are execution unit since Apr 7, 2026 (Introducing Pods). RAGL/ERPL/Operating Reviews deprecated.

Pod model: 46 pods across 3 RAGs (Competition, Data Mgmt & Boundaries, User & Restricted Data). Registry in Google Drive.

## What happened last (as of 2026-05-04 archive)

- URD at 100% pod reporting (21/21), Competition 4/6, DM&B dark 0/18 for 3 weeks
- Forest rollout measurement finalization target 5/11 — timeline: DS reviews with Jeb & Erin 5/4, refined plans 5/6 async, final review 5/7 hold
- ToMM prevalence regressed to 2% (non-prod field), fix landed
- GRC 6-week sprint Apr 14-May 25 — Control Testing Automation (90% SVT), Evals, CAIP/Forge
- Barnaby's "no strong analytics strategy" signal still unaddressed

## Open Threads (from archive — needs fresh check)

- [ ] DM&B reporting gap — 18 pods dark, needs escalation?
- [ ] Self-evidencing metric definition — full vs partial ambiguity (RD Discovery 11.2% full / 42.7% partial)
- [ ] Forest measurement finalization — pressure-test with Jeb/Erin/Abhishek/Stephanie
- [ ] Controls measurement takeover — scope with Connie/Ji, Mark Berryman ~100 SEV-worthy issues
- [ ] Barnaby analytics strategy response
- [ ] Chris Ventura gap — moving to Central Analytics AI Foundation, hands-on SM work gap

## Key Docs

See `key_docs.md` for links + TLDRs.

Pod registry: https://docs.google.com/spreadsheets/d/15eR0KeDTluV1gVySnm6jvbLG8s7ijeERxh1eI60S9FM/edit?gid=449800625
Pod reports: `~/My Drive/DataRiskPods/` in Google Drive (per old system — verify path)
