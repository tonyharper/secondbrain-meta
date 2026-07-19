<!-- Source: https://docs.google.com/document/d/15mku2Nu6gqeclzYi1qpK22f3O-FfUHdZkjJSx67Vmvo/ -->
<!-- Title: RTUP — Real Time Unified Prediction -->
<!-- Date Accessed: 2026-03-31 -->

# [Shift Left] Real Time (RT) Unified Prediction (UP) [RTUP]

## Opportunity

The annotation coverage of hive tables within 1 day is [67.2%](https://fburl.com/daiquery/k4ny8zi3) for Rich Types and [59.7%](https://fburl.com/daiquery/b8wexx2j) for Actors. It would be valuable to land these annotations faster for the following reasons.

### Enable Workstreams

- Readiness to support agent metadata
- Half Life: reduce [avoidable Privacy Tasks](https://fb.workplace.com/groups/1380785639188244/permalink/1744934636106674/): It was shown that 36.4% of 2025H1 Deletion tasks could have been avoided with inner loop suggestions and user implemented deletion plan
- XSU: Reduce the amount of FP blocked flows resulting from missing Actor / Rich type
- MonCR: UPP delay is cited as a reason for 35% of missing actors ([source](https://fburl.com/datainsights/wqbls96b))

### Reduce Fragmentation Risk

- Slow annotation applications may drive teams to build their own service to suit their latency needs
- [GenAI MTC](https://docs.google.com/document/d/1-EQXY84vjgjMFPzeaxN7udhit1cqvY7-2Pus9W94icg/edit?usp=sharing) is an example where a Real Time service was built to provide metadata to reduce GenAI compliance risk and friction

## Definitions

- **SLA1**: Annotation coverage of Hive tables within 1 days.
- **Numerator**: Hive table fields with high confidence UII Bii predictions AND that had assignments or disagreements in less than 1 days (counting since the Bii predictions landed).
- **Denominator**: Hive table fields with high confidence UII Bii predictions.
- [**UPP**](https://www.internalfb.com/wiki/Privacy_Data_Engineering/Privacy_Infra_DE/Unified_Prediction_Pipeline_%28UPP%29/): Unified Prediction Pipeline (UPP) is a framework that is made of 3 Dataswarm Pipelines (signal collection, annotation collection, prediction reconciliation) which provides predictions across 5 annotation types and 47 asset types
- **RTUP**: Real Time (RT) Unified Prediction (UP) service which should provide annotation predictions faster than UPP and would be informed by the decisions on this doc

## Solutions

### Entry Point

There are two existing entry points that make predictions on different populations of hive tables. Eventually the hope would be that the scope of RTUP would expand beyond hive.

#### Dataswarm UPM Diff Time ([Real Time UPP for Rich Type](https://fb.workplace.com/groups/1380785639188244/permalink/1801047017162102/))

This approach listens for tester runs in Dataswarm UPM Dataset diffs - if there is a tester run then we push to Bii via the [Real Time API](https://www.internalfb.com/code/fbsource/[b98dbd2876d6]/www/flib/intern/privacy/bii/real_time_predictions/BiiRealTimePredictionsAPI.php?lines=68) for a scan of a random sample of 1000 rows from each table. Then the Bii results are processed and predictions are made, see [design](https://docs.google.com/document/d/13wh2ELX_x7zSrhmobA_FSSa3YA912VV_sWyb3QKv82U/edit?tab=t.0).

#### Table Creation ([GenAI MTC O2](https://docs.google.com/document/d/1-EQXY84vjgjMFPzeaxN7udhit1cqvY7-2Pus9W94icg/edit?usp=sharing))

This approach listens for [Bii RTE events](https://fb.workplace.com/groups/531972396985049/permalink/2820743314774601/) at table creation time and makes predictions for GenAI metadata like guard columns, attachment columns, modality and data type. This approach could be extended to make predictions for Rich Types, Actor, etc.

#### Tradeoffs

| Entry Point | Technique | [Hive Table Coverage](https://fburl.com/daiquery/spos37ez) | Risks |
| --- | --- | --- | --- |
| **Dataswarm UPM Diff Time** | **Push to Bii RTE** | Overall: <7.39% / Bii Semantic User: <18.2% / Bii Actor User: <14.7% / Dataswarm: <67.8% / Dataswarm UPM Dataset: <100% / Note: [~44%](https://fburl.com/daiquery/u39buznq) of the relevant diff versions (non-codemod) have a tester in the test plan | Coverage is limited to Dataswarm UPM Dataset backed tables / Currently there's a 1000 row scan, that may not be representative of the production data |
| **Table Creation** | **Listen to Bii RTE** | Overall: 54.7% / w/ Bii Semantic User: 41.8% / w/ Bii Actor User: 35.1% / Dataswarm: 82.3% / Dataswarm UPM Dataset: 88.9% / Note: Once fully rolled out for other namespaces (planned by EOY25), currently GenAI / MonCR scope | Coverage will be informed by Bii's filtering and that may change / If the scan happens on an empty table then there is nothing to make predictions on |

### Prediction Implementation

Regardless of the Entry Point, we will need to decide how to process these near real time signals and turn them into annotation predictions. As we already have a batch system (UPP) that applies to many surfaces including Hive (with a high level of coverage) we will need to consider the tradeoffs in how we implement the RTUP system and how it interacts with UPP.

#### Implementation Requirements

The following table covers the work that would be required on the RTUP and UPP side depending on the implementation method.

- **SQL**: RTUP uses UPP SQL prediction logic, UPP remains more or less the same
- **Python**: RTUP implements prediction logic in Python, UPP migrates to the new Python prediction logic
- **Python & SQL (Systems Diverged)**: RTUP and UPP prediction logic are disconnected. RTUP implements prediction logic in Python, UPP remains the same (SQL)

| Method | RTUP | UPP (Batch) |
| --- | --- | --- |
| **SQL** | Place real time signals in a common table and execute existing UPP SQL prediction logic | Nothing changes* |
| **Python** | Process real time signals with Python versions of the batch predictors to make predictions | Migrate to new RTUP Python logic via PythonOperatorV2 or PySpark |
| **Python & SQL (Systems Diverged)** | Process real time signals in a separate real-time service (Python) to make predictions | Nothing changes |

*There may have to be investigation into this - does UPP make assumptions about some signals always being populated?

#### Implementation Tradeoffs

| Method | Benefits | Risks |
| --- | --- | --- |
| **SQL** | Ensure prediction logic alignment with UPP / Little to no effort required to implement prediction logic for RTUP | Effort required to place signals into format expected by UPP / Need to restructure the UPP into "one query" to be runnable / RTUP potentially high latency / failure rate (presto query queuing) if going with solution #3 |
| **Python** | Batch UPP and RealTime UPP have logic synced / More natural (no need to convert to batch format) to implement for a Real Time / Faster execution for Real Time | Effort required to migrate all relevant UPP predictors / Incur risk associated with migration to the system that is providing all annotations today / Significant effort required to duplicate logic from UPP in Python |
| **Python & SQL (Systems Diverged)** | No effort required from UPP / Faster RTUP MVP | Changes to UPP / RTUP would need be made to both systems, which needs to be synced / Higher level of effort required to monitor disagreements between systems |

#### Implementation Strategies

| Option | Name | Method | Divergence | Batch Run | Real Time Run |
| --- | --- | --- | --- | --- | --- |
| **1** | **Real Time UPP (SQL, Python_impl)** | Python | Yes | Same as existing Batch UPP | We run the PythonImpl of each predictor / getPythonImpl: Python logic implementation (not fully implemented) |
| **2** | **Streaming** | SQL | No | Same as existing Batch UPP | Load small batches (every 10m) / Run UPP predictions on these batches |
| **3** | **Common Table** | SQL | No | Same as existing Batch UPP | Run UPP on Real Time signals in CTE |
| **4** | **Python RT service, separate from SQL** | SQL + Python | Yes | Same as existing Batch UPP | We run the Python real time service listener / For real time, we implement an event router listener and then implement logic that likely diverges from the SQL pipeline |
| **5** | **Python Everything** | Python | No | Implement PySpark to run Python logic (shared) | Real time service runs Python logic (shared) |
| **6** | **Python Configs** | Python | Yes | Python Config would be parsed and a SQL Generator would provide prediction logic | Python Config would be parsed and a Python generator would provide prediction logic |

### Application Methods

#### UPM Dataset Code Patch

A prediction is made and if it differs from the existing annotation it surfaces a suggestion in the UPM Dataset diff. If the user accepts the suggestion or adds the suggestion manually we can consider this a successful application.

#### Codemod

A prediction is made and transient/UPM Dataset Codemods are generated, for high confidence they are autolanded and for low confidence they are sent to asset owners for review.

#### Agentic Annotation Application

A prediction is made and available for consumption for an agent to apply the annotations interactively via a recipe, surface as an MCP Tool in DevMate, or as a stacked diff.

#### Application Method Options

| Application Method | Annotations | SLA | Benefits | Risks |
| --- | --- | --- | --- | --- |
| **UPM Dataset Code Patch** | Rich Type | 0 Days | Privacy tasks are more likely to be avoided if there are workstream linters that flag based on accepted annotations | Coverage is limited to Dataswarm UPM Dataset backed tables |
| **Codemod** | Rich Type & Actor | 0-2 days | Can apply to assets other than Dataswarm UPM Dataset backed tables | Confidence for RTUP will need to be tuned properly to ensure autolanding |
| **Agentic Annotation Application** | Rich Type & Actor | 0 days | Privacy tasks are more likely to be avoided if there are workstream linters that flag based on accepted annotations | Improper annotation application from agents could lead to SEVs, data loss, etc. |

## Considerations

### Coexistence

Both of these systems will be annotating Hive datasets and may be at risk of having different prediction output.

| Risk | Description | Mitigations |
| --- | --- | --- |
| **Signals** | RTUP will at least at the start have a subset of signals available, and potentially have differing signals (RTUP will have a smaller subset of data than UPP) | Assign proper confidence levels for RTUP / Prioritize signal buildout that best improve quality |
| **Prediction Implementation** | If it's chosen to have different prediction implementations between RTUP and UPP we are incurring a high risk of prediction divergence given the same input | Don't choose an implementation that has diverged prediction implementation |

Besides the difference in prediction output there are open questions relating to what we do if we've applied a RTUP prediction but UPP disagrees over time. Below are some options to consider:

- **Overwrite**: UPP overwrites RTUP prediction if there's disagreement
- **Do Nothing**: RTUP prediction remains if there's a disagreement

### Maintainability

If the prediction implementation is diverged then there will be a higher cost associated with maintaining tests to ensure there's little to no drift and it will increase the urgency of measurement to ensure that any drift missed by tests are surfaced.

## Appendix

- [Table-Creation Shift-Left, DU infra for AIDR Planning H1 2026](https://docs.google.com/document/d/1TNBIGpfug3eLQwgpyH_MWUgc5oySFYIXLRIMhzYVT1A/edit?usp=sharing)
- [[Shift Left] Real Time UPP Rich Type Suggestions](https://docs.google.com/document/d/1y0KWZJ_5uE_E4-9FQEmaU5wNG3qG5he5NlKfnr-pcho/edit?usp=sharing)
- [Shift-Left UX + Real Time UPP Performance Analysis](https://docs.google.com/document/d/1XUtRhAskiPifXgpEasy2CpvyFbdiZt9_x_HQOQ9xQuM/edit?usp=sharing)
