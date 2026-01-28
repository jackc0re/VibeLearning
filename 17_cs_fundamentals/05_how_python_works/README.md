# 🐍 How Python Works

> Understanding the Python interpreter, bytecode, and the GIL

---

## What You'll Learn

- How Python executes your code
- What is bytecode and the PVM
- The Global Interpreter Lock (GIL)
- How .pyc files work
- Performance implications

---

## Python is an Interpreted Language

Unlike C or C++ which are compiled to machine code, Python code is **interpreted**.

But it's not as simple as "line by line":

```
Your Code (.py)
      ↓
[Parser] → AST (Abstract Syntax Tree)
      ↓
[Compiler] → Bytecode (.pyc)
      ↓
[PVM - Python Virtual Machine] → Execution
```

**Two stages:**
1. **Compilation:** Source code → Bytecode
2. **Interpretation:** Bytecode → Execution

---

## Step 1: Parsing

Python first parses your code into an **Abstract Syntax Tree (AST)**:

```python
# Your code
def greet(name):
    return f"Hello, {name}!"

# Becomes a tree structure:
# Module
#   └── FunctionDef (name='greet')
#         ├── arguments (name='name')
#         └── Return
#               └── JoinedStr (f-string)
```

This checks for **syntax errors** before execution.

---

## Step 2: Compilation to Bytecode

Bytecode is a **platform-independent** intermediate representation:

```python
# Python source
def add(a, b):
    return a + b

# Bytecode (simplified)
# LOAD_FAST     0 (a)    # Push 'a' onto stack
# LOAD_FAST     1 (b)    # Push 'b' onto stack
# BINARY_ADD             # Pop two values, add, push result
# RETURN_VALUE           # Return top of stack
```

Think of bytecode as "assembly language for the Python Virtual Machine."

---

## Step 3: The Python Virtual Machine (PVM)

The PVM is a **stack-based virtual machine**:

```
Execution Stack:
┌─────────────┐
│             │  ← Top (operations work here)
├─────────────┤
│             │
├─────────────┤
│             │
└─────────────┘
```

The PVM executes bytecode instructions one by one, manipulating the stack.

---

## Viewing Bytecode

Use the `dis` module to see bytecode:

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

Output:
```
  4           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE
```

**Column meanings:**
- Line number
- Byte offset
- Opcode name
- Opcode argument
- Human-readable explanation

---

## Common Bytecode Instructions

| Instruction | Description |
|-------------|-------------|
| `LOAD_FAST` | Load local variable onto stack |
| `LOAD_GLOBAL` | Load global variable onto stack |
| `LOAD_CONST` | Load constant onto stack |
| `STORE_FAST` | Store value to local variable |
| `BINARY_ADD` | Add top two stack values |
| `BINARY_MULTIPLY` | Multiply top two stack values |
| `COMPARE_OP` | Compare top two values |
| `POP_JUMP_IF_FALSE` | Conditional jump |
| `CALL_FUNCTION` | Call a function |
| `RETURN_VALUE` | Return top of stack |

---

## .pyc Files and __pycache__

