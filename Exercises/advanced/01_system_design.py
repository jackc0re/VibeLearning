"""
Advanced Exercise 1: System Design & Architecture
================================================
Design and implement complex systems with proper architecture.
"""

print("=" * 50)
print("EXERCISE 1: System Design & Architecture")
print("=" * 50)


# =============================================================================
# EXERCISE 1.1: LRU Cache
# =============================================================================
print("\n--- Exercise 1.1: LRU Cache ---")
"""
Implement a Least Recently Used (LRU) cache with:
- get(key): Return value if exists, else None
- put(key, value): Add/update key-value pair
- Capacity limit: Evict least recently used when full
- O(1) average time complexity
"""


# Your code below:
class LRUCache:
    """Least Recently Used Cache implementation."""

    pass


# Test
cache = LRUCache(capacity=2)
cache.put("a", 1)
cache.put("b", 2)
print(cache.get("a"))  # 1
cache.put("c", 3)  # evicts "b"
print(cache.get("b"))  # None
print(cache.get("c"))  # 3


# =============================================================================
# EXERCISE 1.2: Connection Pool
# =============================================================================
print("\n--- Exercise 1.2: Connection Pool ---")
"""
Implement a database connection pool with:
- Maximum connections
- Get connection (wait if pool full)
- Return connection
- Automatic cleanup
"""

import threading
import time


# Your code below:
class ConnectionPool:
    """Database connection pool."""

    pass


# =============================================================================
# EXERCISE 1.3: Rate Limiter
# =============================================================================
print("\n--- Exercise 1.3: Rate Limiter ---")
"""
Implement a rate limiter using sliding window:
- Allow N requests per time window
- Track timestamps of requests
- Return True if allowed, False otherwise
"""


# =============================================================================
# EXERCISE 1.4: Pub/Sub Message Queue
# =============================================================================
print("\n--- Exercise 1.4: Message Queue ---")
"""
Implement a publish-subscribe message queue:
- Subscribe to topics
- Publish messages to topics
- Unsubscribe from topics
- Thread-safe
"""


# Your code below:
class MessageQueue:
    """Pub/Sub message queue."""

    pass


# =============================================================================
# EXERCISE 1.5: Dependency Injection Container
# =============================================================================
print("\n--- Exercise 1.5: DI Container ---")
"""
Implement a dependency injection container:
- Register services
- Resolve dependencies
- Singleton and transient lifetimes
"""


# Your code below:
class Container:
    """Dependency injection container."""

    pass


# =============================================================================
# EXERCISE 1.5: Dependency Injection Container
# =============================================================================
print(
    "\n--- Exercise 1.5: DI Container ---"
    ""
    """
Implement a dependency injection container:
- Register services
- Resolve dependencies
- Singleton and transient lifetimes
"""
)


# Your code below:
class Container:
    """Dependency injection container."""

    pass


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 1.1
print("\n--- Solution 1.1 ---")
from collections import OrderedDict


class LRUCache:
    """Least Recently Used Cache implementation."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


cache = LRUCache(capacity=2)
cache.put("a", 1)
cache.put("b", 2)
print(f"Get 'a': {cache.get('a')}")
cache.put("c", 3)
print(f"Get 'b': {cache.get('b')}")
print(f"Get 'c': {cache.get('c')}")

# SOLUTION 1.2
print("\n--- Solution 1.2 (Simplified) ---")


class ConnectionPool:
    """Database connection pool."""

    def __init__(self, max_connections=5):
        self.max_connections = max_connections
        self.available = []
        self.in_use = set()
        self.lock = threading.Lock()

    def get_connection(self):
        with self.lock:
            if self.available:
                conn = self.available.pop()
                self.in_use.add(conn)
                return conn
            elif len(self.in_use) < self.max_connections:
                conn = f"connection_{len(self.in_use) + len(self.available)}"
                self.in_use.add(conn)
                return conn
            return None

    def return_connection(self, conn):
        with self.lock:
            if conn in self.in_use:
                self.in_use.remove(conn)
                self.available.append(conn)


print("ConnectionPool implemented (see full solution in code)")

# SOLUTION 1.3
print("\n--- Solution 1.3 ---")
import time
from collections import deque


class RateLimiter:
    """Rate limiter using sliding window."""

    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = deque()

    def allow(self):
        now = time.time()
        while self.requests and now - self.requests[0] > self.window_seconds:
            self.requests.popleft()

        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True
        return False


limiter = RateLimiter(max_requests=3, window_seconds=2)
print("Rate limiter test:")
for i in range(5):
    allowed = limiter.allow()
    print(f"Request {i + 1}: {'Allowed' if allowed else 'Blocked'}")
    time.sleep(0.5)

# SOLUTION 1.4
print("\n--- Solution 1.4 (Simplified) ---")


class MessageQueue:
    """Pub/Sub message queue."""

    def __init__(self):
        self.subscribers = {}
        self.lock = threading.Lock()

    def subscribe(self, topic, callback):
        with self.lock:
            if topic not in self.subscribers:
                self.subscribers[topic] = []
            self.subscribers[topic].append(callback)

    def publish(self, topic, message):
        with self.lock:
            if topic in self.subscribers:
                for callback in self.subscribers[topic]:
                    callback(message)

    def unsubscribe(self, topic, callback):
        with self.lock:
            if topic in self.subscribers:
                self.subscribers[topic].remove(callback)


print("MessageQueue implemented (see full solution in code)")

# SOLUTION 1.5
print("\n--- Solution 1.5 ---")


class Container:
    """Dependency injection container."""

    def __init__(self):
        self._services = {}
        self._singletons = {}

    def register_singleton(self, name, factory):
        self._services[name] = ("singleton", factory)

    def register_transient(self, name, factory):
        self._services[name] = ("transient", factory)

    def resolve(self, name):
        if name not in self._services:
            raise ValueError(f"Service {name} not registered")

        lifetime, factory = self._services[name]

        if lifetime == "singleton":
            if name not in self._singletons:
                self._singletons[name] = factory()
            return self._singletons[name]
        else:
            return factory()


container = Container()
container.register_singleton("db", lambda: {"connection": "active"})
container.register_transient("repo", lambda: {"id": 1})

print(f"DB 1: {container.resolve('db')}")
print(f"DB 2: {container.resolve('db')}")  # Same instance
print(f"Repo 1: {container.resolve('repo')}")
print(f"Repo 2: {container.resolve('repo')}")  # Different instance

print("\n" + "=" * 50)
print("Great job! Move on to 02_optimization.py")
print("=" * 50)
