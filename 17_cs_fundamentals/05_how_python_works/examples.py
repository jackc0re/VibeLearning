"""
How Python Works - Examples
===========================
Exploring bytecode, the GIL, and Python internals.
"""

import dis
import sys

print("=" * 60)
print("HOW PYTHON WORKS - Examples")
print("=" * 60)

# =============================================================================
# VIEWING BYTECODE
# =============================================================================
print("\n--- Viewing Bytecode with dis ---\n")

def simple_add(a, b):
    """Simple function to demonstrate bytecode."""
    return a + b

print("Function: simple_add(a, b)")
print("Bytecode:")
dis.dis(simple_add)

print("\n--- More Complex Function ---\n")

def factorial(n):
    """Calculate factorial."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Function: factorial(n)")
print("Bytecode:")
dis.dis(factorial)

# =============================================================================
# BYTECODE INSTRUCTIONS EXPLAINED
# =============================================================================
print("\n" + "=" * 60)
print("BYTECODE INSTRUCTIONS")
print("=" * 60)

def demo_instructions():
    """Demonstrate various bytecode instructions."""
    x = 5           # LOAD_CONST, STORE_FAST
    y = x + 3       # LOAD_FAST, LOAD_CONST, BINARY_ADD, STORE_FAST
    z = x * y       # LOAD_FAST, LOAD_FAST, BINARY_MULTIPLY, STORE_FAST
    return z        # LOAD_FAST, RETURN_VALUE

print("\nFunction with various instructions:")
dis.dis(demo_instructions)

# =============================================================================
# COMPARING DIFFERENT APPROACHES
# =============================================================================
print("\n" + "=" * 60)
print("COMPARING BYTECODE: LOOP vs COMPREHENSION")
print("=" * 60)

# Method 1: For loop
def loop_version():
    result = []
    for i in range(10):
        result.append(i * 2)
    return result

# Method 2: List comprehension
def comprehension_version():
    return [i * 2 for i in range(10)]

print("\nFor loop version:")
dis.dis(loop_version)

print("\nList comprehension version (simpler bytecode):")
dis.dis(comprehension_version)

# =============================================================================
# CODE OBJECTS
# =============================================================================
print("\n" + "=" * 60)
print("CODE OBJECTS")
print("=" * 60)

def example_function(x, y=10):
    """An example function."""
    z = x + y
    return z * 2

# Every function has a __code__ attribute
code = example_function.__code__

print(f"\nFunction name: {code.co_name}")
print(f"Argument count: {code.co_argcount}")
print(f"Local variables: {code.co_varnames}")
print(f"Constants: {code.co_consts}")
print(f"Bytecode length: {len(code.co_code)} bytes")

# =============================================================================
# __PYCACHE__ AND .PYC FILES
# =============================================================================
print("\n" + "=" * 60)
print("BYTECODE CACHING")
print("=" * 60)

print("""
When you import a module, Python:
1. Compiles .py to bytecode
2. Saves as .pyc in __pycache__/
3. Reuses on next import

Example structure:
  my_module.py
  __pycache__/
    └── my_module.cpython-39.pyc
""")

# Show where Python looks for modules
print("\nPython import path:")
for path in sys.path[:5]:  # First 5 entries
    print(f"  {path}")

# Show compiled bytecode location
print(f"\nCurrent module cache:")
print(f"  __cached__: {getattr(sys.modules[__name__], '__cached__', 'N/A (running as script)')}")

# =============================================================================
# THE GIL DEMONSTRATION
# =============================================================================
print("\n" + "=" * 60)
print("GLOBAL INTERPRETER LOCK (GIL)")
print("=" * 60)

import threading
import time

def cpu_bound_task(n, name):
    """A CPU-intensive task."""
    count = 0
    for i in range(n):
        count += i * i
    print(f"  {name} completed")
    return count

print("\n--- Single-threaded execution ---")
start = time.time()
cpu_bound_task(5000000, "Task 1")
cpu_bound_task(5000000, "Task 2")
single_thread_time = time.time() - start
print(f"Total time: {single_thread_time:.2f}s")

print("\n--- Multi-threaded execution (with GIL) ---")
start = time.time()
t1 = threading.Thread(target=cpu_bound_task, args=(5000000, "Thread 1"))
t2 = threading.Thread(target=cpu_bound_task, args=(5000000, "Thread 2"))
t1.start()
t2.start()
t1.join()
t2.join()
threaded_time = time.time() - start
print(f"Total time: {threaded_time:.2f}s")

print(f"\nNote: Due to the GIL, threads don't run CPU-bound code in parallel.")
print(f"In fact, threading can be SLOWER due to context switching overhead.")

print("\n--- Solution: Multiprocessing for CPU-bound tasks ---")
from multiprocessing import Process

if __name__ == "__main__":
    # This section only runs when executed directly
    print("\n(Note: Multiprocessing example commented out to avoid issues)")
    print("For true parallelism, use:")
    print("  from multiprocessing import Pool")
    print("  with Pool(2) as p:")
    print("      p.map(cpu_bound_task, [data1, data2])")

# =============================================================================
# REFERENCE COUNTING
# =============================================================================
print("\n" + "=" * 60)
print("REFERENCE COUNTING")
print("=" * 60)

import ctypes

def ref_count(address):
    """Get reference count of object at address."""
    return ctypes.c_long.from_address(address).value

# Create an object
my_list = [1, 2, 3]
list_id = id(my_list)

print(f"\nCreated my_list = [1, 2, 3]")
print(f"Object id: {list_id}")
print(f"Initial ref count: {ref_count(list_id)}")

# Add references
another_ref = my_list
print(f"\nAfter another_ref = my_list:")
print(f"Ref count: {ref_count(list_id)}")

# Add to a dictionary
d = {"key": my_list}
print(f"\nAfter d['key'] = my_list:")
print(f"Ref count: {ref_count(list_id)}")

# Remove references
del another_ref
print(f"\nAfter del another_ref:")
print(f"Ref count: {ref_count(list_id)}")

d.pop("key")
print(f"\nAfter removing from dict:")
print(f"Ref count: {ref_count(list_id)}")

print("\nNote: The reference counting mechanism enables Python's")
print("      automatic garbage collection.")

# =============================================================================
# AST (ABSTRACT SYNTAX TREE)
# =============================================================================
print("\n" + "=" * 60)
print("ABSTRACT SYNTAX TREE (AST)")
print("=" * 60)

import ast

code = """
def greet(name):
    return f"Hello, {name}!"
