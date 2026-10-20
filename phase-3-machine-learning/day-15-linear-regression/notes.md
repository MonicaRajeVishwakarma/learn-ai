# Day 15 — Linear Regression

## Learning Objective

Understand how Linear Regression learns a relationship between numerical inputs and outputs, makes predictions, and visualizes the fitted line.

> **Note:** All sleep data in this exercise is synthetic and used only to learn machine learning concepts. It is not a reliable sleep or health recommendation.

## 1. What Is Linear Regression?

Linear Regression is a **supervised machine learning** algorithm that predicts a continuous numerical value.

In the **New Mom Sleep Pattern Recommender** learning example:

- **Feature (`X`):** Baby sleep duration (hours)
- **Target (`y`):** Mom sleep duration (hours)
- **Model:** `LinearRegression()` from scikit-learn

The model learns a straight-line relationship:

```text
y = mx + b
```

- `m` is the **coefficient (slope)**.
- `b` is the **intercept**.

## 2. Preparing Training Data

```python
import numpy as np

# Synthetic examples only
baby_sleep = np.array([5, 6, 7, 8, 9, 6.5, 7.5, 8.5]).reshape(-1, 1)
mom_sleep = np.array([4, 5, 5.5, 6.5, 7, 5.2, 6.0, 6.8])
```

Each value in `baby_sleep` corresponds to the value at the same position in `mom_sleep`.

### Why Is `reshape(-1, 1)` Required?

Scikit-learn expects input features (`X`) to be a **2D array** with shape:

```text
(number_of_samples, number_of_features)
```

For example:

```python
np.array([5, 6, 7, 8, 9]).shape
# (5,)

np.array([5, 6, 7, 8, 9]).reshape(-1, 1).shape
# (5, 1)
```

- `-1` asks NumPy to determine the number of rows automatically.
- `1` means there is **one input feature** per example.
- Our updated dataset has **8 samples and 1 feature**, so its shape is `(8, 1)`.
- The target `y` can remain a 1D array when predicting one value per sample.

## 3. Training the Model

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(baby_sleep, mom_sleep)
```

- `LinearRegression()` creates the model.
- `fit(X, y)` trains it on the provided examples.

## 4. Making a Prediction

```python
prediction = model.predict([[6.5]])
print("Predicted mom sleep:", round(prediction[0], 2))
```

I changed the prediction input from `7.5` to `6.5` hours. The prediction changes because the model evaluates its learned line at a different input value.

The prediction input is written as `[[6.5]]` because scikit-learn expects a 2D feature matrix: **one sample with one feature**.

## 5. Coefficient and Intercept

```python
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
```

### Coefficient (`model.coef_[0]`)

The coefficient is the slope of the learned line. It describes how much **predicted** mom sleep changes when baby sleep increases by one hour.

For example, if the coefficient is `0.75`, the model predicts **0.75 additional hours of mom sleep** for one additional hour of baby sleep, assuming the fitted linear relationship.

This is an association in the synthetic dataset, **not proof of causation**.

### Intercept (`model.intercept_`)

The intercept is the predicted mom sleep duration when baby sleep is `0` hours. This is part of the mathematical equation but may not be meaningful in a real-world sleep scenario.

## 6. Visualizing the Regression Line

```python
import matplotlib.pyplot as plt

plt.scatter(baby_sleep, mom_sleep, label="Training data")
plt.plot(
    baby_sleep,
    model.predict(baby_sleep),
    color="red",
    label="Regression line"
)

plt.xlabel("Baby Sleep (hours)")
plt.ylabel("Mom Sleep (hours)")
plt.title("Linear Regression: Sleep Pattern")
plt.legend()
plt.show()
```

- **Scatter points:** Individual training examples.
- **Red line:** The relationship learned by Linear Regression.
- The line does not have to pass through every point. Linear Regression minimizes the sum of squared prediction errors.

## 7. What I Practiced

- [x] Changed the prediction input from `7.5` to `6.5`.
- [x] Added three synthetic training examples.
- [x] Retrained the model using eight examples.
- [x] Printed and interpreted the coefficient and intercept.
- [x] Visualized the training points and regression line.
- [x] Understood why `reshape(-1, 1)` is necessary.

## Key Takeaways

1. **Linear Regression** predicts continuous numerical values.
2. `fit()` trains a model; `predict()` uses it to estimate outputs.
3. Input features (`X`) must be 2D for scikit-learn.
4. The **coefficient** describes the slope; the **intercept** describes where the line crosses the y-axis.
5. A fitted model is not automatically a reliable model. We will learn how to evaluate predictions in **Day 17**.

## Next: Day 16 — Classification

Learn how to predict categories instead of continuous numerical values.
