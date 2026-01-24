"""
Logging - Exercises

Practice using logging with levels and exception handling.
Run with:
    python exercises.py
"""

import logging


# =============================================================================
# EXERCISE 1: Configure Logger
# =============================================================================


def exercise_1_configure_logger():
    """
    Configure basic logging to INFO level with format:
    "LEVEL | message". Return the logger named "exercise".
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(message)s",
    )
    return logging.getLogger("exercise")


# =============================================================================
# EXERCISE 2: Log Levels
# =============================================================================


def exercise_2_log_levels(logger):
    """
    Using the provided logger, log one message at each level:
    DEBUG, INFO, WARNING, ERROR, CRITICAL.
    """
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")


# =============================================================================
# EXERCISE 3: Log Exception
# =============================================================================


def exercise_3_log_exception(logger):
    """
    Trigger a ValueError and log it with logger.exception().
    Return True if the exception was handled.
    """
    try:
        int("not-a-number")
    except ValueError:
        logger.exception("conversion failed")
        return True


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Logging Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Configure Logger")
    try:
        logger = exercise_1_configure_logger()
        status = "PASS" if isinstance(logger, logging.Logger) else "FAIL"
        if not isinstance(logger, logging.Logger):
            all_passed = False
        print(f"  {status} logger instance -> {logger}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")
        logger = logging.getLogger("exercise")

    # Exercise 2
    print("\nExercise 2: Log Levels")
    try:
        exercise_2_log_levels(logger)
        print("  PASS logged all levels")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    # Exercise 3
    print("\nExercise 3: Log Exception")
    try:
        result = exercise_3_log_exception(logger)
        status = "PASS" if result is True else "FAIL"
        if result is not True:
            all_passed = False
        print(f"  {status} exception handled -> {result}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    print("\n" + "=" * 50)
    if all_passed:
        print("All tests passed! Great job!")
    else:
        print("Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
