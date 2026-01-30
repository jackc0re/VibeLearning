"""
API Best Practices - Examples
=============================
Production-ready techniques for API clients.
"""

print("=" * 60)
print("API BEST PRACTICES - Examples")
print("=" * 60)

# =============================================================================
# RATE LIMITING
# =============================================================================
print("\n--- Rate Limiting ---\n")

import time

class RateLimiter:
    """Simple rate limiter using fixed window."""
    
    def __init__(self, max_requests=10, window_seconds=60):
        self.max_requests = max_requests
        self.window = window_seconds
        self.requests = []
    
    def can_proceed(self):
        """Check if a new request is allowed."""
        now = time.time()
        # Remove old requests outside window
        self.requests = [r for r in self.requests if now - r < self.window]
        return len(self.requests) < self.max_requests
    
    def record_request(self):
        """Record that a request was made."""
        self.requests.append(time.time())
    
    def wait_time(self):
        """Calculate how long to wait before next request."""
        if self.can_proceed():
            return 0
        now = time.time()
        oldest = min(self.requests)
        return self.window - (now - oldest)

# Demo
limiter = RateLimiter(max_requests=3, window_seconds=10)

for i in range(5):
    if limiter.can_proceed():
        limiter.record_request()
        print(f"Request {i+1}: Allowed ✅")
    else:
        wait = limiter.wait_time()
        print(f"Request {i+1}: Rate limited ⏳ (wait {wait:.1f}s)")
    time.sleep(1)

# =============================================================================
# SIMPLE DELAY BETWEEN REQUESTS
# =============================================================================
print("\n--- Simple Rate Limiter (Time Between Requests) ---\n")

import time

class SimpleDelayer:
    """Ensure minimum time between requests."""
    
    def __init__(self, min_interval=1.0):
        self.min_interval = min_interval
        self.last_request = 0
    
    def wait_if_needed(self):
        """Wait if not enough time has passed."""
        elapsed = time.time() - self.last_request
        if elapsed < self.min_interval:
            wait = self.min_interval - elapsed
            print(f"Waiting {wait:.2f}s...")
            time.sleep(wait)
        self.last_request = time.time()

# Demo
delayer = SimpleDelayer(min_interval=0.5)
for i in range(3):
    delayer.wait_if_needed()
    print(f"Making request {i+1}")

# =============================================================================
# RETRY WITH EXPONENTIAL BACKOFF
# =============================================================================
print("\n--- Exponential Backoff Retry ---\n")

import random
import time

def exponential_backoff(attempt, base_delay=1, max_delay=60):
    """
    Calculate delay with exponential backoff and jitter.
    
    attempt: 0-indexed attempt number
    base_delay: initial delay in seconds
    max_delay: maximum delay in seconds
    """
    # Exponential: 1, 2, 4, 8, 16...
    delay = min(base_delay * (2 ** attempt), max_delay)
    # Add jitter: random value between 0 and 1 second
    delay = delay + random.uniform(0, 1)
    return delay

# Demo retry delays
print("Retry delays with exponential backoff:")
for attempt in range(5):
    delay = exponential_backoff(attempt)
    print(f"  Attempt {attempt + 1}: wait {delay:.2f}s")

# =============================================================================
# SIMULATED RETRY LOGIC
# =============================================================================
print("\n--- Retry Logic Simulation ---\n")

def simulate_request_with_retry(max_retries=3):
    """Simulate a request that sometimes fails."""
    for attempt in range(max_retries):
        try:
            # Simulate: first 2 attempts fail, 3rd succeeds
            if attempt < 2:
                raise Exception(f"Simulated error on attempt {attempt + 1}")
            return "Success!"
        except Exception as e:
            print(f"  {e}")
            if attempt < max_retries - 1:
                delay = exponential_backoff(attempt)
                print(f"  Retrying in {delay:.2f}s...")
                time.sleep(delay / 10)  # Speed up for demo
            else:
                raise Exception("Max retries exceeded")

