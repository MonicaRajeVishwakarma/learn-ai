# Day 11 - Cleaning data

import pandas as pd

df = pd.read_csv("local_habits.csv")

#1. Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

#2. Convert 'sleep' column to numeric
df['sleep_hours'] =  df['sleep'].str.replace('h','').astype(float)

#3. Handle missing values
df.fillna(0, inplace=True)

#4. Preview clean data
print(df.head())
print(df.info())