# Composting legacy docs and scripts (`.compost/`)

**`.compost/`** at the repo root is **gitignored**. Use it for **local** copies of superseded files after you replace or delete them in Git — not as a second source of truth.

## When to compost

- You merged content into a newer doc and the old file is redundant.
- You replaced a one-off script with a maintained path under `scripts/`.
- You need a timestamped backup before a risky delete (copy here first).

## Suggested candidates (optional)

These are **archival or tombstone** notes; move **copies** to `.compost/<date>-<name>/` if you retire the tracked originals:

- [`archive-uHOME-app-android.md`](archive-uHOME-app-android.md), [`archive-uHOME-app-ios.md`](archive-uHOME-app-ios.md) — already marked archive; keep in Git until policy says otherwise.
- Long **phase** session reports under `docs/architecture/PHASE-*` — historical; compost locally if you trim the tree.

Do **not** compost secrets, production configs, or anything that must stay in backup outside the repo.

## One-liner (example)

```bash
mkdir -p .compost/$(date +%Y%m%d) && cp path/to/old-file.md .compost/$(date +%Y%m%d)/
```

After verifying the copy, remove or rewrite the original in a normal commit.
