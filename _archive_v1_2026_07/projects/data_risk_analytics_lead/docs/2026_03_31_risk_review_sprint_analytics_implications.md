# Risk Review 8-Week Sprint: Implications for Analytics

## What's happening

The Risk Review org is running an 8-week sprint (starting ~4/2) to deliver a fully agentic Risk Review experience across all Areas. Four pods — Forest (replacing DTs), SIN automation, Verify & Implement, and Escalation Prep — will operate as one team with dedicated SMEs from each Area. Abhishek Gulati owns system decisions; Risk Review SteerCo is retired.

## What's changing on goals and metrics

**All legacy improvement goals are being sunset.** Jeb's post is explicit: teams are no longer expected to improve the legacy system, and goals tied to legacy improvements are deprecated. This includes:

- Regrettable SIN / regrettable triage
- Risk Identification Rate (RIR)
- Triage without Escalation (Tw/oE)
- EO NA rate

The only legacy expectation is **don't regress** — if the current system breaks, teams respond.

**New sprint KRs replace them:**

| KR | Metric | Target |
|---|---|---|
| Forest | Missed risk rate | <5% |
| Forest | SIN routing rate | At or below DT baseline |
| SIN automation | Agentic SIN handling | >75% |
| SIN automation | Escalation recall | >95% |
| SIN automation | Unnecessary escalation rate | <10% |
| Verify & Implement | Reviews with no EO manual effort | >2x current |
| Verify & Implement | Insufficient evidencing rate | Flat |
| Escalation Prep | Prep cost reduction | >50% |
| Escalation Prep | Automated decisions | >10% |

These are described as 50/50 goals — intentionally ambitious.

## What should continue

1. **SIN reviews and escalations** in at least their current form. The sprint goal is to automate most SIN, but human review stays for true escalations. Where Areas have ongoing prompt/agent work, those learnings are a useful input into the central agentification — especially ground truth and evals work.

2. **Mature Requirements and Mature Controls.** These goals should stay or increase. Mature reqs are load-bearing for Forest and Verify & Implement (AI can only evaluate against well-defined requirements). Mature controls reduce the need for manual implementation regardless of the operating model. This investment pays off whether the sprint succeeds on schedule or not.

## What can pause

1. **Risk ID process investment** (RF/Req attachment). Forest is explicitly replacing Decision Trees — 100% migration is the KR1 target. Investing in the current Risk ID process is investing in something being actively superseded.

2. **Legacy process metric improvement.** Per Jeb, maintain but don't invest in improving. Monitor for regression only.

## Recommendations for Analytics

**Shift focus to fast, reliable outcome-based e2e measurement.** The sprint KRs all require measurement infrastructure that either doesn't exist yet or needs to be made robust enough to validate an AI transition. Specifically:

1. **Instrument the new sprint KRs.** Forest missed risk rate, SIN agentic handling rate, escalation recall/precision, EO effort reduction — these need reliable, auditable measurement. This is the proving ground for whether the sprint succeeded.

2. **Strengthen audit-based metrics.** Multiple KRs benchmark against audit outcomes (missed risk rate, insufficient evidencing rate). Audit measurement is the primary defense-in-depth mechanism validating that AI is "as or more effective than the system it is replacing."

3. **Close gaps in e2e measurement.** Any breaks in the measurement chain — between Forest output, SIN routing, SIN decisions, verification, and audit results — undermine the ability to evaluate the sprint and make post-sprint ownership decisions.

4. **Move legacy metrics to maintenance mode.** Keep them running to catch regressions, but stop investing in improving coverage or granularity for metrics tied to the old process.
