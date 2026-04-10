# uHomeNest

**uHomeNest** is the **monorepo** for the **uHOME** product line: household media, kiosk/thin UI, LAN server, Matter/Home Assistant bridges, and the lightweight client runtime.

## Layout

| Directory | Former standalone repo | Role |
| --- | --- | --- |
| **`server/`** | `uHOME-server` | LAN-first server, thin UI, services, docs, wiki |
| **`matter/`** | `uHOME-matter` | Matter / Home Assistant contracts and bridge assets |
| **`host/`** | `uHOME-client` | Lightweight client runtime and contract consumption (local network) |

Each subtree keeps its **existing package layout** and documentation from the pre-monorepo repos. Historical Git history for those repos remains on GitHub until those repositories are archived.

## Clone

```bash
git clone https://github.com/fredporter/uHomeNest.git
cd uHomeNest
```

## Development

- **UDN / tasks:** [`DEV.md`](DEV.md), [`dev/WORKFLOW.md`](dev/WORKFLOW.md), [`dev/TASK_FORGE.md`](dev/TASK_FORGE.md), **[`TASKS.md`](TASKS.md)**
- **Python server:** see `server/README.md`, `server/QUICKSTART.md`
- **Matter:** see `matter/README.md`
- **Client / host runtime:** see `host/README.md`
- **Workspace:** open **`uHomeNest.code-workspace`** in Cursor/VS Code to include sibling **UniversalSurfaceXD** (USXD lab + interchange) alongside this repo.

## Naming

- **uHomeNest** — this repository (nest of uHOME packages).
- **uHOME** — product name (unchanged in docs inside each package).

See **`docs/MONOREPO.md`** for migration notes from `uHOME-family/` sibling checkouts.
