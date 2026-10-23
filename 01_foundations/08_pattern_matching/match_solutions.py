"""
Pattern Matching - Solutions (Python 3.10+)
===========================================
match/case rewrites of the five exercises in exercises.py, plus
run_checks(), which re-runs every expected result against these match
versions and prints PASS/FAIL lines.

This file CANNOT be parsed by Python older than 3.10 - that is exactly
why the 3.8-parseable exercises.py only imports it after a version
check. On Python 3.10+ you can run it directly: python match_solutions.py
"""


# =============================================================================
# EXERCISE 1: Yes/No Replies (literal + or-patterns)
# =============================================================================
def decide(reply):
    """Return True/False for a yes/no reply, None for anything else."""
    match reply.lower():
        case "y" | "yes":
            return True
        case "n" | "no":
            return False
        case _:
            return None


# =============================================================================
# EXERCISE 2: Number Classifier (capture pattern + guards)
# =============================================================================
def classify(n):
    """Sort a number into zero / small / big positive / negative."""
    match n:
        case 0:
            return "zero"
        case n if n > 0 and n < 100:
            return "small positive"
        case n if n >= 100:
            return "big positive"
        case _:
            return "negative"


# =============================================================================
# EXERCISE 3: Where Is the Point? (sequence patterns)
# =============================================================================
def describe_point(point):
    """Describe where a [x, y] point sits."""
    match point:
        case [0, 0]:
            return "the origin"
        case [0, y]:
            return f"on the y-axis (y={y})"
        case [x, 0]:
            return f"on the x-axis (x={x})"
        case [x, y]:
            return f"at ({x}, {y})"


# =============================================================================
# EXERCISE 4: Command Router (sequence patterns with *rest)
# =============================================================================
def run_command(parts):
    """Turn a command like ['say', 'hi', 'there'] into a message."""
    match parts:
        case []:
            return "Type a command."
        case ["help"]:
            return "Showing help."
        case ["go", direction]:
            return f"Walking {direction}."
        case ["say", *words]:
            return "You said: " + " ".join(words)
        case _:
            return "Unknown command."


# =============================================================================
# EXERCISE 5: Event Handler (mapping patterns)
# =============================================================================
def handle_event(event):
    """Turn an event dict into a short message."""
    match event:
        case {"type": "quit"}:
            return "Bye!"
        case {"type": "click", "x": x, "y": y}:
            return f"Click at ({x}, {y})"
        case {"type": "key", "key": key}:
            return f"Key: {key}"
        case {"type": other}:
            return f"Event: {other}"
        case _:
            return "Event: None"


# =============================================================================
# CHECKS: same tables as exercises.py, run against the match versions
# =============================================================================
def check(label, got, expected):
    """Print PASS or FAIL for one expected result. Returns True on PASS."""
    if got == expected:
        print(f"PASS {label}")
        return True
    print(f"FAIL {label}: got {got!r}, expected {expected!r}")
    return False


def run_checks():
    """Run every exercise table against the match/case solutions.

    Returns True when every check passes.
    """
    print("\n" + "=" * 50)
    print("MATCH/CASE SOLUTION CHECKS")
    print("=" * 50)

    failures = 0

    print("\n--- Exercise 1: Yes/No Replies ---")
    for reply, expected in [("yes", True), ("NO", False),
                            ("y", True), ("maybe", None)]:
        if not check(f"decide({reply!r})", decide(reply), expected):
            failures += 1

    print("\n--- Exercise 2: Number Classifier ---")
    for value, expected in [(0, "zero"), (7, "small positive"),
                            (250, "big positive"), (-3, "negative")]:
        if not check(f"classify({value})", classify(value), expected):
            failures += 1

    print("\n--- Exercise 3: Where Is the Point? ---")
    for point, expected in [([0, 0], "the origin"),
                            ([0, 4], "on the y-axis (y=4)"),
                            ([3, 0], "on the x-axis (x=3)"),
                            ([2, 5], "at (2, 5)")]:
        if not check(f"describe_point({point})", describe_point(point), expected):
            failures += 1

    print("\n--- Exercise 4: Command Router ---")
    for parts, expected in [(["help"], "Showing help."),
                            (["go", "north"], "Walking north."),
                            (["say", "hi", "there"], "You said: hi there"),
                            ([], "Type a command."),
                            (["dance"], "Unknown command.")]:
        if not check(f"run_command({parts})", run_command(parts), expected):
            failures += 1

    print("\n--- Exercise 5: Event Handler ---")
    for event, expected in [
            ({"type": "quit"}, "Bye!"),
            ({"type": "click", "x": 3, "y": 9}, "Click at (3, 9)"),
            ({"type": "click", "x": 1, "y": 2, "button": "left"}, "Click at (1, 2)"),
            ({"type": "key", "key": "a"}, "Key: a"),
            ({"type": "scroll", "amount": 2}, "Event: scroll")]:
        if not check(f"handle_event({event})", handle_event(event), expected):
            failures += 1

    print("\n" + "=" * 50)
    if failures == 0:
        print("All match/case solutions behave like the if/elif starters.")
        print("=" * 50)
        return True
    print(f"{failures} check(s) FAILED - compare with exercises.py starters.")
    print("=" * 50)
    return False


if __name__ == "__main__":
    print("=" * 50)
    print("PATTERN MATCHING - Solutions (Python 3.10+)")
    print("=" * 50)
    run_checks()
