"""
HTTP Server - Examples
======================
Demonstrates building web servers with http.server.
"""

print("=" * 60)
print("HTTP SERVER - Examples")
print("=" * 60)

# =============================================================================
# SECTION 1: Basic Handler Structure
# =============================================================================
print("\n--- 1: Basic Handler Structure ---\n")

from http.server import BaseHTTPRequestHandler

class DemoHandler(BaseHTTPRequestHandler):
    """Demonstrates the basic structure of a request handler."""
    
    def do_GET(self):
        """Handle GET requests."""
        # Send HTTP 200 OK response
        self.send_response(200)
        
        # Set content type header
        self.send_header('Content-type', 'text/html; charset=utf-8')
        
        # End headers section
        self.end_headers()
        
        # Write response body (must be bytes!)
        response = b"<h1>Hello from Python!</h1>"
        self.wfile.write(response)
    
    def log_message(self, format, *args):
        """Override to suppress default logging during demo."""
        pass

print("DemoHandler class defined.")
print("Key methods:")
print("  - do_GET(): Handles GET requests")
print("  - send_response(code): Sets HTTP status code")
print("  - send_header(name, value): Adds response headers")
print("  - end_headers(): Marks end of headers")
print("  - wfile.write(data): Sends response body (bytes!)")

# =============================================================================
# SECTION 2: Inspecting Request Information
# =============================================================================
print("\n--- 2: Request Information Available ---\n")

class InfoHandler(BaseHTTPRequestHandler):
    """Shows all the information available about a request."""
    
    def do_GET(self):
        # Build info page showing request details
        info = f"""<!DOCTYPE html>
<html>
<head><title>Request Info</title></head>
<body>
    <h1>Request Information</h1>
    <table border="1" cellpadding="10">
        <tr><td><b>Path</b></td><td>{self.path}</td></tr>
        <tr><td><b>HTTP Method</b></td><td>{self.command}</td></tr>
        <tr><td><b>HTTP Version</b></td><td>{self.request_version}</td></tr>
        <tr><td><b>Client Address</b></td><td>{self.client_address}</td></tr>
        <tr><td><b>Server</b></td><td>{self.server.server_address}</td></tr>
    </table>
    
    <h2>Headers</h2>
    <pre>{self.headers}</pre>
</body>
</html>"""
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(info.encode())
    
    def log_message(self, format, *args):
        pass

print("InfoHandler shows all request information:")
print("  - self.path: The URL path requested")
print("  - self.command: HTTP method (GET, POST, etc.)")
print("  - self.request_version: HTTP version")
print("  - self.client_address: (IP, port) tuple")
print("  - self.headers: All HTTP headers")

# =============================================================================
# SECTION 3: Different Status Codes
# =============================================================================
print("\n--- 3: HTTP Status Codes ---\n")

