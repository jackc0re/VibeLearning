"""
Pattern Matching - Exercises
============================
Each exercise below gives you a WORKING if/elif version - the style you
already know from 03_control_flow. Your job is to rewrite it with
match/case (Python 3.10+) and keep every check printing PASS.

Run this file as-is first: all checks pass, because the if/elif starters
work on any Python. Then rewrite one function at a time, re-run, and
confirm the checks still pass. The match/case answers live in
match_solutions.py.
"""

import sys

print("=" * 50)
print("PATTERN MATCHING - Exercises")
print("=" * 50)


# =============================================================================
# TEST HELPER
# =============================================================================
def check(label, got, expected):
    """Print PASS or FAIL for one expected result. Returns True on PASS."""
    if got == expected:
        print(f"PASS {label}")
        return True
    print(f"FAIL {label}: got {got!r}, expected {expected!r}")
    return False


# =============================================================================
# EXERCISE 1: Yes/No Replies (literal + or-patterns)
# =============================================================================
print("\n--- Exercise 1: Yes/No Replies ---\n")
"""
Rewrite decide() with match/case:
- one case matching "y" or "yes" (any case)  -> return True
  (use an or-pattern: case "y" | "yes":)
- one case matching "n" or "no" (any case)   -> return False
- case _:                                    -> return None
"""

def decide(reply):
    """Return True/False for a yes/no reply, None for anything else."""
    reply = reply.lower()
    if reply == "y" or reply == "yes":
        return True
    elif reply == "n" or reply == "no":
        return False
    else:
        return None

# TODO: rewrite decide() above using match/case, then re-run this file.
# The checks below must still print PASS.
print("Checks for Exercise 1:")
for reply, expected in [("yes", True), ("NO", False), ("y", True), ("maybe", None)]:
    check(f"decide({reply!r})", decide(reply), expected)


# =============================================================================
# EXERCISE 2: Number Classifier (capture pattern + guards)
# =============================================================================
print("\n--- Exercise 2: Number Classifier ---\n")
"""
Rewrite classify() with match/case:
- case 0:                        -> "zero"
- case n if n > 0 and n < 100:   -> "small positive"
- case n if n >= 100:            -> "big positive"
- case _:                        -> "negative"

A guard (the if part) is checked only after its pattern matches.
"""

def classify(n):
    """Sort a number into zero / small / big positive / negative."""
    if n == 0:
        return "zero"
    elif n > 0 and n < 100:
        return "small positive"
    elif n >= 100:
        return "big positive"
    else:
        return "negative"

# TODO: rewrite classify() above using match/case, then re-run this file.
print("Checks for Exercise 2:")
for value, expected in [(0, "zero"), (7, "small positive"),
                        (250, "big positive"), (-3, "negative")]:
    check(f"classify({value})", classify(value), expected)


# =============================================================================
# EXERCISE 3: Where Is the Point? (sequence patterns)
# =============================================================================
print("\n--- Exercise 3: Where Is the Point? ---\n")
"""
Rewrite describe_point() with match/case on the [x, y] list:
- case [0, 0]:  -> "the origin"
- case [0, y]:  -> f"on the y-axis (y={y})"
- case [x, 0]:  -> f"on the x-axis (x={x})"
- case [x, y]:  -> f"at ({x}, {y})"

Order matters! [0, 0] must come first, or [x, 0] would swallow it.
"""

def describe_point(point):
    """Describe where a [x, y] point sits."""
    x, y = point
    if x == 0 and y == 0:
        return "the origin"
    elif x == 0:
        return f"on the y-axis (y={y})"
    elif y == 0:
        return f"on the x-axis (x={x})"
    else:
        return f"at ({x}, {y})"

# TODO: rewrite describe_point() above using match/case, then re-run.
print("Checks for Exercise 3:")
for point, expected in [([0, 0], "the origin"),
                        ([0, 4], "on the y-axis (y=4)"),
                        ([3, 0], "on the x-axis (x=3)"),
                        ([2, 5], "at (2, 5)")]:
    check(f"describe_point({point})", describe_point(point), expected)


