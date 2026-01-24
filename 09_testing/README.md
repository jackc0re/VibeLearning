# ✅ Module 09: Testing

Testing is how we gain confidence that code works **now** and still works **after changes**.
This module focuses on practical testing skills using Python's built-in `unittest` library and the popular third-party framework `pytest`.

> **Estimated Time:** 8-10 hours  \
> **Prerequisites:** Module 01 (Foundations), Module 05 (Functional Programming)  \
> **Level:** ⭐⭐⭐ Intermediate

---

## 📚 Topics Covered

| # | Topic | Description | Key Concepts |
|---|-------|-------------|--------------|
| 01 | [Why Testing](01_why_testing/) | What testing is and why it's valuable | confidence, regression, fast feedback |
| 02 | [Unit Testing](02_unit_testing/) | Testing small units of logic | arrange/act/assert, `unittest`, `pytest` |
| 03 | [Test-Driven Development](03_test_driven_development/) | Writing tests before code | red/green/refactor, small steps |
| 04 | [Mocking](04_mocking/) | Replacing slow/unreliable dependencies | `unittest.mock`, stubs, fakes |
| 05 | [Integration Testing](05_integration_testing/) | Testing multiple components together | boundaries, fixtures, test data |

---

## 🎯 Learning Goals

By the end of this module, you should be able to:

- Explain the difference between **unit**, **integration**, and **end-to-end** tests.
- Write small, readable tests with clear assertions.
- Use `pytest` basics (test functions, assertions, fixtures) and/or Python `unittest`.
- Apply TDD to implement code in safe, incremental steps.
- Use mocks for network/time/randomness/IO dependencies.

---

## 🧰 Recommended Setup (Optional)

This repo does not require extra dependencies, but if you want to use `pytest`:

```bash
pip install pytest
```

---

## 📂 Module Structure

```
09_testing/
├── README.md
├── 01_why_testing/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 02_unit_testing/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 03_test_driven_development/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 04_mocking/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
└── 05_integration_testing/
    ├── README.md
    ├── examples.py
    ├── exercises.py
    └── quiz.md
```

---

**Ready to start? Begin with [01_why_testing](01_why_testing/)!**

