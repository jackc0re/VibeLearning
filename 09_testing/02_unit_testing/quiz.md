# Quiz: Unit Testing

1) What is a unit test supposed to isolate?

2) What does AAA stand for?

3) Why is using the real network in unit tests usually a bad idea?

4) In `unittest`, how do you assert that a function raises an exception?

5) In `unittest`, what base class do test cases inherit from, and what prefix must test method names use?

---

## Suggested Answers

Try to answer each question out loud before reading these.

1. One small piece of code — usually a single function or class — from everything around it. No network, no real files, no real clock, so a failure points at that one unit instead of at the environment.
2. Arrange, Act, Assert: set up the inputs, call the function once, then check the result.
3. The network is slow and outside your control, so the test can fail because a server or connection misbehaved rather than because your code is wrong. Unit tests should assert your logic, not the internet.
4. Use the context manager and call the function inside it: `with self.assertRaises(ValueError):` followed by the call. The test fails if no such exception is raised.
5. Inherit from `unittest.TestCase` and name test methods with a `test_` prefix. `unittest` only discovers and runs methods that start with `test_`, which is what `python -m unittest` looks for.
