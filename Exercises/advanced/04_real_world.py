"""
Advanced Exercise 4: Real-World Applications
============================================
Design a tiny REST-style router, a layered configuration loader,
a leveled logger, and an argparse command-line interface.
Everything runs offline - no servers, no sockets.
"""

print("=" * 50)
print("EXERCISE 4: Real-World Applications")
print("=" * 50)


# =============================================================================
# EXERCISE 4.1: REST API Design (Router)
# =============================================================================
print("\n--- Exercise 4.1: REST API Design (Router) ---")
"""
Build a mini router that mimics how web frameworks dispatch:

- Router.add_route(method, pattern, handler) registers handlers,
  where a pattern like "/users/<id>" matches any single segment
- Router.dispatch(method, path) returns (status_code, body dict):
  200 with handler(params) on a match, 404 for an unknown path,
  405 when the path exists but the method is wrong
"""


# Your code below:
class Router:
    """Tiny REST-style route table."""

    pass


# Test (uncomment after implementing)
# router = Router()
# router.add_route("GET", "/users/<id>", lambda params: {"id": params["id"]})
# print(router.dispatch("GET", "/users/42"))


# =============================================================================
# EXERCISE 4.2: Configuration Management
# =============================================================================
print("\n--- Exercise 4.2: Configuration Management ---")
"""
Layered configuration, later layers win:

- parse_env(env, prefix="VL_"): keep "VL_"-prefixed keys, strip the
  prefix, lowercase the rest, and convert "1"/"true"/"yes" to True
  and "0"/"false"/"no" to False (like reading os.environ)
- Config.from_layers(defaults, file_settings, env) merges the three
  dicts in that order
- Config.get(key, default=None)
"""


# Your code below:
def parse_env(env, prefix="VL_"):
    """Convert prefixed env strings into a settings dict."""
    pass


class Config:
    """Merged, layered application configuration."""

    pass


# Test (uncomment after implementing)
# config = Config.from_layers({"debug": False}, {}, {"VL_DEBUG": "1"})
# print(config.get("debug"))


# =============================================================================
# EXERCISE 4.3: Logging System
# =============================================================================
print("\n--- Exercise 4.3: Logging System ---")
"""
Build a leveled logger that writes into any file-like sink:

- Logger(name, level="INFO", sink): sink is a writable object
- Methods debug / info / warning / error
- Only messages at or above the configured level are written
- Line format: "<timestamp> [LEVEL] name: message"
"""

import io
from datetime import datetime


# Your code below:
LEVELS = {"DEBUG": 10, "INFO": 20, "WARNING": 30, "ERROR": 40}


class Logger:
    """A leveled logger writing to a file-like sink."""

    pass


# Test (uncomment after implementing)
# sink = io.StringIO()
# log = Logger("app", level="INFO", sink=sink)
# log.info("starting up")


# =============================================================================
# EXERCISE 4.4: Command-Line Interface
# =============================================================================
print("\n--- Exercise 4.4: Command-Line Interface ---")
"""
Build a todo CLI with argparse (no sys.argv needed):

- build_parser(): subcommands "add TEXT [--priority high|low]",
  "list", and "done ID"
- main(argv, store=None): parse the given argv list, apply the
  command to a dict store, and return a list of message strings
"""

import argparse


# Your code below:
def build_parser():
    """Return the argparse parser for the todo CLI."""
    pass


# Test (uncomment after implementing)
# print(main(["add", "Write tests", "--priority", "high"], {}))


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 4.1
print("\n--- Solution 4.1 ---")


class Router:
    """Tiny REST-style route table."""

    def __init__(self):
        self._routes = {}

    def add_route(self, method, pattern, handler):
        self._routes[(method, pattern)] = handler

    @staticmethod
    def _match(pattern, path):
        """Return a params dict if path fits pattern, else None."""
        pattern_parts = pattern.strip("/").split("/")
        path_parts = path.strip("/").split("/")
        if len(pattern_parts) != len(path_parts):
            return None
        params = {}
        for expected, actual in zip(pattern_parts, path_parts):
            if expected.startswith("<") and expected.endswith(">"):
                params[expected[1:-1]] = actual
            elif expected != actual:
                return None
        return params

    def dispatch(self, method, path):
        """Return (status_code, body) for a request."""
        for (route_method, pattern), handler in self._routes.items():
            params = self._match(pattern, path)
            if params is not None:
                if route_method == method:
                    return 200, handler(params)
                return 405, {"error": "method not allowed"}
        return 404, {"error": "not found"}


