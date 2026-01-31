# 🧠 Packages Quiz

---

## Question 1
What makes a directory a Python package?

- A) Having at least one `.py` file
- B) Having a `setup.py` file
- C) Having an `__init__.py` file
- D) Being listed in `sys.path`

<details>
<summary>Show Answer</summary>

**C)** A directory becomes a package when it contains an `__init__.py` file (which can be empty). Python 3.3+ also supports namespace packages without `__init__.py`, but traditional packages require it.

</details>

---

## Question 2
What does a relative import like `from ..utils import helper` mean?

- A) Import from the current directory's utils module
- B) Import from the parent package's utils module
- C) Import from the utils package in site-packages
- D) Import from a module two levels up in the file system

<details>
<summary>Show Answer</summary>

**B)** Two dots (`..`) mean "go up one package level." So from `myapp.sub.module`, `..utils` resolves to `myapp.utils`.

</details>

---

## Question 3
When does the code in `__init__.py` execute?

- A) When Python starts
- B) When any module in the package is imported
- C) When the package itself is imported
- D) Only when explicitly called

<details>
<summary>Show Answer</summary>

**C)** `__init__.py` executes when you import the package (e.g., `import mypackage`). Importing a submodule also triggers it if the package wasn't already imported.

</details>

---

## Question 4
How can you tell if an imported module is a package or a regular module?

- A) Packages have `__package__` attribute, modules don't
- B) Packages have `__path__` attribute, regular modules don't
- C) Packages have a `.pkg` extension
- D) Check if `type(module) == 'package'`

<details>
<summary>Show Answer</summary>

**B)** Packages have a `__path__` attribute (a list of paths where submodules can be found). Regular modules don't have this attribute.

</details>

---

## Question 5
Why would you define imports in `__init__.py`?

- A) To make the package load faster
- B) To hide implementation details and provide a clean public API
- C) It's required for the package to work
- D) To prevent circular imports

<details>
<summary>Show Answer</summary>

**B)** By importing key items in `__init__.py`, you let users write `from mypackage import Thing` instead of `from mypackage.deep.module import Thing`. This creates a cleaner API and hides internal structure.

</details>

---

[Back to Packages README](README.md)
