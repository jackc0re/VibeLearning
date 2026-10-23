#!/usr/bin/env python3
"""
check_exercise.py - Check a topic's exercises.py without spoilers
==================================================================

Run the exercises.py of one topic in a child process and print a short
progress report: the PASS/FAIL lines the file's self-tests printed, a
total ("2 passed, 1 failed, 3 not attempted"), and where the file lives.
The solutions section is never shown, so you can run this as often as
you like without spoilers.

Usage:
    python tools/check_exercise.py 02_data_structures/04_sets
    python tools/check_exercise.py 01_foundations/07_type_hints
    python tools/check_exercise.py 02_data_structures/04_sets/exercises.py
    python tools/check_exercise.py --timeout 30 Exercises/beginner/01_variables_and_types.py

The topic can be given with or without the exercises.py filename.

How the total is computed:
  * passed / failed - the PASS / FAIL lines the file printed while running
    (files such as 01_foundations/07_type_hints print one per check;
    files without self-tests print none)
  * not attempted   - a best-effort scan of the source, with the solutions
    section removed, for stubs still left as pass / ... / TODO /
    "Your code here". It is a hint, not an exact science.

Exit codes:
  0  the file ran cleanly and a report was produced (failing checks are
     your progress, not a bug - fix them and run again)
  1  unknown topic, missing file, crash, or timeout
"""

from __future__ import annotations

import argparse
import difflib
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DEFAULT_TIMEOUT = 20

# Source comments that mark an unfinished stub (checked case-insensitively).
STUB_CODE_BODIES = ("pass", "...")

# A comment line like "# SOLUTIONS" or "# SOLUTION 1" starts the solutions
# section in the source; everything from there on is hidden from the report.
SOLUTION_COMMENT_RE = re.compile(r"^#+\s*SOLUTION")

# Any printed line containing the standalone word PASS or FAIL is treated as
# one self-test result. The repo's self-tests print several shapes:
#   "PASS: label", "PASS label", "FAIL label: got ..., expected ...",
#   "PASS Login successful!", "Welcome! PASS"
PASS_RE = re.compile(r"\bPASS\b")
FAIL_RE = re.compile(r"\bFAIL\b")

MAX_RESULT_LINES = 40


# =============================================================================
# Finding the exercise file
# =============================================================================

def module_dirs() -> list[Path]:
    """The NN_* module directories at the repo root."""
    return sorted(p for p in ROOT.iterdir() if p.is_dir() and re.match(r"^\d{2}_", p.name))


def resolve_topic(arg: str) -> Path:
    """Turn a user argument into an existing exercise file, or raise LookupError.

    Accepts a topic directory ("02_data_structures/04_sets"), the same with a
    trailing slash or the filename (".../04_sets/exercises.py"), or a direct
    path to a .py file (e.g. the Exercises/<track> practice files).
    """
    candidate = Path(arg)
    if not candidate.exists():
        rooted = ROOT / candidate
        if rooted.exists():
            candidate = rooted

    if candidate.is_file() and candidate.suffix == ".py":
        return candidate.resolve()

    if candidate.is_dir():
        exercise = candidate / "exercises.py"
        if exercise.is_file():
            return exercise.resolve()
        topics = [
            d.name
            for d in sorted(candidate.iterdir())
            if d.is_dir() and (d / "exercises.py").is_file()
        ]
        if topics:
            raise LookupError(
                f"'{arg}' is a module directory, not a topic. "
                f"Pick a topic inside it, for example: {candidate.name}/{topics[0]}"
            )
        raise LookupError(f"No exercises.py found in '{arg}'.")

    raise LookupError(f"Unknown topic '{arg}'." + suggest_topics(arg))


def suggest_topics(bad: str) -> str:
    """Best-effort 'did you mean ...' names for an unknown topic."""
    names: list[str] = []
    for module in module_dirs():
        for topic in sorted(module.iterdir()):
            if topic.is_dir() and (topic / "exercises.py").is_file():
                names.append(f"{module.name}/{topic.name}")
    close = difflib.get_close_matches(bad, names, n=3, cutoff=0.4)
    if close:
        return " Did you mean: " + ", ".join(close) + "?"
    return ""


# =============================================================================
# Hiding the solutions
# =============================================================================

