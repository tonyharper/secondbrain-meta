<!-- Source: https://fb.workplace.com/groups/2088102991377052/permalink/2742683445919000/ -->
<!-- Title: H2'24 Reflection Post — RIDs for Half-Life -->
<!-- Author: Sunil Rathode -->
<!-- Collaborators: Quinn Sheridan, Colin Glaes, Kapil Pradhan, Tony Harper -->
<!-- Date posted: 2024-12-20 -->
<!-- Date accessed: 2026-03-31 -->

# RIDs for Half-Life - H2'24 Reflection and H1'25 Look Forward

As we approach the end of H2'24, I'd like to take a moment to reflect on the significant efforts made by the entire analytics org in advancing the RID Adoption. This post will summarize the scope covered in H2'24, outline the pending scope that has been moved to H1'25, provide high-level strategy on the major buckets of assets within the pending scope, highlight the effectiveness of RID STB linter and efficiency gains from RID codemods.

## Summary

The adoption of RIDs as primary identification keys are required for privacy compliance while also not disrupting analytics capabilities. By minimizing re-identification risks, reducing capacity needs (full ridification), and enabling consistent schemas and Idempotency, RIDs increase data retention and facilitate more accurate analysis.

- 95%+ of the Addressable tables in scope of Half-Life are RIDified.
- ~73% of the Eligible Pipelines owned by Analytics Org are RID Enriched (Including outside of Half-Life Scope).
- RID STB Linter has driven the RIDification share of eligible assets to 82%, 95% for those with retention > 45 days.
- Any pending scope from H2'24 and tables planned to be unblocked in H1'25 from half-life scope will continue to be the priority for RID workstream in H1'25, while also building infra capabilities to support Full-RIDification to benefit from zero cost deletion.

---

# H2'24 Reflection

## Scope Explained

We've addressed a significant portion of the scope in RIDifying addressable tables in scope for Half-Life which are actionable in H2'24. As of now, **~95%** of these tables have been RIDified. There are around 180 tables (~2%) from the pending addressable tables that don't have associated tasks, primarily because they were created or added to the scope after the last privacy wave 62 or are follow-ups to logger codemods that require manual intervention.

The remaining tables that are Non-Addressable fall into the following categories:

- **Will be Unblocked in H1'25:** ~3.5k tables belong to Bucketed RID, Deltoid, EE Pillar, and Morse, which are currently blocked from RIDification and remediation due to gaps in infrastructure capabilities or requiring special handling. However, we've partnered with the Infra teams in Q4'24 to begin building solutions for some of these categories. These tables will be unblocked for remediation in H1'25.
- **Low Priority:** This category includes tables with low priority, such as legal, temp tables, expected integrity tables, having non user actor prediction etc which do not require immediate attention. Our plan is to descope most of these tables upon alignment with legal. If any remaining tables are deemed necessary for Half-Life compliance, they will be added back to the scope and sent for remediation in Q2'25.
- **No UIDs:** Tables without UIDs are not eligible for RIDification. Can proceed with enrolling on UII-Nullification to fully remediate for Half-Life compliance.
- **Device ID:** DeviceRID is not available, therefore all the tables dependent on DeviceID are currently blocked from RIDification and Half-Life remediation. We expect to have timeline of DeviceRID availability in early Q1'25.
- **Eligible for Retention Reduction & Reaper:** Tables that are eligible for either retention reduction or will be deleted by Reaper, therefore eliminating the need for RIDification.
  - ~850 tables will be deleted by Reaper and do not have any partitions in the last 45 days and have not been refreshed. Additionally, no dependent lineage or access/traffic has been detected for at least 30 days. A custom reaper job configuration has been set up to target these tables.
  - ~1,200 tables do not have UIDs therefore not eligible for RIDification. However, these tables do not have reads on partitions older than 40 days in the last 30 days, making them suitable for retention reduction codemods. The deletion team is sending out these codemods with the option to enroll in UII-Nullification. Tables created by legacy APIs are not supported by codemods and will be federated to table oncalls.

## Effectiveness of RID STB

To lessen the need for federating RID tasks in the future and the significant costs associated, we've launched a linter to enforce new datasets to be RIDified, or in other words have one RID per UID.

The linter has helped drive RIDification of new assets of all retentions to 82%, and those with retentions > 45 days to nearly 95%. Over 1000 UPM Datasets have been linted by error mode.