def demonstrate_status_codes():
    """Show examples of different HTTP status codes."""
    
    status_codes = {
        200: "OK - Request succeeded",
        301: "Moved Permanently - Resource moved to new URL",
        302: "Found - Temporary redirect",
        400: "Bad Request - Malformed request",
        401: "Unauthorized - Authentication required",
        403: "Forbidden - Access denied",
        404: "Not Found - Resource doesn't exist",
        500: "Internal Server Error - Server problem",
        503: "Service Unavailable - Server overloaded"
    }
    
    print("Common HTTP Status Codes:")
    for code, description in status_codes.items():
        category = (code // 100)
        emoji = {2: "✅", 3: "🔄", 4: "❌", 5: "🔥"}.get(category, "❓")
        print(f"  {emoji} {code}: {description}")

demonstrate_status_codes()

# =============================================================================
# SECTION 4: Content Type Headers
# =============================================================================
print("\n--- 4: Content Types (MIME Types) ---\n")

content_types = {
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'application/javascript',
    '.json': 'application/json',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.gif': 'image/gif',
    '.svg': 'image/svg+xml',
    '.txt': 'text/plain',
    '.pdf': 'application/pdf',
    '.zip': 'application/zip'
}

print("Common Content-Type headers:")
for ext, mime in content_types.items():
    print(f"  {ext:6} → {mime}")

# Function to guess content type from filename
def guess_content_type(filename):
    """Guess MIME type from file extension."""
    ext = filename.lower().split('.')[-1] if '.' in filename else ''
    return content_types.get('.' + ext, 'application/octet-stream')

print("\nExamples:")
print(f"  index.html  → {guess_content_type('index.html')}")
print(f"  style.css   → {guess_content_type('style.css')}")
print(f"  data.json   → {guess_content_type('data.json')}")

# =============================================================================
# SECTION 5: URL Routing Pattern
# =============================================================================
print("\n--- 5: Simple URL Routing ---\n")

class RoutingHandler(BaseHTTPRequestHandler):
    """Demonstrates simple URL routing."""
    
    def do_GET(self):
        # Route based on path
        routes = {
            '/': self.serve_home,
            '/about': self.serve_about,
            '/contact': self.serve_contact,
        }
        
        # Get handler for path or serve 404
        handler = routes.get(self.path, self.serve_404)
        handler()
    
    def serve_home(self):
        self.send_html("<h1>Home</h1><p>Welcome to the homepage!</p>")
    
    def serve_about(self):
        self.send_html("<h1>About</h1><p>This is the about page.</p>")
    
    def serve_contact(self):
        self.send_html("<h1>Contact</h1><p>Email us at contact@example.com</p>")
    
    def serve_404(self):
        self.send_response(404)
        self.send_html("<h1>404</h1><p>Page not found!</p>")
    
    def send_html(self, html):
        """Helper to send HTML response."""
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
    
    def log_message(self, format, *args):
        pass

print("Routing pattern implemented:")
print("  /        → serve_home()")
print("  /about   → serve_about()")
print("  /contact → serve_contact()")
print("  *        → serve_404()")

# =============================================================================
# SECTION 6: Serving JSON API
# =============================================================================
print("\n--- 6: JSON API Response ---\n")

import json

class APIHandler(BaseHTTPRequestHandler):
    """Serves JSON API responses."""
    
    def do_GET(self):
        if self.path == '/api/users':
            users = [
                {'id': 1, 'name': 'Alice', 'role': 'admin'},
                {'id': 2, 'name': 'Bob', 'role': 'user'},
                {'id': 3, 'name': 'Carol', 'role': 'user'}
            ]
            self.send_json({'users': users, 'count': len(users)})
        
        elif self.path == '/api/status':
            self.send_json({
                'status': 'online',
                'version': '1.0.0',
                'timestamp': '2026-01-30T12:00:00'
            })
        
        else:
            self.send_response(404)
            self.send_json({'error': 'Not found'})
    
    def send_json(self, data):
        """Send JSON response with proper headers."""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode())
    
    def log_message(self, format, *args):
        pass

print("API endpoints demonstrated:")
print("  GET /api/users  → Returns list of users")
print("  GET /api/status → Returns server status")

# =============================================================================
# SECTION 7: Handling Query Parameters
# =============================================================================
print("\n--- 7: Query Parameters ---\n")

from urllib.parse import urlparse, parse_qs

class QueryHandler(BaseHTTPRequestHandler):
    """Demonstrates parsing query parameters."""
    
    def do_GET(self):
        # Parse URL
        parsed = urlparse(self.path)
        path = parsed.path
        query_string = parsed.query
        
        # Parse query parameters into dictionary
        params = parse_qs(query_string)
        
        # Convert lists to single values (for single values)
        params = {k: v[0] if len(v) == 1 else v for k, v in params.items()}
        
        if path == '/search':
            query = params.get('q', '')
            category = params.get('category', 'all')
            html = f"""<h1>Search Results</h1>
            <p>Query: {query}</p>
            <p>Category: {category}</p>"""
            self.send_html(html)
    
    def send_html(self, html):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
    
    def log_message(self, format, *args):
        pass

print("Query parameter parsing:")
print("  URL: /search?q=python&category=books")
print("  Result: {'q': 'python', 'category': 'books'}")

# Example parsing
from urllib.parse import urlparse, parse_qs
example_url = "/search?q=python&category=books&sort=date"
parsed = urlparse(example_url)
params = parse_qs(parsed.query)
params = {k: v[0] if len(v) == 1 else v for k, v in params.items()}
print(f"\nParsed '{example_url}':")
for key, value in params.items():
    print(f"  {key} = {value!r}")

