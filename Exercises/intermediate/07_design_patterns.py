"""
Intermediate Exercise 7: Design Patterns
========================================
Implement four classic patterns: Singleton, Factory,
Observer, and Strategy.
"""

print("=" * 50)
print("EXERCISE 7: Design Patterns")
print("=" * 50)


# =============================================================================
# EXERCISE 7.1: Singleton
# =============================================================================
print("\n--- Exercise 7.1: Singleton ---")
"""
Make AppConfig a Singleton: calling AppConfig() must always return
the SAME object.

- Override __new__ to create the instance only once (store it on
  a class attribute such as _instance)
- Give it settings = {} and set(key, value) / get(key, default)
"""


# Your code below:
class AppConfig:
    """Application configuration - exactly one instance."""

    pass


# Test (uncomment after implementing)
# a = AppConfig()
# a.set("theme", "dark")
# b = AppConfig()
# print(a is b)  # True


# =============================================================================
# EXERCISE 7.2: Factory
# =============================================================================
print("\n--- Exercise 7.2: Factory ---")
"""
Build a notification factory:

- Notifier subclasses EmailNotifier and SmsNotifier, each with
  send(message) (printing is fine)
- create_notifier(kind) returns the right object for "email"
  or "sms", and raises ValueError for anything else
"""


# Your code below:
class Notifier:
    """Base class for notifiers."""

    pass


class EmailNotifier(Notifier):
    """Sends notifications by email."""

    pass


class SmsNotifier(Notifier):
    """Sends notifications by text message."""

    pass


def create_notifier(kind):
    """Return a notifier for 'email' or 'sms'."""
    pass


# Test (uncomment after implementing)
# notifier = create_notifier("email")
# notifier.send("Deploy finished")


# =============================================================================
# EXERCISE 7.3: Observer
# =============================================================================
print("\n--- Exercise 7.3: Observer ---")
"""
Build a pub/sub news feed:

- NewsFeed: subscribe(observer), unsubscribe(observer),
  publish(news) calls update(news) on every observer
- EmailSubscriber(address): prints where the story was emailed
- ArchiveSubscriber(): stores every story in self.archive
"""


# Your code below:
class NewsFeed:
    """Subject that notifies observers when news is published."""

    pass


class EmailSubscriber:
    """Observer that 'emails' the news."""

    pass


class ArchiveSubscriber:
    """Observer that stores every story."""

    pass


# Test (uncomment after implementing)
# feed = NewsFeed()
# archive = ArchiveSubscriber()
# feed.subscribe(archive)
# feed.publish("Big story")


# =============================================================================
# EXERCISE 7.4: Strategy
# =============================================================================
print("\n--- Exercise 7.4: Strategy ---")
"""
Make discounts swappable at runtime:

- Discount strategies implement apply(total) -> discounted total
- NoDiscount: full price
- PercentDiscount(percent, threshold=50): percent off when the
  order reaches the threshold
- FixedDiscount(amount, threshold=50): flat amount off when the
  order reaches the threshold
- Checkout(strategy): .total(cart_total) delegates to the strategy
"""


# Your code below:
class NoDiscount:
    """Full price, no discount."""

    pass


class PercentDiscount:
    """Take percent off orders over a threshold."""

    pass


class FixedDiscount:
    """Subtract a flat amount on orders over a threshold."""

    pass


class Checkout:
    """Totals a cart using whatever strategy it is given."""

    pass


# Test (uncomment after implementing)
# checkout = Checkout(PercentDiscount(10))
# print(checkout.total(80.0))


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 7.1
print("\n--- Solution 7.1 ---")


class AppConfig:
    """Application configuration - exactly one instance."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {}
        return cls._instance

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key, default=None):
        return self.settings.get(key, default)


first = AppConfig()
first.set("theme", "dark")
second = AppConfig()
print(f"Same object? {first is second}")
print(f"Second instance sees theme: {second.get('theme')}")

# SOLUTION 7.2
print("\n--- Solution 7.2 ---")


class Notifier:
    """Base class for notifiers."""

    def send(self, message):
        raise NotImplementedError


class EmailNotifier(Notifier):
    """Sends notifications by email."""

    def send(self, message):
        print(f"  email -> {message}")


class SmsNotifier(Notifier):
    """Sends notifications by text message."""

    def send(self, message):
        print(f"  sms   -> {message}")


def create_notifier(kind):
    """Return a notifier for 'email' or 'sms'."""
    notifiers = {"email": EmailNotifier, "sms": SmsNotifier}
    if kind not in notifiers:
        raise ValueError(f"unknown notifier kind: {kind!r}")
    return notifiers[kind]()


for kind in ["email", "sms", "fax"]:
    try:
        notifier = create_notifier(kind)
        notifier.send(f"hello via {kind}")
    except ValueError as exc:
        print(f"  {kind}: rejected ({exc})")

# SOLUTION 7.3
print("\n--- Solution 7.3 ---")


class NewsFeed:
    """Subject that notifies observers when news is published."""

    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def publish(self, news):
        print(f"[feed] Publishing: {news}")
        for observer in list(self._observers):
            observer.update(news)


class EmailSubscriber:
    """Observer that 'emails' the news."""

    def __init__(self, address):
        self.address = address

    def update(self, news):
        print(f"  email -> {self.address}: {news}")


class ArchiveSubscriber:
    """Observer that stores every story."""

    def __init__(self):
        self.archive = []

    def update(self, news):
        self.archive.append(news)


feed = NewsFeed()
mailer = EmailSubscriber("ada@example.com")
archive = ArchiveSubscriber()
feed.subscribe(mailer)
feed.subscribe(archive)

feed.publish("Python 4 announced")
feed.publish("Local teen writes perfect code")
print(f"Archive holds {len(archive.archive)} stories")

feed.unsubscribe(mailer)
feed.publish("Quiet day in tech")
print(f"Archive holds {len(archive.archive)} stories (mailer unsubscribed)")

# SOLUTION 7.4
print("\n--- Solution 7.4 ---")


class NoDiscount:
    """Full price, no discount."""

    def apply(self, total):
        return total


class PercentDiscount:
    """Take percent off orders over a threshold."""

    def __init__(self, percent, threshold=50):
        self.percent = percent
        self.threshold = threshold

    def apply(self, total):
        if total >= self.threshold:
            return round(total * (100 - self.percent) / 100, 2)
        return total


class FixedDiscount:
    """Subtract a flat amount on orders over a threshold."""

    def __init__(self, amount, threshold=50):
        self.amount = amount
        self.threshold = threshold

    def apply(self, total):
        if total >= self.threshold:
            return max(total - self.amount, 0)
        return total


class Checkout:
    """Totals a cart using whatever strategy it is given."""

    def __init__(self, strategy):
        self.strategy = strategy

    def total(self, cart_total):
        return self.strategy.apply(cart_total)


cart_total = 80.0
for strategy in [NoDiscount(), PercentDiscount(10), FixedDiscount(5)]:
    name = strategy.__class__.__name__
    print(f"{name:16s} -> ${Checkout(strategy).total(cart_total)}")

small_order = 20.0
print(f"With a ${small_order} order, PercentDiscount gives "
      f"${Checkout(PercentDiscount(10)).total(small_order)} (threshold not met)")

print("\n" + "=" * 50)
print("Great job! Move on to 08_testing.py")
print("=" * 50)
