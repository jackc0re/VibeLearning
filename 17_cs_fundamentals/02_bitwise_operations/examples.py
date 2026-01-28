"""
Bitwise Operations - Examples
=============================
Exploring AND, OR, XOR, NOT, and bit shifting.
"""

print("=" * 60)
print("BITWISE OPERATIONS - Examples")
print("=" * 60)

# =============================================================================
# BITWISE AND (&)
# =============================================================================
print("\n--- Bitwise AND (&) ---")
print("Output is 1 only if BOTH bits are 1\n")

# Visual representation
print("  1010  (decimal 10)")
print("& 1100  (decimal 12)")
print("  ----")
print(f"  {10 & 12:04b}  (decimal {10 & 12})")

# Truth table
print("\nAND Truth Table:")
print("  A | B | A & B")
print("  --|---|------")
for a in [0, 1]:
    for b in [0, 1]:
        result = a & b
        print(f"  {a} | {b} |   {result}")

# More examples
print("\nMore AND Examples:")
examples = [(15, 7), (255, 15), (0b11110000, 0b00001111)]
for a, b in examples:
    result = a & b
    print(f"  {a:3d} & {b:3d} = {result:3d}  ({a:08b} & {b:08b} = {result:08b})")

# =============================================================================
# BITWISE OR (|)
# =============================================================================
print("\n" + "=" * 60)
print("BITWISE OR (|)")
print("=" * 60)
print("Output is 1 if EITHER bit is 1\n")

# Visual representation
print("  1010  (decimal 10)")
print("| 1100  (decimal 12)")
print("  ----")
print(f"  {10 | 12:04b}  (decimal {10 | 12})")

# Truth table
print("\nOR Truth Table:")
print("  A | B | A | B")
print("  --|---|------")
for a in [0, 1]:
    for b in [0, 1]:
        result = a | b
        print(f"  {a} | {b} |   {result}")

# More examples
print("\nMore OR Examples:")
examples = [(5, 3), (16, 8), (0b10100000, 0b00010100)]
for a, b in examples:
    result = a | b
    print(f"  {a:3d} | {b:3d} = {result:3d}  ({a:08b} | {b:08b} = {result:08b})")

# =============================================================================
# BITWISE XOR (^)
# =============================================================================
print("\n" + "=" * 60)
print("BITWISE XOR (^)")
print("=" * 60)
print("Output is 1 if bits are DIFFERENT\n")

# Visual representation
print("  1010  (decimal 10)")
print("^ 1100  (decimal 12)")
print("  ----")
print(f"  {10 ^ 12:04b}  (decimal {10 ^ 12})")

# Truth table
print("\nXOR Truth Table:")
print("  A | B | A ^ B")
print("  --|---|------")
for a in [0, 1]:
    for b in [0, 1]:
        result = a ^ b
        print(f"  {a} | {b} |   {result}")

# XOR properties
print("\nXOR Properties:")
print(f"  A ^ A = 0:     42 ^ 42 = {42 ^ 42}")
print(f"  A ^ 0 = A:     42 ^ 0 = {42 ^ 0}")
print(f"  A ^ ~A = -1:   5 ^ ~5 = {5 ^ ~5}")

# =============================================================================
# BITWISE NOT (~)
# =============================================================================
print("\n" + "=" * 60)
print("BITWISE NOT (~)")
print("=" * 60)
print("Inverts all bits\n")

# In Python, ~n = -n-1 (two's complement with infinite bits)
print("In Python: ~n = -n - 1")
for n in [0, 1, 5, 10, 255]:
    result = ~n
    print(f"  ~{n:3d} = {result:4d}")

# If you want fixed-width behavior (like 8-bit)
print("\n8-bit masking (for fixed-width behavior):")
def not_8bit(n):
    return ~n & 0xFF

for n in [0, 1, 5, 10, 255]:
    result = not_8bit(n)
    print(f"  NOT {n:3d} (8-bit) = {result:3d}  ({n:08b} → {result:08b})")

