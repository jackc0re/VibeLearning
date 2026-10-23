"""
Logging - Examples

Demonstrates why logging beats print, how a format string adds time and level,
how handlers send records to a file, how named loggers differ from the root
logger, and how the level filters which messages survive.
Run with:
    python examples.py
    LOG_LEVEL=DEBUG python examples.py
"""

import logging
import os
import tempfile
from pathlib import Path

# The level is a threshold: records below it never reach a handler.
# Read it from the environment so you can widen the window without editing code.
LEVEL_NAME = os.environ.get("LOG_LEVEL", "INFO").upper()
LOG_LEVEL = getattr(logging, LEVEL_NAME, logging.INFO)


class CountingStreamHandler(logging.StreamHandler):
    """StreamHandler that also counts the records it emits."""

    def __init__(self):
        super().__init__()
        self.count = 0

    def emit(self, record):
        self.count += 1
        super().emit(record)


def setup_logger():
    """Configure the root logger once, with a format that carries time and level."""
    logging.basicConfig(
        level=LOG_LEVEL,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )
    print("Log format: %(asctime)s | %(levelname)-8s | %(name)s | %(message)s")


def demo_print_vs_logging():
    print("\n--- print vs logging ---")
    print("print: always shown, no level, no timestamp, no destination")
    logger = logging.getLogger("demo.compare")
    logger.debug("debug detail: only shown when the level is DEBUG")
    logger.info("info event: shown with its time and level attached")


def demo_levels():
    logger = logging.getLogger("demo")
    print("\n--- One message per level ---")
    # With the default INFO level, the DEBUG line is filtered out.
    logger.debug("This is a debug message")
    logger.info("App started")
    logger.warning("Low disk space")
    logger.error("Failed to connect")
    logger.critical("System outage")


def demo_named_logger():
    print("\n--- Named logger vs root logger ---")
    logger = logging.getLogger(__name__)
    logger.info("record from the %s logger", logger.name)
    print(f"  __name__ when run as a script: {__name__}")
    print(f"  logger.name:                   {logger.name}")
    print(f"  root logger name:              {logging.getLogger().name}")
    print("  The name field shows which module logged the record.")
    print("  A named logger inherits the root handler but can also be")
    print("  leveled on its own: logging.getLogger(name).setLevel(...)")


def emit_three_messages(logger):
    logger.debug("debug: row 42 parsed")
    logger.info("info: import finished")
    logger.warning("warning: 3 rows skipped")


def demo_level_filtering():
    print("\n--- Same code, two levels, different output ---")
    for level_name in ("DEBUG", "WARNING"):
        level = getattr(logging, level_name)
        logger = logging.getLogger(f"demo.filter.{level_name.lower()}")
        logger.setLevel(level)
        logger.propagate = False  # keep this demo out of the root handler
        handler = CountingStreamHandler()
        handler.setFormatter(logging.Formatter("    %(levelname)-8s | %(message)s"))
        logger.addHandler(handler)

        print(f"  LOG_LEVEL={level_name}")
        emit_three_messages(logger)
        print(f"    -> {handler.count} of 3 records emitted")

        logger.removeHandler(handler)
        handler.close()


def demo_file_handler():
    print("\n--- FileHandler: logs outlive the terminal ---")
    with tempfile.TemporaryDirectory() as tmp:
        log_path = Path(tmp) / "app.log"

        logger = logging.getLogger("demo.file")
        logger.setLevel(logging.INFO)
        logger.propagate = False  # write to the file only

        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.name = "app-file"  # name it: real programs attach several handlers
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)-8s | %(message)s",
                datefmt="%H:%M:%S",
            )
        )
        logger.addHandler(file_handler)

        logger.info("job started")
        logger.warning("retrying request")

        file_handler.close()
        logger.removeHandler(file_handler)

        print(f"  handler: {type(file_handler).__name__} (name={file_handler.name})")
        print(f"  file:    {log_path.name}")
        print("  file contents:")
        for line in log_path.read_text(encoding="utf-8").splitlines():
            print("    " + line)
    print("  tempfile removed the file when the block ended - no stray files")


def demo_exception_logging():
    print("\n--- Logging an exception ---")
    logger = logging.getLogger("demo")
    try:
        int("not-a-number")
    except ValueError:
        logger.exception("Conversion failed")


if __name__ == "__main__":
    setup_logger()
    demo_print_vs_logging()
    demo_levels()
    demo_named_logger()
    demo_level_filtering()
    demo_file_handler()
    demo_exception_logging()
    print("\nPASS Examples complete!")