router = Router()
router.add_route("GET", "/users", lambda params: {"users": ["alice", "bob"]})
router.add_route("GET", "/users/<id>", lambda params: {"id": params["id"], "name": f"user{params['id']}"})
router.add_route("POST", "/users", lambda params: {"created": True})

for method, path in [
    ("GET", "/users/42"),
    ("GET", "/users"),
    ("POST", "/users"),
    ("DELETE", "/users/42"),
    ("GET", "/nope"),
]:
    status, body = router.dispatch(method, path)
    print(f"{method:6s} {path:12s} -> {status} {body}")

# SOLUTION 4.2
print("\n--- Solution 4.2 ---")


def parse_env(env, prefix="VL_"):
    """Convert prefixed env strings into a settings dict."""
    settings = {}
    for key, value in env.items():
        if not key.startswith(prefix):
            continue
        name = key[len(prefix):].lower()
        if value in ("1", "true", "yes"):
            settings[name] = True
        elif value in ("0", "false", "no"):
            settings[name] = False
        else:
            settings[name] = value
    return settings


class Config:
    """Merged, layered application configuration."""

    def __init__(self, values):
        self._values = dict(values)

    @classmethod
    def from_layers(cls, defaults, file_settings, env):
        """Merge defaults < file_settings < env (later wins)."""
        merged = dict(defaults)
        merged.update(file_settings)
        merged.update(parse_env(env))
        return cls(merged)

    def get(self, key, default=None):
        return self._values.get(key, default)


config = Config.from_layers(
    {"debug": False, "port": 8000, "theme": "light"},
    {"theme": "dark"},
    {"VL_DEBUG": "1", "VL_PORT": "9000", "UNRELATED": "ignored"},
)
print(f"debug : {config.get('debug')}   (from env, beats False)")
print(f"port  : {config.get('port')}  (from env, beats 8000)")
print(f"theme : {config.get('theme')}  (from file, beats 'light')")

# SOLUTION 4.3
print("\n--- Solution 4.3 ---")

LEVELS = {"DEBUG": 10, "INFO": 20, "WARNING": 30, "ERROR": 40}


class Logger:
    """A leveled logger writing to a file-like sink."""

    def __init__(self, name, level="INFO", sink=None):
        self.name = name
        self.level = LEVELS[level.upper()]
        self.sink = sink if sink is not None else io.StringIO()

    def log(self, level, message):
        if LEVELS[level] >= self.level:
            stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.sink.write(f"{stamp} [{level}] {self.name}: {message}\n")

    def debug(self, message):
        self.log("DEBUG", message)

    def info(self, message):
        self.log("INFO", message)

    def warning(self, message):
        self.log("WARNING", message)

    def error(self, message):
        self.log("ERROR", message)


sink = io.StringIO()
log = Logger("app", level="INFO", sink=sink)
log.debug("too chatty, filtered out")
log.info("starting up")
log.warning("cache is cold")
log.error("disk almost full")

print(sink.getvalue(), end="")
print(f"DEBUG lines written: {sink.getvalue().count('[DEBUG]')} (expected 0)")

# SOLUTION 4.4
print("\n--- Solution 4.4 ---")


def build_parser():
    """Return the argparse parser for the todo CLI."""
    parser = argparse.ArgumentParser(prog="todo")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="add a new todo")
    add.add_argument("text")
    add.add_argument("--priority", choices=["high", "low"], default="low")

    sub.add_parser("list", help="show all todos")

    done = sub.add_parser("done", help="mark a todo complete")
    done.add_argument("id", type=int)
    return parser


def main(argv, store=None):
    """Run one CLI invocation against a dict store."""
    if store is None:
        store = {}
    args = build_parser().parse_args(argv)

    if args.command == "add":
        store[len(store) + 1] = {
            "text": args.text,
            "priority": args.priority,
            "done": False,
        }
        return [f"Added #{len(store)}: {args.text} ({args.priority})"]
    if args.command == "list":
        if not store:
            return ["No todos yet."]
        return [
            f"#{number}: {todo['text']} [{todo['priority']}]"
            + (" (done)" if todo["done"] else "")
            for number, todo in sorted(store.items())
        ]
    if args.command == "done":
        store[args.id]["done"] = True
        return [f"Marked #{args.id} done"]
    return [f"Unknown command: {args.command}"]


store = {}
for invocation in [
    ["add", "Write exercises", "--priority", "high"],
    ["add", "Review pull request"],
    ["list"],
    ["done", "1"],
    ["list"],
]:
    print(f"$ todo {' '.join(invocation)}")
    for message in main(invocation, store):
        print(f"  {message}")

print("\n" + "=" * 50)
print("Great job! Move on to 05_testing.py")
print("=" * 50)
