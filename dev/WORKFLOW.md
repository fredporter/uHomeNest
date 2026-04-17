# Universal Dev Notes — workflow (uHomeNest)

Applies to **`github.com/fredporter/uHomeNest`**. Default local layout: **`~/Code/uHomeNest/`** with optional sibling **`~/Code/UniversalSurfaceXD/`** (see **`uHomeNest.code-workspace`**).

## 1. Core principle

Separate **thinking**, **building**, and **discarding** into distinct spaces.

| Space | Meaning |
| --- | --- |
| **SYSTEM** | What exists in Git — intentional, shareable |
| **LOCAL** | What you are thinking — private |
| **COMPOST** | What you removed or replaced — local safety net |

## 2. Zones

### System (tracked)

- **`server/`** — Python uHOME server, `pyproject.toml`, `docs/`, tests
- **`matter/`** — Matter / Home Assistant contracts and assets
- **`host/`** — client runtime (`uHOME-client` lineage)
- **`dev/`** — this workflow + Task Forge docs
- Root **`README.md`**, **`AGENTS.md`**, **`DEV.md`**, **`TASKS.md`**, **`docs/MONOREPO.md`**

### Local — `.local/` (untracked, gitignored)

Notes, experiments, debug scratch. **Must not** hold production code or final docs.

### Compost — `.compost/` (untracked, gitignored)

Replaced files, dead experiments, temporary backups. **Must not** be referenced by active build/docs.

## 3. Flow

```text
.local → TASKS.md → implementation → .compost (when replacing)
```

1. **Think** — `.local/…`
2. **Formalise** — **`TASKS.md`**
3. **Build** — per package under `server/`, `matter/`, or `host/` (see each **`README.md`**)
4. **Discard copies** — `.compost/…`

## 4. Subtree TASKS

Packages may define **`server/TASKS.md`**, etc., only if a subtree needs its own backlog; otherwise use **repo root `TASKS.md`** with prefixed IDs (e.g. `UHN-SRV-001`).

## 5. Validation

- **Server:** `server/scripts/run-uhome-server-checks.sh` (from `server/`)
- **Matter / host:** `matter/scripts/run-uhome-matter-checks.sh`, `host/scripts/run-uhome-client-checks.sh` when present

Run from the subtree or via workspace tasks.
