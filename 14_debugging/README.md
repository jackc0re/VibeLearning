# 🔍 Module 14: Debugging

Debugging is the process of finding and fixing **bugs** (defects) in your code. It's a critical skill that separates productive developers from frustrated ones.

This module covers:
- **Print debugging** - The simplest and often most effective approach
- **Using debuggers** - Step through code interactively with `pdb`
- **Reading tracebacks** - Understand Python's error messages
- **Common bugs** - Recognize and fix frequent mistakes

> **Estimated Time:** 5-7 hours
> **Prerequisites:** Modules 01-08
> **Level:** ⭐⭐⭐ Intermediate

---

## 📚 Topics Covered

| # | Topic | Description | Key Concepts |
|---|-------|-------------|--------------|
| 01 | [Print Debugging](01_print_debugging/) | Strategic print statements | `print()`, f-strings, logging |
| 02 | [Using Debuggers](02_using_debuggers/) | Interactive debugging with pdb | `breakpoint()`, stepping, inspection |
| 03 | [Reading Tracebacks](03_reading_tracebacks/) | Understanding error messages | stack traces, exception chains |
| 04 | [Common Bugs](04_common_bugs/) | Frequent mistakes and fixes | off-by-one, mutation, scope issues |

---

## 🎯 Learning Goals

By the end of this module, you should be able to:

- Use **print statements** strategically to trace program flow.
- Navigate the **Python debugger (pdb)** to step through code.
- Read and interpret **tracebacks** to locate bugs quickly.
- Recognize **common bug patterns** and know how to fix them.
- Develop a systematic **debugging mindset**.

---

## 📂 Module Structure

```
14_debugging/
├── README.md
├── 01_print_debugging/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 02_using_debuggers/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 03_reading_tracebacks/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
└── 04_common_bugs/
    ├── README.md
    ├── examples.py
    ├── exercises.py
    └── quiz.md
```

---

## 🧠 The Debugging Mindset

1. **Reproduce** - Can you make the bug happen consistently?
2. **Isolate** - What's the smallest code that shows the problem?
3. **Understand** - What did you expect vs. what happened?
4. **Fix** - Change the code to correct the behavior.
5. **Verify** - Does the fix work? Did it break anything else?

---

## 💡 Debugging Strategies

| Strategy | When to Use |
|----------|-------------|
| Print debugging | Quick checks, simple bugs |
| Debugger (pdb) | Complex logic, need to inspect state |
| Rubber duck | Explaining code reveals assumptions |
| Binary search | Narrow down where bug occurs |
| Read the docs | API misunderstanding |
| Take a break | Fresh eyes see more |

---

**Start here:** [01_print_debugging](01_print_debugging/)
