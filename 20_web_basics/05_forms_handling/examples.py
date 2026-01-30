"""
Forms Handling - Examples
=========================
Demonstrates processing HTML form data with Python.
"""

print("=" * 60)
print("FORMS HANDLING - Examples")
print("=" * 60)

# =============================================================================
# SECTION 1: URL Encoding/Decoding
# =============================================================================
print("\n--- 1: URL Encoding/Decoding ---\n")

from urllib.parse import quote, unquote, urlencode, parse_qs

# URL encoding
text = "Hello World! @#$%^&*()"
encoded = quote(text)
print(f"Original: {text}")
print(f"Encoded:  {encoded}")
print(f"Decoded:  {unquote(encoded)}")

# Form data encoding
form_data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'message': 'Hello there!'
}
encoded_form = urlencode(form_data)
print(f"\nForm data: {form_data}")
print(f"Encoded:   {encoded_form}")

# Parsing form data
query_string = "name=John+Doe&email=john%40example.com&tags=python&tags=web"
parsed = parse_qs(query_string)
print(f"\nQuery string: {query_string}")
print(f"Parsed:       {parsed}")

# Single value parsing
simple = {k: v[0] if len(v) == 1 else v for k, v in parsed.items()}
print(f"Simplified:   {simple}")

# =============================================================================
# SECTION 2: Parsing GET Parameters
# =============================================================================
print("\n--- 2: Parsing GET Parameters ---\n")

from urllib.parse import urlparse

def parse_get_params(url):
    """Extract and parse query parameters from URL."""
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    # Convert single-item lists to values
    return {k: v[0] if len(v) == 1 else v for k, v in params.items()}

# Test URLs
test_urls = [
    "http://example.com/search?q=python",
    "http://example.com/search?q=python&page=2&limit=10",
    "http://example.com/filter?category=books&category=tech&sort=price",
]

print("GET parameter parsing:")
for url in test_urls:
    params = parse_get_params(url)
    print(f"  URL: {url}")
    print(f"  Params: {params}")
    print()

# =============================================================================
# SECTION 3: Simulating POST Data Parsing
# =============================================================================
print("\n--- 3: POST Data Parsing ---\n")

def parse_post_data(body_bytes):
    """Simulate parsing POST form data from request body."""
    # In real server: body = self.rfile.read(content_length)
    body = body_bytes.decode('utf-8')
    params = parse_qs(body)
    return {k: v[0] if len(v) == 1 else v for k, v in params.items()}

# Simulate POST body
post_body = b"name=Alice&email=alice%40example.com&message=Hello+World"
data = parse_post_data(post_body)

print("POST data parsing:")
print(f"  Raw body: {post_body}")
print(f"  Parsed:   {data}")

# =============================================================================
# SECTION 4: Form Validation
# =============================================================================
print("\n--- 4: Form Validation ---\n")

def validate_contact_form(data):
    """Validate contact form data."""
    errors = []
    
    # Required fields
    required_fields = ['name', 'email', 'message']
    for field in required_fields:
        value = data.get(field, '').strip()
        if not value:
            errors.append(f"{field.title()} is required")
        elif len(value) > 1000:
            errors.append(f"{field.title()} is too long")
    
    # Email validation (basic)
    email = data.get('email', '').strip()
    if email:
        if '@' not in email or '.' not in email.split('@')[-1]:
            errors.append("Invalid email format")
        if len(email) > 254:
            errors.append("Email is too long")
    
    # Message length
    message = data.get('message', '').strip()
    if message and len(message) < 10:
        errors.append("Message must be at least 10 characters")
    
    return errors

# Test cases
test_cases = [
    {'name': 'Alice', 'email': 'alice@example.com', 'message': 'Hello there!'},
    {'name': '', 'email': 'invalid', 'message': 'Hi'},
    {'name': 'Bob' * 500, 'email': 'bob@example.com', 'message': 'Test message here'},
]

