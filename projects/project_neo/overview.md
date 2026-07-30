# Project Neo — Overview

_Last updated: 2026-07-27_

## State

**Active — A/C PRIV — Tier 2/3 handling required — docs ingested 2026-07-27.** Facebook unifying 4 divergent profile types (Main, ProMode, Pages/AP+ and SOAPs) into single-owner profile with 3 modes Personal/Creator/Business (flag, not fork) like IG Pro. M1 Test Dec '26 / Global Q1 '27, M2 Opt-in Q2 '27 Forced Q3 '27, M3 Q4 '27+ large enterprise migration Pages sunset. Status Red per SteerCo Jul20 — 3 months to code complete, 56 BIS funded / 68+ BIS unfunded M1 +31+ M2/M3.

Plan of Record: **Option 1 — FB Neo will be included in Meta Account as profiles and subject to all Meta Account commitments** (SNA/LPA, AI Training Opt-Out, Data Combination CASD/XSU, Unlink SLA 24h). Pages previously out-of-scope as multi-owner business entities, but Neo single-owner breaks rationale. Option 2 (separate Professional section) not viable.

Key risk: User Data scope erosion by blurring user vs user-as-business (UIBC), Business Linking GDPR XL 50-60 eng months, SNA/LPA $12-550M 28d revenue at risk (realistic $12-43M), AI Training opt-out 2.3% active Pages, T&C Balanced Consent +30-day notice + regulator briefings, iRev -0.5% drop mitigated 6mo + **+3.8% DAP claim is ceiling not loss avoidance — grounded 0.7-2.1% current incremental via second accounts kept under status quo, would only be lost if full ban enforced (hypothetical, not real proposal). Real proposal is relax SUMA + real name (16pLS0t), not block.**

## Privacy Handling

- **This file (Tier 1):** Only scaffold, links, TLDRs, non-sensitive plans. No restricted / A/C priv details — link only — per CLAUDE.md. All 8 docs fetched on demand via knowledge_load, summarized to TLDR only.
- **Tier 2:** Google Drive/Docs — founding docs, sensitive details — stored natively in Drive, fetched via `meta` CLI when needed, NOT saved fully here.
- **Tier 3:** `private/project_neo/` gitignored local-only if needed — never pushed.

## Stakeholders

| Person | Role | Context |
|--------|------|---------|
| Tony Harper | Owner / Data Risk | Ingested 8 docs 2026-07-27, assessing User Data scope erosion, XSU/Competition, Deletion |
| Bunmi Ayeh Nalbantis + Shashwat Gupta | Decision Leads, Competition / User Data | FB Neo Profiles + Meta Account Commitments PoR Option 1, Risk Assessment Jul27, Classification of Business Data |
| Shashwat Gupta + Bunmi Ayeh Nalbantis | Decision QBs, Business Data Classification | Should we continue using page_id + admin_id post-Neo? Options 1-3 |
| Tina Adams + Alexis Cotton + Yifei Tang + Iosef Kaver + Kaushik/Chandra | PM/Design/EM/TL/TPM, Product | Canonical operating model, M1-M3, Product principles |
| Ashu Khaitan + Kwabz Osei-Larbi + Julie Chen | Risk + Growth | Meta Account Representation, AC commitment AC Representation decision week of 7/20 |
| Sarah Sosiak | Monetization | Risk Assessment Monetization POC, SNA/LPA decision (Ads) |
| Bruno Caiado + Anna South + Ethan Pollack + Ryan Begley | Monetization / Competition / Deletion | Biz Linking safeguards (Bruno), SNA/LPA consent (Anna/Ethan), Deletion/Retention (Ryan) — downstream risks |
| Ivan Prikhach + Venessa Lobo + Yoonho Kim + Roxy Wang | Data Model | Logger + warehouse impact, DAU grain voice vs acting_account, dim_all_users refactor |
| Oleksii Aleksandrov + Manush Patel + Harper Ma + Gasser Abdelhamid + Alex Kagan | UIBC / Actor annotation | UIBC understanding 866k assets (72% Business only, 21% UIBC only, 7% both), DST vs XSU vs Deletion consumption — Q3 roadmap |

## Key Docs (link + TLDR only — no full copies for a/c priv) — 9 docs ingested 2026-07-27

