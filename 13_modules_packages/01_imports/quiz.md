# 🧠 Imports Quiz

---

## Question 1
What is the difference between `import math` and `from math import sqrt`?

- A) No difference, they work exactly the same
- B) `import math` loads the whole module; `from math import sqrt` loads only sqrt
- C) `import math` creates a namespace; `from math import sqrt` adds sqrt directly to current namespace
- D) `from math import sqrt` is faster because it loads less code

<details>
<summary>Show Answer</summary>

**C)** Both load the entire module, but `import math` keeps it in the `math` namespace (access via `math.sqrt`), while `from math import sqrt` binds `sqrt` directly in the current namespace.

</details>

---

## Question 2
Where does Python look first when you `import mymodule`?

- A) The standard library
- B) Site-packages directory
- C) The current directory (or script's directory)
- D) PYTHONPATH environment variable

<details>
<summary>Show Answer</summary>

**C)** Python checks the current directory first, then PYTHONPATH, then standard library, then site-packages.

</details>

---

## Question 3
What does `sys.modules` contain?

- A) List of all available modules
- B) Cache of already imported modules
- C) List of module search paths
- D) Configuration for the import system

<details>
<summary>Show Answer</summary>

**B)** `sys.modules` is a dictionary that caches all modules that have been imported, so subsequent imports use the cached version.

</details>

---

## Question 4
Why is `from module import *` generally discouraged?

- A) It's slower than other import styles
- B) It pollutes the namespace and makes it hard to track where names come from
- C) It doesn't work with third-party packages
- D) It imports too little code

<details>
<summary>Show Answer</summary>

**B)** Star imports bring all public names into your namespace, making it unclear where functions come from and potentially causing name collisions.

</details>

---

## Question 5
What happens if you import the same module twice?

- A) The module code runs twice
- B) Python raises an ImportError
- C) The second import uses the cached version from sys.modules
- D) The second import overwrites the first

<details>
<summary>Show Answer</summary>

**C)** Python caches modules in `sys.modules` after the first import. Subsequent imports return the cached module without re-executing the code.

</details>

---

[Back to Imports README](README.md)
