"""\
Test-Driven Development - Examples

This file demonstrates a tiny TDD journey for a function `slugify`.
We simulate "tests first" using plain asserts.

Run with:
    python examples.py
"""


import re


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug.

Rules:
  - lowercase
  - trim whitespace
  - spaces/underscores become '-'
  - remove non-alphanumeric except '-'
  - collapse multiple '-' into one
"""
    text = text.strip().lower().replace("_", " ")
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^a-z0-9-]", "", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def run_demo_tests():
    # "Red" would start with just one of these tests, then expand.
    assert slugify("Hello World") == "hello-world"
    assert slugify("  Multiple   spaces ") == "multiple-spaces"
    assert slugify("Clean__This") == "clean-this"
    assert slugify("100% Real!!!") == "100-real"
    assert slugify("---Already---") == "already"
    print("OK - TDD demo tests passed")


if __name__ == "__main__":
    run_demo_tests()

