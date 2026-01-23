"""
Behavioral Design Patterns - Examples

Demonstrates Observer, Strategy, and Command patterns.
Run with:
    python examples.py
"""

# =============================================================================
# OBSERVER
# =============================================================================


class Newsletter:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, fn):
        self._subscribers.append(fn)

    def publish(self, article):
        for fn in self._subscribers:
            fn(article)


def demo_observer():
    print("Observer demo")
    news = Newsletter()
    news.subscribe(lambda a: print(f"Alice got: {a}"))
    news.subscribe(lambda a: print(f"Bob got: {a}"))
    news.publish("Design Patterns Weekly")


# =============================================================================
# STRATEGY
# =============================================================================


class StandardShipping:
    def cost(self, total):
        return 5 if total < 50 else 0


class ExpressShipping:
    def cost(self, total):
        return 15


def checkout(total, shipping_strategy):
    return total + shipping_strategy.cost(total)


def demo_strategy():
    print("\nStrategy demo")
    print("Standard:", checkout(40, StandardShipping()))
    print("Express:", checkout(40, ExpressShipping()))


# =============================================================================
# COMMAND
# =============================================================================


class Light:
    def __init__(self):
        self.is_on = False

    def on(self):
        self.is_on = True
        return "light on"

    def off(self):
        self.is_on = False
        return "light off"


class Command:
    def execute(self):
        raise NotImplementedError


class LightOn(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.on()


class LightOff(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.off()


def demo_command():
    print("\nCommand demo")
    light = Light()
    on = LightOn(light)
    off = LightOff(light)
    print(on.execute())
    print(off.execute())


if __name__ == "__main__":
    demo_observer()
    demo_strategy()
    demo_command()
    print("\n✓ Examples complete!")
