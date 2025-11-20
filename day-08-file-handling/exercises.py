# Day 08 - File handling

# 1. Write to a file
with open("baby_log.txt","w") as file:
    file.write("Day 1 : Leo smiled today!\n")
    file.write("Day 2 : Leo slept 6 hours.\n")


# 2. Read from a file
with open("baby_log.txt","r") as file:
    print("Reading log")
    print(file.read())

# 3. Append to a file
with open("baby_log.txt","a") as file:
    file.write("Day 3: Leo tried rolling over!\n")

# 4.  Read line by line
with open("baby_log.txt", "r") as file:
    print("\nReading line by line:")
    for line in file:
        print(line.strip())