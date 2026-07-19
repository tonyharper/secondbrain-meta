# Initial Document Review — Data Risk Analytics Lead

**Date:** 2026-03-26
**Documents reviewed:**
- [UDI Strategy One-Pager](https://docs.google.com/document/d/1pkztS1chLSbywtnXjXHI6wodcMvl6FB2tjdNDWity3s/edit)
- [Competition RAGL x ERPL Check-In (March 2026)](https://docs.google.com/document/d/1sXZHzdJP4UTr13GYhX5IBCM0TUwSh4bmL6E-yDhZnmU/edit)

---

## UDI Strategy One-Pager

### Summary

UDI's Q2 2026 strategy covers 5 workstreams with ~24 FTE investment. Core mission: inventory and classify user data storage for FTC consent decree compliance, and provide high-accuracy metadata that downstream risk areas use to avoid false positives and overenforcement.

### Key takeaways

- **Massive cost reduction underway.** Continuous compliance cost from ~9 FTE to ~2 FTE by EOY; federated work from ~2.5 EY to <0.5. Bet is on AI-driven operations replacing human-driven federation.
- **Neo-cloud is an emerging risk.** MSL expanding into neo-cloud/hybrid environments. Building cloud provider register, targeting 90% coverage of top 3 highest-risk providers by end of Q2. Only ~2.5 FTE allocated.
- **Classification accuracy drives enormous partner value.** ~9 EYS savings for Audit-Based Closure, HiveAnon deprecation ($15M compute saving), MSL training data retention expanded 45d to 3yr. ROI: 433% (Deletion), 2100% (ABC).
- **AI-native classification is early.** Prototyping toward RAIAF Stage 2+. Timeline ambiguous (EOY 2026 to H1 2027).
- **OneCatalog being rethought.** Current UI-centric model won't survive agent-driven workflows. Strategy investment only (0.5 Eng + 0.25 PM).

### Concerns

- Assessor risk: material safeguard changes (AI-driven compliance) need assessor alignment. Pushback could derail cost reduction plan.
- Unexpected MAPs could divert resources from cost reduction trajectory.
- Tension between partner trust (Workstream 3) and acceleration of cost reduction/AI-native classification (Workstreams 1, 4).

### Where analytics should lean in

- **Classification accuracy measurement** — false positive rates, coverage gaps, accuracy by annotation type (DST, Actor, Semantic/Rich Type)
- **Cost reduction tracking** — FTE/EY trajectory, are AI gains materializing?
- **Neo-cloud coverage** — coverage percentages across providers and environments

---

## Competition RAGL x ERPL Check-In (March 2026)

### Summary

Monthly operating review for Competition risk area (CDU, CPDP, Cross-Promotion). Covers AI progress, goal updates, control maturity, internal/external pressures, and roadmap status.

### Key takeaways

- **Competition is heavily AI-invested.** 94.7% AI-First WAU, 93% diffs AI-assisted, 98.8% code AI-generated. Multiple AI agents deployed: CDU risk agent, Decision Agent (50% cost reduction), SIN Agent (85% accuracy, 95% risk recall), XARC (upstream risk detection), Audience Management Agent, XSU SupportMate, Handoff Agent.
- **Goal acceleration.** Most H1 goals now targeting May completion. Only Threads XSU and XSU Phase 2 rollout expected to slip to June.
- **Operational verifiers at 31%** (down from 60% in Dec '25). P0 goal, behind target.

### Concerns

- **External pressure is intense and multi-fronted:**
  - AI x Competition: investigations in 4+ markets on anti-competitive intent. Significant business impact if forced to allow 3P AI growth or freeze AI features on FoA.
  - WhatsApp x Meta data sharing: regulatory actions in India, Brazil, Nigeria, Uganda (contagion). India Supreme Court hearing on CCI ads ban.
  - CCI/NCLAT (India): new concern on user data definition re: anonymization and aggregation.
  - DMA designation: Meta AI 40-50% likelihood in 12 months. Catastrophic case: foundation training in scope.
- **CDU safeguarding assumptions invalidated by AI tools.** Proliferation of AI tools (Manus, Nest, Analytics Agent) broke assumptions about human involvement, technical skill requirements, and analytical surface concentration. New multi-layered approach being built but early.
- **Staffing strain.** Team spread thin from central AI initiatives. Two departures.
- **Threads XSU rollout at risk.** Multiple SEVs triggered deployment lockdown, may push Phase 2 to Q3.

### Control maturity snapshot (as of 3/21/2026)

| Metric | Overall | CPDP | CDU | CP |
|--------|---------|------|-----|-----|
| Control Maturity (target >95%) | 92.59% | 90.9% | 100% | 80% |
| Requirement Meeting Min Bar | 100% | 100% | 100% | 100% |
| LaMa Triage w/o Escalation | 54.5% | 54.5% | 100% | N/A |
| Risk Identification Recall | 86.26% | 86.57% | 100% | N/A |

### Where analytics should lean in

- **Control maturity tracking** — which requirements are red/yellow, path to green
- **Risk Flywheel metrics scrutiny** — "Triage w/o Escalation" dropped from 90% to 57%, Risk ID Recall at 86% with 71.4% false positive rate in audit. Are definitions and measurement reliable?
- **AI agent effectiveness measurement** — eval frameworks, accuracy tracking, Ground Truth quality
- **External pressure monitoring** — regulatory actions, investigation timelines, compliance readiness across geos
- **CDU safeguarding for AI tools** — defining "safe" and measuring safeguard effectiveness

---

## Cross-cutting themes

AI is simultaneously the biggest opportunity and biggest risk across Data Risk. UDI bets on AI to slash compliance costs. Competition uses AI agents to accelerate decisions. But AI tools create new risk surfaces (CDU safeguarding) and AI products drive the most intense regulatory pressure (DMA designation, 3P AI on WhatsApp).

## Recommended first moves as analytics lead

1. **Get a unified view of control maturity and requirement compliance across all Data Risk areas** — fragmented today
2. **Own the AI agent effectiveness measurement story** — Ground Truth, evals, accuracy tracking
3. **Build the regulatory pressure tracker** — single view of where things stand across geos and risk areas for Oliver and Arash
4. **Understand what measurement exists today and where the gaps are** — before building anything new
