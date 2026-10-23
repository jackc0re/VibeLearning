"""Async Programming - Examples
==============================

Demonstrations:
- running a coroutine with asyncio.run
- concurrent work with asyncio.gather
- limiting concurrency with asyncio.Semaphore

Run:
    python examples.py
"""

from __future__ import annotations

import asyncio
import time


def _now() -> str:
    return f"{time.perf_counter():.3f}"  # small helper for readable timestamps


# =============================================================================
# DEMO: CONCURRENT WORK WITH GATHER
# =============================================================================

async def demo_gather() -> None:
    async def fetch(name: str, delay: float) -> str:
        print(f"{_now()} start {name}")
        await asyncio.sleep(delay)
        print(f"{_now()} done  {name}")
        return f"{name}:{delay}"

    results = await asyncio.gather(fetch("a", 0.2), fetch("b", 0.1), fetch("c", 0.15))
    print("Results:", results)


# =============================================================================
# DEMO: LIMITING CONCURRENCY WITH SEMAPHORE
# =============================================================================

async def demo_semaphore() -> None:
    sem = asyncio.Semaphore(2)

    async def limited(i: int) -> int:
        async with sem:
            await asyncio.sleep(0.1)
            return i * i

    results = await asyncio.gather(*[limited(i) for i in range(6)])
    print("Limited results:", results)


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    print("=" * 50)
    print("ASYNC PROGRAMMING - Examples")
    print("=" * 50)

    print("\n--- Concurrent work with gather ---\n")
    asyncio.run(demo_gather())

    print("\n--- Limiting concurrency with a semaphore ---")
    asyncio.run(demo_semaphore())

    print("\n" + "=" * 50)
    print("Examples complete! Try exercises.py next.")
    print("=" * 50)


if __name__ == "__main__":
    main()
