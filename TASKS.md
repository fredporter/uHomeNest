# TASKS - v1 execution board

## Backlog

- [ ] [UHN-R1-005] Add real Jellyfin start/stop wiring in `server/jellyfin/orchestrate.sh` #infra
- [ ] [UHN-R2-004] Add media index persistence and incremental update logic #feature
- [ ] [UHN-R3-004] Implement `/api/playback/start` target selection #feature
- [ ] [UHN-R4-003] Add service install units for Ubuntu 22.04/24.04 #infra

## In Progress

- [ ] [UHN-R1-003] Wire API placeholder handlers to modular router flow #core

## Blocked

- [ ] [UHN-R3-002] Controller runtime bindings for dpad/A/B/X/Y in browser
  - Blocked on initial `usxd-runtime.js` implementation details.

## Done

- [x] [UHN-R0-001] Archive pre-v1 codebase into `v0/` and push `v0-beta` tag
- [x] [UHN-R0-002] Scaffold v1 top-level server/ui/media-vault/scripts/docs/tests
- [x] [UHN-R1-001] Stabilize fresh v1 repository structure and docs #meta
- [x] [UHN-R1-002] Add deterministic media-vault fixture coverage #core
