# Day 14 Notes – Feature Engineering

Feature engineering means converting raw data into usable numerical features for machine learning.

---

## 1. Cleaning Numerical Columns

Raw examples:
- `"8h"`  
- `"7.5 hours"`  
- `"6H"`  

Convert using regex:
```python
df['baby_sleep_hours'] = df['baby_sleep'].astype(str).str.extract(r'(\d+\.?\d*)').astype(float)
```

## 2. Encoding Categorical Data

Models can't understand text like:
- `happy`  
- `tired`  
- `overwhelmed` 

Convert to numbers:
```python
df['mood_encoded'] = df['mood'].astype('category').cat.codes
```