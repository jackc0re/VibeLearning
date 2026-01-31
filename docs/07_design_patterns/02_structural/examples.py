"""
Structural Design Patterns - Examples

Demonstrates Adapter, Decorator, and Facade patterns.
Run with:
    python examples.py
"""

# =============================================================================
# ADAPTER
# =============================================================================


class LegacyPayment:
    def pay_cents(self, cents):
        print(f"Paid {cents} cents")


class PaymentAdapter:
    def __init__(self, legacy_payment):
        self.legacy_payment = legacy_payment

    def pay(self, dollars):
        self.legacy_payment.pay_cents(int(dollars * 100))


def demo_adapter():
    print("Adapter demo")
    gateway = PaymentAdapter(LegacyPayment())
    gateway.pay(9.99)


# =============================================================================
# DECORATOR
# =============================================================================


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


def demo_decorator():
    print("\nDecorator demo")
    base = Coffee()
    with_milk = MilkDecorator(base)
    with_milk_sugar = SugarDecorator(with_milk)
    print("Base cost:", base.cost())
    print("With milk:", with_milk.cost())
    print("With milk + sugar:", with_milk_sugar.cost())


# =============================================================================
# FACADE
# =============================================================================


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
    def __init__(self):
        self.auth = AuthService()
        self.orders = OrderService()
        self.payments = PaymentService()

    def checkout(self, user):
        token = self.auth.login(user)
        order = self.orders.create_order(token)
        receipt = self.payments.pay(order)
        return receipt


def demo_facade():
    print("\nFacade demo")
    checkout = CheckoutFacade()
    print(checkout.checkout("maria"))


if __name__ == "__main__":
    demo_adapter()
    demo_decorator()
    demo_facade()
    print("\n✓ Examples complete!")
