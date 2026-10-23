#!/usr/bin/env python3
"""
generate_path.py - Build a personalized, week-by-week VibeLearning path
=======================================================================

Tell this tool your level, how many hours you can study per week, and what
you are aiming for. It picks the modules that fit your level, moves the
goal-relevant ones to the front, and splits the whole thing into a realistic
weekly schedule (about 1.5 hours per topic, including its exercises and quiz).

Usage:
    python tools/generate_path.py --preset beginner --hours 5 --goal general
    python tools/generate_path.py --preset intermediate --hours 8 --goal data
    python tools/generate_path.py --preset advanced --hours 10 --goal interview
    python tools/generate_path.py            # interactive: asks the same questions

Design notes:
  * Non-interactive runs are deterministic: the same flags always produce
    the same path, so you can re-run it any time and compare.
  * --preset selects the module range: beginner = modules 00-02,
    intermediate = 00-09, advanced = 00-20. Topics are discovered dynamically
    from the module folders - nothing is hardcoded.
  * --goal promotes related modules to the top of the order; it never adds
    modules outside the preset range. The 'interview' goal also appends the
    Resources/interview_prep pages at the end of the path.
  * With no flags the tool asks the same three questions interactively and
    re-asks on bad input; a closed stdin exits cleanly, never a traceback.
"""

from __future__ import annotations

import argparse
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INTERVIEW_PREP_DIR = ROOT / "Resources" / "interview_prep"

HOURS_PER_TOPIC = 1.5
DEFAULT_PRESET = "beginner"
DEFAULT_HOURS = 5
DEFAULT_GOAL = "general"
MAX_WEEK_ROWS = 12
MAX_PATH_WIDTH = 60

PRESET_CHOICES = ["beginner", "intermediate", "advanced"]
GOAL_CHOICES = ["general", "web", "data", "interview"]

# Preset -> (first module number, last module number).
PRESET_RANGES: dict[str, tuple[int, int]] = {
    "beginner": (0, 2),
    "intermediate": (0, 9),
    "advanced": (0, 20),
}

# Goal -> module numbers promoted to the top of the path, best first.
GOAL_PROMOTIONS: dict[str, list[int]] = {
    "general": [],
    "web": [18, 20, 10, 13],
    "data": [19, 16, 10, 2],
    "interview": [3, 2, 11],
}


class AbortedInput(Exception):
    """Raised when the interactive questions cannot be answered."""


# =============================================================================
# TOPIC DISCOVERY (mirrors tools/progress_tracker.py)
# =============================================================================

def discover_modules() -> list[str]:
    """Return the numbered module directory names (00_ ... 20_), sorted."""
    if not ROOT.is_dir():
        return []
    return [
        path.name
        for path in sorted(ROOT.iterdir())
        if path.is_dir() and re.match(r"^\d{2}_", path.name)
    ]


def module_number(module: str) -> int:
    """Return the numeric prefix of a module name, e.g. 01_foundations -> 1."""
    return int(module.split("_", 1)[0])


def topics_for_module(module: str) -> list[str]:
    """Return the topic ids of one module, in their natural numbered order."""
    module_path = ROOT / module
    if not module_path.is_dir():
        return []
    topic_dirs = [
        child.name
        for child in sorted(module_path.iterdir())
        if child.is_dir()
        and ((child / "README.md").is_file() or (child / "quiz.md").is_file())
    ]
    if topic_dirs:
        return [f"{module}/{name}" for name in topic_dirs]
    return [f"{module}/{page.stem}" for page in sorted(module_path.glob("[0-9][0-9]_*.md"))]


def interview_prep_topics() -> list[str]:
    """Return the Resources/interview_prep pages (README excluded), sorted."""
    if not INTERVIEW_PREP_DIR.is_dir():
        return []
    return [
        f"Resources/interview_prep/{page.name}"
        for page in sorted(INTERVIEW_PREP_DIR.glob("*.md"))
        if page.name != "README.md"
    ]


def ordered_topics(preset: str, goal: str) -> tuple[list[str], list[str], list[str]]:
    """Build the path. Returns (topics, in_scope_modules, promoted_modules)."""
    low, high = PRESET_RANGES[preset]
    in_scope = [m for m in discover_modules() if low <= module_number(m) <= high]
    promoted = [
        module
        for number in GOAL_PROMOTIONS[goal]
        for module in in_scope
        if module_number(module) == number
    ]
    promoted = list(dict.fromkeys(promoted))  # dedupe, keep goal order
    rest = [module for module in in_scope if module not in promoted]
    topics: list[str] = []
    for module in promoted + rest:
        topics.extend(topics_for_module(module))
    if goal == "interview":
        topics.extend(interview_prep_topics())
    return topics, in_scope, promoted


