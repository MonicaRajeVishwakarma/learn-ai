# Day 4 - Loops Practice

# 1. For Loop - List
baby_items = ["diapers", "bottle", "blanket", "rattle"]
print("Loop through baby items")
for item in baby_items:
    print(item)

# 2. For loop - String
print("\nLoop through baby name")
for char in "Leo":
    print(char)

# 3. While loop
print("\nWhile loop counting")
count = 1
while count <=5:
    print(count)
    count += 1

#4. Break example
print("\nBreak example")
for item in baby_items:
    if item == "bottle":
        break
    print(item)

#5. Continue example
print("\nContinue Example")
for item in baby_items:
    if item == "bottle":
        continue
    print(item)