# =============================================================================
# SECTION 8: Custom Logging
# =============================================================================
print("\n--- 8: Custom Logging ---\n")

class LoggingHandler(BaseHTTPRequestHandler):
    """Demonstrates custom request logging."""
    
    def log_message(self, format, *args):
        """Override to customize how requests are logged."""
        timestamp = self.date_time_string()
        client = self.client_address[0]
        method = self.command
        path = self.path
        
        log_line = f"[{timestamp}] {client} - {method} {path}"
        print(log_line)
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'OK')

print("Custom logging format:")
print("  [timestamp] client_ip - METHOD path")
print("\nExample:")
print("  [30/Jan/2026 12:30:45] 127.0.0.1 - GET /about")

# =============================================================================
# SECTION 9: Error Handling
# =============================================================================
print("\n--- 9: Error Handling ---\n")

class ErrorHandlingHandler(BaseHTTPRequestHandler):
    """Demonstrates proper error handling."""
    
    def do_GET(self):
        try:
            if self.path == '/error':
                # Simulate an error
                raise ValueError("Something went wrong!")
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Success!</h1>')
            
        except Exception as e:
            # Handle errors gracefully
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            error_html = f"""<h1>500 - Server Error</h1>
            <p>An error occurred: {str(e)}</p>
            <a href="/">Go Home</a>"""
            self.wfile.write(error_html.encode())
    
    def log_message(self, format, *args):
        pass

print("Error handling pattern:")
print("  1. Wrap request handling in try/except")
print("  2. Return appropriate status code (500)")
print("  3. Show user-friendly error message")
print("  4. Log error details for debugging")

# =============================================================================
# SECTION 10: Complete Server Example (Not Started)
# =============================================================================
print("\n--- 10: Complete Server Code ---\n")

complete_example = '''
"""
complete_server.py - Full-featured example server
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

class CompleteHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)
        
        if path == '/':
            self.serve_home()
        elif path == '/api/users':
            self.serve_users(params)
        elif path == '/api/user':
            self.serve_user(params)
        else:
            self.serve_404()
    
    def serve_home(self):
        html = """<!DOCTYPE html>
<html>
<head>
    <title>Complete Server</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; }
        code { background: #f4f4f4; padding: 2px 6px; border-radius: 4px; }
    </style>
</head>
<body>
    <h1>🐍 Python HTTP Server</h1>
    <h2>Available Endpoints:</h2>
    <ul>
        <li><code>GET /</code> - This page</li>
        <li><code>GET /api/users</code> - List all users</li>
        <li><code>GET /api/user?id=1</code> - Get specific user</li>
    </ul>
</body>
</html>"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
    
    def serve_users(self, params):
        users = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Carol"}
        ]
        self.send_json({"users": users})
    
    def serve_user(self, params):
        user_id = params.get('id', [''])[0]
        users = {"1": "Alice", "2": "Bob", "3": "Carol"}
        name = users.get(user_id)
        
        if name:
            self.send_json({"id": user_id, "name": name})
        else:
            self.send_response(404)
            self.send_json({"error": "User not found"})
    
    def serve_404(self):
        self.send_response(404)
        self.send_json({"error": "Not found"})
    
    def send_json(self, data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode())

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), CompleteHandler)
    print('Server running at http://localhost:8000')
    server.serve_forever()
'''

print(complete_example)

# =============================================================================
# FINAL NOTES
# =============================================================================
print("\n" + "=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("""
1. BaseHTTPRequestHandler is the foundation for custom handlers
2. Override do_GET(), do_POST(), etc. to handle different methods
3. Always send response code, headers, then body
4. Write bytes to wfile, not strings
5. Parse URLs with urllib.parse for query parameters
6. Set proper Content-Type headers for different responses
7. Implement error handling for robust servers
8. Override log_message() for custom logging

To run a real server:
  from http.server import HTTPServer
  server = HTTPServer(('localhost', 8000), MyHandler)
  server.serve_forever()
""")

print("=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
