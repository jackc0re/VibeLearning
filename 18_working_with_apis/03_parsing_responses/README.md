# 📄 Parsing Responses

> Handling JSON, errors, and response data

---

## Introduction

Making requests is only half the battle—you also need to handle what comes back! This topic covers parsing JSON responses, handling errors gracefully, and working with different response formats.

---

## JSON: The Universal API Language

Most modern APIs return data in **JSON** (JavaScript Object Notation) format. Python's `json` module makes working with JSON easy:

```python
import json

# JSON string to Python object (parsing)
json_string = '{"name": "Alice", "age": 30}'
data = json.loads(json_string)
print(data["name"])  # Alice

# Python object to JSON string (serializing)
person = {"name": "Bob", "hobbies": ["coding", "reading"]}
json_output = json.dumps(person)
print(json_output)  # {"name": "Bob", "hobbies": ["coding", "reading"]}
```

### Complete API Response Cycle

```python
import json
from urllib.request import urlopen

# 1. Make request
with urlopen("https://api.github.com/events") as response:
    # 2. Read bytes
    raw_data = response.read()
    
    # 3. Decode to string
    text = raw_data.decode("utf-8")
    
    # 4. Parse JSON
    data = json.loads(text)
    
    # 5. Use the data
    print(f"Got {len(data)} events")
    print(f"First event type: {data[0]['type']}")
```

---

## Handling Errors

Network requests can fail in many ways. Always use try/except:

```python
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import json

def safe_api_call(url):
    try:
        with urlopen(url) as response:
            # Check status first
            if response.status == 200:
                return json.loads(response.read().decode("utf-8"))
            else:
                return {"error": f"Unexpected status: {response.status}"}
                
    except HTTPError as e:
        # Server returned an error status (4xx, 5xx)
        return {
            "error": f"HTTP {e.code}: {e.reason}",
            "url": e.url
        }
        
    except URLError as e:
        # Network error (no connection, DNS failure, etc.)
        return {"error": f"Network error: {e.reason}"}
        
    except json.JSONDecodeError as e:
        # Response wasn't valid JSON
        return {"error": f"Invalid JSON: {e}"}
        
    except Exception as e:
        # Catch-all for unexpected errors
        return {"error": f"Unexpected: {e}"}
```

---

## HTTP Error Categories

| Error Type | When It Happens | How to Handle |
|------------|-----------------|---------------|
| `HTTPError` | Server returns 4xx/5xx status | Check `e.code`, read `e.read()` for details |
| `URLError` | Network/connectivity issues | Check `e.reason`, retry or notify user |
| `TimeoutError` | Request takes too long | Implement timeout, retry with backoff |
| `JSONDecodeError` | Response isn't valid JSON | Check Content-Type, handle gracefully |

---

## Common Response Patterns

### Pagination

APIs often return data in pages:

```python
def fetch_all_pages(base_url):
    """Fetch all paginated results."""
    all_items = []
    page = 1
    
    while True:
        url = f"{base_url}?page={page}&per_page=100"
        
        with urlopen(url) as response:
            data = json.loads(response.read().decode("utf-8"))
            
        items = data.get("items", [])
        if not items:
            break
            
        all_items.extend(items)
        
        # Check if there are more pages
        if len(items) < 100:
            break
            
        page += 1
    
    return all_items
```

### Rate Limiting Headers

```python
def check_rate_limit(response):
    """Extract rate limit info from response headers."""
    return {
        "limit": response.getheader("X-RateLimit-Limit"),
        "remaining": response.getheader("X-RateLimit-Remaining"),
        "reset": response.getheader("X-RateLimit-Reset"),
    }

# Usage
with urlopen("https://api.github.com/events") as response:
    limits = check_rate_limit(response)
    print(f"Remaining: {limits['remaining']}/{limits['limit']}")
```

---

## Working with Different Formats

While JSON is most common, APIs might return other formats:

### Plain Text

```python
with urlopen("https://httpbin.org/ip") as response:
    text = response.read().decode("utf-8")
    print(text)  # {"origin": "123.45.67.89"}
```

### XML (with standard library)

```python
import xml.etree.ElementTree as ET

xml_data = """<?xml version="1.0"?>
<user>
    <name>Alice</name>
    <age>30</age>
</user>"""

root = ET.fromstring(xml_data)
name = root.find("name").text
```

### CSV Data

```python
import csv
from io import StringIO

# If API returns CSV
csv_text = "name,age\nAlice,30\nBob,25"
reader = csv.DictReader(StringIO(csv_text))
for row in reader:
    print(row["name"])  # Alice, then Bob
```

---

## Response Validation

Always validate API responses:

```python
def validate_user_response(data):
    """Check if response has expected structure."""
    required_fields = ["id", "name", "email"]
    
    if not isinstance(data, dict):
        return False, "Response is not an object"
    
    missing = [f for f in required_fields if f not in data]
    if missing:
        return False, f"Missing fields: {missing}"
    
    return True, "Valid"

# Usage
with urlopen(url) as response:
    data = json.loads(response.read().decode())
    is_valid, message = validate_user_response(data)
    if not is_valid:
        print(f"Invalid response: {message}")
```

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Not checking status code | 404 errors look like success | Always check `response.status` |
| Assuming JSON format | HTML error pages break parsing | Use try/except around `json.loads()` |
| Ignoring encoding | Strange characters in text | Always decode: `.decode("utf-8")` |
| Not handling pagination | Only getting first page | Check for `next` links or page counts |
| Silent failures | Errors go unnoticed | Log all errors, show user-friendly messages |

---

## Quick Reference

```python
import json
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

def api_get(url):
    """Robust API GET with error handling."""
    try:
        with urlopen(url) as response:
            if response.status != 200:
                return {"error": f"HTTP {response.status}"}
            
            content_type = response.getheader("Content-Type", "")
            
            if "application/json" in content_type:
                return json.loads(response.read().decode("utf-8"))
            else:
                return {"text": response.read().decode("utf-8")}
                
    except HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}"}
    except URLError as e:
        return {"error": f"Network error: {e.reason}"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response"}
```

---

## Next Steps

Now that you can parse responses, let's build our own API server!

→ Continue to [04: Building Simple API](../04_building_simple_api/)
