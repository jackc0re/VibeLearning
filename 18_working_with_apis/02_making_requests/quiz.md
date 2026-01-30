# 📡 Making Requests - Quiz

Test your understanding of making HTTP requests with urllib!

---

## Questions

### Question 1
Which function is used to make a simple GET request in urllib?

A) `requests.get()`  
B) `urlopen()`  
C) `http.get()`  
D) `open_url()`  

---

### Question 2
How do you add custom headers to a request?

A) Pass them as a dictionary to `urlopen()`  
B) Create a `Request` object with headers  
C) Headers cannot be customized  
D) Use `set_header()` function  

---

### Question 3
What does `data` parameter do in a Request?

A) Adds query parameters  
B) Sets the body of POST requests  
C) Specifies response format  
D) Sets cookies  

---

### Question 4
How do you send JSON data in a POST request?

A) Pass a dict directly to `data`  
B) Use `json.dumps()` and encode to bytes  
C) Use `json.encode()`  
D) JSON cannot be sent with urllib  

---

### Question 5
What encoding should you use for URL parameters with special characters?

A) `base64`  
B) `utf-16`  
C) `urlencode()`  
D) `html.escape()`  

---

### Question 6
What is the purpose of the `User-Agent` header?

A) To authenticate with the server  
C) To identify the client making the request  
B) To compress the response  
D) To set cookies  

---

### Question 7
What does `response.read()` return?

A) A string  
B) Bytes that need decoding  
C) A dictionary  
D) A file object  

---

### Question 8
Which header tells the server you're sending JSON data?

A) `Accept: application/json`  
B) `Content-Type: application/json`  
C) `Type: json`  
D) `Format: json`  

---

### Question 9
Why should you use `with` statement with `urlopen()`?

A) It's required by Python  
B) It automatically closes the connection  
C) It makes requests faster  
D) It adds security  

---

### Question 10
What is the default HTTP method when creating a Request without specifying?

A) POST  
B) PUT  
C) GET  
D) HEAD  

---

## Answers

<details>
<summary>Click to reveal answers</summary>

| Question | Answer | Explanation |
|----------|--------|-------------|
| 1 | B | `urlopen()` is the main function for making requests |
| 2 | B | Create a `Request` object to add custom headers |
| 3 | B | The `data` parameter sets the request body |
| 4 | B | Use `json.dumps()` to convert dict to string, then `.encode()` |
| 5 | C | `urlencode()` properly encodes URL parameters |
| 6 | C | User-Agent identifies the client (browser, app, etc.) |
| 7 | B | `read()` returns bytes; decode to get a string |
| 8 | B | Content-Type tells server what format you're sending |
| 9 | B | `with` ensures the connection is properly closed |
| 10 | C | Default method is GET unless data is provided |

</details>

---

## Scoring

- **9-10 correct**: Request master! 🏆
- **7-8 correct**: Well connected! 👍
- **5-6 correct**: Good foundation, keep practicing 📚
- **Below 5**: Review the examples and try again 💪
