"""
Beginner Exercise 1: Variables and Types
=========================================
Practice working with different data types and type conversions.
"""

print("=" * 50)
print("EXERCISE 1: Variables and Types")
print("=" * 50)


# =============================================================================
# EXERCISE 1.1: Type Conversions
# =============================================================================
print("\n--- Exercise 1.1: Type Conversions ---")
"""
Complete the following type conversions:
1. Convert string to integer
2. Convert integer to float
3. Convert float to string
4. Convert string to boolean
"""

# Given variables
num_str = "42"
num_int = 10
num_float = 3.14
bool_str = "True"

# Your code below:
str_to_int =  # Convert num_str to integer
int_to_float =  # Convert num_int to float
float_to_str =  # Convert num_float to string
str_to_bool =  # Convert bool_str to boolean

# Test your conversions
print(f"String '{num_str}' to integer: {str_to_int}")
print(f"Integer {num_int} to float: {int_to_float}")
print(f"Float {num_float} to string: '{float_to_str}'")
print(f"String '{bool_str}' to boolean: {str_to_bool}")


# =============================================================================
# EXERCISE 1.2: String Formatting
# =============================================================================
print("\n--- Exercise 1.2: String Formatting ---")
"""
Create a formatted string using f-strings that includes:
- Name (variable: name)
- Age (variable: age)
- City (variable: city)
- A greeting message

Example output: "Hello, my name is Alice. I am 25 years old and live in New York."
"""

name = "Alice"
age = 25
city = "New York"

# Your code below:
greeting =  # Create formatted string
print(greeting)


# =============================================================================
# EXERCISE 1.3: Working with Numbers
# =============================================================================
print("\n--- Exercise 1.3: Working with Numbers ---")
"""
Given a price and discount percentage:
1. Calculate the discount amount
2. Calculate the final price
3. Round to 2 decimal places
4. Format as currency ($X.XX)
"""

price = 99.99
discount_percent = 15  # 15%

# Your code below:
discount_amount =  # Calculate discount
final_price =  # Calculate final price
rounded_price =  # Round to 2 decimals
currency_format =  # Format as $X.XX

print(f"Original price: ${price}")
print(f"Discount: {discount_percent}%")
print(f"Discount amount: ${discount_amount:.2f}")
print(f"Final price: {currency_format}")


# =============================================================================
# EXERCISE 1.4: String Operations
# =============================================================================
print("\n--- Exercise 1.4: String Operations ---")
"""
Given a full name in the format "First Last":
1. Extract the first name
2. Extract the last name
3. Create initials (e.g., "AB")
4. Reverse the full name
"""

full_name = "John Doe"

# Your code below:
first_name =  # Extract first name
last_name =  # Extract last name
initials =  # Create initials
reversed_name =  # Reverse the name

print(f"Full name: {full_name}")
print(f"First name: {first_name}")
print(f"Last name: {last_name}")
print(f"Initials: {initials}")
print(f"Reversed: {reversed_name}")


# =============================================================================
# EXERCISE 1.5: Type Checking
# =============================================================================
print("\n--- Exercise 1.5: Type Checking ---")
"""
Create a function that checks the type of a value and returns:
- "integer" for integers
- "float" for floats
- "string" for strings
- "boolean" for booleans
- "unknown" for anything else
"""

def get_type(value):
    """Return a string describing the type of value."""
    # Your code below:
    pass


# Test the function
test_values = [42, 3.14, "hello", True, [1, 2, 3], {"key": "value"}]
for val in test_values:
    print(f"Value: {val} | Type: {get_type(val)}")


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 1.1
print("\n--- Solution 1.1 ---")
num_str = "42"
num_int = 10
num_float = 3.14
bool_str = "True"

str_to_int = int(num_str)
int_to_float = float(num_int)
float_to_str = str(num_float)
str_to_bool = bool_str == "True"

print(f"String '{num_str}' to integer: {str_to_int}")
print(f"Integer {num_int} to float: {int_to_float}")
print(f"Float {num_float} to string: '{float_to_str}'")
print(f"String '{bool_str}' to boolean: {str_to_bool}")

# SOLUTION 1.2
print("\n--- Solution 1.2 ---")
name = "Alice"
age = 25
city = "New York"

greeting = f"Hello, my name is {name}. I am {age} years old and live in {city}."
print(greeting)

# SOLUTION 1.3
print("\n--- Solution 1.3 ---")
price = 99.99
discount_percent = 15

discount_amount = price * (discount_percent / 100)
final_price = price - discount_amount
rounded_price = round(final_price, 2)
currency_format = f"${final_price:.2f}"

print(f"Original price: ${price}")
print(f"Discount: {discount_percent}%")
print(f"Discount amount: ${discount_amount:.2f}")
print(f"Final price: {currency_format}")

# SOLUTION 1.4
print("\n--- Solution 1.4 ---")
full_name = "John Doe"

first_name = full_name.split()[0]
last_name = full_name.split()[1]
initials = (first_name[0] + last_name[0]).upper()
reversed_name = full_name[::-1]

print(f"Full name: {full_name}")
print(f"First name: {first_name}")
print(f"Last name: {last_name}")
print(f"Initials: {initials}")
print(f"Reversed: {reversed_name}")

# SOLUTION 1.5
print("\n--- Solution 1.5 ---")

def get_type(value):
    if isinstance(value, int) and not isinstance(value, bool):
        return "integer"
    elif isinstance(value, float):
        return "float"
    elif isinstance(value, str):
        return "string"
    elif isinstance(value, bool):
        return "boolean"
    else:
        return "unknown"

test_values = [42, 3.14, "hello", True, [1, 2, 3], {"key": "value"}]
for val in test_values:
    print(f"Value: {val} | Type: {get_type(val)}")

print("\n" + "=" * 50)
print("Great job! Move on to 02_control_flow.py")
print("=" * 50)
