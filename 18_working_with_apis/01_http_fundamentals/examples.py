"""
HTTP Fundamentals - Examples
============================
Understanding URLs, methods, status codes, and headers.
"""

print("=" * 60)
print("HTTP FUNDAMENTALS - Examples")
print("=" * 60)

# =============================================================================
# URL PARSING
# =============================================================================
print("\n--- URL Parsing with urllib.parse ---\n")

from urllib.parse import urlparse, parse_qs, urlencode

# Example URLs to parse
urls = [
    "https://api.github.com/users/octocat",
    "https://api.example.com:8080/users?id=123&sort=date",
    "http://localhost:3000/api/v1/posts?page=1&limit=10",
]

for url in urls:
    print(f"URL: {url}")
    parsed = urlparse(url)
    print(f"  Scheme:   {parsed.scheme}")
    print(f"  Host:     {parsed.hostname}")
    print(f"  Port:     {parsed.port}")
    print(f"  Path:     {parsed.path}")
    print(f"  Query:    {parsed.query}")
    
    # Parse query parameters into a dictionary
    if parsed.query:
        params = parse_qs(parsed.query)
        print(f"  Params:   {params}")
    print()

# =============================================================================
# BUILDING URLs
# =============================================================================
print("\n--- Building URLs with Query Parameters ---\n")

from urllib.parse import urlunparse

# Building a URL from components
scheme = "https"
netloc = "api.example.com"
path = "/search"
params = ""
query = urlencode({"q": "python programming", "page": 1})
fragment = ""

full_url = urlunparse((scheme, netloc, path, params, query, fragment))
print(f"Built URL: {full_url}")

# =============================================================================
# HTTP STATUS CODE CATEGORIES
# =============================================================================
print("\n--- HTTP Status Code Categories ---\n")

def categorize_status(code):
    """Return the category of an HTTP status code."""
    if 100 <= code < 200:
        return "Informational"
    elif 200 <= code < 300:
        return "Success"
    elif 300 <= code < 400:
        return "Redirection"
    elif 400 <= code < 500:
        return "Client Error"
    elif 500 <= code < 600:
        return "Server Error"
    return "Unknown"

# Test various status codes
test_codes = [200, 201, 301, 404, 500, 418]

for code in test_codes:
    category = categorize_status(code)
    print(f"Status {code}: {category}")

# =============================================================================
# COMMON STATUS CODES
# =============================================================================
print("\n--- Common HTTP Status Codes ---\n")

STATUS_CODES = {
    # Success
    200: "OK - Request succeeded",
    201: "Created - Resource was created",
    204: "No Content - Success, nothing to return",
    # Redirection
    301: "Moved Permanently - Resource has new URL",
    302: "Found - Temporary redirect",
    304: "Not Modified - Use cached version",
    # Client Errors
    400: "Bad Request - Malformed request",
    401: "Unauthorized - Need to authenticate",
    403: "Forbidden - No permission",
    404: "Not Found - Resource doesn't exist",
    429: "Too Many Requests - Rate limited",
    # Server Errors
    500: "Internal Server Error - Server crashed",
    502: "Bad Gateway - Invalid upstream response",
    503: "Service Unavailable - Server overloaded",
    504: "Gateway Timeout - Upstream timeout",
}

for code, description in STATUS_CODES.items():
    print(f"{code}: {description}")

# =============================================================================
# HTTP METHODS
# =============================================================================
print("\n--- HTTP Methods Reference ---\n")

HTTP_METHODS = {
    "GET": {
        "purpose": "Retrieve data",
        "safe": True,
        "idempotent": True,
        "analogy": "Looking at a menu",
    },
    "POST": {
        "purpose": "Create new resource",
        "safe": False,
        "idempotent": False,
        "analogy": "Placing an order",
    },
    "PUT": {
        "purpose": "Update/replace resource",
        "safe": False,
        "idempotent": True,
        "analogy": "Changing your entire order",
    },
    "PATCH": {
        "purpose": "Partial update",
        "safe": False,
        "idempotent": False,
        "analogy": "Adding a side dish",
    },
    "DELETE": {
        "purpose": "Remove resource",
        "safe": False,
        "idempotent": True,
        "analogy": "Canceling your order",
    },
}

for method, info in HTTP_METHODS.items():
    print(f"{method}:")
    print(f"  Purpose:     {info['purpose']}")
    print(f"  Safe:        {info['safe']} (doesn't modify server)")
    print(f"  Idempotent:  {info['idempotent']} (same result if repeated)")
    print(f"  Analogy:     {info['analogy']}")
    print()

# =============================================================================
# SIMULATING HTTP HEADERS
# =============================================================================
print("\n--- HTTP Headers Example ---\n")

# Example request headers
request_headers = {
    "User-Agent": "Python-urllib/3.9 MyApp/1.0",
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Host": "api.example.com",
}

print("Typical Request Headers:")
for header, value in request_headers.items():
    print(f"  {header}: {value}")

# Example response headers
response_headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Content-Length": "1024",
    "Date": "Wed, 21 Oct 2025 07:28:00 GMT",
    "Server": "nginx/1.18.0",
    "Cache-Control": "max-age=3600",
}

print("\nTypical Response Headers:")
for header, value in response_headers.items():
    print(f"  {header}: {value}")

# =============================================================================
# PRACTICAL: Checking if a Request Succeeded
# =============================================================================
print("\n--- Practical: Handling Status Codes ---\n")

def is_success(status_code):
    """Check if status code indicates success."""
    return 200 <= status_code < 300

def is_redirect(status_code):
    """Check if status code indicates redirection."""
    return 300 <= status_code < 400

def is_client_error(status_code):
    """Check if status code indicates client error."""
    return 400 <= status_code < 500

def is_server_error(status_code):
    """Check if status code indicates server error."""
    return 500 <= status_code < 600

def get_error_message(status_code):
    """Get a user-friendly error message for status codes."""
    if is_success(status_code):
        return "Success!"
    elif status_code == 404:
        return "Not found - check your URL"
    elif status_code == 401:
        return "Unauthorized - you need to log in"
    elif status_code == 403:
        return "Forbidden - you don't have permission"
    elif status_code == 429:
        return "Rate limited - slow down your requests"
    elif status_code == 500:
        return "Server error - try again later"
    elif is_client_error(status_code):
        return f"Client error {status_code}"
    elif is_server_error(status_code):
        return f"Server error {status_code}"
    return f"Unknown status: {status_code}"

# Test the functions
test_statuses = [200, 404, 500, 401, 301]
for status in test_statuses:
    message = get_error_message(status)
    print(f"Status {status}: {message}")

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. URLs have structure: scheme://host:port/path?query#fragment
2. HTTP Methods define action: GET (read), POST (create), PUT/PATCH (update), DELETE
3. Status codes tell you what happened:
   - 2xx = Success
   - 3xx = Redirect
   - 4xx = Your fault (client error)
   - 5xx = Server's fault
4. Headers carry metadata about the request/response
5. urllib.parse helps you build and parse URLs safely
""")

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
