"""
Number Systems - Examples
=========================
Exploring decimal, binary, octal, and hexadecimal number systems.
"""

print("=" * 60)
print("NUMBER SYSTEMS - Examples")
print("=" * 60)

# =============================================================================
# DECIMAL (BASE-10) - What humans use
# =============================================================================
print("\n--- Decimal (Base-10) ---\n")

decimal_number = 42
print(f"Decimal number: {decimal_number}")
print(f"Type: {type(decimal_number)}")

# Breaking down a decimal number
number = 253
print(f"\nBreaking down {number}:")
print(f"  2 × 100 = {2 * 100}")
print(f"  5 × 10  = {5 * 10}")
print(f"  3 × 1   = {3 * 1}")
print(f"  Sum: {2 * 100 + 5 * 10 + 3 * 1}")

# =============================================================================
# BINARY (BASE-2) - What computers use
# =============================================================================
print("\n" + "=" * 60)
print("BINARY (Base-2)")
print("=" * 60)

# Converting decimal to binary
print("\n--- Converting Decimal to Binary ---")
for i in range(0, 17):
    binary = bin(i)
    print(f"Decimal {i:2d} = Binary {binary}")

# Converting binary to decimal
print("\n--- Converting Binary to Decimal ---")
binary_strings = ['0b1010', '0b1111', '0b10000', '0b11111111']
for b in binary_strings:
    decimal = int(b, 2)
    print(f"Binary {b} = Decimal {decimal}")

# Binary place values
print("\n--- Binary Place Values ---")
binary_num = 0b101101  # Binary literal in Python
print(f"Binary 101101 = Decimal {binary_num}")
print("Breakdown:")
print("  Position:  5    4    3    2    1    0")
print("  Value:     32   16   8    4    2    1")
print("  Bits:      1    0    1    1    0    1")
print(f"  Calc: 32 + 0 + 8 + 4 + 0 + 1 = {32 + 8 + 4 + 1}")

# =============================================================================
# OCTAL (BASE-8)
# =============================================================================
print("\n" + "=" * 60)
print("OCTAL (Base-8)")
print("=" * 60)

# Converting decimal to octal
print("\n--- Decimal to Octal ---")
for i in range(0, 17):
    octal = oct(i)
    print(f"Decimal {i:2d} = Octal {octal}")

# Octal to decimal
print("\n--- Octal to Decimal ---")
octal_values = ['0o10', '0o17', '0o77', '0o100']
for o in octal_values:
    decimal = int(o, 8)
    print(f"Octal {o} = Decimal {decimal}")

# Binary to Octal conversion
print("\n--- Binary ↔ Octal Conversion ---")
print("Each octal digit = 3 binary digits")
print("Binary:  001 010 111 100")
print("Octal:     1   2   7   4  →  0o1274")

# =============================================================================
# HEXADECIMAL (BASE-16)
# =============================================================================
print("\n" + "=" * 60)
print("HEXADECIMAL (Base-16)")
print("=" * 60)

# Hex digits explained
print("\n--- Hex Digits ---")
print("Decimal: 0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15")
print("Hex:     0  1  2  3  4  5  6  7  8  9  A   B   C   D   E   F")

# Converting decimal to hex
print("\n--- Decimal to Hexadecimal ---")
for i in [0, 9, 10, 15, 16, 255, 256, 4095]:
    hex_val = hex(i)
    print(f"Decimal {i:4d} = Hex {hex_val}")

# Hex to decimal
print("\n--- Hex to Decimal ---")
hex_values = ['0xFF', '0x100', '0xABC', '0xDEADBEEF']
for h in hex_values:
    decimal = int(h, 16)
    print(f"Hex {h} = Decimal {decimal}")

# Binary to Hex conversion
print("\n--- Binary ↔ Hex Conversion ---")
print("Each hex digit = 4 binary digits (1 nibble)")
print("Binary:  1101 1011 1111 0000")
print("Hex:        D    B    F    0  →  0xDBF0")

# Real-world: Colors in hex
print("\n--- Real World: Color Codes ---")
colors = {
    'Red': 0xFF0000,
    'Green': 0x00FF00,
    'Blue': 0x0000FF,
    'White': 0xFFFFFF,
    'Black': 0x000000,
    'Yellow': 0xFFFF00,
    'Purple': 0x800080,
}
for name, value in colors.items():
    hex_str = f"#{value:06X}"
    print(f"{name:10s} = {hex_str}")

# =============================================================================
# PYTHON CONVERSION FUNCTIONS
# =============================================================================
print("\n" + "=" * 60)
print("PYTHON CONVERSION FUNCTIONS")
print("=" * 60)