# =============================================================================
# LEFT SHIFT (<<)
# =============================================================================
print("\n" + "=" * 60)
print("LEFT SHIFT (<<)")
print("=" * 60)
print("Shifts bits left, filling with zeros (multiply by 2)\n")

value = 5
print(f"Starting value: {value} ({value:08b})")
for i in range(1, 5):
    result = value << i
    print(f"  {value} << {i} = {result:2d}  ({result:08b})  [×{2**i}]")

# =============================================================================
# RIGHT SHIFT (>>)
# =============================================================================
print("\n" + "=" * 60)
print("RIGHT SHIFT (>>)")
print("=" * 60)
print("Shifts bits right, discarding low bits (divide by 2)\n")

value = 80
print(f"Starting value: {value} ({value:08b})")
for i in range(1, 5):
    result = value >> i
    print(f"  {value} >> {i} = {result:2d}  ({result:08b})  [÷{2**i}]")

# =============================================================================
# PRACTICAL APPLICATION: PERMISSION SYSTEM
# =============================================================================
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: PERMISSION SYSTEM")
print("=" * 60)

# Define permission bits
READ = 1 << 0      # 0b001 = 1
WRITE = 1 << 1     # 0b010 = 2
EXECUTE = 1 << 2   # 0b100 = 4

print(f"\nPermission Flags:")
print(f"  READ    = {READ:3d} ({READ:03b})")
print(f"  WRITE   = {WRITE:3d} ({WRITE:03b})")
print(f"  EXECUTE = {EXECUTE:3d} ({EXECUTE:03b})")

# Grant permissions
print("\n--- Granting Permissions ---")
user1 = READ | WRITE           # Can read and write
user2 = READ | EXECUTE         # Can read and execute
admin = READ | WRITE | EXECUTE # All permissions

print(f"User1 (Read|Write):   {user1:3d} ({user1:03b})")
print(f"User2 (Read|Execute): {user2:3d} ({user2:03b})")
print(f"Admin (All):          {admin:3d} ({admin:03b})")

# Check permissions
print("\n--- Checking Permissions ---")
def has_permission(user, permission):
    return (user & permission) != 0

print(f"User1 can READ?    {has_permission(user1, READ)}")
print(f"User1 can WRITE?   {has_permission(user1, WRITE)}")
print(f"User1 can EXECUTE? {has_permission(user1, EXECUTE)}")

# Add permission
print("\n--- Adding EXECUTE to User1 ---")
user1 |= EXECUTE  # Grant execute
print(f"User1 now: {user1:3d} ({user1:03b})")
print(f"User1 can EXECUTE? {has_permission(user1, EXECUTE)}")

# Remove permission
print("\n--- Removing WRITE from User1 ---")
user1 &= ~WRITE   # Revoke write
print(f"User1 now: {user1:3d} ({user1:03b})")
print(f"User1 can WRITE?   {has_permission(user1, WRITE)}")

# Toggle permission
print("\n--- Toggling EXECUTE on User1 ---")
user1 ^= EXECUTE  # Toggle execute
print(f"User1 now: {user1:3d} ({user1:03b})")
print(f"User1 can EXECUTE? {has_permission(user1, EXECUTE)}")

# =============================================================================
# PRACTICAL APPLICATION: FEATURE FLAGS
# =============================================================================
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: FEATURE FLAGS")
print("=" * 60)

# Define feature flags
FEATURE_DARK_MODE = 1 << 0    # 1
FEATURE_AUTO_SAVE = 1 << 1    # 2
FEATURE_BETA_UI = 1 << 2      # 4
FEATURE_ANALYTICS = 1 << 3    # 8

print("\nAvailable Features:")
print(f"  DARK_MODE  = {FEATURE_DARK_MODE}")
print(f"  AUTO_SAVE  = {FEATURE_AUTO_SAVE}")
print(f"  BETA_UI    = {FEATURE_BETA_UI}")
print(f"  ANALYTICS  = {FEATURE_ANALYTICS}")

