"""
02_encapsulation/examples.py

Demonstrating access modifiers and properties in Python.
"""

# -----------------------------------------------------------------------------
# 1. Public, Protected, and Private Attributes
# -----------------------------------------------------------------------------
print("\n--- 1. Access Modifiers ---")

class Account:
    def __init__(self, owner, balance, pin):
        self.owner = owner         # Public
        self._balance = balance    # Protected (Convention: internal use)
        self.__pin = pin           # Private (Name mangling)

    def show_info(self):
        # We can access everything inside the class
        print(f"Owner: {self.owner}, Balance: {self._balance}")

    def check_pin(self, pin):
        return self.__pin == pin

acct = Account("Alice", 1000, 1234)

# Public access works fine
print(f"Owner: {acct.owner}")

# Protected access works (but you shouldn't do it outside the class/subclass)
print(f"Balance (naughty access): {acct._balance}")

# Private access FAILS
try:
    print(f"PIN: {acct.__pin}")
except AttributeError as e:
    print(f"Error accessing __pin: {e}")

# But... Python is tricky. Name mangling makes it accessible if you really try:
print(f"Sneaky PIN access: {acct._Account__pin}") # Don't do this in real code!


# -----------------------------------------------------------------------------
# 2. Getters and Setters (Old School)
# -----------------------------------------------------------------------------
print("\n--- 2. Getters and Setters ---")

class OldSchoolUser:
    def __init__(self, username):
        self.set_username(username)
    
    def get_username(self):
        return self._username
    
    def set_username(self, value):
        if len(value) < 4:
            print(f"Error: Username '{value}' is too short.")
        else:
            self._username = value
            print(f"Username set to {self._username}")

user = OldSchoolUser("bob")
user.set_username("bo")
user.set_username("superbob")


# -----------------------------------------------------------------------------
# 3. The @property Decorator (Pythonic Way)
# -----------------------------------------------------------------------------
print("\n--- 3. Properties ---")

class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature # This actually calls the setter!

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print(f"Setting value to {value}...")
        if value < -273.15:
            print("Error: Temperature below absolute zero is impossible!")
            # We preserve the old value or set to a default, or raise error.
            # Here keeping the old value if it exists, else setting to min.
            if not hasattr(self, '_temperature'):
                 self._temperature = -273.15
        else:
            self._temperature = value

thermometer = Celsius()
thermometer.temperature = 37
print(f"Current temp: {thermometer.temperature}")

thermometer.temperature = -300
print(f"Current temp: {thermometer.temperature}")
