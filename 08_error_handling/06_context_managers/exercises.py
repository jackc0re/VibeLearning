"""
Context Managers - Exercises
============================
Practice writing class-based and generator-based context managers,
suppressing expected errors, and handling a dynamic number of resources.
Try to solve each exercise before looking at the solutions!
Solutions are provided at the bottom of this file.
Run with:
    python exercises.py
"""

import os
import tempfile
import time
from contextlib import ExitStack, contextmanager, redirect_stdout, suppress
from io import StringIO

print("=" * 50)
print("CONTEXT MANAGERS - Exercises")
print("=" * 50)


# =============================================================================
# EXERCISE 1: Timer (class-based)
# =============================================================================
print("\n--- Exercise 1: Timer ---\n")
"""
Write a class-based context manager that times its with-block:

- __enter__: record the start time with time.perf_counter(), return self
- __exit__: store elapsed seconds on self.elapsed, return False
  (returning False - or nothing - means "never suppress exceptions")

The tests below time a real loop, then check that elapsed is still
set when the block raises.
"""

# Your code below:
class Timer:
    pass  # TODO: replace this stub with your implementation


# =============================================================================
# EXERCISE 2: tag - a generator-based printer
# =============================================================================
print("\n--- Exercise 2: tag printer ---\n")
"""
Write a @contextmanager generator called tag(name) that:

- prints "<name>" when the block starts
- prints "</name>" when the block ends - EVEN IF the body raises

Wrap the yield in try/finally. That finally is the whole point!
"""

# Your code below:
@contextmanager
def tag(name):
    yield  # TODO: print the opening tag, yield inside try/finally, close in finally


# =============================================================================
# EXERCISE 3: Transaction (all-or-nothing writes)
# =============================================================================
print("\n--- Exercise 3: Transaction ---\n")
"""
FakeDatabase (provided below) stores everything in one dict. Write a
Transaction manager so changes land together, or not at all:

- set(key, value) records a pending change (already written for you)
- __enter__ returns self
- __exit__ with no exception: apply the pending changes to db.data and
  append "commit" to self.log
- __exit__ with an exception: do NOT touch db.data, append "rollback"
  to self.log, and return None (or False) so the error still propagates
"""


class FakeDatabase:
    """A pretend database: its whole state is one dict. Do not modify."""

    def __init__(self):
        self.data = {}


# Your code below:
class Transaction:
    def __init__(self, db):
        self.db = db
        self.changes = {}
        self.log = []

    def set(self, key, value):
        self.changes[key] = value

    # TODO: __enter__ -> return self
    # TODO: __exit__ -> commit or rollback; never suppress


# =============================================================================
# EXERCISE 4: load_config with contextlib.suppress
# =============================================================================
print("\n--- Exercise 4: load_config ---\n")
"""
Write load_config(path) that reads a file of "key=value" lines into a
dict (values stay strings). If the file does not exist, return {}.

Use "with suppress(FileNotFoundError):" around a real open() - do not
use os.path.exists or try/except for this one.
"""

# Your code below:
def load_config(path):
    # TODO: suppress(FileNotFoundError) + open() + parse "key=value" lines
    return None


# =============================================================================
# EXERCISE 5: enter_all with ExitStack
# =============================================================================
print("\n--- Exercise 5: ExitStack ---\n")
"""
Write enter_all(managers) that enters a LIST of context managers using
one ExitStack and returns the values they handed back, in order.

TrackedResource (provided below) logs every acquire/release, so the
tests can check that everything entered also exits - in reverse order.
"""


class TrackedResource:
    """A fake resource that records its lifecycle. Do not modify."""

    events = []

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        TrackedResource.events.append("acquire " + self.name)
        return self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        TrackedResource.events.append("release " + self.name)
        return False


# Your code below:
def enter_all(managers):
    # TODO: one ExitStack, enter every manager, return the list of values
    return []


# =============================================================================
# EXERCISE 6: timed - Timer rewritten as a generator
# =============================================================================
print("\n--- Exercise 6: timed ---\n")
"""
Rewrite the Timer idea with @contextmanager:

- record the start time before the yield
- yield inside a try
- in the finally, print:  [label] done in X.XXXXs

The finally must run even when the body raises - that is the whole
point of a context manager.
"""

