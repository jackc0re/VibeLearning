"""Print Debugging - Exercises

Goals:
- create useful debug output functions
- format debug information clearly
- trace program execution

Run with:
    python exercises.py
"""

from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional, TypeVar

T = TypeVar("T")


# =============================================================================
# EXERCISE 1: Debug Print Function
# =============================================================================


def exercise_1_debug_print(
    label: str, value: Any, show_type: bool = False
) -> str:
    """
    Create a formatted debug string.

    Args:
        label: Name/description of the value
        value: The value to display
        show_type: If True, include the type name

    Returns:
        Formatted string like "[DEBUG] label: value" or
        "[DEBUG] label: value (type)"

    Examples:
        debug_print("x", 42) -> "[DEBUG] x: 42"
        debug_print("x", 42, show_type=True) -> "[DEBUG] x: 42 (int)"
        debug_print("name", "Alice", show_type=True) -> "[DEBUG] name: 'Alice' (str)"
    """
    # Use repr for strings to show quotes
    if isinstance(value, str):
        value_str = repr(value)
    else:
        value_str = str(value)

    if show_type:
        type_name = type(value).__name__
        return f"[DEBUG] {label}: {value_str} ({type_name})"
    else:
        return f"[DEBUG] {label}: {value_str}"


# =============================================================================
# EXERCISE 2: Function Tracer
# =============================================================================


def exercise_2_trace_call(
    func_name: str, args: tuple, kwargs: dict
) -> str:
    """
    Format a function call for tracing.

    Returns a string showing the function call with its arguments.

    Examples:
        trace_call("foo", (1, 2), {}) -> "foo(1, 2)"
        trace_call("bar", (1,), {"x": 2}) -> "bar(1, x=2)"
        trace_call("baz", (), {"a": 1, "b": 2}) -> "baz(a=1, b=2)"
    """
    parts = []

    # Add positional args
    for arg in args:
        parts.append(repr(arg))

    # Add keyword args
    for key, val in kwargs.items():
        parts.append(f"{key}={val!r}")

    args_str = ", ".join(parts)
    return f"{func_name}({args_str})"


def exercise_2_make_tracer(func: Callable[..., T]) -> Callable[..., T]:
    """
    Create a wrapper that prints entry/exit traces for a function.

    The wrapper should print:
    - ">>> ENTER func_name(args)" when called
    - "<<< EXIT func_name -> result" when returning

    Returns the wrapped function.
    """

    def wrapper(*args: Any, **kwargs: Any) -> T:
        call_str = exercise_2_trace_call(func.__name__, args, kwargs)
        print(f">>> ENTER {call_str}")
        result = func(*args, **kwargs)
        print(f"<<< EXIT {func.__name__} -> {result!r}")
        return result

    return wrapper


# =============================================================================
# EXERCISE 3: Variable Watcher
# =============================================================================


class VariableWatcher:
    """
    A class that tracks variable changes for debugging.

    Usage:
        watcher = VariableWatcher()
        watcher.watch("x", 1)
        watcher.watch("x", 2)  # Prints change notification
        watcher.watch("x", 2)  # No print (value unchanged)
    """

    def __init__(self) -> None:
        self._values: Dict[str, Any] = {}
        self._history: List[str] = []

    def watch(self, name: str, value: Any) -> Optional[str]:
        """
        Watch a variable. Returns a change message if value changed.

        Returns None if this is the first time seeing the variable
        or if the value hasn't changed.
        """
        message = None

        if name in self._values:
            old_value = self._values[name]
            if old_value != value:
                message = f"[WATCH] {name} changed: {old_value!r} -> {value!r}"
                self._history.append(message)

        self._values[name] = value
        return message

    def get_history(self) -> List[str]:
        """Return list of all change messages."""
        return list(self._history)

    def current_values(self) -> Dict[str, Any]:
        """Return dict of current variable values."""
        return dict(self._values)


# =============================================================================
# EXERCISE 4: Execution Logger
# =============================================================================


class ExecutionLogger:
    """
    Logs execution steps with indentation for nested calls.

    Usage:
        logger = ExecutionLogger()
        logger.enter("outer")
        logger.log("doing something")
        logger.enter("inner")
        logger.log("nested action")
        logger.exit("inner")
        logger.exit("outer")
    """

    def __init__(self) -> None:
        self._indent_level = 0
        self._logs: List[str] = []

    def _indent(self) -> str:
        """Return current indentation string."""
        return "  " * self._indent_level

    def enter(self, name: str) -> None:
        """Log entering a named block/function."""
        line = f"{self._indent()}>>> ENTER {name}"
        self._logs.append(line)
        self._indent_level += 1

    def exit(self, name: str) -> None:
        """Log exiting a named block/function."""
        self._indent_level = max(0, self._indent_level - 1)
        line = f"{self._indent()}<<< EXIT {name}"
        self._logs.append(line)

    def log(self, message: str) -> None:
        """Log a message at current indent level."""
        line = f"{self._indent()}{message}"
        self._logs.append(line)

    def get_logs(self) -> List[str]:
        """Return all logged lines."""
        return list(self._logs)

    def print_logs(self) -> None:
        """Print all logs."""
        for line in self._logs:
            print(line)


