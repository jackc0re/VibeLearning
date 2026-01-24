# 🖨️ Print Debugging

**Print debugging** is the simplest debugging technique: add `print()` statements to see what your code is doing. Despite being "primitive," it's often the fastest way to find bugs.

---

## ✅ Basic Print Debugging

```python
def calculate_total(items):
    print(f"Input items: {items}")  # What did we receive?

    total = 0
    for item in items:
        print(f"  Processing: {item}")  # What are we iterating?
        total += item['price'] * item['quantity']
        print(f"  Running total: {total}")  # State after each step

    print(f"Final total: {total}")  # What are we returning?
    return total
```

---

## ✅ What to Print

1. **Function inputs** - Are arguments what you expected?
2. **Loop iterations** - Is the loop running the right number of times?
3. **Conditional branches** - Which branch is being taken?
4. **Variable state** - What values do variables hold?
5. **Function outputs** - What's being returned?

---

## ✅ Formatting Debug Output

```python
# Include variable names (f-strings with =)
x = 42
print(f"{x=}")  # Output: x=42

# Include types
data = [1, 2, 3]
print(f"data={data!r}, type={type(data).__name__}")

# Add context/labels
print(f"[DEBUG] After loop: count={count}, total={total}")

# Use separators for visibility
print("=" * 40)
print(f"CHECKPOINT: {checkpoint_name}")
print("=" * 40)
```

---

## ✅ Debug Print Patterns

```python
# Pattern 1: Entry/Exit tracing
def process(data):
    print(f">>> Entering process({data!r})")
    result = do_something(data)
    print(f"<<< Exiting process() -> {result!r}")
    return result

# Pattern 2: Conditional debug
DEBUG = True
if DEBUG:
    print(f"[DEBUG] value={value}")

# Pattern 3: Quick type check
print(f"{type(mystery_var)=}")
```

---

## ✅ Using Logging Instead of Print

For production code, use `logging` instead of `print`:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process(data):
    logger.debug(f"Processing {data}")
    # ...
    logger.info(f"Processed {len(data)} items")
```

Advantages:
- Can be turned on/off without code changes
- Has levels (DEBUG, INFO, WARNING, ERROR)
- Can output to files, not just console

---

## ✅ When to Use Print Debugging

**Good for:**
- Quick investigations
- Understanding code flow
- Simple bugs
- Learning new code

**Consider alternatives when:**
- Bug is complex or intermittent
- Need to inspect many variables
- Code is hard to re-run

---

## 🔍 Key Takeaways

- Print debugging is simple but powerful.
- Use f-strings with `=` for quick variable inspection.
- Add context (labels, separators) to make output readable.
- Consider `logging` for production code.
- Remove debug prints before committing!

---

[Back: Module 14 README](../README.md) | [Next: Using Debuggers](../02_using_debuggers/)
