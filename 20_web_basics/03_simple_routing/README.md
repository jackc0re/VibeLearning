# 🛣️ Simple Routing

> Building URL routing systems without frameworks

---

## What is URL Routing?

**URL Routing** is the process of mapping URL paths to specific handler functions. When a user visits `/about`, the router determines which code should run to generate that page.

Think of routing like a restaurant menu:
- Customer orders "Burger #3" → Kitchen makes a burger
- Customer orders "Salad #5" → Kitchen makes a salad
- The menu (router) maps order numbers to recipes (handlers)

---

## Basic Routing Approach

```python
from http.server import BaseHTTPRequestHandler

class RouterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Simple if/elif routing
        if self.path == '/':
            self.serve_home()
        elif self.path == '/about':
            self.serve_about()
        elif self.path == '/contact':
            self.serve_contact()
        else:
            self.serve_404()
```

---

## Building a Router Class

A cleaner approach is to create a separate router:

```python
class SimpleRouter:
    """URL router for mapping paths to handlers."""
    
    def __init__(self):
        self.routes = {}
    
    def add_route(self, path, handler):
        """Register a handler for a path."""
        self.routes[path] = handler
    
    def handle(self, path, request_handler):
        """Route a request to the appropriate handler."""
        if path in self.routes:
            self.routes[path](request_handler)
        else:
            request_handler.send_error(404, "Not Found")

# Usage
router = SimpleRouter()
router.add_route('/', home_handler)
router.add_route('/about', about_handler)
```

---

## Dynamic Route Parameters

Static routes (`/about`) are limiting. Dynamic routes capture parts of the URL:

```python
class DynamicRouter:
    """Router with parameter support like /users/{id}."""
    
    def __init__(self):
        self.routes = []
    
    def add_route(self, pattern, handler):
        """Add a route with optional parameters."""
        # Convert /users/{id} to regex pattern
        import re
        regex = re.sub(r'\{(\w+)\}', r'(?P<\1>[^/]+)', pattern)
        self.routes.append((re.compile(f'^{regex}$'), handler))
    
    def handle(self, path, request_handler):
        """Try to match path against all routes."""
        for pattern, handler in self.routes:
            match = pattern.match(path)
            if match:
                params = match.groupdict()
                handler(request_handler, **params)
                return
        
        request_handler.send_error(404, "Not Found")

# Usage
router = DynamicRouter()
router.add_route('/users/{id}', user_detail_handler)
router.add_route('/posts/{slug}', post_handler)

# /users/123 → user_detail_handler(request, id='123')
# /posts/hello-world → post_handler(request, slug='hello-world')
```

---

## RESTful Route Patterns

Organize routes by resource and HTTP method:

```python
class RESTRouter:
    """Router for RESTful APIs."""
    
    def __init__(self):
        # routes[path][method] = handler
        self.routes = {}
    
    def route(self, path, methods=['GET']):
        """Decorator to register routes."""
        def decorator(func):
            if path not in self.routes:
                self.routes[path] = {}
            for method in methods:
                self.routes[path][method] = func
            return func
        return decorator
    
    def handle(self, method, path, request_handler):
        """Route based on method and path."""
        if path in self.routes and method in self.routes[path]:
            self.routes[path][method](request_handler)
        else:
            request_handler.send_error(404)

# Usage
router = RESTRouter()

@router.route('/users', methods=['GET'])
def list_users(handler):
    handler.send_json({'users': [...]})

@router.route('/users', methods=['POST'])
def create_user(handler):
    # Create user logic
    pass

@router.route('/users/{id}', methods=['GET'])
def get_user(handler, user_id):
    handler.send_json({'id': user_id, ...})
```

---

## Route Priority and Order

Routes are checked in order - put specific routes before general ones:

```python
# ✅ CORRECT: Specific first
router.add_route('/users/new', new_user_form)    # First
router.add_route('/users/{id}', user_detail)     # Second

# ❌ WRONG: General first
router.add_route('/users/{id}', user_detail)     # Matches /users/new too!
router.add_route('/users/new', new_user_form)
```

---

## Complete Routing Example

