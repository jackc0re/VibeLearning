# CLI Cheatsheet

Quick reference for command-line programs in Python: `argparse` skeleton, `sys.argv`, interactive menus, and exit codes.

---

## argparse Minimal Skeleton

Copy this and edit the arguments — it gives you `--help`, type checking, and friendly errors for free:

```python
"""Greet people from the command line."""
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Greet someone, optionally many times."
    )
    # Positional: required, comes in order
    parser.add_argument("name", help="who to greet")
    # Optional flag with a value, converted to int
    parser.add_argument(
        "--count", type=int, default=1,
        help="number of greetings (default: 1)",
    )
    # Value restricted to a fixed set
    parser.add_argument(
        "--style", choices=["plain", "loud"], default="plain",
        help="greeting style",
    )
    # Flag that is either present or absent
    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="print extra details",
    )
    # Optional value that the user MUST provide
    parser.add_argument("--suffix", required=True, help="e.g. '!!!'")

    args = parser.parse_args()

    greeting = f"Hello, {args.name}"
    if args.style == "loud":
        greeting = greeting.upper()
    for _ in range(args.count):
        print(greeting + args.suffix)

    if args.verbose:
        print(f"[verbose] greeted {args.name} {args.count} time(s)")


if __name__ == "__main__":
    main()
```

```text
$ python greet.py Alice --count 2 --style loud --suffix "!"
HELLO, ALICE!
HELLO, ALICE!

$ python greet.py --help      # auto-generated, always up to date
```

### add_argument Cheat Table

| Keyword | Used for | Example |
|---------|----------|---------|
| *(none)* | Positional argument, always required | `add_argument("name")` |
| `type=` | Convert the string the shell gives you | `type=int`, `type=float` |
| `default=` | Value when the flag is absent | `default=1` |
| `choices=[...]` | Restrict to a fixed set | `choices=["plain", "loud"]` |
| `required=True` | Make an optional argument mandatory | (no silent `None`s) |
| `action="store_true"` | On/off flag, no value | `-v`, `--verbose` |
| `help=` | Text shown in `--help` | always add one |

---

## Positional vs Optional Arguments

| | Positional | Optional (flag) |
|---|-----------|-----------------|
| Declared | `add_argument("name")` | `add_argument("--count", ...)` |
| On the command line | `python greet.py Alice` | `python greet.py --count 3` |
| Required? | Yes, by default | No, unless `required=True` |
| Order matters? | Yes — must come in declared order | No — can appear anywhere |
| Best for | The main input (a file, a word) | Modifiers (`--count`, `--verbose`) |

Convention: one dash = short flag (`-v`), two dashes = long flag (`--verbose`). Offering both is a nice touch: `parser.add_argument("-v", "--verbose", ...)`.

---

## sys.argv Quick Use

For tiny scripts, skip argparse and read the raw list:

```python
import sys

print(sys.argv)        # ['script.py', 'hello', '42']  — ALL strings!
script = sys.argv[0]   # the script's own name
args = sys.argv[1:]    # just the user's arguments

if len(args) < 1:
    sys.exit("Usage: python script.py <name>")  # prints to stderr, exits 1

name = args[0]
count = int(args[1]) if len(args) > 1 else 1   # YOU convert types yourself
```

`sys.argv` values are always strings — `"42"` not `42` — and there's no `--help`.
Reach for argparse as soon as you have more than one or two arguments.

---

## Interactive Menu Loop

A small, bounded menu: every input is handled, and there's exactly one exit door.

```python
def menu():
    while True:
        print("\n1) Greet  2) Time  3) Quit")
        choice = input("Pick 1-3: ").strip()

        if choice == "1":
            print("Hello there!")
        elif choice == "2":
            import datetime
            print(datetime.datetime.now().strftime("%H:%M:%S"))
        elif choice == "3":
            print("Bye!")
            break                      # the one exit
        else:
            print("Please enter 1, 2, or 3.")  # bad input ≠ crash

menu()
```

`input()` always returns a string — `.strip()` it, compare it as a string, and
convert with `int()` only when you mean it (inside a `try/except ValueError`
if the user types free-form).

---

## Exit Codes

When your script ends, it reports a number to the shell: **0 means success, anything else means something went wrong.**

| Code | Meaning | How it happens |
|------|---------|----------------|
| `0` | Success | Script ends normally, or `sys.exit(0)` |
| `1` | Generic error | `sys.exit("message")` or `sys.exit(1)` |
| `2` | Bad command-line usage | What `argparse` exits with on invalid arguments |

```python
import sys

def main():
    try:
        with open(sys.argv[1], encoding="utf-8") as f:
            print(f.read())
        return 0                       # success
    except (FileNotFoundError, IndexError):
        print("Usage: python show.py <file>", file=sys.stderr)
        return 1                       # failure

if __name__ == "__main__":
    sys.exit(main())                   # main's return value becomes the exit code
```

Test it from the shell with `echo %ERRORLEVEL%` (Windows) or `echo $?` (macOS/Linux).

---

## Practice: Build Real CLIs

The best way to make this stick is to build things. The repo's
[11 guided projects](../../Projects/README.md) — calculator, todo app, file
organizer, quiz game, password manager and more — are all command-line
programs. Try upgrading one you've finished: replace `input()`-driven flow
with an `argparse` interface, or add a proper exit code when a file is missing.

---

**Back to [Resources](../README.md)**
