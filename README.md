# uHomeNest

`uHomeNest` is reset to a clean **v1.0.0** baseline for a decentralised home network Linux stream server.

Core focus:
- Jellyfin as media backbone
- `~/media/` vault-style library
- Minimal browser surface powered by Tailwind CSS
- USXD console layout for controller-first UX

## Version

- Repo release version: `VERSION` (`1.0.0`)
- This is a fresh-start architecture line; legacy content is treated as `v0` reference material.

## Structure

- `server/` - core streaming server modules (Jellyfin, API, media scanner/indexer/watcher)
- `ui/` - Tailwind + USXD browser surface
- `media-vault/` - `~/media/` schema, example structure, validator
- `scripts/` - install/start/stop/healthcheck operations
- `docs/` - architecture, deployment, media vault, USXD references
- `tests/` - shell-based integration smoke tests
- `v0/` - archive references for pre-1.0.0 material

## Clean Remote Rules

- Commit only source, docs, and intentional fixtures in active v1 paths.
- Keep runtime/local state out of Git (`logs/`, `tmp/`, `runtime/`, `state/`, local DBs, generated media index files).
- Keep package/build outputs out of Git (`dist/`, `build/`, `node_modules/`, generated `.she`/`.delta` bundles).
- Treat `v0/` as archive reference only; do not route active runtime logic through it.

## Quick Start

```bash
./scripts/install.sh
./scripts/start.sh
curl http://localhost:7890/api/health
```

See:
- `QUICKSTART.md`
- `docs/ARCHITECTURE.md`
- `docs/DEPLOYMENT.md`
- `docs/MEDIA_VAULT.md`
- `docs/USXD.md`
- `docs/ROADMAP.md`
- `dev/ROADMAP-ROUNDS.md`
- `TASKS.md`
