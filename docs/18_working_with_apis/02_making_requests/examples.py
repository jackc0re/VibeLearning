"""
Making Requests - Examples
==========================
Using urllib to make GET and POST requests.
"""

print("=" * 60)
print("MAKING REQUESTS - Examples")
print("=" * 60)

# =============================================================================
# SIMPLE GET REQUEST
# =============================================================================
print("\n--- Simple GET Request ---\n")

from urllib.request import urlopen

try:
    # Using httpbin.org for testing - it echoes back your request
    url = "https://httpbin.org/get"
    
    print(f"Fetching: {url}")
    with urlopen(url) as response:
        data = response.read()
        text = data.decode("utf-8")
        print(f"Status: {response.status}")
        print(f"Response (first 500 chars):")
        print(text[:500])
except Exception as e:
    print(f"Error: {e}")
    print("Note: Internet connection required for live examples")

# =============================================================================
# GET WITH CUSTOM HEADERS
# =============================================================================
print("\n--- GET with Custom Headers ---\n")

from urllib.request import Request, urlopen

try:
    url = "https://httpbin.org/headers"
    
    # Create a request object to add headers
    req = Request(
        url=url,
        headers={
            "User-Agent": "Python-urllib/3.9 MyApp/1.0",
            "Accept": "application/json",
            "X-Custom-Header": "MyValue"
        }
    )
    
    print(f"Fetching: {url}")
    print(f"Headers sent: {dict(req.header_items())}")
    
    with urlopen(req) as response:
        result = response.read().decode("utf-8")
        print("\nhttpbin echoes back the headers we sent:")
        print(result[:600])
        
except Exception as e:
    print(f"Error: {e}")

# =============================================================================
# POST REQUEST WITH FORM DATA
# =============================================================================
print("\n--- POST Request with Form Data ---\n")

from urllib.request import Request, urlopen
from urllib.parse import urlencode

try:
    url = "https://httpbin.org/post"
    
    # Data to send
    form_data = {
        "username": "alice",
        "password": "secret123",
        "remember_me": "true"
    }
    
    # Encode the data
    encoded_data = urlencode(form_data).encode("utf-8")
    
    # Create POST request
    req = Request(
        url=url,
        data=encoded_data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "MyApp/1.0",
        },
        method="POST"
    )
    
    print(f"POSTing to: {url}")
    print(f"Data: {form_data}")
    
    with urlopen(req) as response:
        result = response.read().decode("utf-8")
        print("\nResponse (formatted excerpt):")
        # Find and show the form data part
        import json
        response_json = json.loads(result)
        print(f"Server received form: {response_json.get('form', {})}")
        
except Exception as e:
    print(f"Error: {e}")

# =============================================================================
# POST REQUEST WITH JSON
# =============================================================================
print("\n--- POST Request with JSON ---\n")

import json
from urllib.request import Request, urlopen

try:
    url = "https://httpbin.org/post"
    
    # JSON payload
    payload = {
        "user": {
            "name": "Bob",
            "email": "bob@example.com"
        },
        "preferences": {
            "theme": "dark",
            "notifications": True
        }
    }
    
    # Convert to JSON bytes
    json_data = json.dumps(payload).encode("utf-8")
    
    req = Request(
        url=url,
        data=json_data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "MyApp/1.0",
            "Accept": "application/json",
        },
        method="POST"
    )
    
    print(f"POSTing JSON to: {url}")
    print(f"Payload: {json.dumps(payload, indent=2)[:300]}...")
    
    with urlopen(req) as response:
        result = response.read().decode("utf-8")
        response_json = json.loads(result)
        print("\nServer received JSON:")
        print(json.dumps(response_json.get('json', {}), indent=2)[:400])
        
except Exception as e:
    print(f"Error: {e}")

# =============================================================================
# URL ENCODING EXAMPLES
# =============================================================================
print("\n--- URL Encoding ---\n")

from urllib.parse import quote, quote_plus, urlencode

# Encoding special characters
texts = [
    "hello world",
    "price=$100",
    "q=python & programming!",
    "café naïve",
]

print("URL Encoding Examples:")
for text in texts:
    print(f"  Original:     {text}")
    print(f"  quote():      {quote(text)}")
    print(f"  quote_plus(): {quote_plus(text)}")
    print()

