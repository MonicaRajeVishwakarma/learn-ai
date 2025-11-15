# Day 4 Notes – Loops

## For Loop (List)
```python
baby_items = ["diapers", "bottle", "blanket", "rattle"]
for item in baby_items:
    print(item)
```


## For Loop (String)
```python
for char in "Leo":
    print(char)
```


## While Loop
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```


## Break
```python
for item in baby_items:
    if item == "blanket":
        break
    print(item)
```

## Continue
```python
for item in baby_items:
    if item == "bottle":
        continue
    print(item)
```