# Your code below:
@contextmanager
def timed(label):
    yield  # TODO: time the block, print "[label] done in X.XXXXs" in a finally


# =============================================================================
# TESTS
# =============================================================================


def capture_output(func):
    """Run func() and return everything it printed, as a string."""
    buffer = StringIO()
    with redirect_stdout(buffer):
        func()
    return buffer.getvalue()


def run_tests():
    print("\nRunning Context Managers Exercises Tests")
    print("=" * 50)
    all_passed = True

    def report(description, condition, detail=""):
        nonlocal all_passed
        status = "PASS" if condition else "FAIL"
        if not condition:
            all_passed = False
        suffix = f" ({detail})" if detail and not condition else ""
        print(f"  {status} {description}{suffix}")

    def unfinished(exc):
        report("exercise not implemented yet", False,
               f"{type(exc).__name__}: {exc}")

    # Exercise 1
    print("\nExercise 1: Timer")
    try:
        timer = Timer()
        with timer:
            sum(range(200000))
        elapsed = getattr(timer, "elapsed", None)
        report("elapsed is a float >= 0",
               isinstance(elapsed, float) and elapsed >= 0.0,
               f"elapsed={elapsed!r}")
    except Exception as exc:
        unfinished(exc)
    try:
        t2 = Timer()
        propagated = False
        try:
            with t2:
                raise ValueError("boom")
        except ValueError:
            propagated = True
        report("exceptions are not suppressed", propagated)
        elapsed2 = getattr(t2, "elapsed", None)
        report("elapsed is set even on error",
               isinstance(elapsed2, float) and elapsed2 >= 0.0,
               f"elapsed={elapsed2!r}")
    except Exception as exc:
        unfinished(exc)

    # Exercise 2
    print("\nExercise 2: tag printer")
    try:
        def body():
            with tag("b"):
                print("hello")

        text = capture_output(body)
        report("opening tag printed", "<b>" in text, repr(text))
        report("closing tag printed", "</b>" in text, repr(text))

        buffer = StringIO()
        propagated = False
        try:
            with redirect_stdout(buffer):
                with tag("i"):
                    raise ValueError("oops")
        except ValueError:
            propagated = True
        text2 = buffer.getvalue()
        report("error still propagates", propagated)
        report("closing tag printed even on error", "</i>" in text2, repr(text2))
    except Exception as exc:
        unfinished(exc)

    # Exercise 3
    print("\nExercise 3: Transaction")
    try:
        db = FakeDatabase()
        tx = Transaction(db)
        with tx:
            tx.set("health", 100)
        report("commit applied the changes", db.data.get("health") == 100,
               f"data={db.data}")
        report("commit was recorded", getattr(tx, "log", None) == ["commit"],
               f"log={getattr(tx, 'log', None)}")
    except Exception as exc:
        unfinished(exc)
    try:
        db2 = FakeDatabase()
        tx2 = Transaction(db2)
        propagated = False
        try:
            with tx2:
                tx2.set("health", 50)
                raise RuntimeError("connection lost")
        except RuntimeError:
            propagated = True
        report("rollback kept the old data", "health" not in db2.data,
               f"data={db2.data}")
        report("rollback was recorded", getattr(tx2, "log", None) == ["rollback"],
               f"log={getattr(tx2, 'log', None)}")
        report("error still propagates", propagated)
    except Exception as exc:
        unfinished(exc)

    # Exercise 4
    print("\nExercise 4: load_config")
    try:
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "config.ini")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write("theme=dark\nlevel=3\n")
            config = load_config(path)
            report("parses key=value lines",
                   config == {"theme": "dark", "level": "3"},
                   f"got {config!r}")
        # tmp is deleted by now, so this path definitely does not exist
        missing = load_config(os.path.join(tmp, "nope.ini"))
        report("missing file returns {}", missing == {}, f"got {missing!r}")
    except Exception as exc:
        unfinished(exc)

    # Exercise 5
    print("\nExercise 5: ExitStack")
    try:
        TrackedResource.events = []
        names = enter_all(
            [TrackedResource("db"), TrackedResource("cache"), TrackedResource("lock")]
        )
        report("returns entered values in order",
               names == ["db", "cache", "lock"], f"got {names!r}")
        expected = [
            "acquire db", "acquire cache", "acquire lock",
            "release lock", "release cache", "release db",
        ]
        report("all entered, then released in reverse",
               TrackedResource.events == expected,
               f"got {TrackedResource.events}")
    except Exception as exc:
        unfinished(exc)

    # Exercise 6
    print("\nExercise 6: timed")
    try:
        def body():
            with timed("addition"):
                result = 1 + 1
            return result

        text = capture_output(body)
        report("prints the label", "addition" in text, repr(text))
        report("prints the elapsed time", "done in" in text, repr(text))

        buffer = StringIO()
        propagated = False
        try:
            with redirect_stdout(buffer):
                with timed("division"):
                    raise ZeroDivisionError("oh no")
        except ZeroDivisionError:
            propagated = True
        text2 = buffer.getvalue()
        report("error still propagates", propagated)
        report("still prints on error", "done in" in text2, repr(text2))
    except Exception as exc:
        unfinished(exc)

    print("\n" + "=" * 50)
    if all_passed:
        print("All tests passed! Great job!")
    else:
        print("Some tests failed. Keep practicing!")
        print("Tip: scroll down to SOLUTIONS when you are ready.")
    print("=" * 50)


