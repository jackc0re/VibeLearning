"""
Simple Routing - Examples
=========================
Demonstrates URL routing patterns without external frameworks.
"""

print("=" * 60)
print("SIMPLE ROUTING - Examples")
print("=" * 60)

# =============================================================================
# SECTION 1: Basic If/Else Routing
# =============================================================================
print("\n--- 1: Basic If/Else Routing ---\n")

# Simulating request handler
class MockHandler:
    """Mock handler for demonstration."""
    def __init__(self, path):
        self.path = path
        self.response = None
    
    def send_response(self, code):
        self.response = {'status': code}
    
    def set_body(self, body):
        self.response['body'] = body

def basic_route(handler):
    """Route using simple if/elif/else."""
    path = handler.path
    
    if path == '/':
        handler.send_response(200)
        handler.set_body('Home Page')
    elif path == '/about':
        handler.send_response(200)
        handler.set_body('About Page')
    elif path == '/contact':
        handler.send_response(200)
        handler.set_body('Contact Page')
    else:
        handler.send_response(404)
        handler.set_body('Not Found')
    
    return handler.response

# Test routing
test_paths = ['/', '/about', '/contact', '/unknown']
print("Basic routing results:")
for path in test_paths:
    handler = MockHandler(path)
    result = basic_route(handler)
    print(f"  {path:12} → {result['status']}: {result['body']}")

# =============================================================================
# SECTION 2: Dictionary-Based Routing
# =============================================================================
print("\n--- 2: Dictionary-Based Routing ---\n")

def home_handler(handler):
    handler.send_response(200)
    handler.set_body('Home')

def about_handler(handler):
    handler.send_response(200)
    handler.set_body('About')

def not_found_handler(handler):
    handler.send_response(404)
    handler.set_body('Not Found')

# Route dictionary
routes = {
    '/': home_handler,
    '/home': home_handler,
    '/about': about_handler,
}

def dict_route(handler):
    """Route using dictionary lookup."""
    path = handler.path
    
    # Get handler or default to 404
    route_handler = routes.get(path, not_found_handler)
    route_handler(handler)
    
    return handler.response

print("Dictionary routing results:")
for path in ['/', '/home', '/about', '/missing']:
    handler = MockHandler(path)
    result = dict_route(handler)
    print(f"  {path:12} → Handler: {result['body']}")

# =============================================================================
# SECTION 3: Router Class
# =============================================================================
print("\n--- 3: Router Class ---\n")

class Router:
    """Simple router with add/match methods."""
    
    def __init__(self):
        self.routes = {}
    
    def add(self, path, handler):
        """Add a route."""
        self.routes[path] = handler
    
    def match(self, path):
        """Find handler for path."""
        return self.routes.get(path)
    
    def handle(self, handler):
        """Route and call handler."""
        route_handler = self.match(handler.path)
        if route_handler:
            route_handler(handler)
        else:
            not_found_handler(handler)

# Usage
router = Router()
router.add('/', home_handler)
router.add('/about', about_handler)

print("Router class results:")
for path in ['/', '/about', '/other']:
    handler = MockHandler(path)
    router.handle(handler)
    print(f"  {path:12} → {handler.response['body']}")

# =============================================================================
# SECTION 4: Dynamic Route Parameters
# =============================================================================
print("\n--- 4: Dynamic Route Parameters ---\n")

import re

class DynamicRouter:
    """Router with parameter extraction like /users/{id}."""
    
    def __init__(self):
        self.routes = []
    
    def add(self, pattern, handler):
        """Add route with parameter placeholders."""
        # Convert {param} to named regex groups
        regex_pattern = re.sub(r'\{(\w+)\}', r'(?P<\1>[^/]+)', pattern)
        regex = re.compile(f'^{regex_pattern}$')
        self.routes.append({'pattern': regex, 'handler': handler})
    
    def match(self, path):
        """Match path and extract parameters."""
        for route in self.routes:
            match = route['pattern'].match(path)
            if match:
                return route['handler'], match.groupdict()
        return None, None
    
    def handle(self, handler):
        """Route request with params."""
        route_handler, params = self.match(handler.path)
        if route_handler:
            route_handler(handler, **params)
        else:
            not_found_handler(handler)

# Handlers with parameters
def user_handler(handler, user_id):
    handler.send_response(200)
    handler.set_body(f'User Profile: ID={user_id}')

def post_handler(handler, year, month, slug):
    handler.send_response(200)
    handler.set_body(f'Blog Post: {year}/{month}/{slug}')

# Usage
dyn_router = DynamicRouter()
dyn_router.add('/users/{user_id}', user_handler)
dyn_router.add('/blog/{year}/{month}/{slug}', post_handler)

print("Dynamic routing results:")
test_cases = [
    '/users/123',
    '/users/abc',
    '/blog/2026/01/hello-world',
    '/other'
]

