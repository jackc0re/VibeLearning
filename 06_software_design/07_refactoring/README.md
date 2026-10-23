# 🛠️ Refactoring

**Refactoring** is improving the internal structure of code **without changing what it does**. The goal is to make code easier to understand and safer to modify.

---

## ✅ When to Refactor

- When you spot repeated code (DRY)
- When a function/class is doing too much (low cohesion)
- When adding a feature feels risky (high coupling)
- After fixing a bug (so it doesn’t come back)

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
