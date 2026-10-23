# 🕵️ Code Smells

A **code smell** is a warning sign that code might be hard to maintain. Smells aren't necessarily bugs — they're clues that design could be improved.

---

## ✅ Common Code Smells

- **Duplicated code** (DRY violation)
- **Long function** (does too much)
- **God object** (one class knows/does everything)
- **Too many parameters** (hard to understand and call)
- **Feature envy** (one object uses another's data too much)
- **Primitive obsession** (strings/ints used where a type would help)
- **Shotgun surgery** (small change requires many edits)

---

## ✅ Smells in Code

### 1) Long function — does too much

```python
def checkout(items, tax_rate, coupon=None):
    if not items:
        return "No items"
    subtotal = 0.0
    for name, price in items:
        if price < 0:
            return "Invalid price"
        subtotal += price
    total = subtotal * (1 + tax_rate)
    if coupon == "SAVE10":
        total *= 0.9
    return f"Total: ${total:.2f}"
```

Why it smells: validation, totals, discounts, and formatting are mixed — you
can't test or reuse any one of them alone.

### 2) Duplicated code

```python
def email_total(items):
    total = 0
    for _, price in items:
        total += price * 1.1          # tax logic, copy #1
    return round(total, 2)


def report_total(items):
    total = 0
    for _, price in items:
        total += price * 1.1          # same tax logic, copy #2
    return round(total, 2)
```

Why it smells: change the tax rate in one place and the other copy silently
stays wrong. Extract one shared function and call it from both.

### 3) Magic numbers

```python
def shipping_cost(weight):
    return weight * 0.5 + 5           # what are 0.5 and 5?
```

Why it smells: unexplained constants force readers to guess — and invite
inconsistency when someone "fixes" one copy but not another. Name them:

```python
RATE_PER_KG = 0.5
BASE_FEE = 5


def shipping_cost(weight):
    return weight * RATE_PER_KG + BASE_FEE
```

### 4) Feature envy

```python
class Report:
    def __init__(self, user):
        self.user = user

    def summary(self):
        # Reaches into user's data again and again...
        return f"{self.user.name.upper()} from {self.user.city}"
```

Why it smells: `Report` cares about user data more than `Report`'s own. Move
the logic next to the data it envies — for example a `User.display_name()`
method.

---

## ✅ Why Smells Matter

- They predict **future pain**: bugs, slow changes, fragile tests.
- They guide refactoring: you don't refactor randomly — you refactor to remove specific smells.

---

## ✅ Smells Are Contextual

A smell might be fine when:

- The code is tiny and disposable.
- Performance constraints require a trade-off.
- You're in the middle of a transition (temporary duplication).

The key is being intentional.

---

## ⚠️ Common Mistakes

1. **Treating every smell as a bug** - smells are hints, not errors. Code that
   smells but works and rarely changes can be left alone.
2. **Refactoring every smell immediately** - context matters. A "long" 40-line
   function in a throwaway script is fine; the same function in the payment
   path deserves a split.
3. **Chasing smells with big rewrites** - smells are removed by small, safe
   steps (see [Refactoring](../07_refactoring/README.md)), not by rewriting a
   module from scratch on a Friday.

---

## 📝 Quick Reference

| Smell | Looks like | First move |
|---|---|---|
| Duplicated code | same block in two places | extract a shared function |
| Long function | many concerns in one body | extract function |
| Magic numbers | unexplained constants | introduce named constants |
| Feature envy | method keeps using another object's data | move method to that object |
| God object | one class knows everything | split responsibilities |

---

## 🔍 Key Takeaways

- Smells are symptoms, not diagnoses.
- Use smells to start design conversations.
- Many smells can be reduced through small, safe refactors.

---

[Back: Coupling and Cohesion](../05_coupling_and_cohesion/README.md) | [Next: Refactoring](../07_refactoring/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
