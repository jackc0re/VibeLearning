"""
Parsing Responses - Examples
============================
Handling JSON, errors, and different response formats.
"""

print("=" * 60)
print("PARSING RESPONSES - Examples")
print("=" * 60)

# =============================================================================
# JSON BASICS
# =============================================================================
print("\n--- JSON Basics ---\n")

import json

# JSON string to Python object (deserialization)
json_string = '''
{
    "name": "Alice",
    "age": 30,
    "is_student": false,
    "courses": ["Python", "JavaScript"],
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}
'''

print("Parsing JSON string:")
data = json.loads(json_string)
print(f"Name: {data['name']}")
print(f"Age: {data['age']}")
print(f"City: {data['address']['city']}")
print(f"Courses: {', '.join(data['courses'])}")

# Python object to JSON string (serialization)
print("\nConverting Python to JSON:")
person = {
    "name": "Bob",
    "skills": ["Python", "APIs", "Testing"],
    "experience": 5,
    "available": True,
}

json_output = json.dumps(person)
print(f"Compact: {json_output}")

# Pretty print JSON
print("\nPretty printed:")
print(json.dumps(person, indent=2))

# =============================================================================
# COMPLETE API REQUEST CYCLE
# =============================================================================
print("\n--- Complete API Request Cycle ---\n")

from urllib.request import urlopen

try:
    # Step 1: Make the request
    url = "https://httpbin.org/get"
    print(f"Fetching: {url}")
    
    with urlopen(url) as response:
        # Step 2: Check status
        print(f"Status: {response.status}")
        
        # Step 3: Read raw bytes
        raw_bytes = response.read()
        print(f"Raw bytes: {len(raw_bytes)} bytes")
        
        # Step 4: Decode to string
        text = raw_bytes.decode("utf-8")
        print(f"Text preview: {text[:200]}...")
        
        # Step 5: Parse JSON
        data = json.loads(text)
        
        # Step 6: Use the data
        print(f"\nParsed data:")
        print(f"  URL: {data['url']}")
        print(f"  Origin: {data['origin']}")
        print(f"  Headers sent: {list(data['headers'].keys())}")
        
except Exception as e:
    print(f"Error: {e}")

# =============================================================================
# ERROR HANDLING
# =============================================================================
print("\n--- Error Handling ---\n")

from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

def safe_request(url, headers=None):
    """Make a request with comprehensive error handling."""
    try:
        req = Request(url, headers=headers or {})
        
        with urlopen(req) as response:
            content_type = response.getheader("Content-Type", "")
            body = response.read().decode("utf-8")
            
            # Try to parse as JSON
            try:
                data = json.loads(body)
            except json.JSONDecodeError:
                data = {"raw_text": body}
            
            return {
                "success": True,
                "status": response.status,
                "data": data
            }
            
    except HTTPError as e:
        # Server returned error status
        error_body = e.read().decode("utf-8")[:500]
        return {
            "success": False,
            "error_type": "HTTPError",
            "status": e.code,
            "reason": e.reason,
            "body_preview": error_body
        }
        
    except URLError as e:
        # Network error
        return {
            "success": False,
            "error_type": "URLError",
            "reason": str(e.reason)
        }
        
    except json.JSONDecodeError as e:
        return {
            "success": False,
            "error_type": "JSONDecodeError",
            "message": str(e)
        }
        
    except Exception as e:
        return {
            "success": False,
            "error_type": "Unexpected",
            "message": str(e)
        }

# Test with various URLs
test_urls = [
    ("https://httpbin.org/get", "Valid URL"),
    ("https://httpbin.org/status/404", "404 Error"),
    ("https://httpbin.org/status/500", "500 Error"),
]

for url, description in test_urls:
    print(f"\nTesting: {description}")
    print(f"URL: {url}")
    result = safe_request(url, headers={"User-Agent": "TestApp"})
    
    if result["success"]:
        print(f"✅ Success! Status: {result['status']}")
    else:
        print(f"❌ {result['error_type']}")
        if 'status' in result:
            print(f"   Status: {result['status']}")
        if 'reason' in result:
            print(f"   Reason: {result['reason']}")

# =============================================================================
# PAGINATION HANDLING
# =============================================================================
print("\n--- Pagination Example ---\n")

# Simulated paginated response
paginated_responses = {
    1: {"items": ["user1", "user2", "user3"], "has_more": True},
    2: {"items": ["user4", "user5"], "has_more": False},
}

def simulate_paginated_request(page):
    """Simulate fetching a paginated API response."""
    return paginated_responses.get(page, {"items": [], "has_more": False})

