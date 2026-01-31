"""
HTTP Server - Exercises
=======================
Practice building HTTP servers with Python.

NOTE: These are code exercises - they don't actually start servers.
Run the solutions separately to test them!
"""

print("=" * 60)
print("HTTP SERVER - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: Basic Hello Server
# =============================================================================
print("\n--- Exercise 1: Basic Hello Server ---\n")
"""
Create a basic HTTP server handler that:
- Responds to GET requests with "Hello, World!"
- Sets the correct content type
- Returns HTTP 200 status

Write the complete handler class and server setup code.
"""

# Your code here:


# =============================================================================
# EXERCISE 2: JSON API Server
# =============================================================================
print("\n--- Exercise 2: JSON API Server ---\n")
"""
Create an HTTP server that serves JSON data:

Endpoints:
- GET /api/time - Returns current server time
- GET /api/random - Returns a random number
- GET /api/info - Returns server info (Python version, platform)

All endpoints should return JSON with proper Content-Type.
"""

# Your code here:


# =============================================================================
# EXERCISE 3: Calculator API
# =============================================================================
print("\n--- Exercise 3: Calculator API ---\n")
"""
Create a calculator API that uses query parameters:

Endpoint: GET /calc
Parameters: a (number), b (number), op (operation)
Operations: add, subtract, multiply, divide

Example: /calc?a=5&b=3&op=add → {"result": 8}

Handle errors:
- Missing parameters → 400 Bad Request
- Invalid operation → 400 Bad Request
- Division by zero → 400 Bad Request
"""

# Your code here:


# =============================================================================
# EXERCISE 4: Static File Server with Restrictions
# =============================================================================
print("\n--- Exercise 4: Static File Server ---\n")
"""
Create a handler that serves files from a 'public' directory
with security restrictions:

Requirements:
- Only serve files from the 'public' folder
- Block attempts to access files outside (paths with '..')
- Return 403 for forbidden access attempts
- Return 404 if file doesn't exist
- Set correct Content-Type based on file extension
- Only allow .html, .css, .js, .png, .jpg files
"""

# Your code here:


# =============================================================================
# EXERCISE 5: Router Class
# =============================================================================
print("\n--- Exercise 5: Router Class ---\n")
"""
Create a Router class that makes URL routing cleaner:

class Router:
    def add_route(self, path, handler_func)
    def handle(self, request_handler)

Usage:
    router = Router()
    router.add_route('/', home_page)
    router.add_route('/about', about_page)
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            router.handle(self)

The router should:
- Match exact paths
- Call the handler function with the request handler
- Return 404 if no route matches
"""

# Your code here:


# =============================================================================
# EXERCISE 6: Request Logger Middleware
# =============================================================================
print("\n--- Exercise 6: Request Logger ---\n")
"""
Create a logging mixin that tracks all requests:

Requirements:
- Log timestamp, client IP, method, path, status code
- Save logs to a file (server.log)
- Include response time (how long the request took)

Format: [TIMESTAMP] IP METHOD PATH STATUS TIMEms

Example: [2026-01-30 12:30:45] 127.0.0.1 GET / 200 15ms
"""

# Your code here:


# =============================================================================
# SOLUTIONS
# =============================================================================
print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# -------------------------------------------------------------------------
# Solution 1
# -------------------------------------------------------------------------
print("\n--- Solution 1: Basic Hello Server ---\n")

from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, World!')
    
    def log_message(self, format, *args):
        pass  # Suppress logs for cleaner output

print("""
# To run this server:
if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), HelloHandler)
    print('Server at http://localhost:8000')
    server.serve_forever()
""")

# -------------------------------------------------------------------------
# Solution 2
# -------------------------------------------------------------------------
print("\n--- Solution 2: JSON API Server ---\n")

import json
import random
import sys
import platform
from datetime import datetime

class JSONAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/time':
            response = {
                'time': datetime.now().isoformat(),
                'timezone': str(datetime.now().astimezone().tzinfo)
            }
            self.send_json(response)
        
        elif self.path == '/api/random':
            response = {
                'number': random.randint(1, 100),
                'float': round(random.random(), 4)
            }
            self.send_json(response)
        
        elif self.path == '/api/info':
            response = {
                'python_version': sys.version,
                'platform': platform.platform(),
                'processor': platform.processor()
            }
            self.send_json(response)
        
        else:
            self.send_response(404)
            self.send_json({'error': 'Endpoint not found'})
    
    def send_json(self, data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode())
    
    def log_message(self, format, *args):
        pass

print("JSON API Handler created with endpoints:")
print("  /api/time   → Current server time")
print("  /api/random → Random numbers")
print("  /api/info   → Server information")

# -------------------------------------------------------------------------
# Solution 3
# -------------------------------------------------------------------------
print("\n--- Solution 3: Calculator API ---\n")

from urllib.parse import urlparse, parse_qs

class CalculatorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        
        if parsed.path != '/calc':
            self.send_error(404)
            return
        
        params = parse_qs(parsed.query)
        
        # Get parameters
        try:
            a = float(params.get('a', [''])[0])
            b = float(params.get('b', [''])[0])
        except (ValueError, IndexError):
            self.send_error_json(400, 'Missing or invalid parameters: a, b')
            return
        
        op = params.get('op', [''])[0]
        
        # Calculate
        operations = {
            'add': lambda x, y: x + y,
            'subtract': lambda x, y: x - y,
            'multiply': lambda x, y: x * y,
            'divide': lambda x, y: x / y if y != 0 else None
        }
        
        if op not in operations:
            self.send_error_json(400, f'Invalid operation: {op}')
            return
        
        result = operations[op](a, b)
        
        if result is None:
            self.send_error_json(400, 'Division by zero')
            return
        
        self.send_json({'a': a, 'b': b, 'op': op, 'result': result})
    
    def send_json(self, data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def send_error_json(self, code, message):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'error': message}).encode())
    
    def log_message(self, format, *args):
        pass

