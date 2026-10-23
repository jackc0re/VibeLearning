# 🕵️ Code Smells

A **code smell** is a warning sign that code might be hard to maintain. Smells aren’t necessarily bugs — they’re clues that design could be improved.

---

## ✅ Common Code Smells

- **Duplicated code** (DRY violation)
- **Long function** (does too much)
- **God object** (one class knows/does everything)
- **Too many parameters** (hard to understand and call)
- **Feature envy** (one object uses another’s data too much)
- **Primitive obsession** (strings/ints used where a type would help)
- **Shotgun surgery** (small change requires many edits)

---

## ✅ Why Smells Matter

- They predict **future pain**: bugs, slow changes, fragile tests.
- They guide refactoring: you don’t refactor randomly — you refactor to remove specific smells.

---

## ✅ Smells Are Contextual

A smell might be fine when:

- The code is tiny and disposable.
- Performance constraints require a trade-off.
- You’re in the middle of a transition (temporary duplication).

The key is being intentional.

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
