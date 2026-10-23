# 🧠 Test-Driven Development (TDD) Quiz

1) What are the three steps in the TDD cycle?

2) In TDD, what should you do after all tests are green?

3) Why is it a bad idea to write many tests at once before implementing anything?

4) What does it mean to test behavior instead of implementation details?

5) Give one benefit of TDD beyond "catching bugs".

---

## Suggested Answers

Try to answer each question out loud before reading these.

1. Red, Green, Refactor. Write a failing test that describes one small behaviour (red), make it pass with the simplest code you can (green), then clean up the code while the tests keep it honest (refactor).
2. Refactor. Tests staying green is the signal that you can restructure the code without changing behaviour, so fix duplication and naming before moving to the next test.
3. You lose the feedback loop: many failing tests at once are hard to diagnose, and you stop seeing which small step each test was meant to drive. TDD works because each test pins exactly one new behaviour.
4. You assert what a function gives back (its return value, raised error or observable effect) rather than how it does it internally. Behaviour tests survive refactoring; tests bound to private helpers, call order or internals break whenever you clean up the code.
5. It improves design and keeps you honest about scope - writing the test first forces a clear input/output contract, so functions stay small and you only build what a test actually asks for.
