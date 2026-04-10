# Archive: `uHOME-app-android` (local checkout removed)

**Captured:** 2026-04-10  
**Previous path:** `~/Code/uHOME-family/uHOME-app-android`  
**Remote (last known):** `git@github.com:fredporter/uHOME-app-android.git`  
**VERSION file:** `2.3.0`

## Role

Android application lane for **uHOME** mobile and kiosk-style surfaces. Stated purpose: consume **`uHOME-client`** runtime contracts and **`uHOME-server`** services; **not** own public uDOS/uHOME architecture.

## Tech stack

- **Gradle Kotlin** root; Android Gradle Plugin **8.5.0**, Kotlin **1.9.24**
- Single included module: **`:app`** (`settings.gradle.kts`)
- **App:** `applicationId` / namespace **`com.uhome.android`**, `minSdk` 28, `compileSdk` / `targetSdk` 34, Java **17**
- Dependencies (examples from `app/build.gradle.kts`): AndroidX core, AppCompat, Material

## Layout (high level)

| Area | Role |
| --- | --- |
| `app/` | Android application module |
| `feature-kiosk/`, `feature-player/`, `feature-reader/` | Feature lanes (scaffold / README-led) |
| `integrations/` | Integration lane |
| `docs/` | Operator docs; **`docs/activation.md`** describes “activation” tranche and validation |
| `scripts/` | **`run-uhome-app-android-checks.sh`** — repo validation entrypoint |
| `config/` | Checked-in configuration |
| `@dev/` | Private dev rounds / notes / requests (repo-local) |
| `wiki/` | Wiki mirror |

## Behaviour at removal time

The main UI was a **minimal `MainActivity`**: full-screen **`TextView`** showing a short “uHOME Android” launch summary (family modes `standalone-uhome`, `integrated-udos`; runtime owner `uHOME-server`).  
`UHomeAndroidApp` extended **`Application`** (empty body).

**Note:** The tree also contained **`com/omd/android/MainActivity.kt`** alongside `com/uhome/android/` — likely legacy or duplicate package; worth verifying if the repo is revived.

## Contracts & docs to preserve elsewhere

- Activation and boundaries: **`docs/activation.md`**
- Relation to **`uHOME-client`** / **`uHOME-server`** spelled out in root **`README.md`**
