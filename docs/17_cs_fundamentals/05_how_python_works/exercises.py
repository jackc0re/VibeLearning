"""
How Python Works - Exercises
============================
Practice exploring bytecode and Python internals.
"""

import dis
import sys
import time

print("=" * 60)
print("HOW PYTHON WORKS - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: Bytecode Analyzer
# =============================================================================
print("\n--- Exercise 1: Bytecode Analyzer ---")
print("""
Write a function that analyzes bytecode and returns statistics:
- Total number of instructions
- Most frequently used opcodes
- Number of load/store operations
""")

def analyze_bytecode(func):
    """
    Analyze the bytecode of a function.

    Args:
        func: A Python function

    Returns:
        Dictionary with bytecode statistics
    """
    # Your code here:
    # Hint: Use dis.Bytecode(func) to iterate over instructions
    pass

# Test
# def sample_func(x, y):
#     z = x + y
#     if z > 10:
#         return z * 2
#     return z
#
# stats = analyze_bytecode(sample_func)
# print(stats)

# =============================================================================
# EXERCISE 2: Implement a Simple Stack Machine
# =============================================================================
print("\n--- Exercise 2: Simple Stack Machine ---")
print("""
Implement a simple stack-based virtual machine that can execute
a subset of Python bytecode instructions:

- LOAD_CONST: Push constant onto stack
- LOAD_NAME: Push variable onto stack
- STORE_NAME: Store top of stack to variable
- BINARY_ADD: Pop two values, push sum
- BINARY_MULTIPLY: Pop two values, push product
- RETURN_VALUE: Return top of stack
""")

class SimpleVM:
    """A simple stack-based virtual machine."""

    def __init__(self):
        self.stack = []
        self.variables = {}

    def LOAD_CONST(self, value):
        """Push a constant onto the stack."""
        # Your code here:
        pass

    def LOAD_NAME(self, name):
        """Push a variable's value onto the stack."""
        # Your code here:
        pass

    def STORE_NAME(self, name):
        """Store top of stack to a variable."""
        # Your code here:
        pass

    def BINARY_ADD(self):
        """Pop two values, push their sum."""
        # Your code here:
        pass

    def BINARY_MULTIPLY(self):
        """Pop two values, push their product."""
        # Your code here:
        pass

    def RETURN_VALUE(self):
        """Return the top of stack."""
        # Your code here:
        pass

    def execute(self, instructions):
        """
        Execute a list of instructions.

        Args:
            instructions: List of (opcode, arg) tuples

        Returns:
            Result of execution
        """
        # Your code here:
        pass

# Test your VM
# vm = SimpleVM()
# instructions = [
#     ('LOAD_CONST', 5),
#     ('LOAD_CONST', 3),
#     ('BINARY_ADD', None),
#     ('RETURN_VALUE', None)
# ]
# result = vm.execute(instructions)
# print(f"5 + 3 = {result}")  # Expected: 8

# =============================================================================
# EXERCISE 3: GIL Impact Measurement
# =============================================================================
print("\n--- Exercise 3: GIL Impact Measurement ---")
print("""
Measure the actual impact of the GIL on different types of tasks:
1. CPU-bound (calculations)
2. I/O-bound (simulated with sleep)

Use threading vs sequential execution and compare times.
""")

def measure_gil_impact(task_type="cpu"):
    """
    Measure the impact of the GIL.

    Args:
        task_type: "cpu" or "io"

    Returns:
        Dictionary with timing results
    """
    import threading

    def cpu_task():
        """CPU-intensive task."""
        count = 0
        for i in range(1000000):
            count += i ** 2
        return count

    def io_task():
        """I/O-bound task (simulated)."""
        time.sleep(0.1)
        return "done"

    task = cpu_task if task_type == "cpu" else io_task

    # Your code here:
    # Time sequential execution
    # Time threaded execution
    # Return comparison
    pass

# Run measurements
# results = measure_gil_impact("cpu")
# print(f"CPU-bound: Sequential={results['sequential']:.3f}s, Threaded={results['threaded']:.3f}s")
#
# results = measure_gil_impact("io")
# print(f"I/O-bound: Sequential={results['sequential']:.3f}s, Threaded={results['threaded']:.3f}s")

# =============================================================================
# EXERCISE 4: Constant Folding Detector
# =============================================================================
print("\n--- Exercise 4: Constant Folding Detector ---")
print("""
Write a function that checks if Python optimized a constant expression
at compile time by examining the bytecode.

Example: `2 + 3` becomes `LOAD_CONST 5` (optimized)
         `x + 3` stays as `LOAD_FAST x; LOAD_CONST 3; BINARY_ADD`
""")

def is_constant_folded(func):
    """
    Check if a function has constant folding optimization.

    Args:
        func: A function with arithmetic operations

    Returns:
        True if constants are folded, False otherwise
    """
    # Your code here:
    # Look for BINARY_ADD with only constants before it
    pass

# Test functions
# def folded():
#     return 2 + 3  # Should be folded to 5
#
# def not_folded(x):
#     return x + 3  # Cannot fold (x is variable)
#
# print(f"folded() is optimized: {is_constant_folded(folded)}")      # True
# print(f"not_folded() is optimized: {is_constant_folded(not_folded)}")  # False

# =============================================================================
# EXERCISE 5: Import Time Tracker
# =============================================================================
print("\n--- Exercise 5: Import Time Tracker ---")
print("""
Write a context manager that measures how long importing a module takes.
Also check if the module was loaded from .pyc or source.
""")

class ImportTimer:
    """Context manager to time module imports."""

    def __enter__(self):
        # Your code here:
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Your code here:
        pass

    def import_module(self, module_name):
        """Import a module and track details."""
        # Your code here:
        pass

# Usage:
# with ImportTimer() as timer:
#     result = timer.import_module("json")
#     print(f"Imported from: {result['source']}")
#     print(f"Time taken: {result['time']:.4f}s")

# =============================================================================
# EXERCISE 6: Recursion Limit Explorer
# =============================================================================
print("\n--- Exercise 6: Recursion Limit Explorer ---")
print("""
Write a function that safely explores the recursion limit without
actually hitting it and crashing.
""")

def find_recursion_limit_safely():
    """
    Find the recursion limit without exceeding it.

    Returns:
        The recursion limit value
    """
    # Your code here:
    # Use sys.getrecursionlimit() and verify with a bounded test
    pass

# Alternative: Write a tail-recursive function decorator
# that converts recursion to iteration to avoid stack overflow

def tail_recursive(func):
    """
    Decorator to optimize tail-recursive functions.

    This is a simplified version - real implementations are more complex.
    """
    # Your code here:
    pass

# Test
# @tail_recursive
# def factorial(n, acc=1):
#     if n <= 1:
#         return acc
#     return factorial(n - 1, n * acc)
#
# print(f"Factorial of 1000: {factorial(1000)}")  # Won't overflow!

# =============================================================================
# EXERCISE 7: Bytecode Optimizer
# =============================================================================
print("\n--- Exercise 7: Simple Bytecode Optimizer ---")
print("""
Write a function that takes bytecode instructions and performs
simple optimizations:
- Remove redundant loads (LOAD_FAST a; LOAD_FAST a → keep one)
- Constant folding (LOAD_CONST 2; LOAD_CONST 3; BINARY_ADD → LOAD_CONST 5)
""")

def optimize_bytecode(instructions):
    """
    Optimize a list of bytecode instructions.

    Args:
        instructions: List of (opcode, arg) tuples

    Returns:
        Optimized list of instructions
    """
    # Your code here:
    pass

# Test
# instructions = [
#     ('LOAD_CONST', 2),
#     ('LOAD_CONST', 3),
#     ('BINARY_ADD', None),
#     ('STORE_NAME', 'x'),
# ]
# optimized = optimize_bytecode(instructions)
# print("Original:", instructions)
# print("Optimized:", optimized)
# Expected: [('LOAD_CONST', 5), ('STORE_NAME', 'x')]

# =============================================================================
# EXERCISE 8: Code Object Inspector
# =============================================================================
print("\n--- Exercise 8: Code Object Inspector ---")
print("""
Write a comprehensive code object inspector that displays:
- All code object attributes
- Nested functions/closures
- Free variables and cell variables
- Line number mapping
""")

def inspect_code_object(func):
    """
    Display comprehensive information about a function's code object.

    Args:
        func: A Python function
    """
    code = func.__code__

    # Your code here:
    # Print all code object attributes in a formatted way
    # Include nested code objects
    pass

# Test with a complex function
# def outer(x):
#     y = 10
#     def inner(z):
#         return x + y + z
#     return inner
#
# inspect_code_object(outer)

print("\n" + "=" * 60)
print("Exercises complete! Check your answers below.")
print("=" * 60)

# =============================================================================
# SOLUTIONS
# =============================================================================
print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

print("\n--- Exercise 1: Bytecode Analyzer (Solution) ---")
solution_1 = '''
import dis
from collections import Counter

def analyze_bytecode(func):
    stats = {
        "total_instructions": 0,
        "opcode_counts": Counter(),
        "load_operations": 0,
        "store_operations": 0,
        "instructions": []
    }

    for instr in dis.Bytecode(func):
        stats["total_instructions"] += 1
        stats["opcode_counts"][instr.opname] += 1
        stats["instructions"].append((instr.opname, instr.arg))

        if "LOAD" in instr.opname:
            stats["load_operations"] += 1
        elif "STORE" in instr.opname:
            stats["store_operations"] += 1

    return stats
'''
print(solution_1)

print("\n--- Exercise 2: Simple Stack Machine (Solution) ---")
solution_2 = '''
class SimpleVM:
    def __init__(self):
        self.stack = []
        self.variables = {}

    def LOAD_CONST(self, value):
        self.stack.append(value)

    def LOAD_NAME(self, name):
        self.stack.append(self.variables[name])

    def STORE_NAME(self, name):
        self.variables[name] = self.stack.pop()

    def BINARY_ADD(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)

    def BINARY_MULTIPLY(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a * b)

    def RETURN_VALUE(self):
        return self.stack.pop()

    def execute(self, instructions):
        for op, arg in instructions:
            method = getattr(self, op)
            if arg is not None:
                method(arg)
            else:
                method()
        return None
'''
print(solution_2)

print("\n--- Exercise 3: GIL Impact Measurement (Solution) ---")
solution_3 = '''
def measure_gil_impact(task_type="cpu"):
    import threading

    def cpu_task():
        count = 0
        for i in range(1000000):
            count += i ** 2
        return count

    def io_task():
        time.sleep(0.1)
        return "done"

    task = cpu_task if task_type == "cpu" else io_task

    # Sequential
    start = time.time()
    task()
    task()
    sequential_time = time.time() - start

    # Threaded
    start = time.time()
    t1 = threading.Thread(target=task)
    t2 = threading.Thread(target=task)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    threaded_time = time.time() - start

    return {
        "sequential": sequential_time,
        "threaded": threaded_time,
        "speedup": sequential_time / threaded_time
    }
'''
print(solution_3)

print("\n--- Exercise 4: Constant Folding Detector (Solution) ---")
solution_4 = '''
import dis

def is_constant_folded(func):
    """Check if function has constant folding by looking for BINARY_*
    instructions preceded only by LOAD_CONST."""
    bytecode = list(dis.Bytecode(func))

    for i, instr in enumerate(bytecode):
        if "BINARY" in instr.opname:
            # Check if previous two instructions were LOAD_CONST
            if i >= 2:
                prev1 = bytecode[i-1]
                prev2 = bytecode[i-2]
                if (prev1.opname == "LOAD_CONST" and
                    prev2.opname == "LOAD_CONST"):
                    # This is likely constant-folded at runtime
                    # but not at compile time
                    return False

    # If no unfolded constants found, it may be optimized
    # Actually, this is tricky - better to check for LOAD_CONST with computed value
    return True
'''
print(solution_4)

print("\n--- Exercise 5: Import Time Tracker (Solution) ---")
solution_5 = '''
class ImportTimer:
    def __enter__(self):
        self.start_time = None
        self.end_time = None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def import_module(self, module_name):
        import importlib
        import importlib.util

        self.start_time = time.time()
        module = importlib.import_module(module_name)
        self.end_time = time.time()

        # Check if loaded from .pyc
        if hasattr(module, '__cached__') and module.__cached__:
            source = f".pyc cache ({module.__cached__})"
        else:
            source = f"source ({module.__file__})"

        return {
            "module": module,
            "source": source,
            "time": self.end_time - self.start_time
        }
'''
print(solution_5)

print("\n--- Exercise 6: Recursion Limit Explorer (Solution) ---")
solution_6 = '''
def find_recursion_limit_safely():
    """Just use sys.getrecursionlimit() - it's the safe way!"""
    return sys.getrecursionlimit()

def tail_recursive(func):
    """Decorator to convert tail recursion to iteration."""
    def wrapper(*args, **kwargs):
        while True:
            result = func(*args, **kwargs)
            if isinstance(result, tuple) and result[0] == "recurse":
                args = result[1]
                kwargs = result[2] if len(result) > 2 else {}
            else:
                return result
    return wrapper

# Usage pattern for tail recursion:
def factorial_impl(n, acc=1):
    if n <= 1:
        return acc
    return ("recurse", (n-1,), {"acc": n * acc})

# factorial = tail_recursive(factorial_impl)
'''
print(solution_6)

print("\n--- Exercise 7: Bytecode Optimizer (Solution) ---")
solution_7 = '''
def optimize_bytecode(instructions):
    """Simple bytecode optimizer."""
    optimized = []
    i = 0

    while i < len(instructions):
        op, arg = instructions[i]

        # Constant folding for ADD
        if (op == "BINARY_ADD" and i >= 2 and
            instructions[i-1][0] == "LOAD_CONST" and
            instructions[i-2][0] == "LOAD_CONST"):
            # Remove the two LOAD_CONST and BINARY_ADD
            val2 = instructions[i-1][1]
            val1 = instructions[i-2][1]
            optimized = optimized[:-2]
            optimized.append(("LOAD_CONST", val1 + val2))
        else:
            optimized.append((op, arg))

        i += 1

    return optimized
'''
print(solution_7)

print("\n--- Exercise 8: Code Object Inspector (Solution) ---")
solution_8 = '''
def inspect_code_object(func):
    """Display comprehensive code object information."""
    code = func.__code__

    print(f"Function: {func.__name__}")
    print(f"  co_name: {code.co_name}")
    print(f"  co_argcount: {code.co_argcount}")
    print(f"  co_varnames: {code.co_varnames}")
    print(f"  co_names: {code.co_names}")
    print(f"  co_consts: {code.co_consts}")
    print(f"  co_freevars: {code.co_freevars}")
    print(f"  co_cellvars: {code.co_cellvars}")
    print(f"  co_filename: {code.co_filename}")
    print(f"  co_firstlineno: {code.co_firstlineno}")
    print(f"  co_stacksize: {code.co_stacksize}")
    print(f"  co_flags: {code.co_flags}")

    # Check for nested code objects
    for const in code.co_consts:
        if hasattr(const, "co_code"):
            print(f"\\n  Nested function found:")
            print(f"    Name: {const.co_name}")
'''
print(solution_8)

print("\n" + "=" * 60)
print("All solutions provided. Keep practicing!")
print("=" * 60)