print("Form validation:")
for i, test in enumerate(test_cases, 1):
    errors = validate_contact_form(test)
    status = "✅ Valid" if not errors else f"❌ Errors: {errors}"
    print(f"  Test {i}: {status}")

# =============================================================================
# SECTION 5: Input Type Handling
# =============================================================================
print("\n--- 5: Input Type Handling ---\n")

def parse_typed_value(value, input_type):
    """Parse form value based on input type."""
    if value is None or value == '':
        return None
    
    if input_type == 'checkbox':
        return value.lower() in ('on', 'true', '1', 'yes')
    
    elif input_type == 'number':
        try:
            if '.' in str(value):
                return float(value)
            return int(value)
        except ValueError:
            return None
    
    elif input_type == 'date':
        from datetime import datetime
        try:
            return datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            return None
    
    elif input_type == 'boolean':
        return value.lower() in ('true', '1', 'yes', 'on')
    
    else:
        return value.strip()

# Test type parsing
print("Type parsing:")
type_tests = [
    ('on', 'checkbox'),
    ('42', 'number'),
    ('3.14', 'number'),
    ('2026-01-30', 'date'),
    ('true', 'boolean'),
    ('Hello', 'text'),
]

for value, type_ in type_tests:
    result = parse_typed_value(value, type_)
    print(f"  {value!r} ({type_}) → {result!r} ({type(result).__name__ if result else 'None'})")

# =============================================================================
# SECTION 6: Form Data Sanitization
# =============================================================================
print("\n--- 6: Form Data Sanitization ---\n")

from html import escape
import re

def sanitize_form_data(data):
    """Sanitize form data for safe display."""
    sanitized = {}
    
    for key, value in data.items():
        if isinstance(value, str):
            # Strip whitespace
            value = value.strip()
            
            # Escape HTML
            value = escape(value)
            
            # Normalize whitespace
            value = re.sub(r'\s+', ' ', value)
            
            sanitized[key] = value
        elif isinstance(value, list):
            sanitized[key] = [escape(str(v)).strip() for v in value]
        else:
            sanitized[key] = value
    
    return sanitized

# Test sanitization
dirty_data = {
    'name': '  <script>alert("xss")</script>  ',
    'message': 'Hello\n\n\nWorld  \t  !',
    'tags': ['<b>tag1</b>', '  tag2  ']
}

print("Sanitization:")
print(f"  Input:  {dirty_data}")
sanitized = sanitize_form_data(dirty_data)
print(f"  Output: {sanitized}")

# =============================================================================
# SECTION 7: Complete Form Handler Simulation
# =============================================================================
print("\n--- 7: Complete Form Handler Simulation ---\n")

class MockRequest:
    """Simulates an HTTP request for testing."""
    def __init__(self, method, path, body=None):
        self.method = method
        self.path = path
        self.body = body
        self.headers = {'Content-Length': len(body) if body else 0}
    
    def read_body(self):
        return self.body

class FormProcessor:
    """Process form submissions."""
    
    def __init__(self):
        self.submissions = []
    
    def handle_request(self, request):
        """Handle HTTP request."""
        if request.method == 'GET':
            return self.render_form()
        elif request.method == 'POST':
            return self.process_submission(request)
    
    def render_form(self):
        """Render the contact form."""
        return {
            'status': 200,
            'content_type': 'text/html',
            'body': '<form>...</form>'  # Simplified
        }
    
    def process_submission(self, request):
        """Process form submission."""
        # Parse form data
        body = request.read_body()
        data = parse_qs(body.decode('utf-8'))
        form = {k: v[0] if len(v) == 1 else v for k, v in data.items()}
        
        # Validate
        errors = self.validate(form)
        if errors:
            return {
                'status': 400,
                'body': {'errors': errors}
            }
        
        # Sanitize
        clean = sanitize_form_data(form)
        
        # Store
        self.submissions.append(clean)
        
        return {
            'status': 200,
            'body': {'message': 'Thank you!', 'data': clean}
        }
    
    def validate(self, data):
        """Validate form data."""
        errors = []
        if not data.get('name', '').strip():
            errors.append("Name is required")
        if not data.get('email', '').strip():
            errors.append("Email is required")
        return errors

