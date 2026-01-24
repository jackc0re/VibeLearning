"""Dependency Management - Examples

Demonstrations:
- inspecting installed packages
- parsing requirements files
- working with package metadata

Run:
    python examples.py
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def demo_list_installed() -> None:
    """Show installed packages using importlib.metadata."""
    print("=== Installed Packages ===\n")

    try:
        from importlib.metadata import distributions

        packages = []
        for dist in distributions():
            packages.append((dist.metadata["Name"], dist.metadata["Version"]))

        # Sort and show first 10
        packages.sort(key=lambda x: x[0].lower())
        print(f"Found {len(packages)} packages. First 10:")
        for name, version in packages[:10]:
            print(f"  {name}=={version}")
        print()
    except ImportError:
        print("importlib.metadata not available (Python 3.8+ required)")
        print()


def demo_package_info() -> None:
    """Show detailed info about a specific package."""
    print("=== Package Information ===\n")

    try:
        from importlib.metadata import metadata, requires

        # Get info about a common package
        package_name = "pip"  # Always installed

        meta = metadata(package_name)
        print(f"Package: {meta['Name']}")
        print(f"Version: {meta['Version']}")
        print(f"Summary: {meta['Summary']}")
        print(f"Author: {meta.get('Author', 'N/A')}")
        print(f"License: {meta.get('License', 'N/A')}")

        # Get dependencies
        deps = requires(package_name)
        if deps:
            print(f"\nDependencies:")
            for dep in deps[:5]:
                print(f"  {dep}")
            if len(deps) > 5:
                print(f"  ... and {len(deps) - 5} more")
        print()
    except ImportError:
        print("importlib.metadata not available")
        print()


def demo_parse_requirement() -> None:
    """Show how to parse requirement strings."""
    print("=== Parsing Requirements ===\n")

    # Example requirement strings
    requirements = [
        "requests",
        "requests==2.28.0",
        "requests>=2.25.0",
        "requests>=2.25.0,<3.0.0",
        "requests~=2.28.0",
        "requests[security]>=2.25.0",
        "package @ https://example.com/package.whl",
    ]

    print("Requirement string examples:")
    for req in requirements:
        parsed = _parse_requirement_simple(req)
        print(f"  {req}")
        print(f"    -> name: {parsed['name']}, specifier: {parsed['specifier']}")
    print()


def _parse_requirement_simple(req: str) -> Dict[str, str]:
    """Simple requirement parser (for demonstration)."""
    import re

    # Remove extras [security] and URL markers
    req = re.sub(r"\[.*?\]", "", req)
    req = req.split("@")[0].strip()

    # Find where version specifier starts
    match = re.match(r"^([A-Za-z0-9_-]+)(.*)?$", req)
    if match:
        return {"name": match.group(1), "specifier": match.group(2) or ""}
    return {"name": req, "specifier": ""}


def demo_requirements_file_format() -> None:
    """Explain requirements.txt format."""
    print("=== requirements.txt Format ===\n")

    example = """# Example requirements.txt
# ========================

# Basic package
requests

# Pinned version (exact)
flask==2.0.0

# Minimum version
pytest>=7.0.0

# Version range
django>=3.2,<4.0

# Compatible release (~= means >=2.28.0, <2.29.0)
numpy~=2.28.0

# Package with extras
requests[security]>=2.25.0

# Include another requirements file
-r base.txt

# Install from git
# git+https://github.com/user/repo.git@v1.0.0

# Install from local path
# ./path/to/local/package

# Environment markers
pywin32>=300 ; sys_platform == 'win32'
"""

    print(example)


def demo_pyproject_toml_format() -> None:
    """Show pyproject.toml structure for dependencies."""
    print("=== pyproject.toml Format ===\n")

    example = """# Example pyproject.toml
[project]
name = "myproject"
version = "1.0.0"
description = "My awesome project"
readme = "README.md"
requires-python = ">=3.9"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "you@example.com"}
]

# Main dependencies
dependencies = [
    "requests>=2.25.0",
    "flask>=2.0.0",
    "pydantic>=2.0",
]

# Optional dependency groups
[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black",
    "mypy",
    "ruff",
]
docs = [
    "sphinx>=4.0",
    "sphinx-rtd-theme",
]

# Entry points (CLI commands)
[project.scripts]
myapp = "myproject.cli:main"
"""

    print(example)


def demo_version_specifiers() -> None:
    """Explain version specifier meanings."""
    print("=== Version Specifiers ===\n")

    specifiers = [
        ("==1.2.3", "Exactly version 1.2.3"),
        ("!=1.2.3", "Any version except 1.2.3"),
        (">=1.2.3", "Version 1.2.3 or higher"),
        ("<=1.2.3", "Version 1.2.3 or lower"),
        (">1.2.3", "Higher than 1.2.3"),
        ("<1.2.3", "Lower than 1.2.3"),
        ("~=1.2.3", "Compatible: >=1.2.3, <1.3.0 (patch updates only)"),
        ("~=1.2", "Compatible: >=1.2.0, <2.0.0 (minor updates only)"),
        (">=1.2,<2.0", "Range: at least 1.2 but below 2.0"),
    ]

    for spec, meaning in specifiers:
        print(f"  {spec:15} -> {meaning}")
    print()


def demo_check_version_match() -> None:
    """Demonstrate version comparison."""
    print("=== Version Comparison ===\n")

    try:
        from packaging import version
        from packaging.specifiers import SpecifierSet

        # Compare versions
        v1 = version.parse("2.0.0")
        v2 = version.parse("2.1.0")
        v3 = version.parse("1.9.9")

        print("Version comparisons:")
        print(f"  2.0.0 < 2.1.0: {v1 < v2}")
        print(f"  2.0.0 > 1.9.9: {v1 > v3}")

        # Check against specifier
        spec = SpecifierSet(">=2.0.0,<3.0.0")
        print(f"\nSpecifier: {spec}")
        for ver_str in ["1.9.9", "2.0.0", "2.5.0", "3.0.0"]:
            v = version.parse(ver_str)
            print(f"  {ver_str} matches: {v in spec}")
        print()

    except ImportError:
        print("'packaging' library not installed")
        print("Install with: pip install packaging")
        print()


def demo_dependency_tree() -> None:
    """Show concept of dependency tree."""
    print("=== Dependency Tree Concept ===\n")

    tree = """
myproject
├── flask>=2.0.0
│   ├── Werkzeug>=2.0.0
│   ├── Jinja2>=3.0.0
│   │   └── MarkupSafe>=2.0
│   ├── itsdangerous>=2.0.0
│   ├── click>=8.0.0
│   └── blinker>=1.0.0
└── requests>=2.25.0
    ├── charset-normalizer>=2.0.0
    ├── idna>=2.5
    ├── urllib3>=1.21.1
    └── certifi>=2017.4.17
"""

    print("Example dependency tree:")
    print(tree)
    print("Use 'pip install pipdeptree' and run 'pipdeptree' to see your tree")
    print()


if __name__ == "__main__":
    demo_list_installed()
    demo_package_info()
    demo_parse_requirement()
    demo_requirements_file_format()
    demo_pyproject_toml_format()
    demo_version_specifiers()
    demo_check_version_match()
    demo_dependency_tree()
