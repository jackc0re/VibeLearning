# 🧱 Separation of Concerns

**Separation of concerns (SoC)** means organizing code so that each part focuses on a distinct responsibility. When responsibilities are mixed, changes become risky because unrelated behavior is tangled together.

---

## ✅ Common “Concerns” in Programs

- **Input/Output:** CLI, HTTP, file reading/writing
- **Business logic:** rules and computations
- **Data access:** databases, APIs
- **Presentation:** formatting, UI, reporting

---

## ✅ Why SoC Matters

- **Easier changes:** UI changes don’t break business rules.
- **Better tests:** business logic can be tested without I/O.
- **Cleaner boundaries:** reduces coupling between parts.

---

## ✅ Example: Split I/O From Logic

Instead of mixing parsing + computation + printing:

```python
def run():
    text = input("Enter numbers: ")
    nums = [int(x) for x in text.split(",")]
    print(sum(nums) / len(nums))
```

Separate concerns:

```python
def parse_numbers(text):
    return [int(x) for x in text.split(",")]

def average(nums):
    return sum(nums) / len(nums)

def run():
    nums = parse_numbers(input("Enter numbers: "))
    print(average(nums))
```

---

## 🔍 Key Takeaways

- Keep I/O at the edges; keep logic pure where possible.
- Group related responsibilities together.
- Boundaries make testing and refactoring safer.

---

[Back: YAGNI Principle](../03_yagni_principle/README.md) | [Next: Coupling and Cohesion](../05_coupling_and_cohesion/README.md)
