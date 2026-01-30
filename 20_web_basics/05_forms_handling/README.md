# 📝 Forms Handling

> Processing user input from HTML forms with Python

---

## What are HTML Forms?

**HTML Forms** allow users to submit data to a web server. They're essential for:
- User registration and login
- Search functionality
- Data entry and editing
- File uploads
- Feedback and contact

Think of forms like **paper forms** at a doctor's office:
- Fields to fill out (name, age, symptoms)
- A submit button to hand it in
- The staff processes the information

---

## HTML Form Basics

```html
<form action="/submit" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    
    <button type="submit">Submit</button>
</form>
```

**Key Attributes:**

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `action` | URL where form data is sent | `/submit`, `/register` |
| `method` | HTTP method (GET or POST) | `GET`, `POST` |
| `name` | Field identifier (sent to server) | `name="username"` |
| `required` | Makes field mandatory | `required` |

---

## GET vs POST

### GET Method
- Data sent in URL (query parameters)
- Visible in browser address bar
- Limited amount of data (~2048 chars)
- Good for: Search, filters, bookmarkable pages
- Not for: Passwords, sensitive data

```
GET /search?q=python&category=tutorial HTTP/1.1
```

### POST Method
- Data sent in request body
- Not visible in URL
- Can send large amounts of data
- Good for: Login forms, data creation, file uploads
- Required for: Passwords, sensitive information

```
POST /login HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 35

username=alice&password=secret123
```

---

## Form Data Encoding

### application/x-www-form-urlencoded

Default encoding. Key-value pairs joined with `&`:

```
name=John+Doe&email=john%40example.com&message=Hello+World
```

Special characters are URL-encoded:
- Space → `+` or `%20`
- `@` → `%40`
- `&` → `%26`
- `=` → `%3D`

### multipart/form-data

Used for file uploads. More complex format with boundaries.

---

## Parsing Form Data in Python

### From GET Requests (Query String)

```python
from urllib.parse import urlparse, parse_qs

class FormHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse URL
        parsed = urlparse(self.path)
        path = parsed.path
        query_string = parsed.query
        
        # Parse query parameters
        params = parse_qs(query_string)
        
        # Convert single-item lists to values
        data = {k: v[0] if len(v) == 1 else v for k, v in params.items()}
        
        # data = {'search': 'python', 'page': '1'}
```

### From POST Requests (Request Body)

```python
from urllib.parse import parse_qs

class FormHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Get content length from headers
        content_length = int(self.headers.get('Content-Length', 0))
        
        # Read the request body
        post_data = self.rfile.read(content_length)
        
        # Parse form data
        params = parse_qs(post_data.decode('utf-8'))
        
        # Convert to simple dict
        data = {k: v[0] if len(v) == 1 else v for k, v in params.items()}
        
        # Process the data
        self.process_form(data)
```

---

## Complete Form Handling Example

