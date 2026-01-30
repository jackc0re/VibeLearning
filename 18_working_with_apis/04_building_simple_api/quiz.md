# 🏗️ Building a Simple API - Quiz

Test your understanding of building APIs with http.server!

---

## Questions

### Question 1
What class do you extend to create a custom HTTP handler?

A) `HTTPServer`  
B) `BaseHTTPRequestHandler`  
C) `HTTPHandler`  
D) `RequestHandler`  

---

### Question 2
Which method handles GET requests?

A) `handle_get()`  
B) `on_GET()`  
C) `do_GET()`  
D) `process_get()`  

---

### Question 3
What method sends the HTTP status code?

A) `set_status()`  
B) `send_status()`  
C) `send_response()`  
D) `status()`  

---

### Question 4
What must you call before writing the response body?

A) `send_body()`  
B) `end_headers()`  
C) `finish_headers()`  
D) `close_headers()`  

---

### Question 5
How do you write the response body?

A) `self.write()`  
B) `self.response.write()`  
C) `self.wfile.write()`  
D) `self.send_body()`  

---

### Question 6
What attribute contains the request path?

A) `self.url`  
B) `self.path`  
C) `self.route`  
D) `self.endpoint`  

---

### Question 7
How do you read the POST request body?

A) `self.body.read()`  
B) `self.read()`  
C) `self.rfile.read(content_length)`  
D) `self.get_body()`  

---

### Question 8
Where do you get the Content-Length header value?

A) `self.headers.content_length`  
B) `self.headers.get("Content-Length")`  
C) `self.get_header("Content-Length")`  
D) `self.content_length`  

---

### Question 9
What port does this server use: `HTTPServer(("localhost", 8080), Handler)`?

A) 80  
B) 443  
C) 8000  
D) 8080  

---

### Question 10
Why is http.server NOT recommended for production?

A) It doesn't support JSON  
B) It's single-threaded and lacks security features  
C) It can't handle GET requests  
D) It requires Python Pro  

---

## Answers

<details>
<summary>Click to reveal answers</summary>

| Question | Answer | Explanation |
|----------|--------|-------------|
| 1 | B | Extend `BaseHTTPRequestHandler` |
| 2 | C | `do_GET()` handles GET requests |
| 3 | C | `send_response(code)` sends status |
| 4 | B | `end_headers()` must be called before body |
| 5 | C | `self.wfile.write(bytes)` writes body |
| 6 | B | `self.path` contains the URL path |
| 7 | C | Read with `self.rfile.read(content_length)` |
| 8 | B | Use `self.headers.get("Content-Length")` |
| 9 | D | Port is the second element: 8080 |
| 10 | B | http.server is single-threaded, not production-ready |

</details>

---

## Scoring

- **9-10 correct**: API architect! 🏆
- **7-8 correct**: Server savvy! 👍
- **5-6 correct**: Good foundation, keep building 📚
- **Below 5**: Review the examples and code along 💪
