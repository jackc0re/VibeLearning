"""
Try/Except/Finally - Examples

Demonstrates catching exceptions, else blocks, and cleanup with finally.
Run with:
    python examples.py
"""


def demo_basic_try_except():
    print("Basic try/except demo")
    inputs = ["5", "oops"]
    for value in inputs:
        try:
            number = int(value)
            print(f"  Parsed {value!r} -> {number}")
        except ValueError:
            print(f"  Could not parse {value!r}")


def demo_else_finally():
    print("\nElse/finally demo")
    file = None
    try:
        file = open("temp_demo.txt", "w", encoding="utf-8")
        file.write("hello")
    except OSError as exc:
        print("  Failed to write:", exc)
    else:
        print("  Write succeeded")
    finally:
        if file:
            file.close()
            print("  File closed")


def demo_multiple_exceptions():
    print("\nMultiple exceptions demo")
    data = {"total": 0}
    try:
        result = data["count"] / data["total"]
        print("  Result:", result)
    except (KeyError, ZeroDivisionError) as exc:
        print("  Handled error:", exc)


if __name__ == "__main__":
    demo_basic_try_except()
    demo_else_finally()
    demo_multiple_exceptions()
    print("\n✓ Examples complete!")
