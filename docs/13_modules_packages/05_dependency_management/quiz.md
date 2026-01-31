# 🧠 Dependency Management Quiz

---

## Question 1
What does `pip freeze` do?

- A) Stops pip from running
- B) Outputs installed packages with exact versions
- C) Locks packages so they can't be updated
- D) Removes all installed packages

<details>
<summary>Show Answer</summary>

**B)** `pip freeze` outputs a list of installed packages with their exact versions in `package==version` format, suitable for creating a `requirements.txt` file.

</details>

---

## Question 2
What does the version specifier `~=1.4.0` mean?

- A) Exactly version 1.4.0
- B) Any version starting with 1.4 (>=1.4.0, <1.5.0)
- C) Any version greater than 1.4.0
- D) Any version less than 1.4.0

<details>
<summary>Show Answer</summary>

**B)** The `~=` (compatible release) specifier allows patch updates but not minor/major updates. `~=1.4.0` means >=1.4.0 and <1.5.0.

</details>

---

## Question 3
What is the modern standard file for declaring Python project dependencies?

- A) setup.py
- B) requirements.txt
- C) pyproject.toml
- D) package.json

<details>
<summary>Show Answer</summary>

**C)** `pyproject.toml` (defined in PEP 518, 621) is the modern standard for Python project configuration including dependencies. While `requirements.txt` is still widely used, `pyproject.toml` is the recommended approach.

</details>

---

## Question 4
Why should you pin dependency versions in production?

- A) To make the code run faster
- B) To ensure reproducible builds with known-working versions
- C) To reduce file size
- D) It's required by pip

<details>
<summary>Show Answer</summary>

**B)** Pinning versions (e.g., `requests==2.28.0`) ensures everyone gets the exact same dependencies, making builds reproducible and avoiding surprises from unexpected updates.

</details>

---

## Question 5
What is a "transitive dependency"?

- A) A package that's installed temporarily
- B) A dependency of your dependency (indirect dependency)
- C) A package that only works on certain platforms
- D) A dependency that changes frequently

<details>
<summary>Show Answer</summary>

**B)** Transitive dependencies are packages that your direct dependencies depend on. For example, if you install `flask`, you also get `werkzeug`, `jinja2`, etc. as transitive dependencies.

</details>

---

[Back to Dependency Management README](README.md)
