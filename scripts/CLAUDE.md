# Scripts

Regen scripts for generated files, like miles/ `generate_collection.py`.

## Conventions

- Python scripts use `~/.venvs/miles` or note venv in reference
- Mark output files as `<!-- GENERATED from <source> — do not hand-edit -->`
- Source-of-truth lives elsewhere (Discogs, Drive, etc.), script is just formatter
- Document regen command in script header + in folder's CLAUDE.md
- `git diff` review after regen

## Candidates

- `generate_pod_digest.py` — reads ~/My Drive/DataRiskPods/ and writes areas/data_risk/pod_digest_YYYY_MM_DD.md
- `generate_status.py` — pulls from project tracker and writes snapshot

Don't build until needed — manual proves daily first.
