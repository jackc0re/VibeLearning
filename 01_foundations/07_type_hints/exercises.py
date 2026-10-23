"""
Type Hints - Exercises
======================
Practice annotating variables and functions with type hints!

Every exercise has a self-test that prints PASS or FAIL.
With the stubs untouched, most tests FAIL - that is normal.
Work through the tasks, then compare with the SOLUTIONS at the bottom.
"""

from __future__ import annotations

import builtins
import sys
import typing
from typing import Callable, Dict, List, Optional, Tuple, TypeVar

T = TypeVar("T")

print("=" * 50)
print("TYPE HINTS - Exercises")
print("=" * 50)

# =============================================================================
# TEST HELPERS (used by the self-tests; no need to change these)
# =============================================================================

test_results = []


def check(label, condition):
    """Record and print one PASS/FAIL line."""
    if condition:
        print("PASS:", label)
        test_results.append(True)
    else:
        print("FAIL:", label)
        test_results.append(False)


def _norm(hint):
    """Comparable text form of an annotation.

    Understands resolved objects (int, List[int]) and the raw text that
    'from __future__ import annotations' stores ('int', 'List[int]'),
    and accepts both modern (list[int]) and typing (List[int]) spellings.
    """
    text = str(hint)
    if text.startswith("<class '") and text.endswith("'>"):
        text = text[8:-2]
    text = text.replace("typing.", "").replace(" ", "").replace("~", "")
    if text == "none":
        text = "nonetype"
    return text.lower()


def _same_hint(actual, expected):
    """True when an annotation matches the expected one."""
    if actual is None:
        return False
    if actual == expected:
        return True
    return _norm(actual) == _norm(expected)


def _hints(func):
    """Best-effort get_type_hints; falls back to raw annotation text."""
    try:
        return typing.get_type_hints(func)
    except Exception:
        return dict(getattr(func, "__annotations__", {}))


def _module_hints():
    """Resolved module-level annotations (used by Exercise 1)."""
    try:
        return typing.get_type_hints(sys.modules[__name__])
    except Exception:
        resolved = {}
        for name, hint in dict(globals().get("__annotations__", {})).items():
            if isinstance(hint, str):
                resolved[name] = getattr(builtins, hint, hint)
            else:
                resolved[name] = hint
        return resolved


# =============================================================================
# EXERCISE 1: Annotate Variables
# =============================================================================
print("\n--- Exercise 1: Annotate Variables ---\n")
"""
Give each variable below the hint matching what it holds:

    app_name       text
    max_tries      a whole number
    success_rate   a decimal
    debug_mode     True or False

Format:  name: type = value
"""

app_name = "QuizApp"
max_tries = 3
success_rate = 0.87
debug_mode = False


def test_exercise_1():
    hints = _module_hints()
    check("Ex1: app_name is hinted str", _same_hint(hints.get("app_name"), str))
    check("Ex1: max_tries is hinted int", _same_hint(hints.get("max_tries"), int))
    check("Ex1: success_rate is hinted float", _same_hint(hints.get("success_rate"), float))
    check("Ex1: debug_mode is hinted bool", _same_hint(hints.get("debug_mode"), bool))


# =============================================================================
# EXERCISE 2: Annotate Two Given Functions
# =============================================================================
print("\n--- Exercise 2: Annotate Two Functions ---\n")
"""
Annotate every parameter and every return of these two functions:

    send_report     prints one line and returns NOTHING
                    -> the return hint is None

    build_greeting  builds and returns text
                    name is text, excited is True/False

Remember the shape:  def f(param: type) -> type:
"""


def send_report(title, copies):
    print(f"REPORT {title} x{copies} sent.")


def build_greeting(name, excited):
    greeting = "Hi, " + name
    if excited:
        greeting = greeting + "!!!"
    return greeting


def test_exercise_2():
    report_hints = _hints(send_report)
    check("Ex2: send_report title is str", _same_hint(report_hints.get("title"), str))
    check("Ex2: send_report copies is int", _same_hint(report_hints.get("copies"), int))
    check("Ex2: send_report returns None", _same_hint(report_hints.get("return"), type(None)))
    greeting_hints = _hints(build_greeting)
    check("Ex2: build_greeting name is str", _same_hint(greeting_hints.get("name"), str))
    check("Ex2: build_greeting excited is bool", _same_hint(greeting_hints.get("excited"), bool))
    check("Ex2: build_greeting returns str", _same_hint(greeting_hints.get("return"), str))


