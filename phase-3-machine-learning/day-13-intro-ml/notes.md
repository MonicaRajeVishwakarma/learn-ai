# Day 13 - Intro to Machine Learning

## What I learned

### 1. Machine Learning
- Machine Learning is a system that learns patterns from data, instead of being explicitly programmed with rules.
- Traditional programming: rules + input = output
- Machine Learning : input + output → rules*
    - *The model learns the rules automatically. 
    - This shift is the foundation of all modern AI.

### Supervised Learning
- Supervised learning is the type of ML where:
- You give the model inputs (X)
- You give the model correct answers (y)
- The model learns a mapping: f(x) ≈ y
  - | Sleep Hours | Mood |
    |-------------|------|
    | 8           | good |
    | 6           | good |
    | 4           | bad  |
    | 2           | bad  |
- You give the model this labeled data, it learns the pattern.
- This is the core technique behind:
  - baby sleep prediction 
  - sentiment analysis 
  - fraud detection 
  - medical diagnosis 
  - image classification 
  - speech recognition
- Supervised learning is 80% of real-world ML.

### 2. Regression vs Classification
#### Regression
Predict numeric values
Example tasks:
- predict sleep hours 
- predict feeding amount
- predict house prices
- predict temperature

Output: y = 7.5 hours

#### Classification
Predict categories
Example tasks:

- predict baby mood
- predict if sleep tonight will be good/bad 
- predict email spam/not spam
- predict disease present/not present

Output: y = "good"

### 3. How ML Models Learn
Let’s say you want to predict sleep hours from feeding amount.
1. Model starts with a random guess
2. Compares its guess to the true value 
3. Computes error 
4. Adjusts itself to reduce error 
5. Repeats this over and over

This process is called training.
Every ML algorithm, from linear regression to deep learning, follows this idea.

### 4. A simple example (You’ll run this)

Dataset:
  - | Hours | Studied	Score |
    |-------|---------------|
    | 1     | 40            |
    | 2     | 50            |
    | 3     | 60            |
    | 4     | 65            |
  - | 4     | 80            |
- We want to predict the score for 6 hours of study.
- Algorithm: Linear Regression
This fits a straight line through the points.
## What I practiced

## Takeaway
By now you should understand:
- What ML actually is
- What supervised learning means
- Difference between regression & classification
- How models learn patterns
- How to train your first ML model
- How predictions work

This is the foundation of everything else you will build.