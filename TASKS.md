# TASKS.md — uHomeNest

Active work surface (UDN / Task Forge v1). **Syntax:** [`dev/TASK_FORGE.md`](dev/TASK_FORGE.md).

## Backlog

### Q2 2024 Priorities (April-June)

#### CI/CD Infrastructure
- [ ] [UHN-CI-001] Establish GitHub Actions workflows for testing and deployment #infra
- [ ] [UHN-CI-002] Implement branch protection rules for main branch #infra
- [ ] [UHN-CI-003] Set up automated testing pipeline with pytest #testing
- [ ] [UHN-CI-004] Configure release automation with semantic versioning #infra

#### Media & Jobs Foundation
- [ ] [UHN-MEDIA-001] Design DVR rule model and schedule backend #media
- [ ] [UHN-MEDIA-002] Implement basic job queue for recording and post-processing #media
- [ ] [UHN-MEDIA-003] Harden Jellyfin integration with comprehensive tests #media
- [ ] [UHN-MEDIA-004] Design library path model for local disks and mounted partitions #media

#### Documentation Enhancement
- [ ] [UHN-DOCS-001] Update thin UI documentation with default port information #docs
- [ ] [UHN-DOCS-002] Create index page for safe docs/ paths #docs
- [ ] [UHN-DOCS-003] Add LAN-only guard documentation for thin routes #docs
- [ ] [UHN-DOCS-004] Update client API documentation #docs

### Q3 2024 Priorities (July-September)

#### Decentralized LAN Enhancements
- [ ] [UHN-LAN-001] Design failover/election model for multiple nodes #lan
- [ ] [UHN-LAN-002] Implement basic distributed library indexing #lan
- [ ] [UHN-LAN-003] Add replication capabilities for critical data #lan
- [ ] [UHN-LAN-004] Enhance node/storage topology management #lan

#### Client Integration
- [ ] [UHN-CLIENT-001] Finalize stable API contracts for Android/TV/Apple TV apps #clients
- [ ] [UHN-CLIENT-002] Document launcher and session semantics #clients
- [ ] [UHN-CLIENT-003] Implement end-to-end testing for playback handoff #clients
- [ ] [UHN-CLIENT-004] Create comprehensive client integration guide #docs

## In Progress

<!-- Move items here when actively coding -->

## Blocked

<!-- ↳ Notes: reason -->

## Done

- [x] [UHN-META-006] Rename contributor/education brief files; stubs + link sweep #docs
- [x] [UHN-META-005] Complete uHomeNest v3.9 naming in docs, metadata, briefs; MONOREPO canonical names #docs
- [x] [UHN-META-004] Consolidate v4 plan: canonical `ROADMAP-V4.md`, `UHOME-DEV-ROADMAP.md` as redirect #docs
- [x] [UHN-META-003] Retire pre-v4 phase/`@dev` docs and unused `uhome/` scaffold; v4-only dev entry + compost manifest #docs
- [x] [UHN-META-002] uHomeNest **v3.9.0**: `VERSION`, universal dev + v4 roadmap docs, USXD uHOME surface scaffold, compost guidance #docs
- [x] [UHN-META-000] Add `dev/` workflow docs, `DEV.md`, root `TASKS.md`, and `uHomeNest.code-workspace` (USXD sibling) #docs
