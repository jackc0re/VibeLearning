# 🎯 Forms Handling - Quiz

Test your knowledge of HTML form processing with Python.

---

## Multiple Choice Questions

### Question 1
What HTTP method should be used for forms containing passwords?

- A) GET
- B) POST
- C) PUT
- D) DELETE

### Question 2
Where does GET form data appear?

- A) In the request body
- B) In the URL query string
- C) In HTTP headers
- D) In cookies

### Question 3
What is the default content type for form submissions?

- A) `application/json`
- B) `text/html`
- C) `application/x-www-form-urlencoded`
- D) `multipart/form-data`

### Question 4
How do you read POST form data in Python's http.server?

- A) `self.read()`
- B) `self.rfile.read(content_length)`
- C) `self.request.read()`
- D) `self.body.read()`

### Question 5
What function parses URL-encoded form data?

- A) `urllib.parse.parse_url()`
- B) `urllib.parse.parse_qs()`
- C) `urllib.parse.decode_form()`
- D) `html.parser.parse()`

### Question 6
Why is client-side validation not enough?

- A) It's too slow
- B) It can be bypassed
- C) It's not supported in all browsers
- D) It uses too much memory

### Question 7
What does `html.escape()` prevent?

- A) Form submission errors
- B) XSS attacks
- C) Database corruption
- D) Session hijacking

### Question 8
Which header tells you how much POST data to read?

- A) `Content-Type`
- B) `Content-Length`
- C) `Content-Encoding`
- D) `Accept-Length`

### Question 9
What happens to spaces in URL-encoded data?

- A) They are removed
- B) They become `+` or `%20`
- C) They stay as spaces
- D) They become underscores

### Question 10
What is CSRF?

- A) A form validation library
- B) An attack where unauthorized commands are submitted
- C) A type of form encoding
- D) A CSS framework

---

## Short Answer Questions

### Question 11
Explain the difference between GET and POST form methods. When would you use each?

### Question 12
Why is it important to validate form data on the server even if you validated it in the browser?

### Question 13
Describe how you would implement rate limiting for a contact form to prevent spam.

### Question 14
What is the PRG (Post/Redirect/Get) pattern and why is it important?

### Question 15
How would you handle file uploads securely in a Python web application?

---

## Code Challenge

### Question 16
Create a complete login form handler that:
1. Displays a login form (username/password)
2. Validates that both fields are provided
3. Checks credentials against a hardcoded dictionary
4. Sets a session cookie on successful login
5. Redirects to a dashboard page
6. Shows appropriate error messages

Include CSRF protection and password hashing (use hashlib).

---

## Answers

<details>
<summary>Click to expand answers</summary>

### Multiple Choice

1. **B** - POST
2. **B** - In the URL query string
3. **C** - `application/x-www-form-urlencoded`
4. **B** - `self.rfile.read(content_length)`
5. **B** - `urllib.parse.parse_qs()`
6. **B** - It can be bypassed
7. **B** - XSS attacks
8. **B** - `Content-Length`
9. **B** - They become `+` or `%20`
10. **B** - An attack where unauthorized commands are submitted

### Short Answer

11. **GET** sends data in the URL (visible, limited size, bookmarkable) and is good for search/filtering. **POST** sends data in the request body (hidden, larger capacity) and is required for sensitive data, file uploads, and actions that change server state.

12. Client-side validation can be bypassed by disabling JavaScript, modifying the HTML, or making direct HTTP requests. Server-side validation is the only way to ensure data integrity and security.

13. Track submissions by IP or email with timestamps. Store recent submissions in memory or database. Before processing, check if the user has exceeded the limit (e.g., 3 submissions per hour). If exceeded, reject with a message to try again later.

14. **PRG Pattern**: After processing a POST request, redirect to a GET request (e.g., results page). This prevents duplicate form submissions when users refresh the page and separates form processing from result display.

15. Validate file type (check extension AND content), limit file size, use randomized filenames, store outside web root, scan for malware if possible, and never trust the original filename.

### Code Challenge

16. ```python
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from urllib.parse import parse_qs
    from html import escape
    import hashlib
    import secrets
    import time
    
    # Simulated user database with hashed passwords
    USERS = {
        'alice': hashlib.sha256('password123'.encode()).hexdigest(),
        'bob': hashlib.sha256('secret456'.encode()).hexdigest()
    }
    
    # Session storage
    sessions = {}
    
    class LoginHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.serve_login()
            elif self.path == '/dashboard':
                self.serve_dashboard()
            else:
                self.send_error(404)
        
        def do_POST(self):
            if self.path == '/login':
                self.process_login()
            else:
                self.send_error(404)
        
        def serve_login(self, error=None):
            csrf_token = secrets.token_urlsafe(32)
            # Store CSRF token in session (simplified)
            
            error_html = f'<p style="color: red;">{escape(error)}</p>' if error else ''
            
            html = f"""<!DOCTYPE html>
            <html>
            <body style="max-width: 400px; margin: 50px auto; font-family: Arial;">
                <h1>Login</h1>
                {error_html}
                <form method="POST" action="/login">
                    <input type="hidden" name="csrf_token" value="{csrf_token}">
                    <div><label>Username: <input type="text" name="username" required></label></div>
                    <div><label>Password: <input type="password" name="password" required></label></div>
                    <button type="submit">Login</button>
                </form>
            </body>
            </html>"""
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode())
        
        def process_login(self):
            # Read form data
            length = int(self.headers.get('Content-Length', 0))
            data = parse_qs(self.rfile.read(length).decode())
            form = {k: v[0] for k, v in data.items()}
            
            username = form.get('username', '').strip()
            password = form.get('password', '')
            
            # Validate
            if not username or not password:
                return self.serve_login("Username and password required")
            
            # Verify credentials
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            if USERS.get(username) != password_hash:
                return self.serve_login("Invalid credentials")
            
            # Create session
            session_id = secrets.token_urlsafe(32)
            sessions[session_id] = {'username': username, 'created': time.time()}
            
            # Redirect to dashboard with session cookie
            self.send_response(302)
            self.send_header('Location', '/dashboard')
            self.send_header('Set-Cookie', f'session={session_id}; HttpOnly; Path=/')
            self.end_headers()
        
        def serve_dashboard(self):
            # Check session cookie (simplified)
            html = """<!DOCTYPE html>
            <html>
            <body style="max-width: 800px; margin: 50px auto; font-family: Arial;">
                <h1>Dashboard</h1>
                <p>Welcome! You are logged in.</p>
                <a href="/">Logout</a>
            </body>
            </html>"""
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode())
    
    if __name__ == '__main__':
        server = HTTPServer(('localhost', 8000), LoginHandler)
        print('Login server at http://localhost:8000')
        server.serve_forever()
    ```

</details>

---

**Score your quiz:**
- 14-16 correct: 🌟 Form master! You can build secure, production-ready forms!
- 11-13 correct: 👍 Excellent! Practice with more complex form scenarios.
- 8-10 correct: 📚 Good foundation! Review validation and security.
- Below 8: 🎯 Study the basics of form parsing and GET vs POST.

---

**Congratulations on completing Module 20: Web Basics!** 🎉

You now have the skills to:
- Build web servers with Python
- Route URLs to handlers
- Generate dynamic HTML
- Process form submissions
- Build complete web applications
