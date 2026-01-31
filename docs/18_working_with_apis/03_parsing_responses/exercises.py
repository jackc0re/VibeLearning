"""
Parsing Responses - Exercises
=============================
Practice handling JSON, errors, and response validation.
"""

print("=" * 60)
print("PARSING RESPONSES - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: JSON Parser Function
# =============================================================================
print("\n--- Exercise 1: JSON Parser ---\n")
"""
Write a function parse_json_response(text) that:
1. Takes a JSON string
2. Returns the parsed Python object
3. Returns {"error": "Invalid JSON", "details": str(e)} if parsing fails

Test with:
- '{"name": "Alice", "age": 30}' (valid)
- 'not json' (invalid)
- '{"incomplete": ' (invalid)
"""

# Your code here:



# =============================================================================
# EXERCISE 2: Safe API Getter
# =============================================================================
print("\n--- Exercise 2: Safe API Getter ---\n")
"""
Write a function safe_get(url) that:
1. Makes a GET request to the URL
2. Returns a dictionary with:
   - success: True/False
   - data: parsed JSON (if success)
   - error: error message (if failed)
   - status: HTTP status code
3. Handles all common errors (HTTPError, URLError, JSONDecodeError)
"""

# Your code here:



# =============================================================================
# EXERCISE 3: Response Validator
# =============================================================================
print("\n--- Exercise 3: Response Validator ---\n")
"""
Write a function validate_user(data) that validates a user object:

Required fields: id (int), name (str), email (str)
Optional field: active (bool)

Return: (is_valid, list_of_errors)

Examples:
{"id": 1, "name": "Alice", "email": "a@b.com"} -> (True, [])
{"id": "1", "name": "Bob"} -> (False, ["id should be int", "missing email"])
"""

# Your code here:



# =============================================================================
# EXERCISE 4: Extract Nested Data
# =============================================================================
print("\n--- Exercise 4: Extract Nested Data ---\n")
"""
Given this nested structure (like from a weather API):
{
    "location": {"name": "London", "country": "UK"},
    "current": {"temp_c": 15, "condition": {"text": "Cloudy"}},
    "forecast": {"days": [{"date": "2025-01-01", "max_temp": 18}]}
}

Write a function get_weather_summary(data) that returns:
"London, UK: 15°C, Cloudy. Tomorrow's high: 18°C"

Handle missing data gracefully by using "Unknown" for missing values.
"""

# Your code here:



# =============================================================================
# EXERCISE 5: Paginated Fetcher
# =============================================================================
print("\n--- Exercise 5: Paginated Fetcher ---\n")
"""
Write a function fetch_all_pages(fetch_page_func) that:
1. Calls fetch_page_func(page_num) repeatedly
2. Each call returns {"items": [...], "has_more": True/False}
3. Collects all items across all pages
4. Stops when has_more is False or after 100 pages (safety limit)

Note: This uses a simulated function since we're not making real API calls
"""

# Your code here:



# =============================================================================
# EXERCISE 6: Rate Limit Checker
# =============================================================================
print("\n--- Exercise 6: Rate Limit Checker ---\n")
"""
Write a function check_rate_limit_status(headers_dict) that:
1. Takes a dictionary of response headers
2. Returns a dictionary with:
   - limit: total allowed requests
   - remaining: requests left
   - used: requests used
   - percentage_used: percentage (as float)
   - should_slow_down: True if percentage > 80%

Headers format: {"X-RateLimit-Limit": "100", "X-RateLimit-Remaining": "20"}
"""

# Your code here:



# =============================================================================
# BONUS EXERCISE: Data Transformer
# =============================================================================
print("\n--- BONUS: Data Transformer ---\n")
"""
Write a function transform_api_response(raw_data) that converts API data
to a standardized format.

Input format (varies):
{"user_name": "Alice", "user_age": 30, "user_email": "alice@test.com"}
or
{"name": "Bob", "age": 25, "contact": {"email": "bob@test.com"}}

Output format (standardized):
{"name": "...", "age": ..., "email": "..."}

The function should handle both input formats and produce consistent output.
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
import json

def parse_json_response(text):
    """Parse JSON string safely."""
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        return {"error": "Invalid JSON", "details": str(e)}

# Test
tests = [
    '{"name": "Alice", "age": 30}',
    'not json',
    '{"incomplete": ',
]
for test in tests:
    result = parse_json_response(test)
    print(f"Input: {test[:30]}...")
    print(f"Result: {result}")
    print()

# Exercise 2 Solution
print("--- Exercise 2 Solution ---")
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

def safe_get(url):
    """Make a safe GET request."""
    try:
        req = Request(url, headers={"User-Agent": "SafeGetter/1.0"})
        with urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))
            return {
                "success": True,
                "data": data,
                "status": response.status
            }
    except HTTPError as e:
        return {
            "success": False,
            "error": f"HTTP {e.code}: {e.reason}",
            "status": e.code
        }
    except URLError as e:
        return {
            "success": False,
            "error": f"Network error: {e.reason}",
            "status": None
        }
    except json.JSONDecodeError as e:
        return {
            "success": False,
            "error": f"Invalid JSON: {e}",
            "status": None
        }

print("safe_get() defined. Test with safe_get('https://httpbin.org/get')")

# Exercise 3 Solution
print("\n--- Exercise 3 Solution ---")
def validate_user(data):
    """Validate user data structure."""
    errors = []
    
    # Check required fields exist
    required = {"id": int, "name": str, "email": str}
    
    for field, expected_type in required.items():
        if field not in data:
            errors.append(f"missing {field}")
        elif not isinstance(data[field], expected_type):
            actual = type(data[field]).__name__
            errors.append(f"{field} should be {expected_type.__name__}, got {actual}")
    
    # Check optional field type if present
    if "active" in data and not isinstance(data["active"], bool):
        errors.append("active should be bool")
    
    return (len(errors) == 0, errors)

# Test
test_users = [
    {"id": 1, "name": "Alice", "email": "a@b.com"},
    {"id": "1", "name": "Bob"},
    {"id": 2, "name": "Charlie", "email": "c@d.com", "active": True},
]
for user in test_users:
    valid, errs = validate_user(user)
    print(f"User: {user}")
    print(f"Valid: {valid}, Errors: {errs}")
    print()

# Exercise 4 Solution
print("--- Exercise 4 Solution ---")
def get_weather_summary(data):
    """Extract weather summary from nested data."""
    # Safely get nested values
    location = data.get("location", {})
    city = location.get("name", "Unknown")
    country = location.get("country", "Unknown")
    
    current = data.get("current", {})
    temp = current.get("temp_c", "Unknown")
    condition = current.get("condition", {})
    text = condition.get("text", "Unknown")
    
    forecast = data.get("forecast", {})
    days = forecast.get("days", [])
    tomorrow_high = days[0].get("max_temp", "Unknown") if days else "Unknown"
    
    return f"{city}, {country}: {temp}°C, {text}. Tomorrow's high: {tomorrow_high}°C"

# Test
weather_data = {
    "location": {"name": "London", "country": "UK"},
    "current": {"temp_c": 15, "condition": {"text": "Cloudy"}},
    "forecast": {"days": [{"date": "2025-01-01", "max_temp": 18}]}
}
print(get_weather_summary(weather_data))

# Test with missing data
partial_data = {"location": {"name": "Paris"}}
print(get_weather_summary(partial_data))

# Exercise 5 Solution
print("\n--- Exercise 5 Solution ---")
def fetch_all_pages(fetch_page_func):
    """Fetch all items from paginated API."""
    all_items = []
    page = 1
    max_pages = 100
    
    while page <= max_pages:
        result = fetch_page_func(page)
        items = result.get("items", [])
        all_items.extend(items)
        
        if not result.get("has_more", False):
            break
        
        page += 1
    
    return all_items

# Simulate paginated API
def mock_fetch_page(page):
    pages = {
        1: {"items": ["a", "b"], "has_more": True},
        2: {"items": ["c", "d"], "has_more": True},
        3: {"items": ["e"], "has_more": False},
    }
    return pages.get(page, {"items": [], "has_more": False})

all_items = fetch_all_pages(mock_fetch_page)
print(f"Fetched: {all_items}")

# Exercise 6 Solution
print("\n--- Exercise 6 Solution ---")
def check_rate_limit_status(headers_dict):
    """Check rate limit status from headers."""
    try:
        limit = int(headers_dict.get("X-RateLimit-Limit", 0))
        remaining = int(headers_dict.get("X-RateLimit-Remaining", 0))
        used = limit - remaining
        percentage = (used / limit * 100) if limit > 0 else 0
        
        return {
            "limit": limit,
            "remaining": remaining,
            "used": used,
            "percentage_used": round(percentage, 2),
            "should_slow_down": percentage > 80
        }
    except (ValueError, TypeError):
        return {
            "limit": 0,
            "remaining": 0,
            "used": 0,
            "percentage_used": 0.0,
            "should_slow_down": False
        }

# Test
headers = {"X-RateLimit-Limit": "100", "X-RateLimit-Remaining": "20"}
status = check_rate_limit_status(headers)
print(f"Headers: {headers}")
print(f"Status: {status}")

headers2 = {"X-RateLimit-Limit": "100", "X-RateLimit-Remaining": "95"}
status2 = check_rate_limit_status(headers2)
print(f"\nHeaders: {headers2}")
print(f"Status: {status2}")

# Bonus Solution
print("\n--- Bonus Solution ---")
def transform_api_response(raw_data):
    """Transform various API formats to standard format."""
    result = {}
    
    # Handle different name fields
    if "user_name" in raw_data:
        result["name"] = raw_data["user_name"]
    elif "name" in raw_data:
        result["name"] = raw_data["name"]
    else:
        result["name"] = "Unknown"
    
    # Handle different age fields
    if "user_age" in raw_data:
        result["age"] = raw_data["user_age"]
    elif "age" in raw_data:
        result["age"] = raw_data["age"]
    else:
        result["age"] = None
    
    # Handle different email fields
    if "user_email" in raw_data:
        result["email"] = raw_data["user_email"]
    elif "email" in raw_data:
        result["email"] = raw_data["email"]
    elif "contact" in raw_data and isinstance(raw_data["contact"], dict):
        result["email"] = raw_data["contact"].get("email", "Unknown")
    else:
        result["email"] = "Unknown"
    
    return result

# Test
formats = [
    {"user_name": "Alice", "user_age": 30, "user_email": "alice@test.com"},
    {"name": "Bob", "age": 25, "contact": {"email": "bob@test.com"}},
    {"name": "Charlie"},
]

for data in formats:
    print(f"Input: {data}")
    print(f"Output: {transform_api_response(data)}")
    print()

print("=" * 60)
print("All exercises complete! Great job!")
print("=" * 60)
