"""Using Debuggers - Examples

Demonstrations:
- pdb commands and usage
- programmatic debugger control
- debugging techniques

Note: Some examples show debugger concepts without actually
entering the debugger (to allow automated running).

Run:
    python examples.py
"""

from __future__ import annotations

import sys
from typing import Any, Dict, List, Optional


def demo_breakpoint_usage() -> None:
    """Explain how to use breakpoint()."""
    print("=== Using breakpoint() ===\n")

    print("To debug a function, add breakpoint() where you want to pause:")
    print("""
    def calculate(x, y):
        breakpoint()  # <-- Execution pauses here
        result = x + y
        return result
    """)

    print("When hit, you'll see a (Pdb) prompt where you can:")
    print("  p x       - Print value of x")
    print("  n         - Execute next line")
    print("  s         - Step into a function call")
    print("  c         - Continue execution")
    print("  q         - Quit debugger")
    print()


def demo_pdb_commands() -> None:
    """Show common pdb commands."""
    print("=== Common pdb Commands ===\n")

    commands = [
        ("h(elp)", "Show help or help for a command"),
        ("n(ext)", "Execute next line, stepping OVER function calls"),
        ("s(tep)", "Execute next line, stepping INTO function calls"),
        ("r(eturn)", "Continue until current function returns"),
        ("c(ontinue)", "Continue until next breakpoint"),
        ("q(uit)", "Quit the debugger"),
        ("p expression", "Print the value of expression"),
        ("pp expression", "Pretty-print the value"),
        ("l(ist)", "Show source code around current line"),
        ("w(here)", "Show the call stack"),
        ("u(p)", "Move up one level in the call stack"),
        ("d(own)", "Move down one level in the call stack"),
        ("b lineno", "Set breakpoint at line number"),
        ("cl(ear)", "Clear breakpoints"),
    ]

    for cmd, desc in commands:
        print(f"  {cmd:18} - {desc}")
    print()


def demo_inspect_variables() -> None:
    """Show how to inspect variables in debugger."""
    print("=== Inspecting Variables ===\n")

    # Simulate what you'd see in debugger
    data = {"name": "Alice", "scores": [85, 90, 78], "active": True}
    items = [1, 2, 3, 4, 5]

    print("In pdb, you can inspect any variable or expression:\n")

    print(f"(Pdb) p data")
    print(f"{data}")

    print(f"\n(Pdb) pp data")
    import pprint
    pprint.pprint(data)

    print(f"\n(Pdb) p type(data)")
    print(f"{type(data)}")

    print(f"\n(Pdb) p data.keys()")
    print(f"{data.keys()}")

    print(f"\n(Pdb) p [x*2 for x in items]")
    print(f"{[x*2 for x in items]}")

    print(f"\n(Pdb) p len(items), sum(items)")
    print(f"{len(items)}, {sum(items)}")
    print()


def demo_navigation() -> None:
    """Explain debugger navigation."""
    print("=== Navigation Example ===\n")

    print("Consider this code:")
    print("""
    def outer(x):       # Line 1
        y = inner(x)    # Line 2  <-- breakpoint here
        return y * 2    # Line 3

    def inner(n):       # Line 5
        return n + 10   # Line 6
    """)

    print("Starting at line 2 with breakpoint:")
    print()
    print("  (Pdb) n    # Next - executes inner(), stops at line 3")
    print("             # You DON'T see inside inner()")
    print()
    print("  (Pdb) s    # Step - enters inner(), stops at line 6")
    print("             # You DO see inside inner()")
    print()
    print("  (Pdb) r    # Return - runs until inner() returns, back to line 2")
    print()
    print("  (Pdb) c    # Continue - runs until next breakpoint or end")
    print()


def demo_call_stack() -> None:
    """Show how to navigate the call stack."""
    print("=== Call Stack Navigation ===\n")

    def level_3():
        # Imagine breakpoint() here
        pass

    def level_2():
        level_3()

    def level_1():
        level_2()

    print("If stopped in level_3(), the stack looks like:")
    print("""
    (Pdb) w
      /path/script.py(10)level_1()
      /path/script.py(7)level_2()
    > /path/script.py(4)level_3()  <-- current frame

    (Pdb) u     # Move UP to level_2
    (Pdb) p local_var  # See level_2's variables

    (Pdb) u     # Move UP to level_1
    (Pdb) p local_var  # See level_1's variables

    (Pdb) d     # Move DOWN back to level_2
    (Pdb) d     # Move DOWN back to level_3
    """)
    print()


