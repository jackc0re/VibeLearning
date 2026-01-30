"""
Creational Design Patterns - Exercises

Practice Singleton, Factory, and Builder ideas.
Run with:
    python exercises.py
"""

# =============================================================================
# EXERCISE 1: Singleton (Shared Instance)
# =============================================================================


class Settings:
    def __init__(self):
        self.values = {"debug": False}


SETTINGS = Settings()  # should act like a singleton


def exercise_1_toggle_debug():
    """Toggle the debug flag and return the updated value."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Simple Factory
# =============================================================================


class PushNotification:
    def send(self, msg):
        return f"Push: {msg}"


class SlackNotification:
    def send(self, msg):
        return f"Slack: {msg}"


def exercise_2_factory(kind):
    """Return a notification object based on kind: 'push' or 'slack'."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Builder
# =============================================================================


class Profile:
    def __init__(self, name, email=None, phone=None):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"Profile(name={self.name!r}, email={self.email!r}, phone={self.phone!r})"


class ProfileBuilder:
    def __init__(self):
        self._name = None
        self._email = None
        self._phone = None

    def name(self, value):
        self._name = value
        return self

    def email(self, value):
        self._email = value
        return self

    def phone(self, value):
        self._phone = value
        return self

    def build(self):
        return Profile(self._name, self._email, self._phone)


def exercise_3_build_profile():
    """
    Use ProfileBuilder to build a profile with:
    name='Ada', email='ada@dev.com', phone='555-0101'.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Creational Patterns Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Singleton Toggle")
    first = exercise_1_toggle_debug()
    second = exercise_1_toggle_debug()
    if first == second:
        all_passed = False
    status = "✓" if first != second else "✗"
    print(f"  {status} toggled values: {first} -> {second}")

    # Exercise 2
    print("\nExercise 2: Factory")
    try:
        notifier = exercise_2_factory("slack")
        result = notifier.send("Hi")
        status = "✓" if result == "Slack: Hi" else "✗"
        if result != "Slack: Hi":
            all_passed = False
        print(f"  {status} slack factory result: {result}")
    except Exception as exc:
        all_passed = False
        print(f"  ✗ factory raised: {exc}")

    # Exercise 3
    print("\nExercise 3: Builder")
    profile = exercise_3_build_profile()
    expected = "Profile(name='Ada', email='ada@dev.com', phone='555-0101')"
    status = "✓" if repr(profile) == expected else "✗"
    if repr(profile) != expected:
        all_passed = False
    print(f"  {status} built profile: {profile}")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