# =============================================================================
# EXERCISE 5: Debug Decorator
# =============================================================================


def exercise_5_debug_args(func: Callable[..., T]) -> Callable[..., T]:
    """
    Decorator that prints function arguments and return value.

    Should print:
    - Function name and all arguments when called
    - Return value when function completes

    Format:
        Calling func_name:
          arg1 = value1
          arg2 = value2
        Returned: result
    """

    def wrapper(*args: Any, **kwargs: Any) -> T:
        # Get argument names from function signature
        import inspect

        sig = inspect.signature(func)
        params = list(sig.parameters.keys())

        print(f"Calling {func.__name__}:")

        # Print positional args
        for i, arg in enumerate(args):
            if i < len(params):
                print(f"  {params[i]} = {arg!r}")
            else:
                print(f"  *args[{i}] = {arg!r}")

        # Print keyword args
        for key, val in kwargs.items():
            print(f"  {key} = {val!r}")

        result = func(*args, **kwargs)
        print(f"Returned: {result!r}")
        return result

    return wrapper


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Print Debugging Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1: Debug Print Function
    print("\nExercise 1: Debug Print Function")
    try:
        ok1 = exercise_1_debug_print("x", 42) == "[DEBUG] x: 42"
        ok2 = exercise_1_debug_print("x", 42, show_type=True) == "[DEBUG] x: 42 (int)"
        ok3 = exercise_1_debug_print("name", "Alice", show_type=True) == "[DEBUG] name: 'Alice' (str)"
        ok4 = exercise_1_debug_print("items", [1, 2]) == "[DEBUG] items: [1, 2]"

        ok = ok1 and ok2 and ok3 and ok4
        print("  ", "PASS" if ok else "FAIL")
        if not ok:
            print(f"    Test 1: {exercise_1_debug_print('x', 42)}")
            print(f"    Test 2: {exercise_1_debug_print('x', 42, show_type=True)}")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2: Function Tracer
    print("\nExercise 2: Function Tracer")
    try:
        ok1 = exercise_2_trace_call("foo", (1, 2), {}) == "foo(1, 2)"
        ok2 = exercise_2_trace_call("bar", (1,), {"x": 2}) == "bar(1, x=2)"
        ok3 = exercise_2_trace_call("baz", (), {"a": 1, "b": 2}) == "baz(a=1, b=2)"

        # Test tracer wrapper
        @exercise_2_make_tracer
        def add(a: int, b: int) -> int:
            return a + b

        # Capture output would be complex, just test it runs
        result = add(2, 3)
        ok4 = result == 5

        ok = ok1 and ok2 and ok3 and ok4
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3: Variable Watcher
    print("\nExercise 3: Variable Watcher")
    try:
        watcher = VariableWatcher()

        # First watch returns None
        ok1 = watcher.watch("x", 1) is None

        # Same value returns None
        ok2 = watcher.watch("x", 1) is None

        # Changed value returns message
        msg = watcher.watch("x", 2)
        ok3 = msg is not None and "changed" in msg and "1" in msg and "2" in msg

        # History should have one entry
        ok4 = len(watcher.get_history()) == 1

        # Current values
        ok5 = watcher.current_values() == {"x": 2}

        ok = ok1 and ok2 and ok3 and ok4 and ok5
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 4: Execution Logger
    print("\nExercise 4: Execution Logger")
    try:
        logger = ExecutionLogger()
        logger.enter("outer")
        logger.log("step 1")
        logger.enter("inner")
        logger.log("step 2")
        logger.exit("inner")
        logger.exit("outer")

        logs = logger.get_logs()
        ok1 = len(logs) == 6
        ok2 = ">>> ENTER outer" in logs[0]
        ok3 = "  step 1" in logs[1]  # Indented
        ok4 = "  >>> ENTER inner" in logs[2]  # Indented
        ok5 = "    step 2" in logs[3]  # Double indented

        ok = ok1 and ok2 and ok3 and ok4 and ok5
        print("  ", "PASS" if ok else "FAIL")
        if not ok:
            print(f"    Logs: {logs}")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 5: Debug Decorator
    print("\nExercise 5: Debug Decorator")
    try:

        @exercise_5_debug_args
        def multiply(a: int, b: int) -> int:
            return a * b

        # Should print debug info and return correct result
        result = multiply(3, 4)
        ok = result == 12
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
