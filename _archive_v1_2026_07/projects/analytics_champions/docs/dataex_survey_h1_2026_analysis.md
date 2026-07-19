# DataEx Survey H1 2026 — Analysis

Source: Data Experience (DataEx) Survey, H1 2026 (Wave 2). Fielded 2/17/26 - 3/4/26. 41% response rate (n=2,346 starts), 82% completion rate. Produced by Infra & CPP UXR.

## Overall Headlines

Both topline KPIs moved significantly:

- **Overall efficiency** (ease of making progress): **53% favorable, +15pp** from H2 2025
- **Tooling satisfaction**: **76% favorable, +19pp** — now above the 70% "good" threshold

This isn't a data-role-specific phenomenon. Developers, PMs, and data roles all crossed 70% on tooling satisfaction this wave. AI is the clear driver — Analytics Agent and Claude Code usage skyrocketed since the last wave, and all AI task-specific metrics improved between 20 and 50+ pp.

**The AI efficiency story is concentrated in certain tasks.** Authoring queries (72%) and exploratory data analysis (70%) show the highest perceived AI gains. "Identifying key insights" and "identifying the right type of analysis" remain weak (43%) — the higher-judgment work AI hasn't cracked yet.

**All 13 inefficiency drivers improved significantly.** The top-tier pain points — ad hoc requests, access/privacy friction, memory/capacity limits, documentation gaps — all dropped. Fewer than 1 in 5 now report "a lot" of difficulty from any of these. The improvement in ad hoc request burden suggests AI is beginning to deliver on the promise of self-service analytics.

## Counterbalancing Concerns

Three themes from qualitative feedback should temper the positive toplines:

### 1. Output trust is the #1 AI pain point

AI tools present results with high confidence and are frequently wrong — hallucinating table names, generating incorrect SQL, producing contradictory answers across runs. Manual validation erodes time savings.

> "Analytics Agent helps, but wrong half the time. So it is easy to get data and insights, but it is hard to confirm it is the right data." — DS IC, ABM

> "AA can return contradictory findings each run. It requires fine-tuning to prevent it from claiming insights when there is underlying uncertainty." — DE IC, Enterprise Products

### 2. Tool proliferation is creating real confusion

People don't know when to use AA vs. Datamate vs. Claude Code vs. Devmate vs. Metamate. The deck comments (from Jenni Romanek) explicitly ask: "If we don't plan to de-frag, will we at least put together some kind of 'when to use what' framework?"

> "Too many AI based tools causing a lot of noise on what to use; I think Claude Code as a single tool with some persistent memory to continue your sessions work best. Everything else is noise." — DE IC, ABM

> "I'm unclear why we have more than one AI tool for data-related work. I want a single orchestration UI that lets me do all the data-related things." — UXR Manager

### 3. Pace of change is unsustainable

Even adopters report constant UI changes, feature deprecation, and new releases disrupt workflows. No structured training exists.

> "Right now this feels very thrashy with new AI tools coming online constantly. Sometimes when I start using a tool it works and it's amazing, and then other times I waste my time." — UXR IC, CSSR

## Risk Org-Specific Findings

Both Risk cuts have small sample sizes (DE n=23, DS n=22) — below the 30-respondent threshold for statistical testing. Treat everything below as directional.

### Risk DE KPIs vs. Meta Overall

| Metric | Risk DE (n=23) | Meta DE Overall (n=1,012) | Delta |
|---|---|---|---|
| Overall Efficiency | 67% | 60% | +7 |
| Tooling Satisfaction | **69%** | 80% | **-11** |
| Understand Business Context | 62% | 63% | -1 |
| Find Data | 67% | 69% | -2 |
| Explore Data | **94%** | 85% | **+9** |
| Logging | 53% | 52% | +1 |
| Author Pipelines/Metrics | **100%** | 92% | **+8** |
| **Dashboarding** | **34%** | 55% | **-21** |
| Data Operations | 66% | 71% | -5 |

### Risk DS KPIs vs. Meta Overall

| Metric | Risk DS (n=22) | Meta DS Overall (n=970) | Delta |
|---|---|---|---|
| **Overall Efficiency** | **41%** | 47% | **-6** |
| Tooling Satisfaction | 75% | 73% | +2 |
| Understand Business Context | 65% | 67% | -2 |
| Find Data | 59% | 61% | -2 |
| Explore Data | 73% | 80% | -7 |
| Conduct Data Analysis | 73% | 83% | **-10** |
| Communicate Insights | **82%** | 73% | **+9** |
| Dashboarding | 66% | 59% | +7 |
| Experimentation | — | 64% | — |

