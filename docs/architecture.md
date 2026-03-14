# uHOME-server Architecture

uHOME-server is the persistent local-service runtime for the family.

## Main Areas

- `services/` exposes runtime and service surfaces.
- `scheduling/` holds recurring execution logic.
- `modules/` organizes service modules and extensions.
- `config/` stores runtime configuration.
- `src/uhome_server/` remains the active standalone server package while the
  repo converges on the v2 spine.
- `scripts/run-uhome-server-checks.sh` is the activation validation entrypoint.