test_number = 255

print(f"\nStarting number: {test_number}")
print(f"\nTo Binary:   bin({test_number}) = {bin(test_number)}")
print(f"To Octal:    oct({test_number}) = {oct(test_number)}")
print(f"To Hex:      hex({test_number}) = {hex(test_number)}")

print("\n--- Converting back to decimal ---")
print(f"int('0b11111111', 2) = {int('0b11111111', 2)}")
print(f"int('0o377', 8)      = {int('0o377', 8)}")
print(f"int('0xff', 16)      = {int('0xff', 16)}")

# Alternative: without prefix
print("\n--- Without prefix ---")
print(f"int('11111111', 2)   = {int('11111111', 2)}")
print(f"int('377', 8)        = {int('377', 8)}")
print(f"int('FF', 16)        = {int('FF', 16)}")

# Removing prefixes from strings
print("\n--- Removing Prefixes ---")
bin_str = bin(255)  # '0b11111111'
oct_str = oct(255)  # '0o377'
hex_str = hex(255)  # '0xff'

print(f"Original: {bin_str}, {oct_str}, {hex_str}")
print(f"Without prefix: {bin_str[2:]}, {oct_str[2:]}, {hex_str[2:]}")

# Formatting options
print("\n--- Formatting Options ---")
print(f"hex(255) with uppercase: {format(255, 'X')}")
print(f"hex(255) with padding:   {format(255, '04X')}")
print(f"binary with padding:     {format(5, '08b')}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: File permissions (octal)
print("\n--- Example 1: Unix File Permissions ---")
print("Permission 755 = Owner: RWX(7), Group: RX(5), Others: RX(5)")
print(f"7 = {oct(7)} = Binary {format(7, '03b')} = RWX")
print(f"5 = {oct(5)} = Binary {format(5, '03b')} = R-X")

# Example 2: Memory addresses
print("\n--- Example 2: Memory Addresses ---")
variable = "Hello, World!"
address = id(variable)
print(f"Variable value: {variable}")
print(f"Memory address (decimal): {address}")
print(f"Memory address (hex):     {hex(address)}")

# Example 3: Binary flags
print("\n--- Example 3: Binary Flags ---")
READ = 0b001   # 1
WRITE = 0b010  # 2
EXECUTE = 0b100  # 4

permissions = READ | WRITE  # 0b011 = 3
print(f"READ permission:    {bin(READ)} = {READ}")
print(f"WRITE permission:   {bin(WRITE)} = {WRITE}")
print(f"EXECUTE permission: {bin(EXECUTE)} = {EXECUTE}")
print(f"READ | WRITE:       {bin(permissions)} = {permissions}")

# Example 4: Bit masks
print("\n--- Example 4: Checking Bits ---")
flags = 0b10110110  # 182
mask = 0b00001000   # Check if bit 3 is set
result = flags & mask
print(f"Flags: {bin(flags)}")
print(f"Mask:  {bin(mask)}")
print(f"AND:   {bin(result)} ({'Bit is SET' if result else 'Bit is NOT set'})")

# =============================================================================
# CONVERSION ALGORITHMS (Manual Implementation)
# =============================================================================
print("\n" + "=" * 60)
print("MANUAL CONVERSION ALGORITHMS")
print("=" * 60)

# Decimal to binary manually
def decimal_to_binary(n):
    """Convert decimal to binary manually."""
    if n == 0:
        return "0"

    binary = []
    while n > 0:
        remainder = n % 2
        binary.append(str(remainder))
        n = n // 2

    # Reverse to get correct order
    return ''.join(reversed(binary))

print("\n--- Manual Decimal to Binary ---")
for num in [5, 10, 42, 255]:
    manual = decimal_to_binary(num)
    builtin = bin(num)[2:]
    print(f"Decimal {num:3d} → Binary {manual:8s} (builtin: {builtin})")

# Decimal to hex manually
def decimal_to_hex(n):
    """Convert decimal to hexadecimal manually."""
    if n == 0:
        return "0"

    hex_digits = "0123456789ABCDEF"
    hex_result = []

    while n > 0:
        remainder = n % 16
        hex_result.append(hex_digits[remainder])
        n = n // 16

    return ''.join(reversed(hex_result))

print("\n--- Manual Decimal to Hex ---")
for num in [10, 255, 4095, 65535]:
    manual = decimal_to_hex(num)
    builtin = hex(num)[2:].upper()
    print(f"Decimal {num:5d} → Hex {manual:4s} (builtin: {builtin})")

print("\n" + "=" * 60)
print("Examples complete! Try the exercises next.")
print("=" * 60)
