# Day 13 - Intro to Machine Learning (New Mom Sleep Pattern Recommender)

import numpy as np
from sklearn.linear_model import LinearRegression

"""
Goal:
Understand ML basics using a tiny model that predicts
mom sleep based on baby sleep patterns.

This is NOT the full recommender, just the intuition.
"""

# -------------------------------
# 1. Example dataset (simple & small)
# -------------------------------
# baby_sleep_hours → mom_sleep_hours (target)

baby_sleep = np.array([7, 8, 6.5, 9, 5, 8.5, 7.2]).reshape(-1, 1)
mom_sleep  = np.array([6, 6.8, 5.5, 7.5, 4, 6.9, 6.2])

# -------------------------------
# 2. Train a simple ML model
# -------------------------------
model = LinearRegression()
model.fit(baby_sleep, mom_sleep)

# -------------------------------
# 3. Make predictions
# -------------------------------
prediction = model.predict([[8]])  # Baby sleeps 8 hours
print("Prediction for baby sleeping 8 hours:", round(prediction[0], 2), "hours")

print("\n Model coefficient (impact of baby sleep):", model.coef_[0])
print(" Model intercept:", round(model.intercept_, 2))

# -------------------------------
# 4. Interpretation
# -------------------------------
print("\n Interpretation:")
print(" For every extra hour the baby sleeps, the model estimates how much more the mom can sleep.")
print(" This forms the foundation of the AI-Powered New Mom Sleep Pattern Recommender.")
