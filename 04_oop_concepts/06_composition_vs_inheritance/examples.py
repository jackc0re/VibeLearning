"""
06_composition_vs_inheritance/examples.py

Comparing Inheritance ("Is-A") vs Composition ("Has-A").
"""

# -----------------------------------------------------------------------------
# 1. The Problem with Inheritance (Rigid)
# -----------------------------------------------------------------------------
print("\n--- 1. Inheritance (Rigid) ---")

# Imagine we want to add features to a Window
class Window:
    def open(self):
        print("Window opened.")
    
    def close(self):
        print("Window closed.")

# Logic reuse via inheritance
class SecureWindow(Window):
    def open(self):
        print("Authenticating...")
        super().open()

class FilteredWindow(Window):
    def open(self):
        print("Filtering sunlight...")
        super().open()

# What if we want a Secure AND Filtered Window?
# class SecureFilteredWindow(SecureWindow, FilteredWindow): ... ?
# This gets messy (Diamond Problem / Multiple Inheritance Complexity).

sw = SecureWindow()
sw.open()


# -----------------------------------------------------------------------------
# 2. The Solution with Composition (Flexible)
# -----------------------------------------------------------------------------
print("\n--- 2. Composition (Flexible) ---")

class Authentication:
    def authenticate(self):
        print("Authenticating user...")
        return True

class LightFilter:
    def apply(self):
        print("Applying light filter...")

class SmartWindow:
    def __init__(self, auth_system=None, filter_system=None):
        # The window HAS capabilities, it doesn't inherit them
        self.auth = auth_system
        self.filter = filter_system
        self.is_open = False

    def open(self):
        if self.auth:
            if not self.auth.authenticate():
                print("Access denied.")
                return
        
        if self.filter:
            self.filter.apply()
        
        self.is_open = True
        print("SmartWindow opened.")

# Easy to mix and match!
plain_window = SmartWindow()
secure_window = SmartWindow(auth_system=Authentication())
fancy_window = SmartWindow(auth_system=Authentication(), filter_system=LightFilter())

print(">> Plain Window:")
plain_window.open()

print("\n>> Secure Window:")
secure_window.open()

print("\n>> Fancy Window:")
fancy_window.open()
