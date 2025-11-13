# Day 2 Notes – Lists, Tuples, and Dictionaries

## Lists
A list is an ordered, changeable collection of items.
- It can have heterogeneous items. 
- Lists are used everywhere,  from holding numbers in machine learning datasets to storing words in natural language processing tasks.
- Think of a list like a shopping list — you can add or remove things anytime.
- Following operations can be performed on lists
  1. Add 
  2. Remove
  3. Modify
  4. Iterate

## Example
```python
baby_items = ["diapers", "bottle", "blanket",1, True, 11.0]
baby_items.append("rattle")
print(baby_items)
print(baby_items[0])
print(baby_items[-1]) # Prints the last element
```

## Tuples
A tuple is like a list, but it cannot be changed (immutable).
- It’s used for fixed data, information that should stay constant.
- Once created, you can read from it, but not modify it.
- Think of a tuple as a birth record, once it’s written, it’s permanent.
- Tuples are used when you want to protect data from accidental changes, for example, a model’s configuration, coordinates, or constant parameters in AI code.
```python
baby_birth_info = ("Leo", "boy", 14.0)
print(baby_birth_info)
```

## Dictionaries
A dictionary stores data as key–value pairs.
- Each key is unique, and points to a value.
- It’s like a baby’s record card, each label (key) has information (value).
```python
baby = {"name": "Leo", "age_weeks": 14}
baby["favorite_toy"] = "rattle"
print(baby)
```

## For Loop – List
```python
for item in baby_items:
    print("Essential item:", item)
```    

## For Loop – Dictionary
```python
for key, value in baby.items():
    print(key, ":", value)
```