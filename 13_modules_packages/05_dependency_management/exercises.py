"""Dependency Management - Exercises

Goals:
- parse requirements files
- work with package metadata
- understand version specifiers

Run with:
    python exercises.py
"""

from __future__ import annotations

import re
from typing import Dict, List, Optional, Tuple


# =============================================================================
# EXERCISE 1: Parse Requirements Line
# =============================================================================


def exercise_1_parse_requirement(line: str) -> Optional[Dict[str, str]]:
    """
    Parse a single requirement line into components.

    Returns a dict with:
    - "name": package name
    - "specifier": version specifier (e.g., ">=2.0.0,<3.0.0") or ""
    - "extras": extras string (e.g., "security,socks") or ""

    Returns None for comments (#), empty lines, or special lines (-r, -e, etc.)

    Examples:
        "requests" -> {"name": "requests", "specifier": "", "extras": ""}
        "requests>=2.0" -> {"name": "requests", "specifier": ">=2.0", "extras": ""}
        "requests[security]>=2.0" -> {"name": "requests", "specifier": ">=2.0", "extras": "security"}
    """
    line = line.strip()

    # Skip empty lines, comments, and special directives
    if not line or line.startswith("#") or line.startswith("-"):
        return None

    # Remove inline comments
    if " #" in line:
        line = line.split(" #")[0].strip()

    # Remove environment markers (e.g., ; sys_platform == 'win32')
    if ";" in line:
        line = line.split(";")[0].strip()

    # Extract extras [...]
    extras = ""
    extras_match = re.search(r"\[([^\]]+)\]", line)
    if extras_match:
        extras = extras_match.group(1)
        line = re.sub(r"\[[^\]]+\]", "", line)

    # Extract name and specifier
    # Package names: letters, numbers, underscores, hyphens, dots
    match = re.match(r"^([A-Za-z0-9._-]+)(.*)?$", line)
    if not match:
        return None

    name = match.group(1)
    specifier = match.group(2).strip() if match.group(2) else ""

    return {"name": name, "specifier": specifier, "extras": extras}


# =============================================================================
# EXERCISE 2: Parse Requirements File Content
# =============================================================================


def exercise_2_parse_requirements(content: str) -> List[Dict[str, str]]:
    """
    Parse entire requirements file content.

    Returns list of parsed requirements (skipping comments, empty lines, etc.)
    """
    results = []
    for line in content.split("\n"):
        parsed = exercise_1_parse_requirement(line)
        if parsed is not None:
            results.append(parsed)
    return results


def exercise_2_extract_package_names(content: str) -> List[str]:
    """
    Extract just the package names from requirements content.

    Returns sorted, unique list of package names (lowercase).
    """
    requirements = exercise_2_parse_requirements(content)
    names = set()
    for req in requirements:
        names.add(req["name"].lower())
    return sorted(names)


# =============================================================================
# EXERCISE 3: Version Comparison
# =============================================================================


def exercise_3_parse_version(version_str: str) -> Tuple[int, ...]:
    """
    Parse a version string into a tuple of integers.

    "1.2.3" -> (1, 2, 3)
    "2.0" -> (2, 0)
    "1.0.0a1" -> (1, 0, 0)  # Ignore pre-release suffixes

    Handles common version formats.
    """
    # Remove common suffixes (a1, b2, rc1, .dev1, etc.)
    version_str = re.split(r"[a-zA-Z]", version_str)[0]
    version_str = version_str.rstrip(".")

    parts = []
    for part in version_str.split("."):
        try:
            parts.append(int(part))
        except ValueError:
            break

    return tuple(parts) if parts else (0,)


