# Lesson 2: Variables and Data Types
# ==================================

# Variables are like labeled boxes that store information
# In Python, you don't need to declare variable types - Python figures it out!

# STRINGS - Text data (enclosed in quotes)
name = "Alice"
greeting = "Hello"
favorite_color = 'blue'  # Single or double quotes both work

print("Name:", name)
print("Greeting:", greeting)
print("Favorite color:", favorite_color)

# NUMBERS - Integer and Float
age = 25                    # Integer (whole number)
height = 5.6               # Float (decimal number)
temperature = -10          # Negative numbers work too

print("Age:", age)
print("Height:", height)
print("Temperature:", temperature)

# BOOLEAN - True or False
is_student = True
has_license = False

print("Is student:", is_student)
print("Has license:", has_license)

# You can change variable values
name = "Bob"  # Changed from "Alice" to "Bob"
age = age + 1  # Increased age by 1

print("Updated name:", name)
print("Updated age:", age)

# Variable naming rules:
# - Start with letter or underscore
# - Can contain letters, numbers, underscores
# - Case sensitive (Name and name are different)
# - Use descriptive names

# Good variable names:
user_name = "Charlie"
total_score = 100
is_logged_in = True

# Bad variable names (don't do this):
# 2name = "David"     # Can't start with number
# user-name = "Eve"    # Can't use hyphens
# class = "Math"       # Can't use Python keywords

# EXERCISE: Create variables for:
# 1. Your favorite movie
# 2. Your birth year
# 3. Whether you like pizza (True/False)
# 4. Your GPA (if you're a student)
# Then print all of them!