# =============================================================================
# EXERCISE 3: Fix a Wrong Optional
# =============================================================================
print("\n--- Exercise 3: Fix a Wrong Optional ---\n")
"""
find_score returns the score for a name, or None when the name is missing.

Its return hint currently claims plain int - that is a LIE, because the
function can return None.

Task: annotate the parameters and FIX the return hint so it honestly says
"an int, or None". You need typing.Optional (already imported above).
"""


def find_score(scores, name):
    if name in scores:
        return scores[name]
    return None


def test_exercise_3():
    hints = _hints(find_score)
    check("Ex3: scores is Dict[str, int]", _same_hint(hints.get("scores"), Dict[str, int]))
    check("Ex3: name is str", _same_hint(hints.get("name"), str))
    check("Ex3: return is Optional[int] (int or None)",
          _same_hint(hints.get("return"), Optional[int]))


# =============================================================================
# EXERCISE 4: Annotate Collections
# =============================================================================
print("\n--- Exercise 4: Annotate Collections ---\n")
"""
Annotate these three functions:

    average(scores)     takes a list of ints, returns a float
    word_lengths(words) takes a list of strings, returns a dict mapping
                        each word to its length (str keys, int values)
    best_player(scores) takes a dict of str -> int, returns a fixed
                        (name, score) pair - a Tuple[str, int]

Use typing.List, typing.Dict and typing.Tuple (imported above).
"""


def average(scores):
    return sum(scores) / len(scores)


def word_lengths(words):
    counts = {}
    for word in words:
        counts[word] = len(word)
    return counts


def best_player(scores):
    best_name = None
    best_score = -1
    for name, score in scores.items():
        if score > best_score:
            best_name = name
            best_score = score
    return best_name, best_score


def test_exercise_4():
    average_hints = _hints(average)
    check("Ex4: average takes List[int]", _same_hint(average_hints.get("scores"), List[int]))
    check("Ex4: average returns float", _same_hint(average_hints.get("return"), float))

    words_hints = _hints(word_lengths)
    check("Ex4: word_lengths takes List[str]", _same_hint(words_hints.get("words"), List[str]))
    check("Ex4: word_lengths returns Dict[str, int]",
          _same_hint(words_hints.get("return"), Dict[str, int]))

    best_hints = _hints(best_player)
    check("Ex4: best_player takes Dict[str, int]",
          _same_hint(best_hints.get("scores"), Dict[str, int]))
    check("Ex4: best_player returns Tuple[str, int]",
          _same_hint(best_hints.get("return"), Tuple[str, int]))


# =============================================================================
# EXERCISE 5: Write a Generic Function
# =============================================================================
print("\n--- Exercise 5: Write a Generic Function ---\n")
"""
Write last_item so it returns the final element of ANY list:

    signature:  def last_item(items: List[T]) -> T
    body:       return items[-1]

T is the TypeVar created at the top of this file - use it, do not
invent a new one. The T in List[T] and the T after the arrow are the
SAME T: whatever fills the list comes back out.
"""


def last_item(items):
    # TODO: annotate with List[T] and T, then return items[-1]
    pass


def test_exercise_5():
    hints = _hints(last_item)
    check("Ex5: items is hinted List[T]", _same_hint(hints.get("items"), List[T]))
    check("Ex5: return is hinted T", _same_hint(hints.get("return"), T))
    try:
        works_for_ints = last_item([10, 20, 30]) == 30
    except Exception:
        works_for_ints = False
    check("Ex5: last_item([10, 20, 30]) returns 30", works_for_ints)
    try:
        works_for_strings = last_item(["x", "y", "z"]) == "z"
    except Exception:
        works_for_strings = False
    check("Ex5: last_item(['x', 'y', 'z']) returns 'z'", works_for_strings)


# =============================================================================
# EXERCISE 6: Annotate a Callback-Taking Function
# =============================================================================
print("\n--- Exercise 6: Annotate a Callback ---\n")
"""
transform_all applies fn to every value and collects the results:

    values  a list of ints
    fn      a function that takes ONE int and returns ONE int
            -> hint it as Callable[[int], int]
    return  a list of ints

Reading guide: Callable[[int], int] = "int in, int out".
"""


