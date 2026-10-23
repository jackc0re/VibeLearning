# ✅ Unit Testing

Unit tests check **small pieces of code** in isolation.
They should run fast and avoid external dependencies (network, filesystem, real time).

---

## ✅ The Tool: `unittest` (built-in)

- Comes with Python: `import unittest`, nothing to install.
- Uses test classes and `test_*` methods.
- Ships assertion helpers (`assertEqual`, `assertRaises`, ...) and its own runner
  (`python -m unittest`).

> **Aside:** `pytest` is the most common third-party alternative - you will meet it in
> real projects; this repo needs nothing installed. Plain `assert` statements work
> without it, as `examples.py` shows.

---

## ✅ Arrange / Act / Assert (AAA)

Most unit tests follow a simple pattern:

1) **Arrange**: set up inputs
2) **Act**: call the function
3) **Assert**: check the result

---

## ✅ What to Unit Test

- Business rules and pure logic
- Edge cases (empty input, boundaries)
- Error paths (invalid input)

---

## 🔍 Key Takeaways

- Unit tests are the fastest and cheapest tests.
- Keep unit tests independent and deterministic.
- Prefer small functions with clear inputs/outputs.

---

[Next: Test-Driven Development →](../03_test_driven_development/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
