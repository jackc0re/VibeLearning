# Changelog

Notable changes to VibeLearning. The site is published at
<https://jackc0re.github.io/VibeLearning/>.

---

## 2026-10-23 — Repository revision

A maintenance pass over the build pipeline, the theme, the navigation, and CI. The
teaching content itself is unchanged apart from link fixes and a handful of bug fixes.

### Fixed

- **The redesigned theme never deployed.** The repo root held a 985-line Catppuccin
  theme, but the site was built from a stale copy inside `docs/`. The site now builds
  from the real theme.
- **Light mode was broken.** Colors were hardcoded to the dark palette, so switching
  to light mode produced dark-on-dark text. Colors are now semantic `--vl-*` tokens
  with a full Catppuccin **Latte** (light) palette alongside **Mocha** (dark).
- **Broken links.** 217 pages had dead or unresolvable links (directory-style links,
  links to excluded source files, wrong cross-module paths, broken anchors). The build
  now reports **zero warnings** and runs with `--strict`.
- **Six broken examples** that had never been executed: a `None` name, a built-in
  module's missing `__file__`, a `global` used before assignment, `zoneinfo` without
  `tzdata`, a handler body set before its status line, and `{{ name }}` placeholder
  conversion.

### Added

- `tools/sync_docs.py` — mirrors the repo root into `docs/`, so content can no longer
  drift between two copies. Idempotent, standard library only.
- `tools/run_examples.py` — runs all 110 lesson examples with a per-file timeout and a
  documented skip list for the three that need a socket or block forever.
- **Projects**, **Exercises**, **Quizzes**, **Cheatsheets**, **Further Reading**,
  **Roadmap** and **Contributing** are now in the site navigation — previously about a
  third of the repository was unreachable from the site.
- `Resources/quizzes.md` — an index of all 114 quizzes grouped by module, plus a
  "🧠 Test Yourself" footer on every topic page.
- A `404` page.
- A single merged `README.md` that works as both the GitHub landing page and the site
  home page.

### Changed

- Top navigation regrouped into 9 tabs (was 13, which overflowed at laptop widths);
  modules are nested so the sidebar collapses per module.
- `requirements.txt` now pins exact versions.
- `DEVELOPMENT.md` rewritten around the sync-script workflow and Windows-friendly
  commands. The bash helper scripts (`build.sh`, `serve.sh`, `clean.sh`, `deploy.sh`)
  are gone — `deploy.sh` used a `docs_dir: .` configuration that modern MkDocs rejects.
- `AGENTS.md` rewritten to describe the repository as it actually is.
- `docs/` is no longer tracked in git (493 duplicate files removed).

### CI

Workflow `.github/workflows/mkdocs.yml` now has three jobs:

| Job | Trigger | Purpose |
|-----|---------|---------|
| `validate` | PR + `main` | `mkdocs build --strict` — a broken link fails the build |
| `deploy` | `main` only | publishes to GitHub Pages |
| `examples` | PR + `main` | runs every lesson example |

Both build jobs install from the pinned `requirements.txt` instead of an ad-hoc pip
command, and regenerate `docs/` themselves, so a fresh clone needs no setup.

### Removed

- `_config.yml` (unused Jekyll configuration).
- `claude_code_zai_env.sh` (personal tooling script).
- `PROGRESS.md` + `PROGRESS_02.md` merged into one; the proposal moved to
  `plans/enhancement-proposal-2026-01-28.md`.
