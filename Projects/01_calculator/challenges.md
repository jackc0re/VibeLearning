# 🎯 Calculator Challenges

Extend your calculator with these additional features. Each challenge builds on your existing knowledge and introduces new concepts.

---

## Challenge 1: Advanced Scientific Operations

Add scientific functions to make your calculator more powerful.

### Features to Add

1. **Square Root** — Calculate square root of a number
2. **Logarithm** — Natural and base-10 logarithms
3. **Trigonometric Functions** — sin, cos, tan
4. **Absolute Value** — Get absolute value of a number

### Implementation

```python
import math

def square_root(a):
    """Calculate the square root of a number."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)

def natural_log(a):
    """Calculate the natural logarithm of a number."""
    if a <= 0:
        raise ValueError("Logarithm requires positive numbers")
    return math.log(a)

def sin(angle):
    """Calculate sine of an angle (in degrees)."""
    radians = math.radians(angle)
    return math.sin(radians)

def cos(angle):
    """Calculate cosine of an angle (in degrees)."""
    radians = math.radians(angle)
    return math.cos(radians)

def tan(angle):
    """Calculate tangent of an angle (in degrees)."""
    radians = math.radians(angle)
    return math.tan(radians)
```

### New Menu Options

Update your menu to include:
- 10. Square Root (√)
- 11. Natural Log (ln)
- 12. Sine (sin)
- 13. Cosine (cos)
- 14. Tangent (tan)

---

## Challenge 2: Memory Feature

Add memory functionality to store and recall values.

### Features to Add

1. **Memory Store (M+)** — Store current result in memory
2. **Memory Recall (MR)** — Retrieve value from memory
3. **Memory Clear (MC)** — Clear memory
4. **Memory Add (M+ to current)** — Add current result to memory

### Implementation

```python
memory_value = 0
memory_enabled = False

def memory_store(value):
    """Store a value in memory."""
    global memory_value, memory_enabled
    memory_value = value
    memory_enabled = True

def memory_recall():
    """Recall value from memory."""
    global memory_value, memory_enabled
    if not memory_enabled:
        raise ValueError("Memory is empty")
    return memory_value

def memory_clear():
    """Clear the memory."""
    global memory_enabled
    memory_enabled = False

def memory_add(value):
    """Add value to current memory."""
    global memory_value
    memory_value += value
```

### New Menu Options

Add these options to your menu:
- 15. Memory Store (MS)
- 16. Memory Recall (MR)
- 17. Memory Add (M+)
- 18. Memory Clear (MC)

---

## Challenge 3: Persistent History

Save calculation history to a file and load it on startup.

### Features to Add

1. **Save to File** — Automatically save history on exit
2. **Load from File** — Load saved history on startup
3. **Export History** — Export history as text file

### Implementation

```python
import json
import os

HISTORY_FILE = "calculator_history.json"

def save_history(history):
    """Save calculation history to file."""
    data = {
        "history": history,
        "total_calculations": len(history)
    }
    try:
        with open(HISTORY_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Could not save history: {e}")

def load_history():
    """Load calculation history from file."""
    if not os.path.exists(HISTORY_FILE):
        return []
    
    try:
        with open(HISTORY_FILE, 'r') as f:
            data = json.load(f)
            return data.get("history", [])
    except Exception as e:
        print(f"Could not load history: {e}")
        return []

def export_history(history, filename="history_export.txt"):
    """Export history to a text file."""
    try:
        with open(filename, 'w') as f:
            f.write("CALCULATOR HISTORY\n")
            f.write("=" * 40 + "\n")
            for i, calc in enumerate(history, 1):
                f.write(f"{i}. {calc}\n")
        print(f"History exported to {filename}")
    except Exception as e:
        print(f"Could not export history: {e}")
```

### Update Main Function

```python
def main():
    history = load_history()  # Load saved history
    
    # ... rest of your program ...
    
    # Before exiting
    if choice == 9:
        save_history(history)  # Save history on exit
        break
```

---

## Challenge 4: Color Output

Add colored output for a better user experience.

### Installation

```bash
pip install colorama
```

### Implementation

```python
from colorama import Fore, Style, init

init()  # Initialize colorama

def print_success(text):
    """Print text in green."""
    print(f"{Fore.GREEN}{text}{Style.RESET_ALL}")

def print_error(text):
    """Print text in red."""
    print(f"{Fore.RED}{text}{Style.RESET_ALL}")

def print_info(text):
    """Print text in blue."""
    print(f"{Fore.BLUE}{text}{Style.RESET_ALL}")

def print_warning(text):
    """Print text in yellow."""
    print(f"{Fore.YELLOW}{text}{Style.RESET_ALL}")
```

