# Access Request: Token Cost Data — Product Risk & Compliance

**Requesting team:** Risk Data Engineering

**Purpose:** ROI measurement for two compliance automation initiatives.

## Use Case 1: Risk Review System Account Cost Attribution

We need to calculate the token cost of system accounts like Risk Review to measure the ROI of automated review processes against the human workflows they replace. This requires visibility into token consumption for system accounts that operate outside our direct reporting chain. Without this data, we cannot quantify whether automation investments are delivering cost savings or identify where human review is still more cost-effective.

## Use Case 2: Privacy Task Automation Cost Comparison

We are evaluating the cost of completing privacy compliance tasks via LLM versus human effort. This requires measuring token costs for specific activities across Meta, not just within our org. The comparison is straightforward — what does it cost in tokens to accomplish a task that currently requires X hours of human work — but the data we need spans beyond our existing reporting chain.

## Why cross-org visibility is required

Both use cases share a common constraint: the accounts and activities we need to measure are not scoped to our team's reporting hierarchy. System accounts serve cross-functional workflows, and privacy tasks are performed across multiple orgs. Restricting access to our own reporting chain would give us an incomplete and misleading cost picture.

## What we'll do with it

- Build cost-per-action metrics for automated compliance workflows
- Produce ROI analyses comparing automation cost to human process cost
- Inform investment decisions on where to expand or pull back automation
