# Plan: VibeLearning Revision — fix the build pipeline, restore the lost design, and make the site usable

## Context

VibeLearning is a Python learning repo (21 modules, 11 projects, ~245 runnable `.py` examples) with a MkDocs Material site deployed to GitHub Pages by one CI workflow. The current setup has three separate problems that explain everything the user feels:

1. **Content is duplicated and drifting.** Everything exists twice — once at the repo root and again as a full copy inside `docs/` (493 tracked files). `build.sh` only syncs when `docs/` doesn't exist, so the two copies have drifted apart. This double bookkeeping is why the site "feels old."
2. **The big UI overhaul never shipped.** The repo root has a 985-line Catppuccin Mocha/Latte theme (`stylesheets/extra.css`), but the site actually serves the stale 497-line copy in `docs/stylesheets/extra.css` with no colors and no fonts. MkDocs reads `docs_dir: docs`, so the nice CSS never deployed. Also, `mkdocs.yml` sets `primary: custom` / `accent: custom`, and with the stale CSS those variables are undefined — the live site falls back to default Material colors. **This is the single biggest visual fix and it's almost free.**
3. **CI is green but fragile, and nothing checks the actual content.** The workflow installs an ad-hoc pip list that drifts from `requirements.txt` (and installs an unused plugin). `.gitignore` has a malformed `docs/` line (trailing comment breaks the pattern — the only reason `docs/` stayed committed). 245 `.py` example files are never executed anywhere. `mkdocs build` emits ~260 warnings (broken relative links) but never fails because it's not strict. `deploy.sh`'s build path is dead (MkDocs 1.6 rejects `docs_dir: .`).

Plus usability gaps: **Projects/ and Exercises/ are completely missing from the site nav**, 114 quiz pages are unreachable orphans, cheatsheets and further reading aren't in nav, and the landing page exists in two different versions (root README vs docs/README).

**Target architecture:** the repo root becomes the single source of truth. A small cross-platform Python script (`tools/sync_docs.py`, stdlib only — works on Windows) copies root → `docs/` before every build. `docs/` gets properly gitignored and untracked (drift becomes impossible, repo shrinks by ~493 files). CI installs from `requirements.txt` (pinned), runs sync + `mkdocs build --strict`, and deploys. Local dev on Windows = one sync script + `python -m mkdocs serve`.

Key files: `mkdocs.yml`, `.github/workflows/mkdocs.yml`, `stylesheets/extra.css`, `docs/` (to be untracked), `overrides/`, `requirements.txt`, `.gitignore`, `build.sh`/`clean.sh`/`deploy.sh`/`serve.sh`, `DEVELOPMENT.md`, `AGENTS.md`.

> **Note for the executor:** every phase below ends with the site still deploying green. Do the phases in order — Phase 2 (design) depends on Phase 1 (sync), and Phase 4 (strict build) depends on Phase 3.

---

## Phase 0 — Baseline safety (touch nothing yet)

Before changing anything, make sure we can always roll back and can prove what "before" looked like.

- [x] 1. Create a working branch (`git checkout -b revision`) — all later phases commit here. Never work directly on `main`.
      Files: none
      Done when: `git branch` shows the new branch checked out.
