import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Synthetic training data
# Feature (X): Baby sleep hours
baby_sleep = np.array([
    4.5, 5, 5.5, 6, 6.5, 7,
    7.5, 8, 8.5, 9, 9.5, 10
]).reshape(-1, 1)

# Target (y): Mom sleep category
# 0 = Low Sleep
# 1 = Adequate Sleep
mom_sleep_category = np.array([
    0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1
])

# Create classification model
model = LogisticRegression()

# Train the model
model.fit(baby_sleep, mom_sleep_category)

# Predict category for 8 hours
prediction = model.predict([[8]])

print("Predicted class:", prediction[0])

if prediction[0] == 0:
    print("Prediction: Low Sleep")
else:
    print("Prediction: Adequate Sleep")

prediction_5 = model.predict([[5]])

print("Prediction for 5 hours:", prediction_5[0])
print(
    "Category:",
    "Adequate Sleep" if prediction_5[0] == 1 else "Low Sleep"
)

probabilities = model.predict_proba([[8]])

print("Classes:", model.classes_)
print("Probabilities:", probabilities[0])

print(
    "Probability of Low Sleep:",
    round(probabilities[0][0] * 100, 2),
    "%"
)

print(
    "Probability of Adequate Sleep:",
    round(probabilities[0][1] * 100, 2),
    "%"
)

# Create input values for the probability curve
sleep_range = np.linspace(4, 11, 100).reshape(-1, 1)

# Probability of class 1
probabilities = model.predict_proba(sleep_range)[:, 1]

plt.scatter(
    baby_sleep,
    mom_sleep_category,
    label="Training data"
)

plt.plot(
    sleep_range,
    probabilities,
    color="red",
    label="Logistic Regression"
)

plt.axhline(
    y=0.5,
    color="gray",
    linestyle="--",
    label="Decision threshold"
)

plt.xlabel("Baby Sleep (hours)")
plt.ylabel("Probability of Class 1")
plt.title("Sleep Category Classification")
plt.legend()
plt.show()
