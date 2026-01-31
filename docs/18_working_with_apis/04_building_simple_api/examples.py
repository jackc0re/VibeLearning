"""
Building a Simple API - Examples
================================
Creating REST APIs with http.server.
"""

print("=" * 60)
print("BUILDING A SIMPLE API - Examples")
print("=" * 60)

# =============================================================================
# BASIC HTTP SERVER (Not runnable as-is, shown for learning)
# =============================================================================
print("\n--- Basic HTTP Server Structure ---\n")

basic_server_code = '''
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send status code
        self.send_response(200)
        # Send headers
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        # Send body
        self.wfile.write(b"Hello, World!")

# Start server
server = HTTPServer(("localhost", 8000), SimpleHandler)
print("Server running on http://localhost:8000")
server.serve_forever()
'''

print(basic_server_code)
print("\nNote: This is example code. Run it in a separate file to test.")

# =============================================================================
# ROUTING EXAMPLE
# =============================================================================
print("\n--- Routing Example ---\n")

routing_code = '''
class RouterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Home page")
            
        elif self.path == "/about":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"About page")
            
        elif self.path == "/api/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status": "ok"}')
            
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 - Page not found")
'''

print(routing_code)

# =============================================================================
# COMPLETE TODO API EXAMPLE
# =============================================================================
print("\n--- Complete Todo API ---\n")

todo_api_code = '''
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

# In-memory storage (resets when server restarts)
todos = [
    {"id": 1, "task": "Learn Python", "done": False},
    {"id": 2, "task": "Build an API", "done": False},
]

class TodoAPI(BaseHTTPRequestHandler):
    
    # Helper method to send JSON responses
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/todos":
            # GET /todos - List all todos
            self._send_json(todos)
            
        elif self.path.startswith("/todos/"):
            # GET /todos/1 - Get specific todo
            try:
                todo_id = int(self.path.split("/")[-1])
                todo = next((t for t in todos if t["id"] == todo_id), None)
                
                if todo:
                    self._send_json(todo)
                else:
                    self._send_json({"error": "Todo not found"}, 404)
            except ValueError:
                self._send_json({"error": "Invalid ID"}, 400)
        else:
            self._send_json({"error": "Not found"}, 404)
    
    def do_POST(self):
        """Handle POST requests."""
        if self.path == "/todos":
            try:
                # Read request body
                content_length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(content_length)
                data = json.loads(body.decode())
                
                # Create new todo
                new_id = max(t["id"] for t in todos) + 1 if todos else 1
                new_todo = {
                    "id": new_id,
                    "task": data.get("task", ""),
                    "done": data.get("done", False)
                }
                todos.append(new_todo)
                
                self._send_json(new_todo, 201)
            except json.JSONDecodeError:
                self._send_json({"error": "Invalid JSON"}, 400)
        else:
            self._send_json({"error": "Not found"}, 404)
    
    def do_PUT(self):
        """Handle PUT requests (update)."""
        if self.path.startswith("/todos/"):
            try:
                todo_id = int(self.path.split("/")[-1])
                
                # Read request body
                content_length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(content_length)
                data = json.loads(body.decode())
                
                # Find and update todo
                for todo in todos:
                    if todo["id"] == todo_id:
                        todo["task"] = data.get("task", todo["task"])
                        todo["done"] = data.get("done", todo["done"])
                        self._send_json(todo)
                        return
                
                self._send_json({"error": "Todo not found"}, 404)
            except (ValueError, json.JSONDecodeError):
                self._send_json({"error": "Invalid request"}, 400)
    
    def do_DELETE(self):
        """Handle DELETE requests."""
        if self.path.startswith("/todos/"):
            try:
                todo_id = int(self.path.split("/")[-1])
                global todos
                original_len = len(todos)
                todos = [t for t in todos if t["id"] != todo_id]
                
                if len(todos) < original_len:
                    self._send_json({"message": "Todo deleted"})
                else:
                    self._send_json({"error": "Todo not found"}, 404)
            except ValueError:
                self._send_json({"error": "Invalid ID"}, 400)
        else:
            self._send_json({"error": "Not found"}, 404)

# Start server
if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), TodoAPI)
    print("Todo API running on http://localhost:8000")
    print("Try these endpoints:")
    print("  GET    http://localhost:8000/todos")
    print("  GET    http://localhost:8000/todos/1")
    print("  POST   http://localhost:8000/todos")
    print("  PUT    http://localhost:8000/todos/1")
    print("  DELETE http://localhost:8000/todos/1")
    server.serve_forever()
'''

print(todo_api_code)

# =============================================================================
# HOW TO READ REQUEST BODY
# =============================================================================
print("\n--- Reading Request Body ---\n")

