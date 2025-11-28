# Day 11 – Cleaning & Transforming Data

## Convert 'date' column to datetime
```python
df['date'] = pd.to_datetime(df['date'])
```

## Convert numeric columns if stored as strings
```python
df['sleep_hours'] = df['sleep'].str.replace('h','').astype(float)
```

## Handle missing values
```python
df.fillna(0, inplace=True)   # Replace NaN with 0
df.dropna(inplace=True)      # Or drop rows with NaN
```

## Key Points
1. Always ensure correct data types
2. Handle missing or malformed data
3. Transform data to make analysis easier

