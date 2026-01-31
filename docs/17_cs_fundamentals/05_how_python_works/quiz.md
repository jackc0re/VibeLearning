# 📝 How Python Works Quiz

Test your understanding of Python internals, bytecode, and the GIL.

---

## Question 1

What is the first step Python takes when executing a .py file?

- A) Directly execute line by line
- B) Compile to machine code
- C) Parse into an Abstract Syntax Tree (AST)
- D) Load from __pycache__

---

## Question 2

What does the `dis` module do?

- A) Disables Python features
- B) Displays bytecode instructions
- C) Disconnects from the network
- D) Distributes Python programs

---

## Question 3

What is the Global Interpreter Lock (GIL)?

- A) A security feature that prevents code execution
- B) A mutex that allows only one thread to execute Python bytecode at a time
- C) A lock that prevents importing modules
- D) A tool for global variable management

---

## Question 4

Which file extension is used for cached Python bytecode?

- A) .pyo
- B) .pyc
- C) .pyd
- D) .pyb

---

## Question 5

What type of virtual machine is the Python Virtual Machine (PVM)?

- A) Register-based
- B) Stack-based
- C) Queue-based
- D) Heap-based

---

## Question 6

Why might threading not speed up a CPU-bound Python program?

- A) Threads don't work in Python
- B) The GIL prevents true parallel execution of Python bytecode
- C) CPU-bound tasks can't use threads in any language
- D) Python threads are deprecated

---

## Question 7

What does constant folding optimization do?

- A) Folds constants into a single file
- B) Evaluates constant expressions at compile time
- C) Removes all constants from code
- D) Compresses the bytecode

---

## Question 8

Which Python implementation does NOT have a GIL?

- A) CPython
- B) PyPy
- C) Jython
- D) All have a GIL

---

## Question 9

What is stored in `__pycache__`?

- A) Source code backups
- B) Compiled bytecode files
- C) Python documentation
- D) Error logs

---

## Question 10

What happens when a module is imported for the second time in the same program?

- A) It's reloaded from disk
- B) It's retrieved from `sys.modules` cache
- C) It's recompiled every time
- D) An error occurs

---

# Answers

<details>
<summary>Click to reveal answers</summary>

## Answer 1
**C) Parse into an Abstract Syntax Tree (AST)**

Python first parses source code into an AST to check for syntax errors, then compiles to bytecode. The AST is an intermediate representation between source code and bytecode.

---

## Answer 2
**B) Displays bytecode instructions**

The `dis` module (disassembler) displays the bytecode instructions for a Python function or code object. It's useful for understanding what Python is actually executing.

---

## Answer 3
**B) A mutex that allows only one thread to execute Python bytecode at a time**

The GIL is a mutex that prevents multiple native threads from executing Python bytecodes at once. It simplifies memory management but limits multi-threaded performance for CPU-bound tasks.

---

## Answer 4
**B) .pyc**

Python caches compiled bytecode in files with the `.pyc` extension, stored in the `__pycache__` directory.

---

## Answer 5
**B) Stack-based**

The Python Virtual Machine uses a stack-based architecture where operations push and pop values from a stack, rather than using registers like some other virtual machines.

---

## Answer 6
**B) The GIL prevents true parallel execution of Python bytecode**

Because of the GIL, only one thread can execute Python bytecode at a time. For CPU-bound tasks, threads run sequentially (with context switching overhead), not in parallel.

---

## Answer 7
**B) Evaluates constant expressions at compile time**

Constant folding optimizes expressions like `2 + 3` to `5` at compile time, so the runtime doesn't need to calculate them.

---

## Answer 8
**C) Jython**

Jython (Python on the JVM) and IronPython (Python on .NET) don't have a GIL because they use the underlying platform's threading model. CPython and PyPy both have a GIL.

---

## Answer 9
**B) Compiled bytecode files**

The `__pycache__` directory contains `.pyc` files which are the compiled bytecode versions of `.py` source files. These are used to speed up subsequent imports.

---

## Answer 10
**B) It's retrieved from `sys.modules` cache**

Python stores imported modules in `sys.modules`. When you import the same module again, Python checks this cache first and reuses the already-loaded module.

</details>

---

## Scoring

- **9-10 correct:** 🏆 Python Internals Expert!
- **7-8 correct:** 👍 Solid understanding
- **5-6 correct:** 📚 Review the material
- **Below 5:** 🔄 Start with the README and examples

---

## Congratulations!

You've completed **Module 17: Computer Science Fundamentals**! 🎉

You've learned about:
- Number systems (binary, octal, hex)
- Bitwise operations
- Boolean logic and gates
- Memory architecture (stack vs heap)
- How Python works internally

**Next:** Continue with [Module 18: Working with APIs](../../18_working_with_apis/README.md) or revisit any topic you want to review.
