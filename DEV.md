# Development method — uHomeNest

This monorepo follows **Universal Dev Notes (UDN)** shared across `github.com/fredporter/`.

- **Product version:** root [`VERSION`](VERSION) (**uHomeNest 3.9.x**); Python packages use `pyproject.toml`.
- **Universal dev + USXD:** [`dev/UNIVERSAL-DEV.md`](dev/UNIVERSAL-DEV.md)
- **Workflow:** [`dev/WORKFLOW.md`](dev/WORKFLOW.md)
- **Task format:** [`dev/TASK_FORGE.md`](dev/TASK_FORGE.md)
- **Monorepo migration notes:** [`docs/MONOREPO.md`](docs/MONOREPO.md)

## Zones

| Zone | Path | In Git |
| --- | --- | --- |
| Server implementation | `server/` | yes |
| Matter bridges | `matter/` | yes |
| Host / client runtime | `host/` | yes |
| Dev standards (UDN) | `dev/` | yes |
| **Active tasks** | **`TASKS.md`** | yes |
| Private notes | `.local/` | **no** |
| Replaced work | `.compost/` | **no** |

## Editor workspace

Open **`uHomeNest.code-workspace`** (repo root) in Cursor/VS Code to load **uHomeNest** and sibling **UniversalSurfaceXD** for interchange / lab work alongside server and contracts.
