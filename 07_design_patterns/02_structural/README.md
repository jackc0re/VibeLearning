# 🧱 Structural Design Patterns

Structural patterns focus on **how objects and classes are composed** to form larger structures. They help you build systems that are flexible, maintainable, and easy to extend without changing existing code.

---

## ✅ Why Structural Patterns Matter

- **Improve flexibility** by wrapping or adapting existing components.
- **Reduce coupling** between parts of the system.
- **Add features** without modifying existing classes.

---

## ✅ Common Structural Patterns

### 1) Adapter
Makes one interface compatible with another.

✅ Use when: you need to integrate a legacy or third‑party class.

### 2) Decorator
Adds behavior to objects **dynamically** by wrapping them.

✅ Use when: you want optional features without subclass explosion.

### 3) Facade
Provides a **simple interface** to a complex system.

✅ Use when: clients should only see a small, easy entry point.

---

## ✅ Example: Adapter

```python
class LegacyPayment:
    def pay_cents(self, cents):
        print(f"Paid {cents} cents")


class PaymentAdapter:
    def __init__(self, legacy_payment):
        self.legacy_payment = legacy_payment

    def pay(self, dollars):
        self.legacy_payment.pay_cents(int(dollars * 100))


gateway = PaymentAdapter(LegacyPayment())
gateway.pay(9.99)
```

---

## 🔍 Key Takeaways

- Structural patterns organize how parts fit together.
- Adapters translate interfaces, decorators extend behavior.
- Facades simplify complex subsystems.

---

[Next: Behavioral Patterns →](../03_behavioral/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