### Usage Examples

```python
print_success("Result: 42")
print_error("Error: Cannot divide by zero")
print_info("History cleared!")
print_warning("Memory is empty")
```

---

## Challenge 5: History Search and Filter

Add functionality to search and filter calculation history.

### Features to Add

1. **Search by Operator** — Show all additions, multiplications, etc.
2. **Search by Value** — Show calculations containing a specific number
3. **Filter by Date/Time** — Show recent calculations
4. **Count Operations** — Count how many times each operation was used

### Implementation

```python
from datetime import datetime

def search_history(history, operator=None, value=None):
    """Search history by operator or value."""
    results = []
    for calc in history:
        include = True
        if operator and operator not in calc:
            include = False
        if value and str(value) not in calc:
            include = False
        if include:
            results.append(calc)
    return results

def count_operations(history):
    """Count occurrences of each operation."""
    counts = {"+": 0, "-": 0, "*": 0, "/": 0, "^": 0, "%": 0}
    for calc in history:
        for op in counts:
            if op in calc:
                counts[op] += 1
    return counts

def show_operation_stats(history):
    """Display statistics about operations."""
    counts = count_operations(history)
    print("\n" + "=" * 40)
    print("        OPERATION STATISTICS")
    print("=" * 40)
    for op, count in counts.items():
        percentage = (count / len(history) * 100) if history else 0
        bar = "█" * int(percentage / 5)
        print(f"{op:2s}: {count:3d} {bar} {percentage:5.1f}%")
    print("=" * 40)
```

### New Menu Options

Add these options to your menu:
- 19. Search History
- 20. Show Statistics

---

## Challenge 6: Unit Conversion

Add a unit conversion feature to the calculator.

### Features to Add

1. **Length Conversion** — km, m, cm, mm, miles, yards, feet, inches
2. **Weight Conversion** — kg, g, mg, pounds, ounces
3. **Temperature Conversion** — Celsius, Fahrenheit, Kelvin

### Implementation

```python
def convert_length(value, from_unit, to_unit):
    """Convert length between different units."""
    units = {
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    
    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit")
    
    meters = value * units[from_unit]
    return meters / units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    if from_unit == to_unit:
        return value
    
    if from_unit == 'C':
        if to_unit == 'F':
            return (value * 9/5) + 32
        elif to_unit == 'K':
            return value + 273.15
    elif from_unit == 'F':
        if to_unit == 'C':
            return (value - 32) * 5/9
        elif to_unit == 'K':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'K':
        if to_unit == 'C':
            return value - 273.15
        elif to_unit == 'F':
            return (value - 273.15) * 9/5 + 32
    
    raise ValueError("Invalid temperature unit")
```

---

## Challenge 7: Expression Evaluation

Allow users to enter full mathematical expressions.

### Features to Add

1. **Evaluate Expressions** — Parse and evaluate strings like "2 + 3 * 4"
2. **Parentheses Support** — Handle complex expressions
3. **Validation** — Check for valid expressions

### Implementation

```python
import ast
import operator as op

operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
}

def evaluate_expression(expr):
    """Safely evaluate a mathematical expression."""
    try:
        node = ast.parse(expr, mode='eval')
        return eval_node(node.body)
    except (ValueError, SyntaxError, ZeroDivisionError) as e:
        raise ValueError(f"Invalid expression: {e}")

def eval_node(node):
    """Recursively evaluate AST nodes."""
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        left = eval_node(node.left)
        right = eval_node(node.right)
        op_type = type(node.op)
        if op_type in operators:
            return operators[op_type](left, right)
    elif isinstance(node, ast.UnaryOp):
        operand = eval_node(node.operand)
        op_type = type(node.op)
        if op_type in operators:
            return operators[op_type](operand)
    raise TypeError("Invalid expression")
```

### Usage

```python
expr = input("Enter expression: ")
result = evaluate_expression(expr)
print(f"Result: {result}")
```

---

## 🏆 Challenge Completion

Track your progress:

- [ ] Challenge 1: Advanced Scientific Operations
- [ ] Challenge 2: Memory Feature
- [ ] Challenge 3: Persistent History
- [ ] Challenge 4: Color Output
- [ ] Challenge 5: History Search and Filter
- [ ] Challenge 6: Unit Conversion
- [ ] Challenge 7: Expression Evaluation

---

**Tip:** Complete challenges in any order. Start with the ones that interest you most!