```python
"""
routing_server.py - Server with comprehensive routing
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import re

class Router:
    """A flexible URL router with parameter support."""
    
    def __init__(self):
        self.routes = []
    
    def add(self, pattern, handler, methods=['GET']):
        """Add a route with pattern, handler, and allowed methods."""
        # Convert {param} to named capture groups
        regex_pattern = re.sub(r'\{(\w+)\}', r'(?P<\1>[^/]+)', pattern)
        regex = re.compile(f'^{regex_pattern}$')
        
        self.routes.append({
            'pattern': regex,
            'handler': handler,
            'methods': methods
        })
    
    def match(self, path, method):
        """Find a matching route. Returns (handler, params) or (None, None)."""
        for route in self.routes:
            match = route['pattern'].match(path)
            if match and method in route['methods']:
                return route['handler'], match.groupdict()
        return None, None


# Create router
router = Router()

# Sample data
users = {
    '1': {'id': '1', 'name': 'Alice', 'email': 'alice@example.com'},
    '2': {'id': '2', 'name': 'Bob', 'email': 'bob@example.com'},
}

# Define handlers
def home(handler):
    handler.send_html('<h1>Welcome</h1><p>API Server Running</p>')

def about(handler):
    handler.send_html('<h1>About</h1><p>Built with Python http.server</p>')

def list_users(handler):
    handler.send_json({'users': list(users.values())})

def get_user(handler, user_id):
    if user_id in users:
        handler.send_json(users[user_id])
    else:
        handler.send_error(404, "User not found")

def not_found(handler):
    handler.send_error(404, "Page not found")

# Register routes
router.add('/', home)
router.add('/about', about)
router.add('/api/users', list_users)
router.add('/api/users/{id}', get_user)


class RoutedHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        handler, params = router.match(self.path, 'GET')
        if handler:
            if params:
                handler(self, **params)
            else:
                handler(self)
        else:
            not_found(self)
    
    def send_html(self, html, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
    
    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def log_message(self, format, *args):
        print(f"[{self.date_time_string()}] {args[0]}")


if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), RoutedHandler)
    print('Server with routing at http://localhost:8000')
    print('Routes:')
    print('  /')
    print('  /about')
    print('  /api/users')
    print('  /api/users/{id}')
    server.serve_forever()
```

---

## Nested Routers

For larger applications, organize routes into modules:

```python
class NestedRouter:
    """Router that supports sub-routers."""
    
    def __init__(self):
        self.routes = []
        self.sub_routers = {}
    
    def add(self, pattern, handler=None, router=None):
        """Add a handler or sub-router."""
        if router:
            self.sub_routers[pattern] = router
        else:
            regex = re.compile(f'^{pattern}$')
            self.routes.append((regex, handler))
    
    def handle(self, path, handler_instance):
        """Route request, possibly to sub-router."""
        # Check sub-routers first
        for prefix, router in self.sub_routers.items():
            if path.startswith(prefix):
                remaining = path[len(prefix):]
                return router.handle(remaining, handler_instance)
        
        # Check direct routes
        for pattern, handler in self.routes:
            match = pattern.match(path)
            if match:
                handler(handler_instance, **match.groupdict())
                return
        
        handler_instance.send_error(404)

# Usage: Separate routers for different sections
api_router = Router()
api_router.add('/users', list_users)
api_router.add('/users/{id}', get_user)

main_router = NestedRouter()
main_router.add('/', home)
main_router.add('/about', about)
main_router.add('/api', router=api_router)  # Nested!
```

---

## Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|---------|---------------|------------------|
| General routes before specific | `/users/{id}` matches before `/users/new` | Order routes from most specific to least specific |
| Not validating parameters | `user_id` might be invalid | Always validate and return 404/400 if invalid |
| Case-sensitive routes | `/About` vs `/about` | Normalize paths with `.lower()` |
| Trailing slashes matter | `/users` ≠ `/users/` | Decide on a convention and redirect |
| Missing 404 handler | Users get confusing errors | Always have a catch-all handler |

---

## Quick Reference

```python
# Simple routing with if/elif
if path == '/': ...
elif path == '/about': ...

# Router class
router = Router()
router.add('/path', handler)
router.add('/item/{id}', handler_with_params)
handler, params = router.match(path, method)

# Decorator style
@router.route('/users', methods=['GET', 'POST'])
def users(handler): ...
```

---

## Next Steps

Now that you can route URLs, let's learn how to generate dynamic HTML with templates!

→ Continue to [04: Templating](../04_templating/)
