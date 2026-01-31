# 🧪 Why Testing?

Testing is a way to **prove** (with executable checks) that your program behaves as expected.
Good tests act like a **safety net**: you can change code and quickly detect regressions.

---

## ✅ What Testing Gives You

- **Fast feedback**: find bugs in seconds, not days.
- **Regression protection**: if a bug comes back, tests catch it.
- **Better design**: testable code tends to be modular and easier to reason about.
- **Living documentation**: tests show how your code is intended to be used.

---

## ✅ Types of Tests (Typical Pyramid)

1. **Unit tests**
   - Test small pieces (functions/classes)
   - Fast, isolated, no network/files

2. **Integration tests**
   - Test multiple parts working together
   - Example: read a file and parse JSON

3. **End-to-end (E2E) tests**
   - Test the whole system (UI/API + database)
   - Slowest, most expensive to maintain

---

## ✅ What Makes a Test “Good”

- **Readable**: you understand what it checks in 10 seconds.
- **Deterministic**: same result every run (no randomness/time/network).
- **Focused**: one behavior per test.
- **Fast**: the full suite should run quickly.

---

## 🔍 Key Takeaways

- Tests help you ship changes with confidence.
- Unit tests are the foundation; add integration tests at boundaries.
- Deterministic and readable beats “clever”.

---

[Next: Unit Testing →](../02_unit_testing/README.md)