def fetch_all_items():
    """Fetch all items across all pages."""
    all_items = []
    page = 1
    
    while True:
        print(f"Fetching page {page}...")
        data = simulate_paginated_request(page)
        
        items = data.get("items", [])
        all_items.extend(items)
        
        if not data.get("has_more", False):
            break
            
        page += 1
        
        # Safety limit
        if page > 10:
            print("Reached safety limit")
            break
    
    return all_items

items = fetch_all_items()
print(f"\nTotal items fetched: {len(items)}")
print(f"Items: {items}")

# =============================================================================
# RATE LIMIT HEADERS
# =============================================================================
print("\n--- Rate Limit Headers ---\n")

# Simulated headers like GitHub API
class MockResponse:
    def __init__(self, headers):
        self.headers = headers
    
    def getheader(self, name, default=None):
        return self.headers.get(name, default)

# Example response with rate limit headers
mock_response = MockResponse({
    "X-RateLimit-Limit": "60",
    "X-RateLimit-Remaining": "42",
    "X-RateLimit-Reset": "1609459200",
    "Content-Type": "application/json",
})

def parse_rate_limits(response):
    """Extract rate limit information from response."""
    return {
        "limit": response.getheader("X-RateLimit-Limit", "unknown"),
        "remaining": response.getheader("X-RateLimit-Remaining", "unknown"),
        "reset": response.getheader("X-RateLimit-Reset", "unknown"),
    }

limits = parse_rate_limits(mock_response)
print("Rate Limit Info:")
for key, value in limits.items():
    print(f"  {key}: {value}")

# Calculate usage percentage
try:
    limit = int(limits["limit"])
    remaining = int(limits["remaining"])
    used = limit - remaining
    percentage = (used / limit) * 100
    print(f"\nUsed: {used}/{limit} ({percentage:.1f}%)")
except (ValueError, ZeroDivisionError):
    pass

# =============================================================================
# RESPONSE VALIDATION
# =============================================================================
print("\n--- Response Validation ---\n")

def validate_api_response(data, required_fields, field_types=None):
    """
    Validate that an API response has the expected structure.
    
    Args:
        data: The parsed response data
        required_fields: List of field names that must be present
        field_types: Dict of field_name -> expected type
    """
    errors = []
    
    # Check it's a dict
    if not isinstance(data, dict):
        return False, ["Response is not a dictionary"]
    
    # Check required fields
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    
    # Check field types
    if field_types:
        for field, expected_type in field_types.items():
            if field in data and not isinstance(data[field], expected_type):
                actual_type = type(data[field]).__name__
                errors.append(f"Field '{field}' should be {expected_type.__name__}, got {actual_type}")
    
    return len(errors) == 0, errors

# Test validation
test_cases = [
    ({"id": 1, "name": "Alice", "email": "alice@example.com"}, "Valid user"),
    ({"id": 1, "name": "Bob"}, "Missing email"),
    ({"name": "Charlie", "email": "charlie@example.com"}, "Missing id"),
    ("not a dict", "Not a dictionary"),
]

required = ["id", "name", "email"]
types = {"id": int, "name": str, "email": str}

for data, description in test_cases:
    is_valid, errors = validate_api_response(data, required, types)
    status = "✅ Valid" if is_valid else "❌ Invalid"
    print(f"{status}: {description}")
    if errors:
        for error in errors:
            print(f"   - {error}")

# =============================================================================
# WORKING WITH CSV RESPONSES
# =============================================================================
print("\n--- CSV Response Parsing ---\n")

import csv
from io import StringIO

# Simulate CSV data from an API
csv_data = """id,name,role,active
1,Alice,admin,true
2,Bob,developer,true
3,Charlie,designer,false"""

print("Parsing CSV data:")
reader = csv.DictReader(StringIO(csv_data))
for row in reader:
    status = "✅" if row["active"] == "true" else "❌"
    print(f"  {status} {row['name']} ({row['role']})")

# =============================================================================
# SAFE JSON PARSING
# =============================================================================
print("\n--- Safe JSON Parsing ---\n")

def safe_json_loads(text, default=None):
    """
    Safely parse JSON, return default on error.
    
    Args:
        text: JSON string to parse
        default: Value to return if parsing fails
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
        return default

# Test cases
json_tests = [
    ('{"valid": "json"}', "Valid JSON"),
    ("not json", "Invalid JSON"),
    ('{"incomplete": ', "Incomplete JSON"),
]

for text, description in json_tests:
    result = safe_json_loads(text, default={"error": "Parse failed"})
    print(f"{description}: {result}")

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Use json.loads() to parse JSON strings into Python objects
2. Use json.dumps() to convert Python objects to JSON
3. Always wrap json.loads() in try/except for robust error handling
4. Check response.status before parsing
5. Use response.getheader() to access metadata like rate limits
6. Handle pagination by looking for "next" links or has_more flags
7. Validate responses match expected structure before using
8. Different APIs return different formats - be prepared!
""")

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
