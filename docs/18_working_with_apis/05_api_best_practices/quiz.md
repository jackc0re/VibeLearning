# ⭐ API Best Practices - Quiz

Test your understanding of production-ready API techniques!

---

## Questions

### Question 1
What is "exponential backoff"?

A) Reducing API calls over time  
B) Increasing wait time between retries exponentially  
C) A type of authentication  
D) A caching strategy  

---

### Question 2
Which HTTP status codes are typically safe to retry?

A) 404, 401  
B) 200, 201  
C) 500, 502, 503, 429  
D) 301, 302  

---

### Question 3
What does the Retry-After header indicate?

A) The time until the server restarts  
B) How many requests you have left  
C) How long to wait before retrying  
D) The API version  

---

### Question 4
Why add "jitter" to retry delays?

A) To make debugging harder  
B) To prevent synchronized retries from many clients  
C) To increase security  
D) To reduce memory usage  

---

### Question 5
What is the purpose of a circuit breaker?

A) To encrypt API traffic  
B) To fail fast when a service is repeatedly failing  
C) To compress responses  
D) To cache API responses  

---

### Question 6
What should you include in a User-Agent header?

A) Your password  
B) App name, version, and contact info  
C) Server IP address  
D) Credit card number  

---

### Question 7
Which header is used for conditional requests with caching?

A) Cache-Control  
B) If-None-Match  
C) ETag  
D) Last-Modified  

---

### Question 8
What status code means "Not Modified" (for conditional requests)?

A) 200  
B) 304  
C) 404  
D) 204  

---

### Question 9
Why set timeouts on API requests?

A) To make requests faster  
B) To prevent indefinite hanging  
C) To reduce server load  
D) To enable caching  

---

### Question 10
What is rate limiting designed to prevent?

A) Slow internet connections  
B) API abuse and server overload  
C) JSON parsing errors  
D) Authentication failures  

---

## Answers

<details>
<summary>Click to reveal answers</summary>

| Question | Answer | Explanation |
|----------|--------|-------------|
| 1 | B | Exponential backoff increases wait time (1s, 2s, 4s, etc.) |
| 2 | C | Server errors (5xx) and rate limit (429) are retryable |
| 3 | C | Retry-After tells clients how long to wait |
| 4 | B | Jitter prevents "thundering herd" of synchronized retries |
| 5 | B | Circuit breakers fail fast when services are down |
| 6 | B | User-Agent should identify your app with contact info |
| 7 | B | If-None-Match sends ETag to check if content changed |
| 8 | B | 304 Not Modified means cached version is still valid |
| 9 | B | Timeouts prevent requests from hanging forever |
| 10 | B | Rate limiting prevents abuse and protects servers |

</details>

---

## Scoring

- **9-10 correct**: Production-ready expert! 🏆
- **7-8 correct**: Best practices pro! 👍
- **5-6 correct**: Good understanding, keep refining 📚
- **Below 5**: Review the examples and README 💪

---

## 🎉 Module Complete!

You've learned:
- HTTP fundamentals
- Making requests with urllib
- Parsing JSON responses
- Building simple APIs
- Production best practices

**Next:** Try building a project that uses a real API, or explore the `requests` library!
