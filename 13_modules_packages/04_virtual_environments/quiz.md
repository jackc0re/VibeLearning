# 🧠 Virtual Environments Quiz

---

## Question 1
What is the main purpose of a virtual environment?

- A) To make Python run faster
- B) To isolate project dependencies from other projects
- C) To enable multiple Python versions on one system
- D) To protect code from viruses

<details>
<summary>Show Answer</summary>

**B)** Virtual environments isolate project dependencies, so each project can have its own versions of packages without conflicts.

</details>

---

## Question 2
Which command creates a virtual environment using Python's built-in module?

- A) `pip install venv myenv`
- B) `python -m venv myenv`
- C) `virtualenv create myenv`
- D) `python --venv myenv`

<details>
<summary>Show Answer</summary>

**B)** `python -m venv myenv` uses the built-in `venv` module to create a virtual environment in the `myenv` directory.

</details>

---

## Question 3
How can you tell if you're inside an activated virtual environment?

- A) `sys.prefix == sys.base_prefix`
- B) `sys.prefix != sys.base_prefix`
- C) Check if `python --version` works
- D) Look for a `venv` folder in your home directory

<details>
<summary>Show Answer</summary>

**B)** When in a venv, `sys.prefix` (current environment) differs from `sys.base_prefix` (base Python installation).

</details>

---

## Question 4
What should you do with the virtual environment directory when using Git?

- A) Commit it to track exact dependencies
- B) Add it to `.gitignore` and use `requirements.txt` instead
- C) Compress it before committing
- D) Store it in a separate branch

<details>
<summary>Show Answer</summary>

**B)** Virtual environments are large and platform-specific. Add `.venv/` to `.gitignore` and track dependencies in `requirements.txt` or `pyproject.toml` instead.

</details>

---

## Question 5
What does the `pyvenv.cfg` file contain?

- A) A list of installed packages
- B) Python source code
- C) Configuration about the virtual environment (base Python path, version)
- D) Activation scripts

<details>
<summary>Show Answer</summary>

**C)** `pyvenv.cfg` contains metadata about the venv, including the path to the base Python interpreter and whether system site-packages are included.

</details>

---

[Back to Virtual Environments README](README.md)
