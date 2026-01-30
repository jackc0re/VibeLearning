"""
HTTP Fundamentals - Exercises
=============================
Practice URL parsing, status codes, and HTTP concepts.
"""

print("=" * 60)
print("HTTP FUNDAMENTALS - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: Parse a Complex URL
# =============================================================================
print("\n--- Exercise 1: URL Parser ---\n")
"""
Given the URL below, extract and print all its components:
- scheme
- hostname  
- port (if specified, otherwise say "default")
- path
- query parameters (as a dictionary)

URL: https://api.weather.com:8443/v1/current?city=London&units=metric

Expected output format:
Scheme: https
Host: api.weather.com
Port: 8444
Path: /v1/current
Query: {'city': ['London'], 'units': ['metric']}
"""

url = "https://api.weather.com:8443/v1/current?city=London&units=metric"

# Your code here:



# =============================================================================
# EXERCISE 2: Status Code Classifier
# =============================================================================
print("\n--- Exercise 2: Status Code Classifier ---\n")
"""
Write a function classify_status(status_code) that returns:
- "Success" for 2xx codes
- "Redirect" for 3xx codes
- "Client Error" for 4xx codes
- "Server Error" for 5xx codes
- "Invalid" for anything else

Then test it with these codes: 200, 301, 404, 500, 100, 999
"""

# Your code here:



# =============================================================================
# EXERCISE 3: Build a Search URL
# =============================================================================
print("\n--- Exercise 3: Build Search URL ---\n")
"""
Build a complete search URL from components.

Given:
- Base: https://search.example.com
- Path: /api/search
- Query parameters: query="python tutorials", page=1, limit=20

Build and print the complete URL with properly encoded parameters.

Expected: https://search.example.com/api/search?query=python+tutorials&page=1&limit=20
"""

base = "https://search.example.com"
path = "/api/search"
params = {"query": "python tutorials", "page": 1, "limit": 20}

# Your code here:



# =============================================================================
# EXERCISE 4: HTTP Method Matcher
# =============================================================================
print("\n--- Exercise 4: Method Matcher ---\n")
"""
Create a dictionary that maps HTTP methods to their typical use cases.
Then write a function get_method_description(method) that returns
a description for any given method.

Methods to include: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS
"""

# Your code here:



# =============================================================================
# EXERCISE 5: Create Request Headers
# =============================================================================
print("\n--- Exercise 5: Create Request Headers ---\n")
"""
Create a function create_headers(user_agent, accept_format, api_key=None)
that returns a dictionary of HTTP headers.

If api_key is provided, include an Authorization header with "Bearer {api_key}"

Example output:
{
    "User-Agent": "MyApp/1.0",
    "Accept": "application/json",
    "Authorization": "Bearer secret123"  # only if api_key provided
}
"""

# Your code here:



# =============================================================================
# EXERCISE 6: Status Code Handler
# =============================================================================
print("\n--- Exercise 6: Smart Error Handler ---\n")
"""
Write a function handle_response(status_code, retry_count=0) that:
- Returns "Success" for 2xx codes
- Returns "Retry" for 5xx codes (server errors are worth retrying)
- Returns "Check Request" for 4xx codes
- Returns "Follow Redirect" for 3xx codes
- For 429 (Too Many Requests), return "Rate Limited - Wait"
- For 500+ with retry_count >= 3, return "Giving up after 3 retries"
"""

# Your code here:



# =============================================================================
# BONUS EXERCISE: URL Validator
# =============================================================================
print("\n--- BONUS: URL Validator ---\n")
"""
Write a function is_valid_api_url(url) that checks if a URL:
1. Uses https:// (not http:// for APIs!)
2. Has a hostname
3. Has a path that starts with "/api" or "/v"

Return True if valid, False otherwise.
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
from urllib.parse import urlparse, parse_qs

url = "https://api.weather.com:8443/v1/current?city=London&units=metric"
parsed = urlparse(url)

print(f"Scheme: {parsed.scheme}")
print(f"Host: {parsed.hostname}")
print(f"Port: {parsed.port if parsed.port else 'default'}")
print(f"Path: {parsed.path}")
print(f"Query: {parse_qs(parsed.query)}")

# Exercise 2 Solution
print("\n--- Exercise 2 Solution ---")
def classify_status(code):
    if 200 <= code < 300:
        return "Success"
    elif 300 <= code < 400:
        return "Redirect"
    elif 400 <= code < 500:
        return "Client Error"
    elif 500 <= code < 600:
        return "Server Error"
    return "Invalid"

test_codes = [200, 301, 404, 500, 100, 999]
for code in test_codes:
    print(f"{code}: {classify_status(code)}")

# Exercise 3 Solution
print("\n--- Exercise 3 Solution ---")
from urllib.parse import urlencode, urlunparse

base = "https://search.example.com"
path = "/api/search"
params = {"query": "python tutorials", "page": 1, "limit": 20}

# Parse base to get components
base_parsed = urlparse(base)
query_string = urlencode(params)
full_url = urlunparse((
    base_parsed.scheme,
    base_parsed.netloc,
    path,
    "",
    query_string,
    ""
))
print(f"Full URL: {full_url}")

# Exercise 4 Solution
print("\n--- Exercise 4 Solution ---")
METHOD_DESCRIPTIONS = {
    "GET": "Retrieve a resource",
    "POST": "Create a new resource",
    "PUT": "Update/replace a resource",
    "PATCH": "Partially update a resource",
    "DELETE": "Remove a resource",
    "HEAD": "Get headers only (no body)",
    "OPTIONS": "Get supported methods",
}

def get_method_description(method):
    return METHOD_DESCRIPTIONS.get(method.upper(), "Unknown method")

for method in ["GET", "POST", "DELETE", "UNKNOWN"]:
    print(f"{method}: {get_method_description(method)}")

# Exercise 5 Solution
print("\n--- Exercise 5 Solution ---")
def create_headers(user_agent, accept_format, api_key=None):
    headers = {
        "User-Agent": user_agent,
        "Accept": accept_format,
    }
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    return headers

print("Without API key:")
print(create_headers("MyApp/1.0", "application/json"))

print("\nWith API key:")
print(create_headers("MyApp/1.0", "application/json", "secret123"))

# Exercise 6 Solution
print("\n--- Exercise 6 Solution ---")
def handle_response(status_code, retry_count=0):
    if 200 <= status_code < 300:
        return "Success"
    elif status_code == 429:
        return "Rate Limited - Wait"
    elif 300 <= status_code < 400:
        return "Follow Redirect"
    elif 400 <= status_code < 500:
        return "Check Request"
    elif 500 <= status_code < 600:
        if retry_count >= 3:
            return "Giving up after 3 retries"
        return "Retry"
    return "Unknown"

test_cases = [
    (200, 0), (404, 0), (503, 0), (503, 3), (429, 0), (301, 0)
]
for status, retries in test_cases:
    result = handle_response(status, retries)
    print(f"Status {status}, Retry {retries}: {result}")

# Bonus Solution
print("\n--- Bonus Solution ---")
def is_valid_api_url(url):
    parsed = urlparse(url)
    if parsed.scheme != "https":
        return False
    if not parsed.hostname:
        return False
    if not (parsed.path.startswith("/api") or parsed.path.startswith("/v")):
        return False
    return True

test_urls = [
    "https://api.example.com/v1/users",
    "http://api.example.com/v1/users",  # Wrong scheme
    "https://example.com/users",  # Wrong path
    "https:///v1/users",  # No hostname
]
for url in test_urls:
    print(f"{url}: {is_valid_api_url(url)}")

print("\n" + "=" * 60)
print("All exercises complete! Well done!")
print("=" * 60)