def demo_conditional_breakpoint() -> None:
    """Show conditional breakpoints."""
    print("=== Conditional Breakpoints ===\n")

    print("Break only when a condition is true:")
    print()
    print("  (Pdb) b 42, x > 100")
    print("  # Breaks at line 42 only when x > 100")
    print()
    print("  (Pdb) b process_item, item.type == 'special'")
    print("  # Breaks at function only for special items")
    print()
    print("Useful for debugging issues that only occur")
    print("under specific conditions.")
    print()


def demo_post_mortem() -> None:
    """Show post-mortem debugging."""
    print("=== Post-Mortem Debugging ===\n")

    print("Debug AFTER an exception has occurred:")
    print("""
    # Method 1: In your code
    import pdb

    try:
        buggy_function()
    except Exception:
        pdb.post_mortem()  # Enters debugger at failure point

    # Method 2: From command line
    python -m pdb script.py
    # When it crashes, you're in the debugger

    # Method 3: In interactive Python
    >>> buggy_function()
    Traceback ...
    >>> import pdb; pdb.pm()  # Debug last exception
    """)
    print()


def demo_breakpoint_env() -> None:
    """Show PYTHONBREAKPOINT environment variable."""
    print("=== PYTHONBREAKPOINT Environment Variable ===\n")

    print("Control breakpoint() behavior via environment:")
    print()
    print("  # Disable all breakpoints")
    print("  PYTHONBREAKPOINT=0 python script.py")
    print()
    print("  # Use a different debugger (e.g., ipdb)")
    print("  PYTHONBREAKPOINT=ipdb.set_trace python script.py")
    print()
    print("  # Use a custom function")
    print("  PYTHONBREAKPOINT=mymodule.my_debugger python script.py")
    print()
    print("This lets you ship code with breakpoint() calls and")
    print("disable them in production without changing code.")
    print()


def demo_debugging_workflow() -> None:
    """Show a typical debugging workflow."""
    print("=== Typical Debugging Workflow ===\n")

    print("1. REPRODUCE - Run code to see the bug")
    print()
    print("2. HYPOTHESIZE - Where might the bug be?")
    print()
    print("3. SET BREAKPOINT - Add breakpoint() before suspected area")
    print()
    print("4. INSPECT - At the breakpoint:")
    print("   - Check variable values: p variable")
    print("   - Check types: p type(variable)")
    print("   - Check conditions: p x > y")
    print()
    print("5. STEP THROUGH - Use n/s to watch execution")
    print()
    print("6. IDENTIFY - Find where actual != expected")
    print()
    print("7. FIX - Exit debugger, fix the code")
    print()
    print("8. VERIFY - Run again to confirm fix")
    print()


def demo_debugger_in_loops() -> None:
    """Show debugging loops effectively."""
    print("=== Debugging Loops ===\n")

    print("Problem: breakpoint() in a loop stops every iteration")
    print()
    print("Solution 1: Conditional breakpoint")
    print("""
    for i, item in enumerate(items):
        if i == 5:  # Only break on 5th iteration
            breakpoint()
        process(item)
    """)

    print("Solution 2: pdb conditional breakpoint")
    print("""
    for i, item in enumerate(items):
        breakpoint()  # Set once, then in pdb:
        process(item)

    # In pdb:
    (Pdb) condition 1 i == 5  # Only stop when i == 5
    (Pdb) c                   # Continue
    """)

    print("Solution 3: Break on specific condition")
    print("""
    for item in items:
        if item.status == "ERROR":
            breakpoint()  # Only stop for errors
        process(item)
    """)
    print()


if __name__ == "__main__":
    demo_breakpoint_usage()
    demo_pdb_commands()
    demo_inspect_variables()
    demo_navigation()
    demo_call_stack()
    demo_conditional_breakpoint()
    demo_post_mortem()
    demo_breakpoint_env()
    demo_debugging_workflow()
    demo_debugger_in_loops()
