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

print("\n" + "=" * 60)
print("All exercises complete! Great job!")
print("=" * 60)
