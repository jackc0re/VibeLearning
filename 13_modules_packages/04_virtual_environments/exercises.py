"""Virtual Environments - Exercises

Goals:
- detect and inspect virtual environments
- understand environment paths
- work with environment configuration

Run with:
    python exercises.py
"""

from __future__ import annotations

import os
import sys
import site
from pathlib import Path
from typing import Dict, List, Optional


# =============================================================================
# EXERCISE 1: Check If In Virtual Environment
# =============================================================================


def exercise_1_is_venv() -> bool:
    """
    Return True if Python is running inside a virtual environment.

    Use sys.prefix and sys.base_prefix comparison.
    """
    return sys.prefix != sys.base_prefix


def exercise_1_get_venv_path() -> Optional[str]:
    """
    Return the path to the current virtual environment, or None if not in one.
    """
    if exercise_1_is_venv():
        return sys.prefix
    return None


# =============================================================================
# EXERCISE 2: Get Site-Packages Directory
# =============================================================================


def exercise_2_get_site_packages() -> Optional[str]:
    """
    Return the path to the site-packages directory where pip installs packages.

    For a venv, this should be inside the venv.
    For system Python, this is the global site-packages.
    Return None if unable to determine.
    """
    packages = site.getsitepackages()
    if packages:
        # Return the first one (usually the most relevant)
        return packages[0]
    return None


def exercise_2_list_installed_packages() -> List[str]:
    """
    Return a sorted list of directories in site-packages
    (each directory typically represents an installed package).

    Only return directories, not files. Exclude __pycache__ and *.dist-info.
    """
    site_packages = exercise_2_get_site_packages()
    if not site_packages or not os.path.isdir(site_packages):
        return []

    packages = []
    for item in os.listdir(site_packages):
        path = os.path.join(site_packages, item)
        if not os.path.isdir(path):
            continue
        if item.startswith("__"):
            continue
        if item.endswith(".dist-info") or item.endswith(".egg-info"):
            continue
        packages.append(item)

    return sorted(packages)


# =============================================================================
# EXERCISE 3: Parse pyvenv.cfg
# =============================================================================


def exercise_3_parse_pyvenv_cfg(venv_path: str) -> Dict[str, str]:
    """
    Parse the pyvenv.cfg file from a virtual environment directory.

    Returns a dict like:
    {
        "home": "/usr/bin",
        "include-system-site-packages": "false",
        "version": "3.11.0"
    }

    Return empty dict if file doesn't exist.
    """
    cfg_path = Path(venv_path) / "pyvenv.cfg"

    if not cfg_path.exists():
        return {}

    result = {}
    with open(cfg_path, "r") as f:
        for line in f:
            line = line.strip()
            if "=" in line:
                key, value = line.split("=", 1)
                result[key.strip()] = value.strip()

    return result


def exercise_3_get_base_python(venv_path: str) -> Optional[str]:
    """
    Get the path to the base Python interpreter from a venv's pyvenv.cfg.

    Returns the 'home' value from pyvenv.cfg, or None if not found.
    """
    cfg = exercise_3_parse_pyvenv_cfg(venv_path)
    return cfg.get("home")


# =============================================================================
# EXERCISE 4: Environment Path Analysis
# =============================================================================


def exercise_4_get_python_paths() -> Dict[str, str]:
    """
    Return a dictionary of important Python paths.

    Keys: "executable", "prefix", "base_prefix", "site_packages"
    """
    sp = exercise_2_get_site_packages()
    return {
        "executable": sys.executable,
        "prefix": sys.prefix,
        "base_prefix": sys.base_prefix,
        "site_packages": sp if sp else "",
    }


def exercise_4_path_is_in_venv(path: str) -> bool:
    """
    Check if a given path is inside the current virtual environment.

    Return False if not in a venv.
    """
    if not exercise_1_is_venv():
        return False

    try:
        path_resolved = Path(path).resolve()
        venv_resolved = Path(sys.prefix).resolve()
        # Check if path is under venv directory
        return str(path_resolved).startswith(str(venv_resolved))
    except (OSError, ValueError):
        return False


# =============================================================================
# EXERCISE 5: Activation Detection
# =============================================================================


def exercise_5_get_activation_info() -> Dict[str, Optional[str]]:
    """
    Return information about environment activation.

    Returns a dict with:
    - "virtual_env": VIRTUAL_ENV env var (or None)
    - "conda_default_env": CONDA_DEFAULT_ENV env var (or None)
    - "path_first_python": First Python directory in PATH (or None)
    """
    return {
        "virtual_env": os.environ.get("VIRTUAL_ENV"),
        "conda_default_env": os.environ.get("CONDA_DEFAULT_ENV"),
        "path_first_python": _find_first_python_in_path(),
    }


