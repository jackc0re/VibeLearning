#!/usr/bin/env python3
"""
run_quiz.py - Take any topic's quiz.md interactively in the terminal
====================================================================

Every topic directory in this repository ships a quiz.md next to its README.
Those quizzes are written to be read on the site, but questions and answers
are regular markdown, so they can be played straight in the terminal. This
script discovers the quizzes, parses the house quiz format, asks the
multiple-choice questions one by one, and grades you as you go.

Usage:
    python tools/run_quiz.py --list                            # list every quiz
    python tools/run_quiz.py --list --module 02_data_structures
    python tools/run_quiz.py 01_foundations/04_loops           # play one quiz
    python tools/run_quiz.py -t 03_algorithms/02_sorting       # same, via flag
    python tools/run_quiz.py                                   # interactive menu
    python tools/run_quiz.py --module 09_testing               # menu, one module
    python tools/run_quiz.py --random                          # surprise quiz

Design notes:
  * Quizzes are discovered by globbing the numbered module directories for
    NN_topic/quiz.md - there is no hardcoded list to fall out of date.
  * The parser understands the house format: questions start at a
    "## Question N" heading (### variants too), options look like "A) text"
    or "- A) text", and the answer lives in a <details> block as bold text
    such as "**B)**". Quizzes that keep one shared answer key at the end
    (markdown tables, "## Answer N" sections, or numbered bold lists like
    "1. **B**") are supported as a fallback, keyed by question number.
  * Questions with no parseable A-D options (free-response prompts) are
    skipped and counted, never asked.
  * --list never prompts. Running with no arguments opens a small menu and
    waits on input(), so it is meant to be run by hand.
"""

from __future__ import annotations

import argparse
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --- parsing patterns (all file-sourced text is decoded utf-8) ---------------

# "## Question 1", "### Question 1: Time Complexity" - but not "## Questions".
# [ \t]* (not \s*) so the pattern can never spill onto the next line and
# mistake the question text for a subtitle.
QUESTION_RE = re.compile(
    r"(?m)^#{2,3}\s+Question\b[ \t]*(\d+)?[ \t]*[:\-\u2014]?[ \t]*(.*)$")

# "A) text", "a) text", "- B) text" - one answer option.
OPTION_RE = re.compile(r"^[ \t]*-?[ \t]*([A-Da-d])\)[ \t]*(.*)$")

# A whole <details>...</details> block.
DETAILS_RE = re.compile(r"(?ms)^<details>.*?^</details>")

# A section that holds answer keys: "# Answers", "## Answer Key", ...
ANSWERS_HEADING_RE = re.compile(r"(?m)^#{1,4}\s+Answers?\s*$")

# The answer letter in bold: "**B)**", "**B) some text**", "**B.**", "**B**".
BOLD_LETTER_RE = re.compile(r"\*\*\s*([A-Da-d])\s*(?:\)|\.|\*\*)")

# "| 12 | C | explanation |" rows of an answer-key table.
TABLE_ROW_RE = re.compile(r"(?m)^\|\s*(\d+)\s*\|\s*([A-Da-d])\s*\|")

# "**Question 4 - B) Matches anything but binds nothing**" (the class also
# accepts the em and en dash via \u2014/\u2013 escapes, keeping this file ASCII).
QUESTION_KEY_RE = re.compile(
    r"\*\*\s*Question\s+(\d+)\s*[\u2014\u2013-]\s*\**\s*([A-Da-d])\s*(?:\)|\.|\*\*)"
)

# "1. **C** - explanation" numbered bold lists.
NUMBERED_KEY_RE = re.compile(r"(?m)^\s*(\d+)\.\s+\*\*\s*([A-Da-d])\s*(?:\)|\.|\*\*)")


class Question:
    """One quiz question parsed out of a quiz.md file."""

    def __init__(self, number, subtitle, stem, options, answer):
        self.number = number
        self.subtitle = subtitle
        self.stem = stem
        self.options = options  # {"A": "...", "B": "..."} sorted by letter
        self.answer = answer    # "A".."D" or None when no key was found


