# HTTP Cheatsheet

Quick reference for talking to web APIs with Python's standard library
(`urllib`): request anatomy, methods, status codes, and copy-paste snippets.

---

## Request Anatomy

Every HTTP request has the same four parts:

```
POST /api/users HTTP/1.1          <- method, path, HTTP version
Host: api.example.com             <- headers (metadata, one per line)
Content-Type: application/json
Authorization: Bearer xyz123

{"name": "Alice"}                 <- body (optional, used by POST/PUT/PATCH)
```

- **Method** — what you want to do (read, create, update, delete)
- **Path** — which resource, e.g. `/api/users/42`
- **Headers** — metadata: format you're sending/accepting, auth tokens, etc.
- **Body** — the data you're sending (GET requests normally have none)

The server replies with a **status code**, optional headers, and usually a
body (often JSON).

---

## Methods

| Method | Meaning | When to use |
|--------|---------|-------------|
| `GET` | Read | Fetch data. Never changes anything, safe to retry |
| `POST` | Create / submit | Add a new resource, submit a form, log in |
| `PUT` | Replace | Overwrite a resource entirely with your version |
| `PATCH` | Update partially | Change one field of a resource |
| `DELETE` | Remove | Delete a resource |

> Rule of thumb: GET to look, POST to create, PUT/PATCH to change,
> DELETE to remove.

---

## Status Codes

### The Five Families

| Family | Meaning | Vibe |
|--------|---------|------|
| `1xx` | Informational | Rare — the server is still working |
| `2xx` | Success | Everything went fine |
| `3xx` | Redirection | "It's over here instead" |
| `4xx` | Client error | **You** made a mistake — fix the request |
| `5xx` | Server error | **The server** broke — retry later |

### The Codes You'll Actually Meet

| Code | Name | Meaning |
|------|------|---------|
| `200` | OK | Success |
| `201` | Created | Your POST made something new |
| `204` | No Content | Success, empty body (common after DELETE) |
| `301` / `302` | Moved / Found | Redirect: permanent / temporary |
| `400` | Bad Request | Malformed request — check your JSON/params |
| `401` | Unauthorized | Not logged in — missing/invalid credentials |
| `403` | Forbidden | Logged in, but not allowed to do this |
| `404` | Not Found | No such resource (or typo in the URL) |
| `429` | Too Many Requests | Rate limit — slow down, wait and retry |
| `500` | Internal Server Error | The server crashed handling your (valid) request |

> 401 vs 403 in one line: **401 = "who are you?", 403 = "I know who you are —
> the answer is still no."**

---

## GET Request (Copy-Paste)

```python
from urllib.request import urlopen

with urlopen("https://api.github.com/events") as response:
    data = response.read()             # bytes
    text = data.decode("utf-8")        # str
    print(response.status)             # 200
```

With parameters in the URL (a query string):

```python
from urllib.request import urlopen
from urllib.parse import urlencode

params = urlencode({"q": "python", "page": 1})   # q=python&page=1
url = f"https://api.example.com/search?{params}"

with urlopen(url) as response:
    text = response.read().decode("utf-8")
```

## POST Request with JSON (Copy-Paste)

```python
import json
from urllib.request import Request, urlopen

payload = {"name": "Alice", "hobbies": ["coding", "reading"]}

req = Request(
    url="https://httpbin.org/post",
    data=json.dumps(payload).encode("utf-8"),     # JSON as bytes
    headers={
        "Content-Type": "application/json",
        "User-Agent": "MyApp/1.0",
    },
    method="POST",                # Including `data` implies POST anyway
)

with urlopen(req) as response:
    result = json.loads(response.read().decode("utf-8"))
    print(result["json"])         # The server echoes your payload back
```

---

## Headers: User-Agent & Auth

```python
req = Request(
    url="https://api.example.com/data",
    headers={
        # Some APIs (GitHub included) reject requests without a User-Agent
        "User-Agent": "MyApp/1.0 (my-project)",
        # Tell the server which format you can accept
        "Accept": "application/json",
        # Auth lives in headers: a token your API key page gave you
        "Authorization": "Bearer YOUR_TOKEN_HERE",
    },
)
```

- **Never hardcode real tokens in your code** — keep them in environment
  variables and read them with `os.environ["API_TOKEN"]`.
- Header names are case-insensitive; values are not.

---

## Handling JSON Responses (and Errors)

`urlopen` raises `HTTPError` for any 4xx/5xx — treat it as part of the flow:

```python
import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

url = "https://api.github.com/users/python"

try:
    with urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
    print(data["name"])            # Dig into the parsed dict/list
except HTTPError as e:
    print(f"Server said {e.code}: {e.reason}")   # 404, 429, 500, ...
except URLError as e:
    print(f"Network problem: {e.reason}")        # No connection, bad domain
except json.JSONDecodeError:
    print("Response was not JSON")
```

---

## Quick Reference

| I want to... | Do this |
|--------------|---------|
| Fetch a URL | `urlopen(url)` in a `with` block |
| Send JSON | `Request(url, data=json.dumps(obj).encode("utf-8"), headers={"Content-Type": "application/json"})` |
| Add a query string | `urlencode({"q": "python"})` |
| Set headers | `Request(url, headers={...})` |
| Authenticate | `"Authorization": "Bearer <token>"` header |
| Read the status | `response.status` |
| Parse the body | `json.loads(response.read().decode("utf-8"))` |
| Catch server errors | `except HTTPError as e:` (check `e.code`) |
| Catch network errors | `except URLError as e:` (check `e.reason`) |

---

**Learn more:** [Working with APIs module](../../18_working_with_apis/README.md) ·
[HTTP fundamentals](../../18_working_with_apis/01_http_fundamentals/README.md) ·
[Making requests](../../18_working_with_apis/02_making_requests/README.md) ·
[Parsing responses](../../18_working_with_apis/03_parsing_responses/README.md)

**Back to [Resources](../README.md)**
