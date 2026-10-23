# 🐛 Using Debuggers

A **debugger** lets you pause your program and inspect its state interactively. Python's built-in debugger is **pdb** (Python DeBugger).

---

## ✅ Starting the Debugger

```python
# Method 1: breakpoint() (Python 3.7+, recommended)
def calculate(x, y):
    breakpoint()  # Execution pauses here
    return x + y

# Method 2: import pdb
import pdb
def calculate(x, y):
    pdb.set_trace()  # Same effect
    return x + y

# Method 3: Run script with debugger
# python -m pdb script.py
```

---

## ✅ Essential pdb Commands

| Command | Short | Description |
|---------|-------|-------------|
| `help` | `h` | Show help |
| `next` | `n` | Execute next line (step over) |
| `step` | `s` | Step into function call |
| `continue` | `c` | Continue until next breakpoint |
| `return` | `r` | Continue until function returns |
| `quit` | `q` | Exit debugger |
| `print expr` | `p expr` | Print expression value |
| `pp expr` | | Pretty-print expression |
| `list` | `l` | Show current code context |
| `where` | `w` | Show call stack |
| `up` | `u` | Move up the call stack |
| `down` | `d` | Move down the call stack |

---

## ✅ Inspecting State

```python
(Pdb) p variable_name      # Print a variable
(Pdb) pp complex_dict      # Pretty-print
(Pdb) p type(x)            # Check type
(Pdb) p len(items)         # Evaluate expressions
(Pdb) p locals()           # See all local variables
(Pdb) p dir(obj)           # See object attributes
```

---

## ✅ Navigation Commands

```python
(Pdb) n        # Next line (don't enter functions)
(Pdb) s        # Step into function
(Pdb) r        # Run until current function returns
(Pdb) c        # Continue to next breakpoint
(Pdb) l        # List source code around current line
(Pdb) l 1, 20  # List lines 1-20
(Pdb) w        # Where am I? (show stack)
```

---

## ✅ Breakpoints

```python
(Pdb) b 42              # Break at line 42
(Pdb) b func_name       # Break when func_name is called
(Pdb) b file.py:42      # Break at line 42 in file.py
(Pdb) b 42, x > 10      # Conditional breakpoint
(Pdb) cl 1              # Clear breakpoint 1
(Pdb) bl                # List all breakpoints
```

---

## ✅ Example Debug Session

```python
def find_bug(numbers):
    breakpoint()
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)  # Bug: ZeroDivisionError if empty!

find_bug([])
```

```
> find_bug([])
(Pdb) p numbers          # Check input
[]
(Pdb) n                  # Execute next line
(Pdb) p total            # Check state
0
(Pdb) n                  # Step through loop
(Pdb) n                  # Loop doesn't execute (empty list)
(Pdb) p len(numbers)     # Aha! Length is 0
0
(Pdb) c                  # Continue - see the ZeroDivisionError
```

---

## ✅ Post-Mortem Debugging

Debug after an exception:

```python
# In interactive Python or script
import pdb

try:
    buggy_function()
except:
    pdb.post_mortem()  # Debug at point of failure
```

Or run with: `python -m pdb -c continue script.py`

---

## ⚠️ Common Mistakes

1. **Mixing up `s` and `n`** - `s` (step) enters the next function call, so you
   suddenly land inside `print` or library code; `n` (next) runs the whole line
   and stays at your level. When lost, `w` shows where you are and `q` quits.
2. **Forgetting `breakpoint()` in shipped code** - a stray `breakpoint()` in a
   deployed script hangs it waiting for a terminal. Set `PYTHONBREAKPOINT=0`
   to disable all breakpoints globally, and remove them before committing.
3. **Repeating `p var` after every step when `display var` exists** -
   `display var` re-prints the variable automatically each time it changes.
4. **Typing Python into the pdb prompt** - some words are pdb commands, not
   Python: `p x` prints, but bare `l` lists code instead of showing a variable
   named `l`. Prefix real Python with `!` (`!total = 0` reassigns a variable).

---

## 📝 Quick Reference

| Command | Short | Effect |
|---|---|---|
| `next` | `n` | run current line, step **over** calls |
| `step` | `s` | step **into** a call |
| `return` | `r` | finish current function, stop at its return |
| `continue` | `c` | run to the next breakpoint |
| `print expr` | `p expr` | evaluate and print an expression |
| `where` | `w` | show the call stack |
| `list` | `l` | show source around the current line |
| `break 42` | `b 42` | set a breakpoint (optionally conditional: `b 42, x > 10`) |
| `quit` | `q` | leave the debugger |

```python
breakpoint()          # pause here (Python 3.7+); PYTHONBREAKPOINT=0 disables it
```

---

## 🔍 Key Takeaways

- Use `breakpoint()` to pause execution.
- `n` (next) and `s` (step) for navigation.
- `p` and `pp` to inspect variables.
- `c` to continue, `q` to quit.
- Debuggers are powerful for complex, stateful bugs.

---

[Back: Print Debugging](../01_print_debugging/README.md) | [Next: Reading Tracebacks](../03_reading_tracebacks/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
