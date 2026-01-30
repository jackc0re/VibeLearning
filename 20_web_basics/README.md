# 🌐 Module 20: Web Basics

> **Estimated Time:** 8-10 hours  
> **Prerequisites:** Modules 01 (Foundations), 10 (File I/O), 18 (Working with APIs)

---

## What You'll Learn

This module teaches you the fundamentals of web development using only Python's standard library. You'll learn how web servers work, how to serve HTML content, handle different URLs, create dynamic templates, and process form submissions—all without external frameworks like Flask or Django!

---

## Why Web Basics Matter

Understanding how web servers work at a fundamental level is essential for any developer. Before using high-level frameworks, knowing:

- How HTTP requests are handled
- How to route URLs to different content
- How to generate dynamic HTML
- How to process form data

This knowledge helps you debug issues, understand framework internals, and build lightweight solutions when you don't need a full framework.

---

## Module Structure

| Topic | Description |
|-------|-------------|
| [01: HTML & CSS Overview](./01_html_css_overview/) | Structure, tags, basic styling |
| [02: HTTP Server](./02_http_server/) | `http.server` module deep dive |
| [03: Simple Routing](./03_simple_routing/) | Simple URL routing without frameworks |
| [04: Templating](./04_templating/) | String templating for HTML generation |
| [05: Forms Handling](./05_forms_handling/) | Handling GET/POST form data |

---

## Learning Path

```
Start Here
    ↓
01_html_css_overview  →  Learn the building blocks of web pages
    ↓
02_http_server        →  Build a basic web server
    ↓
03_simple_routing     →  Handle different URLs
    ↓
04_templating         →  Generate dynamic HTML pages
    ↓
05_forms_handling     →  Accept user input through forms
```

---

## Real-World Analogy

Think of a web application like a **restaurant**:

- **The dining room (Browser)** = Where customers sit and see the menu
- **The menu (HTML/CSS)** = Lists what's available with descriptions and prices
- **The waiter (HTTP)** = Takes orders from customers to the kitchen
- **The kitchen (Web Server)** = Processes orders and prepares meals
- **The recipes (Templates)** = Instructions for creating each dish consistently
- **The order pad (Forms)** = How customers communicate what they want

Python's `http.server` lets you build the entire restaurant with just the standard library!

---

## What Makes This Module Special

Most web tutorials jump straight to Flask or Django. This module uses **only** Python's built-in `http.server` to show you:

1. How web frameworks work under the hood
2. That you can build functional websites without any dependencies
3. The fundamental concepts behind request handling and routing
4. When you actually need a full framework vs. a simple server

Once you understand the basics, using Flask or Django will feel like having a professional kitchen staff instead of cooking alone!

---

## Projects You Can Build After This

- Personal portfolio website
- Simple blog engine
- Contact form with email notifications
- File upload server
- REST API documentation site
- Admin dashboard for data management

---

## Quick Start

```python
# A simple web server with Python
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello, Web!</h1>')

# Start server on port 8000
server = HTTPServer(('localhost', 8000), SimpleHandler)
print('Server running on http://localhost:8000')
server.serve_forever()
```

Save this as `server.py` and run it with `python server.py`. Visit `http://localhost:8000` in your browser!

---

## ✅ Before You Continue

Before starting this module, make sure you:

1. Understand basic Python (variables, functions, classes)
2. Know how to work with strings and file I/O
3. Understand HTTP basics (GET/POST, status codes)
4. Are comfortable with dictionaries and string formatting

---

**Ready to build your own web server? Let's dive in! 🚀**
