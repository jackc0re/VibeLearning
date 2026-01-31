# 🌐 Module 18: Working with APIs

> **Estimated Time:** 6-8 hours  
> **Prerequisites:** Modules 01 (Foundations), 08 (Error Handling), 10 (File I/O)

---

## What You'll Learn

This module teaches you how to interact with web APIs using only Python's standard library. You'll learn how to make HTTP requests, handle responses, parse JSON data, and even build your own simple API server—all without external dependencies!

---

## Why APIs Matter

APIs (Application Programming Interfaces) are the glue of the modern internet. They let different applications talk to each other, share data, and work together. Every time you:

- Check the weather on your phone
- Log in with "Sign in with Google"
- See a map embedded in a website
- Pay with a credit card online

You're using APIs behind the scenes.

---

## Module Structure

| Topic | Description |
|-------|-------------|
| [01: HTTP Fundamentals](./01_http_fundamentals/) | Methods, status codes, headers, URLs |
| [02: Making Requests](./02_making_requests/) | GET/POST with `urllib` |
| [03: Parsing Responses](./03_parsing_responses/) | JSON handling, error management |
| [04: Building Simple API](./04_building_simple_api/) | REST API with `http.server` |
| [05: API Best Practices](./05_api_best_practices/) | Rate limiting, retries, authentication |

---

## Learning Path

```
Start Here
    ↓
01_http_fundamentals  →  Learn how the web works
    ↓
02_making_requests    →  Make your first API call
    ↓
03_parsing_responses  →  Handle the data you get back
    ↓
04_building_simple_api →  Build your own API server
    ↓
05_api_best_practices  →  Production-ready techniques
```

---

## Real-World Analogy

Think of an API like a **restaurant menu**:

- **The menu (API Documentation)**: Lists what's available and how to ask for it
- **Your order (Request)**: You specify what you want using the menu's format
- **The kitchen (Server)**: Processes your request behind the scenes
- **Your meal (Response)**: You get back what you asked for (or an explanation if they can't make it)

HTTP is the "language" you use to place your order, and the waiter is your internet connection carrying messages back and forth.

---

## What Makes This Module Special

Most API tutorials require installing `requests` library. This module uses **only** Python's built-in `urllib` to show you:

1. How HTTP actually works under the hood
2. That you can make API calls without any dependencies
3. What libraries like `requests` do for you automatically

Once you understand `urllib`, using `requests` will feel like a luxury upgrade!

---

## Projects You Can Build After This

- Weather dashboard
- Currency converter
- GitHub repository viewer
- News headline fetcher
- Custom webhook server

---

## Quick Start

```python
# A simple GET request with urllib
from urllib.request import urlopen
import json

# Fetch data from a public API
url = "https://api.github.com/events"
with urlopen(url) as response:
    data = json.loads(response.read())
    print(f"Got {len(data)} events!")
```

---

## ✅ Before You Continue

Before starting this module, make sure you:

1. Understand basic Python (variables, functions, loops)
2. Can handle exceptions with try/except
3. Know how to work with dictionaries and JSON
4. Are comfortable with string formatting

---

**Ready to connect your Python programs to the world? Let's dive in! 🚀**
