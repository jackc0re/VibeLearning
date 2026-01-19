"""
Control Flow - Examples
=======================
Run this file to see control flow in action!
"""

print("=" * 50)
print("CONTROL FLOW - Examples")
print("=" * 50)

# =============================================================================
# BASIC IF STATEMENT
# =============================================================================
print("\n--- Basic If Statement ---\n")

age = 20

if age >= 18:
    print(f"Age {age}: You are an adult!")

# If condition is False, nothing happens
age = 15

if age >= 18:
    print("This won't print because age < 18")

print("This always prints (outside the if block)")

# =============================================================================
# IF-ELSE STATEMENT
# =============================================================================
print("\n--- If-Else Statement ---\n")

temperature = 35

if temperature > 30:
    weather = "hot"
    advice = "Stay hydrated! 💧"
else:
    weather = "comfortable"
    advice = "Enjoy the weather! 🌤️"

print(f"Temperature: {temperature}°C")
print(f"Weather: {weather}")
print(f"Advice: {advice}")

# =============================================================================
# IF-ELIF-ELSE STATEMENT
# =============================================================================
print("\n--- If-Elif-Else Statement ---\n")

# Grade calculator
score = 85

if score >= 90:
    grade = "A"
    message = "Excellent!"
elif score >= 80:
    grade = "B"
    message = "Great job!"
elif score >= 70:
    grade = "C"
    message = "Good work!"
elif score >= 60:
    grade = "D"
    message = "You passed."
else:
    grade = "F"
    message = "Keep trying!"

print(f"Score: {score}")
print(f"Grade: {grade}")
print(f"Message: {message}")

# Multiple test cases
print("\n--- Multiple Scores ---")
scores = [95, 82, 73, 61, 45]

for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Score {score} → Grade {grade}")

# =============================================================================
# NESTED CONDITIONS
# =============================================================================
print("\n--- Nested Conditions ---\n")

has_ticket = True
age = 15
is_with_adult = True

print(f"Has ticket: {has_ticket}")
print(f"Age: {age}")
print(f"With adult: {is_with_adult}")

if has_ticket:
    if age >= 18:
        print("✅ Welcome! Enjoy the movie!")
    else:
        if is_with_adult:
            print("✅ Welcome! You must stay with your guardian.")
        else:
            print("❌ Sorry, you need an adult guardian.")
else:
    print("❌ Please purchase a ticket at the counter.")

# Flattened (better) version
print("\n--- Same Logic (Flattened) ---")

if not has_ticket:
    print("❌ Please purchase a ticket at the counter.")
elif age >= 18:
    print("✅ Welcome! Enjoy the movie!")
elif is_with_adult:
    print("✅ Welcome! You must stay with your guardian.")
else:
    print("❌ Sorry, you need an adult guardian.")

# =============================================================================
# CONDITIONAL EXPRESSIONS (TERNARY)
# =============================================================================
print("\n--- Conditional Expressions ---\n")

age = 20

# Traditional if-else
if age >= 18:
    status = "adult"
else:
    status = "minor"
print(f"Traditional: {status}")

# Conditional expression
status = "adult" if age >= 18 else "minor"
print(f"Ternary: {status}")

# Practical examples
count = 5
print(f"You have {count} item{'s' if count != 1 else ''}")

count = 1
print(f"You have {count} item{'s' if count != 1 else ''}")

# Finding max/min
a, b = 10, 25
max_val = a if a > b else b
min_val = a if a < b else b
print(f"Between {a} and {b}: max={max_val}, min={min_val}")

# =============================================================================
# TRUTHY AND FALSY VALUES
# =============================================================================
print("\n--- Truthy and Falsy Values ---\n")

# Demonstrating falsy values
falsy_values = [False, None, 0, 0.0, "", [], {}]

print("Falsy values:")
for val in falsy_values:
    result = "truthy" if val else "falsy"
    print(f"  {repr(val):10} → {result}")

# Demonstrating truthy values
print("\nTruthy values:")
truthy_values = [True, 1, -1, 0.1, "hello", [1], {"a": 1}]

for val in truthy_values:
    result = "truthy" if val else "falsy"
    print(f"  {repr(val):15} → {result}")

# Practical application
print("\n--- Practical Truthy/Falsy ---")

username = ""
display_name = username if username else "Anonymous"
print(f"Username: '{username}' → Display: {display_name}")

username = "alice"
display_name = username if username else "Anonymous"
print(f"Username: '{username}' → Display: {display_name}")

# Using 'or' for defaults
print("\n--- Using 'or' for Defaults ---")
name = ""
print(f"Hello, {name or 'Guest'}!")

name = "Bob"
print(f"Hello, {name or 'Guest'}!")

# =============================================================================
# COMPARISON CHAINS
# =============================================================================
print("\n--- Comparison Chains ---\n")

# Check if value is in a range
temperature = 22

if 18 <= temperature <= 25:
    comfort = "comfortable"
elif temperature < 18:
    comfort = "cold"
else:
    comfort = "hot"

print(f"Temperature {temperature}°C is {comfort}")

# Multiple range checks
print("\nTemperature Comfort Levels:")
for temp in [10, 18, 22, 25, 35]:
    if temp < 15:
        level = "❄️ Cold"
    elif 15 <= temp < 20:
        level = "🌤️ Cool"
    elif 20 <= temp < 28:
        level = "☀️ Comfortable"
    else:
        level = "🔥 Hot"
    print(f"  {temp}°C → {level}")

# =============================================================================
# COMBINING CONDITIONS
# =============================================================================
print("\n--- Combining Conditions ---\n")

age = 25
has_license = True
has_car = False

print(f"Age: {age}")
print(f"Has license: {has_license}")
print(f"Has car: {has_car}")

# AND - both must be true
can_drive = age >= 16 and has_license
print(f"\nCan drive (age >= 16 AND has license): {can_drive}")

# OR - at least one must be true
needs_transport = not has_car or age < 16
print(f"Needs transport (no car OR under 16): {needs_transport}")

# Complex condition
is_eligible_driver = age >= 16 and has_license and (has_car or False)
print(f"Eligible driver: {is_eligible_driver}")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