run_tests()


# =============================================================================
# SOLUTIONS (Don't peek until you've tried!)
# =============================================================================
print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 1: Timer
print("\n--- Solution 1: Timer ---")


class Timer:
    """Context manager that measures how long its with-block takes."""

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        return False  # never suppress


with Timer() as timer:
    sum(range(200000))
print(f"  summing took {timer.elapsed:.6f}s")

# SOLUTION 2: tag
print("\n--- Solution 2: tag printer ---")


@contextmanager
def tag(name):
    print(f"<{name}>")
    try:
        yield
    finally:
        print(f"</{name}>")


with tag("greeting"):
    print("hello")

# SOLUTION 3: Transaction
print("\n--- Solution 3: Transaction ---")


class Transaction:
    """All-or-nothing writes to a FakeDatabase."""

    def __init__(self, db):
        self.db = db
        self.changes = {}
        self.log = []

    def set(self, key, value):
        self.changes[key] = value

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.db.data.update(self.changes)
            self.log.append("commit")
            print(f"  committed: {self.changes}")
        else:
            self.log.append("rollback")
            print(f"  rolled back ({exc_type.__name__}: {exc_val})")
        return None  # never suppress


db = FakeDatabase()
with Transaction(db) as tx:
    tx.set("gold", 250)
print(f"  after commit: {db.data}")

try:
    with Transaction(db) as tx:
        tx.set("gold", 999)
        raise RuntimeError("server exploded")
except RuntimeError as exc:
    print(f"  after rollback: {db.data} (error was: {exc})")

# SOLUTION 4: load_config
print("\n--- Solution 4: load_config ---")


def load_config(path):
    """Read "key=value" lines into a dict; missing file -> {}."""
    config = {}
    with suppress(FileNotFoundError):
        with open(path, "r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    return config


with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "app.ini")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("theme=dark\n")
    print(f"  existing file: {load_config(path)}")
    print(f"  missing file:  {load_config(os.path.join(tmp, 'gone.ini'))}")

# SOLUTION 5: enter_all
print("\n--- Solution 5: ExitStack ---")


def enter_all(managers):
    """Enter every manager on one ExitStack; return the values in order."""
    with ExitStack() as stack:
        return [stack.enter_context(manager) for manager in managers]


TrackedResource.events = []
names = enter_all(
    [TrackedResource("db"), TrackedResource("cache"), TrackedResource("lock")]
)
print(f"  entered: {names}")
print(f"  events:  {TrackedResource.events}")

# SOLUTION 6: timed
print("\n--- Solution 6: timed ---")


@contextmanager
def timed(label):
    """Print how long the with-block took, even when it raises."""
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"  [{label}] done in {elapsed:.4f}s")


with timed("demo"):
    sum(range(200000))

print("\n" + "=" * 50)
print("Done! Replace the stubs above with your own code and re-run.")
print("When they all PASS, move on to 09_testing next.")
print("=" * 50)
