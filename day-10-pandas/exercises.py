# Day 10 - Pandas

import pandas as pd

#1. Load CSV
df = pd.read_csv("data/habits.csv")

#2. Preview first 5 rows
print("First 5 rows",df.head())