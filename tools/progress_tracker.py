#!/usr/bin/env python3
"""
progress_tracker.py - Track which VibeLearning topics you have finished
=======================================================================

Working through 100+ topics across 21 modules is a marathon, not a sprint.
This tool is your checklist: mark a topic the day you finish it, then come
back any time to see how far along you are and what to study next.

Progress is stored in ~/.vibelearning/progress.json (your home directory),
so marking topics never writes anything inside the repository itself.

Usage:
    python tools/progress_tracker.py                                # same as 'status'
    python tools/progress_tracker.py status                         # summary + next topics
    python tools/progress_tracker.py list                           # full checklist
    python tools/progress_tracker.py mark 01_foundations/02_operators
    python tools/progress_tracker.py unmark 01_foundations/02_operators
    python tools/progress_tracker.py reset --yes                    # delete all progress

Design notes:
  * Topics are discovered dynamically from the module folders (00_ ... 20_),
    so new lessons show up automatically - nothing is hardcoded.
  * Every subcommand is non-interactive, so the tool is safe to script.
  * A missing or unreadable progress file is not an error: you simply start
    from zero. Unknown topic ids get a friendly "did you mean" list.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_DIR = Path.home() / ".vibelearning"
STATE_FILE = STATE_DIR / "progress.json"

BAR_WIDTH = 20
CLOSE_MATCH_COUNT = 3
NEXT_UP_COUNT = 3


# =============================================================================
# TOPIC DISCOVERY
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


def discover_topics() -> list[str]:
    """Return every topic id as 'module_dir/topic_name', in module order.

    Modules 01 and up contribute their subdirectories that contain a
    README.md or quiz.md (the standard topic layout). Modules without any
    topic subdirectories (like 00_getting_started) contribute their numbered
    top-level pages instead, so reading material counts too.
    """
    topics: list[str] = []
    for module in discover_modules():
        module_path = ROOT / module
        topic_dirs = [
            child.name
            for child in sorted(module_path.iterdir())
            if child.is_dir()
            and ((child / "README.md").is_file() or (child / "quiz.md").is_file())
        ]
        if topic_dirs:
            topics.extend(f"{module}/{name}" for name in topic_dirs)
        else:
            for page in sorted(module_path.glob("[0-9][0-9]_*.md")):
                topics.append(f"{module}/{page.stem}")
    return topics


def clean_topic(user_input: str) -> str:
    """Normalize a user-typed topic id (separators, stray slashes, .md)."""
    cleaned = user_input.strip().replace("\\", "/").strip("/")
    if cleaned.endswith(".md"):
        cleaned = cleaned[: -len(".md")]
    return cleaned


def resolve_topic(user_input: str, topics: list[str]) -> str | None:
    """Return the matching topic id, or None if the input matches none."""
    cleaned = clean_topic(user_input)
    return cleaned if cleaned in set(topics) else None


def suggest_topics(user_input: str, topics: list[str]) -> list[str]:
    """Return up to three existing topic ids that look like `user_input`."""
    cleaned = clean_topic(user_input)
    matches = difflib.get_close_matches(cleaned, topics, n=CLOSE_MATCH_COUNT, cutoff=0.4)
    tail = cleaned.rsplit("/", 1)[-1]
    by_name = {topic.rsplit("/", 1)[-1]: topic for topic in topics}
    for name in difflib.get_close_matches(tail, sorted(by_name), n=CLOSE_MATCH_COUNT, cutoff=0.4):
        if by_name[name] not in matches:
            matches.append(by_name[name])
    return matches[:CLOSE_MATCH_COUNT]


# =============================================================================
# SAVED STATE (~/.vibelearning/progress.json)
# =============================================================================

def fresh_state() -> dict:
    return {"version": 1, "completed": {}}


def load_state() -> dict:
    """Load saved progress. A missing or unreadable file means a fresh start."""
    if not STATE_FILE.is_file():
        return fresh_state()
    try:
        data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
        completed = data.get("completed", {})
        if not isinstance(completed, dict):
            raise ValueError("'completed' is not an object")
    except (OSError, ValueError, AttributeError) as exc:
        backup = STATE_FILE.with_name("progress.json.corrupt")
        note = ""
        try:
            backup.write_text(STATE_FILE.read_text(encoding="utf-8"), encoding="utf-8")
            note = f" (a copy was kept as {backup.name})"
        except OSError:
            pass
        print(f"Warning: could not read {STATE_FILE} ({exc}){note}; starting fresh.")
        return fresh_state()
    return {"version": 1, "completed": completed}


def save_state(state: dict) -> None:
    """Write progress to ~/.vibelearning/, creating the directory if needed."""
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(
        json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


# =============================================================================
# SUBCOMMANDS
# =============================================================================

def print_status_line(topics: list[str], completed: dict) -> None:
    """Print the done/total summary and the next suggested topics."""
    total = len(topics)
    done = sum(1 for topic in topics if topic in completed)
    percent = int(round(done * 100 / total)) if total else 0
    print(f"\nCompleted: {done} / {total} topics ({percent}%)")
    filled = int(round(BAR_WIDTH * done / total)) if total else 0
    bar = "#" * filled + "-" * (BAR_WIDTH - filled)
    print(f"  [{bar}] {percent}%")

    if total == 0:
        print("\nNo topics found - are you running this from the repo root?")
        return
    if done == total:
        print("\nEvery topic marked done - amazing work! Consider revisiting")
        print("the projects in Projects/ or the Resources/ cheatsheets.")
        return

    next_up = [topic for topic in topics if topic not in completed][:NEXT_UP_COUNT]
    print(f"\nNext up - suggested topics:")
    for index, topic in enumerate(next_up, 1):
        print(f"  {index}. {topic}")
    print("\nTips:")
    print("  - Mark one done:  python tools/progress_tracker.py mark <module/topic>")
    print("  - Full checklist: python tools/progress_tracker.py list")
    print("  - Personal order: python tools/generate_path.py")


def cmd_status(_args: argparse.Namespace) -> int:
    topics = discover_topics()
    if not topics:
        print("No topics found under the module folders - are you running this")
        print("from the VibeLearning repository root?")
        return 1
    state = load_state()
    print("=" * 70)
    print("VIBELEARNING PROGRESS")
    print("=" * 70)
    if not state["completed"]:
        print("\nNo saved progress yet - that is about to change!")
    print_status_line(topics, state["completed"])
    return 0


def cmd_list(_args: argparse.Namespace) -> int:
    topics = discover_topics()
    if not topics:
        print("No topics found under the module folders - are you running this")
        print("from the VibeLearning repository root?")
        return 1
    completed = load_state()["completed"]
    print("=" * 70)
    print("ALL TOPICS")
    print("=" * 70)
    current_module = None
    module_done = 0
    module_total = 0
    for topic in topics:
        module = topic.split("/", 1)[0]
        if module != current_module:
            if current_module is not None:
                print(f"  -> {current_module}: {module_done}/{module_total} done")
            group = [t for t in topics if t.split("/", 1)[0] == module]
            module_done = sum(1 for t in group if t in completed)
            module_total = len(group)
            header = f"{module}  ({module_done}/{module_total} done)"
            print(f"\n{header}")
            print("-" * len(header))
            current_module = module
        if topic in completed:
            when = str(completed[topic])[:10]
            print(f"  [x] {topic}  (marked {when})")
        else:
            print(f"  [ ] {topic}")
    if current_module is not None:
        print(f"  -> {current_module}: {module_done}/{module_total} done")
    done = sum(1 for topic in topics if topic in completed)
    print(f"\nTotal: {done}/{len(topics)} topics marked done.")
    return 0


def cmd_mark(args: argparse.Namespace) -> int:
    return change_mark(args.topic, mark=True)


def cmd_unmark(args: argparse.Namespace) -> int:
    return change_mark(args.topic, mark=False)


def change_mark(user_input: str, mark: bool) -> int:
    """Apply mark/unmark to one topic. Unknown ids get close matches, exit 1."""
    topics = discover_topics()
    if not topics:
        print("No topics found under the module folders - are you running this")
        print("from the VibeLearning repository root?")
        return 1
    topic = resolve_topic(user_input, topics)
    if topic is None:
        print(f"I could not find a topic called '{user_input.strip()}'.")
        suggestions = suggest_topics(user_input, topics)
        if suggestions:
            print("\nDid you mean one of these?")
            for suggestion in suggestions:
                print(f"  - {suggestion}")
        else:
            print("\nNothing with a similar name came up.")
        print("\nRun 'python tools/progress_tracker.py list' to see every topic id.")
        return 1

    state = load_state()
    completed = state["completed"]
    verb = "marked done" if mark else "unmarked"
    if mark:
        if topic in completed:
            print(f"Already {verb}: {topic} - nothing to do.")
            return 0
        completed[topic] = datetime.now().isoformat(timespec="seconds")
    else:
        if topic not in completed:
            print(f"Not marked yet: {topic} - nothing to do.")
            return 0
        del completed[topic]
    try:
        save_state(state)
    except OSError as exc:
        print(f"Could not save progress to {STATE_FILE}: {exc}")
        return 1
    print(f"{verb.capitalize()}: {topic}")
    done = sum(1 for t in topics if t in completed)
    percent = int(round(done * 100 / len(topics))) if topics else 0
    print(f"Progress: {done}/{len(topics)} topics ({percent}%). Keep going!")
    return 0


def cmd_reset(args: argparse.Namespace) -> int:
    if not args.yes:
        print("This deletes ALL saved progress.")
        print("If you are sure, re-run with the confirm flag:")
        print("  python tools/progress_tracker.py reset --yes")
        return 1
    if not STATE_FILE.is_file():
        print("No saved progress found - nothing to reset.")
        return 0
    try:
        STATE_FILE.unlink()
    except OSError as exc:
        print(f"Could not delete {STATE_FILE}: {exc}")
        return 1
    print(f"Progress cleared ({STATE_FILE} deleted). Fresh start - enjoy!")
    return 0


# =============================================================================
# ENTRY POINT
# =============================================================================

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="progress_tracker.py",
        description="Track completed VibeLearning topics (saved in ~/.vibelearning).",
    )
    sub = parser.add_subparsers(dest="command", metavar="command")
    sub.add_parser("status", help="show done/total, percent, and the next suggested topics")
    sub.add_parser("list", help="list every topic with [x]/[ ] marks")
    p_mark = sub.add_parser("mark", help="mark a topic as completed")
    p_mark.add_argument("topic", help="topic id, e.g. 01_foundations/02_operators")
    p_unmark = sub.add_parser("unmark", help="remove the completed mark from a topic")
    p_unmark.add_argument("topic", help="topic id, e.g. 01_foundations/02_operators")
    p_reset = sub.add_parser("reset", help="delete all saved progress")
    p_reset.add_argument("--yes", action="store_true",
                         help="confirm the delete (required, no prompt)")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    # Never let a console codepage crash the reporter itself.
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass

    if args.command is None or args.command == "status":
        return cmd_status(args)
    if args.command == "list":
        return cmd_list(args)
    if args.command == "mark":
        return cmd_mark(args)
    if args.command == "unmark":
        return cmd_unmark(args)
    if args.command == "reset":
        return cmd_reset(args)
    print(f"Unknown command: {args.command}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
