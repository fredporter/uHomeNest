# uHOME-server Architecture

uHOME-server is the **always-on household infrastructure node** for the uDOS
family. It is the Linux-based local runtime that owns the local-network runtime,
kiosk UI host, media services, vault exposure, Beacon Activate content surfaces,
and Steam-side host role.

uHOME-server is designed to operate independently of cloud services, with
optional integration through the Empire extension.

## Main Areas

- `services/` exposes runtime and service surfaces.
- `scheduling/` holds recurring execution logic.
- `modules/` organizes service modules and extensions.
- `config/` stores runtime configuration.
- `config/base-runtime-profile.example.json` is the starter checked-in base
  runtime profile.
- `src/uhome_server/` remains the active standalone server package while the
  repo converges on the v2 spine.
- `scripts/run-uhome-server-checks.sh` is the activation validation entrypoint.
- `apps/tablet-kiosk/` is the tablet-and-living-room kiosk application surface.
- `apps/dashboard/` is the household dashboard UI surface.

---

## Topology

Preferred deployment: Linux host on local network.

Linux host owns:

- uHOME-server (this repo)
- Wizard (when deployed)
- Empire extension
- Jellyfin media server
- Matter subsystem (via `uHOME-matter`)

Windows "toybox" side (optional):

- Steam and auxiliary gaming software
- Windows is **never** the orchestration authority

---

## Kiosk Environment

uHOME-server provides a **Steam-console-style launcher interface** designed
for TVs, tablets, and living-room displays.

Primary design principle: **controller-first navigation**.

Supported input:

- Xbox controllers, PlayStation controllers, Bluetooth HID gamepads
- keyboard, mouse, touch

Gamepad is the **primary interaction model**.

### UX Surfaces

**Living-Room Launcher** — tile-based, big-screen-friendly, controller-first.
Launch targets: media, games, automation, vault content, dashboards.

**Thin-GUI Kiosk Mode** — can be pushed or streamed to tablets, TVs, and
secondary displays. Shows: job status, dashboards, playback status, automation panels.

**Media Panel** — Jellyfin library browsing, playback controls, queue management.

**Jobs / Scheduling Panel** — scheduled jobs, automation status, retries/failures.
Jobs may originate from Empire, Wizard, or local automation scripts.

---

## Included Services

### Jellyfin

Jellyfin is the primary media server:

- media library hosting
- local streaming and playback metadata
- household media management
- integrates directly into kiosk UI surfaces

### Steam / Game Services

uHOME-server supports Steam presence and gaming launch surfaces:

- Steam library access
- remote play support
- game launcher integration
- controller-first navigation

---

## Networking Modes

### Default Mode

Standard home networking. Supports WiFi, Ethernet, existing routers.
No Wizard required.

### Wizard-Managed Networking

Wizard defines advanced networking profiles. uHOME-server **hosts the runtime
services** for those profiles.

| Profile | Visibility | Access | Internet |
| --- | --- | --- | --- |
| Beacon | Public / open | Local vault only | No |
| Crypt | Visible, password-protected | Local vault | No |
| Tomb | Hidden, discovery-based | No public internet | No |
| Home | Private household, password-protected | Household devices | Optional |

Wizard defines policies. uHOME-server owns the runtime network services.
See `uDOS-wizard/docs/v2.0.4-sibling-route-set.md` for Wizard networking contracts.

---

## Extension Model

| Extension | Responsibility |
| --- | --- |
| `uHOME-matter` | Home Assistant integration, Matter device support, device graph, room/zone logic, scenes and automations |
| `uHOME-empire` | Vault mirroring, Google API integration, HubSpot API integration, webhook listeners, scheduled jobs, binder-aware routing |

Extensions layer on top of uHOME-server without replacing base runtime ownership.

---

## Contract Edges

- `uDOS-core` defines canonical vault, task, workflow, and binder semantics.
- `sonic-screwdriver` owns deployment, hardware bootstrap, and install
  planning into this runtime.
- `uDOS-wizard` provides network-facing contracts while `uHOME-server` owns the
  local-network runtime and local Beacon Activate content surfaces.
- `uHOME-matter` layers on top for Matter and Home Assistant extension
  contracts without replacing the base runtime owner.
- `uHOME-empire` layers on top for Google and HubSpot sync plus console CRM and
  workflow management.

---

## Design Principles

- local-first
- controller-first UX
- modular extensions
- no mandatory cloud dependency
- server-hosted automation

## Transitional Note

Some Matter-adjacent or Home Assistant runtime code still exists here under
legacy module and service roots. In v2 those surfaces are treated as
transitional local runtime support, while new contract and clone definitions
belong in `uHOME-matter`.
