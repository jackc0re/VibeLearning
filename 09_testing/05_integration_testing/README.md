# 🔗 Integration Testing

Integration tests check that **multiple parts work together**.
They typically cross a boundary: filesystem, database, HTTP, message queue, etc.

Unlike unit tests, integration tests may involve real IO, but should still:

- be deterministic
- clean up after themselves
- be reasonably fast

---

## ✅ What to Integration-Test

- Reading/writing files and parsing
- Calling a database layer
- Using multiple modules together (e.g., parse + validate + transform)

---

## ✅ Good Practices

- Use temporary directories (`tempfile`) for filesystem tests
- Keep test data small and obvious
- Avoid global state; reset or isolate it

---

## 🔍 Key Takeaways

- Integration tests catch bugs that unit tests cannot (wrong wiring, wrong formats).
- Keep them focused on boundaries.
- Still prefer lots of fast unit tests, plus fewer integration tests.

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
