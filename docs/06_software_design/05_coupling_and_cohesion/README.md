# 🔗 Coupling and Cohesion

Two big design qualities:

- **Coupling:** how strongly one part depends on another.
- **Cohesion:** how well the responsibilities inside a part belong together.

Great designs aim for **low coupling** and **high cohesion**.

---

## ✅ Low Coupling

Low coupling means components can change independently.

Signs of high coupling:

- Many imports and cross-calls between modules
- One small change forces changes in many places
- Code can’t be reused without dragging dependencies along

---

## ✅ High Cohesion

High cohesion means a module/class/function does one focused job.

Signs of low cohesion:

- “Utility” modules that contain unrelated helpers
- Classes with many unrelated methods
- Functions that do validation + parsing + storage + formatting

---

## ✅ Example: Improve Cohesion

Before (mixed responsibilities):

```python
def process_order(order):
    validate(order)
    save_to_db(order)
    send_email(order)
    print("Done")
```

After (clear responsibilities):

```python
def validate_order(order):
    ...

def persist_order(order):
    ...

def notify_order_created(order):
    ...
```

---

## 🔍 Key Takeaways

- Low coupling reduces “blast radius” of change.
- High cohesion makes code easier to locate and reason about.
- SoC often improves both coupling and cohesion.

---

[Back: Separation of Concerns](../04_separation_of_concerns/README.md) | [Next: Code Smells](../06_code_smells/README.md)
