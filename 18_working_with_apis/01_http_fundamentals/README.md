# 🌐 HTTP Fundamentals

> Understanding how the web communicates

---

## What is HTTP?

**HTTP** (HyperText Transfer Protocol) is the foundation of data communication on the World Wide Web. It's a **request-response** protocol where:

1. A **client** (like your browser or Python script) sends a request
2. A **server** receives the request, processes it
3. The server sends back a **response**
4. The client receives and interprets the response

Think of it like sending a letter: you write your request (the letter), put it in an envelope (HTTP headers), add the address (URL), and wait for a reply.

---

## URLs: Web Addresses

A **URL** (Uniform Resource Locator) tells your browser where to find something on the web.

```
https://api.example.com:8080/users?id=123#profile
\___/   \_____________/ \__/ \___/ \_____/ \_____/
  |           |          |     |      |       |
Scheme     Host        Port   Path  Query  Fragment
```

| Component | Description | Example |
|-----------|-------------|---------|
| **Scheme** | Protocol to use | `https`, `http`, `ftp` |
| **Host** | Server address | `api.example.com` |
| **Port** | Server entry point (optional) | `8080` (https default: 443, http default: 80) |
| **Path** | Resource location on server | `/users`, `/api/v1/posts` |
| **Query** | Extra parameters (after `?`) | `?id=123&sort=date` |
| **Fragment** | Section within page (after `#`) | `#profile` |

---

## HTTP Methods (Verbs)

Methods tell the server what action you want to perform:

| Method | Action | Analogy | Safe? | Idempotent? |
|--------|--------|---------|-------|-------------|
| **GET** | Retrieve data | "Show me the menu" | ✅ Yes | ✅ Yes |
| **POST** | Create new data | "I'd like to order" | ❌ No | ❌ No |
| **PUT** | Update/replace data | "Change my order" | ❌ No | ✅ Yes |
| **PATCH** | Partial update | "Add fries to my order" | ❌ No | ❌ No |
| **DELETE** | Remove data | "Cancel my order" | ❌ No | ✅ Yes |
| **HEAD** | Get headers only | "What time do you close?" | ✅ Yes | ✅ Yes |
| **OPTIONS** | Get supported methods | "What do you serve?" | ✅ Yes | ✅ Yes |

> **Safe** = Doesn't change server data  
> **Idempotent** = Multiple identical requests have the same effect as one

---

## HTTP Status Codes

Status codes tell you what happened with your request:

### 2xx - Success ✅

| Code | Meaning | When You See It |
|------|---------|-----------------|
| 200 | OK | Request succeeded |
| 201 | Created | New resource was created (usually POST) |
| 204 | No Content | Success, but nothing to return (usually DELETE) |

### 3xx - Redirection 🔄

| Code | Meaning | When You See It |
|------|---------|-----------------|
| 301 | Moved Permanently | Resource has a new permanent URL |
| 302 | Found | Temporary redirect |
| 304 | Not Modified | Cache is still valid, use cached version |

### 4xx - Client Error ❌

| Code | Meaning | When You See It |
|------|---------|-----------------|
| 400 | Bad Request | Your request was malformed |
| 401 | Unauthorized | You need to log in |
| 403 | Forbidden | You're logged in but can't access this |
| 404 | Not Found | Resource doesn't exist |
| 405 | Method Not Allowed | Wrong HTTP method for this URL |
| 429 | Too Many Requests | You're being rate limited |

### 5xx - Server Error 🔥

| Code | Meaning | When You See It |
|------|---------|-----------------|
| 500 | Internal Server Error | Server crashed processing your request |
| 502 | Bad Gateway | Upstream server gave bad response |
| 503 | Service Unavailable | Server is down or overloaded |
| 504 | Gateway Timeout | Upstream server didn't respond in time |

---

## HTTP Headers

Headers are metadata sent with requests and responses:

### Common Request Headers

| Header | Purpose | Example |
|--------|---------|---------|
| `User-Agent` | Identifies the client | `Python-urllib/3.9` |
| `Accept` | What content types you want | `application/json` |
| `Content-Type` | Type of data you're sending | `application/json` |
| `Authorization` | Authentication credentials | `Bearer token123` |
| `Host` | Server domain name | `api.example.com` |

### Common Response Headers

| Header | Purpose | Example |
|--------|---------|---------|
| `Content-Type` | Type of data returned | `application/json; charset=utf-8` |
| `Content-Length` | Size of response body in bytes | `1024` |
| `Date` | When response was sent | `Wed, 21 Oct 2025 07:28:00 GMT` |
| `Server` | Server software | `nginx/1.18.0` |
| `Cache-Control` | Caching instructions | `max-age=3600` |
| `RateLimit-Remaining` | API calls left | `4999` |

---

## Request/Response Flow

```
┌─────────────┐                    ┌─────────────┐
│   CLIENT    │                    │   SERVER    │
│  (Python)   │  ────Request────>  │  (API)      │
│             │  GET /users HTTP/1.1              │
│             │  Host: api.example.com            │
│             │  Accept: application/json         │
└─────────────┘                    └─────────────┘
       │                                   │
       │ <────────Response──────────────   │
       │    HTTP/1.1 200 OK                │
       │    Content-Type: application/json │
       │                                   │
       │    {"users": [...]}               │
       v                                   v
┌─────────────┐                    ┌─────────────┐
│  Process    │                    │  Done!      │
│  the data   │                    │             │
└─────────────┘                    └─────────────┘
```

---

## Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|---------|---------------|------------------|
| Using GET to delete data | GET should be safe and idempotent | Use DELETE method |
| Ignoring status codes | 404 doesn't mean success! | Always check `response.status` |
| Hardcoding full URLs | Makes code hard to maintain | Use a base URL constant |
| Not encoding URL parameters | Special characters break URLs | Use `urllib.parse.quote()` |

---

## Quick Reference

```python
# Status code categories
def get_status_category(code):
    if 200 <= code < 300:
        return "Success"
    elif 300 <= code < 400:
        return "Redirect"
    elif 400 <= code < 500:
        return "Client Error"
    elif 500 <= code < 600:
        return "Server Error"
    return "Unknown"

# Common status codes to remember
SUCCESS = {200, 201, 204}
CLIENT_ERRORS = {400, 401, 403, 404, 405, 422, 429}
SERVER_ERRORS = {500, 502, 503, 504}
```

---

## Next Steps

Now that you understand HTTP basics, let's make some real requests!

→ Continue to [02: Making Requests](../02_making_requests/)
