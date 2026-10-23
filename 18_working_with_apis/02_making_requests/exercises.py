"""
Making Requests - Exercises
===========================
Practice making HTTP requests with urllib.
"""

print("=" * 60)
print("MAKING REQUESTS - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: Simple GET Request
# =============================================================================
print("\n--- Exercise 1: Fetch and Display ---\n")
"""
Write a function fetch_url(url) that:
1. Makes a GET request to the given URL
2. Returns the status code and response text
3. Handles any errors gracefully

Test with: https://httpbin.org/get
"""

# Your code here:



# =============================================================================
# EXERCISE 2: Add Query Parameters
# =============================================================================
print("\n--- Exercise 2: Search with Parameters ---\n")
"""
Write a function search(query, page=1) that:
1. Builds a URL to https://httpbin.org/get
2. Adds query parameters: "search" and "page"
3. Makes the GET request
4. Returns the parsed JSON response

Example: search("python", page=2) should call:
https://httpbin.org/get?search=python&page=2
"""

# Your code here:



# =============================================================================
# EXERCISE 3: POST Form Data
# =============================================================================
print("\n--- Exercise 3: Submit Form ---\n")
"""
Write a function submit_form(username, email) that:
1. POSTs to https://httpbin.org/post
2. Sends the username and email as form data
3. Returns the server's response
"""

# Your code here:



# =============================================================================
# EXERCISE 4: POST JSON Data
# =============================================================================
print("\n--- Exercise 4: Create User ---\n")
"""
Write a function create_user(user_dict) that:
1. POSTs to https://httpbin.org/post
2. Sends the user_dict as JSON
3. Sets the proper Content-Type header
4. Returns the server's response

Example user_dict: {"name": "Alice", "role": "admin"}
"""

# Your code here:



# =============================================================================
# EXERCISE 5: Response Info
# =============================================================================
print("\n--- Exercise 5: Inspect Response ---\n")
"""
Write a function get_response_info(url) that:
1. Makes a GET request to the URL
2. Returns a dictionary with:
   - status: the HTTP status code
   - content_type: the Content-Type header
   - content_length: the Content-Length header
   - server: the Server header
   
If a header is missing, use "unknown" as the value.
"""

# Your code here:



# =============================================================================
# EXERCISE 6: API Client Class
# =============================================================================
print("\n--- Exercise 6: Simple API Client ---\n")
"""
Create a SimpleAPIClient class that wraps urllib with a clean interface:

Methods needed:
- __init__(self, base_url, default_headers=None)
- get(self, endpoint, params=None) - Make GET request
- post(self, endpoint, data=None, json_data=None) - Make POST request
- All methods should return (status_code, response_data)

Example usage:
client = SimpleAPIClient("https://httpbin.org")
status, data = client.get("/get", params={"key": "value"})
status, data = client.post("/post", json_data={"name": "test"})
"""

# Your code here:



# =============================================================================
# BONUS EXERCISE: File Download
# =============================================================================
print("\n--- BONUS: Download File ---\n")
"""
Write a function download_file(url, filename) that:
1. Downloads the content from the URL
2. Saves it to a file with the given name
3. Returns the number of bytes saved
4. Handles errors appropriately

Hint: Use response.read() to get bytes, then write to file in binary mode.
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
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

def fetch_url(url):
    """Fetch URL and return status and text."""
    try:
        with urlopen(url) as response:
            return response.status, response.read().decode("utf-8")
    except HTTPError as e:
        return e.code, f"HTTP Error: {e.reason}"
    except URLError as e:
        return None, f"URL Error: {e.reason}"

print("fetch_url() defined. Test with fetch_url('https://httpbin.org/get')")

# Exercise 2 Solution
print("\n--- Exercise 2 Solution ---")
from urllib.request import urlopen
from urllib.parse import urlencode
import json

def search(query, page=1):
    """Search with query parameters."""
    base_url = "https://httpbin.org/get"
    params = {"search": query, "page": page}
    url = f"{base_url}?{urlencode(params)}"
    
    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))

print("search() defined. Test with search('python', page=2)")

# Exercise 3 Solution
print("\n--- Exercise 3 Solution ---")
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json

def submit_form(username, email):
    """Submit form data via POST."""
    url = "https://httpbin.org/post"
    data = urlencode({"username": username, "email": email}).encode("utf-8")
    
    req = Request(
        url=url,
        data=data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "MyApp/1.0",
        },
        method="POST"
    )
    
    with urlopen(req) as response:
        return json.loads(response.read().decode("utf-8"))

print("submit_form() defined. Test with submit_form('alice', 'alice@example.com')")

# Exercise 4 Solution
print("\n--- Exercise 4 Solution ---")
from urllib.request import Request, urlopen
import json

def create_user(user_dict):
    """Create user via JSON POST."""
    url = "https://httpbin.org/post"
    json_data = json.dumps(user_dict).encode("utf-8")
    
    req = Request(
        url=url,
        data=json_data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "MyApp/1.0",
        },
        method="POST"
    )
    
    with urlopen(req) as response:
        return json.loads(response.read().decode("utf-8"))

print("create_user() defined. Test with create_user({'name': 'Alice', 'role': 'admin'})")

# Exercise 5 Solution
print("\n--- Exercise 5 Solution ---")
from urllib.request import urlopen

def get_response_info(url):
    """Get response information as dictionary."""
    with urlopen(url) as response:
        return {
            "status": response.status,
            "content_type": response.getheader("Content-Type", "unknown"),
            "content_length": response.getheader("Content-Length", "unknown"),
            "server": response.getheader("Server", "unknown"),
        }

print("get_response_info() defined. Test with get_response_info('https://httpbin.org/get')")

# Exercise 6 Solution
print("\n--- Exercise 6 Solution ---")
from urllib.request import Request, urlopen
from urllib.parse import urlencode, urljoin
import json

class SimpleAPIClient:
    """Simple API client using urllib."""
    
    def __init__(self, base_url, default_headers=None):
        self.base_url = base_url.rstrip("/")
        self.default_headers = default_headers or {}
        self.default_headers.setdefault("User-Agent", "SimpleAPIClient/1.0")
        self.default_headers.setdefault("Accept", "application/json")
    
    def _make_request(self, endpoint, method="GET", data=None, json_data=None, params=None):
        """Internal method to make requests."""
        # Build URL
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        if params:
            url = f"{url}?{urlencode(params)}"
        
        # Prepare body
        body = None
        headers = dict(self.default_headers)
        
        if json_data is not None:
            body = json.dumps(json_data).encode("utf-8")
            headers["Content-Type"] = "application/json"
        elif data is not None:
            body = urlencode(data).encode("utf-8")
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        
        # Make request
        req = Request(url, data=body, headers=headers, method=method)
        
        with urlopen(req) as response:
            response_body = response.read().decode("utf-8")
            try:
                return response.status, json.loads(response_body)
            except json.JSONDecodeError:
                return response.status, response_body
    
    def get(self, endpoint, params=None):
        """Make a GET request."""
        return self._make_request(endpoint, method="GET", params=params)
    
    def post(self, endpoint, data=None, json_data=None):
        """Make a POST request."""
        return self._make_request(endpoint, method="POST", data=data, json_data=json_data)

print("SimpleAPIClient class defined. Test with:")
print("  client = SimpleAPIClient('https://httpbin.org')")
print("  status, data = client.get('/get', params={'key': 'value'})")

# Bonus Solution
print("\n--- Bonus Solution ---")
from urllib.request import urlopen

def download_file(url, filename):
    """Download a file from URL."""
    try:
        with urlopen(url) as response:
            content = response.read()
            with open(filename, "wb") as f:
                f.write(content)
            return len(content)
    except Exception as e:
        print(f"Download failed: {e}")
        return 0

print("download_file() defined. Test with download_file('https://httpbin.org/bytes/100', 'test_download.bin')")

# =============================================================================
# OFFLINE DEMONSTRATIONS (no network needed)
# =============================================================================
print("\n" + "=" * 60)
print("OFFLINE DEMONSTRATIONS")
print("=" * 60)
print("""
The solutions above call https://httpbin.org when YOU run them.
So that this file also runs anywhere (CI, a classroom, offline),
the demos below temporarily swap urlopen() for a small fake that
simulates the server. Every solution is still the real code from
above - only the network layer is simulated.
""")

import os
import tempfile
from urllib.parse import urlsplit, parse_qs
from urllib.request import urlopen as real_urlopen


class FakeResponse:
    """Minimal stand-in for the object urlopen() returns."""

    def __init__(self, status, headers, body):
        self.status = status
        self._headers = headers
        self._body = body

    def read(self):
        return self._body

    def getheader(self, name, default=None):
        return self._headers.get(name, default)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


def fake_urlopen(target):
    """Simulate httpbin.org: echo the request back as JSON."""
    if isinstance(target, str):
        url, method = target, "GET"
        data, req_headers = b"", {}
    else:  # urllib.request.Request
        url = target.full_url
        method = target.get_method()
        data = target.data or b""
        req_headers = dict(target.header_items())

    parts = urlsplit(url)
    query = {k: v[0] for k, v in parse_qs(parts.query).items()}
    headers = {
        "Content-Type": "application/json",
        "Server": "FakeHTTPBin/1.0",
    }

    # Route: /bytes/<n> - return n raw bytes (used by download_file)
    if parts.path.startswith("/bytes/"):
        n = int(parts.path.rsplit("/", 1)[1])
        body = bytes(range(256)) * (n // 256) + bytes(range(n % 256))
        headers["Content-Type"] = "application/octet-stream"
        headers["Content-Length"] = str(len(body))
        return FakeResponse(200, headers, body)

    # Route: everything else - echo the request, like httpbin does
    payload = {
        "method": method,
        "path": parts.path,
        "args": query,
        "headers": req_headers,
    }
    if data:
        payload["data"] = data.decode("utf-8", "replace")

    body = json.dumps(payload).encode("utf-8")
    headers["Content-Length"] = str(len(body))
    return FakeResponse(200, headers, body)


# Swap the network layer for the fake. Solution functions look up the
# global name urlopen at call time, so this patch takes effect for them.
urlopen = fake_urlopen

# Exercise 1: fetch_url
print("\n--- Demo 1: fetch_url ---")
status, text = fetch_url("https://httpbin.org/get")
print(f"status={status}")
print(f"body starts with: {text[:50]}...")
print("PASS" if status == 200 and '"method": "GET"' in text else "FAIL")

# Exercise 2: search
print("\n--- Demo 2: search ---")
result = search("python", page=2)
print(f"server saw args: {result['args']}")
print("PASS" if result["args"] == {"search": "python", "page": "2"} else "FAIL")

# Exercise 3: submit_form
print("\n--- Demo 3: submit_form ---")
result = submit_form("alice", "alice@example.com")
print(f"server received form data: {result['data']}")
print("PASS" if "username=alice" in result["data"] else "FAIL")

# Exercise 4: create_user
print("\n--- Demo 4: create_user ---")
result = create_user({"name": "Alice", "role": "admin"})
sent = json.loads(result["data"])
headers_lc = {k.lower(): v for k, v in result["headers"].items()}
print(f"server received JSON: {sent}")
print(f"Content-Type sent: {headers_lc.get('content-type')}")
ok = sent == {"name": "Alice", "role": "admin"} and headers_lc.get("content-type") == "application/json"
print("PASS" if ok else "FAIL")

# Exercise 5: get_response_info
print("\n--- Demo 5: get_response_info ---")
info = get_response_info("https://httpbin.org/get")
print(f"response info: {info}")
ok = info["status"] == 200 and info["server"] == "FakeHTTPBin/1.0"
print("PASS" if ok else "FAIL")

# Exercise 6: SimpleAPIClient
print("\n--- Demo 6: SimpleAPIClient ---")
client = SimpleAPIClient("https://httpbin.org")
get_status, get_data = client.get("/get", params={"key": "value"})
print(f"GET  /get  -> status={get_status}, server saw args={get_data['args']}")
post_status, post_data = client.post("/post", json_data={"name": "test"})
print(f"POST /post -> status={post_status}, server received {post_data['data']}")
ok = (
    get_status == 200
    and get_data["args"] == {"key": "value"}
    and json.loads(post_data["data"]) == {"name": "test"}
)
print("PASS" if ok else "FAIL")

# Bonus: download_file
print("\n--- Demo 7: download_file ---")
with tempfile.TemporaryDirectory() as tmp_dir:
    out_path = os.path.join(tmp_dir, "demo_download.bin")
    n_bytes = download_file("https://httpbin.org/bytes/100", out_path)
    print(f"saved {n_bytes} bytes to {out_path}")
    ok = n_bytes == 100 and os.path.getsize(out_path) == 100
print("PASS" if ok else "FAIL")

# Restore the real network function so pasted-into-a-REPL code works as before
urlopen = real_urlopen
print("\n(fake server disconnected; urlopen is back to the real one)")

print("\n" + "=" * 60)
print("All exercises complete! Great job!")
print("=" * 60)
