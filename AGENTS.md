# VibeLearning — Guide for AI Coding Agents

> **Last Updated:** 2026-10-23

This repository is a self-contained Python teaching resource: 21 modules, 11 projects,
exercise tracks, and a MkDocs Material website published to GitHub Pages.

Read this file before making changes. The most important rule is near the top.

---

## ⚠️ The one rule that will bite you

**Edit files at the repository root. Never edit anything inside `docs/`.**

`docs/` is a **generated mirror** of the root content, produced by
`tools/sync_docs.py` and consumed by MkDocs. It is git-ignored. Any change made
inside `docs/` is destroyed by the next sync and never reaches GitHub.

```
root (source of truth)          docs/ (generated, git-ignored)
├── README.md            ─────►  README.md
├── 00_..20_ modules     ─────►  00_..20_/
├── Resources/           ─────►  Resources/
├── Projects/            ─────►  Projects/
├── Exercises/           ─────►  Exercises/
├── stylesheets/         ─────►  stylesheets/
└── overrides/                   (read from root directly by MkDocs)
```

---

## Project Overview

- **Language:** Python 3.8+ (CI uses 3.12)
- **Lesson code dependency policy:** standard library only — the *lesson content*
  must never require `pip install`
- **Docs toolchain:** MkDocs + Material, pinned in `requirements.txt`
- **Deployment:** GitHub Actions → GitHub Pages (no deploy script, no `gh-pages` branch)

**Current size:** 21 modules, 124 topics, 11 projects, ~288 `.py` files, ~344 `.md` files.

---

## Repository Structure

```
VibeLearning/
├── 00_getting_started/        # Setup, running code, repo orientation
├── 01_foundations/            # Variables, operators, control flow, functions
├── 02_data_structures/        # Lists, dicts, sets, trees, graphs, hash tables
├── 03_algorithms/             # Searching, sorting, recursion, DP, graphs
├── 04_oop_concepts/           # Classes, inheritance, polymorphism, SOLID
├── 05_functional_programming/ # Pure functions, closures, decorators
├── 06_software_design/        # DRY, KISS, YAGNI, coupling/cohesion, refactoring
├── 07_design_patterns/        # Creational, structural, behavioral
├── 08_error_handling/         # Exceptions, defensive programming, logging
├── 09_testing/                # Unit tests, TDD, mocking, integration
├── 10_file_io/                # Files, JSON, CSV, binary
├── 11_memory_performance/     # Big-O, complexity, optimization
├── 12_concurrency/            # Threads, async, synchronization, deadlocks
├── 13_modules_packages/       # Imports, packages, virtual environments
├── 14_debugging/              # Debuggers, tracebacks, common bugs
├── 15_version_control/        # Git basics (uses examples.sh, not .py)
├── 16_essential_libraries/    # collections, datetime, itertools, pathlib, re...
├── 17_cs_fundamentals/        # Number systems, bitwise, boolean logic, memory
├── 18_working_with_apis/      # HTTP, requests, parsing, building APIs
├── 19_data_processing/        # SQLite, SQL, cleaning, transformation, reports
├── 20_web_basics/             # HTML/CSS, HTTP server, routing, templating
├── Projects/                  # 11 guided projects
├── Exercises/                 # beginner / intermediate / advanced
├── Resources/                 # glossary, quizzes index, cheatsheets, interview prep, further reading
├── tools/                     # sync_docs.py, run_examples.py + 5 learner tools (run_quiz, check_exercise, progress_tracker, generate_path, repo_stats)
├── stylesheets/extra.css      # Catppuccin Mocha (dark) + Latte (light) theme
├── overrides/main.html        # Loads JetBrains Mono
├── mkdocs.yml                 # Site config + nav
├── requirements.txt           # Pinned docs dependencies
├── README.md                  # Landing page (GitHub + site)
├── DEVELOPMENT.md             # Local docs workflow
├── ROADMAP.md                 # Suggested learning timeline
└── PROGRESS.md                # Implementation status (internal)
```

### Topic directory convention

Every topic follows the **4-file pattern**:

```
topic_name/
├── README.md       # Theory, analogies, code snippets
├── examples.py     # Runnable demonstrations
├── exercises.py    # Practice problems, solutions at the bottom
└── quiz.md         # Knowledge check, answers at the bottom
```

Projects use `README.md` + source file(s) + optional `challenges.md`.
`15_version_control` uses `examples.sh` instead of `examples.py`.

---

## Common Commands

```bash
# Run a lesson
cd 01_foundations/01_variables_and_types
python examples.py

# Regenerate docs/ from root (required before any MkDocs command)
python tools/sync_docs.py

# Local preview (http://127.0.0.1:8000/VibeLearning/)
python -m mkdocs serve

# The gate CI enforces - must exit 0
python -m mkdocs build --strict

# Run every lesson example (CI job 'examples')
python tools/run_examples.py

# Run one subtree only
python tools/run_examples.py 01_foundations
```

---

## CI: three jobs in `.github/workflows/mkdocs.yml`

| Job | Trigger | What it enforces |
|-----|---------|------------------|
| `validate` | every PR + push to `main` | `mkdocs build --strict` — a single warning fails it |
| `deploy` | push to `main` only | publishes `site/` to GitHub Pages |
| `examples` | every PR + push to `main` | runs all `examples.py` with a per-file timeout |

Because `--strict` is on, **every markdown link must resolve**. Broken links are the
most common way to turn CI red.

---

