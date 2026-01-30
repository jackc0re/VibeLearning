"""Async Programming - Exercises

These exercises use asyncio primitives:
- tasks + gather
- limiting concurrency with asyncio.Semaphore
- timeouts via asyncio.wait_for

Run with:
    python exercises.py
"""

from __future__ import annotations

import asyncio
from typing import Awaitable, Callable, List, Optional, Tuple, TypeVar

T = TypeVar("T")


# =============================================================================
# EXERCISE 1: Fetch All
# =============================================================================


def _make_message(i: int) -> str:
    return f"done-{i}"


async def exercise_1_fetch_all(delays: List[float]) -> List[str]:
    """Return a message for each delay after sleeping concurrently."""

    async def job(i: int, delay: float) -> str:
        await asyncio.sleep(delay)
        return _make_message(i)

    return await asyncio.gather(*[job(i, d) for i, d in enumerate(delays)])


# =============================================================================
# EXERCISE 2: Limited Gather
# =============================================================================


async def exercise_2_limited_gather(
    factories: List[Callable[[], Awaitable[T]]],
    limit: int,
) -> List[T]:
    """Run coroutine factories with a concurrency limit.

    Each factory should create a *new* coroutine when called.
    """

    if limit <= 0:
        raise ValueError("limit must be >= 1")

    sem = asyncio.Semaphore(limit)

    async def run_one(factory: Callable[[], Awaitable[T]]) -> T:
        async with sem:
            return await factory()

    return await asyncio.gather(*[run_one(f) for f in factories])


# =============================================================================
# EXERCISE 3: Timeout Wrapper
# =============================================================================


async def exercise_3_with_timeout(coro: Awaitable[T], timeout: float) -> Tuple[bool, Optional[T]]:
    """Return (True, result) or (False, None) if it times out."""

    try:
        value = await asyncio.wait_for(coro, timeout=timeout)
        return True, value
    except asyncio.TimeoutError:
        return False, None


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Async Programming Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Fetch All")
    try:
        got = asyncio.run(exercise_1_fetch_all([0.02, 0.01, 0.03]))
        ok = got == ["done-0", "done-1", "done-2"]
        print("  ", "PASS" if ok else "FAIL", got)
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2
    print("\nExercise 2: Limited Gather")
    try:
        async def scenario() -> bool:
            active = 0
            max_active = 0
            lock = asyncio.Lock()

            async def make_task(i: int) -> int:
                nonlocal active, max_active
                async with lock:
                    active += 1
                    max_active = max(max_active, active)
                await asyncio.sleep(0.02)
                async with lock:
                    active -= 1
                return i

            def factory(i: int) -> Callable[[], Awaitable[int]]:
                async def run() -> int:
                    return await make_task(i)

                return run

            factories = [factory(i) for i in range(10)]
            out = await exercise_2_limited_gather(factories, limit=3)
            return sorted(out) == list(range(10)) and max_active <= 3

        ok = asyncio.run(scenario())
        print("  ", "PASS" if ok else "FAIL", "concurrency limited")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3
    print("\nExercise 3: Timeout Wrapper")
    try:
        async def slow() -> int:
            await asyncio.sleep(0.05)
            return 123

        ok1, val1 = asyncio.run(exercise_3_with_timeout(slow(), timeout=0.2))
        ok2, val2 = asyncio.run(exercise_3_with_timeout(slow(), timeout=0.01))
        ok = ok1 is True and val1 == 123 and ok2 is False and val2 is None
        print("  ", "PASS" if ok else "FAIL", (ok1, val1), (ok2, val2))
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
