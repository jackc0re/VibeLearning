# 🎯 Simple Routing - Quiz

Test your knowledge of URL routing concepts.

---

## Multiple Choice Questions

### Question 1
What is URL routing?

- A) Sending URLs to different servers
- B) Mapping URL paths to handler functions
- C) Encrypting URLs for security
- D) Shortening long URLs

### Question 2
Why should specific routes be defined before general ones?

- A) General routes are slower
- B) Specific routes might never be matched otherwise
- C) It improves security
- D) It's just a convention

### Question 3
What does the route pattern `/users/{id}` represent?

- A) A literal URL with curly braces
- B) A dynamic route where `{id}` is a parameter
- C) A broken URL pattern
- D) A query parameter

### Question 4
In REST API design, which HTTP method should be used to retrieve data?

- A) POST
- B) PUT
- C) GET
- D) DELETE

### Question 5
What is middleware in routing?

- A) A database layer
- B) Code that runs before/after route handlers
- C) A type of URL pattern
- D) A security protocol

### Question 6
What regex pattern would match `/users/{id}` where id can be any non-slash characters?

- A) `^/users/.+$`
- B) `^/users/(?P<id>[^/]+)$`
- C) `^/users/{id}$`
- D) `^/users/\d+$`

### Question 7
What does "reverse URL building" mean?

- A) Reversing the characters in a URL
- B) Generating a URL from a route name and parameters
- C) Redirecting to a previous page
- D) Creating short URLs

### Question 8
Which status code indicates that a URL exists but the HTTP method is not allowed?

- A) 404
- B) 405
- C) 500
- D) 403

### Question 9
What is the purpose of route groups?

- A) To organize routes alphabetically
- B) To share common prefixes and middleware
- C) To limit the number of routes
- D) To group routes by file size

### Question 10
In a router, what should happen if no route matches the request?

- A) Return 200 OK with empty body
- B) Return 404 Not Found
- C) Redirect to home page
- D) Raise an exception

---

## Short Answer Questions

### Question 11
Explain why route order matters and give an example where incorrect ordering causes problems.

### Question 12
What is the difference between these two route patterns?
- `/users/{id}`
- `/users/new`

Why would you need both, and in what order should they be checked?

### Question 13
Describe how you would implement nested routers (sub-routers) for an API with these prefixes:
- `/api/v1/users`
- `/api/v1/posts`
- `/api/v2/users`

### Question 14
What are the benefits of using named routes and URL generation instead of hardcoding URLs?

### Question 15
Explain the difference between route parameters (like `/users/{id}`) and query parameters (like `/users?id=123`). When would you use each?

---

## Code Challenge

### Question 16
Create a complete router class that supports:
1. Static routes (`/about`)
2. Dynamic routes (`/users/{id}`)
3. HTTP method routing
4. Named routes with URL generation

Include a simple test that demonstrates all features.

---

## Answers

<details>
<summary>Click to expand answers</summary>

### Multiple Choice

1. **B** - Mapping URL paths to handler functions
2. **B** - Specific routes might never be matched otherwise (e.g., `/users/new` vs `/users/{id}`)
3. **B** - A dynamic route where `{id}` is a parameter
4. **C** - GET
5. **B** - Code that runs before/after route handlers
6. **B** - `^/users/(?P<id>[^/]+)$`
7. **B** - Generating a URL from a route name and parameters
8. **B** - 405 Method Not Allowed
9. **B** - To share common prefixes and middleware
10. **B** - Return 404 Not Found

### Short Answer

11. Route order matters because the first matching route wins. If you define `/users/{id}` before `/users/new`, a request to `/users/new` will match the pattern `/users/{id}` with `id='new'`, never reaching the specific handler. Always define specific routes before general ones.

12. `/users/{id}` matches any user ID like `/users/123`, `/users/abc`. `/users/new` matches only that exact path, typically for a form to create new users. Define `/users/new` first, then `/users/{id}`.

13. Create separate routers for v1 and v2, each with their own user and post sub-routers. Mount them at the appropriate prefixes:
    ```python
    v1_router = Router()
    v1_router.add('/users', ...)
    v1_router.add('/posts', ...)
    
    main_router = Router()
    main_router.mount('/api/v1', v1_router)
    main_router.mount('/api/v2', v2_router)
    ```

14. Named routes allow you to change the URL pattern in one place without updating all links in your code. URL generation ensures parameters are properly encoded and reduces errors from typos.

15. Route parameters are part of the URL path (`/users/123`) and define the resource identity. Query parameters (`?status=active`) are for filtering, sorting, or additional options. Use route params for required identifiers, query params for optional modifiers.

### Code Challenge

16. ```python
    import re
    
    class CompleteRouter:
        def __init__(self):
            self.routes = []
            self.named_routes = {}
        
        def add(self, pattern, handler, methods=None, name=None):
            if methods is None:
                methods = ['GET']
            
            # Convert {param} to regex
            regex = re.sub(r'\{(\w+)\}', r'(?P<\1>[^/]+)', pattern)
            regex = re.compile(f'^{regex}$')
            
            self.routes.append({
                'pattern': regex,
                'handler': handler,
                'methods': methods
            })
            
            if name:
                self.named_routes[name] = pattern
        
        def match(self, path, method='GET'):
            for route in self.routes:
                match = route['pattern'].match(path)
                if match and method in route['methods']:
                    return route['handler'], match.groupdict()
            return None, None
        
        def url(self, name, **kwargs):
            if name not in self.named_routes:
                raise ValueError(f"Unknown route: {name}")
            
            url = self.named_routes[name]
            for key, value in kwargs.items():
                url = url.replace(f'{{{key}}}', str(value))
            return url
    
    # Test
    router = CompleteRouter()
    router.add('/', lambda: 'Home', name='home')
    router.add('/users', lambda: 'List', methods=['GET'], name='users')
    router.add('/users', lambda: 'Create', methods=['POST'])
    router.add('/users/{id}', lambda **kw: f"User {kw['id']}", name='user')
    
    print(router.url('home'))           # /
    print(router.url('user', id=123))  # /users/123
    
    handler, params = router.match('/users/456', 'GET')
    print(handler(**params))            # User 456
    ```

</details>

---

**Score your quiz:**
- 14-16 correct: 🌟 Routing master! You can build complex URL systems!
- 11-13 correct: 👍 Solid understanding! Practice with more complex routes.
- 8-10 correct: 📚 Good start! Review dynamic parameters and method routing.
- Below 8: 🎯 Focus on the basics of path matching and route order.
