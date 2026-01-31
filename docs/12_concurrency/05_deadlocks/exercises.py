"""Deadlocks - Exercises

Focus:
- lock ordering to prevent deadlocks
- safe transfer between two locked objects

Run with:
    python exercises.py
"""

from __future__ import annotations

import threading
from dataclasses import dataclass
from typing import List, Tuple


# =============================================================================
# EXERCISE 1: Lock Ordering Helper
# =============================================================================


def exercise_1_order_locks(a: threading.Lock, b: threading.Lock) -> Tuple[threading.Lock, threading.Lock]:
    """Return (first, second) locks in a consistent order.

    Using id() is a simple way to define an ordering for objects.
    """

    return (a, b) if id(a) < id(b) else (b, a)


# =============================================================================
# EXERCISE 2: BankAccount Transfer Without Deadlock
# =============================================================================


@dataclass
class BankAccount:
    name: str
    balance: int

    def __post_init__(self) -> None:
        self._lock = threading.Lock()

    @property
    def lock(self) -> threading.Lock:
        return self._lock


def exercise_2_transfer(src: BankAccount, dst: BankAccount, amount: int) -> bool:
    """Transfer amount from src to dst using consistent lock ordering."""

    if amount < 0:
        raise ValueError("amount must be >= 0")

    first, second = exercise_1_order_locks(src.lock, dst.lock)

    with first:
        with second:
            if src.balance < amount:
                return False
            src.balance -= amount
            dst.balance += amount
            return True


# =============================================================================
# EXERCISE 3: Run Many Transfers
# =============================================================================


def exercise_3_run_transfers(accounts: List[BankAccount], transfers: List[Tuple[int, int, int]]) -> int:
    """Run transfers in threads and return the total final balance."""

    def do_one(src_i: int, dst_i: int, amount: int) -> None:
        exercise_2_transfer(accounts[src_i], accounts[dst_i], amount)

    threads = [threading.Thread(target=do_one, args=t) for t in transfers]
    for th in threads:
        th.start()
    for th in threads:
        th.join()

    return sum(a.balance for a in accounts)


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Deadlocks Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Lock Ordering Helper")
    try:
        a = threading.Lock()
        b = threading.Lock()
        first, second = exercise_1_order_locks(a, b)
        ok = (first is a and second is b) or (first is b and second is a)
        print("  ", "PASS" if ok else "FAIL", "ordered")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2
    print("\nExercise 2: BankAccount Transfer")
    try:
        alice = BankAccount("alice", 100)
        bob = BankAccount("bob", 50)
        ok1 = exercise_2_transfer(alice, bob, 30) is True
        ok2 = (alice.balance, bob.balance) == (70, 80)
        ok3 = exercise_2_transfer(alice, bob, 999) is False
        ok = ok1 and ok2 and ok3
        print("  ", "PASS" if ok else "FAIL", (alice.balance, bob.balance))
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3
    print("\nExercise 3: Run Many Transfers")
    try:
        accounts = [BankAccount(f"a{i}", 1000) for i in range(5)]
        total_before = sum(a.balance for a in accounts)

        transfers = []
        for i in range(100):
            src = i % 5
            dst = (i + 1) % 5
            transfers.append((src, dst, 5))

        total_after = exercise_3_run_transfers(accounts, transfers)
        ok = total_after == total_before
        print("  ", "PASS" if ok else "FAIL", total_after)
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