# =============================================================================
# Discovery
# =============================================================================

def discover(module=None):
    """Return sorted 'module/topic' labels for every quiz in scope.

    Scans the numbered module directories for NN_topic/quiz.md. Returns None
    (after printing a friendly message) when `module` names no directory.
    """
    if module:
        base = ROOT / module
        if not base.is_dir():
            print(f"No module directory named '{module}' in this repository.")
            print("Run with --list and no --module to see what exists.")
            return None
        pattern = "[0-9][0-9]_*/quiz.md"
    else:
        base = ROOT
        pattern = "[0-9][0-9]_*/[0-9][0-9]_*/quiz.md"
    return sorted(p.relative_to(ROOT).parent.as_posix() for p in base.glob(pattern))


def resolve(label):
    """Turn user input like '01_foundations/04_loops' into a quiz.md path.

    Also accepts 'module/topic/quiz.md' or 'module/topic.md'. Returns None
    when nothing on disk matches.
    """
    cleaned = label.strip().strip("\"'").replace("\\", "/").strip("/")
    for suffix in ("/quiz.md", ".md", "/quiz"):
        if cleaned.endswith(suffix):
            cleaned = cleaned[: -len(suffix)]
            break
    parts = [part for part in cleaned.split("/") if part not in ("", ".")]
    if len(parts) != 2:
        return None
    path = ROOT / parts[0] / parts[1] / "quiz.md"
    return path if path.is_file() else None


# =============================================================================
# Parsing
# =============================================================================

def _is_aggregated_key(details_text):
    """True when a <details> block holds a shared answer key, not one answer.

    A per-question details block contains a single "**B)**" line, so any sign
    of several keyed entries means the whole file's key lives here.
    """
    if len(re.findall(r"(?m)^#{2,4}\s*Answer\s+\d+\b", details_text)) >= 2:
        return True
    if len(TABLE_ROW_RE.findall(details_text)) >= 2:
        return True
    if len(NUMBERED_KEY_RE.findall(details_text)) >= 2:
        return True
    if len(re.findall(r"\*\*\s*Question\s+\d+\b", details_text)) >= 2:
        return True
    return False


def _letter_from_details(details_text):
    """Extract the answer letter from one question's <details> block."""
    if _is_aggregated_key(details_text):
        return None
    match = BOLD_LETTER_RE.search(details_text)
    return match.group(1).upper() if match else None


def _build_answer_key(region):
    """Build {question number: letter} from a quiz's shared answer-key region.

    Tolerant of the house variants: markdown tables, "## Answer N" sections,
    "**Question N - X)**" lines, and numbered bold lists ("3. **C** ...").
    """
    key = {}

    def put(number, letter):
        key.setdefault(int(number), letter.upper())

    for match in TABLE_ROW_RE.finditer(region):
        put(match.group(1), match.group(2))
    for match in re.finditer(
        r"(?ms)^#{2,4}\s*Answer\s+(\d+)\s*$"
        r"(.*?)(?=^#{2,4}\s*Answer\s+\d+\s*$|^\s*-{3,}\s*$|\Z)",
        region,
    ):
        letter = BOLD_LETTER_RE.search(match.group(2))
        if letter:
            put(match.group(1), letter.group(1))
    for match in QUESTION_KEY_RE.finditer(region):
        put(match.group(1), match.group(2))
    for match in NUMBERED_KEY_RE.finditer(region):
        put(match.group(1), match.group(2))
    return key


def _answers_region_start(text, search_from):
    """Position where the shared answer-key region starts, or None.

    Found as the first "## Answers"-style heading or the first aggregated
    <details> block after the questions begin. Question bodies must not run
    past this point, or the last question would swallow the whole key.
    """
    candidates = []
    heading = ANSWERS_HEADING_RE.search(text, search_from)
    if heading:
        candidates.append(heading.start())
    for match in DETAILS_RE.finditer(text, search_from):
        if _is_aggregated_key(match.group(0)):
            candidates.append(match.start())
            break
    return min(candidates) if candidates else None


