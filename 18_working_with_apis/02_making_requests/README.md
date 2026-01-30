# 📡 Making Requests

> Making HTTP requests with Python's `urllib`

---

## Introduction

Python's standard library includes `urllib` - a powerful module for making HTTP requests without installing any external packages. While libraries like `requests` are popular, understanding `urllib` gives you insight into how HTTP actually works.

---

## urllib Modules Overview

```python
from urllib.request import urlopen, Request    # Making requests
from urllib.parse import urlencode, quote      # URL encoding
from urllib.error import HTTPError, URLError   # Error handling
```

| Module | Purpose |
|--------|---------|
| `urllib.request` | Open and read URLs |
| `urllib.parse` | Parse and construct URLs |
| `urllib.error` | Exception classes for errors |

---

## Simple GET Request

The simplest way to fetch data:

```python
from urllib.request import urlopen

# Basic GET request
with urlopen("https://api.github.com/events") as response:
    data = response.read()              # Read raw bytes
    text = data.decode("utf-8")          # Convert to string
    print(text[:500])                    # Print first 500 chars
```

> **Always use `with` statement!** It automatically closes the connection.

---

## Adding Headers

Many APIs require specific headers (like User-Agent):

```python
from urllib.request import Request, urlopen

url = "https://api.github.com/events"

# Create request with custom headers
req = Request(
    url=url,
    headers={
        "User-Agent": "Python-urllib/3.9 MyApp/1.0",
        "Accept": "application/json",
    }
)

with urlopen(req) as response:
    data = response.read()
```

Without a proper `User-Agent`, some APIs (including GitHub) may reject your request!

---

## Making POST Requests

POST requests send data to the server:

```python
from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = "https://httpbin.org/post"

# Data to send (as dictionary)
data = {
    "username": "alice",
    "message": "Hello, API!"
}

# Encode data for transmission
encoded_data = urlencode(data).encode("utf-8")

# Create POST request
req = Request(
    url=url,
    data=encoded_data,           # This makes it a POST request
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "MyApp/1.0",
    },
    method="POST"
)

with urlopen(req) as response:
    result = response.read().decode("utf-8")
    print(result)
```

> If you include `data`, it becomes a POST request automatically (unless you specify another method).

---

## Sending JSON Data

Modern APIs often expect JSON:

```python
import json
from urllib.request import Request, urlopen

url = "https://httpbin.org/post"

# JSON data
payload = {
    "name": "Alice",
    "hobbies": ["coding", "reading"]
}

# Convert to JSON bytes
json_data = json.dumps(payload).encode("utf-8")

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
    print(response.read().decode("utf-8"))
```

---

## Reading Response Information

```python
from urllib.request import urlopen

with urlopen("https://api.github.com/events") as response:
    # Status code
    print(f"Status: {response.status}")  # 200
    
    # Response headers (like a dict)
    print(f"Content-Type: {response.getheader('Content-Type')}")
    print(f"All headers: {dict(response.headers)}")
    
    # Response URL (after any redirects)
    print(f"Final URL: {response.url}")
    
    # Read the body
    body = response.read()
    print(f"Body length: {len(body)} bytes")
```

---

## URL Encoding

Special characters in URLs need encoding:

```python
from urllib.parse import quote, quote_plus, urlencode

# Encoding individual strings
query = "hello world & more!"
print(quote(query))         # hello%20world%20%26%20more%21
print(quote_plus(query))    # hello+world+%26+more%21 (spaces become +)

# Encoding dictionary to query string
params = {"q": "python api", "page": 1}
print(urlencode(params))    # q=python+api&page=1
```

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Forgetting to encode data | Special characters break URLs | Use `urlencode()` or `quote()` |
| Not decoding bytes | Get `b'...'` instead of text | Call `.decode("utf-8")` on response |
| Missing User-Agent | APIs may reject request | Always include User-Agent header |
| Forgetting `with` | Connection leaks | Use context manager |
| Not handling errors | App crashes on network issues | Use try/except with urllib.error |

---

## Comparison: urllib vs requests

| Feature | urllib | requests |
|---------|--------|----------|
| Installation | Built-in | `pip install requests` |
| Simple GET | Moderate | Very easy |
| JSON handling | Manual | Automatic |
| Error handling | Manual | Built-in |
| Learning value | High (see how it works) | Lower (magic happens) |

**When to use urllib:**
- No external dependencies allowed
- Learning how HTTP works
- Simple scripts

**When to use requests:**
- Production applications
- Complex authentication
- Automatic JSON handling needed

---

## Quick Reference

```python
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json

# GET with headers
req = Request("https://api.example.com/data", headers={"User-Agent": "MyApp"})
with urlopen(req) as r:
    data = json.loads(r.read().decode())

# POST with form data
data = urlencode({"key": "value"}).encode()
req = Request("https://api.example.com/post", data=data, method="POST")
with urlopen(req) as r:
    response = r.read().decode()

# POST with JSON
json_data = json.dumps({"key": "value"}).encode()
req = Request("https://api.example.com/post", data=json_data, 
              headers={"Content-Type": "application/json"}, method="POST")
```

---

## Next Steps

Now that you can make requests, let's learn to handle the responses properly!

→ Continue to [03: Parsing Responses](../03_parsing_responses/)