result = simulate_request_with_retry()
print(f"Final result: {result}")

# =============================================================================
# RATE LIMIT HEADER PARSER
# =============================================================================
print("\n--- Rate Limit Header Parser ---\n")

class RateLimitInfo:
    """Parse and track rate limit headers."""
    
    def __init__(self, headers):
        self.limit = self._parse_header(headers, "X-RateLimit-Limit")
        self.remaining = self._parse_header(headers, "X-RateLimit-Remaining")
        self.reset_time = self._parse_header(headers, "X-RateLimit-Reset")
    
    def _parse_header(self, headers, name):
        try:
            return int(headers.get(name, 0))
        except (ValueError, TypeError):
            return 0
    
    def is_near_limit(self, threshold=0.2):
        """Check if remaining requests are below threshold."""
        if self.limit == 0:
            return False
        return self.remaining / self.limit < threshold
    
    def __str__(self):
        return f"RateLimit: {self.remaining}/{self.limit} remaining"

# Demo with mock headers
mock_headers = {
    "X-RateLimit-Limit": "100",
    "X-RateLimit-Remaining": "15",
    "X-RateLimit-Reset": "1609459200",
}

rate_info = RateLimitInfo(mock_headers)
print(rate_info)
print(f"Near limit (20% threshold): {rate_info.is_near_limit(0.2)}")

# =============================================================================
# SIMPLE CACHE
# =============================================================================
print("\n--- Simple Time-Based Cache ---\n")

import time

class TimedCache:
    """Simple cache with TTL (time-to-live)."""
    
    def __init__(self, ttl_seconds=300):
        self.ttl = ttl_seconds
        self.cache = {}
    
    def get(self, key):
        """Get value from cache if not expired."""
        if key not in self.cache:
            return None
        
        value, expiry = self.cache[key]
        if time.time() > expiry:
            del self.cache[key]
            return None
        
        return value
    
    def set(self, key, value):
        """Store value in cache with TTL."""
        expiry = time.time() + self.ttl
        self.cache[key] = (value, expiry)
    
    def clear(self):
        """Clear all cached values."""
        self.cache.clear()

# Demo
cache = TimedCache(ttl_seconds=2)  # 2 second TTL for demo

cache.set("user:1", {"name": "Alice"})
print(f"Cached: {cache.get('user:1')}")

time.sleep(2.5)
print(f"After TTL: {cache.get('user:1')}")  # Should be None

# =============================================================================
# LOGGING SETUP
# =============================================================================
print("\n--- Logging Setup ---\n")

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("APIClient")

# Log different levels
logger.debug("This is a debug message (won't show)")
logger.info("Making API request to /users")
logger.warning("Rate limit is getting low")
logger.error("Request failed with 500")

# =============================================================================
# API CLIENT WITH BEST PRACTICES
# =============================================================================
print("\n--- Complete API Client with Best Practices ---\n")

import json
import time
import logging
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