## Code Style

### Python
- `snake_case` functions/variables, `PascalCase` classes
- Module docstring with `=` underline; short docstrings on public functions
- Section headers as `# ===...` banner comments
- f-strings for formatting
- Type hints where they aid clarity (common in modules 09+)

### examples.py shape

```python
"""
Module Name - Examples
======================
What this file demonstrates.
"""

print("=" * 50)
print("MODULE NAME - Examples")
print("=" * 50)

# =============================================================================
# SECTION
# =============================================================================
print("\n--- Section Description ---\n")

# ... examples ...

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
```

Examples must run unattended: no `input()`, no `while True` without a bound, no
network servers. If something genuinely cannot run unattended, add it to `SKIP` in
`tools/run_examples.py` with a reason — do not silently leave it broken.

**ASCII-only print output** (repo-wide policy): every string a lesson `.py` file prints
must be plain ASCII. Emoji, `→`, `✓`, box-drawing chars crash a default Windows console
(cp1251/cp1252/cp437). Use `PASS`/`FAIL`, `->`, `= | + -` banners. If a lesson must show
a non-ASCII value (e.g. URL encoding), write it with `\uXXXX` escapes in the source.
Emoji in Markdown headings/tables are fine — the rule is about Python print output only.

### Markdown links (matters for `--strict`)
- To a page: `01_foundations/01_variables_and_types/README.md`
- To a source file: `01_foundations/01_variables_and_types/examples.py`
- **Not** to a bare directory: `01_variables_and_types/` will fail the strict build

---

## Content Conventions

### Writing style
- Encouraging, beginner-first tone
- Analogies before formalism (boxes, jars, light switches)
- Show the "why", not only the "what"
- Progressive complexity within a file

### README.md sections for a topic
Title with emoji → concept explanation with analogy → code examples in fenced blocks →
common mistakes → quick reference table → quiz link (a "🧠 Test Yourself" footer is
already applied to topic pages).

### Adding a new topic
1. Create `NN_topic_name/` under the right module with the 4 files.
2. Add a nav entry in `mkdocs.yml` (nested under its module section).
3. Add the quiz to `Resources/quizzes.md`.
4. `python tools/sync_docs.py && python -m mkdocs build --strict`.
5. `python tools/run_examples.py <module>/` to confirm it runs.

### Adding a quiz to an existing topic
Quizzes live in `quiz.md` next to the topic's `README.md`: 5–10 questions, answers at
the bottom. Add the topic to `Resources/quizzes.md`, and the topic README already has a
"🧠 Test Yourself" footer linking to it.

---

## Adding Dependencies — Two Different Rules

- **Lesson code** (`examples.py`, `exercises.py`, project sources): standard library
  **only**. This is a promise to beginners — no `pip install` to follow a lesson.
  The single soft exception is `tzdata` on Windows for `zoneinfo`, and the datetime
  example handles its absence gracefully.
- **Docs tooling** (`mkdocs.yml`, `requirements.txt`, `tools/`): adding a pinned
  dependency is fine. Pin exact versions (`==`) so CI and local builds match.

---

## Gotchas

- **Windows consoles** use cp1251/cp1252 and crash on emoji/arrows. Lesson `.py` files
  therefore print ASCII-only (see the policy above). `tools/run_examples.py` still forces
  `PYTHONIOENCODING=utf-8` for children; do the same in any new subprocess code.
- **`docs/` is ignored by git.** `git status` should never show it. If it does, the
  ignore rule broke.
- **The theme uses `--vl-*` tokens** for colors, defined per scheme in
  `stylesheets/extra.css`. Add new colors as tokens with both Mocha and Latte values —
  do not hardcode a hex value, or light mode will inherit a dark color.
- **`custom_dir: overrides` resolves from the repo root**, not from `docs/`.
- **MkDocs `--strict` treats warnings as errors**, including navigation entries that
  point at files that do not exist.

---

## Files Worth Knowing

| File | Purpose |
|------|---------|
| `README.md` | Landing page for GitHub and the site (keep links strict-safe) |
| `DEVELOPMENT.md` | Local docs workflow, troubleshooting, PR checklist |
| `ROADMAP.md` | Suggested learning timeline |
| `mkdocs.yml` | Site config, theme, extensions, nav |
| `tools/sync_docs.py` | Root → `docs/` mirror; idempotent |
| `tools/run_examples.py` | Runs every lesson example with a timeout |
| `tools/` learner tools | `run_quiz.py`, `check_exercise.py`, `progress_tracker.py`, `generate_path.py`, `repo_stats.py` — interactive learner CLIs (not run by CI; state in `~/.vibelearning/`) |
| `stylesheets/extra.css` | Catppuccin theme, `--vl-*` color tokens |
| `.github/workflows/mkdocs.yml` | validate / deploy / examples jobs |
| `PROGRESS.md` | Internal implementation status |
| `plans/`, `issues/` | Internal notes, excluded from the site |

---

## Definition of Done

Before declaring a change complete:

- [ ] `python tools/sync_docs.py` → second run reports 0 copied / 0 updated
- [ ] `python -m mkdocs build --strict` → exit 0, no warnings
- [ ] `python tools/run_examples.py` → 0 failed (skips have reasons)
- [ ] Only root files staged in git (`docs/` and `site/` never staged)
- [ ] New links use `path/README.md`, never a bare directory

This is a learning resource: prefer clarity over cleverness, and keep every example
runnable by a beginner with nothing installed.
