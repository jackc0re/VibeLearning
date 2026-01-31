"""Reading Tracebacks - Exercises

Goals:
- parse and analyze tracebacks
- identify exception types and locations
- suggest fixes based on traceback info

Run with:
    python exercises.py
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple


# =============================================================================
# EXERCISE 1: Parse Traceback Frame
# =============================================================================


def exercise_1_parse_frame(frame_text: str) -> Optional[Dict[str, Any]]:
    """
    Parse a single traceback frame line.

    Input format:
        '  File "path/to/file.py", line 42, in function_name'

    Returns dict with:
    - "file": the file path
    - "line": the line number (int)
    - "function": the function name

    Returns None if the line doesn't match the expected format.
    """
    # Pattern: File "path", line N, in name
    pattern = r'File "([^"]+)", line (\d+), in (.+)'
    match = re.search(pattern, frame_text)

    if match:
        return {
            "file": match.group(1),
            "line": int(match.group(2)),
            "function": match.group(3).strip(),
        }
    return None


# =============================================================================
# EXERCISE 2: Parse Full Traceback
# =============================================================================


def exercise_2_parse_traceback(traceback_text: str) -> Dict[str, Any]:
    """
    Parse a full traceback into structured data.

    Returns dict with:
    - "frames": list of frame dicts (from exercise_1_parse_frame)
    - "exception_type": the exception class name
    - "exception_message": the exception message
    - "bottom_frame": the last frame (where error occurred)
    """
    lines = traceback_text.strip().split("\n")

    frames = []
    exception_type = ""
    exception_message = ""

    for line in lines:
        # Try to parse as frame
        frame = exercise_1_parse_frame(line)
        if frame:
            frames.append(frame)

    # Last line should be exception
    if lines:
        last_line = lines[-1]
        if ":" in last_line:
            parts = last_line.split(":", 1)
            exception_type = parts[0].strip()
            exception_message = parts[1].strip() if len(parts) > 1 else ""
        else:
            exception_type = last_line.strip()

    bottom_frame = frames[-1] if frames else None

    return {
        "frames": frames,
        "exception_type": exception_type,
        "exception_message": exception_message,
        "bottom_frame": bottom_frame,
    }


# =============================================================================
# EXERCISE 3: Identify Exception Category
# =============================================================================


def exercise_3_categorize_exception(exception_type: str) -> str:
    """
    Categorize an exception type into a general category.

    Categories:
    - "lookup": KeyError, IndexError, AttributeError
    - "type": TypeError, ValueError
    - "io": FileNotFoundError, IOError, PermissionError
    - "syntax": SyntaxError, IndentationError
    - "name": NameError, ImportError, ModuleNotFoundError
    - "runtime": ZeroDivisionError, RecursionError, MemoryError
    - "other": anything else
    """
    categories = {
        "lookup": ["KeyError", "IndexError", "AttributeError"],
        "type": ["TypeError", "ValueError"],
        "io": ["FileNotFoundError", "IOError", "PermissionError", "OSError"],
        "syntax": ["SyntaxError", "IndentationError", "TabError"],
        "name": ["NameError", "ImportError", "ModuleNotFoundError", "UnboundLocalError"],
        "runtime": ["ZeroDivisionError", "RecursionError", "MemoryError", "OverflowError"],
    }

    for category, exceptions in categories.items():
        if exception_type in exceptions:
            return category
    return "other"


# =============================================================================
# EXERCISE 4: Suggest Fix
# =============================================================================


def exercise_4_suggest_fix(exception_type: str, message: str) -> List[str]:
    """
    Suggest possible fixes based on exception type and message.

    Returns a list of suggestion strings.
    """
    suggestions = []

    if exception_type == "KeyError":
        key = message.strip("'\"")
        suggestions.append(f"Check if key '{key}' exists before accessing")
        suggestions.append("Use .get() method with a default value")
        suggestions.append("Verify dictionary keys match expected values")

    elif exception_type == "IndexError":
        suggestions.append("Check list length before accessing index")
        suggestions.append("Verify loop bounds are correct")
        suggestions.append("Watch for off-by-one errors")

    elif exception_type == "TypeError":
        suggestions.append("Check the types of arguments being passed")
        suggestions.append("Ensure variables aren't None unexpectedly")
        suggestions.append("Verify function signatures match calls")

    elif exception_type == "AttributeError":
        if "None" in message or "NoneType" in message:
            suggestions.append("Check if variable is None before accessing attribute")
            suggestions.append("Add None check or use Optional typing")
        else:
            suggestions.append("Verify the object has the expected attribute")
            suggestions.append("Check for typos in attribute name")

    elif exception_type == "NameError":
        suggestions.append("Check for typos in variable/function name")
        suggestions.append("Ensure variable is defined before use")
        suggestions.append("Check if import is missing")

    elif exception_type == "FileNotFoundError":
        suggestions.append("Verify the file path is correct")
        suggestions.append("Check if file exists before opening")
        suggestions.append("Use absolute paths or verify working directory")

    elif exception_type == "ValueError":
        suggestions.append("Validate input data before processing")
        suggestions.append("Check format of string being converted")
        suggestions.append("Add try/except for conversion operations")

    elif exception_type == "ZeroDivisionError":
        suggestions.append("Check divisor is not zero before division")
        suggestions.append("Add guard clause for zero values")

    else:
        suggestions.append(f"Look up {exception_type} in Python docs")
        suggestions.append("Check the line indicated in traceback")

    return suggestions


# =============================================================================
# EXERCISE 5: Find User Code Frame
# =============================================================================


def exercise_5_find_user_frame(
    frames: List[Dict[str, Any]], user_paths: List[str]
) -> Optional[Dict[str, Any]]:
    """
    Find the last (deepest) frame that's in user code.

    User code is identified by file paths containing any of the user_paths.
    Library code (site-packages, stdlib) should be skipped.

    Returns the frame dict, or None if no user frames found.
    """
    user_frame = None

    for frame in frames:
        file_path = frame.get("file", "")
        # Check if this is user code
        is_user = any(path in file_path for path in user_paths)
        # Exclude common library paths
        is_library = any(
            lib in file_path
            for lib in ["site-packages", "lib/python", "lib\\python", "<frozen"]
        )

        if is_user and not is_library:
            user_frame = frame

    return user_frame


def exercise_5_format_fix_location(frame: Optional[Dict[str, Any]]) -> str:
    """
    Format a frame as a fix location string.

    Format: "file.py:line in function()"
    Returns "Unknown location" if frame is None.
    """
    if frame is None:
        return "Unknown location"

    filename = frame.get("file", "unknown")
    # Get just the filename, not full path
    if "/" in filename:
        filename = filename.split("/")[-1]
    if "\\" in filename:
        filename = filename.split("\\")[-1]

    line = frame.get("line", "?")
    func = frame.get("function", "?")

    return f"{filename}:{line} in {func}()"


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Reading Tracebacks Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1: Parse Traceback Frame
    print("\nExercise 1: Parse Traceback Frame")
    try:
        frame = exercise_1_parse_frame(
            '  File "myapp/views.py", line 42, in get_user'
        )
        ok1 = frame is not None
        ok2 = frame["file"] == "myapp/views.py"
        ok3 = frame["line"] == 42
        ok4 = frame["function"] == "get_user"
        ok5 = exercise_1_parse_frame("not a frame") is None

        ok = ok1 and ok2 and ok3 and ok4 and ok5
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2: Parse Full Traceback
    print("\nExercise 2: Parse Full Traceback")
    try:
        tb = """Traceback (most recent call last):
  File "main.py", line 10, in main
    result = process(data)
  File "utils.py", line 5, in process
    return data['key']
