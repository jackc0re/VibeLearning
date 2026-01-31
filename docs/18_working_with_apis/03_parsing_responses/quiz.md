# 📄 Parsing Responses - Quiz

Test your understanding of handling API responses!

---

## Questions

### Question 1
What function converts a JSON string to a Python object?

A) `json.dumps()`  
B) `json.loads()`  
C) `json.parse()`  
D) `json.decode()`  

---

### Question 2
What exception is raised when a server returns a 404 status?

A) `URLError`  
B) `HTTPError`  
C) `ConnectionError`  
D) `JSONDecodeError`  

---

### Question 3
How do you convert response bytes to a string?

A) `str(response)`  
B) `response.toString()`  
C) `response.decode("utf-8")`  
D) `response.text()`  

---

### Question 4
What does `response.getheader("Content-Type")` return?

A) The request method  
B) The format of the response body  
C) The server software  
D) The status code  

---

### Question 5
When should you use try/except around `json.loads()`?

A) Always - the API might return invalid JSON  
B) Never - JSON is always valid  
C) Only for POST requests  
D) Only when the status code is 200  

---

### Question 6
What header typically contains rate limit information?

A) `Content-Rate`  
B) `X-RateLimit-Remaining`  
C) `Rate-Limit`  
D) `API-Limit`  

---

### Question 7
How do you pretty-print JSON with indentation?

A) `json.dumps(data, pretty=True)`  
B) `json.dumps(data, indent=2)`  
C) `json.pretty(data)`  
D) `json.format(data)`  

---

### Question 8
What does a `URLError` typically indicate?

A) The server returned 500  
B) Network connectivity issues  
C) The JSON was invalid  
D) The URL was too long  

---

### Question 9
Why is pagination important when fetching API data?

A) It makes requests faster  
B) APIs often limit results per request  
C) It's required by HTTP specification  
D) It reduces server load  

---

### Question 10
What should you do when `X-RateLimit-Remaining` is low?

A) Send more requests quickly  
B) Slow down or wait before making more requests  
C) Change the User-Agent  
D) Use a different HTTP method  

---

## Answers

<details>
<summary>Click to reveal answers</summary>

| Question | Answer | Explanation |
|----------|--------|-------------|
| 1 | B | `json.loads()` parses JSON string to Python object |
| 2 | B | `HTTPError` is raised for HTTP error status codes |
| 3 | C | `.decode("utf-8")` converts bytes to string |
| 4 | B | Content-Type indicates the format of the response |
| 5 | A | Always use try/except as APIs can return unexpected data |
| 6 | B | X-RateLimit-Remaining shows requests left |
| 7 | B | `json.dumps(data, indent=2)` for pretty printing |
| 8 | B | URLError indicates network/connection issues |
| 9 | B | Pagination lets you get all data when APIs limit per-request results |
| 10 | B | Slow down when rate limit remaining is low |

</details>

---

## Scoring

- **9-10 correct**: Response master! 🏆
- **7-8 correct**: Great parser! 👍
- **5-6 correct**: Good progress, review the examples 📚
- **Below 5**: Re-read the README and try again 💪
