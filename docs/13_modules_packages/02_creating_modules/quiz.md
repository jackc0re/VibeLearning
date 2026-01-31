# 🧠 Creating Modules Quiz

---

## Question 1
What is the value of `__name__` when a Python file is run directly (not imported)?

- A) The filename without `.py`
- B) `"__main__"`
- C) `"module"`
- D) `None`

<details>
<summary>Show Answer</summary>

**B)** When a file is run directly, `__name__` is set to `"__main__"`. When imported, it's set to the module name.

</details>

---

## Question 2
What does `__all__` control in a module?

- A) Which functions can be called
- B) What gets imported with `from module import *`
- C) Which names are visible to other modules
- D) What shows up in `dir(module)`

<details>
<summary>Show Answer</summary>

**B)** `__all__` is a list that defines what names are exported when someone uses `from module import *`. It doesn't prevent direct imports of other names.

</details>

---

## Question 3
What naming convention indicates a name is "private" in Python?

- A) Using the `private` keyword
- B) Starting with double underscore `__`
- C) Starting with single underscore `_`
- D) Ending with underscore `_`

<details>
<summary>Show Answer</summary>

**C)** A single leading underscore (e.g., `_helper`) is the convention for private/internal names. Double underscores trigger name mangling in classes, which is different.

</details>

---

## Question 4
When does module-level code execute?

- A) Every time the module is imported
- B) Only when the module is run directly
- C) Once, the first time the module is imported
- D) Never, only function code executes

<details>
<summary>Show Answer</summary>

**C)** Module-level code runs once during the first import. Subsequent imports use the cached module from `sys.modules`.

</details>

---

## Question 5
Why use `if __name__ == "__main__":` at the end of a module?

- A) To make the code run faster
- B) To hide implementation details
- C) To allow the file to work both as a script and as an importable module
- D) To prevent syntax errors

<details>
<summary>Show Answer</summary>

**C)** This pattern lets you put script code (tests, demos, CLI) that only runs when the file is executed directly, while still allowing the file to be imported as a module without running that code.

</details>

---

[Back to Creating Modules README](README.md)