# =============================================================================
# EXERCISE 4: Command Router (sequence patterns with *rest)
# =============================================================================
print("\n--- Exercise 4: Command Router ---\n")
"""
Rewrite run_command() with match/case on the parts list:
- case []:                 -> "Type a command."
- case ["help"]:           -> "Showing help."
- case ["go", direction]:  -> f"Walking {direction}."
- case ["say", *words]:    -> "You said: " + " ".join(words)
- case _:                  -> "Unknown command."

*words gathers every item after "say", no matter how many.
"""

def run_command(parts):
    """Turn a command like ['say', 'hi', 'there'] into a message."""
    if len(parts) == 0:
        return "Type a command."
    head = parts[0]
    if head == "help" and len(parts) == 1:
        return "Showing help."
    elif head == "go" and len(parts) == 2:
        return f"Walking {parts[1]}."
    elif head == "say" and len(parts) >= 1:
        return "You said: " + " ".join(parts[1:])
    else:
        return "Unknown command."

# TODO: rewrite run_command() above using match/case, then re-run.
print("Checks for Exercise 4:")
for parts, expected in [(["help"], "Showing help."),
                        (["go", "north"], "Walking north."),
                        (["say", "hi", "there"], "You said: hi there"),
                        ([], "Type a command."),
                        (["dance"], "Unknown command.")]:
    check(f"run_command({parts})", run_command(parts), expected)


# =============================================================================
# EXERCISE 5: Event Handler (mapping patterns)
# =============================================================================
print("\n--- Exercise 5: Event Handler ---\n")
"""
Rewrite handle_event() with match/case on the event dict:
- case {"type": "quit"}:                  -> "Bye!"
- case {"type": "click", "x": x, "y": y}: -> f"Click at ({x}, {y})"
- case {"type": "key", "key": key}:       -> f"Key: {key}"
- case {"type": other}:                   -> f"Event: {other}"
- case _:                                 -> "Event: None"

Mapping patterns only check the keys you list: a click event that also
carries a "button" key still matches.
"""

def handle_event(event):
    """Turn an event dict into a short message."""
    kind = event.get("type")
    if kind == "quit":
        return "Bye!"
    elif kind == "click" and "x" in event and "y" in event:
        return f"Click at ({event['x']}, {event['y']})"
    elif kind == "key" and "key" in event:
        return f"Key: {event['key']}"
    else:
        return f"Event: {kind}"

# TODO: rewrite handle_event() above using match/case, then re-run.
print("Checks for Exercise 5:")
for event, expected in [
        ({"type": "quit"}, "Bye!"),
        ({"type": "click", "x": 3, "y": 9}, "Click at (3, 9)"),
        ({"type": "click", "x": 1, "y": 2, "button": "left"}, "Click at (1, 2)"),
        ({"type": "key", "key": "a"}, "Key: a"),
        ({"type": "scroll", "amount": 2}, "Event: scroll")]:
    check(f"handle_event({event})", handle_event(event), expected)


# =============================================================================
# SOLUTIONS
# =============================================================================
# The worked match/case solutions for these five exercises live in
# match_solutions.py - a separate file, because match/case syntax would
# stop THIS file from parsing on Python 3.8/3.9 (approved deviation from
# the bottom-of-file solutions convention).

print("\n--- Solutions ---")
print("The match/case rewrites of these exercises are in match_solutions.py.")


# =============================================================================
# VERSION GATE: run the match/case solutions on Python 3.10+
# =============================================================================
if sys.version_info >= (3, 10):
    print("\n--- Running match_solutions checks ---")
    import match_solutions

    match_solutions.run_checks()
else:
    major, minor = sys.version_info[:2]
    print(f"\nPython {major}.{minor} detected; match/case needs 3.10+.")
    print("Open match_solutions.py to READ the match/case answers")
    print("(run that file only on Python 3.10+).")

print("\n" + "=" * 50)
print("Great job! Check yourself with quiz.md next.")
print("=" * 50)
