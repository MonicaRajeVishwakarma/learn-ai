# Day 16 — Classification with Logistic Regression

## What I Learned

Classification is a supervised machine learning technique
used to predict categories rather than continuous values.

## Regression vs Classification

- Regression predicts a numerical value.
- Classification predicts a category or class.

## My Project Example

New Mom Sleep Pattern Recommender

- Feature (X): Baby sleep duration in hours
- Target (y): Mom sleep category
- Class 0: Low Sleep
- Class 1: Adequate Sleep

These are synthetic examples with illustrative labels,
not medically validated sleep recommendations.

## My Experiment: 7 vs 8 Hours

For 7 hours of baby sleep:
- Class 0 probability: 58.98%
- Class 1 probability: 41.02%
- Predicted class: 0 (Low Sleep)

For 8 hours of baby sleep:
- Class 0 probability: 25.17%
- Class 1 probability: 74.83%
- Predicted class: 1 (Adequate Sleep)

### What I Learned

Logistic Regression estimates class probabilities.

The model predicts class 1 when its probability is
at least 50% (using the default binary threshold).

Changing the input changes the probabilities and
can change the predicted class.

## Why Logistic Regression?

Logistic Regression is a classification algorithm because
it models the probability of belonging to a class.

It uses a sigmoid function to transform a numerical score
into a probability between 0 and 1.

## Important Methods

### model.fit(X, y)

Trains the model using input features and known labels.

### model.predict(X)

Returns the predicted class.

### model.predict_proba(X)

Returns the estimated probability for each class.

### model.classes_

Shows the class labels in the order used by predict_proba().

## What I Observed

- For 8 hours of baby sleep, the model predicts class 1.
- For 5 hours of baby sleep, the model predicts class 0.
- The predicted probabilities change with the input.
- The probability curve is S-shaped rather than a straight line.

## Key Takeaway

Linear Regression predicts numerical values.

Logistic Regression predicts categories using learned
class probabilities.

The model is trained on synthetic data, so its outputs
should not be used for real-world sleep decisions.
