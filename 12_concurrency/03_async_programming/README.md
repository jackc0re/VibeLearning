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

## ⚠️ Common Mistakes

- Calling **blocking** code inside a coroutine (`time.sleep`, `requests.get`) — it freezes the whole event loop; use `asyncio.sleep` and async libraries
- Forgetting `await` — you create a coroutine object that never runs (and Python warns you)
- Starting unbounded tasks (10,000 requests at once) — limit concurrency with `asyncio.Semaphore`

---

## 📝 Quick Reference

```python
import asyncio

async def work(delay: float) -> str:
    await asyncio.sleep(delay)     # await = other tasks may run here
    return "done"

asyncio.run(work(0.1))                          # entry point
results = await asyncio.gather(work(0.1), work(0.2))
task = asyncio.create_task(work(0.1))           # schedule now

sem = asyncio.Semaphore(10)
async with sem:                                 # limit parallel work
    ...
```

---

[Back: Module 12 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