| Name | Description |
|------|-------------|
| [North Star Deck — Re-Think Presence](https://docs.google.com/presentation/d/16pLS0tApKCaAjhM9u0Q8nr_NCzj7J5H01rnlyavgB4g/edit?slide=id.g39f7e454829_0_497#slide=id.g39f7e454829_0_497) | Apr 26 Tom-approved vision — unified account model flag not fork, 4 divergent types to 1, pillars display name flex + multi-account SSO + mode switching + single owner + AC — benefits claimed +3.8% DAP (see DAP note: ceiling not expected) |
| [Wanted SUMA Sizing — source of 3.8% DAP](https://docs.google.com/document/d/1OBtggooaqOnt8EujbUuJL_3TVPzEoOTvYxdcd2iS660/edit?tab=t.0#heading=h.8iccchinqrcf) | Yiwen Guo / Lan-Vy Ngo / Priya Gaur MAA — 188M people 2 accounts monthly = 0.7-2.1% DAP today (child-only activity), IG 26% → FB ceiling 22% = +14.2pp * 0.25 ratio = 3.8% ceiling — blocking is hypothetical counterfactual for sizing, real proposal is relax SUMA + real name (remove Reg redirection, build Switcher + logged-in creation) — confidence LOW, no owner, no backtest, Pages 437M not adjusted, ratio won't hold when overlap increases — grounded use 0.7-2.1% as current not threat, 3.8% as ceiling not expected — see private note `private/project_neo/dap_note_for_eng_leadership_2026_07_27.md` |
| [Canonical — Project Neo Operating Model](https://docs.google.com/document/d/1OKqJk_yGHwD3A_5i3i6h02BHFTEXA0Z5efEWoAN-Ttg/edit?tab=t.0#heading=h.fg6cxifxyhgc) | 490KB 10 tabs — M1 enhanced Creator/SMB + ProMode migration, M2 large entity Page creation removed, M3 Pages sunset, Product principles single owner + hybrid compliance + TrueBlue + name flex + friending, Blockers WS1.4 Integrity 35-60 BIS, WS2.5 BAI Biz Linking 50% Buena, WS2.4 Monetization PCA 1-1.5 BIS |
| [SteerCo Jul20 Status Update](https://docs.google.com/document/d/1-btnT4rbgvoz5EDg9ivoUQUZH2uEn_ViDb1uaJOzobU/edit?tab=t.mufvn12ddpsd#heading=h.4fxhsyivimqb) | M1 Red — 3 months to code complete for Dec test, 56 BIS funded / 68+ unfunded M1 +31+ M2/M3, dogfood 92% Creator vs ProMode parity 90% Biz vs AP+, XSU consent checker POC putting Biz out-of-scope, privacy boundary hard enforcement POC |
| [Data Model Changes](https://docs.google.com/document/d/1uFjRAGPAnxRkDZ0jSsZ8uFEeWjTcRb2M3MNdkmc2q5c/edit?tab=t.0#heading=h.7oa4mpxmbahi) | POC Ivan/Venessa — DAU grain acting_account → voice/Neo Account, dim_all_users → voice grain, dim_fb_account → acting_account, dim_fb_profile deprecated with shadow macro, Options table 4 options (new account field recommended) |
| [FB Neo Profiles and Meta Account Commitments (A/C Priv)](https://docs.google.com/document/d/1Ewohc4kKAr5qgT4-gyK1TCaGfdaKqyX-tuYIXk75fro/edit?tab=t.44jbf8y1giso#heading=h.ft774swqm5y6) | PoR: Option 1 — FB Neo as profiles in Meta Account subject to all commitments (SNA/LPA, AI Training Opt-Out, CASD/XSU, Unlink SLA 24h) — Pages previously out-of-scope, Neo single-owner breaks rationale, Implications $12-550M SNA/LPA (realistic $12-43M), AI opt-out 2.3% Pages, biz linking risk 50-60 eng months |
| [Classification of Business Data (A/C Priv)](https://docs.google.com/document/d/1BbBd2V_2TNPFVhQKnkmDsHGlYW_pBQgngLdCvOhXik8/edit?tab=t.7nt4fkqcugxa#heading=h.4ou9h1x84l9a) | Decision: Should we continue page_id + admin_id as business identifiers post-Neo? Over-classification risk, 60-day Page-TTL proposal |
| [Risk Assessment — Project Neo (A/C Priv)](https://docs.google.com/document/d/1fWxp7bg_KLg6tSEQdPB4iz3yQzl4RpaN9HfYMbqzgl8/edit?tab=t.0#heading=h.dsyxla8boop) | Jul27 High Level Risk Assessment — Monetization -0.5% iRev temp + SNA -0.13%, User Data scope erosion, T&C high, Competition XSU 9wks CASD 5wks Unlink 2wks + GDPR biz linking XL 50-60 months, Deletion XL |
| [UIBC Understanding 29 July](https://docs.google.com/document/d/1QJ1VkVpl8jwlwdETFPiYnlmzX_z5Bl9i7m8v6Ng_JLE/edit?tab=t.0) | 866,508 assets — 72% Biz only, 21% UIBC, 7% both — DST vs XSU vs Deletion inconsistent — Q3 POC Gasser/Harper Ma |
| [DAP Benefit Assessment — private, Tier 3](https://www.internalfb.com/intern/staticdocs/mystuff/) | `private/project_neo/dap_note_for_eng_leadership_2026_07_27.md` — Tier 3 gitignored — grounded view: 0.7-2.1% kept under status quo, would only be lost if full ban (hypothetical not real, real is relax), 3.8% ceiling not expected, no owner, need backtest + Pages adjustment + precision |

## Open Threads — Data Risk implications

- [ ] Business Data Criteria Decision — Option 1 continue page_id+admin_id vs Option 2 only if Professional mode vs Option 3 drop — impacts XSU, Restricted, Deletion — owners Shashwat/Bunmi — review with Subrosa + BII
- [ ] UIBC definition — shall we have UIBC distinct vs Business vs User? — 866k assets inventory — DST vs XSU vs Deletion inconsistent consumption — need ground truth, quality measurement Q3
- [ ] Meta Account PoR Option 1 — implications: SNA/LPA $12-43M realistic at risk, AI opt-out 2.3% Pages, Data Combination context-dependent (Personal in-scope XSU, Creator starts in-scope reclassified to business based on activity, Business out-of-scope), Unlink SLA 24h personal linking safeguards vs business linking gaps — need follow-on decisions
- [ ] Data Model grain shift — voice vs acting_account — dim_all_users refactor + shadow metrics M1-M3 via restricted macro + is_acting_account column — backfill coalesce logic error-prone — affects XSU checker POC and Deletion
- [ ] Timeline risk — M1 Red, 68 BIS unfunded — stress-test workback + federation costs across PPGs
- [ ] Link to H2 goaling and Q3 roadmap execution — tie to risk_data_ai_enablement Phase 2 (Semantic Models, Repo Context, Evals need update for new actor labels)

## Key Metrics (Tier 1 only — actual numbers sensitive, store TLDR)

| Metric | Baseline | Target | Note |
|--------|----------|--------|------|
| iRev impact — Pages migration | 0 | -0.5% temp 6mo | Expected mitigated, M2/M3 value in monetization audit |
| SNA/LPA revenue at risk 28d | $0 | $12-43M realistic ($12-550M upper) | 7.2M Pages all CAAs SNA/LPA lower bound $12.15M, half+ $43.45M, at least one $550.1M upper unlikely |
| AI Training opt-out Pages | 0 | 2.3% active Pages, 0.33% Page posts | 1.59M 28d active of 13.78M potential |
| DAP uplift from name flex | 0 | +3.8% topline DAP | From North Star deck |
| DAU uplift streamlined registration | 0 | 1-3% DAU | Plus 2-3x AI dev efficiency unified code |
| UIBC/Business assets | 866,508 total | 72% Biz only, 21% UIBC only, 7% both | No precision/recall measurement yet — Q3 roadmap |
| Eng cost — Biz Linking GDPR | 0 | 50-60 eng months XL unfunded | 100+ BP paths, L1 mid-Aug, need BSuite to build |
| XSU/CASD/Unlink | 0 | 9wks / 5wks / 2wks | Risk team to bring Account Center commitments in scope for Neo |
