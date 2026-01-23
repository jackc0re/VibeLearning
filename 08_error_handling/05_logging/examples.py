"""
Logging - Examples

Demonstrates logging levels and exception logging.
Run with:
    python examples.py
"""

import logging


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(name)s | %(message)s",
    )


def demo_levels():
    logger = logging.getLogger("demo")
    logger.debug("This is a debug message")
    logger.info("App started")
    logger.warning("Low disk space")
    logger.error("Failed to connect")
    logger.critical("System outage")


def demo_exception_logging():
    logger = logging.getLogger("demo")
    try:
        int("not-a-number")
    except ValueError:
        logger.exception("Conversion failed")


if __name__ == "__main__":
    setup_logger()
    demo_levels()
    demo_exception_logging()
    print("\n✓ Examples complete!")
