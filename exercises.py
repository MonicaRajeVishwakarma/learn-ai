import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Prepare synthetic training data
baby_sleep = np.array([
    5, 6, 7, 8, 9, 6.5, 7.5, 8.5
]).reshape(-1, 1)

mom_sleep = np.array([
    4, 5, 5.5, 6.5, 7, 5.2, 6.0, 6.8
])

# 2. Create and train model
model = LinearRegression()
model.fit(baby_sleep, mom_sleep)

# 3. Predict for 6.5 hours
prediction = model.predict([[6.5]])

print("Predicted mom sleep:", round(prediction[0], 2))
print("Coefficient:", round(model.coef_[0], 3))
print("Intercept:", round(model.intercept_, 3))

# 4. Visualize
plt.scatter(
    baby_sleep,
    mom_sleep,
    label="Training data"
)

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