- [x] 2. Capture the "before" state so improvements are provable:
      - run `mkdocs build 2>&1 | tail -5 > .baseline-build.txt` locally and keep the warning count (expect ~260);
      - note `git ls-files | wc -l` and `git ls-files docs | wc -l` (expect 493);
      - save a copy of the live site's current `extra.css` (curl https://jackc0re.github.io/VibeLearning/stylesheets/extra.css — expect 497 lines, no Catppuccin).
      Files: `.baseline-build.txt` (scratch, don't commit — or commit under `plans/`)
      Done when: the three before-numbers are written down somewhere we can compare against later.
- [x] 3. Verify local build + preview work before touching anything: `python -m mkdocs serve`, open http://127.0.0.1:8000, click around. If this fails on the local machine, fix the environment first (see Risks — installing `pip install -r requirements.txt` in a venv).
      Files: none
      Done when: `mkdocs serve` runs locally and renders the site.
- [x] 4. Confirm Python venv instructions for Windows exist in DEVELOPMENT.md — CONFIRMED BROKEN (only `source venv/bin/activate` / `python3`, no Windows path). Full rewrite deferred to Phase 3 step 3, which replaces DEVELOPMENT.md wholesale.
      Files: `DEVELOPMENT.md`
      Done when: a Windows user can follow DEVELOPMENT.md to get a working local build.

---

## Phase 1 — One source of truth: sync script, fixed .gitignore, untracked docs/, one README

**Why:** right now every edit can land in one of two copies, and the site reads the copy nobody edits. This phase makes drift structurally impossible.

- [x] 1. Write `tools/sync_docs.py` (Python stdlib only — no dependencies, works on Windows):
      - mirrors the root content into `docs/`: copy `00_*`–`20_*` module dirs, `Resources/`, `Projects/`, `Exercises/`, `stylesheets/`, `overrides/`, and the merged `README.md` (from Phase 1 step 3);
      - deletes anything in `docs/` that no longer exists at root (a true mirror, not a copy-over);
      - prints a short summary (files copied / removed).
      Files: `tools/sync_docs.py`
      Done when: running `python tools/sync_docs.py` twice in a row is idempotent (second run copies nothing, deletes nothing), and `docs/stylesheets/extra.css` is identical to root `stylesheets/extra.css` (985 lines).
- [x] 2. Fix `.gitignore` and untrack `docs/`:
      - replace the malformed line `docs/           # Local dev docs directory` with `docs/` on its own line (the trailing comment is why the pattern never matched);
      - run `git rm -r --cached docs` so the 493 files stop being tracked (files stay on disk — nothing is lost).
      Files: `.gitignore`
      Done when: `git ls-files | grep -c '^docs/'` returns 0, and `git status` does NOT show docs/ as untracked noise (it's ignored).
- [x] 3. Merge the two READMEs into ONE good `README.md` at root. Root README is the plain 3.7 KB GitHub landing; `docs/README.md` is the nicer 6.9 KB site landing. Keep the better content (site landing), fold in anything useful from the plain one (badges, quick start), and add a clear "how to run the examples locally" section. The sync script then copies it into `docs/`.
      Files: `README.md`
      Done when: one README.md at root serves both GitHub and the site; `docs/README.md` is only ever produced by the sync script.
- [x] 4. Add the sync step to CI BEFORE untracking merges to main (order matters — once docs/ is untracked, CI must regenerate it):
      - in `.github/workflows/mkdocs.yml`, add a step after checkout: `python tools/sync_docs.py`, then `mkdocs build` as today.
      Files: `.github/workflows/mkdocs.yml`
      Done when: a push to the branch produces a green workflow and the deployed site still renders (spot-check a module page).

**Phase acceptance:**
- `git ls-files | grep -c '^docs/'` → 0 (repo ~493 files lighter; clone is faster).
- CI run green with site live and content unchanged.
- `python tools/sync_docs.py` then `mkdocs build` works on Windows with no bash.

---

## Phase 2 — Restore the Catppuccin design (the actual "looks old" fix)

**Why:** the whole UI overhaul exists in the repo but never deployed because CI read the stale copy in `docs/`. With the sync script from Phase 1, this mostly ships itself — but light mode needs finishing.

- [x] 1. After Phase 1's sync, the 985-line Catppuccin Mocha CSS is what gets built. Verify locally: `mkdocs serve` → check the dark palette (Mocha colors, JetBrains Mono code font, Inter text font) renders.
      Files: none (delivered by sync)
      Done when: local preview shows the Catppuccin theme.
- [x] 2. Define the missing Catppuccin **Latte** (light mode) variables in `stylesheets/extra.css`. The CSS defines Mocha (dark) variables but the `default`-scheme (light) block is incomplete or absent — with `primary: custom` in mkdocs.yml, light mode would render undefined. Add the full Latte palette block so the light/dark toggle works properly.
      Files: `stylesheets/extra.css`
      Done when: local preview, toggling dark↔light, shows Mocha dark and Latte light (both readable, no fallback blue).
- [x] 3. Resolve the `overrides/` duplication: keep exactly one canonical copy at root (`overrides/main.html`, which loads JetBrains Mono) — it is what MkDocs actually uses (see step 3b). The sync script does NOT need to mirror `overrides/` into `docs/`; when Phase 1 untracks `docs/`, the stale `docs/overrides/` copy disappears from git entirely.
      Files: `mkdocs.yml`, `overrides/`, sync script
      Done when: exactly one `main.html` exists in the repo, and the built site includes the font-loading override.
- [x] 3b. **Verified correction (this was tested empirically):** `custom_dir: overrides` resolves relative to the **project root** (where mkdocs.yml sits), NOT to `docs/overrides/` — a marker edited into root `overrides/main.html` appears in the built HTML; a marker in `docs/overrides/main.html` does not. So the root copy is the live one today. Two consequences:
      - the sync script does NOT need to mirror `overrides/` into `docs/` for theming to work;
      - BUT `docs/overrides/` currently leaks into the built site as a stray published file (`site/overrides/main.html` is live today). Fix: add `overrides/` to `exclude_docs` in mkdocs.yml so a mirrored overrides dir never publishes.
      Files: `mkdocs.yml` (exclude_docs), `tools/sync_docs.py`
      Done when: root `overrides/main.html` is the only template copy, and `site/overrides/` no longer exists in build output.
- [ ] 4. Deploy and compare: after merge to main, the live site serves the 985-line CSS (verify with `curl https://jackc0re.github.io/VibeLearning/stylesheets/extra.css | wc -l` → 985).
      Files: none
      Done when: live site serves the full Catppuccin stylesheet.

**Phase acceptance:**
- Live `extra.css` is 985 lines (was 497) and contains Catppuccin variables.
- Live site: dark mode = Mocha, light mode = Latte, fonts = Inter + JetBrains Mono.

---

## Phase 3 — CI hardening: pinned deps, strict build, PR validation

**Why:** CI is currently "green but meaningless" — it doesn't validate anything (build is non-strict, ~260 warnings, nothing runs the Python examples). This phase makes green actually mean correct.

- [x] 1. Pin versions in `requirements.txt` (exact `==` pins for `mkdocs`, `mkdocs-material`, `pymdown-extensions`, `pygments`; drop `mkdocs-live-edit-plugin` if unused in mkdocs.yml — check first). Remove the extra `[imaging]` extra only if no `attr_list`-imaged SVG icons are used; keep it if social icons need it.
      Files: `requirements.txt`
      Done when: `pip install -r requirements.txt` on a clean venv installs a reproducible set; versions match what CI uses.
- [x] 2. Rework `.github/workflows/mkdocs.yml`:
      - install from `requirements.txt` (delete the ad-hoc `pip install mkdocs mkdocs-material ...` list — it currently drifts from requirements.txt and installs `mkdocs-minify-plugin` which mkdocs.yml never uses);
      - keep the deploy job on `push: main` as-is;
      - add a **separate validation job** that runs on pull requests (and optionally on main): checkout → `pip install -r requirements.txt` → `python tools/sync_docs.py` → `mkdocs build --strict` → fail on any warning.
      Files: `.github/workflows/mkdocs.yml`, `requirements.txt`
      Done when: opening a PR with a deliberate broken link makes the validation job fail; the deploy workflow still goes green on main.
- [x] 3. Remove the dead scripts and document the new flow:
      - delete `deploy.sh` (its inline `docs_dir: .` config is rejected by MkDocs 1.6 — that path is dead, and DEVELOPMENT.md still documents it as the deploy method, which would mislead the user);
      - replace `build.sh`/`clean.sh`/`serve.sh` with either nothing (Windows users run `python tools/sync_docs.py && python -m mkdocs serve` directly) or thin wrappers — see Open Question 1;
      - rewrite `DEVELOPMENT.md` to the new flow: venv setup on Windows, `python tools/sync_docs.py`, `python -m mkdocs serve`, push to main → CI deploys.
      Files: `deploy.sh`, `build.sh`, `clean.sh`, `serve.sh`, `DEVELOPMENT.md`
      Done when: DEVELOPMENT.md contains zero references to `deploy.sh`, and a Windows user following it verbatim gets a working preview.

**Phase acceptance:**
- Workflow installs exclusively from `requirements.txt` (pinned).
- A PR with a broken link fails CI; a clean PR passes.
- `deploy.sh` gone; DEVELOPMENT.md reflects reality (CI-only deploy).

---

## Phase 4 — Fix the ~260 broken links (required for --strict)

**Why:** these are real dead links visitors hit on the live site today. Mostly mechanical: module READMEs link to directories like `./01_searching/` which MkDocs can't resolve — they need to point at `./01_searching/README.md`.

- [ ] 1. Run `mkdocs build 2>&1 | grep -i "warning" | sort | uniq -c | sort -rn` to get the grouped warning list. Fix the dominant pattern (relative `./NN_topic/` links → `./NN_topic/README.md`) — likely a handful of sed-able patterns across the module READMEs. Fix at the **root copies** (source of truth), never in `docs/`.
      Files: `*/README.md` at root (source files only)
      Done when: warnings from unresolved relative links are gone.
- [ ] 2. Fix anchor breakage: `Resources/further_reading.md` (5 broken in-page anchors) and `Resources/glossary.md` (links to nonexistent anchors `#j` and `#q` — those sections don't exist; either add "no terms" placeholders or remove the links).
      Files: `Resources/further_reading.md`, `Resources/glossary.md`
      Done when: no anchor warnings in build output.
- [ ] 3. Reach zero: `python tools/sync_docs.py && mkdocs build --strict` exits 0 locally.
      Files: none
      Done when: `mkdocs build --strict; echo $?` → 0, and the Phase 3 CI validation job goes green on main.

**Phase acceptance:**
- `mkdocs build --strict` → zero warnings, exit code 0 (was ~260 warnings).
- CI validation job green on main.

---

## Phase 5 — Navigation & usability: Projects, Exercises, Resources, quizzes

**Why:** the site hides roughly a third of the content. 11 projects (including the newest: quiz_game, personal_journal, password_manager, url_shortener, chat_server, static_site_generator, tic_tac_toe_ai) and the whole Exercises track (beginner/intermediate/advanced) exist in the repo but never appear in the site nav. 114 quiz pages are built yet unreachable, and cheatsheets/further reading are likewise orphaned.

- [ ] 1. Extend `nav` in `mkdocs.yml`:
      - add a **Projects** section (Projects/README.md + all 11 project pages);
      - add an **Exercises** section (Exercises/README.md + beginner/intermediate/advanced);
      - extend **Resources** with `Resources/further_reading.md` and the cheatsheets (list every file under `Resources/cheatsheets/`).
      Files: `mkdocs.yml`
      Done when: every entry in nav resolves (strict build catches typos), and Projects + Exercises are clickable in the site header/sidebar.
- [ ] 2. Decide and implement quiz discoverability — see **Open Question 2**. Default recommendation if no answer: keep quiz.md files OUT of the main nav (114 entries would bury everything) and instead add a prominent link from each topic's README to its quiz page (e.g. a "Test yourself 🧠" link at the bottom of every topic page), plus one "Quizzes" index under Resources listing all quizzes grouped by module.
      Files: `mkdocs.yml`, topic READMEs (root copies)
      Done when: every quiz.md is reachable from at least one linked page (no orphans), and strict build still passes.
- [ ] 3. Add a nice 404 fallback? (Optional — MkDocs serves GitHub Pages 404 automatically from `404.md` if present. Only if cheap.)
      Files: `docs/404.md` (via sync)
      Done when: optional; skip without penalty.

**Phase acceptance:**
- Live site nav includes Projects, Exercises, cheatsheets, further reading.
- No orphan quiz pages (every page reachable from nav or a linked index).
- Strict build still passes; CI green.

---

## Phase 6 — CI runs the actual Python examples

**Why:** this is a *learning* repo — the 245 `examples.py` files are the product, and nothing anywhere ever executes them. A broken example ships silently today. One careful job catches regressions forever after.

- [ ] 1. Add a `python-examples` job to the workflow: checkout, setup Python 3.11+, then run every `**/examples.py` at root with a **per-file timeout** (e.g. 10 s via a small runner script or `timeout` command), and a curated skip-list for interactive/slow ones (candidates: `Projects/09_chat_server`, `Projects/10_static_site_generator`, anything with `input()` loops or `time.sleep`). Exercise files stay out of scope for now (they're often intentionally incomplete).
      Files: `.github/workflows/mkdocs.yml`, optionally `tools/run_examples.py`
      Done when: the job runs green on the current code with a documented skip-list, and deliberately breaking one example makes it fail.
- [ ] 2. Fix any examples that fail when first run (expect a handful; this job's first run is also an audit). Keep fixes minimal — this is not a content-rewrite phase.
      Files: failing `examples.py` files (root copies)
      Done when: `python-examples` job green with the minimal skip-list.

**Phase acceptance:**
- Workflow has a green examples job; breaking an example in a PR fails CI.
- Skip-list is short, documented, and reviewed (no blanket skips).

---

## Phase 7 — Housekeeping & docs honesty

**Why:** stale meta-docs actively mislead a future contributor (or the user's future self). AGENTS.md claims "no dependencies, no build system," stops at module 15, and has wrong file counts — reality is 21 modules, 11 projects, MkDocs + CI.

- [ ] 1. Rewrite `AGENTS.md` to match reality: correct structure (00–20 modules, Projects ×11, Exercises, Resources), the sync-script workflow, CI layout (deploy + validation + examples jobs), and where to edit things (root = source of truth, never edit `docs/`).
      Files: `AGENTS.md`
      Done when: every claim in AGENTS.md is verifiably true against the repo.
- [ ] 2. Remove `claude_code_zai_env.sh` (a 7 KB personal tooling script that shouldn't be in a public learning repo).
      Files: `claude_code_zai_env.sh`
      Done when: file gone from the repo.
- [ ] 3. Consolidate scaffolding: `PROGRESS.md` + `PROGRESS_02.md` + `plans/` + `issues/` are internal notes. They're already excluded from the site. Merge the two PROGRESS files into one (or archive both under `plans/`), so the repo root is clean for learners.
      Files: `PROGRESS.md`, `PROGRESS_02.md`, `plans/`, `issues/`
      Done when: at most one progress-tracking file at root; nothing user-facing changed.
- [ ] 4. Final sweep: `mkdocs build --strict` green, all three CI jobs green, live site verified (CSS 985 lines, nav complete, no broken links), and a short "what changed" summary added to README or a CHANGELOG entry.
      Files: `README.md` or new `CHANGELOG.md`
      Done when: every phase acceptance box above re-verified on the live site.

**Phase acceptance:**
- AGENTS.md accurate, no personal scripts committed, one progress file, all CI green, live site verified end-to-end.

---

## Validation (whole-plan checks, run at the end and per-phase where relevant)

```bash
# 1. Sync is idempotent (run twice, expect no changes on second run)
python tools/sync_docs.py && python tools/sync_docs.py

# 2. Strict build passes
mkdocs build --strict && echo "STRICT BUILD OK"

# 3. docs/ is no longer tracked
git ls-files | grep -c '^docs/'   # expect 0

# 4. Live site serves the intended theme
curl -s https://jackc0re.github.io/VibeLearning/stylesheets/extra.css | wc -l   # expect 985
curl -s https://jackc0re.github.io/VibeLearning/stylesheets/extra.css | grep -c catppuccin   # expect > 0

# 5. Nav completeness: Projects, Exercises, cheatsheets all reachable on the live site
# 6. Zero warnings in the CI validation job log
# 7. python-examples CI job green with a minimal skip-list
```

---

## Risks / open questions

**Risks:**
- **Untracking `docs/` is the riskiest single move** (493 files leave git). Mitigation: do it on the branch, verify CI green BEFORE merging to main, and Phase 1 step 4 adds the sync step to CI first — if the order is flipped, main's next deploy publishes an empty site. The files also remain on disk (`git rm --cached` only).
- **`custom_dir: overrides` resolution** (tested — see Phase 2 step 3b): `custom_dir` resolves relative to the project root, so the root `overrides/main.html` keeps working after `docs/` is untracked; nothing to migrate. Just add `overrides/` to `exclude_docs` so a mirrored copy never publishes as a stray file.
- **~245 example scripts running for the first time ever**: expect a handful of genuine failures and possibly a few that hang (why the per-file timeout + skip-list is non-negotiable in Phase 6).
- **Windows dev environment**: bash scripts are friction for the user; the plan replaces them with Python/`python -m mkdocs` commands, but the executor should verify the commands work in PowerShell/cmd, not just bash.
- **Pinned deps may break on future Material major versions** — acceptable trade-off for reproducible builds; note the upgrade path in DEVELOPMENT.md (bump pin → run strict build → fix warnings).

**Open questions (decisions for the user; defaults chosen so /build can proceed without blocking):**
1. **Bash wrappers** — delete `build.sh`/`serve.sh`/`clean.sh` entirely and use direct Python commands (default: delete; simplest, most Windows-friendly), or keep thin wrappers rewritten in Python? *Default: delete + document the two direct commands.*
2. **Quiz pages** — link from topic READMEs + one Quizzes index (default), or add all 114 to the nav (buries the sidebar), or drop quizzes from the site entirely? *Default: link + index.*
3. **`mkdocs-material[imaging]`** — keep the imaging extra (needed only for generated social cards) or trim to plain `mkdocs-material`? *Default: keep if any social-card config exists; else trim.*
4. **PROGRESS/plans/issues scaffolding** — keep on GitHub as-is (public but site-excluded), move into `plans/`, or gitignore them? *Default: consolidate into one file at root.*
5. **Content polish beyond links** — this plan fixes structure, theme, nav, CI. It deliberately does NOT rewrite teaching content (that's a separate, much bigger pass). Confirm scope.