print("Calculator API Handler created")
print("  Example: /calc?a=10&b=5&op=add → {'result': 15.0}")

# -------------------------------------------------------------------------
# Solution 4
# -------------------------------------------------------------------------
print("\n--- Solution 4: Static File Server ---\n")

import os

class StaticFileHandler(BaseHTTPRequestHandler):
    ALLOWED_EXTENSIONS = {'.html', '.css', '.js', '.png', '.jpg', '.jpeg'}
    PUBLIC_DIR = 'public'
    
    def do_GET(self):
        # Security: normalize path
        filepath = os.path.normpath(self.path.lstrip('/'))
        
        # Security: prevent directory traversal
        if '..' in filepath or filepath.startswith('.'):
            self.send_error(403, 'Access denied')
            return
        
        # Security: check file extension
        ext = os.path.splitext(filepath)[1].lower()
        if ext not in self.ALLOWED_EXTENSIONS:
            self.send_error(403, 'File type not allowed')
            return
        
        # Full path
        full_path = os.path.join(self.PUBLIC_DIR, filepath)
        
        # Check if file exists
        if not os.path.exists(full_path) or not os.path.isfile(full_path):
            self.send_error(404, 'File not found')
            return
        
        # Determine content type
        content_types = {
            '.html': 'text/html',
            '.css': 'text/css',
            '.js': 'application/javascript',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg'
        }
        content_type = content_types.get(ext, 'application/octet-stream')
        
        # Serve file
        try:
            with open(full_path, 'rb') as f:
                content = f.read()
            
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        except IOError:
            self.send_error(500, 'Server error')
    
    def log_message(self, format, *args):
        pass

print("StaticFileHandler created with security restrictions")
print("  - Only serves from 'public' directory")
print("  - Blocks directory traversal attempts")
print("  - Only allows specific file extensions")

# -------------------------------------------------------------------------
# Solution 5
# -------------------------------------------------------------------------
print("\n--- Solution 5: Router Class ---\n")

class Router:
    """Simple URL router for HTTP handlers."""
    
    def __init__(self):
        self.routes = {}
    
    def add_route(self, path, handler_func):
        """Add a route handler."""
        self.routes[path] = handler_func
    
    def handle(self, request_handler):
        """Handle a request using registered routes."""
        path = request_handler.path
        
        if path in self.routes:
            self.routes[path](request_handler)
        else:
            request_handler.send_response(404)
            request_handler.send_header('Content-type', 'text/html')
            request_handler.end_headers()
            request_handler.wfile.write(b'<h1>404 Not Found</h1>')

# Example usage
def home_page(handler):
    handler.send_response(200)
    handler.send_header('Content-type', 'text/html')
    handler.end_headers()
    handler.wfile.write(b'<h1>Home</h1>')

def about_page(handler):
    handler.send_response(200)
    handler.send_header('Content-type', 'text/html')
    handler.end_headers()
    handler.wfile.write(b'<h1>About</h1>')

router = Router()
router.add_route('/', home_page)
router.add_route('/about', about_page)

class RoutedHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        router.handle(self)
    
    def log_message(self, format, *args):
        pass

print("Router class created")
print("  router.add_route(path, handler)")
print("  router.handle(request_handler)")

# -------------------------------------------------------------------------
# Solution 6
# -------------------------------------------------------------------------
print("\n--- Solution 6: Request Logger ---\n")

import time

class LoggingMixin:
    """Mixin that adds request logging."""
    
    log_file = 'server.log'
    
    def log_request(self, code='-', size='-'):
        """Log request with timing."""
        if hasattr(self, '_start_time'):
            duration = int((time.time() - self._start_time) * 1000)
        else:
            duration = 0
        
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        client = self.client_address[0]
        method = self.command
        path = self.path
        status = code
        
        log_line = f"[{timestamp}] {client} {method} {path} {status} {duration}ms\n"
        
        # Print to console
        print(log_line.strip())
        
        # Write to file
        with open(self.log_file, 'a') as f:
            f.write(log_line)
    
    def do_GET(self):
        self._start_time = time.time()
        super().do_GET()
        self.log_request(200)

class LoggedHandler(LoggingMixin, BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Logged Request</h1>')
        # log_request called by mixin after
    
    def log_message(self, format, *args):
        pass  # Suppress default

print("LoggingMixin created")
print("  Logs: [timestamp] IP METHOD PATH STATUS TIMEms")
print("  Writes to server.log file")

# Cleanup
import os
try:
    if os.path.exists('server.log'):
        os.remove('server.log')
        print("\n(Cleaned up server.log)")
except:
    pass

print("\n" + "=" * 60)
print("All solutions complete!")
print("\nTo test a solution, create a new file and run the server:")
print("  python your_server.py")
print("Then visit http://localhost:8000 in your browser")
print("=" * 60)
