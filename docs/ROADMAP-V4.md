# Roadmap — uHOME / uHomeNest (v4 line)

This document is the **uHomeNest-side** narrative for the **v4** product line. Execution detail stays in issue trackers and **[`UHOME-DEV-ROADMAP.md`](UHOME-DEV-ROADMAP.md)**; **UniversalSurfaceXD** owns **[USXD v4 lab + interchange](https://github.com/fredporter/UniversalSurfaceXD/blob/main/docs/roadmap-v4.md)** separately.

## How v4 is split

| Layer | Repository | Role |
| --- | --- | --- |
| **Runtime** (LAN server, thin UI, Matter, host) | **uHomeNest** | Ship household media, kiosk/thin surfaces, contracts |
| **Surface language + UX lab** | **UniversalSurfaceXD** | JSON interchange, browser mockup, Storybook — **not** the production uHOME server runtime |

v4 **does not** require uDOS **#binder / Workspace** as operator UX; thin reading stays **Markdown + Tailwind Prose** (see [`uHOME-server-dev-brief.md`](uHOME-server-dev-brief.md)).

## Current baseline (uHomeNest **3.9.x**)

- Monorepo layout: **`server/`**, **`matter/`**, **`host/`**, shared `docs/`, `src/uhome_server/`.
- Thin routes and automation contracts as documented in [`thin-ui-feature-completion.md`](thin-ui-feature-completion.md).
- Dashboard and client API expectations in [`ui/UHOME-DASHBOARD.md`](ui/UHOME-DASHBOARD.md).

## Near-term (v4 direction)

1. **Interchange-aligned thin UX** — Author and review kiosk-oriented layouts in USXD (`surface-uhome-thin-kiosk.json`, composer **`?sample=uhomeThin`**), then implement against real APIs in server/host repos.
2. **Hardening** — File-backed registries toward clearer operational guarantees (see limitations in [`UHOME-DEV-ROADMAP.md`](UHOME-DEV-ROADMAP.md)).
3. **Cross-repo docs** — Prefer links over duplication; monorepo [`README.md`](../README.md) + [`docs/README.md`](README.md) as indexes.

## Version tags

- **uHomeNest product line:** root **`VERSION`** (e.g. **3.9.0**).
- **Python `uhome-server` package:** `pyproject.toml` / `server/pyproject.toml` (independent semver).

## Retired material

Pre-v4 **phase milestone** Markdown, **migration status** snapshots, and tracked **`@dev/`** binder trees were removed from Git in **2026-04** (optional local archive: **`.compost/cleanup-2026-04-10/`**). See [`../dev/COMPOST-LEGACY.md`](../dev/COMPOST-LEGACY.md).
