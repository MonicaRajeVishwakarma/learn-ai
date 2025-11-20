# Day 06 - Modules and Imports

# 1. Importing a built-in module
import math
from math import factorial
print("square root of 36:",math.sqrt(36))
print("value of pi",math.pi)

# 2. Importing specific functions
print("Factorial of 5 using specific function",factorial(5))
print("Factorial of 5 using main module",math.factorial(5))

#3. Using alias
import math as m
print("Cosine of 0 :", m.cos(0))

#4. Importing your own module
import my_utils
print(my_utils.greet("Monica"))

# 5. Using datetime module
print("\nUsing datetime module")
from datetime import date, datetime, timedelta
today = date.today()
print("Today's date",today)

now = datetime.now()
print("Current time",now)

future_date = today + timedelta(days=7)
print("Future date",future_date)

formatted_date = today.strftime("%A, %d %B %Y")
print("Formatted date",formatted_date)

# 6. Using random module
print("\nUsing random module")
import random
random_int = random.randint(0,10)
print("Random integer", random_int)

random_choice = random.choice(["diapers", "pacifier", "bottle"])
print("Random choice",random_choice)

items = ["toys", "food", "clothes"]
random.shuffle(items)
print("Shuffled items",items)

