# 🏗️ Creational Design Patterns

Creational patterns focus on **how objects are created**. They help you control construction so that code stays flexible, testable, and easy to extend.

---

## ✅ Why Creational Patterns Matter

- **Encapsulate creation logic** so the rest of your code stays simple.
- **Reduce coupling** to specific classes or constructors.
- **Improve testability** by swapping implementations easily.

---

## ✅ Common Creational Patterns

### 1) Singleton

Ensures a class has **only one instance** and provides a global access point.

**Analogy:** a town has exactly one post office. Everyone in town uses the same
one — nobody builds a private post office in their garage.

```python
class AppConfig:
    _instance = None

    def __new__(cls):
        # First call creates the instance; every later call reuses it.
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


a = AppConfig()
b = AppConfig()
a.theme = "dark"

print(a is b)   # True -> both names point at one shared object
print(b.theme)  # dark -> the change is visible through any name
```

> **Pythonic note:** a module-level instance (like `CONFIG = _Config()` in this
> topic's [examples.py](examples.py)) is often all you need — a module is only
> imported once, so its top-level objects are naturally shared.

✅ **Use when:** a resource must exist exactly once — app config, a logger, a
connection pool.
❌ **Avoid when:** you only want "convenient global access". Hidden global state
makes tests order-dependent; passing the object explicitly is usually better.

### 2) Factory (Simple/Factory Method)

Delegates object creation to a function or method based on input.

**Analogy:** a pharmacy counter. You describe what you need ("something for a
headache") and the pharmacist hands you the right product — you don't wander
the aisles picking a brand yourself.

✅ **Use when:** the caller shouldn't know (or care) which concrete class it
gets — the choice depends on input, config, or environment.
❌ **Avoid when:** there is only one implementation — a plain constructor is
simpler.

The full worked example is in the next section.

### 3) Builder

Creates complex objects **step-by-step**, often with a fluent API.

**Analogy:** ordering at a sandwich bar. You call out choices one at a time
("wheat bread, add cheese, no onions") and the builder assembles the final
sandwich — instead of one giant order form demanding every answer up front.

```python
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
        return self            # returning self is what enables chaining

    def charts(self, enabled=True):
        self._include_charts = enabled
        return self

    def summary(self, enabled=True):
        self._include_summary = enabled
        return self

    def build(self):
        return Report(self._title, self._include_charts, self._include_summary)


report = ReportBuilder().title("Q1 Results").charts().summary().build()
print(report)  # Report(title='Q1 Results', charts=True, summary=True)
```

✅ **Use when:** an object has many optional parts and "telescoping"
constructors (`Report(title, charts, summary, appendix, footer, ...)`) become
unreadable.
❌ **Avoid when:** the object has one or two fields — a plain constructor is
less code.

---

## ✅ Example: Simple Factory

```python
class EmailNotification:
    def send(self, msg):
        print(f"Email: {msg}")


class SMSNotification:
    def send(self, msg):
        print(f"SMS: {msg}")


def notification_factory(kind):
    if kind == "email":
        return EmailNotification()
    if kind == "sms":
        return SMSNotification()
    raise ValueError("Unknown notification type")


notifier = notification_factory("email")
notifier.send("Hello!")   # Email: Hello!
```

The caller only knows `send()` — the factory decides which class to build.

---

## ⚠️ Common Mistakes

1. **Treating a Singleton as a global dumping ground** - once any code can
   write `AppConfig().settings[...]`, every module depends on that shared state
   and test order starts to matter. Keep what lives in a singleton small and
   read-mostly.
2. **Building a Builder for a two-field object** - the builder is five times
   the code of the plain constructor. Reach for it only when optional fields
   genuinely multiply.
3. **Forgetting `return self` in builder methods** - chaining then breaks with
   `AttributeError`, because `.charts()` returned `None` instead of the builder.

---

## 📝 Quick Reference

| Pattern | One-liner | Reach for it when |
|---|---|---|
| Singleton | exactly one shared instance | config, logger, connection pool |
| Factory | pick the class at runtime | which class to build depends on input |
| Builder | assemble step by step, then `build()` | many optional fields |

---

## 🔍 Key Takeaways

- Creational patterns manage object creation complexity.
- Factories centralize construction decisions.
- Builders help when many optional fields are needed.

---

[Next: Structural Patterns →](../02_structural/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