read_body_code = '''
def do_POST(self):
    # Step 1: Get content length from headers
    content_length = int(self.headers.get("Content-Length", 0))
    
    # Step 2: Read exactly that many bytes
    body_bytes = self.rfile.read(content_length)
    
    # Step 3: Decode bytes to string
    body_text = body_bytes.decode("utf-8")
    
    # Step 4: Parse JSON (if JSON was sent)
    try:
        data = json.loads(body_text)
        print(f"Received: {data}")
    except json.JSONDecodeError:
        # Handle non-JSON data
        print(f"Received text: {body_text}")
'''

print(read_body_code)

# =============================================================================
# TESTING THE API
# =============================================================================
print("\n--- Testing the API (Client Code) ---\n")

test_code = '''
import json
from urllib.request import urlopen, Request

# Test GET all
def get_all_todos():
    with urlopen("http://localhost:8000/todos") as r:
        return json.loads(r.read().decode())

# Test GET one
def get_todo(todo_id):
    try:
        with urlopen(f"http://localhost:8000/todos/{todo_id}") as r:
            return json.loads(r.read().decode())
    except HTTPError as e:
        return {"error": e.code}

# Test POST
def create_todo(task):
    req = Request(
        "http://localhost:8000/todos",
        data=json.dumps({"task": task}).encode(),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urlopen(req) as r:
        return json.loads(r.read().decode())

# Test PUT
def update_todo(todo_id, task=None, done=None):
    data = {}
    if task is not None:
        data["task"] = task
    if done is not None:
        data["done"] = done
    
    req = Request(
        f"http://localhost:8000/todos/{todo_id}",
        data=json.dumps(data).encode(),
        headers={"Content-Type": "application/json"},
        method="PUT"
    )
    with urlopen(req) as r:
        return json.loads(r.read().decode())

# Test DELETE
def delete_todo(todo_id):
    req = Request(
        f"http://localhost:8000/todos/{todo_id}",
        method="DELETE"
    )
    with urlopen(req) as r:
        return json.loads(r.read().decode())

# Run tests
if __name__ == "__main__":
    print("All todos:", get_all_todos())
    print("Created:", create_todo("New task from client"))
    print("Updated:", update_todo(1, done=True))
    print("Deleted:", delete_todo(2))
    print("Final list:", get_all_todos())
'''

print(test_code)

# =============================================================================
# HANDLING DIFFERENT CONTENT TYPES
# =============================================================================
print("\n--- Handling Different Content Types ---\n")

content_type_code = '''
class FlexibleAPI(BaseHTTPRequestHandler):
    def do_POST(self):
        content_type = self.headers.get("Content-Type", "")
        
        # Read body
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        
        if "application/json" in content_type:
            # Handle JSON
            data = json.loads(body.decode())
            response = {"received": data, "type": "json"}
            
        elif "application/x-www-form-urlencoded" in content_type:
            # Handle form data
            from urllib.parse import parse_qs
            data = parse_qs(body.decode())
            response = {"received": data, "type": "form"}
            
        else:
            # Handle plain text or unknown
            response = {"received": body.decode(), "type": "text"}
        
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
'''

print(content_type_code)

# =============================================================================
# SERVER RUNNER UTILITIES
# =============================================================================
print("\n--- Server Runner Utilities ---\n")

runner_code = '''
import socket
from http.server import HTTPServer

def find_free_port(start_port=8000, max_port=9000):
    """Find an available port."""
    for port in range(start_port, max_port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(("localhost", port))
            sock.close()
            if result != 0:  # Port is free
                return port
        except:
            pass
    raise RuntimeError("No free port found")

def run_server(handler_class, port=None):
    """Run server with optional port auto-detection."""
    if port is None:
        port = find_free_port()
    
    server = HTTPServer(("localhost", port), handler_class)
    print(f"Server running on http://localhost:{port}")
    print("Press Ctrl+C to stop")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\\nShutting down...")
        server.shutdown()

# Usage
# run_server(TodoAPI, port=8080)  # Use specific port
# run_server(TodoAPI)             # Auto-find port
'''

print(runner_code)

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Extend BaseHTTPRequestHandler to create custom handlers
2. Implement do_GET, do_POST, do_PUT, do_DELETE for each method
3. Always call send_response(), send_header(), end_headers() before body
4. Use self.wfile.write() to send response body (must be bytes)
5. Read request body with self.rfile.read(content_length)
6. Parse JSON body with json.loads(body.decode())
7. Check self.path to route requests to different handlers
8. Return appropriate status codes (200, 201, 404, etc.)
9. Use Ctrl+C to stop the server
10. http.server is great for learning, but use Flask/FastAPI for production
""")

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
