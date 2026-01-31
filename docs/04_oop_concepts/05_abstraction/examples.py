"""
05_abstraction/examples.py

Demonstrating Abstract Base Classes (ABCs).
"""

from abc import ABC, abstractmethod

# -----------------------------------------------------------------------------
# 1. Standard Abstract Base Class
# -----------------------------------------------------------------------------
print("\n--- 1. Abstract Base Class ---")

class PaymentProcessor(ABC):
    
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    @abstractmethod
    def refund_payment(self, amount):
        pass
    
    def log_transaction(self, message):
        # Concrete method in abstract class (shared logic)
        print(f"[LOG]: {message}")

# class GenericProcessor(PaymentProcessor):
#     pass
# p = GenericProcessor() 
# TypeError: Can't instantiate abstract class GenericProcessor with abstract methods...

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        self.log_transaction(f"Processing PayPal payment of ${amount}")
        print("Redirecting to PayPal...")

    def refund_payment(self, amount):
        self.log_transaction(f"Refunding ${amount} via PayPal")

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        self.log_transaction(f"Processing Credit Card payment of ${amount}")
        print("Charging credit card via Stripe...")
        
    def refund_payment(self, amount):
        self.log_transaction(f"Refunding ${amount} via Stripe")

# Usage
def checkout(processor, cost):
    processor.process_payment(cost)

paypal = PayPalProcessor()
stripe = StripeProcessor()

checkout(paypal, 50)
checkout(stripe, 100)


# -----------------------------------------------------------------------------
# 2. Abstract Properties
# -----------------------------------------------------------------------------
print("\n--- 2. Abstract Properties ---")

class Device(ABC):
    @property
    @abstractmethod
    def power_usage(self):
        pass

class Laptop(Device):
    def __init__(self, watts):
        self._watts = watts

    @property
    def power_usage(self):
        return self._watts

class Phone(Device):
    @property
    def power_usage(self):
        return 5  # Fixed value

l = Laptop(65)
p = Phone()

print(f"Laptop power: {l.power_usage}W")
print(f"Phone power: {p.power_usage}W")
