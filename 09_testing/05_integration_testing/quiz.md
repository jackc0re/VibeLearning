# Quiz: Integration Testing

1) What is an integration test?

2) Give one example boundary that integration tests commonly cross.

3) Why are temporary directories useful in filesystem integration tests?

4) Why should integration tests still be deterministic?

5) Should you have more unit tests or integration tests in most projects? Why?

---

## Suggested Answers

Try to answer each question out loud before reading these.

1. A test that checks several parts of your code working together, rather than one unit in isolation. It is the level where wrong wiring, wrong formats and mismatched assumptions between components show up.
2. The filesystem, a database, HTTP, or a message queue - for example writing JSON to disk and reading it back. Real IO is what makes it an integration test rather than a unit test.
3. `tempfile.TemporaryDirectory()` gives each test a throwaway folder that is deleted afterwards. The test never depends on leftover files and never touches real user data, which keeps it repeatable and safe.
4. A flaky test is worthless as a signal, even at the integration level: no one can tell a genuine bug from a timing or leftover-state problem. Isolate state, use small fixed test data, and clean up so the same run gives the same result.
5. More unit tests, plus a smaller number of integration tests at the boundaries. Unit tests are fast and cheap so they cover the bulk of the logic, while integration tests are slower and fewer but catch the things unit tests cannot see.
