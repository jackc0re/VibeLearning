# 🏗️ SOLID Principles

SOLID is an acronym for five design principles that make object-oriented code
easier to change, easier to test, and harder to break. Each one is a rule of
thumb, not a law of physics — but following them saves you from the classic
"one tiny change breaks five unrelated features" trap.

> Every principle below has a **runnable demonstration** in
> [examples.py](examples.py) — run it while you read.

---

## 1. Single Responsibility Principle (SRP)

> **"A class should have one job — one reason to change."**

**Analogy:** In a restaurant, the chef cooks, the cashier handles money, and
the waiter carries plates. If one person did all three, every menu change
would drag all three jobs into the chaos. Classes work the same way.

```python
# BEFORE: one class, three reasons to change
class Order:
    def calculate_total(self): ...
    def save_to_database(self): ...         # changes when the database changes
    def send_confirmation_email(self): ...  # changes when email rules change

# AFTER: each class has exactly one job
class Order: ...            # order logic only
class OrderRepository: ...  # the ONLY class that knows about the database
class EmailService: ...     # the ONLY class that knows about email
```

- **Bad**: a `User` class that holds logic, saves itself to the database,
  AND sends its own welcome email.
- **Good**: `User` (logic), `UserRepository` (database), `EmailService` (email).

## 2. Open/Closed Principle (OCP)

> **"Open for extension, closed for modification."**

**Analogy:** A power strip: you plug in new devices without rewiring the
wall. New behavior should plug into your code without you editing (and
re-testing) the old parts.

```python
# BEFORE: every new shape means editing this if/elif chain again
def area(shape):
    if isinstance(shape, Rectangle):
        return shape.width * shape.height
    elif isinstance(shape, Circle):
        return 3.14 * shape.radius ** 2
    # ...forever

# AFTER: new shapes plug in; the calculator never changes
class Shape(ABC):
    @abstractmethod
    def area(self): ...

class AreaCalculator:
    def total_area(self, shapes):
        return sum(s.area() for s in shapes)   # works for every future Shape
```

Adding `Triangle(Shape)` later touches **zero** lines of `AreaCalculator`.

## 3. Liskov Substitution Principle (LSP)

> **"A subclass must work anywhere its parent class works."**

**Analogy:** If a recipe says "add any bird", a penguin should be fine —
but only if "bird" never promised flying. A subclass keeps every promise
its parent made; otherwise code that trusted the parent breaks.

```python
# BEFORE: Bird promises fly(), but Penguin is a Bird that cannot fly
class Bird:
    def fly(self): ...

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins cannot fly!")

make_it_fly(Penguin())   # crashes: the substitution broke the caller

# AFTER: the base promise is just "move"; only flying birds add fly()
class Animal: ...               # promises move()
class FlyingBird(Animal): ...   # adds fly()
class Penguin(Animal): ...      # adds swim() -- no broken promises
```

## 4. Interface Segregation Principle (ISP)

> **"No class should be forced to implement methods it does not use."**

**Analogy:** Don't hand a guest a 40-page menu when they only want coffee.
Several small menus beat one giant menu that forces everyone to pretend.

```python
# BEFORE: one fat interface forces a basic printer to fake faxing
class OfficeMachine(ABC):
    @abstractmethod
    def print_doc(self): ...
    @abstractmethod
    def scan_doc(self): ...   # a basic printer cannot scan!
    @abstractmethod
    def fax_doc(self): ...    # a basic printer cannot fax!

# AFTER: small interfaces; classes take only what they need
class Printer(ABC):
    @abstractmethod
    def print_doc(self): ...

class Scanner(ABC):
    @abstractmethod
    def scan_doc(self): ...

class AllInOne(Printer, Scanner): ...   # implements both
class BasicPrinter(Printer): ...        # implements only printing
```

## 5. Dependency Inversion Principle (DIP)

> **"Depend on abstractions, not on concrete classes."**

**Analogy:** Your laptop charger depends on the *socket standard*, not on a
specific power plant. Swap the power source and the charger doesn't care.
High-level logic should plug into a "socket" (an abstraction) too.

```python
# BEFORE: the service builds its own dependency -- welded to email
class NotificationService:
    def __init__(self):
        self.sender = EmailSender()      # hardcoded, cannot swap

# AFTER: both sides depend on a Notifier abstraction
class Notifier(ABC):
    @abstractmethod
    def send(self, message): ...

class NotificationService:
    def __init__(self, notifier):        # the "socket"
        self.notifier = notifier

service = NotificationService(EmailNotifier())   # or SmsNotifier() -- no edits
```

Passing the dependency in from outside is called **dependency injection**.

---

### A note on `ABC` and `@abstractmethod`

`ABC` with `@abstractmethod` is Python's way of saying "every subclass MUST
implement this method" (it comes from the standard-library `abc` module).
See [Abstraction](../05_abstraction/README.md) for a beginner-friendly primer.

---

## ⚠️ Common Mistakes

1. **Applying SOLID to everything, always** — a 20-line script does not need
   five classes. These principles pay off as code grows; splitting too early
   just adds indirection (see [YAGNI](../../06_software_design/03_yagni_principle/README.md)).
2. **Confusing "many methods" with "many responsibilities"** — a class can
   have several related methods and still have one reason to change. Split
   classes along *reasons to change*, not by counting methods.
3. **Inheriting because "it is one in real life"** — a square IS-A rectangle
   in geometry, but if `Square` cannot behave like `Rectangle` in code
   (changing width must also change height), the inheritance is a lie. That
   is exactly the LSP violation shown above.
4. **God interfaces** — an ABC with ten unrelated `@abstractmethod`s forces
   every subclass to implement all ten, even the ones that make no sense
   for it. Split the interface (ISP).
5. **Hardcoding dependencies inside `__init__`** — `self.db = PostgresDB()`
   deep inside a class makes swapping and testing painful. Accept the
   dependency as a parameter instead (DIP).

---

## 📝 Quick Reference

| Letter | Principle | One-line rule | Smell you are breaking it |
|---|---|---|---|
| **S** | Single Responsibility | one class, one job | "this class handles X, Y, and Z" |
| **O** | Open/Closed | extend by adding, not editing | growing `if/elif` + `isinstance` chains |
| **L** | Liskov Substitution | subclasses keep the parent's promises | subclass raises errors where the parent worked |
| **I** | Interface Segregation | small, focused interfaces | forced methods that raise or do nothing |
| **D** | Dependency Inversion | depend on abstractions | `__init__` builds its own concrete helpers |

---

[Return to Module Overview](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
