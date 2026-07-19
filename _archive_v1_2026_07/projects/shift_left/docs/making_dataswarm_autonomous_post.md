<!-- Source: https://fb.workplace.com/groups/803837402998210/permalink/30652942740994282/ -->
<!-- Title: Making Dataswarm Development Autonomous with Claude -->
<!-- Date Accessed: 2026-03-31 -->

# Making Dataswarm Development Autonomous with Claude

**Author:** Evan Calzolaio
**Published:** 2026-01-27

## The Problem

We've all made a minor change to a pipeline that required us to sift through UPM logs, run tester, and possibly iterate (if we remember to check the chronos job status later). Then, finally, compare the test and prod table to make sure you didn't regress anything.

**What if Claude could just do that for you?**

## How It Works

In order to make the dataswarm development flow agentic, we need to connect four pieces:

1. **Code** (devmate/claude already do this well)
2. **Dataswarm tool use** (./status, ./linter, ./tester)
3. **Chronos awareness** (skills like [chronos-analysis](https://fb.workplace.com/groups/claude.code.community/permalink/894160979792690/) unlock this)
4. **Presto querying via CLI** (devmate/claude do this already)

Given these, we can capture most exceptions and data quality issues and feed them back into the agent such that it can iterate on the pipeline autonomously. Potentially saving us time on a pretty inefficient development workflow. [D91472318](https://www.internalfb.com/diff/D91472318?entry_point=20) is a practical example of some minor pipeline changes implemented and tested end to end with Claude, including final validation.

## Skills to Kick Off the Workflow

The challenge is keeping the agent focused and handling the errors and edge cases appropriately. This is where skills come in. Here are a few you can try:

1. **`/dataswarm-de-dev-loop <pipeline path>`** (authored by Evan, [D91229628](https://www.internalfb.com/diff/D91229628?entry_point=20))
   - A skill for end-to-end linting and tester workflow, explicitly using other skills to help round out and scale context
2. **`/dataswarm-pipeline <pipeline path>`** (existing skill, [D87863994](https://www.internalfb.com/diff/D87863994?entry_point=20))
   - A more general skill also attempting end-to-end pipeline authoring and testing

To invoke either of these skills you need to first install them:

```
claude-templates skill dataswarm-de-dev-loop install
```

## CTA

This workflow is still experimental, but **the core loop works**. Take a moment to try out either of these skills for your next dataswarm change and help iterate on them. We'll need to improve guidance for comparing output tables, tackle advanced testing cases (like running only a subset of tasks) and iterate on edge cases and common UPM errors.

Contributing to skills is straightforward and is mostly prompting and context. We can make this workflow nearly autonomous this half and it's something we'll be pursuing even further.

**tl;dr** -- There have been several LLM skills to tackling specific portions of the DE workflow, but the real efficiency gain will come from tying all of these tools together in an agentic workflow. Let's build that workflow!

## Setup Notes

1. Persist chronos CLI across devservers: `devfeature install chronos_scripts --persist`
2. Update your `~/.claude/settings.json` to allow executing the chronos CLI:
   ```json
   "allow": [
     "Bash(*chronos-*.sh *)"
   ]
   ```

## Notable Discussion Points (from comments)

- **DEmate plugin**: An existing plugin for Claude Code with skills, MCP tools, and automated validations. Install via `claude-templates plugin demate install` (use `--dev` for latest).
- **DETEX**: A separate tool focused on automating end-to-end testing for Dataswarm pipelines. Available as a Claude Code skill.
- **Test plan hallucinations**: A known challenge -- Claude can hallucinate test results. Mitigations include forcing CLI logging to tmp files and auditing commands run. A "trust but verify" approach with explicit query logging helps.
- **Linter skill**: May need manual re-save to trigger; can be added/updated as part of the workflow.
