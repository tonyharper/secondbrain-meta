<!-- Source: https://fb.workplace.com/groups/1380785639188244/permalink/1737163660217105/ -->
<!-- Title: "Shift-Left" for Data Understanding in H1 2025 -->
<!-- Date Accessed: 2026-03-31 -->

# "Shift-Left" for Data Understanding in H1 2025

**Author:** Chetan Bhat
**Published:** 2025-07-01

## TL;DR

- We achieved the H1 2025 goal of > 99% 14-day and > 40% creation-time SLA coverage for Rich Types, improving semantic and contextual data understanding for privacy compliance.
- Expanded UPM DataSets support to cover 80% of Hive assets, including non-schema and dynamic SQL-backed tables, enabling consistent metadata assignment across producers.
- Developed user-facing runtime-agnostic APIs and prototyped automated diff stacking to improve authoring-time and diff-time data understanding signals, enhancing developer experience.
- Reduced privacy task friction significantly, lowering impacted assets from 13K to 8.7K in six months, with insights guiding classifier improvements and manual task reduction.
- Set H2 2025 goal to reduce Hive Deletion privacy-workstream tasks to under 4000 by improving lint messages, productionizing code-patch interventions, migrating legacy APIs, and expanding dataset-backed producers.

## Context: What is "Shift-Left" for Data Understanding?