# =============================================================================
# SCHEDULE
# =============================================================================

def per_week_count(hours: int) -> int:
    """Topics per week: floor(hours / 1.5), at least one."""
    return max(1, int(hours // HOURS_PER_TOPIC))


def format_hours(value: float) -> str:
    return f"{value:g}"


def week_rows(topics: list[str], per_week: int) -> list[tuple[int, str, str, int, float]]:
    """One row per week: (week, first topic, last topic, count, hours)."""
    rows: list[tuple[int, str, str, int, float]] = []
    for start in range(0, len(topics), per_week):
        chunk = topics[start:start + per_week]
        rows.append((len(rows) + 1, chunk[0], chunk[-1], len(chunk),
                     len(chunk) * HOURS_PER_TOPIC))
    return rows


def print_week_table(rows: list[tuple[int, str, str, int, float]]) -> None:
    """Print the ASCII week table. Paths longer than MAX_PATH_WIDTH clip."""
    week_w = max([len("Week")] + [len(str(r[0])) for r in rows])
    from_w = min(MAX_PATH_WIDTH, max([len("From")] + [len(r[1]) for r in rows]))
    to_w = min(MAX_PATH_WIDTH, max([len("To")] + [len(r[2]) for r in rows]))
    count_w = max([len("Topics")] + [len(str(r[3])) for r in rows])
    hours_w = max([len("Hours")] + [len(format_hours(r[4])) for r in rows])

    def clip(text: str, width: int) -> str:
        if len(text) <= width:
            return text
        return text[: max(1, width - 3)] + "..."

    border = (f"+-{'-' * week_w}-+-{'-' * from_w}-+-{'-' * to_w}"
              f"-+-{'-' * count_w}-+-{'-' * hours_w}-+")
    print(border)
    print(f"| {'Week':<{week_w}} | {'From':<{from_w}} | {'To':<{to_w}}"
          f" | {'Topics':>{count_w}} | {'Hours':>{hours_w}} |")
    print(border)
    for week, first, last, count, hours in rows:
        print(f"| {week:>{week_w}} | {clip(first, from_w):<{from_w}}"
              f" | {clip(last, to_w):<{to_w}}"
              f" | {count:>{count_w}} | {format_hours(hours):>{hours_w}} |")
    print(border)


# =============================================================================
# PATH REPORT
# =============================================================================

def build_path(preset: str, hours: int, goal: str, notes: list[str]) -> int:
    topics, in_scope, promoted = ordered_topics(preset, goal)
    if not topics:
        print("No topics found under the module folders - are you running this")
        print("from the VibeLearning repository root?")
        return 1

    per_week = per_week_count(hours)
    print("=" * 70)
    print("PERSONALIZED LEARNING PATH")
    print("=" * 70)
    for note in notes:
        print(f"Note: {note}")
    print(f"Level: {preset}   Goal: {goal}   "
          f"Pace: {hours} h/week (about {HOURS_PER_TOPIC:g} h per topic)")
    print(f"\nModules in scope: {len(in_scope)}")
    if promoted:
        print(f"Moved to the front for the '{goal}' goal: {', '.join(promoted)}")

    print(f"\nSUGGESTED TOPIC ORDER ({len(topics)} topics)")
    print("-" * 70)
    for index, topic in enumerate(topics, 1):
        print(f"{index:>4}. {topic}")

    weeks = week_rows(topics, per_week)
    total_weeks = len(weeks)
    print(f"\nWEEK-BY-WEEK SCHEDULE (about {per_week} topic"
          f"{'s' if per_week != 1 else ''} per week)")
    print("-" * 70)
    print_week_table(weeks[:MAX_WEEK_ROWS])
    if total_weeks > MAX_WEEK_ROWS:
        hidden = weeks[MAX_WEEK_ROWS:]
        hidden_topics = sum(row[3] for row in hidden)
        hidden_hours = sum(row[4] for row in hidden)
        print(f"  ... and {len(hidden)} more weeks: {hidden_topics} more topics, "
              f"about {format_hours(hidden_hours)} h in total.")

    total_hours = len(topics) * HOURS_PER_TOPIC
    print(f"\nTotal: {len(topics)} topics, about {format_hours(total_hours)} h "
          f"-> roughly {total_weeks} week"
          f"{'s' if total_weeks != 1 else ''} at {hours} h/week.")
    print("\nNext steps:")
    print(f"  1. Start with: {topics[0]}/README.md")
    print(f"  2. When done, track it: "
          f"python tools/progress_tracker.py mark {topics[0]}")
    print("  3. Re-run this tool any time - same flags, same path.")
    return 0


# =============================================================================
# INTERACTIVE MODE (used only when no flags are given)
# =============================================================================

def ask_choice(question: str, options: list[tuple[str, str]]) -> str:
    """Ask a numbered question until the answer is valid; returns the value."""
    print(question)
    for index, (label, _value) in enumerate(options, 1):
        print(f"  {index}. {label}")
    while True:
        try:
            raw = input(f"Enter 1-{len(options)}: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            raise AbortedInput("no answer given") from None
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return options[int(raw) - 1][1]
        print(f"  Please type a number from 1 to {len(options)}.")


def ask_hours() -> int:
    """Ask for weekly study hours until the answer is a whole number 1-80."""
    while True:
        try:
            raw = input("How many hours can you study per week? (1-80): ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            raise AbortedInput("no answer given") from None
        try:
            hours = int(raw)
        except ValueError:
            print("  Please type a whole number, for example 6.")
            continue
        if 1 <= hours <= 80:
            return hours
        print("  Please pick a number between 1 and 80.")


def interactive_answers() -> tuple[str, int, str]:
    print("Let's build your learning path - three quick questions.")
    print("(Prefer flags? Try: python tools/generate_path.py --help)\n")
    preset = ask_choice("How experienced are you with Python?", [
        ("Beginner - brand new or shaky on the basics (modules 00-02)",
         "beginner"),
        ("Intermediate - comfortable, wants the core plus more (modules 00-09)",
         "intermediate"),
        ("Advanced - I want everything, all 21 modules (modules 00-20)",
         "advanced"),
    ])
    hours = ask_hours()
    goal = ask_choice("What are you aiming for?", [
        ("General Python skills", "general"),
        ("Web development and APIs", "web"),
        ("Data processing and analysis", "data"),
        ("Interview preparation", "interview"),
    ])
    return preset, hours, goal


# =============================================================================
# ENTRY POINT
# =============================================================================

def positive_hours(text: str) -> int:
    try:
        value = int(text)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{text}' is not a whole number") from None
    if not 1 <= value <= 80:
        raise argparse.ArgumentTypeError(
            "weekly hours must be a whole number between 1 and 80")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="generate_path.py",
        description="Build a personalized week-by-week VibeLearning path.",
    )
    parser.add_argument("--preset", choices=PRESET_CHOICES,
                        help="your level: beginner, intermediate or advanced")
    parser.add_argument("--hours", type=positive_hours, metavar="N",
                        help="study hours per week, 1-80 (default %d)"
                             % DEFAULT_HOURS)
    parser.add_argument("--goal", choices=GOAL_CHOICES,
                        help="what you are aiming for: general, web, data or "
                             "interview")
    args = parser.parse_args(argv)

    # Never let a console codepage crash the reporter itself.
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass

    notes: list[str] = []
    if args.preset is None and args.hours is None and args.goal is None:
        try:
            preset, hours, goal = interactive_answers()
        except AbortedInput:
            print("No answers received - nothing was generated.")
            print("Run it with flags instead, for example:")
            print("  python tools/generate_path.py --preset intermediate "
                  "--hours 8 --goal data")
            return 1
    else:
        # Any flag given means non-interactive: fill the gaps with defaults.
        preset = args.preset or DEFAULT_PRESET
        hours = args.hours if args.hours is not None else DEFAULT_HOURS
        goal = args.goal or DEFAULT_GOAL
        if args.preset is None:
            notes.append(f"--preset not given; using '{preset}'.")
        if args.hours is None:
            notes.append(f"--hours not given; using {hours} h/week.")
        if args.goal is None:
            notes.append(f"--goal not given; using '{goal}'.")
    return build_path(preset, hours, goal, notes)


if __name__ == "__main__":
    sys.exit(main())
