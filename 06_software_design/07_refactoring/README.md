# 🛠️ Refactoring

**Refactoring** is improving the internal structure of code **without changing what it does**. The goal is to make code easier to understand and safer to modify.

---

## ✅ When to Refactor

- When you spot repeated code (DRY)
- When a function/class is doing too much (low cohesion)
- When adding a feature feels risky (high coupling)
- After fixing a bug (so it doesn't come back)

---

## ✅ Refactoring Safety

Refactoring is safest when you have a **safety net**:

- Good automated tests
- Small, incremental changes
- Frequent re-running of examples/tests

---

## ✅ Common Refactoring Moves

- Extract function / extract class
- Rename for clarity
- Replace conditionals with polymorphism (when appropriate)
- Introduce value objects instead of primitive obsession
- Reduce parameter lists by grouping data

---

## ✅ A Worked Example: Before and After

A price function that grew a coupon and a bulk discount. It works — but the
names tell you nothing, the numbers are magic, and the edge case hides in the
middle.

```python
# BEFORE: vague names, magic numbers, nested edge case
def calc(p, c):
    if p > 0:
        if c:
            r = p * 0.9
        else:
            r = p
        if r > 100:
            r = r - 10
        return r
    else:
        return 0
```

Three small moves — rename, extract, guard clause — leave the behavior
identical but the intent visible:

```python
# AFTER: guard clause first, named constants, extracted step, clear names
COUPON_RATE = 0.9
BULK_THRESHOLD = 100
BULK_DISCOUNT = 10


def apply_coupon(price, has_coupon):
    return price * COUPON_RATE if has_coupon else price


def final_price(price, has_coupon):
    if price <= 0:                       # guard clause: edge case first
        return 0
    discounted = apply_coupon(price, has_coupon)
    if discounted > BULK_THRESHOLD:      # happy path reads top to bottom
        discounted -= BULK_DISCOUNT
    return discounted
```

---

## ✅ The Refactoring Checklist, as Code

Pin the old behavior *before* you touch anything, then prove nothing changed:

```python
cases = [(200, True), (50, False), (0, True), (-5, False)]

# Step 1: capture the OLD behavior before refactoring
golden = [calc(price, coupon) for price, coupon in cases]

# Step 2: ...do the refactor (final_price above)...

# Step 3: prove nothing changed
for (price, coupon), old in zip(cases, golden):
    assert final_price(price, coupon) == old, f"behavior changed for ({price}, {coupon})"
print("PASS behavior preserved")   # PASS behavior preserved
```

As a habit, each refactoring session is:

1. Tests (or examples) pass **before** you start.
2. Capture current output as your "golden" behavior.
3. Make **one** small move (extract, rename, guard clause).
4. Re-run and compare. Same behavior? Repeat with the next move.

---

## ⚠️ Common Mistakes

1. **Refactoring and adding a feature in the same change** - if something
   breaks you can't tell whether the new feature or the cleanup did it. Two
   separate commits keep the blame clear.
2. **Refactoring without a safety net** - "it still looks right" is not
   proof. Without tests or captured output, you are guessing that behavior
   stayed the same.
3. **"While I'm here" scope creep** - a rename becomes a rewrite becomes a
   rewrite of a rewrite. Finish the one move, re-run, commit, then decide.

---

## 📝 Quick Reference

| Move | Reach for it when |
|---|---|
| Extract function | a block does one nameable thing |
| Rename | the name hides what the code does |
| Guard clause | an edge case is buried in nesting |
| Introduce constant | a magic number appears (again) |
| Replace conditional with polymorphism | the same if/else chain repeats everywhere |

---

## 🔍 Key Takeaways

- Refactor in small steps and keep behavior the same.
- Use design principles to guide what to refactor.
- Prefer clarity over cleverness.

---

[Back: Code Smells](../06_code_smells/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
