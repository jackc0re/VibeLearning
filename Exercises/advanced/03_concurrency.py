"""
Advanced Exercise 3: Concurrency & Parallelism
==============================================
Thread-safe state, the producer-consumer pattern, an async
"API client" (simulated latency), and parallel processing with
concurrent.futures. No multiprocessing, no real network.
"""

import queue
import threading
import time

print("=" * 50)
print("EXERCISE 3: Concurrency & Parallelism")
print("=" * 50)


# =============================================================================
# EXERCISE 3.1: Thread-Safe Data Structure
# =============================================================================
print("\n--- Exercise 3.1: Thread-Safe Data Structure ---")
"""
Implement SafeCounter:
- increment() adds 1 to an internal count under a threading.Lock
- count is a property that also reads under the lock

The solution starts 4 threads that each increment 25,000 times and
verifies the final count is exactly 100,000 (without the lock,
some increments would silently vanish).
"""


# Your code below:
class SafeCounter:
    """A counter many threads can increment safely."""

    pass


# Test (uncomment after implementing)
# counter = SafeCounter()
# for _ in range(1000):
#     counter.increment()
# print(counter.count)


# =============================================================================
# EXERCISE 3.2: Producer-Consumer Pattern
# =============================================================================
print("\n--- Exercise 3.2: Producer-Consumer Pattern ---")
"""
Wire up a bounded work queue:

- 2 producers each put 5 task strings into queue.Queue(maxsize=5)
- 2 consumers loop on task_queue.get(), recording results
- After joining the producers, put one sentinel None per consumer
  so they can stop; join the consumers
- All 10 tasks must be processed exactly once
"""


# Your code below:
task_queue = queue.Queue(maxsize=5)
results = []
results_lock = threading.Lock()


def producer(pid):
    """Put 5 tasks into the queue."""
    pass


def consumer(cid):
    """Take tasks until a None sentinel arrives."""
    pass


# =============================================================================
# EXERCISE 3.3: Async API Client (Simulated)
# =============================================================================
print("\n--- Exercise 3.3: Async API Client (Simulated) ---")
"""
Simulate a slow API without any network:

- fetch_user(uid) is a coroutine that waits asyncio.sleep(0.1)
  (pretend latency) and returns {"id": uid, "name": f"user{uid}"}
- fetch_all_sequential(ids) awaits the users one at a time
- fetch_all_concurrent(ids) gathers them all at once

The solution times both approaches: 5 users should take about
0.5s sequentially but only about 0.1s concurrently.
"""

import asyncio


# Your code below:
async def fetch_user(uid):
    """Return a fake user record after simulated latency."""
    pass


# =============================================================================
# EXERCISE 3.4: Parallel Data Processing
# =============================================================================
print("\n--- Exercise 3.4: Parallel Data Processing ---")
"""
Use concurrent.futures.ThreadPoolExecutor to count words across
several "documents" in parallel:

- word_count(text) returns a {word: count} dict for one document
- Feed all documents through executor.map, then merge the partial
  counts into one combined dict
"""

from concurrent.futures import ThreadPoolExecutor


# Your code below:
def word_count(text):
    """Count words in one document."""
    pass


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 3.1
print("\n--- Solution 3.1 ---")


class SafeCounter:
    """A counter many threads can increment safely."""

    def __init__(self):
        self._count = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self._count += 1

    @property
    def count(self):
        with self._lock:
            return self._count


def bump(counter, times):
    for _ in range(times):
        counter.increment()


counter = SafeCounter()
threads = [threading.Thread(target=bump, args=(counter, 25_000)) for _ in range(4)]

start = time.perf_counter()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
elapsed = time.perf_counter() - start

final = counter.count
print(f"4 threads x 25,000 increments finished in {elapsed:.3f}s")
print(f"Final count: {final} (expected 100000)")
print("PASS" if final == 100_000 else "FAIL")

# SOLUTION 3.2
print("\n--- Solution 3.2 ---")

task_queue = queue.Queue(maxsize=5)
results = []
results_lock = threading.Lock()
ITEMS_PER_PRODUCER = 5


def producer(pid):
    """Put 5 tasks into the queue."""
    for i in range(ITEMS_PER_PRODUCER):
        task_queue.put(f"task-p{pid}-{i}")


def consumer(cid):
    """Take tasks until a None sentinel arrives."""
    while True:
        task = task_queue.get()
        if task is None:
            break
        with results_lock:
            results.append(f"{task} (done by consumer {cid})")


producers = [threading.Thread(target=producer, args=(p,)) for p in (1, 2)]
consumers = [threading.Thread(target=consumer, args=(c,)) for c in (1, 2)]

for thread in consumers:
    thread.start()
for thread in producers:
    thread.start()
for thread in producers:
    thread.join()

task_queue.put(None)  # one stop signal per consumer
task_queue.put(None)
for thread in consumers:
    thread.join()

print(f"Processed {len(results)} tasks (expected 10)")
for line in sorted(results):
    print(f"  {line}")
print("PASS" if len(results) == 10 else "FAIL")

# SOLUTION 3.3
print("\n--- Solution 3.3 ---")

API_LATENCY = 0.1
USER_IDS = [1, 2, 3, 4, 5]


async def fetch_user(uid):
    """Return a fake user record after simulated latency."""
    await asyncio.sleep(API_LATENCY)  # pretend this is a network call
    return {"id": uid, "name": f"user{uid}"}


async def fetch_all_sequential(ids):
    """Await each request one at a time."""
    users = []
    for uid in ids:
        users.append(await fetch_user(uid))
    return users


async def fetch_all_concurrent(ids):
    """Fire every request at once and gather the results."""
    return await asyncio.gather(*(fetch_user(uid) for uid in ids))


start = time.perf_counter()
sequential = asyncio.run(fetch_all_sequential(USER_IDS))
seconds_sequential = time.perf_counter() - start

start = time.perf_counter()
concurrent = asyncio.run(fetch_all_concurrent(USER_IDS))
seconds_concurrent = time.perf_counter() - start

print(f"Sequential: {len(sequential)} users in {seconds_sequential:.2f}s")
print(f"Concurrent: {len(concurrent)} users in {seconds_concurrent:.2f}s")
print(
    "PASS"
    if len(concurrent) == 5 and concurrent[2]["name"] == "user3" and seconds_concurrent < seconds_sequential
    else "FAIL"
)

# SOLUTION 3.4
print("\n--- Solution 3.4 ---")


def word_count(text):
    """Count words in one document."""
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


documents = [("alpha beta gamma " * 100) + f"doc{i}" for i in range(8)]

combined = {}
start = time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as pool:
    for partial in pool.map(word_count, documents):
        for word, count in partial.items():
            combined[word] = combined.get(word, 0) + count
elapsed = time.perf_counter() - start

print(f"Merged counts: {combined}")
print(f"Processed {len(documents)} documents in {elapsed:.4f}s")
print("PASS" if combined.get("alpha") == 800 else "FAIL")

print("\n" + "=" * 50)
print("Great job! Move on to 04_real_world.py")
print("=" * 50)
