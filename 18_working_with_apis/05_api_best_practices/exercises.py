"""
API Best Practices - Exercises
==============================
Practice implementing production-ready API techniques.
"""

print("=" * 60)
print("API BEST PRACTICES - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: Token Bucket Rate Limiter
# =============================================================================
print("\n--- Exercise 1: Token Bucket Rate Limiter ---\n")
"""
Implement a TokenBucket rate limiter:

The bucket has a maximum capacity and refills at a constant rate.
Each request consumes 1 token. If no tokens available, request must wait.

Class should have:
- __init__(self, capacity, refill_rate): capacity is max tokens, refill_rate is tokens/sec
- consume(self, tokens=1): Returns wait time (0 if tokens available)
- _refill(self): Internal method to add tokens based on time passed

Example:
bucket = TokenBucket(capacity=5, refill_rate=1)  # 5 max, 1 per second
print(bucket.consume())  # Returns 0 (token available)
print(bucket.consume())  # Returns 0 (token available)
# ... after 5 consumes, should return wait time until refill
"""

# Your code here:



# =============================================================================
# EXERCISE 2: Retry Decorator
# =============================================================================
print("\n--- Exercise 2: Retry Decorator ---\n")
"""
Create a decorator @retry(max_retries=3, exceptions=(Exception,)) that:
1. Retries the decorated function up to max_retries times
2. Only catches specified exception types
3. Uses exponential backoff between retries
4. Logs each retry attempt

Example usage:
@retry(max_retries=3, exceptions=(ConnectionError,))
def fetch_data():
    # Might raise ConnectionError
    pass
"""

# Your code here:



# =============================================================================
# EXERCISE 3: Circuit Breaker Pattern
# =============================================================================
print("\n--- Exercise 3: Circuit Breaker ---\n")
"""
Implement a Circuit Breaker pattern:

The circuit has 3 states:
- CLOSED: Normal operation, requests pass through
- OPEN: Too many failures, requests fail fast without trying
- HALF_OPEN: After timeout, allow one test request

Class should have:
- __init__(self, failure_threshold=5, timeout=60)
- call(self, func, *args, **kwargs): Execute func or raise CircuitBreakerOpen
- record_success(): Switch to CLOSED
- record_failure(): Increment counter, possibly switch to OPEN

This prevents hammering a failing service with requests.
"""

# Your code here:



# =============================================================================
# EXERCISE 4: Request Timing Middleware
# =============================================================================
print("\n--- Exercise 4: Request Timing ---\n")
"""
Create a TimedRequest class that wraps urllib requests and tracks:
- Total requests made
- Average response time
- Success/failure counts
- Slowest request time

Methods:
- request(url): Make request, track timing
- get_stats(): Return dictionary with all metrics
"""

# Your code here:



# =============================================================================
# EXERCISE 5: Smart Retry Client
# =============================================================================
print("\n--- Exercise 5: Smart Retry Client ---\n")
"""
Create a SmartRetryClient that combines multiple best practices:

Features:
1. Only retries on specific status codes (429, 500, 502, 503)
2. Respects Retry-After header if present
3. Exponential backoff with jitter
4. Max total retry duration (don't retry forever)
5. Logs all retry attempts

Method:
- request(url, max_total_time=300): Make request with smart retry

The client should distinguish between:
- Retryable errors (server errors, rate limit)
- Non-retryable errors (404, 401, client errors)
"""

# Your code here:



# =============================================================================
# BONUS EXERCISE: API Response Cache with ETag
# =============================================================================
print("\n--- BONUS: ETag Cache ---\n")
"""
Implement an ETag-aware cache:

HTTP ETag header lets clients check if content changed without downloading.

Class ETagCache:
- get_cached_etag(url): Return stored ETag for URL
- store(url, etag, data): Store ETag and data
- is_modified(url, server_etag): Check if server ETag differs from cached

The request flow:
1. First request: GET url, store ETag and response
2. Subsequent requests: GET url with If-None-Match: <etag>
3. If 304 Not Modified: return cached data
4. If 200: store new ETag and response
"""

# Your code here:



# =============================================================================
# SOLUTIONS
# =============================================================================
print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# Exercise 1 Solution
print("\n--- Exercise 1 Solution ---")
import time

class TokenBucket:
    """Token bucket rate limiter."""
    
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate  # tokens per second
        self.last_refill = time.time()
    
    def _refill(self):
        """Add tokens based on time passed."""
        now = time.time()
        elapsed = now - self.last_refill
        tokens_to_add = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill = now
    
    def consume(self, tokens=1):
        """
        Try to consume tokens.
        Returns wait time (0 if successful, positive if need to wait).
        """
        self._refill()
        
        if self.tokens >= tokens:
            self.tokens -= tokens
            return 0
        
        # Calculate wait time needed
        tokens_needed = tokens - self.tokens
        wait_time = tokens_needed / self.refill_rate
        return wait_time

# Test
bucket = TokenBucket(capacity=3, refill_rate=2)
print("Token Bucket (capacity=3, refill=2/sec):")
for i in range(5):
    wait = bucket.consume()
    if wait == 0:
        print(f"  Request {i+1}: ✅ Consumed token")
    else:
        print(f"  Request {i+1}: ⏳ Wait {wait:.2f}s")

# Exercise 2 Solution
print("\n--- Exercise 2 Solution ---")
import time
import functools
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def retry(max_retries=3, exceptions=(Exception,), backoff=1):
    """Decorator for retry logic with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_retries - 1:
                        raise
                    delay = backoff * (2 ** attempt)
                    logger.warning(f"{func.__name__} failed (attempt {attempt + 1}), retrying in {delay}s: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator

# Test
attempts = 0

@retry(max_retries=3, exceptions=(ValueError,), backoff=0.1)
def flaky_function():
    global attempts
    attempts += 1
    if attempts < 3:
        raise ValueError(f"Failure #{attempts}")
    return "Success!"

print("Testing retry decorator:")
result = flaky_function()
print(f"Result: {result} after {attempts} attempts")

# Exercise 3 Solution
print("\n--- Exercise 3 Solution ---")
import time
from enum import Enum

class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

class CircuitBreakerOpen(Exception):
    pass

class CircuitBreaker:
    """Circuit breaker pattern implementation."""
    
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.last_failure_time = None
    
    def can_execute(self):
        """Check if request should be allowed."""
        if self.state == CircuitState.CLOSED:
            return True
        
        if self.state == CircuitState.OPEN:
            if time.time() - self.last_failure_time >= self.timeout:
                self.state = CircuitState.HALF_OPEN
                return True
            return False
        
        return True  # HALF_OPEN
    
    def record_success(self):
        """Record successful execution."""
        self.failure_count = 0
        self.state = CircuitState.CLOSED
    
    def record_failure(self):
        """Record failed execution."""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
    
    def call(self, func, *args, **kwargs):
        """Execute function with circuit breaker."""
        if not self.can_execute():
            raise CircuitBreakerOpen("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            self.record_success()
            return result
        except Exception as e:
            self.record_failure()
            raise

# Test
cb = CircuitBreaker(failure_threshold=3, timeout=5)

print("Circuit Breaker test:")
fail_count = 0

def unreliable():
    global fail_count
    fail_count += 1
    if fail_count < 4:
        raise ConnectionError("Service down")
    return "Working!"

for i in range(6):
    try:
        result = cb.call(unreliable)
        print(f"  Call {i+1}: ✅ {result}")
    except CircuitBreakerOpen:
        print(f"  Call {i+1}: ⛔ Circuit open (fast fail)")
    except ConnectionError as e:
        print(f"  Call {i+1}: ❌ {e}")

# Exercise 4 Solution
print("\n--- Exercise 4 Solution ---")
import time
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

class TimedRequest:
    """Track request timing statistics."""
    
    def __init__(self):
        self.total_requests = 0
        self.success_count = 0
        self.failure_count = 0
        self.total_time = 0
        self.slowest_time = 0
        self.fastest_time = float('inf')
    
    def request(self, url):
        """Make request and track metrics."""
        start = time.time()
        self.total_requests += 1
        
        try:
            response = urlopen(url)
            success = True
            self.success_count += 1
            return response
        except (HTTPError, URLError) as e:
            success = False
            self.failure_count += 1
            raise
        finally:
            elapsed = time.time() - start
            self.total_time += elapsed
            self.slowest_time = max(self.slowest_time, elapsed)
            self.fastest_time = min(self.fastest_time, elapsed)
    
    def get_stats(self):
        """Return timing statistics."""
        avg_time = self.total_time / self.total_requests if self.total_requests > 0 else 0
        return {
            "total_requests": self.total_requests,
            "success_count": self.success_count,
            "failure_count": self.failure_count,
            "avg_response_time": round(avg_time, 3),
            "slowest_request": round(self.slowest_time, 3) if self.slowest_time > 0 else 0,
            "fastest_request": round(self.fastest_time, 3) if self.fastest_time != float('inf') else 0,
        }

# Test
tr = TimedRequest()
print("TimedRequest stats (demo values):")
# Simulate some requests
for _ in range(3):
    tr.total_requests += 1
    tr.success_count += 1
    tr.total_time += 0.5
    tr.slowest_time = max(tr.slowest_time, 0.5)
    tr.fastest_time = min(tr.fastest_time, 0.5)

print(f"  Stats: {tr.get_stats()}")

# Exercise 5 Solution
print("\n--- Exercise 5 Solution ---")
import random
import time
import logging
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

logger = logging.getLogger("SmartRetryClient")

class SmartRetryClient:
    """API client with smart retry logic."""
    
    RETRYABLE_STATUSES = {429, 500, 502, 503}
    
    def __init__(self):
        self.retry_count = 0
    
    def request(self, url, max_total_time=300):
        """Make request with smart retry logic."""
        start_time = time.time()
        attempt = 0
        
        while True:
            try:
                req = Request(url, headers={"User-Agent": "SmartRetryClient/1.0"})
                response = urlopen(req)
                logger.info(f"Request succeeded on attempt {attempt + 1}")
                return response
                
            except HTTPError as e:
                # Check if we should retry
                if e.code not in self.RETRYABLE_STATUSES:
                    logger.error(f"Non-retryable error: {e.code}")
                    raise
                
                # Check retry-after header
                retry_after = e.headers.get("Retry-After")
                if retry_after:
                    try:
                        delay = int(retry_after)
                    except ValueError:
                        delay = 2 ** attempt
                else:
                    # Exponential backoff with jitter
                    delay = (2 ** attempt) + random.uniform(0, 1)
                
                # Check total time
                elapsed = time.time() - start_time
                if elapsed + delay > max_total_time:
                    logger.error(f"Max total time exceeded after {attempt + 1} attempts")
                    raise TimeoutError(f"Max retry time exceeded: {elapsed:.1f}s")
                
                attempt += 1
                logger.warning(f"Attempt {attempt} failed with {e.code}, waiting {delay:.1f}s")
                time.sleep(delay)
                
            except URLError as e:
                # Network errors are retryable
                elapsed = time.time() - start_time
                delay = (2 ** attempt) + random.uniform(0, 1)
                
                if elapsed + delay > max_total_time:
                    raise
                
                attempt += 1
                logger.warning(f"Network error on attempt {attempt}, retrying: {e.reason}")
                time.sleep(delay)

print("SmartRetryClient defined")
print("Features: selective retry, Retry-After support, backoff with jitter, max time limit")

# Bonus Solution
print("\n--- Bonus Solution ---")
class ETagCache:
    """ETag-aware response cache."""
    
    def __init__(self):
        self.cache = {}  # url -> (etag, data)
    
    def get_cached_etag(self, url):
        """Get stored ETag for URL."""
        if url in self.cache:
            return self.cache[url][0]
        return None
    
    def get_cached_data(self, url):
        """Get cached data for URL."""
        if url in self.cache:
            return self.cache[url][1]
        return None
    
    def store(self, url, etag, data):
        """Store ETag and data."""
        self.cache[url] = (etag, data)
    
    def is_modified(self, url, server_etag):
        """Check if content changed."""
        cached_etag = self.get_cached_etag(url)
        if cached_etag is None:
            return True
        return cached_etag != server_etag
    
    def make_conditional_request(self, url):
        """
        Make request with If-None-Match if we have cached ETag.
        Returns (data, from_cache) tuple.
        """
        from urllib.request import Request
        
        etag = self.get_cached_etag(url)
        
        if etag:
            # Make conditional request
            req = Request(url, headers={
                "If-None-Match": etag,
                "User-Agent": "ETagCache/1.0"
            })
        else:
            req = Request(url, headers={"User-Agent": "ETagCache/1.0"})
        
        try:
            response = urlopen(req)
            # Got new content
            data = response.read().decode()
            new_etag = response.getheader("ETag")
            if new_etag:
                self.store(url, new_etag, data)
            return data, False
            
        except HTTPError as e:
            if e.code == 304:
                # Not modified, return cached
                return self.get_cached_data(url), True
            raise

print("ETagCache defined")
print("Use: cache.make_conditional_request(url) -> (data, from_cache)")

print("\n" + "=" * 60)
print("All exercises complete! You're ready for production! 🚀")
print("=" * 60)
