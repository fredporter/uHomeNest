# Roadmap Dev Rounds

This plan operationalizes the v1.0.0 brief into near-term rounds.

## Round 1 - Foundation hardening (2-3 days)

- Finalize repo structure and archive boundaries
- Replace API placeholders with modular handlers
- Add deterministic media vault validation and sample fixtures
- Exit criteria:
  - `README.md`, `QUICKSTART.md`, and `docs/` are aligned
  - `tests/ui_smoke_test.sh` and `tests/media_scan_test.sh` pass

## Round 2 - Media indexing core (3-4 days)

- Implement scanner -> indexer pipeline against `~/media/`
- Produce `.media-index.json` with stable schema
- Add search endpoint behavior over generated index
- Exit criteria:
  - `/api/media/browse` and `/api/media/search` return real data
  - `media-vault/validate.sh` is part of setup checks

## Round 3 - Playback and UI integration (3-4 days)

- Wire playback start/stop orchestration paths
- Add USXD runtime loader for launcher/media/now-playing surfaces
- Implement controller navigation bindings (dpad, A/B/X/Y)
- Exit criteria:
  - Browser launcher renders from `ui/usxd/launcher.json`
  - Playback endpoints report actionable state transitions

## Round 4 - Deployment readiness (2-3 days)

- Implement production-grade `scripts/install.sh`
- Add service units and startup dependencies
- Add end-to-end smoke check for install -> start -> health
- Exit criteria:
  - Fresh Ubuntu 22.04/24.04 install passes quickstart flow
  - `curl /api/health` returns `{\"status\":\"ok\"}` post-install
