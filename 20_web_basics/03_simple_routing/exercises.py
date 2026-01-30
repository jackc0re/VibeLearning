"""
Simple Routing - Exercises
==========================
Practice building URL routing systems.
"""

print("=" * 60)
print("SIMPLE ROUTING - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: Basic Router
# =============================================================================
print("\n--- Exercise 1: Basic Router ---\n")
"""
Create a SimpleRouter class that:
- Has an add(path, handler) method
- Has a match(path) method that returns the handler or None
- Supports at least 5 different routes

Test it with paths: '/', '/about', '/contact', '/products', '/products/123'
"""

# Your code here:


# =============================================================================
# EXERCISE 2: Dynamic Parameters
# =============================================================================
print("\n--- Exercise 2: Dynamic Parameters ---\n")
"""
Extend your router to support parameters like /users/{id}:
- Parse {param} syntax in route patterns
- Extract parameter values from URLs
- Return both handler and parameters from match()

Test: /users/123 should match /users/{id} with {'id': '123'}
"""

# Your code here:


# =============================================================================
# EXERCISE 3: HTTP Method Routing
# =============================================================================
print("\n--- Exercise 3: HTTP Method Routing ---\n")
"""
Create a RESTRouter that considers HTTP methods:
- add(path, method, handler) - register handler for specific method
- match(path, method) - returns handler only if method matches

Support GET, POST, PUT, DELETE for /users endpoint with different handlers.
"""

# Your code here:


# =============================================================================
# EXERCISE 4: Route Groups
# =============================================================================
print("\n--- Exercise 4: Route Groups ---\n")
"""
Create a router that supports route groups with shared prefixes:
- group(prefix, callback) - creates a sub-router with prefix
- Routes added in callback automatically get the prefix

Example:
    router.group('/api', lambda r:
        r.add('/users', list_users)
        r.add('/posts', list_posts)
    )
    
Results in:
    /api/users → list_users
    /api/posts → list_posts
"""

# Your code here:


# =============================================================================
# EXERCISE 5: Route Middleware
# =============================================================================
print("\n--- Exercise 5: Route Middleware ---\n")
"""
Create middleware support for your router:
- before_request(handler) - runs before route handler
- after_request(response) - runs after, can modify response

Create two middleware:
1. TimingMiddleware - adds X-Response-Time header
2. AuthMiddleware - checks for Authorization header on /admin/* routes
"""

# Your code here:


# =============================================================================
# EXERCISE 6: URL Generation
# =============================================================================
print("\n--- Exercise 6: URL Generation ---\n")
"""
Add reverse URL generation to your router:
- add(path, handler, name='route_name') - register named route
- url(name, **kwargs) - generate URL for named route with params

Example:
    router.add('/users/{id}', user_handler, name='user_detail')
    router.url('user_detail', id=123) → '/users/123'
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
print("\n--- Solution 1: Basic Router ---\n")

class SimpleRouter:
    """Basic router with path to handler mapping."""
    
    def __init__(self):
        self.routes = {}
    
    def add(self, path, handler):
        """Add a route."""
        self.routes[path] = handler
    
    def match(self, path):
        """Find handler for path."""
        return self.routes.get(path)

# Test
router = SimpleRouter()
router.add('/', lambda: 'Home')
router.add('/about', lambda: 'About')
router.add('/contact', lambda: 'Contact')
router.add('/products', lambda: 'Products List')
router.add('/products/123', lambda: 'Product 123')

print("Routes registered:")
test_paths = ['/', '/about', '/contact', '/products', '/products/123', '/missing']
for path in test_paths:
    handler = router.match(path)
    result = handler() if handler else '404 Not Found'
    print(f"  {path:15} → {result}")

# -------------------------------------------------------------------------
# Solution 2
# -------------------------------------------------------------------------
print("\n--- Solution 2: Dynamic Parameters ---\n")

import re

class DynamicRouter:
    """Router with parameter extraction."""
    
    def __init__(self):
        self.routes = []
    
    def add(self, pattern, handler):
        """Add route with {param} placeholders."""
        # Convert {param} to named capture groups
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

# Test
dyn_router = DynamicRouter()
dyn_router.add('/users/{id}', lambda **kw: f"User {kw['id']}")
dyn_router.add('/posts/{year}/{month}/{slug}', 
               lambda **kw: f"Post: {kw['year']}/{kw['month']}/{kw['slug']}")
dyn_router.add('/products/{category}/{id}', 
               lambda **kw: f"Product {kw['id']} in {kw['category']}")

print("Dynamic routes:")
test_cases = [
    '/users/123',
    '/users/abc',
    '/posts/2026/01/hello-world',
    '/products/electronics/456',
    '/unknown'
]

for path in test_cases:
    result = dyn_router.match(path)
    if result:
        handler, params = result
        print(f"  {path:30} → {handler(**params)} (params: {params})")
    else:
        print(f"  {path:30} → 404")

# -------------------------------------------------------------------------
# Solution 3
# -------------------------------------------------------------------------
print("\n--- Solution 3: HTTP Method Routing ---\n")

class RESTRouter:
    """Router with HTTP method support."""
    
    def __init__(self):
        self.routes = {}  # {path: {method: handler}}
    
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
    
    def get_allowed_methods(self, path):
        """Get allowed methods for a path (for 405 response)."""
        if path in self.routes:
            return list(self.routes[path].keys())
        return []

# Test
rest = RESTRouter()
rest.add('/users', 'GET', lambda: 'List users')
rest.add('/users', 'POST', lambda: 'Create user')
rest.add('/users', 'PUT', lambda: 'Update user')
rest.add('/users', 'DELETE', lambda: 'Delete user')
rest.add('/users/{id}', 'GET', lambda: 'Get single user')

print("REST routing for /users:")
for method in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']:
    handler = rest.match('/users', method)
    if handler:
        print(f"  {method:6} → {handler()}")
    else:
        allowed = rest.get_allowed_methods('/users')
        print(f"  {method:6} → 405 (allowed: {', '.join(allowed)})")

# -------------------------------------------------------------------------
# Solution 4
# -------------------------------------------------------------------------
print("\n--- Solution 4: Route Groups ---\n")

class GroupRouter:
    """Router with support for grouped routes."""
    
    def __init__(self):
        self.routes = {}
        self.prefix = ''
    
    def add(self, path, handler):
        """Add route with current prefix."""
        full_path = self.prefix + path
        self.routes[full_path] = handler
    
    def group(self, prefix, callback):
        """Create a route group with prefix."""
        old_prefix = self.prefix
        self.prefix = old_prefix + prefix
        callback(self)
        self.prefix = old_prefix
    
    def match(self, path):
        """Find handler for path."""
        return self.routes.get(path)

# Test
group_router = GroupRouter()

# Add regular routes
group_router.add('/', lambda: 'Home')
group_router.add('/about', lambda: 'About')

# Add API group
group_router.group('/api', lambda r: [
    r.add('/users', lambda: 'API: List users'),
    r.add('/users/{id}', lambda: 'API: Get user'),
    r.add('/posts', lambda: 'API: List posts'),
])

# Add admin group  
group_router.group('/admin', lambda r: [
    r.add('/dashboard', lambda: 'Admin: Dashboard'),
    r.add('/users', lambda: 'Admin: Manage users'),
])

print("Grouped routes:")
test_paths = ['/', '/about', '/api/users', '/api/users/123', 
              '/api/posts', '/admin/dashboard', '/admin/users']
for path in test_paths:
    handler = group_router.match(path)
    result = handler() if handler else '404'
    print(f"  {path:20} → {result}")

# -------------------------------------------------------------------------
# Solution 5
# -------------------------------------------------------------------------
print("\n--- Solution 5: Route Middleware ---\n")

class MiddlewareRouter:
    """Router with middleware support."""
    
    def __init__(self):
        self.routes = {}
        self.before_handlers = []
        self.after_handlers = []
    
    def add(self, path, handler):
        self.routes[path] = handler
    
    def before_request(self, handler):
        """Register before middleware."""
        self.before_handlers.append(handler)
    
    def after_request(self, handler):
        """Register after middleware."""
        self.after_handlers.append(handler)
    
    def handle(self, path, request):
        """Handle request with middleware."""
        # Run before middleware
        for middleware in self.before_handlers:
            result = middleware(request)
            if result:  # If middleware returns something, abort
                return result
        
        # Run route handler
        handler = self.routes.get(path)
        if not handler:
            return {'status': 404, 'body': 'Not Found'}
        
        response = handler(request)
        
        # Run after middleware
        for middleware in self.after_handlers:
            response = middleware(request, response)
        
        return response

# Timing middleware
import time

def timing_middleware(request):
    request['start_time'] = time.time()

def add_timing_header(request, response):
    duration = int((time.time() - request['start_time']) * 1000)
    response['headers'] = response.get('headers', {})
    response['headers']['X-Response-Time'] = f"{duration}ms"
    return response

# Auth middleware
def auth_middleware(request):
    if request.get('path', '').startswith('/admin'):
        auth = request.get('headers', {}).get('Authorization')
        if not auth:
            return {'status': 401, 'body': 'Unauthorized'}
    return None

# Test
mw_router = MiddlewareRouter()
mw_router.add('/', lambda r: {'status': 200, 'body': 'Home'})
mw_router.add('/admin/dashboard', lambda r: {'status': 200, 'body': 'Dashboard'})

# Add middleware
mw_router.before_request(timing_middleware)
mw_router.before_request(auth_middleware)
mw_router.after_request(add_timing_header)

print("Middleware routing:")

# Test without auth
request1 = {'path': '/'}
result1 = mw_router.handle('/', request1)
print(f"  GET /              → {result1['status']} ({result1.get('headers', {})})")

# Test admin without auth
request2 = {'path': '/admin/dashboard'}
result2 = mw_router.handle('/admin/dashboard', request2)
print(f"  GET /admin         → {result2['status']} ({result2['body']})")

# Test admin with auth
request3 = {'path': '/admin/dashboard', 'headers': {'Authorization': 'Bearer token'}}
result3 = mw_router.handle('/admin/dashboard', request3)
print(f"  GET /admin (auth)  → {result3['status']} ({result3.get('headers', {})})")

# -------------------------------------------------------------------------
# Solution 6
# -------------------------------------------------------------------------
print("\n--- Solution 6: URL Generation ---\n")

class URLRouter:
    """Router with named routes and URL generation."""
    
    def __init__(self):
        self.routes = {}      # path -> handler
        self.named_routes = {}  # name -> path pattern
    
    def add(self, path, handler, name=None):
        """Add route with optional name."""
        self.routes[path] = handler
        if name:
            self.named_routes[name] = path
    
    def match(self, path):
        """Find handler for path."""
        return self.routes.get(path)
    
    def url(self, name, **kwargs):
        """Generate URL for named route."""
        if name not in self.named_routes:
            raise ValueError(f"Unknown route: {name}")
        
        url = self.named_routes[name]
        for key, value in kwargs.items():
            placeholder = f'{{{key}}}'
            if placeholder in url:
                url = url.replace(placeholder, str(value))
        
        # Check if all params filled
        if '{' in url:
            raise ValueError(f"Missing parameters for URL: {url}")
        
        return url

# Test
url_router = URLRouter()
url_router.add('/', lambda: 'Home', name='home')
url_router.add('/about', lambda: 'About', name='about')
url_router.add('/users', lambda: 'List', name='users')
url_router.add('/users/{id}', lambda: 'Detail', name='user_detail')
url_router.add('/posts/{year}/{month}/{slug}', lambda: 'Post', name='blog_post')

print("URL generation:")
print(f"  home              → {url_router.url('home')}")
print(f"  about             → {url_router.url('about')}")
print(f"  users             → {url_router.url('users')}")
print(f"  user_detail(id=1) → {url_router.url('user_detail', id=1)}")
print(f"  blog_post(...)    → {url_router.url('blog_post', year=2026, month=1, slug='hello')}")

print("\n" + "=" * 60)
print("All solutions complete!")
print("=" * 60)