class RobustAPIClient:
    """
    API client implementing best practices:
    - Rate limiting
    - Retry with exponential backoff
    - Timeout handling
    - Logging
    - Error handling
    """
    
    def __init__(self, base_url, rate_limit_delay=1.0, timeout=30):
        self.base_url = base_url.rstrip("/")
        self.rate_limit_delay = rate_limit_delay
        self.timeout = timeout
        self.logger = logging.getLogger("RobustAPIClient")
        self.last_request_time = 0
    
    def _wait_for_rate_limit(self):
        """Ensure we don't exceed rate limits."""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.rate_limit_delay:
            wait = self.rate_limit_delay - elapsed
            self.logger.debug(f"Rate limit wait: {wait:.2f}s")
            time.sleep(wait)
    
    def _make_request(self, url, method="GET", data=None, headers=None):
        """Make a single HTTP request."""
        req_headers = {
            "User-Agent": "RobustAPIClient/1.0 (Python 3.x)",
            "Accept": "application/json",
        }
        if headers:
            req_headers.update(headers)
        
        req = Request(
            url=url,
            data=data,
            headers=req_headers,
            method=method
        )
        
        return urlopen(req, timeout=self.timeout)
    
    def request(self, endpoint, method="GET", data=None, headers=None, 
                max_retries=3):
        """
        Make request with retry logic and rate limiting.
        
        Returns: (success: bool, response_data or error_message)
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        for attempt in range(max_retries):
            try:
                # Rate limiting
                self._wait_for_rate_limit()
                
                self.logger.info(f"{method} {url} (attempt {attempt + 1})")
                
                # Make request
                response = self._make_request(url, method, data, headers)
                self.last_request_time = time.time()
                
                # Parse response
                body = response.read().decode("utf-8")
                try:
                    data = json.loads(body)
                except json.JSONDecodeError:
                    data = body
                
                self.logger.info(f"Success: {response.status}")
                return True, data
                
            except HTTPError as e:
                self.last_request_time = time.time()
                
                # Retry on server errors and rate limits
                if e.code in (500, 502, 503, 429) and attempt < max_retries - 1:
                    delay = 2 ** attempt
                    self.logger.warning(f"HTTP {e.code}, retrying in {delay}s")
                    time.sleep(delay)
                else:
                    self.logger.error(f"HTTP Error {e.code}: {e.reason}")
                    return False, f"HTTP {e.code}: {e.reason}"
                    
            except URLError as e:
                self.logger.error(f"URL Error: {e.reason}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                else:
                    return False, f"Network error: {e.reason}"
                    
            except Exception as e:
                self.logger.error(f"Unexpected error: {e}")
                return False, str(e)
        
        return False, "Max retries exceeded"

# Demo (using httpbin for testing)
print("Creating robust client...")
client = RobustAPIClient("https://httpbin.org", rate_limit_delay=0.5)

success, data = client.request("/get")
print(f"Request result: {'✅ Success' if success else '❌ Failed'}")
if success:
    print(f"Got response with URL: {data.get('url', 'N/A')}")

# =============================================================================
# TIMEOUT CONFIGURATION
# =============================================================================
print("\n--- Timeout Configuration ---\n")

import socket

# Method 1: Global timeout
print("Method 1: Global timeout")
print("socket.setdefaulttimeout(10)  # All socket operations timeout after 10s")

# Method 2: Per-request timeout
print("\nMethod 2: Per-request timeout")
print("urlopen(request, timeout=10)  # This request times out after 10s")

# =============================================================================
# USER-AGENT BEST PRACTICES
# =============================================================================
print("\n--- User-Agent Best Practices ---\n")

def create_user_agent(app_name, version, contact=None):
    """Create a descriptive User-Agent string."""
    import sys
    
    user_agent = f"{app_name}/{version} (Python/{sys.version_info.major}.{sys.version_info.minor})"
    
    if contact:
        user_agent += f"; Contact: {contact}"
    
    return user_agent

# Examples
print(create_user_agent("MyApp", "1.0"))
print(create_user_agent("DataScraper", "2.1", contact="admin@example.com"))
print(create_user_agent("WeatherBot", "0.5", contact="https://github.com/user/weatherbot"))

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Rate Limiting: Don't exceed API limits, use delays or token buckets
2. Retries: Use exponential backoff for transient failures
3. Timeouts: Always set timeouts to prevent hanging
4. Logging: Log requests, responses, and errors for debugging
5. Caching: Cache responses to reduce API calls
6. User-Agent: Identify your app properly with contact info
7. Error Handling: Distinguish between retryable and permanent errors
8. Jitter: Add randomness to backoff to prevent thundering herd
9. Headers: Check rate limit headers and respond appropriately
10. Security: Never hardcode credentials, use environment variables
""")

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
