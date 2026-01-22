# 🧩 Composition vs Inheritance Quiz

## 1. What relationship does Inheritance represent?
- [ ] Has-A
- [ ] Is-A
- [ ] Uses-A
- [ ] Was-A

## 2. What relationship does Composition represent?
- [ ] Has-A
- [ ] Is-A
- [ ] Kind-Of
- [ ] Parent-Of

## 3. Which approach is generally generally preferred for flexibility and loose coupling?
- [ ] Deep Inheritance Hierarchies
- [ ] Composition
- [ ] Multiple Inheritance
- [ ] Copy-Pasting Code

## 4. Why might you choose Composition over Inheritance?
- [ ] To change behavior at runtime by swapping components
- [ ] To write less code initially
- [ ] To enforce a strict hierarchy
- [ ] Because inheritance is deprecated

## 5. In "A Car has an Engine", which is the correct design?
- [ ] `class Car(Engine): ...`
- [ ] `class Engine(Car): ...`
- [ ] `class Car: def __init__(self): self.engine = Engine()`
- [ ] `class Car: def engine(self): return "V8"`

---

### Answers
1. Is-A
2. Has-A
3. Composition
4. To change behavior at runtime by swapping components
5. `class Car: def __init__(self): self.engine = Engine()`
