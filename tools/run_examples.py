#!/usr/bin/env python3
"""
run_examples.py - Execute every lesson's examples.py/exercises.py and report failures
====================================================================================

This is a *learning* repository: the `examples.py` and `exercises.py` files are the
product. Nothing used to run them, so a broken file could ship silently. This script
runs each one in its own process, with a timeout, and fails loudly if any of them crash.

Usage:
    python tools/run_examples.py               # run everything
    python tools/run_examples.py --verbose     # show per-file output too
    python tools/run_examples.py --timeout 20  # change the per-file limit (seconds)
    python tools/run_examples.py path/to/dir   # only a subtree

Design notes:
  * Each example gets its own subprocess, so one `sys.exit()` or infinite loop
    cannot take the whole run down.
  * stdin is closed (`DEVNULL`), so an example that waits for `input()` fails fast
    instead of hanging until the timeout.
  * Examples that are *meant* to be interactive or to open a socket are listed in
    SKIP below, with a reason. Keep that list short and specific.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Directories that are not lesson content.
SKIP_DIRS = {"docs", "site", ".git", "venv", "node_modules", "__pycache__", "tools"}

# Examples that cannot run unattended. Each entry needs a reason, and the list
# should stay short - if something is merely broken, fix it instead of skipping.
SKIP: dict[str, str] = {
    "18_working_with_apis/05_api_best_practices/examples.py":
        "makes live HTTP requests to httpbin.org; no network in CI",
}

DEFAULT_TIMEOUT = 15


def discover(target: Path | None) -> list[Path]:
    """Find every examples.py and exercises.py under the repo root (or under `target`).

    The Exercises/<track>/NN_*.py practice files are also discovered by name,
    so the practice tracks get the same crash protection as lesson content.
    """
    base = target or ROOT
    found: list[Path] = []
    for name in ("examples.py", "exercises.py"):
        for path in sorted(base.rglob(name)):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            found.append(path)
    # Find the Exercises root: `base` itself, an ancestor of it, or base/Exercises.
    exercises_dir = next(
        (p for p in [base, *base.parents] if p.name == "Exercises"),
        base / "Exercises",
    )
    if exercises_dir.is_dir():
        for path in sorted(exercises_dir.glob("*/*.py")):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            found.append(path)
    return sorted(set(found))


def run_one(path: Path, timeout: int) -> tuple[bool, str, float]:
    """Run a single example. Returns (ok, detail, seconds)."""
    relative = path.relative_to(ROOT).as_posix()
    started = time.monotonic()
    env = dict(os.environ)
    # Examples print arrows and emoji; force UTF-8 so this behaves identically on
    # Windows (cp1251/cp1252 consoles) and in Linux CI.
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    try:
        result = subprocess.run(
            [sys.executable, str(path)],
            cwd=str(path.parent),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=env,
        )
    except subprocess.TimeoutExpired:
        return False, f"timed out after {timeout}s", time.monotonic() - started

    elapsed = time.monotonic() - started
    if result.returncode == 0:
        return True, "", elapsed

    output = (result.stdout or "").strip().splitlines()
    tail = "\n".join(output[-12:]) if output else "(no output)"
    return False, f"exit code {result.returncode}\n{tail}", elapsed


def main() -> int:
    parser = argparse.ArgumentParser(description="Run every examples.py with a timeout.")
    parser.add_argument("target", nargs="?", help="only run examples under this directory")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT,
                        help=f"per-file timeout in seconds (default {DEFAULT_TIMEOUT})")
    parser.add_argument("--verbose", action="store_true", help="print output of passing files")
    args = parser.parse_args()

    # Failure output can contain characters the Windows console codepage cannot
    # represent. Never let the reporter crash while reporting a crash.
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass

    target = Path(args.target).resolve() if args.target else None
    examples = discover(target)

    if not examples:
        print("No examples.py files found.", file=sys.stderr)
        return 1

    print(f"Running {len(examples)} examples.py files (timeout {args.timeout}s each)\n")

    failures: list[tuple[str, str]] = []
    skipped: list[tuple[str, str]] = []

    for index, path in enumerate(examples, 1):
        relative = path.relative_to(ROOT).as_posix()
        label = f"[{index:>3}/{len(examples)}]"

        if relative in SKIP:
            skipped.append((relative, SKIP[relative]))
            print(f"{label} SKIP  {relative}  ({SKIP[relative]})")
            continue

        ok, detail, elapsed = run_one(path, args.timeout)
        if ok:
            print(f"{label} ok    {relative}  ({elapsed:.1f}s)")
            if args.verbose:
                print(f"          {detail}")
        else:
            failures.append((relative, detail))
            print(f"{label} FAIL  {relative}")
            for line in detail.splitlines():
                print(f"          {line}")

    print("\n" + "=" * 70)
    passed = len(examples) - len(failures) - len(skipped)
    print(f"{passed} passed, {len(failures)} failed, {len(skipped)} skipped")

    if skipped:
        print("\nSkipped (cannot run unattended):")
        for relative, reason in skipped:
            print(f"  - {relative}: {reason}")

    if failures:
        print("\nFailed examples:")
        for relative, _ in failures:
            print(f"  - {relative}")
        print("\nFix these before merging - they are the product users run.")
        return 1

    print("\nAll examples ran cleanly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
