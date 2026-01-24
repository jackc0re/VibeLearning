# 🏠 Virtual Environments

A **virtual environment** is an isolated Python installation that keeps project dependencies separate from other projects and the system Python.

---

## ✅ Why Virtual Environments?

Without virtual environments:
- Project A needs `requests==2.25.0`
- Project B needs `requests==2.28.0`
- **Conflict!** Only one version can be installed globally.

With virtual environments:
- Each project has its own isolated `site-packages`
- No conflicts between projects
- Reproducible installations

---

## ✅ Creating a Virtual Environment

```bash
# Using the built-in venv module (recommended)
python -m venv myenv

# Creates a directory structure:
# myenv/
# ├── bin/           (or Scripts/ on Windows)
# ├── include/
# ├── lib/
# └── pyvenv.cfg
```

---

## ✅ Activating and Deactivating

```bash
# Linux/macOS
source myenv/bin/activate

# Windows (PowerShell)
myenv\Scripts\Activate.ps1

# Windows (CMD)
myenv\Scripts\activate.bat

# Deactivate (any platform)
deactivate
```

When activated:
- `python` points to the venv's Python
- `pip install` installs to the venv's `site-packages`
- Your prompt usually shows `(myenv)` prefix

---

## ✅ Checking Your Environment

```bash
# See which Python is active
which python        # Linux/macOS
where python        # Windows

# Check the environment
python -c "import sys; print(sys.prefix)"

# List installed packages
pip list
```

---

## ✅ Project Workflow

```bash
# 1. Create venv in project folder
cd myproject
python -m venv .venv

# 2. Activate it
source .venv/bin/activate  # or Windows equivalent

# 3. Install dependencies
pip install requests flask

# 4. Save dependencies
pip freeze > requirements.txt

# 5. Work on your project
python app.py

# 6. Deactivate when done
deactivate
```

---

## ✅ Common Conventions

- Name: `.venv` or `venv` (dot prefix hides it on Unix)
- Location: Inside the project directory
- Git: Add `.venv/` to `.gitignore` (don't commit it!)
- Always use a venv per project

---

## ✅ Alternatives to venv

| Tool | Description |
|------|-------------|
| `venv` | Built-in, simple, recommended for most cases |
| `virtualenv` | Third-party, more features, faster |
| `conda` | Full environment manager, great for data science |
| `pyenv` | Manages multiple Python versions |
| `poetry` | Modern dependency + venv management |

---

## 🔍 Key Takeaways

- Always use virtual environments for Python projects.
- `python -m venv .venv` creates an isolated environment.
- Activate before installing packages, deactivate when done.
- Add `.venv/` to `.gitignore`.

---

[Back: Packages](../03_packages/) | [Next: Dependency Management](../05_dependency_management/)
