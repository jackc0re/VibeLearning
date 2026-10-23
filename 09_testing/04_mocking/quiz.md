# Quiz: Mocking

1) What problem does mocking solve in unit tests?

2) Name two dependencies you commonly mock.

3) Why can too much mocking make tests brittle?

4) What is the difference between a mock and a stub (in spirit)?

5) Which Python standard library module provides mocking tools?

---

## Suggested Answers

Try to answer each question out loud before reading these.

1. It lets a test replace a slow, unreliable or non-deterministic dependency with a controlled fake. The test then stays fast, repeatable and focused on your own logic instead of on the outside world.
2. Any two of: an external API/network call, the current time (`datetime.now()`), randomness (`random.random()`), filesystem access, a slow database or function.
3. The more you fake, the more your test describes your code's internal call sequence rather than its behaviour, so a harmless refactor breaks the test. If mocking gets complicated, that is usually a hint to redesign the boundary.
4. A stub just returns canned data and nothing else; a mock also records how it was used (calls, arguments) so you can assert on interactions. In practice both are usually built with `unittest.mock`, and you should only assert on interactions when the call itself is the behaviour you care about.
5. `unittest.mock` - for example `from unittest.mock import patch, Mock`, as used in this topic's `examples.py`.