for path in test_cases:
    handler = MockHandler(path)
    dyn_router.handle(handler)
    print(f"  {path:30} → {handler.response['body']}")

# =============================================================================
# SECTION 5: Method-Based Routing
# =============================================================================
print("\n--- 5: Method-Based Routing (REST) ---\n")

class RESTRouter:
    """Router that considers HTTP method."""
    
    def __init__(self):
        # routes[path][method] = handler
        self.routes = {}
    
    def add(self, path, method, handler):
        """Add handler for specific method."""
        if path not in self.routes:
            self.routes[path] = {}
        self.routes[path][method] = handler
    
    def match(self, path, method):
        """Match path and method."""
        if path in self.routes and method in self.routes[path]:
            return self.routes[path][method]
        return None

# Handlers for /users endpoint
def list_users(handler):
    handler.set_body('GET /users → List all users')

def create_user(handler):
    handler.set_body('POST /users → Create new user')

def update_user(handler):
    handler.set_body('PUT /users → Update user')

def delete_user(handler):
    handler.set_body('DELETE /users → Delete user')

# Usage
rest_router = RESTRouter()
rest_router.add('/users', 'GET', list_users)
rest_router.add('/users', 'POST', create_user)
rest_router.add('/users', 'PUT', update_user)
rest_router.add('/users', 'DELETE', delete_user)

print("REST routing results:")
test_methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
for method in test_methods:
    handler = MockHandler('/users')
    route_handler = rest_router.match('/users', method)
    if route_handler:
        route_handler(handler)
        print(f"  {method:6} /users → {handler.response['body']}")
    else:
        print(f"  {method:6} /users → 405 Method Not Allowed")

# =============================================================================
# SECTION 6: Route Priority
# =============================================================================
print("\n--- 6: Route Priority (Order Matters) ---\n")

class PriorityRouter:
    """Router that checks routes in order."""
    
    def __init__(self):
        self.routes = []
    
    def add(self, pattern, handler, priority=0):
        """Add route with priority (higher = checked first)."""
        regex = re.compile(f'^{pattern}$')
        self.routes.append((priority, regex, handler))
        # Sort by priority descending
        self.routes.sort(key=lambda x: -x[0])
    
    def match(self, path):
        for priority, pattern, handler in self.routes:
            if pattern.match(path):
                return handler
        return None

# Example: specific vs general routes
def new_user_form(handler):
    handler.set_body('New User Form (specific)')

def user_detail(handler):
    handler.set_body('User Detail (general)')

# Correct order: specific first
priority_router = PriorityRouter()
priority_router.add('/users/new', new_user_form, priority=10)  # High priority
priority_router.add('/users/([^/]+)', user_detail, priority=5)  # Lower priority

print("Route priority (specific first):")
for path in ['/users/new', '/users/123']:
    handler = MockHandler(path)
    route_handler = priority_router.match(path)
    if route_handler:
        route_handler(handler)
        print(f"  {path:15} → {handler.response['body']}")

# =============================================================================
# SECTION 7: Middleware Pattern
# =============================================================================
print("\n--- 7: Middleware Pattern ---\n")

class Middleware:
    """Base middleware class."""
    
    def __init__(self, app):
        self.app = app
    
    def __call__(self, handler):
        return self.app(handler)

class LoggingMiddleware(Middleware):
    """Logs all requests."""
    
    def __call__(self, handler):
        print(f"  [LOG] {handler.path}")
        return self.app(handler)

class AuthMiddleware(Middleware):
    """Simple auth check."""
    
    def __call__(self, handler):
        if handler.path.startswith('/admin'):
            handler.send_response(401)
            handler.set_body('Unauthorized')
            return handler.response
        return self.app(handler)

# Simple app
def simple_app(handler):
    handler.send_response(200)
    handler.set_body(f'Response for {handler.path}')
    return handler.response

# Wrap with middleware
logged_app = LoggingMiddleware(simple_app)
protected_app = AuthMiddleware(logged_app)

print("Middleware chain:")
print("  Request → AuthMiddleware → LoggingMiddleware → App")
print()

for path in ['/home', '/admin/dashboard']:
    handler = MockHandler(path)
    result = protected_app(handler)
    print(f"  Final: {result['status']} - {result['body']}")
    print()

# =============================================================================
# SECTION 8: Nested Routers
# =============================================================================
print("\n--- 8: Nested Routers ---\n")

class NestedRouter:
    """Router that supports sub-routers."""
    
    def __init__(self):
        self.routes = {}
        self.sub_routers = {}
    
    def add(self, path, handler):
        self.routes[path] = handler
    
    def mount(self, prefix, router):
        """Mount a sub-router at a prefix."""
        self.sub_routers[prefix] = router
    
    def handle(self, path):
        """Handle path, possibly delegating to sub-router."""
        # Check sub-routers
        for prefix, router in self.sub_routers.items():
            if path.startswith(prefix):
                remaining = path[len(prefix):]
                if not remaining.startswith('/'):
                    remaining = '/' + remaining
                return router.handle(remaining)
        
        # Check direct routes
        return self.routes.get(path, lambda: '404')

