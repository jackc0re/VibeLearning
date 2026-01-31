"""Using Debuggers - Exercises

Goals:
- understand debugger commands
- simulate debugger state inspection
- practice debugging scenarios

Note: These exercises test understanding of debugger concepts
without actually entering interactive debug mode.

Run with:
    python exercises.py
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple


# =============================================================================
# EXERCISE 1: Parse Debugger Command
# =============================================================================


def exercise_1_parse_pdb_command(command: str) -> Dict[str, Any]:
    """
    Parse a pdb command string into components.

    Returns a dict with:
    - "command": the command name (full form)
    - "args": list of arguments (if any)

    Command mappings (short -> full):
    - h -> help, n -> next, s -> step, c -> continue
    - r -> return, q -> quit, p -> print, l -> list
    - w -> where, u -> up, d -> down, b -> break

    Examples:
        "n" -> {"command": "next", "args": []}
        "p x" -> {"command": "print", "args": ["x"]}
        "b 42" -> {"command": "break", "args": ["42"]}
        "l 1, 10" -> {"command": "list", "args": ["1", "10"]}
    """
    SHORT_TO_FULL = {
        "h": "help",
        "n": "next",
        "s": "step",
        "c": "continue",
        "r": "return",
        "q": "quit",
        "p": "print",
        "pp": "pprint",
        "l": "list",
        "w": "where",
        "u": "up",
        "d": "down",
        "b": "break",
        "cl": "clear",
        "bl": "breaklist",
    }

    parts = command.strip().split(None, 1)  # Split into command and rest
    if not parts:
        return {"command": "", "args": []}

    cmd = parts[0]
    # Map short form to full form
    full_cmd = SHORT_TO_FULL.get(cmd, cmd)

    args = []
    if len(parts) > 1:
        # Split arguments by comma or space
        arg_str = parts[1]
        # Handle comma-separated args like "1, 10"
        if "," in arg_str:
            args = [a.strip() for a in arg_str.split(",")]
        else:
            args = arg_str.split()

    return {"command": full_cmd, "args": args}


# =============================================================================
# EXERCISE 2: Simulate Variable Inspector
# =============================================================================


class DebugInspector:
    """
    Simulates debugger variable inspection.

    Stores variables and allows inspection commands.
    """

    def __init__(self) -> None:
        self._variables: Dict[str, Any] = {}

    def set_context(self, variables: Dict[str, Any]) -> None:
        """Set the current variable context (like locals())."""
        self._variables = dict(variables)

    def evaluate(self, expression: str) -> Tuple[bool, Any]:
        """
        Evaluate an expression in the current context.

        Returns (success, result) tuple.
        If evaluation fails, returns (False, error_message).
        """
        try:
            # Create safe eval context with our variables and safe builtins
            safe_builtins = {
                "len": len,
                "sum": sum,
                "min": min,
                "max": max,
                "abs": abs,
                "round": round,
                "sorted": sorted,
                "list": list,
                "dict": dict,
                "set": set,
                "tuple": tuple,
                "str": str,
                "int": int,
                "float": float,
                "bool": bool,
                "type": type,
                "isinstance": isinstance,
                "range": range,
                "enumerate": enumerate,
                "zip": zip,
                "map": map,
                "filter": filter,
                "any": any,
                "all": all,
                "True": True,
                "False": False,
                "None": None,
            }
            result = eval(expression, {"__builtins__": safe_builtins}, self._variables)
            return (True, result)
        except Exception as e:
            return (False, str(e))

    def get_type(self, var_name: str) -> Optional[str]:
        """Get the type name of a variable, or None if not found."""
        if var_name in self._variables:
            return type(self._variables[var_name]).__name__
        return None

    def list_variables(self) -> List[str]:
        """Return sorted list of variable names in context."""
        return sorted(self._variables.keys())


# =============================================================================
# EXERCISE 3: Call Stack Simulator
# =============================================================================


class CallStackFrame:
    """Represents a single frame in the call stack."""

    def __init__(
        self, function_name: str, line_number: int, local_vars: Dict[str, Any]
    ) -> None:
        self.function_name = function_name
        self.line_number = line_number
        self.local_vars = local_vars


class CallStackSimulator:
    """
    Simulates debugger call stack navigation.
    """

    def __init__(self) -> None:
        self._frames: List[CallStackFrame] = []
        self._current_index: int = 0

    def push_frame(
        self, function_name: str, line_number: int, local_vars: Dict[str, Any]
    ) -> None:
        """Add a frame to the stack (simulating a function call)."""
        frame = CallStackFrame(function_name, line_number, local_vars)
        self._frames.append(frame)
        self._current_index = len(self._frames) - 1

    def up(self) -> bool:
        """Move up the stack (toward caller). Returns False if at top."""
        if self._current_index > 0:
            self._current_index -= 1
            return True
        return False

    def down(self) -> bool:
        """Move down the stack (toward callee). Returns False if at bottom."""
        if self._current_index < len(self._frames) - 1:
            self._current_index += 1
            return True
        return False

    def current_frame(self) -> Optional[CallStackFrame]:
        """Get the current frame."""
        if self._frames:
            return self._frames[self._current_index]
        return None

    def where(self) -> List[str]:
        """
        Return stack trace like pdb's 'where' command.
        Mark current frame with '>'.
        """
        result = []
        for i, frame in enumerate(self._frames):
            marker = "> " if i == self._current_index else "  "
            line = f"{marker}{frame.function_name}() at line {frame.line_number}"
            result.append(line)
        return result


# =============================================================================
# EXERCISE 4: Breakpoint Manager
# =============================================================================


class BreakpointManager:
    """
    Manages breakpoints like pdb does.
    """

    def __init__(self) -> None:
        self._breakpoints: Dict[int, Dict[str, Any]] = {}  # id -> breakpoint info
        self._next_id: int = 1

    def add_breakpoint(
        self, line: int, condition: Optional[str] = None
    ) -> int:
        """
        Add a breakpoint at a line number.
        Returns the breakpoint ID.
        """
        bp_id = self._next_id
        self._next_id += 1
        self._breakpoints[bp_id] = {
            "line": line,
            "condition": condition,
            "enabled": True,
            "hits": 0,
        }
        return bp_id

    def remove_breakpoint(self, bp_id: int) -> bool:
        """Remove a breakpoint by ID. Returns True if removed."""
        if bp_id in self._breakpoints:
            del self._breakpoints[bp_id]
            return True
        return False

    def should_break(self, line: int, context: Dict[str, Any]) -> bool:
        """
        Check if execution should break at this line.

        Evaluates conditions if present.
        Increments hit count for matching breakpoints.
        """
        for bp_id, bp in self._breakpoints.items():
            if bp["line"] != line or not bp["enabled"]:
                continue

            # Check condition if present
            if bp["condition"]:
                try:
                    if not eval(bp["condition"], {"__builtins__": {}}, context):
                        continue
                except Exception:
                    continue  # Condition evaluation failed, skip

            bp["hits"] += 1
            return True

        return False

    def list_breakpoints(self) -> List[Dict[str, Any]]:
        """Return list of all breakpoints with their info."""
        result = []
        for bp_id, bp in self._breakpoints.items():
            result.append({"id": bp_id, **bp})
        return result


# =============================================================================
# EXERCISE 5: Debug Session Simulator
# =============================================================================


def exercise_5_simulate_debug_session(
    commands: List[str], initial_line: int, total_lines: int
) -> List[Tuple[str, int]]:
    """
    Simulate a debug session given a list of commands.

    Commands supported:
    - "n" (next): advance to next line
    - "c" (continue): jump to end
    - "l" (list): stay on current line

    Returns list of (command, line_number) tuples showing
    the line number after each command.

    Stops if line exceeds total_lines.
    """
    results = []
    current_line = initial_line

    for cmd in commands:
        if current_line > total_lines:
            break

        parsed = exercise_1_parse_pdb_command(cmd)
        action = parsed["command"]

        if action == "next":
            current_line += 1
        elif action == "continue":
            current_line = total_lines + 1  # Past the end
        elif action == "list":
            pass  # Stay on current line
        # Other commands don't change line

        results.append((cmd, min(current_line, total_lines + 1)))

    return results


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Using Debuggers Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1: Parse Debugger Command
    print("\nExercise 1: Parse Debugger Command")
    try:
        r1 = exercise_1_parse_pdb_command("n")
        ok1 = r1["command"] == "next" and r1["args"] == []

        r2 = exercise_1_parse_pdb_command("p x")
        ok2 = r2["command"] == "print" and r2["args"] == ["x"]

        r3 = exercise_1_parse_pdb_command("b 42")
        ok3 = r3["command"] == "break" and r3["args"] == ["42"]

        r4 = exercise_1_parse_pdb_command("l 1, 10")
        ok4 = r4["command"] == "list" and r4["args"] == ["1", "10"]

        ok = ok1 and ok2 and ok3 and ok4
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2: Simulate Variable Inspector
    print("\nExercise 2: Simulate Variable Inspector")
    try:
        inspector = DebugInspector()
        inspector.set_context({"x": 10, "y": 20, "items": [1, 2, 3]})

        success, result = inspector.evaluate("x + y")
        ok1 = success and result == 30

        success, result = inspector.evaluate("len(items)")
        ok2 = success and result == 3

        ok3 = inspector.get_type("x") == "int"
        ok4 = inspector.get_type("items") == "list"
        ok5 = inspector.get_type("nonexistent") is None

        vars_list = inspector.list_variables()
        ok6 = vars_list == ["items", "x", "y"]

        ok = ok1 and ok2 and ok3 and ok4 and ok5 and ok6
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3: Call Stack Simulator
    print("\nExercise 3: Call Stack Simulator")
    try:
        stack = CallStackSimulator()
        stack.push_frame("main", 10, {"a": 1})
        stack.push_frame("helper", 20, {"b": 2})
        stack.push_frame("inner", 30, {"c": 3})

        # Should be at bottom (inner)
        ok1 = stack.current_frame().function_name == "inner"

        # Move up
        ok2 = stack.up() is True
        ok3 = stack.current_frame().function_name == "helper"

        # Move up again
        stack.up()
        ok4 = stack.current_frame().function_name == "main"

        # Can't go higher
        ok5 = stack.up() is False

        # Move down
        stack.down()
        ok6 = stack.current_frame().function_name == "helper"

        # Check where output
        where = stack.where()
        ok7 = len(where) == 3 and any(">" in w for w in where)

        ok = ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 4: Breakpoint Manager
    print("\nExercise 4: Breakpoint Manager")
    try:
        mgr = BreakpointManager()

        # Add breakpoints
        bp1 = mgr.add_breakpoint(10)
        bp2 = mgr.add_breakpoint(20, condition="x > 5")

        ok1 = bp1 == 1 and bp2 == 2

        # Should break at line 10 (no condition)
        ok2 = mgr.should_break(10, {}) is True

        # Should break at line 20 when x > 5
        ok3 = mgr.should_break(20, {"x": 10}) is True
        ok4 = mgr.should_break(20, {"x": 3}) is False

        # Remove breakpoint
        ok5 = mgr.remove_breakpoint(bp1) is True
        ok6 = mgr.should_break(10, {}) is False

        # List breakpoints
        bps = mgr.list_breakpoints()
        ok7 = len(bps) == 1 and bps[0]["line"] == 20

        ok = ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 5: Debug Session Simulator
    print("\nExercise 5: Debug Session Simulator")
    try:
        commands = ["n", "n", "l", "n", "c"]
        results = exercise_5_simulate_debug_session(commands, 1, 10)

        # After n, n, l, n: should be at lines 2, 3, 3, 4
        # After c: should be past end (11)
        ok1 = len(results) == 5
        ok2 = results[0] == ("n", 2)
        ok3 = results[1] == ("n", 3)
        ok4 = results[2] == ("l", 3)  # list doesn't move
        ok5 = results[3] == ("n", 4)
        ok6 = results[4] == ("c", 11)  # continue to end

        ok = ok1 and ok2 and ok3 and ok4 and ok5 and ok6
        print("  ", "PASS" if ok else "FAIL")
        if not ok:
            print(f"    Results: {results}")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