# Test
processor = FormProcessor()

# Simulate GET request
get_request = MockRequest('GET', '/contact')
result = processor.handle_request(get_request)
print(f"GET /contact: {result['status']}")

# Simulate valid POST
post_body = b"name=Alice&email=alice@example.com&message=Hello"
post_request = MockRequest('POST', '/contact', post_body)
result = processor.handle_request(post_request)
print(f"POST /contact (valid): {result['status']} - {result['body']['message']}")

# Simulate invalid POST
invalid_body = b"name=&email=invalid"
invalid_request = MockRequest('POST', '/contact', invalid_body)
result = processor.handle_request(invalid_request)
print(f"POST /contact (invalid): {result['status']} - {result['body']['errors']}")

# =============================================================================
# SECTION 8: File Upload Handling (Theory)
# =============================================================================
print("\n--- 8: File Upload Handling (Conceptual) ---\n")

print("""
File uploads use multipart/form-data encoding:

1. HTML form must have:
   <form enctype="multipart/form-data" method="POST">
       <input type="file" name="document">
   </form>

2. The request body has a special format with boundaries:
   ------WebKitFormBoundary
   Content-Disposition: form-data; name="document"; filename="file.txt"
   Content-Type: text/plain
   
   [file contents here]
   ------WebKitFormBoundary--

3. Python's standard library doesn't include multipart parsing.
   You would need to:
   - Implement a parser manually (complex)
   - Use cgi.parse_multipart (deprecated but works)
   - For production, use a framework like Flask or Django

Example with cgi module:
   import cgi
   form = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
                           environ={'REQUEST_METHOD': 'POST'})
   file_item = form['document']
   if file_item.filename:
       with open('uploads/' + file_item.filename, 'wb') as f:
           f.write(file_item.file.read())
""")

# =============================================================================
# SECTION 9: CSRF Protection (Conceptual)
# =============================================================================
print("\n--- 9: CSRF Protection (Conceptual) ---\n")

print("""
CSRF (Cross-Site Request Forgery) Protection:

Problem: Malicious site can submit forms to your site using user's session

Solution: Include a unique token in forms that must be validated:

1. Generate token when showing form:
   token = generate_random_token()  # e.g., secrets.token_hex(16)
   store in session
   include in form: <input type="hidden" name="csrf_token" value="{token}">

2. Validate on submission:
   submitted_token = form.get('csrf_token')
   stored_token = session.get('csrf_token')
   if submitted_token != stored_token:
       reject request (403 Forbidden)

Example:
   class SecureFormHandler:
       def generate_csrf_token(self):
           import secrets
           return secrets.token_urlsafe(32)
       
       def validate_csrf(self, form_data):
           token = form_data.get('csrf_token')
           return token == self.session.get('csrf_token')
""")

# =============================================================================
# SECTION 10: Best Practices Summary
# =============================================================================
print("\n--- 10: Best Practices Summary ---\n")

print("""
Form Handling Best Practices:

1. VALIDATION
   - Always validate on server (never trust client)
   - Check required fields, formats, lengths
   - Return clear error messages

2. SANITIZATION
   - Escape HTML output to prevent XSS
   - Strip whitespace from inputs
   - Normalize data types

3. SECURITY
   - Use POST for sensitive data
   - Implement CSRF protection
   - Set Content-Length limits
   - Validate file uploads (type, size)

4. USER EXPERIENCE
   - Preserve form data on errors
   - Show inline validation when possible
   - Provide clear success/error messages
   - Redirect after POST (PRG pattern)

5. ENCODING
   - Always use UTF-8
   - Handle URL encoding properly
   - Be aware of multipart boundaries

6. ERROR HANDLING
   - Catch parsing errors gracefully
   - Log form errors for debugging
   - Don't expose sensitive info in errors
""")

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
