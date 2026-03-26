# UDI Strategy One-Pager

**Risk Area:** User Data Inventory (UDI)
**Date:** March 2026
**Source:** [Google Doc](https://docs.google.com/document/d/1pkztS1chLSbywtnXjXHI6wodcMvl6FB2tjdNDWity3s/edit)

---

## Mission

UDI defines, inventories, and classifies user data storage systems and assets to (1) ensure Meta meets FTC consent decree obligations for data storage in approved environments and inventorying user data, and (2) enable Risk Areas and product teams to meet their own compliance requirements efficiently through providing high-accuracy metadata — reducing compliance overhead and preserving product value by narrowing scope and avoiding false-positives.

## Workstreams

### 1. Reduce KTLO cost by closing defensibility gaps and automating continuous compliance

- **End State (EOY 2026):** RQ66914 & RQ66915 remain green with ~2 FTE (from ~9) continuous investment and < 0.5 EY (from ~2.5EY) of federated work
- **Why invest?** Current operational cost of continuous compliance is high, preventing effective re-allocation of resources
- **How?** Eliminate human-driven federation outside of edge-cases, mature AI-driven operations, adjust verifiers to check compliance outcomes over process adoption, drive proactive remediation of violations
- **Q2 targets:**
  - Met all MAP milestones and must-do compliance work, understood residual Safeguard risk and progressed proactive remediation
  - UDI cost of continuous compliance reduced to ~5.5 FTE (from 9) and federated work reduced to 1.75 EYS (from 2.5)
- **Q2 investment:** ~10 Eng, 0.5 TPM, 0.25 DE, 1 CW (expect investment to decrease quarter-over-quarter as AI gains materialize and MAPs close)
  - Eng investment split ~50/50 between must-do compliance and process-improvement/cost-reduction
  - Directionally expect ~5.5 FTE start of H2 and ~2 FTE by EOY, 1.75 EYS federated work start of H2 and < 0.5 by EOY
  - Frontload assessor communication/collaboration — need to connect into general programme for Risk

### 2. Continuous compliance for new computing environments

- **End State (Q3 2026):** Meta has aligned risk posture and continuously meets FTC inventory obligations for new deployments
- **Why invest?** With MSL expanding into neo-cloud and hybrid developments driven by compute needs, we risk failing obligations without proper inventory controls
- **How?** Align risk posture and compliance bar for user data storage in neo-cloud and hybrid environments, proactively identify risk and enforce requirements for new deployments
- **Q2 targets:**
  - Built register of neo-cloud providers and covered 90% of accounts for top 3 highest-risk providers
  - Enumerated 90% of covered cloud environments' assets with high risk of data storage
- **Q2 investment:** ~2 Eng, 0.5 DE (in collaboration with PAI Asset Observability in Cloud team)

### 3. High-accuracy user data classification for dependent teams

- **Success criteria** (ongoing, scoped to partner needs): Classification quality drives measurable EY savings and retains maximum product value for compliance partners
- **Why invest?** Gaps in coverage and accuracy lead to false-positives, wasted effort and overenforcement of requirements leading to data loss
- **How?** Improve coverage and accuracy across annotations (Data Subject Type, Actor, Semantic/Rich Type) through new signals (like lineage), Ground Truth curation, and continuous accuracy tuning. Leverage AI advancements from workstream 4 as they mature.
- **Q2 targets:**
  - Realised ~9 EYS for Audit-Based Closure (within FB monetization FAM) by adopting DST
  - Realised ~2.5 EYS, unblocked HiveAnon deprecation ($15M compute saving) and closed UGC coverage gaps for Deletion
  - Expanded MSL training data retention 45d to 3yr by improving non-user actor classification accuracy for training data
- **Q2 investment:** ~6 Eng, 1 DE, 0.5 TPM

### 4. AI-native classification and cross-Risk Group scaling

- **End State (EOY 2026 - H1 2027):** End-to-end classifier development has transformed from highly manual to human-in-the-loop, driving 2x-4x speed-up on developing new and tuning existing classifiers. New AI-powered UII-classifiers shipped in < 4 weeks (from ~8 weeks today) and continuous accuracy tuning becomes majorly automated with human-in-the-loop oversight
- **Why invest?** Classifying assets is labor-intensive, manual and bespoke across all stages of the workflow — can be massively accelerated by AI
- **How?** Build reusable framework (in collaboration with PAI & Risk DE) maturing all stages of end-to-end classification flow to RAIAF stage 3+, drive adoption within URD and across Risk Groups. Evolve classification strategy for changing assumptions about human-driven taxonomy, schema and metadata creation/annotation
- **Q2 targets:**
  - Matured both P0 JTBD (Ground Truth curation, new classifier development) to RAIAF Stage 2+, validated across 3+ use-cases in User & Restricted Data
  - Completed ownership transition of UII-related classifiers from PAI to UDI
  - Unblocked product launches for MFT, Spectra, Manus, Gismo with new/improved UII classifiers
- **Q2 investment:** ~5.5 Eng, 0.5 TPM, 0.5 DE

### 5. OneCatalog for agent-driven compliance

- **End State (EOY 2026):** OneCat acts as source of truth to agents for compliance-related asset metadata and allows humans-in-the-loop to perform high-leverage manual actions and required audits. Sense is that OneCat will be relevant for certain jobs but not all, and not in the form it exists today.
- **Why invest?** OneCat is an inventory of Privacy's entities and data, enabling teams to assess privacy implications and enforce compliance. Current UI-centric model will not meet demands in a world of agent-driven workflows
- **How?** Integrate MCP, drive discoverability through agent-integration, understand and modify/build highest-leverage workflows where full autonomy is undesirable or unlikely
- **Q2 targets:**
  - Updated strategy centered on enabling AI agent workflows and API integration in May
  - Made invest-divest decisions on workflows based on potential human-in-the-loop use-cases
  - Prototyped 1+ agent integrations by end of Q2
- **Q2 investment:** ~0.5 Eng, 0.25 PM

## Tradeoffs

By reducing investment in workstream 3 in Q2 we could either:
- Accelerate workstream 1, more quickly reducing operational burden to operate UDI Safeguards
- Accelerate workstream 4, more quickly maturing classification to be primarily human-in-the-loop

However investments in workstream 3 are:
- **Risk of breaking trust:** High priority P0 asks proactively raised by partners. ABC and Deletion asks were previously paused in Q4 scope transition. Not progressing them risks breaking trust.
- **High-leverage bets:** Strong ROI for Meta (433% ROI for Deletion EYS, 2100% ROI for ABC EYS)

## Risks

- **Material changes to Safeguards:** AI-driven process changes require assessor alignment
  - *Mitigation:* Front-load assessor engagement; connect to larger Risk workstream aligning overall narrative of AI shift for compliance
- **Unexpected MAPs:** Additional must-do compliance work could divert resources from cost-reduction efforts
  - *Mitigation:* Evaluating residual risk for potential severity; proactively addressing gaps perceived as high-risk to external defensibility
