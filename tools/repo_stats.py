#!/usr/bin/env python3
"""
repo_stats.py - Repository statistics for VibeLearning
=======================================================

Scan the repository and print plain-ASCII tables: how many modules, topics,
quizzes, projects and exercise tracks it holds, how many .py and .md files
(and total lines) it contains, and which topics are the largest by line
count. Everything is counted dynamically by scanning - nothing is hardcoded
- and nothing is written anywhere.

Usage:
    python tools/repo_stats.py            # default: top 5 topics
    python tools/repo_stats.py --top 10   # more of the largest topics

Counting rules:
  * modules         - NN_* directories at the repo root
  * topics          - directories inside a module that contain a quiz.md
  * quizzes         - quiz.md files found anywhere in the scan
  * projects        - subdirectories of Projects/
  * exercise tracks - subdirectories of Exercises/
  * generated or vendored trees are never counted: docs/, site/, .git,
    __pycache__, venv, node_modules
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Directories that are not repository content.
SKIP_DIRS = {"docs", "site", ".git", "venv", "node_modules", "__pycache__"}

MODULE_RE = re.compile(r"^\d{2}_")


# =============================================================================
# Scanning
# =============================================================================

def scan_files(root: Path) -> list[Path]:
    """Every file under root, skipping generated/vendored directories."""
    found: list[Path] = []

    def walk(directory: Path) -> None:
        for entry in sorted(directory.iterdir()):
            if entry.is_dir():
                if entry.name not in SKIP_DIRS:
                    walk(entry)
            elif entry.is_file():
                found.append(entry)

    walk(root)
    return found


def count_lines(path: Path) -> int:
    """Line count as wc -l counts it (newline bytes); never raises."""
    try:
        return path.read_bytes().count(b"\n")
    except OSError:
        return 0


# =============================================================================
# Counting the things the tables show
# =============================================================================

def find_modules() -> list[Path]:
    return sorted(p for p in ROOT.iterdir() if p.is_dir() and MODULE_RE.match(p.name))


def find_topics(modules: list[Path]) -> list[Path]:
    return sorted(
        topic
        for module in modules
        for topic in module.iterdir()
        if topic.is_dir() and (topic / "quiz.md").is_file()
    )


def topic_line_counts(files: list[Path], topics: list[Path]) -> dict[str, tuple[str, int]]:
    """Map 'module/topic' -> (module_name, total lines of all files inside)."""
    by_prefix: dict[tuple[str, str], int] = {}
    for path in files:
        parts = path.relative_to(ROOT).parts
        if len(parts) >= 3:
            key = (parts[0], parts[1])
            by_prefix[key] = by_prefix.get(key, 0) + count_lines(path)
    counts: dict[str, tuple[str, int]] = {}
    for topic in topics:
        key = (topic.parent.name, topic.name)
        counts[f"{key[0]}/{key[1]}"] = (key[0], by_prefix.get(key, 0))
    return counts


# =============================================================================
# Printing
# =============================================================================

def print_table(headers: list[str], rows: list[list[str]]) -> None:
    """A plain '|' table: first column left-aligned, the rest right-aligned."""
    widths = [len(header) for header in headers]
    for row in rows:
        for index, cell in enumerate(row):
            widths[index] = max(widths[index], len(cell))

    def format_row(row: list[str]) -> str:
        cells = [
            cell.ljust(widths[index]) if index == 0 else cell.rjust(widths[index])
            for index, cell in enumerate(row)
        ]
        return "| " + " | ".join(cells) + " |"

    print(format_row(headers))
    print("|" + "|".join("-" * (width + 2) for width in widths) + "|")
    for row in rows:
        print(format_row(row))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Print repository statistics (modules, topics, files, lines) as ASCII tables."
    )
    parser.add_argument("--top", type=int, default=5,
                        help="how many of the largest topics to show (default 5)")
    args = parser.parse_args()

    modules = find_modules()
    topics = find_topics(modules)
    files = scan_files(ROOT)

    projects = sorted(p for p in (ROOT / "Projects").iterdir() if p.is_dir()) \
        if (ROOT / "Projects").is_dir() else []
    tracks = sorted(p for p in (ROOT / "Exercises").iterdir() if p.is_dir()) \
        if (ROOT / "Exercises").is_dir() else []

    py_files = [f for f in files if f.suffix == ".py"]
    md_files = [f for f in files if f.suffix == ".md"]
    py_lines = sum(count_lines(f) for f in py_files)
    md_lines = sum(count_lines(f) for f in md_files)
    quizzes = sum(1 for f in files if f.name == "quiz.md")

    print("VibeLearning repository statistics")
    print("==================================")
    print()
    print("Counts")
    print("------")
    print_table(
        ["Metric", "Value"],
        [
            ["Modules (NN_* directories)", str(len(modules))],
            ["Topics (directories with a quiz.md)", str(len(topics))],
            ["Quizzes (quiz.md files)", str(quizzes)],
            ["Projects (Projects/ subdirectories)", str(len(projects))],
            ["Exercise tracks (Exercises/ subdirectories)", str(len(tracks))],
        ],
    )

    print()
    print("Files and lines")
    print("---------------")
    print_table(
        ["Kind", "Files", "Lines"],
        [
            ["Python (.py)", str(len(py_files)), str(py_lines)],
            ["Markdown (.md)", str(len(md_files)), str(md_lines)],
        ],
    )

    ranked = sorted(
        ((name, module, lines) for name, (module, lines) in topic_line_counts(files, topics).items()),
        key=lambda item: item[2],
        reverse=True,
    )[: max(args.top, 0)]

    title = f"Largest {len(ranked)} topics by line count"
    print()
    print(title)
    print("-" * len(title))
    if ranked:
        print_table(
            ["Topic", "Module", "Lines"],
            [[name, module, str(lines)] for name, module, lines in ranked],
        )
    else:
        print("(no topics found)")

    print()
    print("Counts are computed by scanning the repository; generated docs/,")
    print("site/, caches and .git are excluded. Nothing was written to disk.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
