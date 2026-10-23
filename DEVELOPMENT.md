# Local Development Guide

How to preview the VibeLearning website on your machine, edit content safely, and
understand what CI does when you push.

---

## The one important rule

> **Edit files at the repository root. Never edit anything inside `docs/`.**

`docs/` is a **generated mirror**. MkDocs builds the site from it, but its content is
produced from the repo root by `tools/sync_docs.py`. Anything you change in `docs/` is
overwritten on the next sync. `docs/` is also git-ignored, so it never reaches GitHub.

```
repo root                      docs/ (generated, ignored)
├── README.md          ───────►  README.md
├── 00_getting_started/ ──────►  00_getting_started/
├── ...
├── Resources/          ──────►  Resources/
├── Projects/           ──────►  Projects/
├── Exercises/          ──────►  Exercises/
├── stylesheets/        ──────►  stylesheets/
└── overrides/                   (read from root directly)
```

---

## Prerequisites

- **Python 3.8+** (3.12 is what CI uses)
- `pip`

No other tooling is required — the sync script uses the standard library only.

---

## Quick Start

### 1. Create a virtual environment

**Windows (PowerShell or cmd):**

```bat
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install the documentation dependencies

```bash
pip install -r requirements.txt
```

Versions are pinned, so this matches exactly what CI installs.

### 3. Sync the content into `docs/`

```bash
python tools/sync_docs.py
```

Useful options:

```bash
python tools/sync_docs.py --dry-run   # show what would change, touch nothing
```

The script is idempotent: running it twice in a row does nothing the second time.

### 4. Start the live-reload server

```bash
python -m mkdocs serve
```

Open <http://127.0.0.1:8000/VibeLearning/>. The browser refreshes automatically when
you save a file — but remember to re-run the sync after editing root files:

```bash
python tools/sync_docs.py     # then the browser refreshes
```

> **Tip:** if port 8000 is busy, add `--dev-addr=127.0.0.1:8001`.

### 5. Build the static site (optional)

```bash
python tools/sync_docs.py
python -m mkdocs build            # output goes to site/
python -m mkdocs build --strict   # same, but fails on any warning
```

---

## Everyday workflow

| Task | Command |
|------|---------|
| Edit a lesson | change `01_foundations/.../README.md` **at the root** |
| Preview | `python tools/sync_docs.py && python -m mkdocs serve` |
| Check for broken links | `python tools/sync_docs.py && python -m mkdocs build --strict` |
| Start from scratch | delete `docs/` and `site/`, then sync again |

`--strict` is the important one: it turns every build warning into an error, which is
exactly what CI runs. If it passes locally, CI passes too.

---

## Deployment

**Deployment happens only through CI.** There is no deploy script to run and no
`gh-pages` branch to manage.

1. Open a pull request → the **validate** job builds with `--strict`; a broken link
   fails the PR.
2. Merge to `main` → the **deploy** job builds and publishes to GitHub Pages.

Live site: <https://jackc0re.github.io/VibeLearning/>

You do not need to be able to deploy locally, and you should not try to — the CI
environment is the same one that produces the live site.

---

## CI jobs

The workflow lives in `.github/workflows/mkdocs.yml`:

| Job | Trigger | What it does |
|-----|---------|--------------|
| `validate` | every PR and push to `main` | installs pinned deps → syncs → `mkdocs build --strict` |
| `deploy` | pushes to `main` only | installs pinned deps → syncs → builds → publishes to Pages |

Both jobs build from the repo root, so `docs/` is always regenerated during CI. A
fresh clone works with no setup.

---

## Troubleshooting

### `docs_dir` or "not found" errors

You probably deleted or edited something inside `docs/`. Regenerate it:

```bash
python tools/sync_docs.py
```

### Port 8000 already in use

```bash
python -m mkdocs serve --dev-addr=127.0.0.1:8001
```

### Build warnings about links

Those are real and `--strict` will reject them. Fix the link in the **root** file:

- Link to a folder: `01_foundations/01_variables_and_types/README.md` (**not** `01_variables_and_types/`)
- Link to a page: `Resources/glossary.md`
- Link to a source file: `01_foundations/01_variables_and_types/examples.py`

### Fonts look wrong

`overrides/main.html` loads JetBrains Mono from Google Fonts. Check your internet
connection and the browser console. Text uses Inter (via the Material theme config).

### Changes not showing up

You edited a root file but did not sync:

```bash
python tools/sync_docs.py
```

---

## Checklist before opening a pull request

- [ ] `python tools/sync_docs.py` runs clean
- [ ] `python -m mkdocs build --strict` exits 0 (no warnings)
- [ ] `docs/` and `site/` are **not** in `git status` (they are ignored)
- [ ] Only root files are staged
- [ ] `python tools/sync_docs.py` twice gives "0 copied, 0 updated" the second time

---

## Notes

- `docs/` — generated mirror of the content; git-ignored, safe to delete
- `site/` — build output; git-ignored, safe to delete
- `overrides/` — Jinja template overrides, read from the repo root
- `stylesheets/extra.css` — the Catppuccin Mocha/Latte theme
- Python examples (`examples.py`, `exercises.py`) are published to the site as
  downloadable files so the links in lesson pages work