def _find_first_python_in_path() -> Optional[str]:
    """Helper to find first directory containing 'python' in PATH."""
    path = os.environ.get("PATH", "")
    sep = ";" if sys.platform == "win32" else ":"

    for directory in path.split(sep):
        if not directory:
            continue
        python_name = "python.exe" if sys.platform == "win32" else "python"
        if os.path.isfile(os.path.join(directory, python_name)):
            return directory

    return None


def exercise_5_is_properly_activated() -> bool:
    """
    Check if the environment appears to be properly activated.

    Criteria:
    - If in a venv, VIRTUAL_ENV should match sys.prefix
    - The first Python in PATH should be in the venv
    """
    if not exercise_1_is_venv():
        return True  # Not in venv, nothing to check

    info = exercise_5_get_activation_info()

    # VIRTUAL_ENV should match
    if info["virtual_env"] != sys.prefix:
        return False

    # First Python in PATH should be in venv
    first_python = info["path_first_python"]
    if first_python:
        return exercise_4_path_is_in_venv(first_python)

    return False


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Virtual Environments Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1: Check If In Virtual Environment
    print("\nExercise 1: Check If In Virtual Environment")
    try:
        is_venv = exercise_1_is_venv()
        venv_path = exercise_1_get_venv_path()

        # Logic check: if is_venv, venv_path should not be None
        ok1 = (is_venv and venv_path is not None) or (not is_venv and venv_path is None)
        print(f"   In venv: {is_venv}")
        print(f"   Venv path: {venv_path}")
        print("  ", "PASS" if ok1 else "FAIL")
        all_passed = all_passed and ok1
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2: Get Site-Packages Directory
    print("\nExercise 2: Get Site-Packages Directory")
    try:
        site_packages = exercise_2_get_site_packages()
        ok1 = site_packages is None or os.path.isdir(site_packages)

        packages = exercise_2_list_installed_packages()
        ok2 = isinstance(packages, list)
        ok3 = packages == sorted(packages)  # Should be sorted

        print(f"   Site-packages: {site_packages}")
        print(f"   Package count: {len(packages)}")

        ok = ok1 and ok2 and ok3
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3: Parse pyvenv.cfg
    print("\nExercise 3: Parse pyvenv.cfg")
    try:
        # Test with current prefix (may or may not have pyvenv.cfg)
        cfg = exercise_3_parse_pyvenv_cfg(sys.prefix)
        ok1 = isinstance(cfg, dict)

        # If in venv, should have data
        if exercise_1_is_venv():
            ok2 = len(cfg) > 0
            base = exercise_3_get_base_python(sys.prefix)
            ok3 = base is not None
            print(f"   Config keys: {list(cfg.keys())}")
            print(f"   Base Python: {base}")
        else:
            ok2 = True
            ok3 = True
            print("   (Not in venv, skipping pyvenv.cfg checks)")

        ok = ok1 and ok2 and ok3
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 4: Environment Path Analysis
    print("\nExercise 4: Environment Path Analysis")
    try:
        paths = exercise_4_get_python_paths()
        ok1 = all(k in paths for k in ["executable", "prefix", "base_prefix", "site_packages"])
        ok2 = paths["executable"] == sys.executable
        ok3 = paths["prefix"] == sys.prefix

        print(f"   Executable: {paths['executable'][:50]}...")

        # Test path_is_in_venv with current executable
        if exercise_1_is_venv():
            ok4 = exercise_4_path_is_in_venv(sys.executable)
        else:
            ok4 = not exercise_4_path_is_in_venv(sys.executable)

        ok = ok1 and ok2 and ok3 and ok4
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 5: Activation Detection
    print("\nExercise 5: Activation Detection")
    try:
        info = exercise_5_get_activation_info()
        ok1 = isinstance(info, dict)
        ok2 = all(k in info for k in ["virtual_env", "conda_default_env", "path_first_python"])

        print(f"   VIRTUAL_ENV: {info['virtual_env']}")
        print(f"   CONDA_DEFAULT_ENV: {info['conda_default_env']}")

        is_activated = exercise_5_is_properly_activated()
        ok3 = isinstance(is_activated, bool)
        print(f"   Properly activated: {is_activated}")

        ok = ok1 and ok2 and ok3
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
