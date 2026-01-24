# 📋 Dependency Management

**Dependency management** is how you track, install, and update the external packages your project needs. Good dependency management ensures reproducible builds.

---

## ✅ pip - The Package Installer

```bash
# Install a package
pip install requests

# Install a specific version
pip install requests==2.28.0

# Install with version constraints
pip install "requests>=2.25.0,<3.0.0"

# Install from requirements file
pip install -r requirements.txt

# Show installed packages
pip list

# Show package info
pip show requests

# Uninstall a package
pip uninstall requests
```

---

## ✅ requirements.txt

The traditional way to track dependencies:

```text
# requirements.txt
requests==2.28.0
flask>=2.0.0
pytest>=7.0.0
numpy~=1.23.0
```

**Version specifiers:**
- `==2.28.0` - Exact version
- `>=2.25.0` - Minimum version
- `<3.0.0` - Maximum version
- `~=1.23.0` - Compatible release (1.23.x but not 1.24.0)
- `>=2.0,<3.0` - Range

**Generate from current environment:**
```bash
pip freeze > requirements.txt
```

---

## ✅ pyproject.toml (Modern Standard)

The modern way to configure Python projects (PEP 518, 621):

```toml
[project]
name = "myproject"
version = "1.0.0"
description = "My awesome project"
requires-python = ">=3.9"
dependencies = [
    "requests>=2.25.0",
    "flask>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black",
    "mypy",
]
```

Install with:
```bash
pip install .              # Install dependencies
pip install ".[dev]"       # Include dev dependencies
```

---

## ✅ Dependency Groups

Organize dependencies by purpose:

```text
# requirements/base.txt
requests>=2.25.0
flask>=2.0.0

# requirements/dev.txt
-r base.txt
pytest>=7.0.0
black

# requirements/prod.txt
-r base.txt
gunicorn>=20.0.0
```

---

## ✅ Pinning vs Ranges

| Approach | Example | Pros | Cons |
|----------|---------|------|------|
| Pinned | `requests==2.28.0` | Reproducible | May miss security fixes |
| Range | `requests>=2.25,<3` | Gets updates | May break unexpectedly |
| Compatible | `requests~=2.28` | Balance | Limited flexibility |

**Best practice:** Pin in production, use ranges in libraries.

---

## ✅ Lock Files

Lock files record exact versions of all dependencies (including transitive):

- `pip freeze > requirements.lock`
- `pip-tools`: generates `requirements.txt` from `requirements.in`
- `poetry.lock`, `Pipfile.lock`: managed by respective tools

---

## ✅ Modern Tools

| Tool | Description |
|------|-------------|
| **pip-tools** | Compile `requirements.in` to `requirements.txt` |
| **Poetry** | All-in-one dependency + packaging management |
| **pipenv** | Combines pip + venv with `Pipfile` |
| **uv** | Fast pip/pip-tools replacement in Rust |

---

## 🔍 Key Takeaways

- Use `requirements.txt` or `pyproject.toml` to track dependencies.
- Pin versions for reproducible deployments.
- Separate dev dependencies from production dependencies.
- Use lock files to capture exact versions including transitive deps.

---

[Back: Virtual Environments](../04_virtual_environments/) | [Back to Module 13](../README.md)
