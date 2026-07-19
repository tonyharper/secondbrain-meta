<!-- Source: https://docs.google.com/document/d/1YhSddiEYoDqfVVb52xnjDfZBD226mFlH_TbTBjKW8b4/edit -->
<!-- Title: FRAPS - Measurement Inventory March 2026 -->
<!-- Accessed: 2026-03-31 -->

# FRAPS - Measurement Inventory March 2026

## Existing Artifacts

- [Initial 2026 Measurement Plan](https://fb.workplace.com/groups/1948585412696066/posts/1949653572589250)
- [SPARE H1 2026 dashboard](https://www.internalfb.com/unidash/dashboard/spare/draft_spare_h1_26_goals/overview) - in maintenance mode
- [Agent Data Access Friction dashboard](https://agent-execution-di.nest.x2p.facebook.net/) - early view of agent data access executions, based on logs processed by DIPS (DataInfra Permission Service)
  - Logging: [datainfra_permission_service_logger_logs](https://fburl.com/data/ul46hil1)
  - Employee data: [d_employee_plus](https://fburl.com/data/23j0et3d)
  - Fact: [fct_agent_execution_dpas_requests](https://fburl.com/data/l7chfhdv)
  - Agg: [agg_agent_execution_dpas_metrics](https://fburl.com/data/3zftpy4e)
- [Security Measurement Dashboard](https://claude-code.nest.x2p.facebook.net/) - updated version in Hatch, legacy in unidash
  - Core fact table: [fct_agent_security_traces](https://www.internalfb.com/intern/data/search/?_v=1774310843&silica_token=HiveTable%2Ffct_agent_security_traces%3Asecurity&surface=info_page)
  - Core logging table: [artillery_agent_platform_events](https://www.internalfb.com/intern/data/search/?_v=1774310880&silica_token=HiveTable%2Fartillery_agent_platform_events%3Ainfrastructure&surface=info_page)
  - Employee data: [d_employee_plus](http://d_employee_plus)
  - Broader set of tables available in this [recipe](https://www.internalfb.com/analytics-agent/recipes?recipeID=729126150167126)
  - Metric calculation logic: [S4AI Observability Logging](https://docs.google.com/document/d/1hUD5laqMl0V2lENo1pyTBiqsGLz_ArfwbeNrp3-O_5k/edit?tab=t.gzvxkueephl9#heading=h.6rfzca5f0qqs)
- Meta CLI Data sources

**Tracking items in related forums**

- Claude Code sprint
  - [Claude Code - Two Week Sprint Plan](https://docs.google.com/document/d/1_SNGbIOJaVl_FHjWhAX7USeD57HKKAnxc1viMyqPk64/edit?tab=t.mb4untonv7fs#heading=h.9qqbzw3unpza)
  - [Progress post](https://fb.workplace.com/groups/1426023281530911/permalink/2132542730878959/)
- Agent friction available insights: [CC Sprint Demo - Observability (3/16)](https://docs.google.com/document/d/1j-HNz6oQTOzkINq6jqeYzK7maDLh1vEoU0LHro6ml40/edit?tab=t.0#heading=h.7p5mmbm4h6py)

## OKRs

- [[Canonical] FRAPS: Friction Reduction for Agents Privacy & Security](https://docs.google.com/document/d/1N5nKaNhcafg4kaxpPZdFNmZBEM5qyzFIPmsNJYs93TQ/edit?tab=t.0#bookmark=kix.4kaw4axgj6tz)

**Agents in Scope**

- [[CANONICAL] Agent Security SPF](https://docs.google.com/spreadsheets/d/1BGa6Ydk5nWebc9YfYIpliYW9AH7smBAslF36kHqk7gY/edit?gid=926611909#gid=926611909)

## Things we seem to be missing

- Topline FRAPS dashboard. Simple, similar to SPARE. Uses the same forecasting / seasonality methodology
- Probably missing PAI data in the security datasets. Possibly missing DW data as well