def exercise_3_compare_versions(v1: str, v2: str) -> int:
    """
    Compare two version strings.

    Returns:
        -1 if v1 < v2
         0 if v1 == v2
         1 if v1 > v2
    """
    parsed1 = exercise_3_parse_version(v1)
    parsed2 = exercise_3_parse_version(v2)

    # Pad shorter tuple with zeros
    max_len = max(len(parsed1), len(parsed2))
    parsed1 = parsed1 + (0,) * (max_len - len(parsed1))
    parsed2 = parsed2 + (0,) * (max_len - len(parsed2))

    if parsed1 < parsed2:
        return -1
    elif parsed1 > parsed2:
        return 1
    return 0


# =============================================================================
# EXERCISE 4: Version Specifier Matching
# =============================================================================


def exercise_4_matches_specifier(version: str, specifier: str) -> bool:
    """
    Check if a version matches a specifier.

    Supports: ==, !=, >=, <=, >, <
    Does NOT need to support ~= or complex ranges for this exercise.

    Examples:
        matches("2.0.0", ">=2.0.0") -> True
        matches("1.9.0", ">=2.0.0") -> False
        matches("2.0.0", "==2.0.0") -> True
        matches("2.0.0", "!=2.0.0") -> False
    """
    specifier = specifier.strip()

    if not specifier:
        return True  # No specifier = any version

    # Parse operator and version
    match = re.match(r"^(==|!=|>=|<=|>|<)(.+)$", specifier)
    if not match:
        return False

    op = match.group(1)
    spec_version = match.group(2).strip()

    cmp = exercise_3_compare_versions(version, spec_version)

    if op == "==":
        return cmp == 0
    elif op == "!=":
        return cmp != 0
    elif op == ">=":
        return cmp >= 0
    elif op == "<=":
        return cmp <= 0
    elif op == ">":
        return cmp > 0
    elif op == "<":
        return cmp < 0

    return False


def exercise_4_matches_all_specifiers(version: str, specifiers: str) -> bool:
    """
    Check if version matches all comma-separated specifiers.

    Example: matches_all("2.5.0", ">=2.0.0,<3.0.0") -> True
    """
    if not specifiers.strip():
        return True

    for spec in specifiers.split(","):
        spec = spec.strip()
        if spec and not exercise_4_matches_specifier(version, spec):
            return False
    return True


# =============================================================================
# EXERCISE 5: Generate Requirements Content
# =============================================================================


def exercise_5_generate_requirements(
    packages: List[Dict[str, str]], pinned: bool = False
) -> str:
    """
    Generate requirements.txt content from a list of packages.

    Each package dict has: {"name": str, "version": str}

    If pinned=True, use ==version
    If pinned=False, use >=version

    Sort packages alphabetically by name.
    """
    lines = []
    for pkg in sorted(packages, key=lambda p: p["name"].lower()):
        name = pkg["name"]
        version = pkg.get("version", "")
        if version:
            op = "==" if pinned else ">="
            lines.append(f"{name}{op}{version}")
        else:
            lines.append(name)
    return "\n".join(lines)