"""

# Parse code into AST
tree = ast.parse(code)

print("\nParsed AST for:")
print(code)
print("\nAST structure (simplified):")
print(ast.dump(tree, indent=2))

# =============================================================================
# PERFORMANCE COMPARISON
# =============================================================================
print("\n" + "=" * 60)
print("PERFORMANCE COMPARISON")
print("=" * 60)

# Compare different ways to build a string
print("\n--- String Building ---")

def concat_strings(n):
    """Naive string concatenation."""
    result = ""
    for i in range(n):
        result += str(i)
    return result

def join_strings(n):
    """Efficient string building."""
    parts = []
    for i in range(n):
        parts.append(str(i))
    return "".join(parts)

def list_comp_strings(n):
    """List comprehension + join."""
    return "".join(str(i) for i in range(n))

# Time each approach
n = 100000

start = time.time()
concat_strings(n)
t1 = time.time() - start

start = time.time()
join_strings(n)
t2 = time.time() - start

start = time.time()
list_comp_strings(n)
t3 = time.time() - start

print(f"Naive concatenation: {t1:.4f}s")
print(f"List append + join:  {t2:.4f}s")
print(f"Generator + join:    {t3:.4f}s")
print(f"\nList comprehension is {t1/t3:.1f}x faster than naive!")

# =============================================================================
# BYTECODE OPTIMIZATION
# =============================================================================
print("\n" + "=" * 60)
print("BYTECODE OPTIMIZATION")
print("=" * 60)

# Python optimizes constant expressions at compile time

def with_constant():
    """This is optimized at compile time."""
    return 2 + 3  # Becomes LOAD_CONST 5

def with_variables():
    """This must be computed at runtime."""
    a = 2
    b = 3
    return a + b

print("\nConstant folding optimization:")
print("Function with constant expression:")
dis.dis(with_constant)

print("\nFunction with variables:")
dis.dis(with_variables)

# =============================================================================
# IMPORT MECHANISM
# =============================================================================
print("\n" + "=" * 60)
print("IMPORT MECHANISM")
print("=" * 60)

print("""
When Python imports a module:

1. Check sys.modules cache
2. Find the module file (.py, .pyc, .so, etc.)
3. Load source or bytecode
4. Compile if needed (.py → .pyc)
5. Execute module code
6. Store in sys.modules
7. Bind names in importing namespace

Example:
  import os

  1. Check sys.modules['os'] - exists? Use it!
  2. Find os.py or os.pyc
  3. Load/compile
  4. Execute (defines os functions)
  5. Store in sys.modules['os']
  6. 'os' available in current namespace
""")

# Show loaded modules
print(f"\nNumber of loaded modules: {len(sys.modules)}")
print(f"Some loaded modules:")
for name in list(sys.modules.keys())[:10]:
    print(f"  {name}")

# =============================================================================
# PYTHON IMPLEMENTATION INFO
# =============================================================================
print("\n" + "=" * 60)
print("PYTHON IMPLEMENTATION INFO")
print("=" * 60)

print(f"\nPython Implementation:")
print(f"  Implementation: {sys.implementation.name}")
print(f"  Version: {sys.version}")
print(f"  Version Info: {sys.version_info}")
print(f"  Platform: {sys.platform}")
print(f"  Max Unicode: {sys.maxunicode}")
print(f"  Default Encoding: {sys.getdefaultencoding()}")

print(f"\nInteger Properties:")
print(f"  Max int size: Unlimited! (Python 3)")
print(f"  Max size for containers: {sys.maxsize:,}")

print(f"\nRecursion Limit:")
print(f"  Current limit: {sys.getrecursionlimit()}")

# =============================================================================
# COMPILATION FLAGS
# =============================================================================
print("\n" + "=" * 60)
print("COMPILATION FLAGS")
print("=" * 60)

# Show compilation flags
code_obj = compile("x = 1 + 2", "<string>", "exec")
print(f"\nCompiled code object flags: {code_obj.co_flags}")

# Different optimization levels
print("\nOptimization levels:")
print("  -O : Remove assert statements and __debug__ code")
print("  -OO: Also remove docstrings")
print(f"\nCurrent __debug__ flag: {__debug__}")

print("\n" + "=" * 60)
print("Examples complete! Try the exercises next.")
print("=" * 60)
