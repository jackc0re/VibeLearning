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

## 🔍 Key Takeaways

- Use `breakpoint()` to pause execution.
- `n` (next) and `s` (step) for navigation.
- `p` and `pp` to inspect variables.
- `c` to continue, `q` to quit.
- Debuggers are powerful for complex, stateful bugs.

---

[Back: Print Debugging](../01_print_debugging/) | [Next: Reading Tracebacks](../03_reading_tracebacks/)
