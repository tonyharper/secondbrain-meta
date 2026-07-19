<!-- Source: https://docs.google.com/document/d/1y0KWZJ_5uE_E4-9FQEmaU5wNG3qG5he5NlKfnr-pcho/ -->
<!-- Title: Realtime UPP Rich Type Suggestions -->
<!-- Date Accessed: 2026-03-31 -->

# [Shift Left] Realtime UPP Rich Type Suggestions

## TLDR

- There have been [192 Rich Type suggestions (0.9% of predictions](https://fburl.com/daiquery/et5c95ds), [5.0% of non-empty predictions](https://fburl.com/daiquery/8wdie8qz)) made by Realtime UPP overall as of 10/29. Given this low suggestion count, the current iteration has had little to no realized impact on Shift Left yet.

## Context

[Realtime UPP Predictions for Rich Type](https://fb.workplace.com/groups/1380785639188244/permalink/1801047017162102/) suggestions was launched on 09/22 with the goal of increasing data understanding coverage for assets linked to UPM Datasets produced by UPM Dataswarm Pipelines at authoring time.

Accurate Rich Type suggestions at asset creation time should enhance shift left and reduce privacy tasks (e.g. Deletion).

## Investigation

[Realtime UPP Predictions for Rich Type](https://fb.workplace.com/groups/1380785639188244/permalink/1801047017162102/) uses Code Suggestions in Phabricator Diffs as the mechanism to surface and ideally incorporate (if the author accepts) the predictions.

The predictions made by Realtime UPP are stored in [`EntSandcastleDatasetMutationAnnotationPrediction`](https://www.internalfb.com/ent_node_console/ent/EntSandcastleDatasetMutationAnnotationPredictionSchema) which has a field CodePatchSuggestionID which connects to the [`EntPhabricatorCodePatchSuggestion`](https://www.internalfb.com/ent_node_console/ent/EntPhabricatorCodePatchSuggestionSchema) and is the Ent that stores the information for the code suggestion. Both have hive dumps [`scrape_xdb_upm_upm_dataset_mutation_annotation_prediction`](https://www.internalfb.com/intern/bunny/?q=ht+scrape_xdb_upm_upm_dataset_mutation_annotation_prediction) ([pipeline](https://www.internalfb.com/code/fbsource/[2986202e392b89dff3cc917fa65e9e83ee52777b]/fbcode/dataswarm-pipelines/tasks/privacy/xdb_scrapes/xdb_to_scrape_config.py?lines=2220-2224)) and [`scrape_phabricator_code_patch_suggestion`](https://www.internalfb.com/intern/bunny/?q=ht+scrape_phabricator_code_patch_suggestion) ([pipeline](https://www.internalfb.com/code/fbsource/fbcode/dataswarm-pipelines/tasks/infrastructure/phabricator/scrape/scrape_phabricator_code_patch_suggestion.py)).

| Attribute | Real Time UPP Prediction | Code Patch Suggestion |
| --- | --- | --- |
| Description | Store metadata like the file path (UPM Dataset), column, prediction type (e.g. RICH_TYPE) and prediction value (e.g. PageID) and code patch suggestion | Store metadata like the code path, whether or not the suggestion was accepted, etc. Will be used for accept / decline / inaction rates |
| EntSchema | [`EntSandcastleDatasetMutationAnnotationPredictionSchema`](https://www.internalfb.com/ent_node_console/ent/EntSandcastleDatasetMutationAnnotationPredictionSchema) | [`EntPhabricatorCodePatchSuggestionSchema`](https://www.internalfb.com/ent_node_console/ent/EntPhabricatorCodePatchSuggestionSchema) |
| Hive Dump | [`scrape_xdb_upm_upm_dataset_mutation_annotation_prediction`](https://www.internalfb.com/intern/bunny/?q=ht+scrape_xdb_upm_upm_dataset_mutation_annotation_prediction) | [`scrape_phabricator_code_patch_suggestion`](https://www.internalfb.com/intern/bunny/?q=ht+scrape_phabricator_code_patch_suggestion) |

Based on analysis of these Hive Dumps only [0.9% (192) of Realtime UPP Predictions](https://fburl.com/daiquery/et5c95ds) have a Code Patch Suggestion.

When looking at a 30 row sample of the [`EntSandcastleDatasetMutationAnnotationPredictionSchema`](https://www.internalfb.com/ent_node_console/ent/EntSandcastleDatasetMutationAnnotationPredictionSchema) that has a non empty prediction value there don't appear to be any data gaps for the code patch suggestion field, but there do appear to be lots of predictions that are the same as the existing rich type (66.66%), bugs (16.66%) and unsupported API (6.66%).

| Has Code Patch | Reason | Example (Tracker ID, Diff Version, Extra) | Count (%) |
| --- | --- | --- | --- |
| Yes | Suggestion Surfaced in Diff | [1226852979232977](https://www.internalfb.com/id3/id/1226852979232977), [1312899170311160](https://www.internalfb.com/diff/D84070460?dst_version_fbid=1312899170311160&inline_id=1312908683643542) | 3 (10%) |
| No | Already Covered with predicted Rich Type | [1419352316430152](https://www.internalfb.com/id3/id/1419352316430152), [1969381543881301](https://www.internalfb.com/diff/D82989101?dst_version_fbid=1969381543881301) | 20 (66.66%) |
| No | Codemod Bug (Incorrect Type) | [1287560983144028](https://www.internalfb.com/id3/id/1287560983144028), [1161394262618413](https://www.internalfb.com/diff/D84474371?dst_version_fbid=1161394262618413) | 2 (6.66%) |
| No | Infra Bug | [1080735240546937](https://www.internalfb.com/id3/id/1080735240546937), [1673784186913865](https://www.internalfb.com/diff/D83509139?dst_version_fbid=1673784186913865), [failed workflow](https://www.internalfb.com/sandcastle/workflow/4395513236324216257/artifact/actionlog.4395513236499127803.stdout.1) | 3 (10%) |
| No | Unsupported API (column_from, table_as) | [768047292892444](https://www.internalfb.com/id3/id/768047292892444), [1671696540184075](https://www.internalfb.com/diff/D82249209?dst_version_fbid=1671696540184075) | 2 (6.66%) |

Additionally the assumed scope of these predictions is new columns (from new and existing datasets), however in 8 (26.66%) of the samples there were predictions on existing columns. Tracker ids for these are in the [sheet](https://docs.google.com/spreadsheets/d/1f1Ou11Kc98qW-aNh0uLUVQy8yYP46N5wUXl6SfDdAo8/edit?usp=sharing).

## Questions

- **[Data Gap]**: Is there a data gap; i.e. we are creating code patch suggestions but they are not being recorded in [`EntSandcastleDatasetMutationAnnotationPredictionSchema`](https://www.internalfb.com/ent_node_console/ent/EntSandcastleDatasetMutationAnnotationPredictionSchema)?
- **[Functional Gap]**: Is there a functional gap; i.e. we are not providing code patch suggestions because of bugs (e.g. incorrect type), rich types that don't differ from existing ones (from `./linter --update-schema`)?

## Conclusion

| Name | Data Gap? | Functional Gap? | Commentary |
| --- | --- | --- | --- |
| Katia Lopez | Yes, but minor | Yes | |
| Ria Garg | No | Yes | |
| Chetan Bhat | No | Yes | |
| Michael You | Real Time UPP is the engine that provides suggested annotation values (currently scoped to rich type but could include other like actor) provided a single data asset. This differs from batch in that it can be called online and is currently being used in Diff Suggestions. Having the ability to use this online should inherently allow us to shift left. | | See comments above about the functional gap |
| Colin Glaes | Problem Group | Problem | |

## Next Steps

### Real Time UPP

Real Time UPP is the engine that provides suggested annotation values (currently scoped to rich type but could include other like actor) provided a single data asset. This differs from batch in that it can be called online and is currently being used in Diff Suggestions as seen in the [Realtime UPP Predictions for Rich Type](https://fb.workplace.com/groups/1380785639188244/permalink/1801047017162102/) post, it could also be used immediately after table creation which is the plan for GenAI. Having the ability to use this online should inherently allow us to shift left.

The following table lists the opportunities for improving Real Time UPP ranked by relative impact.

| Problem Group | Problem | Solution |
| --- | --- | --- |
| Coverage Parity | Current Predictions are similar to `./linter --update-schema` (one hop propagation from upstream datasets) | Build out missing predictors that exist in Batch UPP |
| Coverage Parity | We're missing suggestions that could have been made and they result in privacy wave tasks | Build out missing predictors that exist in Batch UPP |
| Quality | We're suggesting rich types with incorrect underlying types (Str vs Int) | Ensure we're utilizing the correct version of the Rich Type (OculusUserID vs StrOculusUserID) |

### Diff Suggestions

We are surfacing the Rich Type predictions made by Real Time UPP via Diff Suggestions. The current implementation relies on a tester run to be attached to the diff we make suggestions on since Real Time UPP scans the test tables output from the tester run. Diff versions that are in the current scope for the Diff Suggestions show that only [~26.9%](https://fburl.com/daiquery/u39buznq) (as of 11/13) have tester runs.

The following table lists the opportunities for improving Diff Suggestions ranked by relative impact.

| Problem Group | Problem | Solution |
| --- | --- | --- |
| Coverage | This only covers Dataswarm, UPM Dataset backed datasets | Expand to additional surfaces (all Dataswarm, potentially outside of Dataswarm) |
| Coverage | Tester runs placed in Diff test plans are not 100% since even if a tester run was executed developers may not add them | Retrieve tester runs from a logger or ent for a diff instead of parsing it from test plan / **Risk**: Quality gaps arising from non-representative tester runs |
| Coverage | Some developers may never test their pipelines or never add it to test plan | Dump resolved queries from Dataswarm [`./linter`](https://www.internalfb.com/wiki/Dataswarm/Test_Pipeline/Linter/) or [`./tasks_metadata_exporter`](https://www.internalfb.com/wiki/Dataswarm-development/Components/Datacastle/tasks_metadata_exporter_Development/) and execute and pass those to Real Time UPP / Linter for Dataswarm |
| Coverage | Some developers will use backfills to test their pipeline | Utilize these production tables for scans |
| Engagement | Users are not accepting suggestions. There have been [7 suggestions explicitly accepted (from diff tool)](https://fburl.com/daiquery/hbdei2lz) so far with another [20 implicitly accepted](https://fburl.com/daiquery/3nnjbuk1) (added in VSCode) for new datasets | Consider changing to an opt out strategy where users can decline the annotations but if they don't they're automatically accepted |
| Coverage | UPM Datasets that use `column_from` or `table_as` are not supported | Enable support for column references, or potentially overwrite these |
| Coverage | There are infra errors preventing valid prediction from being applied | Investigate "Rich Type ID cannot be null for type id for prediction" errors and resolve |
| Quality | Predictions are being triggered for columns that aren't new. This isn't in scope and should not be happening | Ensure that predictions for non new columns are not created |

## Resources

### Sheets

- [Code Patch Gaps](https://docs.google.com/spreadsheets/d/1f1Ou11Kc98qW-aNh0uLUVQy8yYP46N5wUXl6SfDdAo8/edit?usp=sharing)

### Queries

- [Overall Prediction Suggestion Coverage](https://fburl.com/daiquery/406mmrcw)
- [Non-Empty Prediction Suggestion Coverage](https://fburl.com/daiquery/sdv1u9r9)

### Posts

- [[Shift-Left] Real-time Rich Type Predictions are now live!](https://fb.workplace.com/groups/1380785639188244/permalink/1801047017162102/)

### Docs

- [Shift-Left UX + Real Time UPP Performance Analysis](https://docs.google.com/document/d/1XUtRhAskiPifXgpEasy2CpvyFbdiZt9_x_HQOQ9xQuM/edit?usp=sharing)