def transform_all(values, fn):
    result = []
    for value in values:
        result.append(fn(value))
    return result


def test_exercise_6():
    hints = _hints(transform_all)
    check("Ex6: values is hinted List[int]", _same_hint(hints.get("values"), List[int]))
    check("Ex6: fn is hinted Callable[[int], int]",
          _same_hint(hints.get("fn"), Callable[[int], int]))
    check("Ex6: return is hinted List[int]", _same_hint(hints.get("return"), List[int]))
    try:
        doubled_ok = transform_all([1, 2, 3], lambda n: n * 2) == [2, 4, 6]
    except Exception:
        doubled_ok = False
    check("Ex6: transform_all still works at runtime", doubled_ok)


# =============================================================================
# SELF-TESTS (WITH THE STUBS AS THEY ARE)
# =============================================================================
print("\n" + "=" * 50)
print("SELF-TESTS - running with the stubs as they are")
print("(failures are expected until you do the exercises)")
print("=" * 50)

test_exercise_1()
test_exercise_2()
test_exercise_3()
test_exercise_4()
test_exercise_5()
test_exercise_6()

print(f"\nStub score: {sum(test_results)}/{len(test_results)} checks passing")

# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 1
print("\n--- Solution 1 ---")
app_name: str = "QuizApp"
max_tries: int = 3
success_rate: float = 0.87
debug_mode: bool = False
print("All four variables now carry honest labels.")

# SOLUTION 2
print("\n--- Solution 2 ---")


def send_report(title: str, copies: int) -> None:
    print(f"REPORT {title} x{copies} sent.")


def build_greeting(name: str, excited: bool) -> str:
    greeting = "Hi, " + name
    if excited:
        greeting = greeting + "!!!"
    return greeting


send_report("Weekly quiz", 3)
print(build_greeting("Sam", True))
print("send_report returns nothing -> None; build_greeting returns text -> str.")

# SOLUTION 3
print("\n--- Solution 3 ---")


def find_score(scores: Dict[str, int], name: str) -> Optional[int]:
    if name in scores:
        return scores[name]
    return None


scores_table = {"Ann": 90, "Ben": 75}
print("Ann ->", find_score(scores_table, "Ann"))
print("Zed ->", find_score(scores_table, "Zed"), "(None is now part of the promise)")

# SOLUTION 4
print("\n--- Solution 4 ---")


def average(scores: List[int]) -> float:
    return sum(scores) / len(scores)


def word_lengths(words: List[str]) -> Dict[str, int]:
    counts = {}
    for word in words:
        counts[word] = len(word)
    return counts


def best_player(scores: Dict[str, int]) -> Tuple[str, int]:
    best_name = None
    best_score = -1
    for name, score in scores.items():
        if score > best_score:
            best_name = name
            best_score = score
    return best_name, best_score


print("average([90, 70, 85]) =", average([90, 70, 85]))
print("word_lengths(['bee', 'cat']) =", word_lengths(["bee", "cat"]))
print("best_player({'Ann': 90, 'Ben': 75}) =", best_player({"Ann": 90, "Ben": 75}))

# SOLUTION 5
print("\n--- Solution 5 ---")


def last_item(items: List[T]) -> T:
    return items[-1]


print("last_item([10, 20, 30]) =", last_item([10, 20, 30]))
print("last_item(['x', 'y', 'z']) =", last_item(["x", "y", "z"]))
print("One definition; T adapts to whatever the list holds.")

# SOLUTION 6
print("\n--- Solution 6 ---")


def transform_all(values: List[int], fn: Callable[[int], int]) -> List[int]:
    result = []
    for value in values:
        result.append(fn(value))
    return result


print("transform_all([1, 2, 3], lambda n: n * 2) =",
      transform_all([1, 2, 3], lambda n: n * 2))

print("\n" + "=" * 50)
print("SELF-TESTS AGAINST THE SOLUTIONS")
print("=" * 50)

test_results.clear()
test_exercise_1()
test_exercise_2()
test_exercise_3()
test_exercise_4()
test_exercise_5()
test_exercise_6()

print(f"\nSolution score: {sum(test_results)}/{len(test_results)} checks passing")

print("\n" + "=" * 50)
print(" Congratulations - you finished the type hints topic!")
print("Try the quiz next: quiz.md")
print("=" * 50)
