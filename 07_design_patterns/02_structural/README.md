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

The full worked example is in the next section.

### 2) Decorator

Adds behavior to objects **dynamically** by wrapping them.

> **Not the same thing as Python's `@decorator` syntax!** A Python decorator is
> a language feature that wraps a *function* (`@cache`, `@staticmethod`). The
> Decorator *pattern* wraps an *object* in another object with the **same
> interface**. They are cousins — both wrap and forward — but here we mean the
> class-design idea.

**Analogy:** ordering a coffee and adding extras. The cup stays a coffee —
milk wraps it (still answers `.cost()`), sugar wraps that. Every wrapper adds a
little to the total without changing the coffee underneath.

```python
class Coffee:
    def cost(self):
        return 3.0


class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 0.5


class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 0.2


base = Coffee()
with_milk = MilkDecorator(base)
with_milk_sugar = SugarDecorator(with_milk)

print(base.cost())           # 3.0
print(with_milk.cost())      # 3.5  (3.0 + 0.5)
print(with_milk_sugar.cost())  # 3.7  (3.0 + 0.5 + 0.2)
```

✅ **Use when:** you want optional, stackable features. Without wrapping, two
extras already mean four subclasses (milk, sugar, milk+sugar, sugar+milk) —
five extras mean a lot more.
❌ **Avoid when:** one or two plain subclasses would cover every case — each
wrapper layer is indirection a reader must follow.

### 3) Facade

Provides a **simple interface** to a complex system.

**Analogy:** a hotel concierge. You ask one person for "a taxi to the airport"
and they coordinate the front desk, the bellhop, and the taxi company. You
never phone each department yourself.

```python
class AuthService:
    def login(self, user):
        return f"Auth:{user}"


class OrderService:
    def create_order(self, user):
        return f"Order({user})"


class PaymentService:
    def pay(self, order_id):
        return f"Paid:{order_id}"


class CheckoutFacade:
    """One call hides three subsystem calls and their required order."""

    def __init__(self):
        self.auth = AuthService()
        self.orders = OrderService()
        self.payments = PaymentService()

    def checkout(self, user):
        token = self.auth.login(user)
        order = self.orders.create_order(token)
        return self.payments.pay(order)


print(CheckoutFacade().checkout("maria"))  # Paid:Order(Auth:maria)
```

✅ **Use when:** clients need one easy entry point — `checkout()`, `render()`,
`backup()` — and shouldn't have to know subsystem call order.
❌ **Avoid when:** the subsystems are already simple; a facade nobody needs is
just an extra layer to maintain.

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
        self.legacy_payment.pay_cents(round(dollars * 100))


gateway = PaymentAdapter(LegacyPayment())
gateway.pay(9.99)   # Paid 999 cents
```

---

## ⚠️ Common Mistakes

1. **Confusing the Decorator pattern with `@decorator` syntax** - `@cache`
   decorates functions; the pattern decorates objects by wrapping them in a
   class with the same interface. Knowing both is useful, mixing the words is
   not.
2. **Wrappers that only forward some methods** - a decorator must offer the
   *whole* interface of what it wraps. If `MilkDecorator` forgets `description`
   but callers use it, the wrapped coffee is unreachable through the wrapper.
3. **Letting the Facade grow its own business logic** - the moment the facade
   starts making decisions instead of forwarding, it becomes a god object.
   Facades translate and simplify; they don't decide.

---

## 📝 Quick Reference

| Pattern | One-liner | Reach for it when |
|---|---|---|
| Adapter | translates one interface into another | integrating legacy or third-party code |
| Decorator | wraps to add behavior, same interface | optional, stackable features |
| Facade | one simple front door for a subsystem | hiding multi-step subsystem calls |

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
