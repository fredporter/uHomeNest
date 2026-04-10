# Archive: `uHOME-app-ios` (local checkout removed)

**Captured:** 2026-04-10  
**Previous path:** `~/Code/uHOME-family/uHOME-app-ios`  
**Remote (last known):** `git@github.com:fredporter/uHOME-app-ios.git`  
**VERSION file:** `2.3.0`

## Role

iOS application lane for **uHOME** mobile and kiosk-style surfaces. Stated purpose: consume **`uHOME-client`** runtime contracts and **`uHOME-server`** services; **not** own public uDOS/uHOME architecture.

## Tech stack

- **Swift Package Manager** (`Package.swift`, swift-tools-version **5.10**)
- Platforms: **iOS 17+**, **macOS 10.15+** (package platforms)
- Product: **library** `uHOME-app-ios` → target **`App`**
- Targets: **`App`** (depends on Core, UI, Integrations), **`Core`**, **`UI`**, **`Integrations`**, tests **`AppTests`** (uses **`swift-testing`**)
- Sparse Swift surface at removal: **4** `.swift` files under `Sources/` (scaffold / contract-style structs)

## Layout (high level)

| Area | Role |
| --- | --- |
| `Sources/App/` | `UHomeAppModule` — composes runtime + kiosk + endpoint profiles |
| `Sources/Core/` | `UHomeRuntimeProfile` — default modes `integrated-udos`, `standalone-uhome`; owner `uHOME-server`; primary surface `mobile-reader` |
| `Sources/UI/` | `UHomeKioskSurface` — e.g. `living-room-kiosk`, `fullscreen` |
| `Sources/Integrations/` | `UHomeServerEndpointProfile` — default `http://127.0.0.1:8000`, launcher path `/api/launcher/status` |
| `Tests/AppTests/` | Test target present |
| `Docs/` | **`Docs/activation.md`** — activation tranche, **`run-uhome-app-ios-checks.sh`** validation |
| `scripts/` | Validation entrypoint |
| `config/` | Checked-in configuration |
| `@dev/` | Private dev rounds / notes (repo-local) |
| `wiki/` | Wiki mirror |

## Behaviour at removal time

No full SwiftUI/UIKit app shell was evident in the small file count; the package centred on **typed profiles** and a **`launchSummary()`** string on `UHomeAppModule` (runtime owner, kiosk surface id/presentation, launcher URL).

## Contracts & docs to preserve elsewhere

- Activation and boundaries: **`Docs/activation.md`**
- Relation to **`uHOME-client`** / **`uHOME-server`** in root **`README.md`**
