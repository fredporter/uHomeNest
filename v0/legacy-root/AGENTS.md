# Agent notes — uHomeNest

**Repository name:** **uHomeNest** (**v3.9.x**, see root `VERSION`). **Product:** **uHOME**. Prefer **uHomeNest** when referring to this Git repo; reserve **`uHOME-server`** for legacy JSON wire strings only.

## What this is

**uHomeNest** is a **monorepo** replacing separate clones under `uHOME-family/`:

- **`server/`** — uHOME server (Python, docs, wiki) — primary operational surface
- **`matter/`** — Matter / Home Assistant integration contracts
- **`host/`** — client runtime (formerly **uHOME-client**); “host” = local-network consumer of server contracts

## How to work

1. Prefer **path-scoped** edits inside `server/`, `matter/`, or `host/` unless changing monorepo-wide policy.
2. **Tracked intent** → root **`TASKS.md`** (Task Forge: **`dev/TASK_FORGE.md`**). **Method** → **`DEV.md`**, **`dev/WORKFLOW.md`**.
3. **Thinking** → **`.local/`** (gitignored). **Replaced material** → **`.compost/`** (gitignored).
4. Each subtree may retain its own **`README.md`** and scripts; read the subtree’s root before large changes.
5. **Multi-root editor:** **`uHomeNest.code-workspace`** adds sibling **UniversalSurfaceXD** for USXD / interchange work next to uHOME packages.

## Non-goals

- This repo does **not** subsume **SonicScrewdriver** (USB/bootstrap) or generic uDOS governance — only uHOME product code that lived in the three former repos.
