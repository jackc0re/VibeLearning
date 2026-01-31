# 🖥️ HTTP Server

> Building web servers with Python's built-in http.server module

---

## What is http.server?

The `http.server` module is Python's built-in library for creating HTTP servers. It provides:

- `HTTPServer` class - The server that listens for connections
- `BaseHTTPRequestHandler` class - Handles incoming HTTP requests
- Zero dependencies - Part of Python's standard library

Think of it like a small restaurant that:
- Opens its doors (binds to a port)
- Waits for customers (listens for requests)
- Takes orders (reads HTTP requests)
- Serves food (sends HTTP responses)

---

## Basic Server Structure

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Handle GET requests
        self.send_response(200)  # OK status
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, World!')

# Create and start server
server = HTTPServer(('localhost', 8000), MyHandler)
print('Server running on http://localhost:8000')
server.serve_forever()
```

**Key Components:**

| Component | Purpose |
|-----------|---------|
| `HTTPServer` | The actual server that listens for connections |
| `BaseHTTPRequestHandler` | Base class for handling requests |
| `do_GET()` | Method called for GET requests |
| `send_response(code)` | Sets HTTP status code |
| `send_header(name, value)` | Adds HTTP headers |
| `end_headers()` | Finishes header section |
| `wfile.write(data)` | Sends response body |

---

## Understanding Request Handlers

### The Handler Class

```python
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Called when browser requests a page
        pass
    
    def do_POST(self):
        # Called when form is submitted
        pass
    
    def log_message(self, format, *args):
        # Override to customize logging
        print(f"[{self.date_time_string()}] {args[0]}")
```

### Request Information Available

```python
def do_GET(self):
    # The requested path (e.g., "/about")
    path = self.path
    
    # HTTP method used (GET, POST, etc.)
    method = self.command
    
    # Request headers (dictionary-like)
    user_agent = self.headers.get('User-Agent')
    
    # Client address
    client_ip = self.client_address[0]
```

---

## HTTP Status Codes

Always send appropriate status codes:

| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Request succeeded |
| 301 | Moved Permanently | Resource moved to new URL |
| 302 | Found | Temporary redirect |
| 400 | Bad Request | Request was malformed |
| 404 | Not Found | Resource doesn't exist |
| 405 | Method Not Allowed | Wrong HTTP method |
| 500 | Internal Server Error | Server error occurred |

```python
def do_GET(self):
    if self.path == '/':
        self.send_response(200)
    elif self.path == '/old-page':
        self.send_response(301)
        self.send_header('Location', '/new-page')
    else:
        self.send_response(404)
```

---

## Serving Different Content Types

```python
def do_GET(self):
    self.send_response(200)
    
    # Set content type based on what's being served
    if self.path.endswith('.html'):
        self.send_header('Content-type', 'text/html')
    elif self.path.endswith('.css'):
        self.send_header('Content-type', 'text/css')
    elif self.path.endswith('.js'):
        self.send_header('Content-type', 'application/javascript')
    elif self.path.endswith('.json'):
        self.send_header('Content-type', 'application/json')
    elif self.path.endswith('.png'):
        self.send_header('Content-type', 'image/png')
    else:
        self.send_header('Content-type', 'text/plain')
    
    self.end_headers()
```

---

## Serving Static Files

```python
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class StaticFileHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Map URL path to file path
        if self.path == '/':
            filepath = 'index.html'
        else:
            # Remove leading slash
            filepath = self.path.lstrip('/')
        
        # Security: prevent directory traversal
        filepath = os.path.normpath(filepath)
        if filepath.startswith('..'):
            self.send_error(403, "Access denied")
            return
        
        # Check if file exists
        if not os.path.exists(filepath):
            self.send_error(404, "File not found")
            return
        
        # Read and serve file
        try:
            with open(filepath, 'rb') as f:
                content = f.read()
            
            self.send_response(200)
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
            
        except IOError:
            self.send_error(500, "Server error")
```

---

## Complete Example: Simple Web Server

```python
"""
simple_server.py - A basic HTTP server with multiple routes
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Route based on path
        if self.path == '/':
            self.serve_home()
        elif self.path == '/about':
            self.serve_about()
        elif self.path == '/api/data':
            self.serve_api_data()
        else:
            self.serve_404()
    
    def serve_home(self):
        html = """<!DOCTYPE html>
<html>
<head><title>Home</title></head>
<body>
    <h1>Welcome!</h1>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/api/data">API Data</a>
    </nav>
</body>
</html>"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
    
    def serve_about(self):
        html = """<!DOCTYPE html>
<html>
<head><title>About</title></head>
<body>
    <h1>About This Server</h1>
    <p>Built with Python's http.server module!</p>
    <a href="/">← Back Home</a>
</body>
</html>"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
    
    def serve_api_data(self):
        data = {'message': 'Hello from API', 'status': 'ok'}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def serve_404(self):
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>404 - Page Not Found</h1>')
    
    def log_message(self, format, *args):
        # Custom logging
        print(f"[{self.date_time_string()}] {self.client_address[0]} - {args[0]}")

# Start server
if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), SimpleHandler)
    print('Server running at http://localhost:8000')
    print('Press Ctrl+C to stop')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down...')
        server.shutdown()
```

---

## Handling POST Requests

```python
def do_POST(self):
    # Get content length from headers
    content_length = int(self.headers.get('Content-Length', 0))
    
    # Read the request body
    post_data = self.rfile.read(content_length)
    
    # Parse form data (application/x-www-form-urlencoded)
    from urllib.parse import parse_qs
    form_data = parse_qs(post_data.decode())
    
    # Handle the data
    username = form_data.get('username', [''])[0]
    
    # Send response
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(f'Hello, {username}!'.encode())
```

---

## Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|---------|---------------|------------------|
| Not calling `end_headers()` | Browser won't receive response | Always call after sending headers |
| Writing strings to `wfile` | `wfile` expects bytes | Use `.encode()` or `b'...'` |
| Not checking file paths | Security vulnerability | Use `os.path.normpath()` and validation |
| Blocking `serve_forever()` | Can't stop server cleanly | Use threads or signal handlers |
| Forgetting content length | May cause connection issues | Set `Content-Length` header |

---

## Quick Reference

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class QuickHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello!</h1>')
    
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length)
        # Process data...
        self.send_response(200)
        self.end_headers()

# Run server
server = HTTPServer(('localhost', 8000), QuickHandler)
server.serve_forever()
```

**Start server in one line (for development only):**
```bash
python -m http.server 8000
```

---

## Next Steps

Now that you can build a basic server, let's learn how to route different URLs!

→ Continue to [03: Simple Routing](../03_simple_routing/)
