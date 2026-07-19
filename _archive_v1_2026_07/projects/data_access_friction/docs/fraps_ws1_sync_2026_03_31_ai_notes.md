# FRAPS WS1: Intake/Triage Taxonomy & Routing - March 31, 2026, 9:05-9:30 AM PDT [AI meeting notes by Zoom]

*These meeting notes were created using generative AI. AI experiences are experimental and may not always provide accurate information. You may remove this disclaimer once meeting participants have reviewed the document and confirmed its accuracy.*




# Mar 31, 2026

Invitees: Anisha Patel, Kyle Murphy, Tony Harper, Aaron Morris, Tola Dalton, Rachel Lee

## Quick recap

- The meeting focused on developing an intake and routing system for agent friction issues across different workstreams.
- Aaron Morris and Kyle Murphy presented their current dashboard and taxonomy for MetaCLI Workstream 2, which uses LLM classification to categorize posts and generate tasks in their GSD.
- The team discussed expanding this system to cover all workstreams and include routing to appropriate teams.
- Tony Harper raised concerns about attributing top-line metric improvements to specific workplace posts due to the complex nature of friction metrics.
- The group agreed to start with basic reporting of reported issues and resolved tasks, while exploring ways to correlate post data with analytics.
- They also discussed using existing block inventory lists and identifying sources of friction across different systems.
- The team decided to move forward with implementing a basic version of the system while continuing to iterate on routing and inventory mapping.
## Next steps

- Aaron Morris & Kyle Murphy: Expand the current MetaCLI Workstream 2 dashboard and classification system to cover all agent friction workstreams, including updating LLM prompts and classification logic to extract agent, system, and task information, and begin generating roll-up reports on themes and issues.
- Aaron Morris & Kyle Murphy: Iterate on the LLM prompts and classification scripts to improve routing and task generation, including mapping posts to the correct teams and enriching task details for easier human follow-up.
- Aaron Morris & Kyle Murphy: Add new data fields (e.g., agent, system, what the user is trying to do) to the post classification pipeline as discussed, to enable better correlation with analytics and prioritization.
- Anisha Patel: Help coordinate with Aaron Morris & Kyle Murphy to enumerate all known sources of access blocks/failures across teams, including reaching out to relevant POCs from Workstream 3, Workstream 4, data warehouse, and security teams.
- Anisha Patel, Aaron Morris, Kyle Murphy: Work with POCs from other workstreams (e.g., data warehouse, security) to scope out inventory blocks and determine the right level of granularity for mapping and routing.
- Aaron Morris & Kyle Murphy: Start generating weekly roll-up reports showing number of reported frictions and number of tasks closed, as a first step towards metrics and visibility.
- Rachel Lee: Reach out to Hansi to identify where to access privacy-related blockage data (e.g., trusted enforcer, artillery logs) and assess feasibility of mining these sources.
- Aaron Morris & Kyle Murphy: Continue work on mapping detected issues to existing inventory of blocks (e.g., S4 AI guardrails), and develop a logical categorization/tree for routing issues to the correct workstream.
- Anisha Patel: Keep the core group engaged for ongoing feedback and iteration as the dashboard and process evolve.
## Summary

### Reporting Structure and Updates Discussion

- The team discussed challenges with reporting structures and updates across different systems including infra updates, PROTI updates, and agent oversight.
- Anisha Patel explained they are navigating three different update models and sought clarity on how to properly scope and report on Fraps work, particularly regarding what should be included in version 5.4.
- The main focus of the meeting was to establish a clear intake process across agent friction and human-reported intake, with plans to expand on the existing frameworks developed by Arun and Kyle Murphy's MetaCLI team for Workstream 2.
### Access Friction Taxonomy Dashboard

- Aaron Morris presented an access friction taxonomy dashboard developed with Kyle Murphy and the MetaCLI friction team.
- The system uses an LLM to classify posts from workplace groups and maps them to specific categories of problems, though it currently contains significant noise due to posts about dev friction rather than access friction.
- The dashboard runs daily via a cron job and generates tasks in the Agent Friction GST, though task routing to specific teams still needs to be implemented.
### MetaCLI Routing System Expansion Discussion

- The team discussed the current routing system for MetaCLI Workstream 2, which currently generates tests only for high-confidence predictions of access friction.
- kmurf and Rachel Lee proposed expanding the system to cover all workstreams and creating reports on friction identification and resolution metrics.
- Tony Harper pushed back on the idea of attributing metric improvements to workplace posts, arguing that such attribution would not be realistic due to the complex nature of friction metrics and release processes.
### Product Launch Metrics Attribution Challenges

- The team discussed challenges with measuring top-line metric attribution for product launches, particularly the difficulty in obtaining definitive data without dedicated resources.
- Tony Harper suggested using proxies like number of reported issues and closed tasks, and recommended leveraging UXR for anecdotal feedback.
- The group acknowledged that while getting statistical significance might be challenging due to resource constraints and the fast-paced nature of their work, implementing some observable metrics and gathering qualitative feedback could provide valuable insights.
### Social Media Analysis Strategy

- The team discussed ways to analyze social media posts and cross-reference them with analytics to better prioritize efforts and understand user needs.
- Tony Harper suggested using dimensions to break down complaints and correlate them with top-line measurements.
- The group agreed to first implement post analysis across the entire workstream before integrating it with top-line measurement systems.
- They also discussed the importance of understanding the specific tasks users are trying to accomplish, which could help in identifying common user goals or "jobs to be done."
### New Classification System Implementation Discussion

- The team discussed adding new classification capabilities to their existing system, which already scans posts with an LLM daily and stores information.
- They explored using an existing inventory of blocks rather than creating new ones from scratch, with Aaron Morris suggesting to map new blocks to existing categories like those in S4 AI's guardrails documentation.
- Anisha Patel raised questions about identifying the right POCs from Workstream 3 and 4 to scope out inventory blocks, and questioned whether the current level of granularity from S4 AI is appropriate for their needs, noting potential overlap that could create confusion.
### Data Sources and Controls Discussion

- The team discussed challenges with data sources and controls for their project.
- They identified the need to determine which blocks are expected versus unexpected, and discussed potential sources including trusted enforcers and PZM/GDAs.
- Anisha Patel outlined next steps including creating a list of known sources across teams, developing an inventory of failure types, and establishing a logical categorization system.
- The team agreed to start with updating their dashboard to show current findings while continuing work on inventory and routing, with Anisha Patel planning to maintain a core group for ongoing iteration and feedback.





