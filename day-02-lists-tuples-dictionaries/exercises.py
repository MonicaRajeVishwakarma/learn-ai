# Day 2 - Lists, Tuples and Dictionaries

# 1. Lists
baby_items = ["diapers" , "bottle", "blanket", 1, True, 11.0]
print(baby_items)
print(baby_items[0])
print(baby_items[1])
print(baby_items[2])
# prints the last item.
print(baby_items[-1])

baby_items.append("rattle")
print("After append : ", baby_items)

baby_items.remove("diapers")
print("After remove : ", baby_items)

baby_items[0] = "wipes"
print("After replace : ", baby_items)

# 2. Tuples
baby_birth_info = ("Leo", "boy", 14.0)
print(baby_birth_info)
print(baby_birth_info[-1])
# baby_birth_info[1] = "Leon" TypeError: 'tuple' object does not support item assignment

# 3. Dictionaries
baby = {"name" : "Leo", "age_weeks" : 14, "favorite_toy": "rattle"}
print(baby)
print(baby["name"])
print(baby["age_weeks"])

# Add item
baby["likes_music"] = True
print("After adding : ", baby)

baby["age_weeks"] = 15
print("After update: ", baby)

del baby["favorite_toy"]
print("After del : ", baby)

# Looping through a Dictionary
for key, value in baby.items():
    print(key, ":", value)

