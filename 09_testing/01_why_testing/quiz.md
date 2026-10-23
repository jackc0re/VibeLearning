# Quiz: Why Testing

1) What problem do regression tests prevent?

2) Name the three common test levels (unit/integration/...).

3) Why should tests be deterministic?

4) What is the Arrange / Act / Assert structure?

5) Give one example of a dependency that should usually be avoided in unit tests.

---

## Suggested Answers

Try to answer each question out loud before reading these.

1. A regression test prevents an already-fixed bug from quietly coming back. The test pins the behaviour you care about, so any later change that breaks it fails the suite instead of reaching a user.
2. Unit, integration and end-to-end (E2E). Unit tests check one small piece fast and isolated, integration tests check several parts working together, and E2E tests drive the whole system the way a user would.
3. A deterministic test gives the same result on every run for the same code. If a test depends on time, randomness or the network it fails at random, and people stop trusting red results.
4. Arrange sets up the inputs, Act calls the thing under test once, Assert checks the outcome. The shape keeps each test readable and focused on one behaviour.
5. A real network call (also the real clock, `random`, or the filesystem). Those make a unit test slow and flaky, so they are replaced with a mock or a fake value.