# Enable some features
settings = FEATURE_DARK_MODE | FEATURE_AUTO_SAVE
print(f"\nInitial settings: {settings} ({settings:04b})")

# Check which features are enabled
def is_enabled(settings, feature):
    return (settings & feature) != 0

print("\nEnabled features:")
print(f"  Dark Mode:  {is_enabled(settings, FEATURE_DARK_MODE)}")
print(f"  Auto Save:  {is_enabled(settings, FEATURE_AUTO_SAVE)}")
print(f"  Beta UI:    {is_enabled(settings, FEATURE_BETA_UI)}")
print(f"  Analytics:  {is_enabled(settings, FEATURE_ANALYTICS)}")

# Enable beta UI
settings |= FEATURE_BETA_UI
print(f"\nAfter enabling Beta UI: {settings} ({settings:04b})")

# Disable dark mode
settings &= ~FEATURE_DARK_MODE
print(f"After disabling Dark Mode: {settings} ({settings:04b})")

# Toggle analytics twice (should end up same)
settings ^= FEATURE_ANALYTICS
print(f"After toggling Analytics: {settings} ({settings:04b})")
settings ^= FEATURE_ANALYTICS
print(f"After toggling again: {settings} ({settings:04b})")

# =============================================================================
# BIT MASKING
# =============================================================================
print("\n" + "=" * 60)
print("BIT MASKING")
print("=" * 60)

# Extract lower 4 bits
print("\n--- Extract Lower 4 Bits ---")
value = 0b10101111
mask = 0b00001111
result = value & mask
print(f"Value: {value:3d} ({value:08b})")
print(f"Mask:  {mask:3d} ({mask:08b})")
print(f"Result:{result:3d} ({result:08b})")

# Extract upper 4 bits
print("\n--- Extract Upper 4 Bits ---")
value = 0b10101111
mask = 0b11110000
result = (value & mask) >> 4
print(f"Value: {value:3d} ({value:08b})")
print(f"Mask:  {mask:3d} ({mask:08b})")
print(f"After AND and shift >> 4: {result}")

# Extract specific bit
print("\n--- Check if Bit 3 is Set ---")
value = 0b00001010  # Bit 3 (0-indexed from right) is 1
bit_position = 3
mask = 1 << bit_position
is_set = (value & mask) != 0
print(f"Value: {value:3d} ({value:08b})")
print(f"Bit {bit_position} mask: {mask:3d} ({mask:08b})")
print(f"Bit {bit_position} is {'SET' if is_set else 'NOT set'}")

# =============================================================================
# FAST MULTIPLY/DIVIDE BY POWERS OF 2
# =============================================================================
print("\n" + "=" * 60)
print("FAST OPERATIONS WITH SHIFTS")
print("=" * 60)

n = 25
print(f"\nStarting number: {n}")
print(f"Multiply by 2:  {n} << 1 = {n << 1}")
print(f"Multiply by 4:  {n} << 2 = {n << 2}")
print(f"Multiply by 8:  {n} << 3 = {n << 3}")
print(f"Divide by 2:    {n} >> 1 = {n >> 1}")
print(f"Divide by 4:    {n} >> 2 = {n >> 2}")
print(f"Divide by 8:    {n} >> 3 = {n >> 3}")

# =============================================================================
# SWAPPING WITHOUT TEMP VARIABLE
# =============================================================================
print("\n" + "=" * 60)
print("SWAPPING VALUES WITHOUT TEMP VARIABLE")
print("=" * 60)

a = 42
b = 17
print(f"\nBefore swap: a = {a}, b = {b}")

# XOR swap algorithm
a = a ^ b
b = a ^ b
a = a ^ b

print(f"After swap:  a = {a}, b = {b}")
print("(Note: This is a fun trick, but don't use it in production Python!)")

print("\n" + "=" * 60)
print("Examples complete! Try the exercises next.")
print("=" * 60)
