"""
Building a Simple API - Exercises
==================================
Practice building REST APIs with http.server.
"""

print("=" * 60)
print("BUILDING A SIMPLE API - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: Basic Handler
# =============================================================================
print("\n--- Exercise 1: Basic Handler ---\n")
"""
Create a BasicHandler class that:
1. Responds to GET requests at / with "Hello from my API!"
2. Responds to GET requests at /time with the current time
3. Returns 404 for any other path

Hints:
- Import datetime for the time
- Use datetime.now().isoformat()
- Check self.path to route requests
"""

# Your code here (write in a separate file to test):

'''
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

class BasicHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Your implementation here
        pass

# Uncomment to run:
# server = HTTPServer(("localhost", 8000), BasicHandler)
# server.serve_forever()
'''

# =============================================================================
# EXERCISE 2: Calculator API
# =============================================================================
print("\n--- Exercise 2: Calculator API ---\n")
"""
Create a CalculatorAPI that handles GET requests like:
- /add/5/3      -> returns {"operation": "add", "result": 8}
- /subtract/10/4 -> returns {"operation": "subtract", "result": 6}
- /multiply/6/7  -> returns {"operation": "multiply", "result": 42}
- /divide/15/3   -> returns {"operation": "divide", "result": 5}

Handle division by zero with an appropriate error response.
"""

# Your code here:

'''
import json
from http.server import BaseHTTPRequestHandler

class CalculatorAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse path like /add/5/3
        # Your implementation here
        pass
'''

# =============================================================================
# EXERCISE 3: Book Store API
# =============================================================================
print("\n--- Exercise 3: Book Store API ---\n")
"""
Create a BookStoreAPI with an in-memory list of books.
Each book has: id, title, author, year

Implement these endpoints:
- GET /books           -> List all books
- GET /books/1         -> Get book with id 1
- POST /books          -> Add a new book (read from request body)
- DELETE /books/1      -> Delete book with id 1

Use this initial data:
books = [
    {"id": 1, "title": "Python Basics", "author": "Alice", "year": 2023},
    {"id": 2, "title": "Web Development", "author": "Bob", "year": 2024},
]
"""

# Your code here:

'''
import json
from http.server import BaseHTTPRequestHandler

class BookStoreAPI(BaseHTTPRequestHandler):
    books = [
        {"id": 1, "title": "Python Basics", "author": "Alice", "year": 2023},
        {"id": 2, "title": "Web Development", "author": "Bob", "year": 2024},
    ]
    
    # Implement _send_json helper, do_GET, do_POST, do_DELETE
'''

# =============================================================================
# EXERCISE 4: Request Logger
# =============================================================================
print("\n--- Exercise 4: Request Logger ---\n")
"""
Create a LoggingHandler that:
1. Logs every request to a file (requests.log)
2. Logs: timestamp, method, path, client IP
3. Still returns a normal response

Hint: Use self.headers.get('Host') and self.client_address
"""

# Your code here:

'''
from http.server import BaseHTTPRequestHandler
from datetime import datetime

class LoggingHandler(BaseHTTPRequestHandler):
    def log_request(self, method, path):
        # Your implementation here
        pass
    
    def do_GET(self):
        # Log and respond
        pass
'''

# =============================================================================
# EXERCISE 5: JSON Echo API
# =============================================================================
print("\n--- Exercise 5: JSON Echo API ---\n")
"""
Create an EchoAPI that:
1. Accepts any JSON POST to /echo
2. Returns the same JSON back with additional fields:
   - "echo": true
   - "received_at": timestamp
   - "path": the request path
   
Example:
POST {"message": "Hello"}
Response: {"message": "Hello", "echo": true, "received_at": "...", "path": "/echo"}
"""

# Your code here:

'''
import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler

class EchoAPI(BaseHTTPRequestHandler):
    def do_POST(self):
        # Your implementation here
        pass
'''

# =============================================================================
# BONUS EXERCISE: API Key Authentication
# =============================================================================
print("\n--- BONUS: API Key Authentication ---\n")
"""
Create a ProtectedAPI that:
1. Requires an API key for all endpoints except /public
2. Check for X-API-Key header
3. Return 401 if key is missing or invalid
4. Valid keys: "secret123", "demo456"

Endpoints:
- GET /public          -> No key needed
- GET /protected       -> Needs valid key
- GET /admin           -> Needs "secret123" specifically
"""

# Your code here:

'''
import json
from http.server import BaseHTTPRequestHandler

class ProtectedAPI(BaseHTTPRequestHandler):
    VALID_KEYS = {"secret123", "demo456"}
    ADMIN_KEY = "secret123"
    
    def check_auth(self):
        # Your implementation here
        pass
'''

# =============================================================================
# SOLUTIONS
# =============================================================================
print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# Exercise 1 Solution
print("\n--- Exercise 1 Solution ---")
solution1 = '''
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

class BasicHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello from my API!")
            
        elif self.path == "/time":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            current_time = datetime.now().isoformat()
            self.wfile.write(f"Current time: {current_time}".encode())
            
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 - Not Found")

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), BasicHandler)
    print("Server on http://localhost:8000")
    server.serve_forever()
'''
print(solution1)

# Exercise 2 Solution
print("\n--- Exercise 2 Solution ---")
solution2 = '''
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class CalculatorAPI(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def do_GET(self):
        # Parse path: /add/5/3
        parts = self.path.strip("/").split("/")
        
        if len(parts) != 3:
            self._send_json({"error": "Invalid format. Use: /operation/a/b"}, 400)
            return
        
        operation, a, b = parts
        
        try:
            a, b = float(a), float(b)
        except ValueError:
            self._send_json({"error": "Arguments must be numbers"}, 400)
            return
        
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            if b == 0:
                self._send_json({"error": "Division by zero"}, 400)
                return
            result = a / b
        else:
            self._send_json({"error": f"Unknown operation: {operation}"}, 400)
            return
        
        self._send_json({
            "operation": operation,
            "a": a,
            "b": b,
            "result": result
        })

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), CalculatorAPI)
    print("Calculator API on http://localhost:8000")
    print("Try: http://localhost:8000/add/5/3")
    server.serve_forever()
'''
print(solution2)

# Exercise 3 Solution
print("\n--- Exercise 3 Solution ---")
solution3 = '''
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class BookStoreAPI(BaseHTTPRequestHandler):
    books = [
        {"id": 1, "title": "Python Basics", "author": "Alice", "year": 2023},
        {"id": 2, "title": "Web Development", "author": "Bob", "year": 2024},
    ]
    next_id = 3
    
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def do_GET(self):
        if self.path == "/books":
            self._send_json(self.books)
            
        elif self.path.startswith("/books/"):
            try:
                book_id = int(self.path.split("/")[-1])
                book = next((b for b in self.books if b["id"] == book_id), None)
                if book:
                    self._send_json(book)
                else:
                    self._send_json({"error": "Book not found"}, 404)
            except ValueError:
                self._send_json({"error": "Invalid ID"}, 400)
        else:
            self._send_json({"error": "Not found"}, 404)
    
    def do_POST(self):
        if self.path == "/books":
            try:
                content_length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(content_length)
                data = json.loads(body.decode())
                
                new_book = {
                    "id": BookStoreAPI.next_id,
                    "title": data.get("title", ""),
                    "author": data.get("author", ""),
                    "year": data.get("year", 2024)
                }
                BookStoreAPI.books.append(new_book)
                BookStoreAPI.next_id += 1
                
                self._send_json(new_book, 201)
            except json.JSONDecodeError:
                self._send_json({"error": "Invalid JSON"}, 400)
        else:
            self._send_json({"error": "Not found"}, 404)
    
    def do_DELETE(self):
        if self.path.startswith("/books/"):
            try:
                book_id = int(self.path.split("/")[-1])
                original_len = len(BookStoreAPI.books)
                BookStoreAPI.books = [b for b in BookStoreAPI.books if b["id"] != book_id]
                
                if len(BookStoreAPI.books) < original_len:
                    self._send_json({"message": "Book deleted"})
                else:
                    self._send_json({"error": "Book not found"}, 404)
            except ValueError:
                self._send_json({"error": "Invalid ID"}, 400)
        else:
            self._send_json({"error": "Not found"}, 404)

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), BookStoreAPI)
    print("Book Store API on http://localhost:8000")
    server.serve_forever()
'''
print(solution3)

# Exercise 4 Solution
print("\n--- Exercise 4 Solution ---")
solution4 = '''
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

class LoggingHandler(BaseHTTPRequestHandler):
    def log_request_details(self):
        timestamp = datetime.now().isoformat()
        client_ip = self.client_address[0]
        method = self.command
        path = self.path
        
        log_line = f"[{timestamp}] {client_ip} - {method} {path}\\n"
        
        with open("requests.log", "a") as f:
            f.write(log_line)
        
        print(log_line.strip())
    
    def do_GET(self):
        self.log_request_details()
        
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Request logged!")
    
    def do_POST(self):
        self.log_request_details()
        
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"POST request logged!")

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), LoggingHandler)
    print("Logging server on http://localhost:8000")
    print("Requests are being saved to requests.log")
    server.serve_forever()
'''
print(solution4)

# Exercise 5 Solution
print("\n--- Exercise 5 Solution ---")
solution5 = '''
import json
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

class EchoAPI(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def do_POST(self):
        if self.path == "/echo":
            try:
                content_length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(content_length)
                data = json.loads(body.decode())
                
                # Add echo fields
                response = dict(data)
                response["echo"] = True
                response["received_at"] = datetime.now().isoformat()
                response["path"] = self.path
                
                self._send_json(response)
            except json.JSONDecodeError:
                self._send_json({"error": "Invalid JSON"}, 400)
        else:
            self._send_json({"error": "Use /echo endpoint"}, 404)

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), EchoAPI)
    print("Echo API on http://localhost:8000")
    server.serve_forever()
'''
print(solution5)

# Bonus Solution
print("\n--- Bonus Solution ---")
bonus_solution = '''
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class ProtectedAPI(BaseHTTPRequestHandler):
    VALID_KEYS = {"secret123", "demo456"}
    ADMIN_KEY = "secret123"
    
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def get_api_key(self):
        return self.headers.get("X-API-Key")
    
    def check_auth(self, require_admin=False):
        key = self.get_api_key()
        
        if not key:
            return False, "Missing API key"
        
        if require_admin:
            if key != self.ADMIN_KEY:
                return False, "Admin access required"
        else:
            if key not in self.VALID_KEYS:
                return False, "Invalid API key"
        
        return True, None
    
    def do_GET(self):
        if self.path == "/public":
            self._send_json({"message": "Public endpoint - no key needed"})
            
        elif self.path == "/protected":
            authorized, error = self.check_auth()
            if authorized:
                self._send_json({"message": "Protected data", "key": self.get_api_key()})
            else:
                self._send_json({"error": error}, 401)
                
        elif self.path == "/admin":
            authorized, error = self.check_auth(require_admin=True)
            if authorized:
                self._send_json({"message": "Admin data"})
            else:
                self._send_json({"error": error}, 401)
        else:
            self._send_json({"error": "Not found"}, 404)

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), ProtectedAPI)
    print("Protected API on http://localhost:8000")
    print("Valid keys: secret123 (admin), demo456")
    server.serve_forever()
'''
print(bonus_solution)

print("\n" + "=" * 60)
print("All exercises complete! Try building your own API!")
print("=" * 60)
