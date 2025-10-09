# Lesson 4: Input and Output
# ==========================

# GETTING INPUT FROM USER
print("=== GETTING USER INPUT ===")

# The input() function gets text from the user
name = input("What's your name? ")
print("Hello,", name + "!")

# Input always returns a string, even for numbers
age_input = input("How old are you? ")
print("You entered:", age_input, "(this is a string)")

# To convert string to number, use int() or float()
age = int(age_input)  # Convert to integer
print("Your age as a number:", age)
print("Next year you'll be:", age + 1)

# You can do the conversion in one line
height = float(input("What's your height in feet? "))
print("Your height is:", height, "feet")

# FORMATTING OUTPUT
print("\n=== FORMATTING OUTPUT ===")

# String formatting with f-strings (Python 3.6+)
name = "Alice"
age = 25
score = 87.5

# f-string formatting
print(f"Name: {name}, Age: {age}, Score: {score}")

# You can format numbers
print(f"Score: {score:.1f}")  # 1 decimal place
print(f"Score: {score:.2f}")  # 2 decimal places

# Multiple ways to format strings
print("Name: {}, Age: {}".format(name, age))  # .format() method
print("Name: %s, Age: %d" % (name, age))      # % formatting (older style)

# CONDITIONAL INPUT
print("\n=== CONDITIONAL INPUT ===")

# Ask for a number and check if it's valid
while True:
    try:
        number = int(input("Enter a number between 1 and 10: "))
        if 1 <= number <= 10:
            print(f"Great! You entered: {number}")
            break
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("Please enter a valid number!")

# MULTIPLE INPUTS
print("\n=== MULTIPLE INPUTS ===")

# Get multiple values at once
print("Enter two numbers separated by a space:")
numbers = input().split()  # Split by spaces
num1 = int(numbers[0])
num2 = int(numbers[1])
print(f"Sum: {num1 + num2}")

# Or get them separately
print("Enter your favorite colors (press Enter after each):")
color1 = input("Color 1: ")
color2 = input("Color 2: ")
color3 = input("Color 3: ")
print(f"Your favorite colors are: {color1}, {color2}, and {color3}")

# EXERCISE: Create a simple calculator that:
# 1. Asks for two numbers
# 2. Asks what operation to perform (+, -, *, /)
# 3. Performs the operation and shows the result
# 4. Handles division by zero gracefully
