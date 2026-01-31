# 🎭 Mocking

Mocking is replacing a dependency with a controlled fake so your test can be:

- **Fast** (no network/disk)
- **Deterministic** (no randomness/time)
- **Focused** (test only your logic)

In Python, the standard tool is `unittest.mock`.

---

## ✅ When to Mock

- External APIs / network calls
- Current time (`datetime.now()`)
- Randomness (`random.random()`)
- Filesystem access
- Slow functions

---

## ✅ What NOT to Mock (Usually)

- Your own logic (you want to test it)
- Simple value objects
- Too many internal calls (tests become brittle)

---

## 🔍 Key Takeaways

- Mock the *boundary*, not the core logic.
- Keep tests readable: the fake should be obvious.
- If mocking gets complicated, consider redesigning.

---

[Next: Integration Testing →](../05_integration_testing/README.md)

