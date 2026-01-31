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

✅ Use when: you need a single shared resource (config, logger).  
⚠️ Watch out: too much global state can hurt testability.

### 2) Factory (Simple/Factory Method)
Delegates object creation to a function or method based on input.

✅ Use when: you want to create related objects without hard-coding classes.

### 3) Builder
Creates complex objects **step-by-step**, often with a fluent API.

✅ Use when: objects have many optional parts or configurations.

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
notifier.send("Hello!")
```

---

## 🔍 Key Takeaways

- Creational patterns manage object creation complexity.
- Factories centralize construction decisions.
- Builders help when many optional fields are needed.

---

[Next: Structural Patterns →](../02_structural/README.md)
