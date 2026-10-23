# Content Quality Review — Master Checklist

> **Started:** 2026-10-23
> **Method:** automated structural audit + parallel per-module deep review (4 dimensions: technical accuracy, pedagogy, exercises/quiz quality, convention consistency)
> **Policy:** small fixes applied directly; big issues reported for decision.

Audience calibration: complete beginners, no CS background, nothing installed but Python 3.8+.

---

## Status Overview

| Scope | Status | Verdict |
|-------|--------|---------|
| 00_getting_started | ✅ Reviewed (s1) + fixes (s2) | First program now ASCII-safe; Atom removed; Jupyter reframed optional; workflow advice consistent |
| 01_foundations | ✅ Reviewed (s1) + fixes (s2) | Runs clean, answers correct; primers added (f-strings section, list & dict primer, for-loop sneak peek) |
| 02_data_structures (01–05) | ✅ Reviewed (s1) + fixes (s2) | 6 accuracy bugs fixed (s1); tuples expanded to 6 exercises, eval() removed, zero-division guard (s2) |
| 02_data_structures (06–10) | ✅ Reviewed (s1) + fixes (s2) | 9 defects fixed (s1); class primer + recursion aside + 3 solutions + parity sections + BST code + weighted graphs + get() unified (s2) |
| 03_algorithms | ✅ Reviewed (s1) + fixes (s2) | Brute-force verified, 4 broken answer-keys fixed (s1); DP table trace + optional banners added (s2) |
| 04_oop_concepts | ✅ Reviewed (s2) + depth (s4) | SOLID README expanded (before/after code for all 5 principles, ABC primer, Common Mistakes + Quick Reference); all 5 principles now execute in examples.py; 2 quiz questions added |
| 05_functional_programming | ✅ Reviewed (s2) + depth (s4) | Late-binding gotcha, `nonlocal`/UnboundLocalError trap, decorator factories, `@wraps` damage all taught; 35/35 reference solutions shipped (stub re-definition + PASS re-run pattern); parity sections on all 7 READMEs |
| 06_software_design | ✅ Reviewed (s3) + depth (s4) | 4 false-FAIL exercise assertions + DRY demo fixed (s3); 06/06 & 06/07 READMEs now have worked code examples + runnable demos + parity sections |
| 07_design_patterns | ✅ Reviewed (s3) + depth (s4) | Adapter cent + observer fixed (s3); all 6 stub patterns (Singleton/Builder/Decorator/Facade/Observer/Command) now full README sections with working verified code; parity sections added |
| 08_error_handling | ✅ Reviewed (s3) + gaps closed | `finally` snippet crashed; example littered CWD; wrong exception family; **logging now teaches handlers/levels/named loggers**; Common Mistakes + Quick Reference added to 4 READMEs |
| 09_testing | ✅ Reviewed (s3) + gaps closed | **All 5 quizzes had ZERO answers → 25 answer keys written**; pytest/`pip install` removed (2 labelled asides); recursive side_effect dead code |
| 10_file_io | ✅ Reviewed (s3) + depth (s4) | All 5 quizzes expanded to 6 questions (verified answers); Common Mistakes + Quick Reference on all 5 topic READMEs |
| 11_memory_performance | ✅ Reviewed (s3) + depth (s4) | Now actually measures: `perf_counter`, `timeit.repeat`, `cProfile`/pstats demos in 06; O() primers + forward links in 03/04; quizzes at 5-6 questions; full parity |
| 12_concurrency | ✅ Reviewed (s3) + depth (s4) | RLock properly taught (re-entrancy demo, no deadlock); `multiprocessing` section + Windows-safe CPU-bound demo (`__main__` guard, 3 verified runs); deadlock `False` output explained; quizzes at 5; full parity |
| 13_modules_packages | ✅ Reviewed (s3) | Broken `connect()` snippet, 2 false platform claims, reload claim fixed; pip sections lack "not needed here" labels |
| 14_debugging | ✅ Reviewed (s3) + parity (s4) | pdb `r` semantics + impossible quiz snippet verified fixed; Common Mistakes + Quick Reference + banners added to all 4 topics |
| 15_version_control | ✅ Reviewed (s3) | **16 defects** — inverted `--no-ff`, nonexistent `theirs` strategy, `recursive` vs `ort`, rebase→push always rejected, exercises that could not behave as documented |
| 16_essential_libraries | ✅ Reviewed (s3) + s4 | MAC→`hmac` fixed (s3); **s4: 16/08 README's `pip install bcrypt` example replaced with verified stdlib `hashlib.scrypt` hash/verify pair** (lesson code stays stdlib-only) |
| 17_cs_fundamentals | ✅ Reviewed (s3) | 5 wrong test expectations / broken solutions (bitwise bits, boolean rental rule, VM RETURN_VALUE, constant folding) |
| 18_working_with_apis | ✅ Reviewed (s3) + gaps (s4) | The 7 never-called solutions in 18/02 now execute via an offline `FakeResponse` swap-in (7 PASS); all 6 string-literal solutions in 18/04 converted to real executed handlers via `call_handler()` (6 PASS); no network added |
| 19_data_processing | ✅ Reviewed (s3) + gap (s4) | **SQL injection now demonstrated**: f-string query leaks 3 rows vs parameterized `?` returning 0 (in-memory sqlite, PASS-checked) + README teaching note |
| 20_web_basics | ✅ Reviewed (s3) | Content accurate; skip reason was wrong (file only prints a listing) → now covered by CI |
| Projects (11) | ✅ Reviewed (s3) + s4 | 02/03 broken paths fixed (s3); **s4: 07 password manager cipher replaced** — PBKDF2-derived split keys + SHAKE-256 keystream + HMAC tag (`compare_digest`), honest Security Notes ("never roll your own crypto"); 8/8 crypto smoke tests; ROADMAP synced to 11 projects |
| Exercises (3 tracks) | ✅ Reviewed (s3) + s4 | **All 14 missing files written** — intermediate & advanced now 8/8 each, matching their READMEs; every file runs unattended (slowest 0.91s); **CI now runs all track files** (`tools/run_examples.py` discovers `Exercises/*/*.py`); duplicate Exercise 1.5 removed from advanced/01 |
| Resources | ✅ Reviewed (s3) + s4 | **s4: glossary 71 → 116 terms** (added 06, 09, 16–20 coverage), further reading now covers modules 16–20 (17 canonical links), Resources README lists the 114-quiz index |

