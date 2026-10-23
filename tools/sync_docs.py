#!/usr/bin/env python3
"""
sync_docs.py - Mirror the repository content into docs/ for MkDocs
==================================================================

MkDocs is configured with ``docs_dir: docs``, so the site is built from
``docs/``. The *real* source of truth is the repository root. This script
copies the root content into ``docs/`` so the two can never drift apart.

Why a script instead of copying by hand:
  * one command keeps the site in sync (and CI runs it on every build)
  * ``docs/`` is git-ignored, so it can be rebuilt from scratch anytime
  * it works the same on Windows, macOS and Linux (standard library only)

Usage:
    python tools/sync_docs.py            # mirror root -> docs/
    python tools/sync_docs.py --dry-run  # show what would happen
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Repository root is the parent of the directory holding this file.
ROOT = Path(__file__).resolve().parent.parent

# Where MkDocs expects the rendered sources.
DOCS = ROOT / "docs"

# Numbered module directories: 00_getting_started ... 20_web_basics
MODULE_DIR_PATTERN = re.compile(r"^\d{2}_")

# Non-numbered directories that also belong on the site.
EXTRA_DIRS = ("Resources", "Projects", "Exercises", "stylesheets")

# Root-level files that belong on the site (copied only if they exist).
EXTRA_FILES = ("README.md", "404.md")

# Files/directories never copied, even if they live inside a source dir.
IGNORED_NAMES = {".DS_Store", "Thumbs.db", "__pycache__", ".git", ".pytest_cache"}
IGNORED_SUFFIXES = {".pyc", ".pyo", ".swp", ".swo", "~"}


def log(message: str) -> None:
    """Print a message immediately (so output interleaves correctly)."""
    print(message, flush=True)


def source_directories() -> list[Path]:
    """Return every directory at the root that should be mirrored."""
    dirs: list[Path] = []
    for entry in sorted(ROOT.iterdir()):
        if not entry.is_dir():
            continue
        if entry.name in {"docs", "site", ".git"}:
            continue
        if MODULE_DIR_PATTERN.match(entry.name) or entry.name in EXTRA_DIRS:
            dirs.append(entry)
    return dirs


def is_ignored(path: Path) -> bool:
    """True for files we never want to mirror (caches, editor cruft...)."""
    if path.name in IGNORED_NAMES:
        return True
    return path.suffix in IGNORED_SUFFIXES or path.name.endswith("~")


def collect_sources() -> dict[str, Path]:
    """Map destination-relative POSIX path -> absolute source path."""
    mapping: dict[str, Path] = {}

    for directory in source_directories():
        for path in directory.rglob("*"):
            if path.is_dir() or is_ignored(path):
                continue
            mapping[path.relative_to(ROOT).as_posix()] = path

    for name in EXTRA_FILES:
        path = ROOT / name
        if path.is_file():
            mapping[name] = path

    return mapping


def needs_copy(source: Path, destination: Path) -> bool:
    """True when the destination is missing or out of date.

    Size + mtime is enough here: while developing, any edited file gets a new
    mtime, and ``shutil.copy2`` preserves mtime so a second run never re-copies.
    """
    if not destination.exists() or not destination.is_file():
        return True
    src_stat = source.stat()
    dst_stat = destination.stat()
    return src_stat.st_size != dst_stat.st_size or int(src_stat.st_mtime) != int(dst_stat.st_mtime)


def prune(desired: set[str], dry_run: bool) -> int:
    """Delete files in docs/ that no longer exist at the root."""
    if not DOCS.exists():
        return 0

    removed = 0
    for path in DOCS.rglob("*"):
        if path.is_dir():
            continue
        relative = path.relative_to(DOCS).as_posix()
        if relative in desired:
            continue
        removed += 1
        if not dry_run:
            path.unlink()

    # Remove directories that became empty, deepest first.
    if not dry_run:
        directories = [p for p in DOCS.rglob("*") if p.is_dir()]
        for path in sorted(directories, key=lambda p: len(p.parts), reverse=True):
            try:
                next(path.iterdir())
            except StopIteration:
                path.rmdir()

    return removed


def main() -> int:
    parser = argparse.ArgumentParser(description="Mirror repository content into docs/.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without touching any file.",
    )
    args = parser.parse_args()

    if not DOCS.exists() and not args.dry_run:
        DOCS.mkdir(parents=True, exist_ok=True)

    sources = collect_sources()
    log(f"Syncing {len(sources)} files into {DOCS.relative_to(ROOT).as_posix()}/ ...")

    copied = updated = unchanged = 0

    for relative, source in sorted(sources.items()):
        destination = DOCS / relative
        if destination.exists() and not needs_copy(source, destination):
            unchanged += 1
            continue

        is_new = not destination.exists()
        if not args.dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

        if is_new:
            copied += 1
        else:
            updated += 1

    removed = prune(set(sources), args.dry_run)

    prefix = "[dry run] " if args.dry_run else ""
    log(
        f"{prefix}Done: {copied} copied, {updated} updated, "
        f"{unchanged} unchanged, {removed} removed."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