# Create API sub-router
api_router = NestedRouter()
api_router.add('/users', lambda: 'API: List users')
api_router.add('/posts', lambda: 'API: List posts')

# Create main router
main_router = NestedRouter()
main_router.add('/', lambda: 'Home')
main_router.add('/about', lambda: 'About')
main_router.mount('/api', api_router)

print("Nested routing results:")
test_paths = ['/', '/about', '/api/users', '/api/posts']
for path in test_paths:
    result = main_router.handle(path)
    print(f"  {path:15} → {result}")

# =============================================================================
# SECTION 9: URL Building
# =============================================================================
print("\n--- 9: Reverse URL Building ---\n")

class URLBuilder:
    """Build URLs from route names and parameters."""
    
    def __init__(self):
        self.named_routes = {}
    
    def add(self, name, pattern):
        """Register a named route."""
        self.named_routes[name] = pattern
    
    def build(self, name, **kwargs):
        """Build URL for named route with parameters."""
        if name not in self.named_routes:
            raise ValueError(f"Unknown route: {name}")
        
        url = self.named_routes[name]
        for key, value in kwargs.items():
            url = url.replace(f'{{{key}}}', str(value))
        
        return url

# Usage
url_builder = URLBuilder()
url_builder.add('home', '/')
url_builder.add('about', '/about')
url_builder.add('user', '/users/{id}')
url_builder.add('post', '/blog/{year}/{month}/{slug}')

print("URL building:")
print(f"  home              → {url_builder.build('home')}")
print(f"  user(id=123)      → {url_builder.build('user', id=123)}")
print(f"  post(...)         → {url_builder.build('post', year=2026, month=1, slug='hello')}")

# =============================================================================
# SECTION 10: Complete Routing System
# =============================================================================
print("\n--- 10: Complete Routing System ---\n")

class CompleteRouter:
    """Full-featured router combining all patterns."""
    
    def __init__(self):
        self.routes = []
        self.middleware = []
    
    def add(self, pattern, handler, methods=None, name=None):
        """Add a route with options."""
        if methods is None:
            methods = ['GET']
        
        # Convert pattern to regex
        regex = re.sub(r'\{(\w+)\}', r'(?P<\1>[^/]+)', pattern)
        regex = re.compile(f'^{regex}$')
        
        route = {
            'pattern': regex,
            'handler': handler,
            'methods': methods,
            'name': name
        }
        self.routes.append(route)
    
    def use(self, middleware):
        """Add middleware."""
        self.middleware.append(middleware)
    
    def match(self, path, method='GET'):
        """Find matching route."""
        for route in self.routes:
            match = route['pattern'].match(path)
            if match and method in route['methods']:
                return route['handler'], match.groupdict()
        return None, None

# Create complete router
complete = CompleteRouter()

# Add routes with various options
complete.add('/', lambda h: 'Home', name='home')
complete.add('/about', lambda h: 'About', name='about')
complete.add('/users', lambda h: 'List users', methods=['GET'])
complete.add('/users', lambda h: 'Create user', methods=['POST'])
complete.add('/users/{id}', lambda h, **kw: f"User {kw.get('id')}", name='user')

print("Complete router routes:")
print("  /                 → Home (GET)")
print("  /about            → About (GET)")
print("  /users            → List users (GET)")
print("  /users            → Create user (POST)")
print("  /users/{id}       → User detail (GET)")

# Test matching
print("\nMatching tests:")
tests = [
    ('/', 'GET'),
    ('/users', 'GET'),
    ('/users', 'POST'),
    ('/users/42', 'GET'),
    ('/users/42', 'DELETE'),
]

for path, method in tests:
    handler, params = complete.match(path, method)
    if handler:
        result = handler(None) if not params else handler(None, **params)
        print(f"  {method:6} {path:15} → {result}")
    else:
        print(f"  {method:6} {path:15} → 404")

print("\n" + "=" * 60)
print("Key Routing Patterns:")
print("=" * 60)
print("""
1. Basic:        if/elif/else for simple routing
2. Dictionary:   routes = {'/path': handler}
3. Router Class: router.add(path, handler)
4. Dynamic:      router.add('/users/{id}', handler)
5. REST:         router.add('/users', handler, methods=['GET', 'POST'])
6. Priority:     Order matters - specific routes first
7. Middleware:   Chain processing before/after handlers
8. Nested:       Mount sub-routers at prefixes
9. URL Building: Reverse routes for links
10. Complete:    Combine all features as needed
""")

print("=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
