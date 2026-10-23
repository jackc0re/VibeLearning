# 🧠 Behavioral Design Patterns

Behavioral patterns focus on **how objects communicate and share responsibilities**. They help you design interactions that are flexible, testable, and easy to change.

---

## ✅ Why Behavioral Patterns Matter

- **Reduce tight coupling** between objects that need to collaborate.
- **Encapsulate behavior** so it can change independently.
- **Make systems extensible** by plugging in new behaviors.

---

## ✅ Common Behavioral Patterns

### 1) Observer

One object (subject) notifies multiple observers when its state changes.

**Analogy:** a video channel. You subscribe once; when a new video is
published, every subscriber hears about it. The channel doesn't know or care
who the subscribers are — it just keeps a list and notifies everyone on it.

```python
class Newsletter:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, fn):
        self._subscribers.append(fn)

    def publish(self, article):
        for fn in self._subscribers:
            fn(article)


news = Newsletter()
news.subscribe(lambda a: print(f"Alice got: {a}"))
news.subscribe(lambda a: print(f"Bob got: {a}"))

news.publish("Design Patterns Weekly")
# Alice got: Design Patterns Weekly
# Bob got: Design Patterns Weekly
```

✅ **Use when:** a state change should fan out to any number of listeners —
UI events, notifications, metrics — without the subject knowing their types.
❌ **Avoid when:** you need guaranteed delivery order, return values, or
retries; `publish` just calls each subscriber and moves on. Also remember to
provide (and use) an `unsubscribe`, or observers pile up and never get
collected.

### 2) Strategy

Encapsulates interchangeable algorithms behind a common interface.

**Analogy:** choosing a route in a maps app. The destination is fixed, but you
pick "fastest", "shortest", or "no highways" — same question, different
algorithm behind it.

✅ Use when: you want to swap logic without changing the caller.

The full worked example is in the next section.

### 3) Command

Encapsulates an action as an object, enabling queues, history, or undo.

**Analogy:** a waiter's order slip. Your request becomes a piece of paper that
can sit in a queue, be handed to another cook, or be reversed — the waiter and
the kitchen never talk directly, they only pass slips.

```python
class Light:
    def __init__(self):
        self.is_on = False

    def on(self):
        self.is_on = True
        return "light on"

    def off(self):
        self.is_on = False
        return "light off"


class LightOn:
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.on()

    def undo(self):
        return self.light.off()


class LightOff:
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.off()

    def undo(self):
        return self.light.on()


class CommandHistory:
    """Remembers executed commands so the last one can be undone."""

    def __init__(self):
        self._done = []

    def execute(self, command):
        result = command.execute()
        self._done.append(command)
        return result

    def undo_last(self):
        if not self._done:
            return "nothing to undo"
        return self._done.pop().undo()


light = Light()
history = CommandHistory()

print(history.execute(LightOn(light)))   # light on
print(history.execute(LightOff(light)))  # light off
print(history.undo_last())               # light on   (undoes the "off")
print(history.undo_last())               # light off  (undoes the "on")
print(history.undo_last())               # nothing to undo
```

✅ **Use when:** actions must be queued, logged, scheduled, or undone — text
editors, macros, job queues.
❌ **Avoid when:** a plain method call is enough; turning every action into a
class adds boilerplate with no payoff.

---

## ✅ Example: Strategy

```python
class StandardShipping:
    def cost(self, total):
        return 5 if total < 50 else 0


class ExpressShipping:
    def cost(self, total):
        return 15


def checkout(total, shipping_strategy):
    return total + shipping_strategy.cost(total)


total = checkout(40, ExpressShipping())   # 55
```

---

## ⚠️ Common Mistakes

1. **Forgetting to unsubscribe observers** - a subject holds strong references
   to its subscribers, so a forgotten observer lives forever (and keeps
   reacting). Offer `unsubscribe(fn)` and call it when a listener is done.
2. **Letting one observer crash the broadcast** - `publish` calls each
   subscriber in turn; if the first raises, the rest never hear the news.
   Wrap each callback in `try/except` when subscribers are less trusted.
3. **Undo that doesn't restore the exact previous state** - "toggle" is not
   undo. `LightOn.undo()` must switch the light *off*, not blindly flip it —
   that's why each command above remembers what to reverse.

---

## 📝 Quick Reference

| Pattern | One-liner | Reach for it when |
|---|---|---|
| Observer | subject broadcasts to subscribers | event-style updates |
| Strategy | swap the algorithm, same interface | interchangeable logic |
| Command | an action as an object | queues, logs, undo |

---

## 🔍 Key Takeaways

- Behavioral patterns structure collaboration between objects.
- Observers react to events without direct coupling.
- Strategies and commands make behavior swappable and reusable.

---

[Back: Structural Patterns](../02_structural/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
