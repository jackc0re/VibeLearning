# 🏗️ System Design Basics

> What "design a URL shortener" interviews actually ask at junior level -
> explained with the tools you already have from this site.

---

## What These Interviews Actually Ask

Nobody expects a junior candidate to sketch Netflix's architecture. A first
design conversation is usually small and familiar:

1. **A small product**: URL shortener, pastebin, rate limiter, to-do API.
2. **Clarifying questions matter more than the answer**: How many users? How much
   data per item? Read-heavy or write-heavy? Saying "it depends - let me ask" is
   the *good* move.
3. **A sketch of the data flow**: client → server → database, plus the parts that
   break first as traffic grows.
4. **Trade-offs said out loud**: "A cache makes reads faster but can serve stale
   data - for write-once URLs that is fine."

The vocabulary below is most of what junior rounds probe. The rest of this page
builds it around an app you have already written.

## 📖 The Core Vocabulary

| Term | In one sentence |
|------|-----------------|
| **Load balancer** | Sits in front of identical servers and hands each request to one of them, so no single machine melts and dead ones get skipped. |
| **Cache** | Keeps hot data in fast memory near the request; **cache invalidation** is deciding when the stored copy is stale and must be refreshed - the famously hard part. |
| **Database index** | A sorted side-structure (like a book's index) that turns "scan every row" into "jump straight to the match". |
| **Replication vs sharding** | Replication = copies of the *same* data on several machines (speed and safety); sharding = *different* slices of data on different machines (capacity). |
| **CAP (one sentence)** | If the network splits, a system must pick availability (always answer) or consistency (always answer correctly) - it cannot guarantee both. |
| **Horizontal vs vertical scaling** | Vertical = buy a bigger machine (simple, has a ceiling); horizontal = buy more machines (near-unlimited, but needs a load balancer and shared state). |
| **Stateless service** | A server keeping no session data of its own, so *any* server can handle *any* request - the property that makes load balancing safe. |

---

## 🔧 Worked Walkthrough: Scale Your URL Shortener

You built this app in [Project 8: URL Shortener](../../Projects/08_url_shortener/README.md):
a dictionary in memory plus a JSON file, in one Python process. Let's grow it,
one bottleneck at a time.

### Step 1: Persistence in SQLite

The JSON file is rewritten in full on every save - two saves at once and the last
writer wins, losing data. Swap it for a real database, taught in
[SQLite Basics](../../19_data_processing/01_sqlite_basics/README.md):

```sql
CREATE TABLE urls (
    short_code   TEXT PRIMARY KEY,
    original_url TEXT NOT NULL,
    created_at   TEXT NOT NULL,
    clicks       INTEGER NOT NULL DEFAULT 0
);
```

Now writes touch one row, readers don't trip over writers, and you can ask real
questions ("top 10 most clicked") instead of loading everything into a dict.

### Step 2: An Index on the Short Code

Resolution asks "find the row where `short_code = ?`". Without an index SQLite
scans every row; with one it jumps straight there. `PRIMARY KEY` already indexes
`short_code` - but the project also checks "does this long URL already exist?" on
every shorten, so index that column too:

```sql
CREATE INDEX idx_urls_original ON urls (original_url);
```

Rule of thumb: one index per lookup pattern. Indexes make reads fast and writes
slightly slower.

### Step 3: Cache the Hot Codes

Most traffic hits a few famous links, so put a dictionary in front of the
database:

```python
import sqlite3

cache = {}  # short_code -> original_url
MAX_CACHE = 10_000


def resolve(code):
    """Return the original URL for a short code, or None."""
    if code in cache:
        return cache[code]                    # cache hit: database untouched
    conn = sqlite3.connect("shortener.db")    # cache miss: ask the database
    try:
        row = conn.execute(
            "SELECT original_url FROM urls WHERE short_code = ?", (code,)
        ).fetchone()
    finally:
        conn.close()
    if row is not None:
        if len(cache) >= MAX_CACHE:
            cache.pop(next(iter(cache)))      # drop the oldest entry
        cache[code] = row[0]
    return row[0] if row else None
```

Notice why caching is *easy* here: a short code's target never changes
(write-once data), so a cached copy can never go stale. Cache invalidation is
hard exactly when data *can* change - then you must decide when to refresh, and
every answer trades freshness against speed.

### Step 4: A Rate Limiting Sketch

Public APIs get abused, so cap each client at N requests per window. The simplest
correct design is a fixed-window counter:

```python
import time

WINDOW_SECONDS = 60
LIMIT = 100
windows = {}  # client_id -> (window_start, count)


def allow(client_id):
    """Return True if this client may make another request right now."""
    now = time.time()
    start, count = windows.get(client_id, (now, 0))
    if now - start >= WINDOW_SECONDS:  # window expired: start a new one
        start, count = now, 0
    count += 1
    windows[client_id] = (start, count)
    return count <= LIMIT
```

Real limiters smooth this out (try the exercise below), but the shape - check,
count, decide - stays the same.

### Step 5: What Changes at "Many Machines"

One process with one SQLite file saturates eventually. Now the vocabulary earns
its keep:

- **Load balancer** spreads requests across identical copies of the app. This
  only works because the app is **stateless** - every mapping lives in the
  database, so any server can answer any request.
- **Shared database**: four processes cannot safely share one SQLite file over a
  network drive. You reach for a database server built for many clients - beyond
  this site's stdlib scope, but your schema and indexes carry over unchanged.
- **Shared cache**: each server's private dict now knows only part of the hot
  data. Real systems add a dedicated cache server; the logic (hit → serve,
  miss → database, store) is exactly what you wrote in Step 3.
- **Replication** of the database buys read speed and a backup; **sharding** by
  short-code hash is the escape hatch when one machine cannot hold all rows.

If you can narrate those four bullets for any small product, you can pass a
junior design round.

---

## ✏️ Two Mini-Designs to Try Yourself

Design each out loud first - requirements, data flow, first bottleneck. Then
compare with the sketch.

### Mini-Design 1: A Pastebin

Users paste text (up to 100 KB) and get a shareable link. Anyone with the link
reads it; pastes can expire.

<details>
<summary>Click for a sketch</summary>

- **Storage**: `pastes(id TEXT PRIMARY KEY, content TEXT, created_at TEXT,
  expires_at TEXT)` - the id is a random short code, exactly like the URL
  shortener's. You have built this shape before.
- **Read path**: id → cache → database, the same three layers as Step 3.
- **Expiry**: reads treat rows past `expires_at` as missing; a periodic cleanup
  job (`DELETE FROM pastes WHERE expires_at < now`) reclaims space.
- **First bottleneck to name**: large pastes flooding the cache - answer: cache
  only small hot pastes, or skip the cache and lean on the index.

</details>

### Mini-Design 2: A Rate Limiter

Design the limiter itself: who gets rejected, where it lives, what changes with
many servers.

<details>
<summary>Click for a sketch</summary>

- **Placement**: in front of the API - call `allow(client_id)` before doing any
  real work, and reject fast with an error.
- **Algorithms**: fixed window (Step 4) is simplest but lets a client sneak 2×
  the limit across a boundary; a sliding window counts a true trailing 60
  seconds; a token bucket refills at a steady rate and allows short bursts. Name
  all three; implement the fixed window.
- **Many machines**: the per-process dict is now wrong - four servers each allow
  100, so the real limit is 4×. Move the counter to a shared store every server
  increments atomically. The function signature stays; what is behind it changes.

</details>

For a code-first version of this kind of task, see
[Exercises/advanced/01_system_design.py](../../Exercises/advanced/01_system_design.py).

---

## 🙋 An Honest Note About Scope

This site teaches the **Python side** of design: the data structures, the SQLite
schema, the cache function, plus the concurrency ideas in module 12 and the HTTP
basics in module 18. What it deliberately does *not* teach is operating real
infrastructure - database servers, message queues, cloud load balancers - none of
which is standard library Python.

For the books and courses that take you from this page to real design depth, see
[Further Reading](../further_reading.md). And when the interview drifts back to
"how would you implement it?" - that is your home turf: head back to
[algorithm_problems.md](algorithm_problems.md).

Back to the [Interview Prep guide](README.md) or the
[Resources index](../README.md).
