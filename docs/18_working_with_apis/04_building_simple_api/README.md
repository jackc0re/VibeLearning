# 🏗️ Building a Simple API

> Creating REST APIs with Python's `http.server`

---

## Introduction

Python's `http.server` module lets you build HTTP servers without external frameworks. While not suitable for production (use Flask, FastAPI, or Django for that), it's perfect for:

- Learning how HTTP servers work
- Testing and prototyping
- Local development tools
- Understanding what frameworks do for you

---

## Basic HTTP Server

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send 200 OK status
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
```

Run this and visit `http://localhost:8000` in your browser!

---

## Handling Routes

Check `self.path` to route requests:

```python
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
            
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Page not found")
```

---

## REST API Example

Let's build a simple Todo API:

```python
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

# In-memory storage
todos = [
    {"id": 1, "task": "Learn Python", "done": False},
    {"id": 2, "task": "Build API", "done": False},
]

class TodoAPI(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        """Helper to send JSON response."""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/todos":
            # Get all todos
            self._send_json(todos)
            
        elif self.path.startswith("/todos/"):
            # Get single todo
            todo_id = int(self.path.split("/")[-1])
            todo = next((t for t in todos if t["id"] == todo_id), None)
            
            if todo:
                self._send_json(todo)
            else:
                self._send_json({"error": "Not found"}, 404)
        else:
            self._send_json({"error": "Not found"}, 404)
    
    def do_POST(self):
        """Handle POST requests."""
        if self.path == "/todos":
            # Read request body
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            data = json.loads(body.decode())
            
            # Create new todo
            new_id = max(t["id"] for t in todos) + 1
            new_todo = {
                "id": new_id,
                "task": data.get("task", ""),
                "done": False
            }
            todos.append(new_todo)
            
            self._send_json(new_todo, 201)
    
    def do_DELETE(self):
        """Handle DELETE requests."""
        if self.path.startswith("/todos/"):
            todo_id = int(self.path.split("/")[-1])
            global todos
            todos = [t for t in todos if t["id"] != todo_id]
            self._send_json({"message": "Deleted"})

# Start server
server = HTTPServer(("localhost", 8000), TodoAPI)
print("API running on http://localhost:8000")
server.serve_forever()
```

---

## Reading Request Body

```python
def do_POST(self):
    # Get content length from headers
    content_length = int(self.headers.get("Content-Length", 0))
    
    # Read that many bytes
    body = self.rfile.read(content_length)
    
    # Decode and parse
    text = body.decode("utf-8")
    data = json.loads(text)
    
    # Process data...
```

---

## API Design Patterns

### RESTful Endpoints

| Method | Endpoint | Action |
|--------|----------|--------|
| GET | `/items` | List all items |
| GET | `/items/1` | Get item with ID 1 |
| POST | `/items` | Create new item |
| PUT | `/items/1` | Update item 1 |
| DELETE | `/items/1` | Delete item 1 |

### Response Format

```python
# Success response
{
    "success": True,
    "data": { ... }
}

# Error response
{
    "success": False,
    "error": "Item not found",
    "code": 404
}
```

---

## Testing Your API

```python
# In another terminal, test with:
import json
from urllib.request import urlopen, Request

# GET all todos
with urlopen("http://localhost:8000/todos") as r:
    print(json.loads(r.read().decode()))

# POST new todo
req = Request(
    "http://localhost:8000/todos",
    data=json.dumps({"task": "New task"}).encode(),
    headers={"Content-Type": "application/json"},
    method="POST"
)
with urlopen(req) as r:
    print(json.loads(r.read().decode()))
```

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Forgetting `end_headers()` | Client hangs waiting | Always call before `wfile.write()` |
| Not decoding request body | Binary data instead of text | Use `.decode("utf-8")` |
| Missing Content-Length | Can't read POST data | Check headers before reading body |
| Not handling 404s | All paths return 200 | Check path and return appropriate status |

---

## When to Use What

| Use Case | Solution |
|----------|----------|
| Learning/testing | `http.server` |
| Small production API | Flask or FastAPI |
| Large application | Django REST Framework |
| High performance | FastAPI + async |

---

## Quick Reference

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class APIHandler(BaseHTTPRequestHandler):
    def _json_response(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def do_GET(self):
        self._json_response({"message": "GET received"})
    
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length).decode())
        self._json_response({"received": body}, 201)

server = HTTPServer(("localhost", 8000), APIHandler)
server.serve_forever()
```

---

## Next Steps

Now you can build APIs! Let's learn best practices for production-ready code.

→ Continue to [05: API Best Practices](../05_api_best_practices/)