When you import a module, Python:
1. Compiles it to bytecode
2. Saves it in `__pycache__/` as `.pyc` file
3. Reuses it next time (if source hasn't changed)

```
my_project/
├── my_module.py
└── __pycache__/
    └── my_module.cpython-39.pyc
```

**Why?** Loading bytecode is faster than recompiling source code!

---

## The Global Interpreter Lock (GIL)

The GIL is a **mutex** that protects access to Python objects:

### What the GIL Does

- Only **one thread** can execute Python bytecode at a time
- Prevents race conditions on Python objects
- Simplifies memory management

### Why Have the GIL?

1. **Reference counting safety:** Prevents race conditions when incrementing/decrementing reference counts
2. **Simpler C extensions:** Single-threaded access makes writing C extensions easier
3. **Single-threaded performance:** Faster for single-threaded programs

### The Problem

```python
import threading

def cpu_bound_task():
    """This won't run faster with threads due to GIL."""
    count = 0
    for i in range(10000000):
        count += 1

# These threads run sequentially, not in parallel!
t1 = threading.Thread(target=cpu_bound_task)
t2 = threading.Thread(target=cpu_bound_task)
```

**CPU-bound tasks** don't benefit from threads in Python!

### Workarounds

| Approach | Use Case |
|----------|----------|
| **multiprocessing** | CPU-bound tasks (true parallelism) |
| **asyncio** | I/O-bound tasks (concurrency) |
| **C extensions** | Release GIL (NumPy does this) |
| **Alternative Python** | Jython, IronPython (no GIL) |

---

## CPython vs Other Implementations

| Implementation | Description | GIL? |
|----------------|-------------|------|
| **CPython** | The standard Python (written in C) | Yes |
| **Jython** | Python on the JVM | No |
| **IronPython** | Python on .NET | No |
| **PyPy** | Python with JIT compiler | Yes (but faster) |
| **MicroPython** | For microcontrollers | Yes |

---

## Performance Considerations

### Compiled vs Interpreted

| Language | Type | Speed |
|----------|------|-------|
| C/C++ | Compiled to machine code | Fastest |
| Java | Compiled to bytecode + JIT | Fast |
| Python | Interpreted bytecode | Slower |

**Why is Python slower?**
- Bytecode interpretation overhead
- Dynamic typing (type checking at runtime)
- Object model overhead

### When Python is Fast Enough

- I/O-bound tasks (web requests, file operations)
- Glue code (coordinating other systems)
- Rapid development
- Data science (NumPy uses optimized C)

### Optimization Strategies

1. **Use built-in functions** (written in C)
2. **Use appropriate data structures**
3. **Use libraries like NumPy/Pandas** (C extensions)
4. **Profile before optimizing**
5. **Consider Cython or Numba** for hot paths
6. **Use multiprocessing** for CPU-bound work

---

## How Import Works

```python
import mymodule
```

**What Python does:**
1. Check `sys.modules` (cache) - already loaded?
2. Find the file (`.py`, `.pyc`, `.so`, etc.)
3. Load/compile the bytecode
4. Execute the module code
5. Store in `sys.modules`
6. Bind to local name

**Why check cache first?**
Prevent circular imports and speed up repeated imports.

---

## Common Mistakes ⚠️

### 1. Relying on bytecode
```python
# Don't manually edit .pyc files!
# They can be regenerated and deleted anytime
```

### 2. Ignoring the GIL
```python
# Don't expect thread speedup for CPU-bound work
import threading

# Use multiprocessing instead:
from multiprocessing import Pool
```

### 3. Assuming Python is always slow
```python
# Python + NumPy can beat naive C!
import numpy as np

# This is fast (implemented in C)
arr = np.random.rand(1000000)
result = np.sum(arr)
```

---

## Try It Out! 🚀

Run `examples.py` to see Python internals in action:
```bash
python examples.py
```

Then try `exercises.py` to practice:
```bash
python exercises.py
```

---

## Key Takeaways

1. Python code is **compiled to bytecode** then **interpreted** by the PVM
2. **Bytecode** is platform-independent intermediate code
3. Use the **`dis`** module to view bytecode
4. **.pyc files** cache bytecode for faster loading
5. The **GIL** allows only one thread to execute Python code at a time
6. For **CPU-bound parallelism**, use multiprocessing, not threading
7. Python's "slowness" is often acceptable and worth the productivity gain

---

**Previous:** [Memory Architecture ←](../04_memory_architecture/README.md)  
**Back to Module:** [CS Fundamentals](../README.md)

---

## Further Reading

- [CPython Internals](https://realpython.com/cpython-source-code-guide/)
- [Python Bytecode](https://docs.python.org/3/library/dis.html)
- [Understanding the GIL](https://realpython.com/python-gil/)