KeyError: 'key'"""

        parsed = exercise_2_parse_traceback(tb)
        ok1 = len(parsed["frames"]) == 2
        ok2 = parsed["exception_type"] == "KeyError"
        ok3 = parsed["exception_message"] == "'key'"
        ok4 = parsed["bottom_frame"]["file"] == "utils.py"

        ok = ok1 and ok2 and ok3 and ok4
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3: Identify Exception Category
    print("\nExercise 3: Identify Exception Category")
    try:
        ok1 = exercise_3_categorize_exception("KeyError") == "lookup"
        ok2 = exercise_3_categorize_exception("TypeError") == "type"
        ok3 = exercise_3_categorize_exception("FileNotFoundError") == "io"
        ok4 = exercise_3_categorize_exception("SyntaxError") == "syntax"
        ok5 = exercise_3_categorize_exception("NameError") == "name"
        ok6 = exercise_3_categorize_exception("CustomError") == "other"

        ok = ok1 and ok2 and ok3 and ok4 and ok5 and ok6
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 4: Suggest Fix
    print("\nExercise 4: Suggest Fix")
    try:
        key_suggestions = exercise_4_suggest_fix("KeyError", "'username'")
        ok1 = len(key_suggestions) > 0
        ok2 = any("get()" in s for s in key_suggestions)

        attr_suggestions = exercise_4_suggest_fix(
            "AttributeError", "'NoneType' object has no attribute 'foo'"
        )
        ok3 = any("None" in s for s in attr_suggestions)

        ok = ok1 and ok2 and ok3
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 5: Find User Code Frame
    print("\nExercise 5: Find User Code Frame")
    try:
        frames = [
            {"file": "/usr/lib/python3.9/json/__init__.py", "line": 10, "function": "loads"},
            {"file": "/home/user/myapp/utils.py", "line": 20, "function": "parse"},
            {"file": "/home/user/myapp/views.py", "line": 30, "function": "handle"},
        ]

        user_frame = exercise_5_find_user_frame(frames, ["/home/user/myapp"])
        ok1 = user_frame is not None
        ok2 = user_frame["file"] == "/home/user/myapp/views.py"  # Last user frame

        loc = exercise_5_format_fix_location(user_frame)
        ok3 = "views.py:30" in loc
        ok4 = "handle()" in loc

        ok5 = exercise_5_format_fix_location(None) == "Unknown location"

        ok = ok1 and ok2 and ok3 and ok4 and ok5
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
