"""Reading Tracebacks - Examples

Demonstrations:
- different exception types
- interpreting traceback information
- exception chaining

Run:
    python examples.py
"""

from __future__ import annotations

import traceback
import sys
from typing import Any, Dict, List


def demo_basic_traceback() -> None:
    """Show a basic traceback structure."""
    print("=== Basic Traceback Structure ===\n")

    print("A traceback like this:")
    print("""
Traceback (most recent call last):
  File "script.py", line 10, in main
    result = process(data)
  File "script.py", line 5, in process
    return data['key']
KeyError: 'key'
""")

    print("Read from BOTTOM to TOP:")
    print("  1. KeyError: 'key'         <- The exception (what happened)")
    print("  2. Line 5 in process()     <- Where it happened")
    print("  3. Line 10 in main()       <- How we got there")
    print()


def demo_keyerror() -> None:
    """Demonstrate KeyError traceback."""
    print("=== KeyError Example ===\n")

    def get_user_email(users: Dict[str, Dict], name: str) -> str:
        return users[name]["email"]

    try:
        users = {"alice": {"email": "alice@example.com"}}
        email = get_user_email(users, "bob")
    except KeyError:
        print("Caught KeyError. Traceback:")
        traceback.print_exc()
        print()
        print("Meaning: Key 'bob' doesn't exist in the users dict")
    print()


def demo_indexerror() -> None:
    """Demonstrate IndexError traceback."""
    print("=== IndexError Example ===\n")

    def get_third_item(items: List[Any]) -> Any:
        return items[2]

    try:
        result = get_third_item([1, 2])
    except IndexError:
        print("Caught IndexError. Traceback:")
        traceback.print_exc()
        print()
        print("Meaning: Tried to access index 2, but list only has 2 items (0, 1)")
    print()


def demo_typeerror() -> None:
    """Demonstrate TypeError traceback."""
    print("=== TypeError Example ===\n")

    def add_numbers(a: int, b: int) -> int:
        return a + b

    try:
        result = add_numbers("hello", 5)
    except TypeError:
        print("Caught TypeError. Traceback:")
        traceback.print_exc()
        print()
        print("Meaning: Can't concatenate str and int with +")
    print()


def demo_attributeerror() -> None:
    """Demonstrate AttributeError traceback."""
    print("=== AttributeError Example ===\n")

    def process_data(data: Any) -> int:
        return data.count()  # Assumes data has a count method

    try:
        result = process_data(None)
    except AttributeError:
        print("Caught AttributeError. Traceback:")
        traceback.print_exc()
        print()
        print("Meaning: None doesn't have a 'count' method")
    print()


def demo_valueerror() -> None:
    """Demonstrate ValueError traceback."""
    print("=== ValueError Example ===\n")

    def parse_int(s: str) -> int:
        return int(s)

    try:
        result = parse_int("not a number")
    except ValueError:
        print("Caught ValueError. Traceback:")
        traceback.print_exc()
        print()
        print("Meaning: String 'not a number' can't be converted to int")
    print()


def demo_nested_traceback() -> None:
    """Demonstrate a deeper call stack in traceback."""
    print("=== Nested Traceback Example ===\n")

    def level_1(data: Dict) -> str:
        return level_2(data)

    def level_2(data: Dict) -> str:
        return level_3(data)

    def level_3(data: Dict) -> str:
        return data["missing_key"]

    try:
        result = level_1({})
    except KeyError:
        print("Caught KeyError with deep stack. Traceback:")
        traceback.print_exc()
        print()
        print("The traceback shows the full call chain:")
        print("  level_1 -> level_2 -> level_3 -> error")
    print()


def demo_chained_exception() -> None:
    """Demonstrate exception chaining."""
    print("=== Chained Exception Example ===\n")

    class ConfigError(Exception):
        pass

    def load_config(path: str) -> Dict:
        try:
            with open(path) as f:
                import json

                return json.load(f)
        except FileNotFoundError as e:
            raise ConfigError(f"Config file not found: {path}") from e

    try:
        config = load_config("nonexistent.json")
    except ConfigError:
        print("Caught ConfigError. Traceback:")
        traceback.print_exc()
        print()
        print("Notice: Shows BOTH the original FileNotFoundError")
        print("        AND the ConfigError that was raised from it")
    print()


def demo_syntax_error() -> None:
    """Show what SyntaxError looks like."""
    print("=== SyntaxError Example ===\n")

    print("SyntaxErrors look different:")
    print("""
  File "script.py", line 5
    if x == 1
           ^
SyntaxError: expected ':'
""")

    print("The ^ points to where Python got confused.")
    print("The actual mistake (missing colon) is at the end of the line.")
    print()


def demo_traceback_module() -> None:
    """Show using the traceback module."""
    print("=== Using traceback Module ===\n")

    def faulty_function() -> None:
        x = 1 / 0

    try:
        faulty_function()
    except ZeroDivisionError:
        print("1. Get traceback as string:")
        tb_string = traceback.format_exc()
        print(f"   Length: {len(tb_string)} characters")

        print("\n2. Get just the exception info:")
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(f"   Type: {exc_type.__name__}")
        print(f"   Value: {exc_value}")

        print("\n3. Extract stack frames:")
        frames = traceback.extract_tb(exc_tb)
        for frame in frames:
            print(f"   {frame.filename}:{frame.lineno} in {frame.name}")
    print()


def demo_common_mistakes() -> None:
    """Show tracebacks from common mistakes."""
    print("=== Common Mistake Tracebacks ===\n")

    examples = [
        ("NameError", "prnt('hello')", "Typo in function name"),
        ("TypeError", "len(42)", "Wrong argument type"),
        ("ZeroDivisionError", "1/0", "Division by zero"),
    ]

    for exc_name, code, explanation in examples:
        print(f"{exc_name}: {explanation}")
        print(f"  Code: {code}")
        try:
            eval(code)
        except Exception:
            # Just show the exception line
            tb = traceback.format_exc().strip().split("\n")[-1]
            print(f"  Error: {tb}")
        print()


def demo_interpreting_traceback() -> None:
    """Show how to interpret a traceback systematically."""
    print("=== Interpreting Tracebacks Systematically ===\n")

    print("Step-by-step approach:")
    print("""
1. START at the BOTTOM
   - Read the exception type and message
   - Example: "KeyError: 'username'"
   - Question: What does this exception mean?

2. FIND your code
   - Look for files you recognize (not library code)
   - Example: File "myapp/views.py", line 42
   - Question: What's on that line?

3. TRACE the path
   - How did execution get to this point?
   - Follow the frames from top to bottom
   - Question: Is the error where it happened, or was
     bad data passed from earlier?

4. IDENTIFY the fix
   - Is the data wrong? Fix where it's created.
   - Is the code wrong? Fix the logic.
   - Is input validation missing? Add it.
""")


if __name__ == "__main__":
    demo_basic_traceback()
    demo_keyerror()
    demo_indexerror()
    demo_typeerror()
    demo_attributeerror()
    demo_valueerror()
    demo_nested_traceback()
    demo_chained_exception()
    demo_syntax_error()
    demo_traceback_module()
    demo_common_mistakes()
    demo_interpreting_traceback()