def exercise_5_filter_dev_packages(
    packages: List[Dict[str, str]], dev_patterns: List[str]
) -> Tuple[List[Dict[str, str]], List[Dict[str, str]]]:
    """
    Split packages into main and dev dependencies.

    dev_patterns is a list of package name patterns (case-insensitive).
    A package is "dev" if its name contains any pattern.

    Common dev patterns: ["pytest", "black", "mypy", "ruff", "coverage"]

    Returns: (main_packages, dev_packages)
    """
    main = []
    dev = []

    for pkg in packages:
        name_lower = pkg["name"].lower()
        is_dev = any(pattern.lower() in name_lower for pattern in dev_patterns)
        if is_dev:
            dev.append(pkg)
        else:
            main.append(pkg)

    return main, dev


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Dependency Management Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1: Parse Requirements Line
    print("\nExercise 1: Parse Requirements Line")
    try:
        # Test basic package
        r1 = exercise_1_parse_requirement("requests")
        ok1 = r1 == {"name": "requests", "specifier": "", "extras": ""}

        # Test with version
        r2 = exercise_1_parse_requirement("requests>=2.25.0")
        ok2 = r2["name"] == "requests" and r2["specifier"] == ">=2.25.0"

        # Test with extras
        r3 = exercise_1_parse_requirement("requests[security]>=2.0")
        ok3 = r3["name"] == "requests" and r3["extras"] == "security"

        # Test comments return None
        r4 = exercise_1_parse_requirement("# comment")
        ok4 = r4 is None

        # Test -r returns None
        r5 = exercise_1_parse_requirement("-r base.txt")
        ok5 = r5 is None

        ok = ok1 and ok2 and ok3 and ok4 and ok5
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2: Parse Requirements File Content
    print("\nExercise 2: Parse Requirements File Content")
    try:
        content = """
# My requirements
requests>=2.25.0
flask==2.0.0
-r base.txt
pytest  # dev dependency
"""
        parsed = exercise_2_parse_requirements(content)
        ok1 = len(parsed) == 3  # requests, flask, pytest

        names = exercise_2_extract_package_names(content)
        ok2 = names == ["flask", "pytest", "requests"]

        ok = ok1 and ok2
        print("  ", "PASS" if ok else "FAIL")
        if not ok:
            print(f"    Parsed count: {len(parsed)}")
            print(f"    Names: {names}")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3: Version Comparison
    print("\nExercise 3: Version Comparison")
    try:
        # Parse version
        ok1 = exercise_3_parse_version("1.2.3") == (1, 2, 3)
        ok2 = exercise_3_parse_version("2.0") == (2, 0)
        ok3 = exercise_3_parse_version("1.0.0a1") == (1, 0, 0)

        # Compare versions
        ok4 = exercise_3_compare_versions("1.0.0", "2.0.0") == -1
        ok5 = exercise_3_compare_versions("2.0.0", "2.0.0") == 0
        ok6 = exercise_3_compare_versions("2.1.0", "2.0.0") == 1
        ok7 = exercise_3_compare_versions("1.10.0", "1.9.0") == 1

        ok = ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 4: Version Specifier Matching
    print("\nExercise 4: Version Specifier Matching")
    try:
        ok1 = exercise_4_matches_specifier("2.0.0", ">=2.0.0") is True
        ok2 = exercise_4_matches_specifier("1.9.0", ">=2.0.0") is False
        ok3 = exercise_4_matches_specifier("2.0.0", "==2.0.0") is True
        ok4 = exercise_4_matches_specifier("2.0.1", "==2.0.0") is False
        ok5 = exercise_4_matches_specifier("2.0.0", "!=2.0.0") is False

        # Test range
        ok6 = exercise_4_matches_all_specifiers("2.5.0", ">=2.0.0,<3.0.0") is True
        ok7 = exercise_4_matches_all_specifiers("3.0.0", ">=2.0.0,<3.0.0") is False

        ok = ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 5: Generate Requirements Content
    print("\nExercise 5: Generate Requirements Content")
    try:
        packages = [
            {"name": "flask", "version": "2.0.0"},
            {"name": "requests", "version": "2.28.0"},
        ]

        # Test pinned
        pinned = exercise_5_generate_requirements(packages, pinned=True)
        ok1 = "flask==2.0.0" in pinned and "requests==2.28.0" in pinned

        # Test not pinned
        unpinned = exercise_5_generate_requirements(packages, pinned=False)
        ok2 = "flask>=2.0.0" in unpinned

        # Test sorting (flask before requests)
        ok3 = pinned.index("flask") < pinned.index("requests")

        # Test filter
        all_pkgs = [
            {"name": "flask", "version": "2.0.0"},
            {"name": "pytest", "version": "7.0.0"},
            {"name": "requests", "version": "2.28.0"},
            {"name": "black", "version": "23.0.0"},
        ]
        main, dev = exercise_5_filter_dev_packages(all_pkgs, ["pytest", "black"])
        ok4 = len(main) == 2 and len(dev) == 2
        ok5 = all(p["name"] in ["flask", "requests"] for p in main)

        ok = ok1 and ok2 and ok3 and ok4 and ok5
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
