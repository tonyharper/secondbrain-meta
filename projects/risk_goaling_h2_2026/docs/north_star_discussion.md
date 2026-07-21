# Risk Org North Star — Discussion Doc Summary

_Source: https://docs.google.com/document/d/1iSxSzXVE4HI_bi__7r9bADtFNmC8gityFhzyXft2MhY/edit?tab=t.0_
_Title: [For Analytics & Research] Risk Org North Star_
_Owner: Stephanie Yee, created 2026-07-16, modified 2026-07-16_
_Date: June 15, 2026 discussion_

_Local: /tmp/doc2_full.html (7KB), /tmp/doc2_full.md (57 lines)_

## Purpose

Previously, we discussed North Star metrics in context of H2 goals — useful for near-term planning but doesn't connect to Risk org's actual north star, creating myopic mental model. Need shared mental model of north star to make right tradeoffs. This doc is strawman to spark discussion.

## Mission Translation

**Risk org mission:** _Instill responsible practices. Enable Innovation._

### Instill responsible practices = (1) meets obligations + (2) protects users

**Meeting obligations** = satisfy legally-required commitments + sufficiently reduce risk to Meta. Ideally measure:

- **Defensibility & resilience of current strategy and execution** – On requirement-by-requirement basis, understand (a) interpretation risk and where competitors stand; (b) how well we did it; (c) how future-proof status quo is.
- **External assessment and scrutiny** – Counts of enforcement actions, assessor marks, report acceptance.
- **Realized risk** – What slipping through cracks and how things fare when tested. Typically counter metrics, e.g., quantity of SEVs/Issues and regulatory finding/inquiries.

**Protecting users** = manage level of risk users are actually subject to + whether they trust Meta to manage it.

- **Actual risk** – Level of risk users are actually subject to. Currently measured via PRA, though externally-oriented quantification.
- **User trust** – Whether users believe we are protecting them. For Youth, Parental Alignment captures this already. Whether other areas need comparable trust measure is open question.

### Enable innovation = empower company to keep building

About _way_ company manages risk, not positions it takes or how positions impact users. Success = company operating in acceptable place in context of regulatory risk, without processes becoming bottleneck. Requires (1) reasoning about holistic cost of compliance and (2) monitoring efficiency of processes.

**Holistic cost of compliance** = what company gives up to stay in line with regulations:

- **Product opportunity cost** – Product capabilities company forgoes because of restrictions we impose.
- **Cost of compliance** – Direct cost of meeting obligations across company (federated work/waves, friction, operational expense, etc.). Measured in $ today, though more telling units are time and tokens.

**Efficiency of processes** = whether compliance happens with minimal friction, i.e., Risk org can manage risk at company's scale without becoming bottleneck. Underneath sits bet: systematize risk work and some level centralized tooling/process is preferable for PG experience and overall org efficiency. Need to capture:

- **PG experience of risk review** – Several metrics behind this:
  - Simple reviews should be frictionless.
  - More complicated reviews requiring escalation should be efficient.
  - Most product critical ("white glove") decisions should be timely and well-reasoned.
- **Team Defense's efficiency at 'processing' risk** – Conceptually, higher share of risk & compliance efforts (e.g., ARP, GRC) that are systematized rather than done by hand helps better manage risk.

## Appendix: North Star vs Half-over-Half Priority Metrics

| | North Star Metrics | H2 Priority Metrics |
|---|---|---|
| Horizon | 5+ years; stable | One half; reset each cycle |
| Tied to | Mission and vision | Current priorities |
| Scope | Whole picture, across every area | Selected subset we choose to move now |
| Changes when | Mission changes (rarely) | Priorities change (every half) |
| Used to | Orient strategy and measure overall posture | Drive and track near-term execution |

## Implications for H2 Goaling

- H2 Tier-1 goals should be seen as _priority metrics_ – subset we choose to push now – not the full North Star.
- Data Risk implications:
  - Defensibility & resilience: Mature positions for 7 priority areas (RD, Wearables, Cloud, Self-preferencing, Data In, Access, Anonymization) – directly addresses defensibility.
  - Realized risk: SEV prevalence, proactive interception, % requirements effective, self-evidencing controls – counter metrics.
  - Cost of compliance: Cost-of-compliance USD, PG compliance cost $/EY, created company value iRev – aligns to holistic cost concept.
  - PG experience: SINs under SLO, % Minimal LaMas, Unnecessary SIN rate, L1 Rate reduction – aligns to PG experience.
  - Team Defense efficiency: % controls agentic-ready, Agentic Review Share, automation % – aligns to systematized share.

- Open question from doc: Does Risk need trust measures beyond Youth Parental Alignment for other areas (e.g., Data Risk user trust)?

## Links to other docs

- H2 Goals v3 (Priority 1-4) – https://docs.google.com/document/d/1U9vrVFRO4A_jbi7QhhDbYdWv8n834gq3udR3M1KTjQQ – should be evaluated against this North Star framing – does it cover all concepts?
- Tier-1 Metrics sheet – https://docs.google.com/spreadsheets/d/1MCTfdFwYLl6VDrVthczHEd1OIQhMp1yRdjA9wY7pGFA – 118 rows are priority metrics, but North Star is stable longer term.
