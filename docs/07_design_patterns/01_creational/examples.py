"""
Creational Design Patterns - Examples

Demonstrates Singleton, Simple Factory, and Builder patterns.
Run with:
    python examples.py
"""

# =============================================================================
# SINGLETON (simple module-level approach)
# =============================================================================


class _Config:
    def __init__(self):
        self.settings = {"theme": "dark", "retries": 3}


CONFIG = _Config()  # single shared instance


def demo_singleton():
    print("Singleton demo")
    a = CONFIG
    b = CONFIG
    b.settings["retries"] = 5
    print("Same instance:", a is b)
    print("Config settings:", a.settings)


# =============================================================================
# SIMPLE FACTORY
# =============================================================================


class EmailNotification:
    def send(self, message):
        print(f"Email -> {message}")


class SMSNotification:
    def send(self, message):
        print(f"SMS -> {message}")


def notification_factory(kind):
    if kind == "email":
        return EmailNotification()
    if kind == "sms":
        return SMSNotification()
    raise ValueError("Unknown notification type")


def demo_factory():
    print("\nFactory demo")
    notifier = notification_factory("email")
    notifier.send("Welcome!")


# =============================================================================
# BUILDER
# =============================================================================


class Report:
    def __init__(self, title, include_charts, include_summary):
        self.title = title
        self.include_charts = include_charts
        self.include_summary = include_summary

    def __repr__(self):
        return (
            f"Report(title={self.title!r}, charts={self.include_charts}, "
            f"summary={self.include_summary})"
        )


class ReportBuilder:
    def __init__(self):
        self._title = "Untitled"
        self._include_charts = False
        self._include_summary = False

    def title(self, value):
        self._title = value
        return self

    def charts(self, enabled=True):
        self._include_charts = enabled
        return self

    def summary(self, enabled=True):
        self._include_summary = enabled
        return self

    def build(self):
        return Report(self._title, self._include_charts, self._include_summary)


def demo_builder():
    print("\nBuilder demo")
    report = (
        ReportBuilder()
        .title("Q1 Results")
        .charts(True)
        .summary(True)
        .build()
    )
    print(report)


if __name__ == "__main__":
    demo_singleton()
    demo_factory()
    demo_builder()
    print("\n✓ Examples complete!")
