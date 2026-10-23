"""
Pattern Matching - Examples
===========================
Structural pattern matching (match/case) needs Python 3.10+, and older
Pythons cannot even PARSE the syntax. This file therefore contains no
match/case code itself:

- On Python 3.10+ it imports match_demo (where the real demos live)
  and calls match_demo.run().
- On older Pythons it prints a friendly notice and exits cleanly, so
  the file still runs end to end everywhere the repo is supported.
"""

import sys

print("=" * 50)
print("PATTERN MATCHING - Examples")
print("=" * 50)

if sys.version_info >= (3, 10):
    import match_demo

    match_demo.run()
else:
    major, minor = sys.version_info[:2]
    print(f"\nThis demo needs Python 3.10+. You have {major}.{minor}.")
    print()
    print("match/case syntax cannot be parsed by older Pythons, so the")
    print("demonstrations live in match_demo.py and are only imported")
    print("here on Python 3.10+. You can still:")
    print("  - read README.md (its examples are for reading, not running)")
    print("  - run exercises.py (its if/elif starters work on 3.8+)")
    print("  - open match_solutions.py to READ the match/case answers")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
