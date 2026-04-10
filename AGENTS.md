# Agent notes — uHomeNest

## What this is

**uHomeNest** is a **monorepo** replacing separate clones under `uHOME-family/`:

- **`server/`** — uHOME server (Python, docs, wiki) — primary operational surface
- **`matter/`** — Matter / Home Assistant integration contracts
- **`host/`** — client runtime (formerly **uHOME-client**); “host” = local-network consumer of server contracts

## How to work

1. Prefer **path-scoped** edits inside `server/`, `matter/`, or `host/` unless changing monorepo-wide policy.
2. Each subtree may retain its own **`TASKS.md`**, **`README.md`**, and tooling; read the subtree’s root before large changes.
3. Scratch: **`.local/`** / **`.compost/`** remain per-family conventions where those repos already used them (see subtree `README` / `.gitignore`).

## Non-goals

- This repo does **not** subsume **SonicScrewdriver** (USB/bootstrap) or generic uDOS governance — only uHOME product code that lived in the three former repos.
