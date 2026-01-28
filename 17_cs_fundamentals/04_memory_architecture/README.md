# 💾 Memory Architecture

> Understanding how computers store and manage data

---

## What You'll Learn

- What is RAM and how it works
- Stack vs Heap memory
- How Python manages memory
- References vs values
- Memory allocation basics

---

## What is Memory?

Computer **memory (RAM - Random Access Memory)** is like a giant grid of storage boxes. Each box has:
- An **address** (like a street address)
- A **value** stored inside

Think of it like a massive warehouse with numbered storage units:
```
Address    Value
-------    -----
1000       42
1001       "hello"
1002       [1, 2, 3]
...
```

---

## Memory Units

| Unit | Size | Comparison |
|------|------|------------|
| Bit (b) | 1 binary digit | 0 or 1 |
| Byte (B) | 8 bits | One character |
| Kilobyte (KB) | 1,024 bytes | Short text file |
| Megabyte (MB) | 1,024 KB | A photo |
| Gigabyte (GB) | 1,024 MB | A movie |
| Terabyte (TB) | 1,024 GB | Large database |

**Note:** Computers use base-2 (1024 = 2¹⁰), not base-10 (1000).

---

## Stack vs Heap

Programs use two main memory regions:

### Stack Memory 📚

Think of a stack of books:
- **Last In, First Out (LIFO)**
- Automatically managed
- Fast access
- Fixed size

**What goes on the stack:**
- Local variables
- Function parameters
- Return addresses

```python
def calculate():
    x = 5        # x is on the stack
    y = 10       # y is on the stack
    return x + y

# When calculate() returns, x and y are automatically removed
```

**Stack Frame:** Each function call gets a "frame" on the stack:
```
[main frame     ]
[calculate frame]  <- Current function
[stack grows ↑  ]
```

### Heap Memory 🏭

Think of a warehouse with open storage:
- Dynamically allocated
- Programmer-managed (in some languages)
- Slower access
- Flexible size

**What goes on the heap:**
- Objects
- Data structures (lists, dicts)
- Anything with dynamic size

```python
# The list itself is on the heap
# The variable 'data' (reference) is on the stack
data = [1, 2, 3, 4, 5]  # Heap allocation
```

---

## Key Differences

| Feature | Stack | Heap |
|---------|-------|------|
| Speed | Very fast | Slower |
| Size | Limited | Large |
| Management | Automatic | Manual (in C/C++) |
| Lifetime | Function scope | Program controlled |
| Fragmentation | No | Yes |
| Use case | Temporary data | Long-lived objects |

---

## The Call Stack

When you call a function, Python creates a **stack frame**:

```python
def a():
    x = 1
    b()
    print("A done")

def b():
    y = 2
    c()
    print("B done")

def c():
    z = 3
    print("C done")

a()
```

**Stack evolution:**
```
Step 1: [main]           Step 2: [main][a]        Step 3: [main][a][b]
        a() is called            b() is called           c() is called

Step 4: [main][a][b][c]  Step 5: [main][a][b]     Step 6: [main][a]
        c() executes             c() returns             b() returns

Step 7: [main]
        a() returns
```

---

## Stack Overflow

The stack has limited size. Too many nested calls cause a **stack overflow**:

```python
def infinite_recursion():
    return infinite_recursion()  # Stack overflow!
```

**Common causes:**
- Infinite recursion
- Very deep recursion
- Large local variables

---

## References vs Values

### Pass by Value

Some languages copy the actual value:
```
Before: x = 5
After passing to function: x = 5, function has its own copy
Changes in function don't affect x
```

### Pass by Reference

Python uses **references** (like pointers):
```python
def modify_list(lst):
    lst.append(4)  # Modifies the original list!

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4]
```

### Python's Model: Call by Object Reference

Python is neither purely pass-by-value nor pass-by-reference:

```python
def try_to_change(x, lst):
    x = 100           # Rebinds x to a new integer - doesn't affect original
    lst.append(4)     # Modifies the list object

num = 5
my_list = [1, 2, 3]
try_to_change(num, my_list)

print(num)       # 5 (unchanged!)
print(my_list)   # [1, 2, 3, 4] (modified!)
```

**Why?**
- Integers are **immutable** - can't change them, only rebind
- Lists are **mutable** - can modify them in place

---

## Memory in Python

### `id()` - Memory Address

Every Python object has a unique identifier (memory address):

```python
x = 42
print(id(x))  # e.g., 140735893619216

y = 42
print(id(y))  # Same address! Python caches small integers
```

### `is` vs `==`

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a == b   # True (same values)
a is b   # False (different objects in memory)
a is c   # True (same object!)
```

### `sys.getsizeof()` - Object Size

```python
import sys

print(sys.getsizeof(42))           # 28 bytes
print(sys.getsizeof([]))           # 56 bytes (empty list overhead)
print(sys.getsizeof([1, 2, 3]))    # More bytes
print(sys.getsizeof("hello"))      # 54 bytes
```

---

## Garbage Collection

Python automatically cleans up unused memory:

### Reference Counting

Every object tracks how many references point to it:
```python
x = [1, 2, 3]      # Reference count = 1
y = x              # Reference count = 2
del x              # Reference count = 1
y = None           # Reference count = 0 → Garbage collected!
```

### Cyclic References

Sometimes objects reference each other:
```python
a = []
b = []
a.append(b)  # a references b
b.append(a)  # b references a
```

Python's **cyclic garbage collector** detects and cleans these up.

---

## Memory Best Practices

### 1. Don't create unnecessary objects
```python
# Bad: Creates many intermediate strings
result = ""
for i in range(1000):
    result += str(i)  # New string each time!

# Better: Use join
result = "".join(str(i) for i in range(1000))
```

### 2. Use generators for large data
```python
# Bad: Creates entire list in memory
sum([x**2 for x in range(1000000)])

# Better: Generator, processes one at a time
sum(x**2 for x in range(1000000))
```

### 3. Delete references when done
```python
data = load_huge_file()
process(data)
del data  # Free memory for garbage collection
```

### 4. Be careful with mutable default arguments
```python
# Bug!
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - Same list reused!

# Fix:
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

---

## Common Mistakes ⚠️

### 1. Modifying a list while iterating
```python
# Wrong!
for item in my_list:
    my_list.remove(item)  # Skips items!

# Right
for item in my_list[:]:   # Iterate over a copy
    my_list.remove(item)
```

### 2. Creating references when you want copies
```python
# Both variables point to same list!
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # [1, 2, 3, 4] - Oops!

# Right: Make a copy
list2 = list1.copy()  # or list(list1) or list1[:]
```

### 3. Memory leaks with circular references
```python
# Can happen in complex data structures
a = {}
b = {}
a['other'] = b
b['other'] = a
# Both objects keep each other alive
# (Python's GC handles this, but not all languages do)
```

---

## Try It Out! 🚀

Run `examples.py` to see memory concepts in action:
```bash
python examples.py
```

Then try `exercises.py` to practice:
```bash
python exercises.py
```

---

## Key Takeaways

1. **Stack** is for temporary data (local variables, function calls)
2. **Heap** is for objects and long-lived data
3. Python uses **references** to objects, not copies
4. **Mutable** objects (lists, dicts) can be modified in place
5. **Immutable** objects (integers, strings, tuples) cannot be changed
6. Python has **automatic garbage collection**
7. Understanding memory helps you write efficient code

---

**Previous:** [Boolean Logic ←](../03_boolean_logic/README.md)  
**Next:** [How Python Works →](../05_how_python_works/README.md)