def _split_options(body):
    """Split a question body into (stem, options). Fence-aware so that
    "A)" lines inside ``` code blocks are never mistaken for options."""
    stem_lines = []
    options = {}
    in_fence = False
    started = False
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            if not started:
                stem_lines.append(line)
            continue
        if in_fence:
            if not started:
                stem_lines.append(line)
            continue
        match = OPTION_RE.match(line)
        if match:
            started = True
            letter = match.group(1).upper()
            if letter not in options:
                options[letter] = match.group(2).strip()
            continue
        if started:
            # A non-option line ends the options list (details block, rule).
            if stripped and not stripped.startswith("<details") and stripped != "---":
                break
        else:
            stem_lines.append(line)
    return "\n".join(stem_lines), options


def parse_quiz(text):
    """Parse quiz.md text into a list of Question objects."""
    headings = list(QUESTION_RE.finditer(text))
    if not headings:
        return []
    region_start = _answers_region_start(text, headings[0].start())
    key = _build_answer_key(text[region_start:]) if region_start is not None else {}

    questions = []
    for index, heading in enumerate(headings):
        body_start = heading.end()
        body_end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        if region_start is not None:
            body_end = min(body_end, region_start)
        body = text[body_start:body_end]

        number = int(heading.group(1)) if heading.group(1) else index + 1
        subtitle = (heading.group(2) or "").strip()
        stem, options = _split_options(body)

        answer = None
        for details in DETAILS_RE.finditer(body):
            answer = _letter_from_details(details.group(0))
            if answer:
                break
        if answer is None:
            answer = key.get(number)

        questions.append(Question(number, subtitle, stem, options, answer))
    return questions


# =============================================================================
# Playing
# =============================================================================

def _letter_range(options):
    """Human hint for the prompt, e.g. 'A-D'."""
    letters = sorted(options)
    return f"{letters[0]}-{letters[-1]}"


