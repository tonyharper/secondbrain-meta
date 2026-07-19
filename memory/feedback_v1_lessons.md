# Feedback — v1 Lessons

Source: debrief of cal/ v1 that stalled.

- **Dual source of truth (para/ + projects/) was fatal.** PARA said source is ~/secondbrain/para synced via GDrive, projects/ said flat list. Never clear which to use. Fix: single structure, folder=domain, CLAUDE.md=contract per folder.

- **Context sync as pipeline was homework.** config.yaml 190 lines tracking authors/groups, manifest.yaml 300 lines, triage files daily, post_sync_status_update.md requiring rewrite of all status.md files. Never earned keep — produced artifacts to triage. Fix: on-demand fetch only via meta google.docs get when ingesting, link + TLDR only in repo.

- **Status files as obligation.** Designed to be rewritten after each sync with opinions, heat maps. If you don't sync, they go stale and feel broken. Fix: overview.md kept current via meeting ingestion, not daily rewrite. Projects.md checkboxes like home/renovation pattern in miles/.

- **Root tasks.md died.** Same lesson as miles/: real todos live in project folders, not root. Fix: projects/*/projects.md Active/On Hold/Complete.

- **Para gitignored but essential.** Para was excluded from git, only in GDrive via rclone. Risk if Drive sync breaks, no version history. Fix: everything Tier 1 in git (private GitHub), sensitive Tier 2 stays in Drive as link only, Tier 3 private/ local-only gitignored intentionally.

- **Writing voice protection missing initially?** v1 had writing/claude.md but not enforced in root CLAUDE.md. Fix: root CLAUDE.md explicitly defines where Cal can/can't draft, proofread-only quotes original exactly.

- **No typed memory.** Old system had no memory/ — learnings lost on compaction. Fix: memory/ with feedback_, project_, person_, reference_ + MEMORY.md index, version-controlled.

- **Design for retrieval.** Personal brain works because tomorrow requires today's note: packing list at airport, wine calendar, deadwax decode at store. Work v1 was archive, not retrieval tool. Fix: 3 workflows that must earn keep — meeting ingestion, doc ingestion, morning pull. If folder doesn't serve one, delete it.
