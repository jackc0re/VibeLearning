# 🌐 Async Programming (`asyncio`)

`asyncio` provides concurrency via **cooperative multitasking**:

- code runs in a single OS thread
- tasks voluntarily yield control at `await`
- great for "lots of I/O" workloads (many sockets, many requests)

Async is not automatically faster—it’s a tool for scaling I/O concurrency while keeping code readable.

---

## ✅ Coroutines and `await`

```python
import asyncio

async def say_after(delay: float, msg: str) -> None:
    await asyncio.sleep(delay)
    print(msg)

asyncio.run(say_after(1.0, "hello"))
```

---

## ✅ Tasks and `gather()`

- `asyncio.create_task(...)` schedules a coroutine.
- `asyncio.gather(...)` waits for many tasks and returns results.

---

## ✅ Limiting Concurrency

Even in async code you sometimes need to limit parallel work (e.g. 1000 requests at once is still too many). Use an `asyncio.Semaphore`.

---

## 🔍 Key Takeaways

- `async`/`await` is for high-concurrency I/O.
- `await` is where other tasks can run.
- Use tasks + `gather()` to run many coroutines.

---

[Back: Module 12 README](../README.md)