```python
"""
forms_server.py - Complete form handling example
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from html import escape

class FormHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Serve the form page."""
        if self.path == '/':
            self.serve_form()
        elif self.path.startswith('/result'):
            self.serve_result_get()
        else:
            self.send_error(404)
    
    def do_POST(self):
        """Process form submission."""
        if self.path == '/submit':
            self.process_form_post()
        else:
            self.send_error(404)
    
    def serve_form(self):
        """Display the contact form."""
        html = """<!DOCTYPE html>
<html>
<head>
    <title>Contact Form</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 500px; margin: 50px auto; }
        .field { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, textarea { width: 100%; padding: 8px; border: 1px solid #ddd; }
        button { background: #007bff; color: white; padding: 10px 20px; 
                 border: none; cursor: pointer; }
        button:hover { background: #0056b3; }
    </style>
</head>
<body>
    <h1>Contact Us</h1>
    <form action="/submit" method="POST">
        <div class="field">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
        </div>
        <div class="field">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div class="field">
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" required></textarea>
        </div>
        <button type="submit">Send Message</button>
    </form>
</body>
</html>"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
    
    def process_form_post(self):
        """Process POST form submission."""
        # Read form data
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        # Parse form data
        params = parse_qs(post_data.decode('utf-8'))
        data = {k: v[0] for k, v in params.items()}
        
        # Extract fields
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')
        
        # Validate
        errors = []
        if not name:
            errors.append("Name is required")
        if not email or '@' not in email:
            errors.append("Valid email is required")
        if not message:
            errors.append("Message is required")
        
        if errors:
            self.serve_error(errors)
        else:
            # Success - show confirmation
            self.serve_success(name, email, message)
    
    def serve_success(self, name, email, message):
        """Show success page."""
        html = f"""<!DOCTYPE html>
<html>
<head><title>Success</title></head>
<body style="font-family: Arial; max-width: 500px; margin: 50px auto;">
    <h1>✅ Message Sent!</h1>
    <p>Thank you, <strong>{escape(name)}</strong>!</p>
    <p>We've received your message and will reply to {escape(email)}.</p>
    <h3>Your Message:</h3>
    <blockquote style="background: #f5f5f5; padding: 15px; border-left: 4px solid #007bff;">
        {escape(message)}
    </blockquote>
    <a href="/">← Back to Form</a>
</body>
</html>"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
    
    def serve_error(self, errors):
        """Show error page."""
        errors_html = ''.join(f'<li>{escape(e)}</li>' for e in errors)
        html = f"""<!DOCTYPE html>
<html>
<head><title>Error</title></head>
<body style="font-family: Arial; max-width: 500px; margin: 50px auto;">
    <h1>❌ Error</h1>
    <p>Please fix the following issues:</p>
    <ul style="color: #dc3545;">{errors_html}</ul>
    <a href="/">← Back to Form</a>
</body>
</html>"""
        self.send_response(400)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
    
    def log_message(self, format, *args):
        print(f"[{self.date_time_string()}] {args[0]}")


if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), FormHandler)
    print('Form server running at http://localhost:8000')
    server.serve_forever()
```

---

## Form Validation

Always validate form data on the server:

```python
def validate_form(data):
    """Validate form data and return errors list."""
    errors = []
    
    # Required fields
    required = ['name', 'email', 'message']
    for field in required:
        if not data.get(field, '').strip():
            errors.append(f"{field.title()} is required")
    
    # Email format
    email = data.get('email', '')
    if email and '@' not in email:
        errors.append("Invalid email format")
    
    # Length limits
    name = data.get('name', '')
    if len(name) > 100:
        errors.append("Name is too long (max 100 characters)")
    
    # Type checking
    age = data.get('age', '')
    if age:
        try:
            age = int(age)
            if age < 0 or age > 150:
                errors.append("Age must be between 0 and 150")
        except ValueError:
            errors.append("Age must be a number")
    
    return errors
```

---

## Handling Different Input Types

```python
def parse_input(value, input_type):
    """Parse form value based on input type."""
    if input_type == 'checkbox':
        # Checkbox: present = True, absent = False
        return value == 'on'
    
    elif input_type == 'number':
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return None
    
    elif input_type == 'date':
        from datetime import datetime
        try:
            return datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            return None
    
    elif input_type == 'select-multiple':
        # Multiple select returns list
        return value if isinstance(value, list) else [value]
    
    else:
        # text, email, password, etc.
        return value.strip()
```

---

## Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|---------|---------------|------------------|
| Trusting client-side validation | Can be bypassed | Always validate on server |
| Not escaping output | XSS vulnerability | Use `html.escape()` |
| Using GET for sensitive data | Visible in URL/history | Use POST for passwords |
| Not checking Content-Length | Could read forever | Limit and validate size |
| Storing passwords in plain text | Security risk | Hash with bcrypt/argon2 |
| Not handling encoding | Unicode errors | Always specify UTF-8 |

---

## Quick Reference

```python
from urllib.parse import parse_qs
from html import escape

# Parse POST form data
content_length = int(self.headers.get('Content-Length', 0))
post_data = self.rfile.read(content_length)
data = parse_qs(post_data.decode('utf-8'))

# Convert to simple dict
form = {k: v[0] if len(v) == 1 else v for k, v in data.items()}

# Access fields
name = form.get('name', '')
email = form.get('email', '')

# Validate
if not name:
    errors.append("Name required")

# Escape for display
safe_name = escape(name)
```

---

## Next Steps

Congratulations! You've completed Module 20: Web Basics. You now know how to:

- Write HTML and CSS
- Build HTTP servers with Python
- Route URLs to handlers
- Generate dynamic templates
- Handle form submissions

**Where to go next:**
- Practice by building a complete web application
- Learn about cookies and sessions
- Explore Flask or Django for production applications
- Study web security in depth
