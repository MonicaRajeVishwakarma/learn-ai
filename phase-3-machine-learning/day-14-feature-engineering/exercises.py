# Day 14 – Feature Engineering Exercises

import pandas as pd
import numpy as np

# ------------------------------
# 1. Load raw dataset
# ------------------------------
df = pd.read_csv("../../data/habits.csv")
print("🔹 Raw Data Loaded\n", df.head())


# ------------------------------
# 2. Clean numeric columns
# ------------------------------

# Baby sleep (convert "8h", "7.5 hours" → 8.0, 7.5)
if 'baby_sleep' in df.columns:
    df['baby_sleep_hours'] = (
        df['baby_sleep']
        .astype(str)
        .str.extract(r'(\d+\.?\d*)')
        .astype(float)
    )

# Mom sleep
if 'mom_sleep' in df.columns:
    df['mom_sleep_hours'] = (
        df['mom_sleep']
        .astype(str)
        .str.extract(r'(\d+\.?\d*)')
        .astype(float)
    )


# ------------------------------
# 3. Clean feeding & crying columns
# ------------------------------
numeric_cols = ['feeding_ml', 'crying_min', 'caffeine_mg', 'stress']

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')


# ------------------------------
# 4. Encode categorical columns
# ------------------------------
if 'mood' in df.columns:
    df['mood_encoded'] = df['mood'].astype('category').cat.codes


# ------------------------------
# 5. Create new ML features
# ------------------------------
if 'baby_sleep_hours' in df.columns and 'mom_sleep_hours' in df.columns:
    df['sleep_difference'] = df['baby_sleep_hours'] - df['mom_sleep_hours']
    df['sleep_ratio'] = df['baby_sleep_hours'] / (df['mom_sleep_hours'] + 1)

# Example: fatigue score
if all(col in df.columns for col in ['stress', 'caffeine_mg', 'baby_sleep_hours']):
    df['fatigue_index'] = df['stress'] + (df['caffeine_mg'] / 50) - df['baby_sleep_hours']


# ------------------------------
# 6. Handle missing values
# ------------------------------
df = df.fillna(df.mean(numeric_only=True))


# ------------------------------
# 7. Save ML-ready dataset
# ------------------------------
df.to_csv("ml_ready.csv", index=False)
print("\n✅ Saved ML-ready dataset as ml_ready.csv")


# ------------------------------
# 8. Exercises for You
# ------------------------------
print("\n📝 Your tasks:")
print("1. Add a new feature: baby_sleep_quality (1–5 scale).")
print("2. Add day_of_week extracted from date.")
print("3. Normalize caffeine_mg (between 0 and 1).")
print("4. Create a 'stress_level' category (low/medium/high).")
print("5. Plot correlation between all new features (optional).")