### Interpretation

**Risk DEs and DSs tell opposite stories on certain dimensions:**

- **Risk DEs** feel more efficient than average (67% vs. 60%) but are significantly less satisfied with tooling (69% vs. 80%). They're productive *despite* tooling, not because of it.
- **Risk DSs** feel less efficient than average (41% vs. 47% — in the red zone) but are satisfied with tooling (75% vs. 73%). They have decent tools but are struggling to make progress, possibly due to domain complexity, ad hoc burden, or organizational friction.

**Risk DE dashboarding at 34% is the worst of any org in the survey** — deep in the red zone. Even WhatsApp (36%) and IG (43%) are higher. This validates the strategic importance of our moves towards Nest.

**Risk DS communicating insights at 82% is the highest of any org** — well above Meta DS overall (73%). This could reflect the nature of Risk analytics work (often tied to incident response or compliance where the audience is captive and the stakes are clear).

**Risk DS conducting data analysis at 73% lags Meta overall (83%) by 10pp.** This suggests Risk-specific data complexity — more joins, more edge cases, more domain-specific logic — is making core analysis harder than average.

**Risk DE pipeline/metrics authoring at 100%** and explore data at 94% are bright spots, suggesting the CDM/Dataswarm toolchain and semantic model investments are landing well.

### Risk DE Inefficiency Drivers (n=17)

| Driver | Risk DE | Meta DE Overall |
|---|---|---|
| Ad hoc requests | 11% | 21% |
| Memory/capacity limits | 11% | 11% |
| Access/privacy friction | 8% | 18% |
| **Documentation for data artifacts** | **16%** | 8% |
| **Combining data sources** | **21%** | 4% |
| **Using 3P packages** | **12%** | 3% |

### Risk DS Inefficiency Drivers (n=17)

| Driver | Risk DS | Meta DS Overall |
|---|---|---|
| Ad hoc requests | 26% | 29% |
| Memory/capacity limits | 20% | 19% |
| **Access/privacy friction** | **23%** | 15% |
| **Documentation for data artifacts** | **27%** | 20% |
| **Documentation for data tools** | **24%** | 9% |
| **Slow/delayed data landing** | **19%** | 8% |
| **Using 3P packages** | **30%** | 6% |
| **Oncall rotation maintenance** | **25%** | 5% |
| Combining data sources | 14% | 11% |

### What Stands Out Across DE and DS

**Combining data sources is a DE problem (21% vs. 4%), not a DS problem for Risk.** This aligns with the structural reality — DEs are the ones building cross-risk-area joins and dealing with schema inconsistencies.

**Documentation gaps hit both functions hard.** Risk DE: 16% vs. 8% for data artifacts. Risk DS: 27% vs. 20% for data artifacts, and 24% vs. 9% for data tools. Risk's domain complexity makes tribal knowledge a bigger problem than average.

**Risk DSs are hit hard by 3P package friction (30% vs. 6%) and oncall maintenance (25% vs. 5%).** These are extremely elevated. What 3P packages are we using?

**Access/privacy friction is below average for Risk DEs (8% vs. 18%) but above average for Risk DSs (23% vs. 15%).** This is intersting and one we should dive into.

## Overall DataEx Scorecard (Activity KPIs by Function)

Color coding: blue (>=70% favorable), yellow (50-69%), red (<=49%).

### Data Engineer (n=1,021)

| Activity | % Favorable | Change from H2 2025 |
|---|---|---|
| Author Pipelines/Metrics | 92% | +11 |
| Explore Data | 85% | +17 |
| Data Operations | 71% | +9 |
| Find Data | 69% | +16 |
| Understand Business Context | 63% | +4 |
| Dashboarding | 55% | +6 |
| Logging | 52% | +13 |

Logging (52%) and dashboarding (55%) remain the lowest-rated DE activities, though both improved. DEs praised Nest as a "game-changer for dashboarding." Absence of consistent logging spec standards continues as a pain point.

### Data Scientist (n=1,014)

| Activity | % Favorable | Change from H2 2025 |
|---|---|---|
| Conduct Data Analysis | 83% | +12 |
| Explore Data | 80% | +16 |
| Communicate Insights | 73% | +4 |
| Understand Business Context | 67% | +7 |
| Experimentation | 64% | +5 |
| Find Data | 61% | +22 |
| Dashboarding | 59% | +4 |

