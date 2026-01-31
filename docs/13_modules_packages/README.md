# 📦 Module 13: Modules & Packages

As your Python projects grow, you need to **organize code** into reusable, maintainable pieces. This module teaches you how Python's module and package system works.

In Python:
- A **module** is a single `.py` file containing definitions
- A **package** is a directory of modules with an `__init__.py`
- **Virtual environments** isolate project dependencies
- **Dependency management** tracks what packages your project needs

> **Estimated Time:** 6-8 hours
> **Prerequisites:** Modules 01-05
> **Level:** ⭐⭐⭐ Intermediate

---

## 📚 Topics Covered

| # | Topic | Description | Key Concepts |
|---|-------|-------------|--------------|
| 01 | [Imports](01_imports/) | How Python finds and loads modules | `import`, `from`, `as`, `sys.path` |
| 02 | [Creating Modules](02_creating_modules/) | Writing reusable modules | `__name__`, `__all__`, module design |
| 03 | [Packages](03_packages/) | Organizing modules into packages | `__init__.py`, subpackages, relative imports |
| 04 | [Virtual Environments](04_virtual_environments/) | Isolating project dependencies | `venv`, activation, isolation |
| 05 | [Dependency Management](05_dependency_management/) | Managing external packages | `pip`, `requirements.txt`, `pyproject.toml` |

---

## 🎯 Learning Goals

By the end of this module, you should be able to:

- Understand the **import system** and how Python finds modules.
- Create your own **reusable modules** with clean APIs.
- Structure larger projects using **packages**.
- Set up and use **virtual environments** for project isolation.
- Manage **dependencies** effectively with pip and requirements files.

---

## 📂 Module Structure

```
13_modules_packages/
├── README.md
├── 01_imports/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 02_creating_modules/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 03_packages/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 04_virtual_environments/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
└── 05_dependency_management/
    ├── README.md
    ├── examples.py
    ├── exercises.py
    └── quiz.md
```

---

## 🔗 Why This Matters

Real-world Python projects are rarely single files. You need:

- **Code reuse** - Don't repeat yourself across files
- **Organization** - Group related functionality together
- **Isolation** - Keep project dependencies separate
- **Reproducibility** - Others can install the same packages

This module teaches the standard Python practices used in professional development.

---

**Start here:** [01_imports](01_imports/)
