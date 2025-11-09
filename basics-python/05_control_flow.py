# Lesson 5: Control Flow - Making Decisions
# ==========================================

# IF STATEMENTS - Making decisions
print("=== IF STATEMENTS ===")

age = 18

# Basic if statement
if age >= 18:
    print("You are an adult!")

# if-else statement
if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")

# if-elif-else statement
score = 85

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

print(f"Score: {score}, Grade: {grade}")

# Multiple conditions
temperature = 75
is_sunny = True

if temperature > 70 and is_sunny:
    print("Perfect weather for a picnic!")
elif temperature > 70 or is_sunny:
    print("Good weather, but not perfect.")
else:
    print("Stay indoors!")

# Nested if statements
age = 20
has_license = True

if age >= 16:
    print("You can get a learner's permit.")
    if has_license:
        print("You can drive!")
    else:
        print("You need to get a license first.")
else:
    print("You're too young to drive.")

# LOOPS - Repeating code
print("\n=== FOR LOOPS ===")

# Basic for loop
print("Counting from 1 to 5:")
for i in range(1, 6):  # range(1, 6) gives 1, 2, 3, 4, 5
    print(i)

# Loop through a list
fruits = ["apple", "banana", "orange"]
print("\nFruits:")
for fruit in fruits:
    print(f"- {fruit}")

# Loop with index
print("\nFruits with index:")
for i, fruit in enumerate(fruits):
    print(f"{i + 1}. {fruit}")

# WHILE LOOPS
print("\n=== WHILE LOOPS ===")

# Basic while loop
count = 1
print("Counting with while loop:")
while count <= 5:
    print(count)
    count += 1  # Same as count = count + 1

# While loop with user input
print("\nGuess the number game:")
secret_number = 7
guess = 0
attempts = 0

while guess != secret_number and attempts < 3:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You won!")

if guess != secret_number:
    print(f"Game over! The number was {secret_number}")

# LOOP CONTROL
print("\n=== LOOP CONTROL ===")

# break - exit the loop immediately
print("Numbers 1-10, stopping at 5:")
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# continue - skip to next iteration
print("\nEven numbers 1-10:")
for i in range(1, 11):
    if i % 2 != 0:  # If odd number
        continue    # Skip to next iteration
    print(i)

# else with loops (runs when loop completes normally)
print("\nSearching for number 6:")
for i in range(1, 6):
    if i == 6:
        print("Found 6!")
        break
else:
    print("6 not found in range 1-5")

# EXERCISE: Create a program that:
# 1. Asks the user for their age
# 2. If they're under 13, say "You're a child"
# 3. If they're 13-19, say "You're a teenager"
# 4. If they're 20-64, say "You're an adult"
# 5. If they're 65+, say "You're a senior"
# 6. Use a loop to ask 3 different people's ages
