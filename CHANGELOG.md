# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-04-16

### Changed

- Reset repository direction to the v1.0.0 fresh-start architecture focused on Jellyfin, a `~/media/` vault model, Tailwind browser surface, and USXD controller-first console layout.
- Added clean baseline scaffolding for `server/`, `ui/`, `media-vault/`, `scripts/`, `docs/`, and `tests/` paths aligned to the new objective.
- Added `v0/` archive pointer/manifest scaffolding to preserve pre-1.0.0 material as historical reference.
- Archived legacy top-level trees into `v0/` and cleaned the active root to the v1-only structure.
- Added planning assets for next execution cycles: `docs/ROADMAP.md`, `dev/ROADMAP-ROUNDS.md`, and refreshed `DEV.md`/`TASKS.md`.
- Modularized API routing into handler modules under `server/api/handlers/` with a dedicated `server/api/router.py`.
- Added deterministic media vault fixture structure under `media-vault/example/` and a validation test script `tests/media_vault_validate_test.sh`.
- Added Sonic Home Express future lane planning to roadmap docs and tracked brief `docs/UDN-SONIC-001.md`.
- Added route-registry style API dispatch with contract test coverage and upgraded Jellyfin orchestration to real runtime control paths (docker compose, docker container, or systemd fallback).
- Added persistent media indexing with incremental change stats (`added`, `changed`, `removed`) and watcher-driven index refresh loop.
- Completed Round 2 API data wiring: media browse/search now read persisted index data; started Round 3 by adding playback target/media request contracts on `/api/playback/start` and `/api/playback/stop`.
- Added Round 3 now-playing session state so playback start/stop mutates shared state exposed via `GET /api/now-playing`.