## Remediation of Analytics Assets

In addition to driving RID adoption, the RID workstream has also supported the half-life remediation of RIDified analytics assets. Supported PPGs with a guide to enroll analytics assets into UII-Nullification to drive remediation efforts and provided a dataset and dashboard to evaluate the readiness of RIDified assets and monitor the enrollment progress for analytics assets in Half-Life scope.

## RID Infra

### RID Continuous Codemods

To tackle the massive scope of RIDification and alleviate some of the workload on FTE/CW, we developed a codemod to streamline the process of adding RIDs for identified UIDs in Hive tables.

At a high level, we utilized existing RID/Half Life data marts to generate inputs for the codemod service, which then applied our custom pipeline transformation logic.

The codemod generated RIDification diffs for 1961 pipelines with 48.3% (948) committed, totaling 2,844 hours of realized savings based on LOE. The overall **average time to close for committed diffs is ~14.5 days** with the latest data showing **just under one week**.

### Improved Infra Reliability

We have landed some changes to improve reliability of RID First World data foundation, which were previously hindered by latency issues in the RID pipeline landing times and delays in task auto-close. These delays were often caused by upstream signal delays or limitations in the task auto-close logic.

Key changes in H2'24:

- D67262993 - Remove the dependency on dim_tables which often used to delay the RID pipelines
- D61437645 - Identified tables eligible for Retention Reduction and Reaper to reduce the scope of Federation
- D62193965 - Added FamilyAccountRID RichType to RID list for RID verification
- D62421761 - Auto-close Tasks belong to Non-User Actor Annotation Tables
- D63858647 - Auto-Close Tasks when Half-Life inscope tables are RIDified and not required to RIDify tables < 45
- D64017777 - Readiness of the RIDified table for UII Nullification
- D66349546 - Include coverage to Arraytype fields for RID verification
- D66608997 - Fix logic to identify morse downstream tables

---

# H1'25 Look Forward

Our efforts in H2'24 for the HL program have significantly reduced the backlog by clearing ~95% of the addressable tables, but there are still ~3k RID eligible tables in the Half-Life Analytics backlog. The majority of the remaining tables are blocked due to lack of infrastructure capability and we continue to see backlog increasing due to the early-stage maturity of the STB tooling and improved detection of assets with UII richtypes.

The guidance from **Deletion Privacy Area (PA)** is to prepare for the full compliance process by the end of H1'25 while they are in discussions with assessors to finalize the timeline.

As a result, program efforts need to be extended beyond 2024 to H1'25 to address the remaining backlog.

## Scope for H1'25

Any remaining table from current scope and Non-Addressable tables from H2'24 will be moved to H1'25 scope of RIDification. As and when RID eligible tables which belong to edge cases are unblocked from ridification they will be added to the federation scope.

We have established partnerships with various teams, including DI, Experimentation Platform, Data Understanding, and EE Pillar, to tackle edge cases that require special attention for RID and Half-Life remediation. Our collaborative efforts aim to build capabilities to unblock tables belonging to these edge cases by H1'25.

While we have clearly defined next steps and are confident about remediating some of these assets before the end of H1'25, there are still categories such as DeviceRID where we lack clear commitment or timelines on next steps. Unfortunately, these assets will remain at risk for RID and Half-Life remediation until further updates in Q1'25.

Half-Life Remediation of Analytics efforts in H1'25 can be organized into following workstreams:

- **RIDification for the assets in HL (Continue):** Building on our previous efforts, we will continue to focus on RIDifying assets in the Half-Life scope. This includes:
  - Backlog assets that are being unblocked from edge case categories (e.g., Morse Downstreams, Bucketed RID)
  - New assets added to the current backlog after PW62

- **Onboarding to UII Nullification (Continue):** We will continue to onboard assets with RID into nullification using a codemod or bulk enrollment. PPGs can choose to receive UII-Nullification enrollment diffs generated centrally to benefit from auto-rebase and reduce operational overload or create these diffs by bulk enrollment script. However, PPGs are still expected to drive the acceptance of these codemods to fully remediate analytics tables.

- **Centrally Remediated CODMODs/REAPER (Continue):** The Deletion team will increase the scope of Reaper by targeting tmp/test tables with their existing config in H1'25. Assets eligible for Reaper or retention reduction codemods will not be included in federation and are expected to be remediated centrally with minimal support from PPGs on nudging and raising urgency to close the diffs. If there is any disagreement on retention reduction codemod, reviewers can choose to enroll on UII-Nullification directly. These tables are most likely to be tmp or do not have UIDs, therefore no risk to directly enroll on UII-Nullification.

