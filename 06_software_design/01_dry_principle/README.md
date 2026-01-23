# 🧩 DRY Principle (Don't Repeat Yourself)

**DRY** means: *every piece of knowledge should have a single, unambiguous, authoritative representation in the system.* In practice, it’s about reducing duplication so that when requirements change, you change code in **one place**, not five.

---

## ✅ What Counts as Duplication?

Duplication isn’t only copy/paste.

- **Copy/paste code** (same logic repeated)
- **Parallel logic** (same idea expressed differently in multiple places)
- **Duplicated rules** (e.g., validation constraints repeated in UI + API + DB)

---

## ✅ Why DRY Matters

- **Fewer bugs:** Fix once, benefit everywhere.
- **Faster changes:** Requirements change constantly.
- **Clearer intent:** Shared logic becomes a named concept.

---

## ⚠️ DRY vs “Over-Abstraction”

DRY is not the same as “make everything generic”.

- Good DRY: Extract shared logic with a clear name.
- Bad DRY: Create complex helper layers that hide simple behavior.

A useful rule: if two pieces of code are identical *by accident* and likely to diverge soon, it may be okay to keep them separate.

---

## ✅ Example: Refactor Duplication

Before (duplicated discounts):

```python
def vip_price(price):
    return price * 0.8

def student_price(price):
    return price * 0.8
```

After (single source of truth):

```python
def apply_discount(price, percent):
    return price * (1 - percent / 100)

vip_price = lambda p: apply_discount(p, 20)
student_price = lambda p: apply_discount(p, 20)
```

---

## 🔍 Key Takeaways

- DRY reduces repeated knowledge, not just repeated lines.
- Centralize rules that must stay consistent.
- Don’t over-abstract; keep the simplest shared design that works.

---

[Next: KISS Principle](../02_kiss_principle/README.md)
