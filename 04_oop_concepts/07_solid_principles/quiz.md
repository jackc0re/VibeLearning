# 🏗️ SOLID Principles Quiz

## 1. What does the "S" in SOLID stand for?
- [ ] Simple Responsibility Principle
- [ ] Single Responsibility Principle
- [ ] Static Responsibility Principle
- [ ] Secure Responsibility Principle

## 2. Which principle states "Software entities should be open for extension, but closed for modification"?
- [ ] Single Responsibility Principle (SRP)
- [ ] Open/Closed Principle (OCP)
- [ ] Liskov Substitution Principle (LSP)
- [ ] Interface Segregation Principle (ISP)

## 3. The Liskov Substitution Principle (LSP) is closely related to which OOP concept?
- [ ] Encapsulation
- [ ] Polymorphism
- [ ] Recursion
- [ ] File I/O

## 4. What is the problem with "God Interfaces" (interfaces with too many methods)?
- [ ] They violate the Interface Segregation Principle (ISP)
- [ ] They use too much memory
- [ ] They are too small
- [ ] They violate the Open/Closed Principle

## 5. Dependency Inversion Principle (DIP) suggests depending on what?
- [ ] Concrete implementations
- [ ] Low-level modules
- [ ] Database drivers
- [ ] Abstractions (Interfaces)

## 6. A `Square` class inherits from `Rectangle`, but `Square.set_width()` must also change `height`, breaking callers that set width and height independently. Which principle does this violate?
- [ ] Single Responsibility Principle (SRP)
- [ ] Open/Closed Principle (OCP)
- [ ] Liskov Substitution Principle (LSP)
- [ ] Dependency Inversion Principle (DIP)

## 7. `NotificationService` accepts any object with a `send()` method through its constructor, instead of creating an `EmailSender` internally. Which principle -- and which technique -- is this?
- [ ] ISP, via method overriding
- [ ] DIP, via dependency injection
- [ ] OCP, via operator overloading
- [ ] SRP, via inheritance

---

### Answers
1. Single Responsibility Principle
2. Open/Closed Principle (OCP)
3. Polymorphism
4. They violate the Interface Segregation Principle (ISP)
5. Abstractions (Interfaces)
6. Liskov Substitution Principle (LSP)
7. DIP, via dependency injection
