# Day 8 Notes – File Handling

## What Is File Handling?
File handling allows Python to **read**, **write**, and **modify** files.  
It’s essential for storing data, logs, and results, and you will use it a lot when building real projects.

Common operations:
- Reading files
- Writing files
- Appending new data
- Working with `with open(...)` for safe file access

---

## Opening a File
Use `open()` with a **mode**:
- `"r"` → read  
- `"w"` → write (overwrites file)  
- `"a"` → append  
- `"r+"` → read and write  

```python
file = open("notes.txt", "r")
content = file.read()
file.close()
```

## Using with open() (Recommended)
Automatically closes the file — safer and cleaner.
```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

## Writing to a File
"w" creates the file if it doesn’t exist.
```python
with open("baby_log.txt", "w") as file:
    file.write("Leo slept for 2 hours.\n")
```

## Appending to a File
"a" adds new content without deleting previous data.
```python
with open("baby_log.txt", "a") as file:
    file.write("He drank 120ml milk.\n")
```

## Reading Lines
Useful when processing logs or CSV-like data.
```python
with open("baby_log.txt", "r") as file:
    for line in file:
        print(line.strip())
```

## Summary

File handling lets you store, retrieve, and manage data across program runs.
It forms the foundation for projects like tracking habits, logs, or datasets, and will be essential later in your AI journey.



