# ✅ Unit Testing

Unit tests check **small pieces of code** in isolation.
They should run fast and avoid external dependencies (network, filesystem, real time).

---

## ✅ Two Common Tools

### 1) `unittest` (built-in)

- Comes with Python.
- Uses test classes and methods.
- Great when you can't install extra dependencies.

### 2) `pytest` (third-party)

- Very popular in the Python ecosystem.
- Uses simple `assert` statements.
- Excellent output and fixtures.

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

