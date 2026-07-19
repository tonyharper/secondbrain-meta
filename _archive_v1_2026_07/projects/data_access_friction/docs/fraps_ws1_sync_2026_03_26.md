# FRAPS WS1 Sync - Mar 26, 2026

Source: [Google Doc](https://docs.google.com/document/d/1xwyt3EhbRQFFGSz4py1zcvdJptXsWriQAQwN1bFW7k8/edit)

Invitees: Wenlong Dong, Anisha Patel, Tola Dalton, Can Lin, George Schnabel, Rachel Lee, Tony Harper, Aaron Morris

## Quick Recap

- The meeting focused on discussing agent platform priorities and friction measurement approaches across Workstream 1.
- The team discussed whether to use internal or external agent usage metrics to determine priority platforms, with Tony Harper agreeing to gather usage statistics and propose a unified list.
- The scope of agents to include was explored, with Can Lin suggesting a focus on internal productivity workflows rather than specific 1P/2P/3P classifications.
- The group discussed establishing friction intake processes, with Tola Dalton noting that Workstream 4 was working on metrics-based intake and expressing caution about prioritizing user reports without data cross-referencing.
- Rachel Lee proposed integrating user-reported friction metrics into an existing dashboard being built by Workstream 2, and Anisha Patel agreed to coordinate next steps with a small working group.

## Next Steps

- **Tony**: Gather usage statistics on agent platforms, propose a single list of agent platforms for the group, and circulate a proposal for dimensions (e.g., platform, agent, employee type) for categorizing friction before the next meeting.
- **Tony**: Talk to Jordan to clarify the difference between the guardrail friction measurement post and other ongoing friction tracking efforts.
- **Anisha Patel**: Kick off a chat thread with identified participants (including Rachel Lee, Kyle, and others) to discuss next steps for onboarding metrics and user-reported friction onto the Nest-based dashboard.
- **Wenlong Dong**: Share the morning's L1 security risk review discussion to the group as an example of risk review-related friction.
- **Group**: Revisit risk review integration and operationalization in the next meeting.

## Discussion Topics (from notes doc)

### Mar 26, 2026

- **Rachel Lee**: Are we talking to [these folks](https://fb.workplace.com/groups/ai4re/permalink/2414688382311758/)?
  - Confirmed: These are accounted for.
  - Follow-up: Understand specific differences between this post and security/privacy friction. Do we need to do some form of split in the friction measurement? (Tony Harper)

- **Tola Dalton**: How do we decide on top agent platforms for workstream KR focus?
  - Enumeration of agents in-scope (focused on employee access 1P/2P): agent list from Privacy Risk: [Internal Agent Risk Executive Review - March 2026](https://docs.google.com/document/d/1ka_eVAakpZIj-np6ETtU1lxyThclx8-Pp_JU57TKp3M/edit?tab=t.qotepimrdquz#heading=h.5ej42ek2f2ky)
    - Metamate (+ DataMate)
    - DevMate
    - Claude Code
    - Manus (Prod)
    - Confucius
  - Each workstream to determine their specific stack ranking/scope

- **Wenlong Dong**: Intake of frictions — how to get them into the execution pipeline from different sources?
  - Measurement / detection: **what is the taxonomy?**
    - Dimensions: 1) agents, 2) platforms, 3) user roles, 4) tools (Tony Harper)
  - User reports: e.g. devinfra coding agent friction [tracker](https://codingagentfriction_tracker.nest.x2p.facebook.net/), WS2 - Kyle Murphy has something?
    - Prioritization, measurement based
  - LLM analysis
  - Can we onboard the different workstreams onto: [agent-friction-monitor](https://agent-friction-monitor.nest.x2p.facebook.net/)
    - Need to share out workplace references
    - Aligned on kicking off a dedicated thread for this effort

- **Anisha Patel**: Risk Reviews
  - Privacy Reviews: Can & Wenlong Dong
  - Simon for Risk Reviews

### Mar 19, 2026

- Discuss WS1 OKRs
- Discuss expected input/outputs from each workstream to ensure we are best complementing each other vs any overlaps
