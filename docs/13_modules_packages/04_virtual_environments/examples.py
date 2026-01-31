"""Virtual Environments - Examples

Demonstrations:
- inspecting the current Python environment
- understanding sys.prefix and site-packages
- programmatically creating virtual environments

Run:
    python examples.py
"""

from __future__ import annotations

import os
import sys
import site
import sysconfig
from pathlib import Path


def demo_environment_info() -> None:
    """Show information about the current Python environment."""
    print("=== Current Environment Info ===\n")

    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    print()


def demo_prefix_paths() -> None:
    """Explain sys.prefix, sys.base_prefix, and sys.exec_prefix."""
    print("=== Prefix Paths ===\n")

    print(f"sys.prefix:      {sys.prefix}")
    print(f"sys.base_prefix: {sys.base_prefix}")
    print(f"sys.exec_prefix: {sys.exec_prefix}")
    print()

    # Check if we're in a virtual environment
    in_venv = sys.prefix != sys.base_prefix
    print(f"In virtual environment: {in_venv}")

    if in_venv:
        print(f"  venv location: {sys.prefix}")
        print(f"  base Python: {sys.base_prefix}")
    print()


def demo_site_packages() -> None:
    """Show where packages are installed."""
    print("=== Site-Packages Locations ===\n")

    # Get site-packages directories
    site_packages = site.getsitepackages()
    print("System site-packages:")
    for sp in site_packages:
        print(f"  {sp}")

    # User site-packages
    user_site = site.getusersitepackages()
    print(f"\nUser site-packages: {user_site}")
    print(f"  Enabled: {site.ENABLE_USER_SITE}")
    print()


def demo_check_venv() -> None:
    """Show different ways to check if in a virtual environment."""
    print("=== Detecting Virtual Environment ===\n")

    # Method 1: Compare prefixes
    method1 = sys.prefix != sys.base_prefix
    print(f"Method 1 (prefix comparison): {method1}")

    # Method 2: Check for VIRTUAL_ENV environment variable
    venv_var = os.environ.get("VIRTUAL_ENV")
    method2 = venv_var is not None
    print(f"Method 2 (VIRTUAL_ENV env var): {method2}")
    if venv_var:
        print(f"  VIRTUAL_ENV = {venv_var}")

    # Method 3: Look for pyvenv.cfg file
    pyvenv_cfg = Path(sys.prefix) / "pyvenv.cfg"
    method3 = pyvenv_cfg.exists()
    print(f"Method 3 (pyvenv.cfg exists): {method3}")
    print()


def demo_path_configuration() -> None:
    """Show how paths are configured."""
    print("=== Path Configuration ===\n")

    # sysconfig provides detailed path info
    paths = sysconfig.get_paths()
    print("Key paths from sysconfig:")
    for key in ["stdlib", "purelib", "scripts", "include"]:
        if key in paths:
            print(f"  {key}: {paths[key]}")
    print()


def demo_create_venv_programmatically() -> None:
    """Show how to create a venv from Python code."""
    print("=== Creating Venv Programmatically ===\n")

    import venv

    # venv.EnvBuilder is the class that creates environments
    print("venv.EnvBuilder options:")
    print("  - system_site_packages: Include system packages")
    print("  - clear: Delete existing venv first")
    print("  - symlinks: Use symlinks instead of copies")
    print("  - with_pip: Install pip in the venv")

    # Example (not actually creating to avoid side effects):
    print("\nExample code to create a venv:")
    print("""
    import venv

    # Create a builder
    builder = venv.EnvBuilder(
        system_site_packages=False,
        clear=True,
        with_pip=True
    )

    # Create the environment
    builder.create('/path/to/new/venv')
    """)
    print()


def demo_venv_structure() -> None:
    """Explain the structure of a virtual environment."""
    print("=== Virtual Environment Structure ===\n")

    print("Typical venv directory structure:")
    print("""
    .venv/
    ├── bin/                    # (Scripts/ on Windows)
    │   ├── activate            # Activation script (bash)
    │   ├── activate.csh        # Activation script (csh)
    │   ├── activate.fish       # Activation script (fish)
    │   ├── Activate.ps1        # Activation script (PowerShell)
    │   ├── pip                 # pip executable
    │   ├── pip3
    │   ├── python              # Python symlink/copy
    │   └── python3
    ├── include/                # Header files (for building C extensions)
    ├── lib/
    │   └── pythonX.Y/
    │       └── site-packages/  # Installed packages go here
    └── pyvenv.cfg              # Configuration file
    """)

    print("pyvenv.cfg contents (example):")
    print("""
    home = /usr/bin
    include-system-site-packages = false
    version = 3.11.0
    """)
    print()


def demo_sys_path() -> None:
    """Show how sys.path differs in a venv."""
    print("=== sys.path in Current Environment ===\n")

    print("Current sys.path:")
    for i, path in enumerate(sys.path[:7]):  # Show first 7
        marker = "(empty = current dir)" if path == "" else ""
        print(f"  {i}: {path} {marker}")

    if len(sys.path) > 7:
        print(f"  ... and {len(sys.path) - 7} more entries")
    print()


def demo_environment_variables() -> None:
    """Show relevant environment variables."""
    print("=== Environment Variables ===\n")

    vars_to_check = [
        "VIRTUAL_ENV",
        "PYTHONPATH",
        "PYTHONHOME",
        "PATH",
    ]

    for var in vars_to_check:
        value = os.environ.get(var)
        if value:
            # Truncate long values
            display = value[:60] + "..." if len(value) > 60 else value
            print(f"{var}: {display}")
        else:
            print(f"{var}: (not set)")
    print()


if __name__ == "__main__":
    demo_environment_info()
    demo_prefix_paths()
    demo_site_packages()
    demo_check_venv()
    demo_path_configuration()
    demo_venv_structure()
    demo_sys_path()
    demo_environment_variables()
    demo_create_venv_programmatically()
