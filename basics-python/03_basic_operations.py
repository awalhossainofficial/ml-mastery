# Lesson 3: Basic Operations
# ==========================

# ARITHMETIC OPERATIONS
print("=== ARITHMETIC OPERATIONS ===")

# Addition
result = 10 + 5
print("10 + 5 =", result)

# Subtraction
result = 10 - 5
print("10 - 5 =", result)

# Multiplication
result = 10 * 5
print("10 * 5 =", result)

# Division (always returns a float)
result = 10 / 5
print("10 / 5 =", result)

# Floor division (returns integer, rounds down)
result = 10 // 3
print("10 // 3 =", result)

# Modulus (remainder)
result = 10 % 3
print("10 % 3 =", result)

# Exponentiation (power)
result = 2 ** 3
print("2 ** 3 =", result)

# STRING OPERATIONS
print("\n=== STRING OPERATIONS ===")

first_name = "John"
last_name = "Doe"

# String concatenation (joining strings)
full_name = first_name + " " + last_name
print("Full name:", full_name)

# String repetition
greeting = "Hello! " * 3
print("Greeting:", greeting)

# String length
name_length = len(full_name)
print("Name length:", name_length)

# COMPARISON OPERATIONS
print("\n=== COMPARISON OPERATIONS ===")

a = 10
b = 5

print("a =", a, ", b =", b)
print("a > b:", a > b)    # Greater than
print("a < b:", a < b)    # Less than
print("a >= b:", a >= b)  # Greater than or equal
print("a <= b:", a <= b)  # Less than or equal
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal to

# LOGICAL OPERATIONS
print("\n=== LOGICAL OPERATIONS ===")

x = True
y = False

print("x =", x, ", y =", y)
print("x and y:", x and y)  # Both must be True
print("x or y:", x or y)    # At least one must be True
print("not x:", not x)      # Opposite of x

# ASSIGNMENT OPERATIONS
print("\n=== ASSIGNMENT OPERATIONS ===")

number = 10
print("Initial number:", number)

number += 5  # Same as: number = number + 5
print("After += 5:", number)

number -= 3  # Same as: number = number - 3
print("After -= 3:", number)

number *= 2  # Same as: number = number * 2
print("After *= 2:", number)

number /= 4  # Same as: number = number / 4
print("After /= 4:", number)

# EXERCISE: Try these calculations:
# 1. Calculate the area of a rectangle (length = 8, width = 5)
# 2. Calculate the circumference of a circle (radius = 3, use 3.14 for pi)
# 3. Check if 15 is greater than 10 and less than 20
# 4. Create two strings and concatenate them
