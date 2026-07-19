<!-- Source: https://fb.workplace.com/groups/1167810663557228/permalink/2528290264175921/ -->
<!-- Title: SEV S512065 Post — OGRE Migration for Risk Data -->
<!-- Author: Tony Harper -->
<!-- Date posted: 2025-04-25 -->
<!-- Date accessed: 2026-03-31 -->

# SEV S512065 - OGRE Migration for Risk Data

## TL;DR

- Old Compliance Graph data is now known to be inaccurate and/or corrupted post-OGRE migration. As such, **all Hive data and analytics reporting related to the Compliance Graph should be considered unreliable until it has been migrated to new OGRE sources. We will be adding megaphones to dashboards as appropriate.**
- This migration is complex and it is not possible to estimate a precise timeline. Risk DE is going into lockdown to complete it as quickly as possible.
- In the meantime, expect dashboards, metrics, and Hive tables that rely on the Compliance Graph to stop showing new data until they are migrated.
- The recently released Risk Review (formerly CS 2.0) dashboards have already been migrated and as such are not impacted.
- Please direct all escalations to me.

## Context

With the migration of the compliance graph to [OGRE](https://www.internalfb.com/intern/staticdocs/ogre/docs/users/intro), Risk DE has identified significant inaccuracies and breakages in the old CG data, to the point that many of our pipelines, tables, and metrics are broken or inaccurate.

To remedy this, Risk DE is migrating all of our data from old CG datasets to the new OGRE datasets. **This is non-trivial, as many of the data elements and models that existed in the old CG no longer exist. We are effectively redesigning/rewriting all data pipelines related to the compliance graph.** As such, we can expect dashboards, Hive tables, and metrics that consume compliance graph data to be impacted during this migration.

## Migration Strategy

Our highest usage datasets (dim_pfh_node, agg_privacy_review_verification_action) that rely on CG will have been migrated to OGRE by 4/25. Any downstreams of those tables will be unblocked at that point.

Risk DE will go into lockdown starting 4/28/25 to migrate the remaining tables, supported by Risk Review SWE. It is not possible to project a timeline at this point, as each migration represents unique challenges. This is Risk DE's P0, and we have reprioritized all DEs who are equipped to help. **Expect many pre-CS2.0 dashboards and metrics to be unavailable for the coming weeks, and expect heavy disruption to Risk DE priorities.**

Anastasia Gandrik will follow up shortly with a post on the lockdown.

## Reporting Issues and Escalations

Please flag any issues in the SEV. If you find impacted tables or dashboards, you are also welcome to add them to the documents linked below.

Please report any other concerns or escalations to me.

Please refer to [S512065](https://www.internalfb.com/sevmanager/view/512065) for updates.

## Tables to Migrate

[Link to spreadsheet where additional metrics, tables, and dashboards may be flagged](https://docs.google.com/spreadsheets/d/1EG-YM9wEBEvPNazVsKC7nynLSOqj7VK4zICInAAriXU/edit?gid=1978986313#gid=1978986313)

- dim_pfh_node
- agg_privacy_review_verification_action
- privacy_ta_commitments
- agg_privacy_review_verification_action_flattened
- dim_requirement_versions
- agg_privacy_review_duration_metrics
- agg_privacy_review_canonical

## Impacted Dashboards/Metrics/Analyses

Note: only P0s have been collected so far. We expect P1s and P2s to be added over the next several days.

[Link to spreadsheet where additional metrics, tables, and dashboards may be flagged](https://docs.google.com/spreadsheets/d/1EG-YM9wEBEvPNazVsKC7nynLSOqj7VK4zICInAAriXU/edit?gid=1978986313#gid=1978986313)

Key impacted items include:

- **CS 2.0 Health Dashboard** (Steve Fischer) - P0, Cannot track CS 2.0 - underlying data: dim_pfh_node
- **CS 2.0 Operations Dashboard** (Steve Fischer) - P0, Cannot track CS 2.0 - underlying data: dim_pfh_node
- **CS 2.0 Executive Dashboard** (Steve Fischer) - P0, Cannot track CS 2.0 - underlying data: dim_pfh_node
- **CS 2.0 Funnel Dashboard** (Steve Fischer) - P0, Cannot track CS 2.0 - underlying data: dim_pfh_node
- **Foundations OKR 1.1** - PPG Distributed Work Progress (Reiko Yoshida) - P0, Cannot track P0 Foundations OKR
- **Foundations OKR 1.2** - % COP Owned MAP Milestones Meeting SLA (Reiko Yoshida) - P0
- **Foundations OKR 1.3** - Risk Review Product-Level Coverage Rate (Reiko Yoshida) - P0
- **Retention H1'25 Goal Tracking Dashboard** (Jeevanreddy Kommula) - P0, underlying data: privacy_ta_commitments
- **PR verification duration bottlenecks / % low touch reviews / % of automated evidencing requirements** (Oliver Kaus) - P0, underlying data: agg_privacy_review_verification_action_flattened, dim_requirement_versions, agg_privacy_review_duration_metrics, agg_privacy_review_canonical