def run_quiz(path, label):
    """Play one quiz interactively. Returns a process exit code."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        print(f"Could not read {label}: {exc}")
        return 1

    questions = parse_quiz(text)
    askable = [q for q in questions if len(q.options) >= 2]
    free_response = [q for q in questions if len(q.options) < 2]
    gradable = [q for q in askable if q.answer in q.options]
    no_key = [q for q in askable if q.answer not in q.options]

    print("=" * 60)
    print(f"Quiz: {label}")
    print("=" * 60)
    if not gradable:
        print("\nNo gradeable multiple-choice questions found in this quiz.")
        if free_response:
            print(f"Skipped {len(free_response)} free-response question(s).")
        return 0

    print(f"\n{len(gradable)} multiple-choice questions. Answer with a letter.")
    print("Good luck!\n")

    score = 0
    answered = 0
    aborted = False
    for index, question in enumerate(gradable, 1):
        title = f"Question {index} of {len(gradable)}"
        if question.subtitle:
            title += f" - {question.subtitle}"
        print(title)
        print("-" * len(title))
        stem = question.stem.strip("\n").rstrip()
        if stem:
            print(stem)
        print()
        for letter in sorted(question.options):
            print(f"  {letter}) {question.options[letter]}")

        guess = None
        while guess is None:
            try:
                raw = input(f"Your answer ({_letter_range(question.options)}, "
                            "or Q to quit): ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                aborted = True
                break
            if not raw:
                continue
            if raw.upper() in ("Q", "QUIT", "EXIT"):
                aborted = True
                break
            candidate = raw.upper()[:1]
            if candidate in question.options:
                guess = candidate
            else:
                print(f"Please answer with one of "
                      f"{_letter_range(question.options)} (or Q to quit).")

        if aborted:
            break
        answered += 1
        if guess == question.answer:
            score += 1
            print("Correct!")
        else:
            correct = question.options[question.answer]
            print(f"Wrong - the correct answer is {question.answer}) {correct}")

    print("\n" + "=" * 60)
    if aborted and answered == 0:
        print("Stopped before answering any question - come back soon!")
    elif aborted:
        print(f"You scored {score}/{answered} before stopping - come back soon!")
    else:
        print(f"You scored {score}/{len(gradable)}.")
        if score == len(gradable):
            print("Perfect score - outstanding!")
        else:
            print("Missed some? Revisit the topic's README.md and examples.py, "
                  "then run this quiz again.")
    if free_response:
        print(f"Skipped {len(free_response)} free-response question(s).")
    if no_key:
        print(f"Skipped {len(no_key)} question(s) with no answer key found.")
    print("=" * 60)
    return 0


# =============================================================================
# Listing and the menu
# =============================================================================

def list_quizzes(module):
    """Print every quiz as 'module/topic', one per line, alphabetically."""
    labels = discover(module)
    if labels is None:
        return 1
    if not labels:
        where = f" under module '{module}'" if module else ""
        print(f"No quizzes found{where}.")
        return 1
    plural = "quiz" if len(labels) == 1 else "quizzes"
    scope = f" in module {module}" if module else ""
    print(f"{len(labels)} {plural} found{scope}:\n")
    for label in labels:
        print(label)
    return 0


def menu(module):
    """Interactive topic picker shown when the tool runs with no topic."""
    labels = discover(module)
    if labels is None:
        return 1
    if not labels:
        where = f" under module '{module}'" if module else ""
        print(f"No quizzes found{where}.")
        return 1
    scope = f" in module {module}" if module else ""
    print(f"VibeLearning quiz runner - {len(labels)} quizzes{scope} available.")
    print("Topics look like '01_foundations/04_loops'.\n")
    for label in labels[:12]:
        print(f"  {label}")
    if len(labels) > 12:
        print(f"  ... and {len(labels) - 12} more (--list shows every one)")

    modules = sorted({label.split("/")[0] for label in labels})
    while True:
        print()
        try:
            raw = input("Which topic? (module/topic, a module name, "
                        "Q to quit): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nNo problem - run the tool again any time.")
            return 0
        if not raw:
            continue
        if raw.upper() in ("Q", "QUIT", "EXIT"):
            print("Happy studying!")
            return 0
        if raw in modules:
            for label in labels:
                if label.split("/")[0] == raw:
                    print(f"  {label}")
            continue
        path = resolve(raw)
        if path is None:
            print(f"Couldn't find a quiz for '{raw}'. "
                  "Try --list to see every topic.")
            continue
        return run_quiz(path, path.relative_to(ROOT).parent.as_posix())


# =============================================================================
# Entry point
# =============================================================================

def _harden_streams():
    """Never crash reporting on a legacy Windows console codepage."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


def main():
    """Argument handling. Returns the process exit code."""
    parser = argparse.ArgumentParser(
        description="Take a topic quiz.md interactively in the terminal.")
    parser.add_argument(
        "topic", nargs="?",
        help="quiz to play, as module/topic (e.g. 01_foundations/04_loops)")
    parser.add_argument(
        "-t", "--topic", dest="topic_flag",
        help="same as the positional topic argument")
    parser.add_argument(
        "--list", action="store_true",
        help="print every quiz as module/topic and exit (never prompts)")
    parser.add_argument(
        "--module", metavar="DIR",
        help="restrict to one module directory, e.g. 02_data_structures")
    parser.add_argument(
        "--random", action="store_true",
        help="play one quiz picked at random")
    args = parser.parse_args()

    _harden_streams()

    if args.list:
        return list_quizzes(args.module)

    if args.random:
        labels = discover(args.module)
        if not labels:
            return 1 if labels is None else 0
        label = random.choice(labels)
        return run_quiz(ROOT / label / "quiz.md", label)

    chosen = args.topic or args.topic_flag
    if chosen:
        path = resolve(chosen)
        if path is None:
            print(f"Couldn't find a quiz for '{chosen}'.")
            print("Run 'python tools/run_quiz.py --list' to see every quiz.")
            return 1
        return run_quiz(path, path.relative_to(ROOT).parent.as_posix())

    return menu(args.module)


if __name__ == "__main__":
    sys.exit(main())