The main idea behind "[Shift-Left](https://engineering.fb.com/2025/04/28/security/how-meta-understands-data-at-scale/#:~:text=shifting)" is to integrate developer actions, such as data understanding annotations and policy assignments (eg: [Privacy Metadata](https://www.internalfb.com/wiki/Privacy/Deletion_Data_Warehouse/Applying_Deletion_Plan_on_Hive_Assets/)), as early as possible into the data-engineering development experience. Our goals are to:

- Minimize end-to-end developer friction and reduce the cost of compliance
- Significantly improve the SLA, quality, and coverage for above-mentioned metadata

## Our Strategy: Consistency, Early Action, High Quality

To achieve these goals, we've focused on three key pillars:

- **Consistency**: Standardizing processes and tools for uniform application of Data Understanding Metadata and privacy policies across all programs and data producers.
- **Early Action**: Integrating metadata as early as possible in the asset lifecycle, ideally during the asset creation stage.
- **High Quality**: Implementing checks and validations to maintain high quality and communicate downstream impact.

## Key Technical Investments and Progress

Our technical strategy involves building and supporting high-quality development-time interventions. We've made good progress in many areas:

### Expanding UPM DataSets Support for All Producers

A standardized metadata container (UPM DataSet) is crucial for consistent assignment of Rich Types, Actor, and other metadata. We expanded UPM DataSet reach to the remaining 80% of Hive assets (including non-schema in code producers) through [in-memory datasets](https://docs.google.com/document/d/1-0nSh_LX8jv_8im4WaTjRQk7V7C5lmzM2EnN0OdoBrE/edit?tab=t.0) and "[external datasets](https://fb.workplace.com/groups/1290212214459059/posts/2982695251877405)".

- User-Facing APIs for Runtime-agnostic callers: We now support an expanding set of "public-facing APIs" to enable seamless creation, validation, and actualization of UPM DataSets for all Hive Assets, even outside Dataswarm. This includes broad-stroke APIs for descoping using context(..) style APIs (e.g., [DataUnderstandingMetadataContext](https://docs.google.com/document/d/1-0nSh_LX8jv_8im4WaTjRQk7V7C5lmzM2EnN0OdoBrE/edit?tab=t.0#bookmark=id.wv32kbifq669)) that can be used in non-dataswarm contexts to apply NonUser actor.
- Dynamic SQL-backed Hive tables: We continue to leverage in-memory dataset APIs to improve attaching rich type metadata to dynamically created tables, which account for at least [35% of new creation-time](https://www.internalfb.com/unidash/dashboard/rich_type/rich_type_sla/?dimensional_context_947935263697350=%7B%22macros%22%3A[]%2C%22limit%22%3A5%7D) Rich Type assignments.

### Authoring-time and Diff-time Data Understanding Signals

Bringing high-quality rich type and actor predictions to authoring and diff time continues to be a major focus. We are addressing known gaps such as poor quality regex-based lints and a lack of representative data samples at early stages.

- **[In-Progress] Automated Diff Stacking Prototypes**: We are prototyping an automated process for generating [just-in-time stacked diffs and code-patches](https://docs.google.com/document/u/0/d/1QuCOMQ4Zl_QtsK-9Qfhy86udO9F8eBUQ3M0hOMOWeVo/edit) based on signals from tester runs, BII real-time predictions, and on-demand Unified Prediction Pipeline (UPP) predictions. Initial feasibility measurements are promising, showing a high number (almost 70%) of [diffs with schemas have recent tester runs](https://fburl.com/daiquery/x3wlx4i6).
  - We are going to run a more [comprehensive backtesting](https://docs.google.com/document/u/0/d/1bTesgixzkocTUagQLNPHd5Sn4fbWz3gtcZyAclMWpmw/edit) / simulation to identify the right problem areas that block us from achieving high coverage and quality
  - We are currently working with the Dataswarm team to [maintain high-bar](https://docs.google.com/document/u/0/d/1-SAWwLhtoSzAl9DQwQ6LJpSeXJcixJtiN_H_lUa5vFk/edit) for Tester runs (used for generating representative data samples)
  - In H1, BII shipped new real-time APIs that we leverage for Rich Type, Actor Data Understanding predictions.
- **[New] Linter Effectiveness**: We are investing in our linting ecosystem to increase its effectiveness, which will help with rich types and actor annotations, and potentially help in newer areas (GenAI guard columns). Our goal is to minimize false positives and guide disagreement flows.

### Privacy Impact Analysis and DataSet Change Management

Providing guardrails against risky changes across various authoring surfaces is essential for moving fast with confidence.

- **[Continue] Privacy Impact Analysis**: We are building new [privacy impact analysis](https://fb.workplace.com/groups/6135794916526503/posts/9596374260468534) signals, such as quantifying deletion impact on Rich Type assignment changes and validating distinct and union type definition changes.
- **[Needs Revisit] Validation Infra for Transient Diffs**: We [initially planned](https://docs.google.com/document/d/1YU6V3UaLwltKFXCRJfIRGiB1zICZkmEpZlo4SXuxuvY/edit?tab=t.0#heading=h.86y16vrd4qh2) expanding our validation infrastructure to support transient diffs, which has potential to enhance change management, but temporarily paused this to support higher priority items. Based on customer feedback, we will re-evaluate this workstream and assess the expected impact.

## H1 2025 Goals and Progress

In H1, we focused on reducing the time it takes per asset to achieve sufficient semantic (Rich Type) and contextual (Actor) understanding for Privacy.

### Rich Types 14-Day SLA

Our H1 goal for 14-day rich type coverage was [> 99%](https://fburl.com/datainsights/u5l57wzq), and we successfully met this target, reaching 99.4%.

Our H1 goal for 1-day rich-type coverage (proxy for creation-time assignments) was also met by reaching > 42%.

### 1-day (creation-time) SLA for Actor Annotation and Rich Types

We're tackling these goals through several levers:

- Expanding In-memory API to dynamic producers and hot-spot on-calls: These key interventions will help address a significant volume of violating 0-day SLA fields (similar to the past work we did for HealthCompass and O2O)
- Stack Diffs and Codepatches for Dataset-backed Assets: This new approach will be key to improving both Actor annotation and Rich Type coverage at authoring time in the future. The same user experience will allow Hive Deletion teams to apply effective and compliant Deletion plans to the user's schema with low-effort.
- Improving Lint Effectiveness: Addressing false positives in lint assignments, especially for Rich Type assignments, will reduce friction for developers.

### Measuring Privacy Friction

Harper Ma and Privacy DE team did analysis work in Q2 ([Shift Left Measurement](https://fburl.com/gdoc/75xprj40) and [Shift Left Goals](https://fburl.com/gdoc/bdhwn92v)) to understand the key friction areas that would potentially benefit from shift-lefting in different stages of the development lifecycle. Key insights:

In the past six months, [8.7K](https://fburl.com/unidash/2qnqjoez) assets have been subject to at least one privacy task. Our Shift Left initiative on RT and Actor Coverage has yielded significant results, reducing the number of impacted assets by 4K compared to H2 2024, when [13K](https://fburl.com/daiquery/w253sucn) assets required privacy tasks for Half Life.

- Of the 8.7K, 86.4% (~[7.5K](https://fburl.com/daiquery/s8xy38cj)) are Deletion tasks. Breakdown by table producers:
  - 2.5K are dataswarm backed which can be improved by investments in stack codemod and lint message for retention warnings
  - 1.4K are produced by logger/public
  - 0.7K are produced by dataswarm/withschema/legacy_table. We can improve this bucket by migrating them to DataSwarm backed.
- ~[1.2K](https://fburl.com/daiquery/xozohwj7) are Rich Type manual assignment tasks.
  - 66% were closed by asset owners abandoning the codemod diffs. We should improve the classifier in the next half for top abandoned labels such as UserIGID and MaybeUserFBID.
  - The rest tasks were closed by owners accepting the diffs. We should gradually move them to High Confidence predictions to reduce manual confirmation from owners.

This informs our technical investments and relative priorities.

## Pivoting to Reducing Friction: Privacy Wave Tasks in H2

Our H2 goal for Privacy Wave Tasks is to reduce the number of Hive Deletion privacy-workstream tasks (from dataset backed + legacy producers) by more than 50%, from a [baseline ~9500](https://fburl.com/unidash/36lad2fa).

We're addressing this by:

- [Measuring the friction](https://docs.google.com/document/d/1UnRATp8h6O-41xovvPPxmPpIbn5UzTwn8q5HQr5eOrc/edit?tab=t.0#heading=h.4n2ml3kp3sdu) and baseline cost-of-compliance
- Improving Lint Messages for Shorting Retention: This is a major lever for dataswarm/withschema/dataset and logger/public producers.
- [Productionizing](https://docs.google.com/spreadsheets/d/1w8pbzsZ2O7EnI-FDVuAcU5yJcvxT9tEn_2togAe6_88/edit?gid=0#gid=0) the Stacked Diff + Code patches interventions
- Migrating Legacy API to supported DataSet backed operators: This will help reduce tasks for dataswarm/withschema/legacy_table producers.
- Expanding In-memory DataSets to other asset producers
- Increase UPM-managed retention coverage for hive assets.

We will continue to meet our customers where they are and adjust our strategy to ensure we meet our Shift-Left goals and provide the best possible developer experience and supporting compliance initiatives.
