"""Optimization Techniques - Examples

Demonstrations:
- caching with functools.lru_cache
- string joining

Run:
    python examples.py
"""

from __future__ import annotations

from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def join_demo(parts: list[str]) -> str:
    return "".join(parts)


if __name__ == "__main__":
    print("fib(10):", fib(10))
    print("join_demo:", join_demo(["a", "b", "c"]))

