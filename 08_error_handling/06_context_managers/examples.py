"""
Context Managers - Examples
===========================

Demonstrates what `with` guarantees, class-based and generator-based
context managers, exception suppression, contextlib.suppress, and ExitStack.
Run with:
    python examples.py
"""

import os
import tempfile
import time
from contextlib import ExitStack, contextmanager, suppress

print("=" * 50)
print("CONTEXT MANAGERS - Examples")
print("=" * 50)


# =============================================================================
# SECTION 1: FROM TRY/FINALLY TO WITH
# =============================================================================
print("\n--- From try/finally to with ---\n")

# Topic 02 showed cleanup with try/finally: the finally block runs no
# matter how the body ends.
handle = None
try:
    print("  try/finally: (imagine opening a resource here)")
    print("  try/finally: (imagine using it here)")
finally:
    print("  try/finally: cleanup runs no matter what")

# The with statement builds that shape into the language. A temp folder
# keeps this demo from leaving files behind.
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "demo.txt")

    # The manual way, one last time:
    handle = open(path, "w", encoding="utf-8")
    try:
        handle.write("written with try/finally")
    finally:
        handle.close()
        print("  try/finally: we closed the file ourselves")

    # The with way: same guarantee, no bookkeeping.
    with open(path, "w", encoding="utf-8") as file:
        file.write("written with a context manager")
    print("  with: the file was closed for us")


# =============================================================================
# SECTION 2: WHAT WITH GUARANTEES
# =============================================================================
print("\n--- What with guarantees ---\n")


class Tracer:
    """Prints every protocol call it receives."""

    def __enter__(self):
        print("  __enter__ ran -> returning a value for 'as'")
        return "tracer-value"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("  __exit__ ran -> body finished, exc_type is None")
        else:
            print(f"  __exit__ ran -> exc_type is {exc_type.__name__}")
            print(f"  exc_val is {exc_val!r}")
            print(f"  exc_tb is a traceback object: {exc_tb is not None}")
        return False  # never suppress


with Tracer() as value:
    print(f"  body sees {value!r}")

try:
    with Tracer():
        raise ValueError("boom")
except ValueError as exc:
    print(f"  exception propagated out of the with block: {exc}")


# =============================================================================
# SECTION 3: RETURNING TRUE FROM __exit__ SUPPRESSES THE EXCEPTION
# =============================================================================
print("\n--- Returning True suppresses the exception ---\n")


class BlackHole:
    """A manager that swallows every error. Almost always a bad idea!"""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"  BlackHole received {exc_type.__name__}: {exc_val!r}")
        print("  returning True -> Python acts like nothing happened")
        return True


with BlackHole():
    raise ValueError("this error vanishes")
print("  execution just continues - the error is gone!")

print()
print("  *** WARNING: returning True hides ALL errors, even real bugs. ***")
print("  *** Returning None (or False) propagates - usually correct!   ***")
print("  *** To ignore a specific error, prefer contextlib.suppress.   ***")


# =============================================================================
# SECTION 4: CLASS-BASED MANAGERS - TIMER AND A FAKE DATABASE
# =============================================================================
print("\n--- Class-based managers: Timer and Transaction ---\n")


class Timer:
    """Measures how long its with-block takes."""

    def __enter__(self):
        self.start = time.perf_counter()
        return self  # bound to the name after 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"  block took {self.elapsed:.6f}s")
        return False  # never suppress


with Timer() as timer:
    total = sum(range(500000))
print(f"  summed to {total}; elapsed stored on the timer: {timer.elapsed:.6f}s")


class FakeDatabase:
    """A pretend database: its whole state is one dictionary."""

    def __init__(self):
        self.data = {"users": 0}

    def commit(self, changes):
        self.data.update(changes)
        print(f"  COMMIT: data is now {self.data}")

    def rollback(self):
        print(f"  ROLLBACK: data stays {self.data}")


class Transaction:
    """All changes land together, or none of them do."""

    def __init__(self, db):
        self.db = db
        self.pending = {}

    def set(self, key, value):
        self.pending[key] = value

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.db.commit(self.pending)
        else:
            print(f"  error inside transaction: {exc_type.__name__}: {exc_val}")
            self.db.rollback()
        return False  # let real errors surface


db = FakeDatabase()
with Transaction(db) as tx:
    tx.set("users", 41)
    tx.set("logged_in", True)

try:
    with Transaction(db) as tx:
        tx.set("users", 99)
        raise RuntimeError("network cable unplugged")
except RuntimeError as exc:
    print(f"  caught outside: {exc}")


# =============================================================================
# SECTION 5: GENERATOR MANAGERS - @contextmanager
# =============================================================================
print("\n--- Generator managers: @contextmanager ---\n")


@contextmanager
def timed(label):
    """The Timer idea, rewritten as a generator.

    Before the yield = __enter__.
    The yield itself marks where the with-body runs.
    After the yield (in finally!) = __exit__.
    """
    start = time.perf_counter()
    try:
        yield label
    finally:
        elapsed = time.perf_counter() - start
        print(f"  [{label}] finished in {elapsed:.6f}s")


with timed("summing"):
    total = sum(range(500000))

try:
    with timed("failing block"):
        raise ValueError("oops")
except ValueError as exc:
    print(f"  finally ran even though the block raised: {exc}")


# =============================================================================
# SECTION 6: CONTEXTLIB.SUPPRESS - IGNORE A SPECIFIC ERROR
# =============================================================================
print("\n--- contextlib.suppress ---\n")

config = {}
with suppress(FileNotFoundError):
    with open("no_such_config.ini", "r", encoding="utf-8") as file:
        config["loaded"] = True
print(f"  missing file was ignored, config = {config}")

numbers = {"a": 1}
with suppress(KeyError):
    value = numbers["b"]
    print(f"  got {value}")
print("  missing key was ignored too")

try:
    with suppress(KeyError):
        raise ValueError("not a KeyError")
except ValueError as exc:
    print(f"  suppress only catches what you asked for: {exc}")


# =============================================================================
# SECTION 7: EXITSTACK - A DYNAMIC NUMBER OF MANAGERS
# =============================================================================
print("\n--- ExitStack ---\n")

events = []


class FakeResource:
    """A fake resource that logs when it is acquired and released."""

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        events.append("acquire " + self.name)
        print(f"  acquired {self.name}")
        return self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        events.append("release " + self.name)
        print(f"  released {self.name}")
        return False


# The number of managers is decided at runtime, so 'with a, b, c' will not
# work - but ExitStack handles any count.
resources = [FakeResource("db-connection"), FakeResource("config"), FakeResource("lock")]
with ExitStack() as stack:
    opened = [stack.enter_context(resource) for resource in resources]
    print(f"  all {len(opened)} resources ready: {opened}")

print(f"  release happened in reverse: {events[3:]}")

print("\n" + "=" * 50)
print("PASS Examples complete! Try exercises.py next.")
print("=" * 50)
