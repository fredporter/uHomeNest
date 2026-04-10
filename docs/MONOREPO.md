# uHomeNest monorepo migration

## Engineering (UDN)

Tracked workflow lives under **`dev/`** (`WORKFLOW.md`, `TASK_FORGE.md`), with **`DEV.md`** and **`TASKS.md`** at repo root. Open **`uHomeNest.code-workspace`** to pair this monorepo with sibling **UniversalSurfaceXD** (USXD).

## Mapping (standalone → monorepo path)

| Old repo (GitHub) | New path | Notes |
| --- | --- | --- |
| `fredporter/uHOME-server` | `server/` | Default path for server docs and Python package |
| `fredporter/uHOME-matter` | `matter/` | Bridge contracts and Matter-facing assets |
| `fredporter/uHOME-client` | `host/` | Renamed folder only; still the **client** runtime in prose |

## Local layout change

Previously, many setups used a parent folder (e.g. `uHOME-family/`) with **three sibling git clones**. That layout is replaced by **one clone** of **uHomeNest** with three subtrees.

A backup of the old sibling folder may exist as `uHOME-family.pre-uHomeNest-monorepo` under `~/Code/` after migration.

## Git history

The first **uHomeNest** commit imports file trees without preserving per-package `git` history in the monorepo. To inspect old line-by-line history, use the archived standalone repositories on GitHub until they are retired.

## Next steps (operator)

1. Create **`https://github.com/fredporter/uHomeNest`** (empty), add `origin`, push this repo.
2. When satisfied, **archive** `uHOME-server`, `uHOME-matter`, and `uHOME-client` on GitHub with a pointer to **uHomeNest**.
3. Update any CI, bookmarks, or docs that still reference the old repo URLs.
