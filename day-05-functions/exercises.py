# Day 5 - Functions

# 1. Basic functions
def greet():
    print("Hello Monica")

greet()

# 2. Function with parameters
def greet_baby(name):
    print("Hello",name)

greet_baby("Leo")

#3. Function that returns a value
def add(a, b):
    return a+b

total = add(2,4)
print("Addition is", total)

#4. Function with default parameter
def welcome(name="Leo"):
    print("Welcome,",name)

welcome()
welcome("Monica")

#5. small practice function
def baby_age_in_months(weeks):
    return weeks/4

print("Leo's age in months",baby_age_in_months(15))




