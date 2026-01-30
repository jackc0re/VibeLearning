# ⭐ API Best Practices

> Production-ready techniques for working with APIs

---

## Introduction

Writing code that works is just the beginning. Writing code that handles errors gracefully, respects rate limits, and performs well under pressure—that's what separates hobby projects from production systems.

This topic covers essential practices for building robust API clients and servers.

---

## 1. Rate Limiting

### Understanding Rate Limits

APIs limit how many requests you can make to prevent abuse:

| Approach | Description | Example |
|----------|-------------|---------|
| Fixed Window | X requests per time window | 100 requests/hour |
| Sliding Window | Smooth rate over time | 1.6 requests/minute |
| Token Bucket | Tokens refill over time | 10 tokens, refill 1/sec |

### Respecting Rate Limits

```python
import time
from urllib.request import urlopen

def rate_limited_request(url, min_interval=1.0):
    """Make requests with minimum time between them."""
    if not hasattr(rate_limited_request, "last_call"):
        rate_limited_request.last_call = 0
    
    # Calculate wait time
    elapsed = time.time() - rate_limited_request.last_call
    if elapsed < min_interval:
        time.sleep(min_interval - elapsed)
    
    # Make request
    response = urlopen(url)
    rate_limited_request.last_call = time.time()
    
    return response
```

### Checking Rate Limit Headers

```python
def get_rate_limit_info(response):
    """Extract rate limit information."""
    return {
        "limit": int(response.getheader("X-RateLimit-Limit", 0)),
        "remaining": int(response.getheader("X-RateLimit-Remaining", 0)),
        "reset": int(response.getheader("X-RateLimit-Reset", 0)),
    }

def should_wait(response):
    """Check if we should slow down."""
    info = get_rate_limit_info(response)
    if info["remaining"] < 5:
        return True
    return False
```

---

## 2. Retry Logic

### When to Retry

| Error | Retry? | Strategy |
|-------|--------|----------|
| 500 Server Error | ✅ Yes | Exponential backoff |
| 502 Bad Gateway | ✅ Yes | Wait and retry |
| 503 Service Unavailable | ✅ Yes | Wait and retry |
| 429 Rate Limited | ✅ Yes | Wait for reset |
| 404 Not Found | ❌ No | Resource doesn't exist |
| 401 Unauthorized | ❌ No | Fix credentials first |

### Exponential Backoff

```python
import time
from urllib.request import urlopen
from urllib.error import HTTPError

def fetch_with_retry(url, max_retries=3):
    """Fetch URL with exponential backoff retry."""
    for attempt in range(max_retries):
        try:
            return urlopen(url)
        except HTTPError as e:
            if e.code in (500, 502, 503, 429) and attempt < max_retries - 1:
                # Exponential backoff: 1s, 2s, 4s
                wait_time = 2 ** attempt
                print(f"Error {e.code}, retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise
```

### Jitter

Add randomness to prevent thundering herd:

```python
import random

wait_time = (2 ** attempt) + random.uniform(0, 1)
```

---

## 3. Authentication Basics

### API Keys in Headers

```python
from urllib.request import Request

def make_authenticated_request(url, api_key):
    req = Request(
        url=url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "X-API-Key": api_key,  # Alternative format
        }
    )
    return urlopen(req)
```

### Basic Auth (with base64)

```python
import base64
from urllib.request import Request

def basic_auth_request(url, username, password):
    # Encode credentials
    credentials = f"{username}:{password}".encode()
    encoded = base64.b64encode(credentials).decode()
    
    req = Request(
        url=url,
        headers={
            "Authorization": f"Basic {encoded}"
        }
    )
    return urlopen(req)
```

> ⚠️ **Security Note:** Never hardcode API keys in your code! Use environment variables.

---

## 4. Timeouts

Always set timeouts to prevent hanging:

```python
from urllib.request import urlopen
import socket

# Set global timeout
socket.setdefaulttimeout(10)  # 10 seconds

# Or per-request
req = Request(url)
response = urlopen(req, timeout=10)
```

---

## 5. Connection Pooling (with http.client)

For multiple requests to same server, reuse connections:

```python
import http.client

# Create persistent connection
conn = http.client.HTTPSConnection("api.example.com")

# Make multiple requests
conn.request("GET", "/users")
response1 = conn.getresponse()

conn.request("GET", "/posts")
response2 = conn.getresponse()

conn.close()
```

---

## 6. Logging

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def logged_request(url):
    logger.info(f"Requesting: {url}")
    try:
        response = urlopen(url)
        logger.info(f"Success: {response.status}")
        return response
    except Exception as e:
        logger.error(f"Failed: {e}")
        raise
```

---

## 7. Caching

```python
import time
from functools import lru_cache

class SimpleCache:
    """Simple time-based cache."""
    
    def __init__(self, ttl=300):  # 5 minutes default
        self.ttl = ttl
        self.cache = {}
    
    def get(self, key):
        if key in self.cache:
            value, expiry = self.cache[key]
            if time.time() < expiry:
                return value
            del self.cache[key]
        return None
    
    def set(self, key, value):
        self.cache[key] = (value, time.time() + self.ttl)
```

---

## 8. User-Agent Best Practices

```python
def get_user_agent():
    """Return a descriptive User-Agent string."""
    return (
        "MyApp/1.0 "
        "(Python/3.9; "
        "Contact: developer@example.com)"
    )

# Include contact info so API providers can reach you if there's a problem
```

---

## Quick Reference Checklist

### For API Clients:

- [ ] Set appropriate timeouts
- [ ] Implement retry with exponential backoff
- [ ] Respect rate limits
- [ ] Handle all error cases
- [ ] Use descriptive User-Agent
- [ ] Add logging
- [ ] Consider caching
- [ ] Never expose API keys in code

### For API Servers:

- [ ] Return proper status codes
- [ ] Include rate limit headers
- [ ] Validate all input
- [ ] Return consistent error formats
- [ ] Log requests
- [ ] Support pagination
- [ ] Use HTTPS

---

## Summary

| Practice | Purpose |
|----------|---------|
| Rate Limiting | Don't get banned, be a good citizen |
| Retries | Handle temporary failures |
| Timeouts | Prevent indefinite hangs |
| Authentication | Secure access |
| Caching | Improve performance |
| Logging | Debug issues |
| User-Agent | Identify your client |

---

## Congratulations! 🎉

You've completed the Working with APIs module! You now know how to:

1. ✅ Understand HTTP fundamentals
2. ✅ Make requests with urllib
3. ✅ Parse JSON responses
4. ✅ Build simple APIs
5. ✅ Apply production best practices

**Next Steps:**
- Build a project that uses a real API
- Try the `requests` library (it's much nicer!)
- Learn about async APIs with `aiohttp`
