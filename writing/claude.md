# Claude Writing Guide for Tony Harper

## File Organization

### Directory Structure

Writing is organized by type:

- `essays/` — Personal essays, reflections, blog-style posts
- `proposals/` — Technical proposals and 1-pagers
- `decision-docs/` — Decision documents, option analyses
- `comms/` — Team communications, announcements, meeting materials

### File Naming

Files use date-first naming: `YYYY-MM-DD-title-in-lowercase-kebab-case.md`

- Use the publication date if known
- Use `YYYY-MM` if only the month is known (e.g., `2026-03-engineering-review.md`)
- For meeting-related docs, use the meeting date

### Frontmatter

Every file includes YAML frontmatter:

```yaml
---
title: The Full Title
date: 2026-02-26
audience: engineers | leadership | general
status: draft | review | published
tags: [relevant, topic, tags]
---
```

- **title**: The display title of the piece
- **date**: Publication or meeting date (YYYY-MM-DD)
- **audience**: Who this is written for — `engineers`, `leadership`, or `general`
- **status**: Current state — `draft`, `review`, or `published`
- **tags**: Lowercase, hyphenated topic tags

## Voice and Tone

Tony writes in a direct, conversational-but-professional register. He uses contractions naturally and doesn't over-formalize. His tone is warm without being soft — he states positions clearly and isn't afraid to be candid about uncertainty, limitations, or disagreement. He's reflective without being sentimental.

When writing personally, he favors simple declarative sentences that land with weight: "Then I graduated into the Great Recession." When writing technically, he's structured and thorough but still sounds like a person talking, not a document generating itself.

He does not use jargon for its own sake, but is comfortable with technical terms when they're the right words. He avoids corporate buzzwords and empty superlatives.

## Structure

Tony is an organized thinker and writer. His posts typically follow a pattern:

- **Lead with context or a TLDR** — he often opens with a brief summary of what the post covers and why it matters, before going into detail.
- **Clear headers and sections** — he breaks complex topics into labeled sections. He uses bold for emphasis, bullet points for lists, and tables when comparing options.
- **Problem → Constraints → Options → Recommendation** — in technical writing, he frames decisions by laying out the problem, the constraints, the options considered (including ones rejected and why), and the recommended path.
- **Acknowledgments** — he is generous with credit, calling out individuals by name and describing their specific contributions. He doesn't do this performatively; he's specific about what each person did.

## Sentence Style

- Mix of short punchy sentences and longer explanatory ones. The short ones often carry the emotional or rhetorical weight.
- Uses em dashes frequently — often to insert a clarification or aside mid-sentence.
- Comfortable with parentheticals for secondary detail.
- Doesn't over-qualify statements. Says "this is what we should do" rather than "it might potentially be worth considering."
- Will occasionally use a one-line paragraph for emphasis or a turning point.

## Personal and Reflective Writing

When writing about himself or his career, Tony is candid and introspective. He references his background openly — growing up in Kentucky, his family's expectations, learning to program on a VTech Precomputer 1000, majoring in Computer Engineering and Computer Science, graduating into the Great Recession, building a career in data warehouse engineering and then management.

He frames career and personal growth as a journey of learning what he actually wants, not just what's expected. He's honest about things he struggled with (making friends as a kid, not knowing what he wanted from his career until later in life) without being self-pitying about it.

He connects personal experience to professional insight naturally — his childhood programming connects to his current AI enthusiasm; his data warehouse training connects to his views on AI readiness.

## Technical Writing

- Always grounds technical recommendations in the "why" — the problem statement and constraints come before the solution.
- Provides concrete artifacts: SQL queries, links to dashboards, sample code, specific table names.
- Distinguishes between short-term and long-term approaches, and explains the tradeoffs of each.
- Acknowledges what's uncertain or unknown rather than papering over gaps.
- When presenting options, includes rejected options and explains why they were rejected. This provides transparency and lets the reader understand the decision-making process.

## Things to Avoid

- Don't use empty corporate language ("leverage synergies," "drive alignment," "move the needle") — Tony uses plain language even for complex organizational topics.
- Don't be overly cautious or hedge everything. Tony states his views.
- Don't add unnecessary emoji or exclamation points. His enthusiasm comes through in word choice, not punctuation.
- Don't over-explain simple points or pad for length.
- Don't strip out personality in technical writing — Tony's technical posts still sound like him.

## Interests and Background (for context, not to shoehorn in)

- Kentucky roots; parents steered him toward engineering
- Learned BASIC at eight on a VTech Precomputer 1000, copying programs from 3-2-1 Contact magazine
- Computer Engineering & Computer Science degree; favorite class was Artificial Intelligence
- Career in data warehouse engineering, then management, then Meta
- Deep interest in data privacy and data warehouse governance
- Currently leading Risk Data Engineering at Meta
- Music: progressive rock (Dream Theater, Jethro Tull), folk rock (The Decemberists), broad tastes
- Audio equipment enthusiast (KEF, Marantz, Technics turntables)
- Dog person
- Low risk tolerance, values stability, but intellectually adventurous
