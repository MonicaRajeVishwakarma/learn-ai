# Day 07 -  Error Handling

# 1. Handling a ZeroDivisionError
print("Exercise 1:")
try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero")

# 2. Handling multiple exceptions
print("\nExercise 2:")
try:
    num = input("Enter a number:")