def source_without_solutions(path: Path) -> str:
    """The file's source, cut at the first '# SOLUTION...' comment banner."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if SOLUTION_COMMENT_RE.match(line.strip()):
            return "\n".join(lines[:index])
    return text


def output_without_solutions(output: str) -> tuple[list[str], bool]:
    """Captured child output, cut at a printed SOLUTIONS banner.

    Returns (kept_lines, hidden_something).
    """
    kept: list[str] = []
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.upper().startswith("SOLUTION") and len(stripped) <= 80:
            return kept, True
        kept.append(line)
    return kept, False


# =============================================================================
# Counting unfinished stubs
# =============================================================================

def count_stubs(source: str) -> int:
    """Count stub regions still marked pass / ... / TODO / "Your code here".

    Adjacent marker lines (a "Your code here" comment directly above a pass,
    for instance) count as ONE stub.
    """
    marker_lines: list[int] = []
    for index, line in enumerate(source.splitlines()):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped in STUB_CODE_BODIES or stripped.startswith("raise NotImplementedError"):
            marker_lines.append(index)
            continue
        if stripped.startswith("#"):
            comment = stripped.lstrip("#").strip().lower()
            if "todo" in comment or "your code" in comment:
                marker_lines.append(index)

    if not marker_lines:
        return 0
    regions = 1
    for previous, current in zip(marker_lines, marker_lines[1:]):
        if current - previous > 3:
            regions += 1
    return regions


# =============================================================================
# Running the file
# =============================================================================

def run_file(path: Path, timeout: int) -> tuple[int, str, bool, float]:
    """Run one exercise file. Returns (exit_code, output, timed_out, seconds)."""
    started = time.monotonic()
    env = dict(os.environ)
    # Exercise files may print arrows or emoji; force UTF-8 so this behaves
    # identically on Windows (cp1251/cp1252 consoles) and in Linux CI.
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    try:
        result = subprocess.run(
            [sys.executable, str(path)],
            cwd=str(path.parent),
            stdin=subprocess.DEVNULL,  # input() fails fast instead of hanging
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=env,
        )
    except subprocess.TimeoutExpired:
        return 1, "", True, time.monotonic() - started
    return result.returncode, result.stdout or "", False, time.monotonic() - started


# =============================================================================
# Reporting
# =============================================================================

def show_result_lines(passed: list[str], failed: list[str]) -> None:
    if not passed and not failed:
        print("Self-test lines the file printed:")
        print("  (none - this file prints no PASS/FAIL self-tests)")
        return
    print("Self-test lines the file printed:")
    lines = failed + passed  # failures first: they are what to work on
    for line in lines[:MAX_RESULT_LINES]:
        print(f"  {line.strip()}")
    if len(lines) > MAX_RESULT_LINES:
        print(f"  ... and {len(lines) - MAX_RESULT_LINES} more")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Run one topic's exercises.py and report your progress "
            "(PASS/FAIL lines + unfinished stubs) without showing solutions."
        )
    )
    parser.add_argument(
        "topic",
        help="topic to check, e.g. 02_data_structures/04_sets (exercises.py optional)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"per-file time limit in seconds (default {DEFAULT_TIMEOUT})",
    )
    args = parser.parse_args()

    # Never let the reporter crash while reporting (Windows codepages etc.).
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass

    try:
        path = resolve_topic(args.topic)
    except LookupError as error:
        print(f"Oops - {error}", file=sys.stderr)
        print("Try: python tools/check_exercise.py <module>/<topic>", file=sys.stderr)
        return 1

    try:
        relative = path.relative_to(ROOT).as_posix()
    except ValueError:  # file outside the repository - show it as given
        relative = str(path)
    print(f"Checking {relative} ...")

    code, output, timed_out, elapsed = run_file(path, args.timeout)

    if timed_out:
        print(f"\nTimed out after {args.timeout}s.")
        print("The file may be waiting for keyboard input (input()) or stuck")
        print(f"in a loop. Try running it yourself: python {relative}")
        return 1

    kept_lines, hid_solutions = output_without_solutions(output)
    passed = [line for line in kept_lines if PASS_RE.search(line)]
    failed = [line for line in kept_lines if FAIL_RE.search(line)]
    stubs = count_stubs(source_without_solutions(path))

    print(f"({elapsed:.1f}s, exit code {code})\n")
    show_result_lines(passed, failed)
    print(f"\nProgress: {len(passed)} passed, {len(failed)} failed, "
          f"{stubs} not attempted")

    if hid_solutions:
        print("(Everything at or after the file's SOLUTIONS banner was hidden - no spoilers.)")

    print(f"\nFile: {relative}")
    if stubs:
        print(f"Open it, solve the {stubs} unfinished stub(s) marked pass/TODO/"
              f"\"Your code here\",")
        print("then run this check again.")
    elif not passed and not failed:
        print("No self-tests and no unfinished stubs were detected - nothing to score.")

    if code != 0:
        print("\nThe file stopped early with an error, so its full output is not")
        print("shown here (it may contain solution code). See the whole picture")
        print(f"by running it directly: python {relative}")
        if "input" in output.lower():
            print("(This file appears to ask for keyboard input, which this")
            print(" checker cannot provide - run it in your terminal instead.)")
        return 1

    print("\nKeep going - small steps every day!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
