"""
YAGNI Principle - Examples

Demonstrates avoiding speculative abstractions until requirements demand them.
Run with:
    python examples.py
"""

# =============================================================================
# EXAMPLE 1: START SIMPLE
# =============================================================================


def save_note_simple(store, title, text):
    """Simple storage: store notes in a dict."""
    store[title] = text


# =============================================================================
# EXAMPLE 2: DON'T OVERBUILD
# =============================================================================


def format_report_simple(items):
    """A report format that matches today's requirement."""
    lines = ["REPORT"]
    for name, value in items:
        lines.append(f"- {name}: {value}")
    return "\n".join(lines)


# =============================================================================
# DEMONSTRATIONS
# =============================================================================


def demo_yagni():
    print("=" * 60)
    print("YAGNI: You Aren't Gonna Need It")
    print("=" * 60)

    store = {}
    save_note_simple(store, "todo", "Refactor later")
    save_note_simple(store, "idea", "Ship something useful")
    print("Stored notes:")
    for k, v in store.items():
        print(f"  {k} -> {v}")

    print("\nSimple report:")
    report = format_report_simple([("users", 10), ("errors", 1)])
    print(report)

    print("\nYAGNI reminder: build the interface when you have")
    print("multiple real backends or real format requirements.")


if __name__ == "__main__":
    demo_yagni()
    print("\n✓ Examples complete!")
