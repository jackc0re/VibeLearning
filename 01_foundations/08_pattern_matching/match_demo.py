"""
Pattern Matching - Demonstrations (Python 3.10+)
================================================
All match/case demonstrations for the pattern matching topic, wrapped in
one run() function so examples.py can import this module after it has
checked the Python version.

This file is written WITH match/case syntax, so Python older than 3.10
cannot even parse it. That is intentional: examples.py stays 3.8-parseable
and only imports this file on Python 3.10+.
"""


def run():
    """Print every demonstration. Called by examples.py on Python 3.10+."""

    # =========================================================================
    # LITERAL PATTERNS
    # =========================================================================
    print("\n--- Literal Patterns ---\n")

    # A literal pattern compares the subject with ==, just like
    # `if code == 404:`. The FIRST case whose pattern matches wins;
    # everything below it is skipped.
    for code in [200, 404, 418, 500]:
        match code:
            case 200:
                print(f"  HTTP {code}: OK")
            case 404:
                print(f"  HTTP {code}: Not Found")
            case 418:
                print(f"  HTTP {code}: I'm a teapot")
            case _:
                print(f"  HTTP {code}: something else")

    # Gotcha: a BARE NAME is a capture pattern, not a comparison!
    # `case limit:` would match ANY value and bind it to the name limit.
    # To compare against an existing variable, use a guard:
    limit = 100
    for value in [42, 100]:
        match value:
            case v if v == limit:
                print(f"  {value} equals the limit")
            case _:
                print(f"  {value} does not equal the limit ({limit})")

    # =========================================================================
    # CAPTURE PATTERNS
    # =========================================================================
    print("\n--- Capture Patterns ---\n")

    # A bare name in a pattern always MATCHES and binds the subject to it.
    # Read `case anything:` as "match anything, call it anything".
    for subject in [42, "hello", [1, 2, 3]]:
        match subject:
            case anything:
                print(f"  captured {anything!r} (type: {type(anything).__name__})")

    # =========================================================================
    # THE WILDCARD PATTERN _
    # =========================================================================
    print("\n--- The Wildcard Pattern (_) ---\n")

    # _ matches anything but binds nothing: the catch-all "else" of match.
    for command in ["GO", "STOP", "jump"]:
        match command:
            case "GO":
                print(f"  {command}: going!")
            case "STOP":
                print(f"  {command}: stopping!")
            case _:
                print(f"  {command}: unknown command (the wildcard caught it)")

    # =========================================================================
    # OR-PATTERNS
    # =========================================================================
    print("\n--- Or-Patterns ---\n")

    # The | operator lets ONE case accept several alternatives.
    for answer in ["y", "YES", "no", "maybe"]:
        match answer.lower():
            case "y" | "yes":
                print(f"  {answer!r}: agreed")
            case "n" | "no":
                print(f"  {answer!r}: declined")
            case _:
                print(f"  {answer!r}: unclear answer")

    # =========================================================================
    # GUARDS (case PATTERN if CONDITION)
    # =========================================================================
    print("\n--- Guards ---\n")

    # A guard is an extra condition attached to a case. The case matches
    # only when BOTH the pattern and the guard are true.
    # `case n if n > 0` means: "match anything, bind it to n,
    # but only take this case when n > 0".
    for n in [-5, 0, 7, 999]:
        match n:
            case 0:
                print(f"  {n}: exactly zero")
            case n if n > 0:
                print(f"  {n}: positive")
            case _:
                print(f"  {n}: negative")

    # =========================================================================
    # SEQUENCE PATTERNS (DESTRUCTURING)
    # =========================================================================
    print("\n--- Sequence Patterns (Destructuring) ---\n")

    # A sequence pattern tests the SHAPE of a list or tuple and unpacks it
    # in one step. `case [0, 0]` means "exactly two items, both zero".
    for point in [[0, 0], [3, 0], [0, 4], [2, 5], [1, 2, 3]]:
        match point:
            case [0, 0]:
                print(f"  {point}: the origin")
            case [x, 0]:
                print(f"  {point}: on the x-axis (x = {x})")
            case [0, y]:
                print(f"  {point}: on the y-axis (y = {y})")
            case [x, y]:
                print(f"  {point}: somewhere in the plane ({x}, {y})")
            case _:
                print(f"  {point}: not a 2D point")

    # *rest gathers "all the remaining items" - however many there are.
    print("\n--- Head With *rest ---")
    for hand in [[], [7], [7, 5], [7, 5, 3, 1]]:
        match hand:
            case []:
                print("  empty hand")
            case [first]:
                print(f"  one card: {first}")
            case [first, *rest]:
                print(f"  first = {first}, rest = {rest}")

    # =========================================================================
    # MAPPING PATTERNS (DICTIONARIES)
    # =========================================================================
    print("\n--- Mapping Patterns (Dictionaries) ---\n")

    # A mapping pattern checks only the keys you list; extra keys are fine.
    # **rest collects any remaining keys and values.
    events = [
        {"type": "click", "x": 10, "y": 20},
        {"type": "key", "key": "escape"},
        {"type": "scroll", "amount": 3, "source": "touchpad"},
        {"type": "quit"},
    ]

    for event in events:
        match event:
            case {"type": "click", "x": x, "y": y}:
                print(f"  click at ({x}, {y})")
            case {"type": "key", "key": key}:
                print(f"  key pressed: {key}")
            case {"type": "quit"}:
                print("  goodbye!")
            case {"type": other, **details}:
                print(f"  {other} event, extra details: {details}")

    # =========================================================================
    # CLASS PATTERNS (comment-only note)
    # =========================================================================
    # Class patterns match an object by its class and attribute values, e.g.
    #     case Point(x=0, y=0):   -> matches a Point instance at the origin
    # They need classes (and optionally __match_args__) to be useful, so
    # there is no demo here yet. Classes arrive in 04_oop_concepts; come
    # back to this idea once you have met them.


if __name__ == "__main__":
    print("=" * 50)
    print("PATTERN MATCHING - Examples (Python 3.10+)")
    print("=" * 50)
    run()
    print("\n" + "=" * 50)
    print("Examples complete! Try exercises.py next.")
    print("=" * 50)