"Find Data" saw the largest DS improvement (+22pp) but remains in yellow. Experimentation is flat — SWEs still depend on DS for experiment design/analysis, and AI hasn't shifted this yet. "Communicate Insights" was also flat; qualitative feedback points to AI-generated comms creating more noise, making it harder for DS to land impact with stakeholders.

## AI Tooling Feedback (by Tool)

### Analytics Agent
Most mentioned data tool. Trust, performance, and fragmentation limit potential.
- Trust gap: confident outputs still require manual verification
- Performance/UX: sessions hang, unclear errors, dated UI
- Fragmentation: users want AA + Datamate + Claude unified

### Datamate
Useful for table discovery, but hallucination and tool overlap with AA limit adoption. Dashboard building via Datamate is "pretty terrible."

### Claude Code
Most rapidly adopted tool, but:
- **DSS-4 and privacy data restrictions block key workflows** for UXR, DS, and DSS roles
- CLI-only interface and complex setup deter non-SWE adoption
- Tool proliferation creates confusion about when to use Claude vs. AA vs. Datamate

> "The tools are very powerful, however, a big blocker is that Claude Code and Nest are not yet approved for DSS-4 level data, which includes user data." — DS IC, RL

## Inefficiency Drivers

All improved significantly from H2 2025. Top-tier pain points (% reporting "a lot" of difficulty):

| Driver | All Data Roles | DE | DS |
|---|---|---|---|
| Frequent ad hoc requests | — | 21% | 29% |
| Memory/capacity limits | — | 11% | 19% |
| Access/privacy friction | — | 18% | 15% |
| Documentation for data artifacts | — | 8% | 20% |
| Privacy review | — | 12% | 10% |
| Combining data sources | — | 4% | 11% |

DS top pain: documentation for data artifacts (20%) and memory/capacity limits (19%). DE top pain: ad hoc requests (21%) and access/privacy friction (18%).

## Recent Hires

94% of recent hires now report AI is more helpful for work at Meta than at prior job (up from 77% in H2 2025). 59% say it's easier to make progress at Meta overall (up from 46%). The AI tooling story is strong for talent attraction, but general ease of progress still lags.

---



---

## Implications for Projects

### Data Access Friction (FRAPS)
- Access/privacy friction improved significantly company-wide but remains top-3 for DEs overall. For Risk, it's concentrated on the DS side (23%), not DE (8%).
- "Combining data sources" being 5x worse for Risk DEs than Meta overall is a FRAPS-adjacent signal — friction isn't just about permissions, it's about the structural difficulty of getting data from multiple risk areas into one place.
- Claude Code's DSS-4 restriction is a named blocker in qualitative feedback, directly relevant to how AI tools interact with Risk-domain data.

### Risk Data AI Enablement
- AI efficiency gains are massive company-wide, but output trust is the #1 concern. This validates the measurement work around eval quality.
- "Identifying key insights" and "identifying the right type of analysis" remaining low (43%) suggests significant opportunity for AI in the analytic judgment layer.
- Claude Code's DSS-4 restriction is explicitly called out as limiting adoption — track resolution.
- Risk DS 3P package friction (30%) could be an AI enablement opportunity if the right tools can abstract away package management.

### Risk Leads Dashboard
- **34% dashboarding satisfaction for Risk DEs is the worst of any org in the survey.** This is the strongest possible validation for the dashboard strategy.
- DEs praised Nest as a "game-changer" — worth evaluating whether Risk dashboard work should lean harder into Nest.
- Risk DS dashboarding (66%) is actually above Meta DS average (59%), suggesting the DE side is where the pain is concentrated.

### Things to Flag for Stephanie
- Risk DE tooling satisfaction gap (-11pp vs. Meta) combined with the dashboarding crisis (34%) is a clear story for leadership.
- "Combining data sources" being 5x worse for Risk DEs than average is the strongest data point for prioritizing data unification / semantic model work.
- Risk DS pain on 3P packages (30% vs. 6%), oncall (25% vs. 5%), and data tool documentation (24% vs. 9%) are unusually elevated — worth investigating whether these are known issues or newly surfaced.
- The trust problem with AI outputs will hit Risk harder than other orgs — in a domain where wrong answers have compliance/safety implications, the bar for AI output trust is higher than in product analytics.
- The divergent DE/DS stories (DEs efficient but tooling-frustrated; DSs well-tooled but struggling to make progress) suggest different intervention strategies are needed for each function.
