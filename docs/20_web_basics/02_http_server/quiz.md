# 🎯 HTTP Server - Quiz

Test your knowledge of Python's http.server module.

---

## Multiple Choice Questions

### Question 1
What class do you inherit from to create a custom request handler?

- A) `HTTPServer`
- B) `BaseHTTPRequestHandler`
- C) `HTTPRequestHandler`
- D) `SimpleHTTPRequestHandler`

### Question 2
Which method handles GET requests?

- A) `handle_get()`
- B) `on_get()`
- C) `do_GET()`
- D) `process_get()`

### Question 3
What method must you call after sending headers but before writing the response body?

- A) `finish_headers()`
- B) `end_headers()`
- C) `complete_headers()`
- D) `close_headers()`

### Question 4
What type of data must you write to `self.wfile`?

- A) String
- B) Integer
- C) Bytes
- D) JSON

### Question 5
Which status code indicates "Not Found"?

- A) 400
- B) 401
- C) 403
- D) 404

### Question 6
What is the correct content type for JSON responses?

- A) `text/json`
- B) `application/javascript`
- C) `application/json`
- D) `text/javascript`

### Question 7
How do you get the requested URL path in a handler?

- A) `self.url`
- B) `self.path`
- C) `self.request_path`
- D) `self.route`

### Question 8
What method can you override to customize request logging?

- A) `log()`
- B) `log_request()`
- C) `log_message()`
- D) `write_log()`

### Question 9
Which header specifies the type of content being sent?

- A) `Content-Encoding`
- B) `Content-Type`
- C) `Accept-Type`
- D) `Media-Type`

### Question 10
What does `HTTPServer(('localhost', 8000), Handler)` do?

- A) Makes a request to localhost:8000
- B) Creates a server listening on localhost:8000
- C) Connects to an existing server
- D) Tests the handler class

---

## Short Answer Questions

### Question 11
Explain the purpose of `self.send_response(200)` and when you might use different status codes.

### Question 12
What security concern exists when serving files based on URL paths, and how can you prevent it?

### Question 13
How would you parse query parameters from a URL like `/search?q=python&limit=10`?

### Question 14
What's the difference between `send_header()` and `end_headers()`? What happens if you forget to call `end_headers()`?

### Question 15
How can you run a basic static file server without writing any Python code?

---

## Code Challenge

### Question 16
Write a complete HTTP server that:
1. Returns a welcome page at `/`
2. Returns the current time at `/time`
3. Echoes back query parameters at `/echo?name=xxx`
4. Returns 404 for any other path

---

## Answers

<details>
<summary>Click to expand answers</summary>

### Multiple Choice

1. **B** - `BaseHTTPRequestHandler`
2. **C** - `do_GET()`
3. **B** - `end_headers()`
4. **C** - Bytes (use `.encode()` on strings)
5. **D** - 404
6. **C** - `application/json`
7. **B** - `self.path`
8. **C** - `log_message()`
9. **B** - `Content-Type`
10. **B** - Creates a server listening on localhost:8000

### Short Answer

11. `send_response(200)` sets the HTTP status code to 200 (OK). Different codes indicate different outcomes: 2xx = success, 3xx = redirect, 4xx = client error, 5xx = server error.

12. **Directory traversal attack** - users could access files outside the intended directory using `..` in paths. Prevent it by normalizing paths with `os.path.normpath()` and checking for `..` in the path.

13. Use `urllib.parse`:
    ```python
    from urllib.parse import urlparse, parse_qs
    parsed = urlparse(self.path)
    params = parse_qs(parsed.query)
    ```

14. `send_header()` adds a single header, `end_headers()` signals that all headers are sent and the body follows. Forgetting `end_headers()` causes the browser to wait indefinitely for more headers.

15. Use the built-in command:
    ```bash
    python -m http.server 8000
    ```

### Code Challenge

16. ```python
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from urllib.parse import urlparse, parse_qs
    from datetime import datetime
    import json
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = urlparse(self.path)
            path = parsed.path
            
            if path == '/':
                self.send_html('<h1>Welcome!</h1>')
            
            elif path == '/time':
                time_str = datetime.now().isoformat()
                self.send_json({'time': time_str})
            
            elif path == '/echo':
                params = parse_qs(parsed.query)
                echo_data = {k: v[0] if len(v) == 1 else v 
                            for k, v in params.items()}
                self.send_json(echo_data)
            
            else:
                self.send_response(404)
                self.send_html('<h1>404 Not Found</h1>')
        
        def send_html(self, html):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode())
        
        def send_json(self, data):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
    
    if __name__ == '__main__':
        server = HTTPServer(('localhost', 8000), MyHandler)
        print('Server running at http://localhost:8000')
        server.serve_forever()
    ```

</details>

---

**Score your quiz:**
- 14-16 correct: 🌟 Expert! You can build production-ready servers!
- 11-13 correct: 👍 Good understanding! Keep practicing routing and handlers.
- 8-10 correct: 📚 Review the examples and try building more servers.
- Below 8: 🎯 Focus on understanding the basic handler structure first.
