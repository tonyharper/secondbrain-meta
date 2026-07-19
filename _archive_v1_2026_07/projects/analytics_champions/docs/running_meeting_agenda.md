# Analytics Champions Biweekly Meeting Agenda & Notes


*Workplace group: *[*https://fburl.com/workplace/lrzi9bwx*](https://fburl.com/workplace/lrzi9bwx)


*Feedback document - *[Running Document](https://docs.google.com/spreadsheets/d/1jQPACin7lWVRJlpCqFaWjhS7pvhYgBE2uxo-D0Ik63M/edit#gid=0)



Apr 1, 2026



- Proposal to update SME Champions Charter: [Evolving the Analytics Champions and SME Group Model](https://docs.google.com/document/d/1qzjQJRqZ4t1tlHr_TW_zBfgy-B2FxlNAGH3YqxM4RZc/edit?tab=t.0#heading=h.3qmm022v7xw6)
- Q1 DataEx Survey Results: [[Draft] DataEx | Central Efficiency Metrics Report | H1 2026](https://docs.google.com/presentation/d/1nO8SgB8HtKiaJHspgb1uiAQrFNoBdCHpFNw_xzTF0wg/edit?slide=id.p#slide=id.p)

Mar 13, 2026


- [Inform only] Reference; bunny lol “*aiadash*’ - AI for analytics measurement
  - On evals side, engaging with Bertram Chan and Olivia on measurement and merging some of the learnings and practices.
    - [Analytics Eval Quick Start Guide ](https://docs.google.com/document/d/1A0EQ24cI1eIvks2HEqicwoiYDixGK0_C8-sk2RzgwZk/edit?tab=t.0#heading=h.uj40jket91c2)
    - [Eval Measurement Framework](https://docs.google.com/document/d/1hA29hlUr3NkzeCLaNbwmqbJviz69tD3xxNEf3RVbpU4/edit?tab=t.0)
    - [AI4Analytics Eval Standards V1.1](https://docs.google.com/document/d/16pHEDLO2RkumBoyas3woVwDMZalTDNv6eFt5xte1tKE/edit?tab=t.fwkil9zcldg#heading=h.4khhgjlzwkq4)

- SME group relevancy (or need for reconfiguration?) as we make the AI transition 





- If you want to try out auto migrations it helps to try it from within [IG Data Apps Dogfooding](https://docs.google.com/document/d/1R60hvBVve6Hc8PYYPLZK7G_dUNfxDXjmYUSpWt8Cmas/edit?tab=t.0#heading=h.ae0x4yypvu84) even if you fork the dash to a new app before landing. 
- The SOTA for automatic migrations looks something like this, explicitly invoke [https://www.internalfb.com/claude-templates/skills/data-apps](https://www.internalfb.com/claude-templates/skills/data-apps) and prompt in plan mode with something like:
  - *Make a plan to migrate the dashboard at https://www.internalfb.com/unidash/dashboard/ai_usage_at_meta/goal/ to this app and write it to a markdown file in the new dash folder. Fetch the Unidash JSON and include relevant portions in the same folder as a reference. Create a more natural presentation rather than exactly recreating the layout and existing widgets. Rely on the same SQL macros that are already being used. (from *[*D93505123*](https://www.internalfb.com/diff/D93505123)*)*
- Matej Krajnak is taking the lead on improving this and it’s probably already better (I haven’t tried it in about three weeks). 
- You can see what IG is working on for enablement and a bit about our work with DI at [IG AI Dashboarding Planning](https://docs.google.com/document/d/1cbmcy3257W-qsesPQqGrLqYVP1gtM3oH27CuMGShza0/edit?tab=t.u8h1qdd4wl9s#heading=h.eangqvoflv9q)

Feb 25, 2026

- Upcoming 3/2 Q1’26 DI x Analytics Quarterly Business Review [Status: Outline]
  - [AIDI Q1 ‘26 Analytics & DI Quarterly Business Review](https://docs.google.com/document/d/1C8f0E_nuj6-LXf8ke1dp2m9VJoHM5Y9YjQa6zcRJ9ws/edit?tab=t.0#heading=h.n8l3vmcr0f4u)
  - We’re seeking to standardize the format of [async content](https://docs.google.com/document/d/1C8f0E_nuj6-LXf8ke1dp2m9VJoHM5Y9YjQa6zcRJ9ws/edit?tab=t.0#heading=h.n8l3vmcr0f4u) to reduce cognitive load.
  - Objective for the meeting is to have meaty [discussion on 2-3 topics](https://docs.google.com/document/d/1C8f0E_nuj6-LXf8ke1dp2m9VJoHM5Y9YjQa6zcRJ9ws/edit?tab=t.x8pg4nxo2pr3#heading=h.2f62nw3lc51d). 
- (if we have time) - Data Domain Entity - Omri Ziv - how do we move forward ?
- [NK] - Urge your teams to complete DataEx.

Feb 13, 2026

- [Semantic Model Beta Release](https://fb.workplace.com/groups/1784340412328888/permalink/2077899499639643/) (how Infra DE is looking to implement… WIP [doc](https://docs.google.com/document/d/1Lb-iUTkEOxmiM7tMeqkAo0-hTUZJwMFGJmEFeb0aIU4/edit?tab=t.0#heading=h.2mpa0bi0f82r)) - Tony Cantin
  - TODO: Tony to share measurement strategy
- Omri - AI Readiness Guidance 2026 Q1/Q2 - [AI Readiness Guide for DS & DE Teams - Q2 2026](https://docs.google.com/document/u/0/d/1UmsKHlZrEuFaePLHzbIP1K2plqPLA3VcpFdtSvP6QAg/edit)
- Analytics/DI Workstreams (eg: Semantic Model, AI Readiness, Capacity) - How should we think about them in H1? - Narendra Kambam
- Domains for semantic models - How is everyone thinking about it? Narendra Kambam
  - [EE Domain Taxonomy](https://docs.google.com/spreadsheets/d/1vrPiXBEkGO-B-e-eDpcnLWVhSZFfYo3pU6m_bztoXWA/edit?gid=0#gid=0)
  - Eval accuracy (eval drift, context effectiveness, context coverage, user feedback)
- Data Maturity and Governance - Engin Sözer
  - What rules do you guys care about? We are completely overhauling Admin Portal rules now to enable a scalable system that also supports us to measure quality of semantic models
- Alex: Data app development in Nest is improving rapidly: [launch post](https://fb.workplace.com/groups/nest.fyi/posts/1155611169846083), [example](https://ig-data-apps.nest.x2p.facebook.net/)
  - IG is working closely with DI, there’s also a group for analytics users building off the @nest/data-apps ecosystem. If anyone’s interested and not already in it, let me know. 
  - One-shot dashboard migrations now work reasonably well for moderately complicated dashes
    - [NK] Few Nest examples from EE ([here](https://fb.workplace.com/groups/588820711674120/permalink/1962302410992603/), [here](https://fb.workplace.com/groups/588820711674120/permalink/2757598704593184/), [here](https://fb.workplace.com/groups/588820711674120/permalink/1962545504301627/), and [Manus one](https://fb.workplace.com/groups/719231465096595/permalink/2750344878651900/)) 
- Upcoming 3/2 Q1’26 DI x Analytics Quarterly Business Review [Status: Outline]
  - [AIDI Q1 ‘26 Analytics & DI Quarterly Business Review](https://docs.google.com/document/d/1C8f0E_nuj6-LXf8ke1dp2m9VJoHM5Y9YjQa6zcRJ9ws/edit?tab=t.0#heading=h.n8l3vmcr0f4u)
  - We’re seeking to standardize the format of [async content](https://docs.google.com/document/d/1C8f0E_nuj6-LXf8ke1dp2m9VJoHM5Y9YjQa6zcRJ9ws/edit?tab=t.0#heading=h.n8l3vmcr0f4u) to reduce cognitive load.
  - Objective for the meeting is to have meaty [discussion on 2-3 topics](https://docs.google.com/document/d/1C8f0E_nuj6-LXf8ke1dp2m9VJoHM5Y9YjQa6zcRJ9ws/edit?tab=t.x8pg4nxo2pr3#heading=h.2f62nw3lc51d). 

Jan 30, 2026

- Evals Partnership with DEs - Omri Ziv - Setting expectations on the role we need from DEs for Evals as Domain Experts
  - Evals for New Assets - review/approve - synthetic question following real users questions style
  - Unified Evals - sampling real question - need mapping to ground truth
- Synthetic Eval Generation at Scale - Engin Sözer
- AI Governance - Engin Sözer

Dec 5, 2025

- Will WestRanjini VaidyanathanAlan Leung - [Analytics Productivity](https://docs.google.com/presentation/d/1Xx_QtOQ0u-cwf90D7IqLxFQdFC0HpPojoki-RhoGfjk/edit?brid=vBiwfKo3bijOfbf1sLi9Aw&slide=id.g39129f8ae32_0_0#slide=id.g39129f8ae32_0_0)

Nov 21, 2025

- 

Oct 10, 2025

- Tony HarperMatt Hartwig
  - Summit
    - Agenda[Analytics Summit Fall 2025 Agenda](https://docs.google.com/document/d/1A3z4SvuDZTPiBfTjURxMjsTA1v-FHRXfK7p4WiG2rP4/edit?tab=t.0)
    - Invite List [Analytics/DI Summit Attendees - H2 2025](https://docs.google.com/spreadsheets/d/1fVD5_Rr4BfpIQtVENXLJq0RNeddndzk3RpcJ2Rd0xl8/edit?gid=0#gid=0)

Sep 25, 2025

- Tony HarperDI Summit prep - update?
  - Thasneem DataEx Survey results - anything we need to do? This means the Problem collection we used to do for Summit may look different (or go away?)


Sep 12, 2025

- Data Leads meeting taking place Sep 24 - Matt Hartwig - 3 hour review ( demos, SOTU)
- Improving AI agents for Data  quality through better semantic metadata -> Evals, Evals, Evals - Omri Ziv
- 
- Admin Portal Reliability issues/SEV - FYI 
  - Steve Fischer beyond this ^ what is Admin Portal adoption, usage? - [link to usage](https://fburl.com/unidash/ecsx434l)
- Admin Portal Usability
  - Engin Sözer - Spoke to John today and collected some feedback from other DE managers. We need to quickly fix some usability issues - currently, it’s difficult to navigate through categories/policies
- Engin Sözer - When are we starting the DI Summit prep? Let’s make sure we won’t do this last minute this time
  - Omri Ziv to work with Engin Sözer Tony Harper Thasneem Farzana and bring Jie Chen

Aug 29, 2025

- [Alex] Making current pillar roadmaps readily available
  - Omri Ziv Matt Hartwig to check with DI PMs to have canonical workplace post pinned with links to resources (roadmap, shared goals, meeting agenda)
  - [AI for Data SME group - Canonical pinned post](https://fb.workplace.com/groups/1225687455626858/permalink/1238808684314735/)
  - [Metric Trust and Data Governance - SME ](https://fb.workplace.com/groups/391158253390744/permalink/739863198520246/)
- [Tony] FYI - we’ll be removing DAPR in >80% of cases in the next two weeks. Will flag announcement post when it is ready
- [Elaine] FYI welcome Mike Roumanosas the new champion for Whatsapp!
- [Omri] - Updates on AI Readiness - Tiering is done. Want to partner on resolving discoverability issues.
- [Omri] - DataEx Survey
- [Omri] - H2’25 Analytics<>DI Summit - Dates and heads-up (28-29 Oct)
- [Omri/Carlin] - Eval Set Update
- [Steve] next steps on [DxI Resources for Pillars](https://docs.google.com/document/d/16rECseOQPkimm0kUwA6T0lhBA5AWhJpXd7dp94jEOxY/edit?tab=t.0#heading=h.8wzhjjqsl37k)?
  - List of links in first topic ^ helps
- [Alex] Meta: what’s the vision for this group?
  - References: [Analytics/DI Collaboration](https://docs.google.com/document/d/1L6B2dr3Wi8uIggDN1fSNpel7t2WUy5T6uczZygd95Uc/edit?tab=t.0#heading=h.p2um3c53qbzn)

Aug 15, 2025

- [Tony] Rebooting the Privacy Analytics/DI SME group:[Privacy Analytics/DI SME Group - H2 2025 Focus and Composition](https://docs.google.com/document/d/1m75Y8BQoUUZXkGTHnz20wDr1-BfDP14o044MWVCrrcs/edit?tab=t.0)
- AI: Carlin Eng to have DI PM group review Map of the World, points of contact, comms/feedback channels etc
  - [DxI Resources for Pillars](https://docs.google.com/document/d/16rECseOQPkimm0kUwA6T0lhBA5AWhJpXd7dp94jEOxY/edit?tab=t.0)

Aug 1, 2025

- [Steve] Draft [DxI Resources for Pillars](https://docs.google.com/document/d/16rECseOQPkimm0kUwA6T0lhBA5AWhJpXd7dp94jEOxY/edit?tab=t.0#heading=h.8wzhjjqsl37k) in response to discussion at last meeting on better defining DxI pathways


Jul 15, 2025

- [Alex] 
  - [Analytics/DI Champions, STOs, and SMEs](https://docs.google.com/spreadsheets/d/1R2BNPbdPjHwIAOS7ya-EtQcVcRg-w6abQFI901wiQJE/edit?gid=637275732#gid=637275732) is out of date in a few ways, can we update it with the current SME groups including links to meeting invites, chats and a workplace group for every SME group?
- [Ryan] 
  - Number of[ issues flagged by FF](https://docs.google.com/spreadsheets/d/1l0sMba_nQA-mzCmb2mnUZl9z4kjLk4yysucH56Kd0Ys/edit?gid=1516647257#gid=1516647257) that I’m looking to triage 
  - AI: Steve Fischer work with Thasneem Farzana People Map to consolidate SME groups, papercuts, wp groups, etc for the purpose of communicating to pillars where they need help
    - Detailed post, RFC easier…can leverage AI (w/more info)
  - 
- [Thasneem] What is the state of shared goals for Privacy, given Privacy was the theme in the top 3 pain points? Is Raj still the PoC?
- [Omri]  update on shared goals for M360 and AI Readiness - [Taking shared H2'25 goals across DI<>EP<>DE for M360/Unidash/AI](https://docs.google.com/document/u/0/d/1vMMfxlpu9gYHatq_SvYg9nHwRcgR3Z78_K_pD-i-uTg/edit)
- [See Dashboard: https://fburl.com/unidash/7ogsl27v](https://fburl.com/unidash/7ogsl27v)
- [Engin] Assessing documentation quality [[post](https://fb.workplace.com/groups/1225687455626858/permalink/1251345659727704/)]
  - Guest Speakers: Ram Gaddam, Chibu Agu, Zach Freundt

Jun 30, 2025

- Omri Ziv Engin Sözer Tony Cantin - [RFC] Revised narrative for Shared Goals
  - [Taking shared H2’25 goals across DI<>EP<>DE for M360/Unidash/AI ](https://docs.google.com/document/u/0/d/1vMMfxlpu9gYHatq_SvYg9nHwRcgR3Z78_K_pD-i-uTg/edit)
  - [AI Readiness dashboard](https://www.internalfb.com/unidash/dashboard/ai_readiness_shared_goals/ai_readiness_data_asset_compliance_metrics/)
- Omri Ziv AI Readiness program structure shaping up
  - [WP Group](https://fb.workplace.com/groups/1225687455626858)
  - [SME list](https://docs.google.com/document/d/17Dbi1zMMXphXpPOkVQ3X0EL7o7ugMzcxKM60QpE0cWA/edit?tab=t.oc0xdlmdfip#heading=h.xc6va3qd5hbb)
- 
Jun 13, 2025

- Omri Ziv - [Taking shared H2’25 goals across DI<>EP<>DE for M360/Unidash/AI ](https://docs.google.com/document/u/0/d/1vMMfxlpu9gYHatq_SvYg9nHwRcgR3Z78_K_pD-i-uTg/edit)
- [Engin] AI workstreams - how can we, as Champions, help accelerate?
  - Data Trust
  - Data Exploration
  - Report Generation
  - Query Authoring
- Please update the SME list for AI workstreams
  - [Analytics/DI Champions, STOs, and SMEs](https://docs.google.com/spreadsheets/d/1R2BNPbdPjHwIAOS7ya-EtQcVcRg-w6abQFI901wiQJE/edit?gid=71961732#gid=71961732)
- 

May 23, 2025

- [Karthik] Map of the World - DI focus areas / strategic pillars and people map
- [Engin] [Early headsup] Merging Admin Portal and Governance Portal under Raj
  - Please add rules that you / your pillar cares about in this list - [[Meta Analytics] Governance Rule Repository](https://docs.google.com/spreadsheets/d/11c315rNG5p4HcawMgc8a5jG6kNib6PjM8I5ZZnbwndU/edit?gid=0#gid=0)
- [Omri] - H2’25 Shared goals across DE and DxI for - [Taking shared H2’25 goals across DI<>EP<>DE for M360/Unidash/AI ](https://docs.google.com/document/u/0/d/1vMMfxlpu9gYHatq_SvYg9nHwRcgR3Z78_K_pD-i-uTg/edit)

- 
Apr 25, 2025

- Signal Boost [Survey](https://fb.workplace.com/groups/1380257442915780/permalink/1749387512669436/) and [Strategic inputs](https://drive.google.com/drive/folders/161i6GTiZVDhNB53nc6jgCwE85v9bwZhX) from champions.
- M360 - Enforcement of net new done - celebrate 
  - Next steps: migration strategy 
- [Tony] bring in very senior analytics leadership’s POV


Apr 11, 2025

  - [Analytics & DI Summit, 05/07-08 2025](https://docs.google.com/document/d/1iMjerxmYgx7IavPGLl046qFf9-aens7MbhonqBpTCV8/edit?tab=t.0#heading=h.2s0ttvltx8pj)
    - **Asks for demos: GenAI for Analytics** 
  -  Planning for summit inputs - do we need to do anything here? Tony Harper

Mar 28, 2025

- Alex Ryckman Mellnik: This program has been successful at influencing the development and rollout of specific features, but we haven’t had as much impact on influencing high level priorities. Do we think DI is making the right investments to meet our needs? If not, how can we intercept this part of the decision making process?
- Thasneem FarzanaTony CantinOmri ZivDE-DI Collab EMEA -> NORAM Expansion
  - How does the [EMEA Program](https://fb.workplace.com/groups/3078705362438100/permalink/3416978078610825/) work?
    - Beginning of half:
      - Project identification every half ([H1 projects](https://docs.google.com/document/d/1QLApE2fg2CpJJ6PJv3HbIfgp8wdczbAAU83SjcrsPVc/edit?fbclid=IwY2xjawInEF1leHRuA2FlbQIxMQABHdDl5VSmdkSRT1UvyJKrVVkgxVkCLoYd9lJ5_15fLLzQC7fRTWkH_K-0Xw_aem_qUngEdUdga0lxmF-xgTXSQ&tab=t.0#heading=h.u19tq6silwei))
      - DEs signup
      - Kick-off meeting
    - During half
      - Execution
      - Small group check in within projects
    - End of half
      - Review with leads
      - Celebration
      - Org impact!
  - We think this is a great way to move fast on non-urgent/non-roadmap but necessary DI changes through DE community, AND org contribution opportunity for non-infra DEs.
    - DE as DE
    - DE as SWE (will explore papercut as project intake)
  - We are working on details, will bring back proposal next, for alignment with this group.
  - <u>Is this group on board </u><u>with</u><u> this program?</u>
  - <u>Rebrand it to remove confusion?</u>
- [Maor] Time permitting - GenAI powered Data discovery & exploration demo
  - We’d love for you to test it too and help us improve the product. Join our [alpha WP group](https://fb.workplace.com/groups/980503364212278) or ping Maor Kleider
  - Context: [https://fb.workplace.com/groups/905420740747554/permalink/1310746230215001/](https://fb.workplace.com/groups/905420740747554/permalink/1310746230215001/)	
- [Syed/Roy] on ICPC Migration approach?

Mar 14, 2025

- [*QBR Follow up post *](https://fb.workplace.com/groups/di.reviews/permalink/1696121267989180/)* - *Karthik Lakshminarayanan
- *M360: ASK - Need to understand what MDF metrics MUST be migrated (History is required) vs what is WANTED to migrate - *Omri Ziv
- *[Engin] Just a question (want to get a feel from the room):*
  - *Do we need to follow up on orphaned solutions / frameworks (DE or DI owned)?*
  - *Is there anyone who’d volunteer to help steer this?*
- *[Engin] Next steps for AI for Data & Analytics?*
  - [1c Data exploration execution plan](https://docs.google.com/document/d/1y_q-xMYLD1yTeprpl03Pv8DUdX8_J0SzIQWNyctx1Mo/edit?tab=t.0#bookmark=id.ark1poytp3he)
  - *Do we have a structured working group already?*
  - *What’s the status & followup from the ask last time from Chalmers?*
- *[Syed] - Malloy - do we have enough engagement from DE volunteers? Any blockers and additional help the team needs to meet their goals*

Feb 28, 2025


1. [Maor, 10 min] Trustworthiness and Data Exploration within AI for Data & Analytics
  1. Steve Fischer / Narendra Kambam to pull together SME names across the pillars

*Context shared over chat *


*Hello Champions, *


*When we connect this Friday, time permitting, I’d love to get 10 minutes to discuss GenAI for Data & Analytics to get your feedback and help. Two topics:*


***1. Trustworthiness****. We’re making progress on the AI for Data & Analytics effort that we talked about last week, and need your help with the trustworthiness workstream https://fb.workplace.com/groups/905420740747554/permalink/1310746230215001/ *


*As part of the trustworthiness workstream, we’re looking to improve the accuracy of metamate agents, and by doing so, enable data experts and consumers to become more productive rather than answering repeat questions manually. *


*One of our initial use cases is verifying the accuracy of queries written with DaiAgent. We’re looking to partner with a small number (5-10) SMEs from the Analytics community who are highly experienced in writing queries and helping others fix/improve their queries. This group will help with providing feedback on the product experience, usefulness (perceived impact of initiative), and accuracy (providing feedback on queries generated by DaiAgent) as we build out this capability and integrate it into existing metamate agents and product surfaces. *


*More information about the trustworthiness workstream can be found here and we can discuss it live when we connect this Friday *[AI for Trust](https://docs.google.com/document/d/1F7_V4ZIt4_k8rIPq5H69Uxz8TJbMs-MLFjqMKk22E7o/edit?tab=t.rcgpqsxzhxlb#heading=h.40w73x264wd3)


*ASK: Nominate SMEs who can be part of the initial group for this SQL/DaiAgent use case. Please reach out to me or to Chalmers Brown directly. Thank you!*


***2. Data exploration product experience.**** We’re working to enable users to explore, slice & dice data and answer data-related questions. We’d like to show you proposed design for the product experience and get your feedback. More details in *[*https://fb.workplace.com/groups/905420740747554/permalink/1318044712818486/*](https://fb.workplace.com/groups/905420740747554/permalink/1318044712818486/)


1. [Engin] Data Governance Measurement Strategy (with contributions to above “trustworthiness” part in AI for Analytics)
  1. [Data Governance Strategy - DE View](https://docs.google.com/document/d/1iRMZg_8npy-xc2niCTD7Nru6tuRR6ikuOH32VMrPzuc/edit?tab=t.x1d97brmamft#heading=h.dflp3q7eq5b6)
2. [Engin] Community-driven and/or orphaned solutions
  1. Can we curate a list of these and have a discussion re the future of these solutions and how/if they can fit into the central stack? Examples below:
    1. [DNT (Downstream Notification Tool)](https://www.internalfb.com/wiki/MMT_DE/Tools_%26_Bots/Downstream_Notification_Tool/)
    2. [Data Profiler](https://docs.google.com/document/d/1YCfSajf-6gv-2obkoTCGrw70b1M5xZzZp3iJI5I3JQE/)
    3. [dsfmt (Dataswarm SQL Formatter)](https://fb.workplace.com/groups/dataswarm.fyi/posts/2514888018845686)
    4. …
3. [Carlin] Data Engineering New Hire Survey
  1. DI Analytics has an ongoing workstream to keep us up to date with the latest in the industry. As part of this, we want to understand the relative productivity of our analytics community versus other companies. We’re going to be undertaking a New Hire Sentiment Survey in partnership with UXR, modeled after DevInfra’s program (see [New Hire Survey Results, Q4 2024](https://docs.google.com/document/d/1zIco8t3a8WR1p80nyqVQhwobeSStvbWcgkHv0wItgfQ/edit?tab=t.0#heading=h.pnaidxwdq4h0))
  2. In addition to this, we would like to have a series of one-on-one interviews with new hires to get a more qualitative and in-depth perspective.
  3. ASK: nominate new hires in your org in the 6 month - 1 year tenure range who would be willing to spend 45 minutes to discuss their prior experience, and how it compares with their current role.
4. [Robert] Industry research for AI & Analytics ([draft plan](https://docs.google.com/document/d/19qOQzGW28E5lzFWYQoc935RGUwdLXtR1P_DYc_DyVLs/edit?tab=t.0))
	(more to come in the next few weeks…)

1/ Inform data infra (and stakeholders) about relevant trends and innovations in the industry and land ‘so what’ for our customers & DI, with 5 focus problem spaces: AI for analytics, exploratory analysis, governance, data processing, and serving infra for internal & external analytics


2/ influence the prioritization, strategy/roadmap of teams to be industry leaders in areas that DI and customers care


3/ Improve how PM team show up to our partners and communicate the value of what our products offer


with Bricklaying Work to building the culture in longer term:

-Reach out to other companies to try to get traction

-Look into internal industry benchmarks 

- Engagement channels for active community for industry inspiration - eventually turn everyone in DI  into a Data Nerd.


Feb 13, 2025

- [NK] Question for the team.
  - Was there any discussion with M360 or other teams to support laddering of metrics by setting parent-child relationships? For example, if the north star metric is growth (MAU), then the L1 metric could be retaining users, and the L2 metric could be the number of resurrections, then L3 and so on. This would provide a clear linkage between the goal maps. If I click on the north star metric, it should show the linkages to all other metrics in the goal map.
- [SH] AI for Analytics. When do we want to make this part of the DE<>DI collaboration

Dec 20, 2024

- [Tony/Ahmed] Data Warehouse move to ICPC
  - [DWH ICPC Migration](https://docs.google.com/document/d/1fOzPw80HzQ0YHO0Fwq50sS6xXmHM3TwLjbnGkM-AY6I/edit?usp=sharing)
- [NK] Will be travelling at this time.
  - [Data Governance - FAQs and Approach](https://docs.google.com/spreadsheets/d/1D9onbvd_Tc1PIHpGBWHWmYxNK4s6-I1pjElTudfDd-8/edit?gid=862061277#gid=862061277)
    - Completed the template per my action item from the Governance kickoff meeting.
    - Kudos to WhatsApp team for entering a data governance use case.
    - For other pillars, please continue to add.

Dec 4, 2024

1. [Engin]
  1. M360 - EP Summit happening now
    1. [Agenda](https://docs.google.com/document/d/1PBL_AUjmVeojgtieZ-o9xG3Rk1H8gpEuqWv09TwpYF8/edit?tab=t.0)
    2. [Pre-read](https://docs.google.com/document/d/1SJVF5fEJkVGxTs7xesUVeIkXV8zaLN6DMqRG17AyjxI/edit?tab=t.0)
  2. Kicking off [Data Governance strategy](https://docs.google.com/document/d/1iRMZg_8npy-xc2niCTD7Nru6tuRR6ikuOH32VMrPzuc/edit?tab=t.0) working group today
2. [Alex] 
  1. Timeline for decision w.r.t. Malloy?
  2. Connections with SME groups?
3. [Narendra]
  1. Impulse use cases for POC - [EP Patterns of Analytics/In-product Analytics (with xdb/Presto, etc)](https://docs.google.com/document/d/147xi8n-hsrgXsxOyGoy8Paxf4jpA0Zx_D1Zij4nAG-I/edit?tab=t.0#heading=h.iaucdjq8fous)
  2. Unidash Adoption
4. [Matt H] Cockpit CAB & Data Processing SME Group 



Nov 22, 2024

1. [Maor & team][Analytics & DI H2 ‘24 Summit Summary](https://docs.google.com/document/d/1CefqZsJjvdjCe7bIbynuhCksoRD-3neQ77ngGKsZFuA/edit?usp=sharing)
  1. In this time we identified top problems to solve for each problem domain, and then strategic pillar (tying to DI vision for Analytics -> forming DI roadmap OKRs). New Challenges were identified in the summit, such as asset management and data finding annotations, which require deeper impact analysis for prioritization and funding.
  2. Next Steps: involve the summit summary informing DI planning for 2025 and sharing roadmaps with the analytics community (ETA 12/16 for async review), focusing on the priorities highlighted during the summit. 
  3. H2 recap + H1 roadmap review on 1/23 9a PT ([invite](https://fburl.com/meeting/2x6swyd2))
2. [Tony] Overall summit feedback. What worked and what didn’t?
3. [Tony] Summit input format. What worked and what didn’t? What should we change?
4. [Engin] Summit followups. What are the working groups we need to initiate to create extreme focus towards key strategic areas? Should we structure SME groups to divide&conquer across strategies?

Nov 8, 2024

1. [Maor]  DI Vision for Analytics - review & feedback from champions 
  1. [DI vision for Analytics](https://docs.google.com/document/d/1WQ9DZL9RoeUnCdp8FqKrlQOEQx1vYLZN-slhk19xjKk/edit?tab=t.0)
2. [Maor] DE Connect DI presentation - review & feedback from champions
  1. [track_di_maor_de_connect](https://docs.google.com/presentation/d/1MAsly9xVav29iy50chm91zOpRWtrB71x-Pzb2xzkWDw/edit#slide=id.g2f9c1f8fcb6_1_566)
3. [Summit]
  1. Agenda is out, invite is out. Please double check if attendees you want from your pillars are invited.
  2. Please respond to dinner invite and add STO/SME 

Oct 23, 2024

- [Summit] 
  - Prioritization framework [DI - DE Prioritization Framework](https://docs.google.com/document/d/1oX3Wv84H1EQnsYC5-qQbJQ23cJcrqKCnyEQNjr3tM7o/edit#heading=h.z1zzi342c5jy)
  - Problem 1-pgr due 10/31
  - [Analytics DI Summit - H2 2024 - DE/DS Presenters](https://docs.google.com/spreadsheets/d/1OagmnDBvmIAeTrRAwHIg_RfZk3UwdkLbjFAe3-6kwYc/edit?usp=sharing)
    - **Ask for Champions: **Please nominate DE/DS Presenters (Champions/STOs/SMEs) for non-Demo sections
  - Attendee: please make sure the attendee from your pillar is in invite ([day1](https://fburl.com/meeting/yr2lylc0), [day2](https://fburl.com/meeting/emv3n486))
- [Engin] DI - DE Operating model 
  - Any highlights / lowlights / feedback this group wants to share?
  - Do we feel like the empathy / listening to each other across DE - DI has improved over the past 6 months?
- [Engin] Problem-solving at holistic level 
  - Are we able to address this well so far? How do we feel about our ability to address the cross-cutting priorities / x-domain workflows?
- [Maor] DE Connect presentation
- [Robert] H1 2025 review 
  - Time: After psc cycle for managers? 1/22-28 please vote for a date
  - Format: combine H1 DI Analytics roadmap review w/ champions
    - H2 recap
    - H1 roadmap


Oct 11, 2024

- [Engin/robert/thasneem/carlin] prioritization framework update
- [Maor] Quarterly Business Review
- [Tony] Experimentation Platform in the summit
- 

9/27/2024

- [Robert/ Thasneem] Summit update, plans, template for pain point 
  - [Analytics & DI H2‘24 Summit Proposal](https://docs.google.com/document/d/1KkMTPKkYnof6fC3MyvEAmPM9wyPLtx84UGSYiXT4mxc/edit)
  - [DRAFT  [Analytics Pillar] Summary One Pager template H2 2024](https://docs.google.com/document/d/1CugfkHj3k639FZDNRRAEyUkPXwyV96q8KPlp1QE3m-8/edit)
  - [Engin] What working sessions would we like to see / propose? (brainstorm sessions)
  - [Engin] Do we plan to try and find a metric / option to help with pain point sizing?
- [Omri] - Help needed with driving consensus around  Metrics Governance and creating goals for metric consistency for DE org 

9/13/2024

- [Maor] Quarterly business review and Analytics/DI Summit plans / feedback
- [Maor] General feedback on what can be done better
- [Tony] Getting organized around Metrics and Role governance
  - [Thasneem] Capacity governance too? - Move from Namespace ownership to Pillar-level team ownership
- [Thasneem] Starting to think about GenAI in Analytics - CPP is working with GenAi team
- [Raj] Data Understanding for Analytics use cases - POCs to validate/test problem hypothesis/ideas.
- [Engin] Increasing the SME group engagement further, incentivizing/motivating others
  - Site-based monthly meetups between DE-DI
- [Elaine] M360 WA challenges and next steps
### 8/20/24


- [[Canonical] Business Data Portal (BDC) - Product and Technical Vision](https://docs.google.com/document/d/14q2qCyLoBg7096HS9vcGglTGhtXRDeYcAttLv9JWhmg/edit#heading=h.f2i5yyp3bt2i)* - Narendra’s data portal and metric council document*

### 8/9/24


- DI proposal for how they work with the champions group
- Q3 review
### 7/25/24

- Latest on the new engagement model with DI
- Meeting Notes
  - Two adhoc workstreams spun off
    - Tony and others to meet with Maor and push for monthly reviews
    - Thasneem to work with Vibha and look into SME groups, specifically WaaS/WaaP workstream, understand the Dataswarm/CDM/Capacity workstreams better 
### 6/25/24

- [Tony]
  - Look for the DI roadmaps (delayed) today in the summit group
  - Walkthrough of proposed changes to the collaboration
- [NK]
  - Proposed topic for next bi-weekly. [Review H1 OKRs](https://docs.google.com/document/d/1L6B2dr3Wi8uIggDN1fSNpel7t2WUy5T6uczZygd95Uc/edit); Mark ones that are complete and identify if we need anything for H2 to keep us on track.

### 6/11/24

- [Engin] 
  - Clarifying the scope of each domain (tools within each scope) - Who’s ultimately accountable for this clarity?
    - AI: Tony will raise an escalation to the Steering Committee about the areas that don’t have PM / SME group alignment
  - Some of the topics/projects raised in DI Summit already kickstarted but I think there’s a comms gap as it’s not visible to everyone. How do we fix this?
    - Examples: Uhaul Governance, 
    - 
- [Tony]
  - Next steps in DI planning cycle
- 

### 5/28/24

- Lana and Britton - presenting options for Warehouse as a product SME group.

### 4/30/24

- Update from DI (Abhishek Marwah and Raghu Raman) on DIRCU to BCU conversion
### 4/16/24

- Tee up Superset decision
- [VV] STO’s collaboration with other STO’s
- [VV] DIRCU to BCU challenges - [Feedback](https://fb.workplace.com/groups/616602652034841/permalink/2144969365864821/), [Questions](https://fb.workplace.com/groups/616602652034841/permalink/2144954772532947/)

## 04/02/2024

- [TH] Analytics Summit Kickoff with Tony and Briton
- 

## 03/19/2024

Agenda

- [TH] DI to present the Apache Superset pilot, get feedback and alignment from Analytics Champions [45 min]
## 03/04/2024

Agenda

- [VV] Experimentation group in the same rhythm as other domains - ETA -3/12
  - Lana has been able to align Chris Altman…should get going starting 3/12
  - AI for all: review and update [STOs for experimentation group](https://docs.google.com/document/d/1f7Dh_XNRVrezKovEdnaAvxGd6toVTCjMR6eoEjxjUfc/edit#bookmark=id.ies18vbakln3)
- [KW] Escalation paths discussing (how, where, who, when).
  - Tony to share Escalation path document
  - Put feedback in running doc (Vibha to link) - [Running Document](https://docs.google.com/spreadsheets/d/1jQPACin7lWVRJlpCqFaWjhS7pvhYgBE2uxo-D0Ik63M/edit#gid=0)
  - TLDR: Mode of operation across domains is a bit of mixed bag
    - WaaP and ML - room for improvement
    - Data consumption, Privacy, and MTDG working well
  - Vibha is escalation point for feedback on how groups are operating
- [KW] Giving SMEs a sense of ownership?
  - Champions are handling this internally to give folks those opportunities/ownership
  - Tony to share a doc on this
  - DI has expectation that there’s an STO from DE for each domain, but should SMEs be able to plug in to sub-workstreams/domains for larger areas (e.g. WaaP)
- [TH] Planning and comms kickoff
  - Planning summit will upon us before we know it
  - Jyotsa to be the POC 
  - Need to get comms out to DE orgs by end of March
  - Suggestion to consolidate comms as well
  - NK to follow up on/carve out time to discuss comms strategy
- [EG] Pushing fast m360 migration, goals on dashboard & deltoid unified definition nodes, and useful features utilizing joint definitions. + Datelists for all vitals. Added a DS SMEs to consumption/ML. Well-integrated into DI discussions around all relevant workstreams.
- [NK] [Analytics/DI Collaboration](https://docs.google.com/document/d/1L6B2dr3Wi8uIggDN1fSNpel7t2WUy5T6uczZygd95Uc/edit)
  - Ask for folks to take a look and provide feedback/input
    - In particular, check out the roles/responsibilities (shoot for Thursday, 3/7 to get this done)
## 02/20/2024


Agenda

- [Tony] Revised H1 Goals for Analytics/DI Champions[Analytics/DI Champions - H1 2024 Goals](https://docs.google.com/document/d/1TZXmsuMZaCdnJrrmsABjZf-0UVOXglcw1l1HBzvE3dA/edit?usp=drive_web&ouid=111365624290269850853)
  - Aiming to lock these today
- [VV] Continuous Feedback cycle
  - [Running Document](https://docs.google.com/spreadsheets/d/1jQPACin7lWVRJlpCqFaWjhS7pvhYgBE2uxo-D0Ik63M/edit#gid=0)
- [Ali] Experimentation group?
- [Elaine] GenAI - separate domain?
  - Keep under ML (ensure to flag the GenAI needs there)
- [NK] Canonical document
- [Engin] SEV handling 
  - Should we involve STOs in SEV2+ that require DI to improve tooling & features?
- [Emma] DI commitment to papercuts 
- [Erik] M360 deprecation and pivot to improving MDF versus completing mdf migration in an extremely short timeline (1 week aspirationally). Mitigate cost to EP entirely.

Notes

- Any recurring SME meetings should have one person as a representative.
  - Right now meetings are a mix of too many or too few. How to align.
- ML - combine or have separate for GenAI
  - Team leans to keep together, as there is overlap
- M360 vs MDF
  - Since M360 is not actually going away, Erik is attempting to accelerate migration to it. Escalation meeting with DI and EP on Wed afternoon, EP SME group will report back with an update after that completes
- Actions: 
  - Vibha to follow up with Lana on experimentation. Need to follow the standard processes.
  - All Champions to review OKRs today and comment on the document.
  - NK to create a canonical document
  - Tony to ask DI for SEV criteria
## 02/06/2024


Agenda

- [Tony] Discuss proposed H1 Goals for Analytics/DI Champions[Analytics/DI Champions - H1 2024 Goals](https://docs.google.com/document/d/1TZXmsuMZaCdnJrrmsABjZf-0UVOXglcw1l1HBzvE3dA/edit?usp=drive_web&ouid=111365624290269850853)
  - Tony’s thoughts: I drafted this, but very open to feedback
  - Feedback
    - Set of principles vs measurable outcomes (e.g. how do we measure ‘healthy champions group’)
- [Tony] Decide if we need one chat thread with Analytics and DI champions together, or two - one for Analytics+DI and one for Analytics only
  - Tony’s thoughts: there’s probably some value in being able to talk amongst ourselves; we can get alignment on our strategies and discuss issues with DI if needed
Notes

- Quick summary from analytics kick-off last Friday
  - Justin kicked it off and set the stage/expectations
  - Activity is meant to be role/goal drive rather than task-driven
- General feedback/open conversation
  - Feels like we’re trying to catch a running train (e.g. roadmaps already fleshed out; how to get SMEs engaged; etc)
  - Information is disjointed; Vibha to follow up with Lana directly about how to streamline process/rhythms
  - How do we affect change and influence the current roadmaps?
    - Many groups already 
    - Need clear escalation paths; not seeing the same level of effort from DI
  - Across 8 categories, unclear what the actual execution strategy and priorities are
    - Maybe focus on small handful (e.g. metric trust and governance) to ‘get right’ and follow up on
  - We should start to prep how we want to work with DI and help define the roadmaps and prios
  - Narendra to follow up on getting syncs scheduled with DI champions as well
## 01/23/2024

Canceled


Agenda

- 
- Next steps/follow ups [5mins]

## 01/09/2024

Agenda

- Intros [5-10mins]
- Review and align on expectations for SMEs and Champions [15 mins]
  - [Expectations for DE Champions](https://docs.google.com/document/d/1lRMzb0Gwprnyq8VZH5zNRtZK_GxzvmryqgLpaZMQE6g/edit)
  - [Data Infra Collaboration - SME Role and Responsibilities](https://docs.google.com/document/d/1oHAvxxfbgMn7SV_mzxgPL3HXi87VlYKVdKBqN5x0R5g/edit#heading=h.h0zbh7gpmlqb)
- Next steps/follow ups [5mins]

Notes

- How do we avoid previous failure modes of previous working groups/collaboration models
  - Tony to take an AI on ensuring that there are respective POCs on the DI side that we can interface with and hold accountable
  - Engin: DI struggles with focusing and may not be leveraging DE strengths/skills to get more involved and drive execution
  - Ali: How are the SME groups going to organize and operationalize their efforts (e.g. through STOs)?
    - Tony: Each SME group may operate differently.Champions are ultimately accountable, but can work through STOs to empower them to figure out what works best for each group
  - Jyotsna: What is the execution going to look like (on the DI side). How are we going to deal with the ‘papercuts’, issues, bugs, features that weren’t part of the original roadmap/strategy
    - Tony: ‘papercuts’ process is a solution, but DI owes us clarity.
  - Narendra: How STOs are going to coordinate work and pass that on to DI. 
  - [SME/STO List](https://docs.google.com/document/d/1f7Dh_XNRVrezKovEdnaAvxGd6toVTCjMR6eoEjxjUfc/edit#heading=h.1afs777ujlko)

Open Qs

- What is the status of the DI category/product roadmaps? Can we collate/organize all of the roadmaps?
- Are SMEs defined and integrated?
- How are we going to coordinate our respective efforts? How often should we meet?
- What is the communication plan around the DI/DE collaboration process?
- 

Action Items

- Tony to follow up with DI and get respective ‘STO’/’SME’ POCs on the DI side for each category
- Tony? To get clarity on the (papercut) process by which we can bring and prioritize features, bugs, issues, etc on an ongoing basis
- Champions to create SME meetings in each pillar

