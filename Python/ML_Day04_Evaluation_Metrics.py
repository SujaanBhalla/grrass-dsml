# ==========================================================
# Machine Learning
# Day 4
# Topic: Train-Test Split & Evaluation Metrics
# ==========================================================

# Train-Test Split:
# Before building a model, we divide the dataset into two parts:
# 1. Training Set (usually 80%): Used to train the model
# 2. Testing Set (usually 20%): Used to evaluate model performance
#
# Why?
# - To check if the model generalizes well on unseen data
# - To avoid overfitting (model memorizing the training data)
# - To get a realistic estimate of model performance


# ==========================================================
# EXAMPLE 1: Train-Test Split
# ==========================================================

from sklearn.model_selection import train_test_split

# Sample data
x = [[2], [3], [4], [5], [6]]  # input | features
y = [30, 40, 50, 60, 70]  # output | target

# Split dataset
# test_size=0.2 means 20% data for testing, 80% for training
# random_state=42 ensures reproducible results
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

print("=== Train-Test Split Results ===")
print("\nTraining features:")
print(x_train)

print("\nTesting features:")
print(x_test)

print("\nTraining labels:")
print(y_train)

print("\nTesting labels:")
print(y_test)


# ==========================================================
# EXAMPLE 2: Linear Regression with Train-Test Split
# ==========================================================

import pandas as pd
from sklearn.linear_model import LinearRegression

# Create sample dataset
data = {
    "experience": [1, 2, 3, 4, 5],
    "salary": [3, 5, 7, 9, 11]
}

df = pd.DataFrame(data)

x = df[["experience"]]
y = df["salary"]

# Train model
model = LinearRegression()
model.fit(x, y)

# Make prediction
new_data = pd.DataFrame({
    "experience": [6]
})

pred = model.predict(new_data)

print("\n=== Linear Regression Prediction ===")
print(f"Predicted salary for 6 years experience: {pred[0]:.2f}")


# ==========================================================
# EVALUATION METRICS:
# ==========================================================

# Evaluation metrics are used to check how good or bad a machine learning model is.
# They compare the actual values with the predicted values.

import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Sample actual and predicted values
y_true = np.array([50, 60, 75, 90, 100])  # Actual values
y_pred = np.array([52, 58, 78, 88, 105])  # Predicted values

print("\n=== EVALUATION METRICS ===")
print(f"Actual values:    {y_true}")
print(f"Predicted values: {y_pred}")


# ==========================================================
# 1. MAE (Mean Absolute Error):
# ==========================================================

# MAE tells the average absolute difference between actual and predicted values.
# Formula: MAE = (1/n) * sum(|actual - predicted|)
#
# Interpretation:
# - Lower MAE means better model performance
# - Easy to understand because it is in the same unit as the target variable
# - Does not penalize large errors heavily

mae = mean_absolute_error(y_true, y_pred)

print(f"\n1. MAE (Mean Absolute Error): {mae:.2f}")
print("   -> Average error between actual and predicted values")


# ==========================================================
# 2. MSE (Mean Squared Error):
# ==========================================================

# MSE tells the average squared difference between actual and predicted values.
# Formula: MSE = (1/n) * sum((actual - predicted)^2)
#
# Interpretation:
# - Lower MSE means better model performance
# - Penalizes large errors more than MAE
# - Units are squared, so it is harder to interpret directly

mse = mean_squared_error(y_true, y_pred)

print(f"\n2. MSE (Mean Squared Error): {mse:.2f}")
print("   -> Punishes larger errors more heavily")


# ==========================================================
# 3. RMSE (Root Mean Squared Error):
# ==========================================================

# RMSE is the square root of MSE.
# Formula: RMSE = sqrt(MSE)
#
# Interpretation:
# - Lower RMSE means better model performance
# - In the same unit as the target variable, so it is easier to interpret
# - Commonly used in regression problems

rmse = np.sqrt(mse)

print(f"\n3. RMSE (Root Mean Squared Error): {rmse:.2f}")
print("   -> Square root of MSE, easier to interpret")


# ==========================================================
# 4. R2 Score (Coefficient of Determination):
# ==========================================================

# R2 Score tells how well the model explains the data.
# Formula: R2 = 1 - (SS_residual / SS_total)
#
# Interpretation:
# - Value between 0 and 1 in most cases, but it can be negative
# - 1.0 = Perfect prediction
# - 0.5 = Model explains 50% of variance
# - 0.0 = Model is as good as average prediction
# - Negative = Model is worse than average prediction
#
# What it means:
# - R2 of 0.85 = Model explains 85% of the variability in data

r2 = r2_score(y_true, y_pred)

print(f"\n4. R2 Score: {r2:.2f}")
print("   -> How well the model explains the data variability")