- **Remediation of Deltoid Tables (New Workstream):** EP will send diffs to table oncalls to enable inner join behavior. Depending on the PPG's remediation strategy, these tables will either receive tasks or codemods to enroll on UII-Nullification. While most of this work will be centralized, PPGs may need to support a small subset of tables where EP cannot confidently infer the correct action, which will be federated.

- **Continuous Compliance (New Workstream):** To ensure ongoing compliance with Half-Life requirements, we will establish a Continuous Compliance workstream. The Deletion team has recently defined criteria for continuous compliance, which will be used by the RIDification workstream. We will federate tasks for assets that are eligible for RIDification via the Continuous Compliance workstream. More details on the Continuous Compliance workstream will be shared in January 2025.

## Planned RID Infra Improvements in H1'25

### Federation

We recognize the need to enhance the user-facing experience of the RID workstream, and have planned several improvements to address this. Our focus will be on updating RID tasks with signals that explain why a task remains unresolved. These signals will be displayed on the Half-Life UI, with links to the tasks, making it easier for users to understand why a task is still marked as unresolved and hasn't been auto-closed.

- We will also explore the option of piloting interactive workstreams on Fedplat for the continuous compliance RIDification workstream.
- Many user group questions revolve around updating Actor Annotation, Richtype and Retention. Therefore, we will prioritize embedding these options into the current smart workflow, allowing tasks to be auto-closed sooner if the issue is related to incorrect RichType, Actor, or reduced Retention.

### Stop The Bleed

The backlog has been growing across all workstreams with creation of new assets, adjustments of retention, or newly discovered to have UIIs. Our plan is to achieve continuous compliance and improve governance at the authoring time with linters and diff enforcement.

- We will invest in improving the user experience to drive down the bypass rate
- We will invest in the reliability and the framework we're leveraging
- We may invest in a STB program for LoggerConfigs (Blocked until S461573 is resolved)

### RID Codemods

Given that there are historical assets that will not be caught by STB and our objective is to make the warehouse RID First we must invest in continuous codemods at the root and downstream levels. To achieve success we must invest in driving the metrics that matter the most for codemods:

1. **Coverage:** We will invest in improving the codemod itself to handle more complex cases
2. **Close Rate:** We will invest further in our nudger, improve test plans, and explore other strategies

## Acknowledgment

Thanks to PPG Partners Chandra Sreeram, Kapil Pradhan, Abhijeet Bubne, Mahendra Reddy, Liz Chan, Dan Corcoran for partnership to drive this effort at PPG level.

Thanks to Colin Glaes for constantly improving the RID STB linter user experience and blocking ~1000 datasets from being added to the backlog, and building RID codemod utility to automate the RID enrichment and creating diffs for 1961 pipelines with 48.3% (948) committed.

Thanks to Chandra Sreeram for laying the groundwork of the UII Nullification readiness tracker.

Thanks to Somya Kumar for adding tables with no UIDs and no reads on older partitions to scope of Retention Reduction Codemods within Half-Life which reduced the federation scope within RID workstream.

Thanks to Mike Athanasakis for evaluating the criteria and adding custom config within reaper to target those tables in scope of half-life which helped in reducing the scope of federation.

Thanks to Shradha Budhiraja, Gustavo, Ria Garg, Omer Khalid, Huey Ning Lok for prioritizing RID requirements for analytics assets and supporting the RID workstream within the Half-Life program.

Thanks to DI partners Ethan Dickinson, Robert Rusch, Jon Griffin, Dan Arpino for landing optimizations for UII Nullification and supporting analytics use-cases in the Data Warehouse.

Thanks to Tuncay Tekle, Saurav Sen, Peishan Wang, Chris Green, Dmitry Ponomarev, Aaron McGhie for building infra capability to add RIDs on Morse tables.

Thanks to Chelsea Miller for stepping in and ramping up on the Deltoid anonymization issue, which was blocking tables from Half-Life remediation.

Thanks to Quinn Sheridan, Ramakant Shankar, Anupriya Tripathi, Mahesh Kshirsagar, Atul Mogha for being key members in shaping the project's early stages and setting up a foundation for the RID Adoption within Analytics.