---

## DECISIONS RESOLVED (owner decisions from session 1 → implemented in session 2)

1. ✅ **ASCII-only print output, repo-wide (option c).** All 108 `.py` files that contained non-ASCII converted: `✓/✗`→`PASS/FAIL`, arrows→`->`, box-drawing→`=|+-`, decorative emoji removed, context maps for todo checkboxes/journal moods/medals/card suits, `café naïve`→`\uXXXX` escapes (URL-encoding lesson keeps its point). **0 non-ASCII left** in any lesson `.py`; 245 files compile clean; policy codified in `AGENTS.md` ("ASCII-only print output").
2. ✅ **Ordering fixed via primers (no restructure).** Class primer at first-ever `class` (02/06) + one-line callouts in 07/08/10; recursion aside in 02/08 + DFS link in 09; f-string section in 01/01; list & dict primer in 01_foundations README; for-loop sneak peek in 01/03.
3. ✅ **3 missing solutions written** (linked-list remove-duplicates; tree BST check — labeled Solution 3 to match the file's own exercise numbering; graph count-components, incl. split-graph demo).
4. ✅ **Structural parity for 02 (06–10):** Common Mistakes in all five, Quick Reference + quiz scoring footers + examples banners/footers in 07–10, BST insert/search code, weighted-graph example + real adjacency-matrix list, HashTable `get()` unified to return `None` (README callout added), `eval()`→`getattr()` in 02_strings, `05_tuples` expanded to 6 exercises + Common Mistakes.
5. ✅ **Module 03 editorial:** hand-traced DP coin-change table, Master Theorem "optional" banner, graph algorithms essentials/optional markers.
6. ✅ **Getting-started:** Atom removed, Jupyter explicitly optional, read/run advice consistent.
7. ✅ **CI now runs exercises.py too** (`tools/run_examples.py` extended). The probe caught 2 real crashes, both fixed: `16/08_hashlib_secrets` missing `json` import; `20/03_simple_routing` `match()` returning `(None, None)` (truthy → demo crash). Module 05's 4 crashing harnesses fixed via `safe_call` (unimplemented stubs now print FAIL lines, exit 0).

## Open items — RESOLVED in session 4 (2026-10-23)

All 17 items from the session-3 close-out are now addressed. None remain open.

1. ✅ **04 SOLID** — README expanded (rule + analogy + before/after code for all 5 principles, ABC primer); all 5 principles now execute in examples.py; Common Mistakes + Quick Reference; 2 new quiz questions.
2. ✅ **05 closures & decorators** — late-binding loop gotcha (+ default-arg fix), `nonlocal` with the `UnboundLocalError` counter-example, decorator factories, and the `@wraps` damage demo all added and runnable.
3. ✅ **07 pattern stubs** — Singleton, Builder, Decorator (with pattern-vs-syntax note), Facade, Observer, Command are full README sections with executed snippets; additive demos in creational/behavioral examples.py.
4. ✅ **06 bullets-only READMEs** — 06/06 got 4 smell code examples + runnable demos; 06/07 got a worked before/after refactor + "pin, change, prove" checklist demo.
5. ✅ **Missing exercise files** — decision: WRITE them. All 14 written (intermediate 02–08, advanced 02–08); both tracks now 8/8 matching their READMEs; every file runs unattended exit 0 (slowest 0.91s); `tools/run_examples.py` extended so CI runs all track files.
6. ✅ **Projects/07 cipher** — decision: option (b). `SimpleEncryption` → `VaultCrypto`: PBKDF2-HMAC-SHA256 (dklen=64) split into separate encryption + MAC keys, SHAKE-256 keystream (never repeats), HMAC-SHA256 tag verified with `hmac.compare_digest` before decrypting. 8/8 smoke tests (round-trip, wrong password, tampered body/tag, truncation, unicode). README: honest Security Notes, "why each piece" table, "never roll your own crypto" takeaway; `challenges.md` references renamed.
7. ✅ **05 reference solutions** — all 35 exercises ship solutions at the bottom of each exercises.py (stub re-definition + same tests re-run → PASS lines). Stubs stay stubs up top.
8. ✅ **11 measures now** — `perf_counter` vs-join timing, `timeit.repeat` list-vs-set micro-benchmark, `cProfile`+pstats top-3 demo in 11/06; O() primer boxes + forward links in 11/03–04.
9. ✅ **12 depth** — RLock section + re-entrancy demo (with a safe non-deadlocking Lock contrast); `multiprocessing` README section + Windows-verified CPU-bound demo (spawn, `__main__` guard, join timeout); deadlock demo's `False` explained in comments + printed text.
10. ✅ **README parity** — Common Mistakes + Quick Reference added across 04, 05, 10, 11, 12, 14 topic READMEs; banner header/footer added to 11, 12, 14 examples.py.
11. ✅ **Quiz depth** — module 10: 5 quizzes × 6 questions; module 11: all quizzes ≥5 (06 has 6); module 12 quizzes also expanded to 5 (same spec violation, fixed while in scope). All answers verified.
12. ✅ **18/19 gaps** — 18/02: the 7 dead solutions execute via an offline `FakeResponse` swap-in (7 PASS); 18/04: 6 string-literal solutions converted to executed handlers via a socketless `call_handler()` (6 PASS); 19/01: SQL-injection demonstrated (f-string leaks 3 rows vs parameterized 0) + README note.
13. ✅ **Glossary + further reading** — glossary 71 → 116 terms (06, 09, 16–20 covered); further reading gained modules 16–20 (17 canonical links); Resources README now lists the 114-quiz index and fixes stale counts.
14. ✅ **Exercises exit code** — closed as BY DESIGN: CI runs exercise files to catch crashes, and unattempted stubs legitimately print FAIL summaries, so exit 0 cannot double as a red/green signal; the printed PASS/FAIL summary is the learner-facing signal. Verified all 7 `03_algorithms` files exit 0.
15. ⏸️ **Solution-convention split** — consciously DEFERRED (unifying bottom-of-file vs inline vs `--solutions` is a repo-wide style change with pedagogical churn and no correctness impact). Both conventions are documented as valid in the session-1 notes.
16. ✅ **16/08 bcrypt suggestion** — README now teaches a verified stdlib `hashlib.scrypt` hash/verify pair (0.17s/hash measured); bcrypt/argon2 mentioned as the real-app third-party choice.
17. ✅ **Duplicated Exercise 1.5** — removed from `Exercises/advanced/01_system_design.py`; file runs clean.

**Also in session 4:** ROADMAP.md sanity pass — modules 17–20 were missing entirely (added with time/level tables), stage numbering body-vs-table mismatch fixed, project list updated to all 11, "unit testing with pytest" reworded (module 09 is deliberately stdlib-first with pytest as labelled asides).

---

## Session 1 fix summary (all verified: sync → strict build → run_examples green)

- Agent A (00–01): precedence table `not` row, undefined `has_bicycle`, BMI rounding, ambiguous lambda quiz option, 5 output-alignment fixes, `Exercises/Projects` casing, + systemic findings above.
- Agent B (02: 01–05): list-methods return-None note, mutated-`nums` comprehension demo, `s.join()` quick-ref fix, title-case word list `of`, set-union complexity `O(a+b)`, tuple hashability caveat.
- Agent C (02: 06–10): node-chain + tree diagrams rebuilt, `self.head` module-level NameError, height definition, 3 missing exercises.py links, `contains()` false-negative on None, comment-in-output, hash-seed nondeterminism explained.
- Agent D (03): corrupted quiz answer (binary search 1024), one-swap exercise wrong test (every correct learner failed), coin-change answer 7→6, quick-sort trace mismatched code, shortest-path test impossible, greedy "fails" examples that didn't fail, quick-select "1th/3th", closest-pair bound 6→8, naive-fib(30) timing, invalid pseudo-Python template, mutated-array harness, TSP arithmetic, module ASCII path diagram.
- Session lead: mkdocs nav (71 topics), 2 quiz titles, 5 git artifacts, .gitignore, this checklist.

## Session 2 fix summary (all verified: sync → strict build → run_examples incl. exercises green)

- **Decisions implemented:** ASCII sweep (108 files, 0 non-ASCII remaining, AGENTS.md policy codified); ordering primers (class/recursion/f-strings/list&dict/for-loop); 3 missing exercise solutions; structural parity for 02 (06–10); module 03 editorial (DP trace, optional banners); getting-started content fixes.
- **Module 04 review (agent):** 13 small fixes — grammar ("got a A"), false diamond-problem claim about Python, self-contradictory ABC quiz question, missing ABC-instantiation demo in exercise solution, `FlyingCar` NameError note, float noise, indentation, typos. Open items logged above.
- **Module 05 review (agent):** 2 accuracy fixes — closures "capture values" → "capture variables" (corrects the exact misconception behind the late-binding gotcha), mislabeled section banner. All 35 quiz answers verified correct; all 35 exercises proven satisfiable by an injected reference solution set.
- **Module 05 harness (agent):** `safe_call` helper added in 4 exercises files; 24 call sites routed; unimplemented stubs now degrade to FAIL lines with exit 0 (was `TypeError` traceback, exit 1).
- **CI hardening (session lead):** `tools/run_examples.py` now discovers and runs `exercises.py` too; probe found and fixed 2 real crashes (missing `json` import in 16/08; `match()` returning `(None, None)` in 20/03); `19/03_data_cleaning` regex docstrings made raw (was a `SyntaxWarning`, becomes an error in future Python).
- **Session lead also:** AGENTS.md ASCII policy, checklist updates.

## Session 3 fix summary — full review of modules 06–20, Projects, Exercises, Resources

**Method:** 9 parallel reviewer agents (3 batches), each running every `examples.py`/`exercises.py`, injecting reference solutions to detect false-FAIL assertions, checking every quiz answer individually, and verifying links. Plus 2 follow-up agents closing module 08/09 gaps. Session lead handled cross-cutting repo hygiene.

**The dominant bug class, found in nearly every module:** *test harnesses that fail a correct learner solution.* Root causes: exact float equality (`110.00000000000001 != 110` in 06), wrong expected values (bitwise bits in 17, coin change in 03), unreachable expectations (observer in 07), and unanswerable requirements (sender email in 06/06). Every one is invisible to a normal run because stubs only print FAIL.

**Worst individual defects fixed:**
- `Projects/02_todo_app` — **any due date crashed `display_tasks()`** (project was broken on the most common path).
- `Projects/03_file_organizer` — **dry run created real folders**; "Undo All" undid only 1 file. (It never deleted real files — verified.)
- `16/08_hashlib_secrets` — exercise solution built a **length-extension-forgeable MAC** (`sha256(payload + secret)`) and the hint endorsed it → now `hmac.new(...)`.
- `15_version_control` — **16 defects**, incl. inverted `--no-ff` comment, a nonexistent `theirs` merge strategy, `recursive` described as default (modern Git uses `ort`), and rebase→plain-push sequences guaranteed to be rejected.
- `06/01_dry_principle` — the DRY "before/after" demo printed **different totals**, teaching the opposite of the lesson.
- `07/02_structural` — adapter lost a cent: `int(1.15 * 100)` → 114 (hidden because `9.99` happens to work).
- `09_testing` — **all 5 quizzes had zero answers** (25 unanswerable questions) and the module advertised pytest + `pip install pytest`.
- `Resources/cheatsheets` — `list.clear()` followed by `my_list[0] = 10` (**IndexError** for anyone running top-to-bottom), plus several wrong documented outputs. Cheatsheets are copied verbatim, so these were high-risk.
- `08/02` — README `finally` snippet crashed with `UnboundLocalError`; example littered `temp_demo.txt` into the working dir (now `tempfile`).

**Gaps closed by follow-up agents:**
- `08/05_logging` now teaches the full progression: why not print → `basicConfig` formatting → `FileHandler` into a temp dir → named loggers → level filtering, with a matching runnable demo. Plus `Common Mistakes` + `Quick Reference` added to 4 module-08 READMEs.
- `09_testing`: 25 model answers written (free-response kept), pytest reduced to two clearly-labelled asides, `plain_assert_demo` renamed.

**Session-lead repo hygiene:**
- **33 tracked `.pyc` files removed from git** — compiled bytecode was committed, so `git status` went dirty after every example run.
- `.gitignore`: added learner-run artifacts (organizer logs, journal `entries.json`).
- **`tools/run_examples.py` SKIP list corrected** — all three entries described behaviour that no longer exists. `20/02_http_server` and `18/04_building_simple_api` only *print* code listings (verified: exit 0 in <1s), so they now run in CI; `18/05` genuinely hits httpbin.org, so it stays skipped with an accurate reason. Coverage went 217 passed / 3 skipped → **219 passed / 1 skipped**.

**Final gates:** `sync_docs` idempotent (0/0/563) · `mkdocs build --strict` exit 0, zero warnings · **219 passed, 0 failed, 1 skipped** · 0 non-ASCII in any lesson `.py`.

## Session 4 fix summary (2026-10-23) — closing all 17 remaining open items

**Method:** 7 parallel content agents, each owning a disjoint file set, every snippet executed before it was pasted, every file run after editing. Session lead handled the crypto swap, CI extension, ROADMAP, small fixes, and the final gates.

**Depth fixes (items 1–4):** 04 SOLID README/examples/quiz; 05 closures+decorators READMEs (late binding, `nonlocal`, decorator factories, `@wraps`); 06 code-smells & refactoring READMEs now show real code; 07's six stub patterns became full sections.

**Exercises (items 5, 7, 17):** 14 missing track files written (both tracks 8/8); 35 reference solutions shipped for module 05 (stub re-definition + PASS re-run); duplicate Exercise 1.5 removed. `tools/run_examples.py` now discovers `Exercises/*/*.py`, putting the practice tracks under CI crash protection.

**Crypto (item 6, decision b):** Projects/07 `SimpleEncryption` → `VaultCrypto` (PBKDF2 split keys + SHAKE-256 keystream + HMAC tag with `compare_digest`), README rewritten around "why each piece" + a "never roll your own crypto" warning; 8/8 smoke tests.

**Modules 10–12, 14, 18, 19 (items 8–12):** module 11 now measures (`perf_counter`/`timeit`/`cProfile`) and defines O() before using it; module 12 teaches RLock + `multiprocessing` (Windows-verified) and explains the deadlock demo's `False`; quiz depth raised to spec in 10, 11, 12; parity sections/banners completed in 10, 11, 12, 14, 04, 05; 18's dead solutions execute offline (13 new PASS checks across 18/02 + 18/04); 19/01 demonstrates SQL injection with a PASS-checked leak-vs-parameterized comparison.

**Resources (item 13):** glossary 71 → 116 terms; further reading for 16–20; Resources README lists the quiz index.

**Small items (14, 16, 17) + ROADMAP:** exit-code question closed by design (documented above); 16/08 bcrypt → verified stdlib `scrypt`; ROADMAP gained modules 17–20, all 11 projects, consistent stage numbering.

**Final gates (after all work):** `sync_docs` idempotent (0/0/577) · `mkdocs build --strict` exit 0, zero warnings · **243 passed, 0 failed, 1 skipped** (skip = live httpbin.org request, accurate reason) · 0 non-ASCII in any lesson `.py` · 4-file pattern intact on every topic · 114/114 quizzes registered.

---

## Findings & Fixes Log

### Session 1 (2026-10-23)

**Automated audit — real issues:**

1. ✅ **FIXED — Nav:** 71 topics in modules 06–20 were missing from `mkdocs.yml` nav (pages built but unreachable via sidebar; `--strict` passes because "not in nav" is INFO-level). Added all topics under Advanced/Practical sections, titles sourced from module README topic tables (06–15) and topic H1s (16–20).
2. ✅ **FIXED — Quiz title copy-paste:** `04_oop_concepts/01_classes_and_objects/quiz.md` was titled "Function Basics Quiz".
3. ✅ **FIXED — Quiz title terse:** `09_testing/03_test_driven_development/quiz.md` was "Quiz: TDD".
4. ✅ **FIXED — Committed artifacts:** `temp_demo.txt`, `example_library.db`, `reports_examples.db`, `sales_report.csv`, `sample_report.txt` untracked from git + .gitignore entries added (examples regenerate them on each run). `Projects/06_personal_journal/prompts.txt` is legitimate data — kept.

**Automated audit — false positives (verified fine, do not re-flag):**

- Quiz answers: two conventions exist — `<details><summary>Click for answer</summary>` (foundations-style) and `### Answers` section (OOP/testing-style). Both valid.
- Solutions: two conventions — "SOLUTIONS at bottom" (modules 01–03) and inline solutions after each exercise (modules 04+). Both valid; noted as a style inconsistency to accept or unify (decision pending).
- `input()` grep hits in 01_foundations/06, 06/04, 14/04 — all in comments/strings (simulated input), safe.
- `while True` in 16_essential_libraries/03_itertools — properly bounded generator.
- mkdocs INFO "not in nav" for `quiz.md`, `15_*/exercises.md`, `Projects/*/challenges.md` — by design (linked from pages, not nav).

**Known conventions divergence (needs decision, not urgent):**

- Modules 16–20 READMEs don't use the topics-table format that 06–15 use. Minor.

---

## Review Rubric (reuse for future sessions)

For each topic (README.md + examples.py + exercises.py + quiz.md):

1. **Technical accuracy** — snippets correct, claims about Python correct, complexity claims correct. Verify by running `PYTHONIOENCODING=utf-8 python examples.py` and `exercises.py`.
2. **Pedagogy** — analogies help, difficulty curve sane, no concepts used before taught (note: 02_data_structures 06–10 use classes before module 04 teaches them — known ordering tension to evaluate).
3. **Exercises & quiz** — solutions solve the stated problems and run; every quiz answer actually correct; difficulty appropriate.
4. **Consistency** — README: emoji title → concept → examples → common mistakes → quick reference → quiz link; examples.py: banner header/footer, section banners, no input()/unbounded loops/network; solutions present (either convention).

Windows note: always set `PYTHONIOENCODING=utf-8` when running lesson scripts or grep-like scans (cp1251 console).

---

## Remaining Structural Checks (for later sessions)

- [x] Structural audit (s4, lightweight re-run): 4-file pattern intact on every topic · 114/114 quizzes registered in `Resources/quizzes.md` · nav/file coverage enforced by `mkdocs build --strict` (exit 0)
- [x] Projects review pass (s3, README + source + challenges.md each)
- [x] Exercises tracks review pass (s3; s4 wrote the 14 missing files and put tracks under CI)
- [x] Resources review pass (s3; s4 closed the glossary/further-reading/README gaps)
- [x] Cross-module link integrity sweep — subsumed by `mkdocs build --strict` (every internal link must resolve; exit 0 with zero warnings)
- [x] ROADMAP.md sanity vs actual content (s4: modules 17–20 added, 11 projects listed, stage numbering unified, pytest wording fixed)