# Building query strings
params = {
    "search": "python tutorials",
    "category": "programming",
    "page": 1,
    "sort": "newest"
}
query_string = urlencode(params)
print(f"Query string: {query_string}")

# =============================================================================
# READING RESPONSE INFORMATION
# =============================================================================
print("\n--- Reading Response Information ---\n")

try:
    url = "https://httpbin.org/get"
    
    with urlopen(url) as response:
        print(f"Status Code:       {response.status}")
        print(f"Status Message:    {response.reason}")
        print(f"Final URL:         {response.url}")
        print(f"Content-Type:      {response.getheader('Content-Type')}")
        print(f"Content-Length:    {response.getheader('Content-Length')} bytes")
        print(f"Server:            {response.getheader('Server')}")
        print(f"Date:              {response.getheader('Date')}")
        
        # All headers as dictionary
        print(f"\nAll Headers:")
        for header, value in response.headers.items():
            print(f"  {header}: {value}")
            
except Exception as e:
    print(f"Error: {e}")

# =============================================================================
# DIFFERENT HTTP METHODS
# =============================================================================
print("\n--- Different HTTP Methods ---\n")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

for method in methods:
    try:
        # httpbin has endpoints for each method
        url = f"https://httpbin.org/{method.lower()}"
        
        # For methods other than GET, we need to specify the method
        if method == "GET":
            req = Request(url)
        else:
            req = Request(url, data=b"", method=method)
        
        with urlopen(req) as response:
            print(f"{method:6} -> {url}: Status {response.status}")
            
    except Exception as e:
        print(f"{method:6} -> {url}: Error - {e}")

# =============================================================================
# BUILDING A REUSABLE REQUEST FUNCTION
# =============================================================================
print("\n--- Reusable Request Function ---\n")

import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

def make_request(url, method="GET", data=None, headers=None, json_data=None):
    """
    Make an HTTP request with proper error handling.
    
    Args:
        url: The URL to request
        method: HTTP method (GET, POST, PUT, DELETE, etc.)
        data: Form data (dict) to send
        headers: Additional headers (dict)
        json_data: JSON-serializable data to send as body
    
    Returns:
        tuple: (status_code, response_data or error_message)
    """
    # Default headers
    default_headers = {
        "User-Agent": "Python-urllib/3.9 ExampleApp/1.0",
        "Accept": "application/json",
    }
    
    if headers:
        default_headers.update(headers)
    
    # Prepare request body
    body = None
    if json_data is not None:
        body = json.dumps(json_data).encode("utf-8")
        default_headers["Content-Type"] = "application/json"
    elif data is not None:
        from urllib.parse import urlencode
        body = urlencode(data).encode("utf-8")
        default_headers["Content-Type"] = "application/x-www-form-urlencoded"
    
    # Create request
    req = Request(url, data=body, headers=default_headers, method=method)
    
    try:
        with urlopen(req) as response:
            response_body = response.read().decode("utf-8")
            try:
                # Try to parse as JSON
                return response.status, json.loads(response_body)
            except json.JSONDecodeError:
                return response.status, response_body
                
    except HTTPError as e:
        # Server returned an error status
        error_body = e.read().decode("utf-8")
        return e.code, f"HTTP Error: {error_body[:200]}"
        
    except URLError as e:
        # Network error
        return None, f"URL Error: {e.reason}"
        
    except Exception as e:
        return None, f"Error: {str(e)}"

# Test the function
try:
    # GET request
    status, data = make_request("https://httpbin.org/get")
    print(f"GET Status: {status}")
    
    # POST with JSON
    status, data = make_request(
        "https://httpbin.org/post",
        method="POST",
        json_data={"test": "data"}
    )
    print(f"POST Status: {status}")
    if isinstance(data, dict) and "json" in data:
        print(f"Echoed back: {data['json']}")
        
except Exception as e:
    print(f"Function test error: {e}")

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Use urlopen() for simple GET requests
2. Use Request() to add headers or change methods
3. Always encode data before sending (urlencode for forms, json.dumps for JSON)
4. Always decode response bytes to strings (.decode("utf-8"))
5. Use with statement for automatic connection cleanup
6. Handle errors with try/except (HTTPError, URLError)
7. Include User-Agent header to avoid being blocked
""")

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
