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

## ⚠️ Common Mistakes

1. **Leaving debug prints in committed code** - they flood the user's console
   and can even leak data. Remove them before committing, or switch to
   `logger.debug(...)` which you can silence without edits.
2. **Printing too little context** - `print(x)` in a big log is useless an hour
   later. Print the variable *name* (`f"{x=}"`) and a location label so you can
   tell 40 prints apart.
3. **Prints that change behavior** - a print inside a loop can mask a bug that
   only appears when the loop is fast (timing-sensitive code), or consume a
   generator's items if you print next(...) instead of peeking. Prefer passive
   inspection.
4. **Debugging the wrong run** - editing the file while it runs, or prints
   buffered so they never appear before the crash. In scripts that die, prints
   to a pipe may be buffered; `print(..., flush=True)` forces output.

---

## 📝 Quick Reference

| Goal | Code |
|---|---|
| Show name and value | `print(f"{x=}")` -> `x=42` |
| Show type too | `print(f"{type(x)=}")` |
| Show repr (spots hidden spaces) | `print(f"{value!r}")` |
| Label the checkpoint | `print("[DEBUG] after loop:", total)` |
| Force output before a crash | `print(..., flush=True)` |
| Production-grade version | `logger.debug(...)` from the `logging` module |

---

## 🔍 Key Takeaways

- Print debugging is simple but powerful.
- Use f-strings with `=` for quick variable inspection.
- Add context (labels, separators) to make output readable.
- Consider `logging` for production code.
- Remove debug prints before committing!

---

[Back: Module 14 README](../README.md) | [Next: Using Debuggers](../02_using_debuggers/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
