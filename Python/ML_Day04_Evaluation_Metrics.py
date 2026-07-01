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

# Ridge Regression:
# Ridge reduces the effect of less important features.
# It does not usually make feature values exactly zero.
# It helps reduce overfitting.

# Lasso Regression:
# Lasso can reduce the effect of less important features to zero.
# This means it can remove useless features automatically.
# It helps in feature selection.

# Example:
# If "garden" is not very important for predicting house price,
# Lasso may make its coefficient zero.
# Use:
# They are used when we have many features, such as house size,
# location, distance from city, number of bedrooms, garden, and age of house.

# Ridge Regression:
# Ridge Regression is an improved version of Linear Regression.
# It is used to reduce overfitting in a regression model.

# In Linear Regression, the model may give very large coefficient values
# to some features.
# This can make the model too complex and cause overfitting.
#lasso vs ridge regression
# lasso vs ridge regression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge,Lasso
from sklearn.metrics import mean_absolute_error,mean_squared_error
 
data = {
    "size":[1000,1200,1500,1800,2000,2200,2500,2700,3000,3200],
    "bedrooms":[2,2,3,3,3,4,4,4,5,5],
    "age":[20,18,15,12,10,8,6,5,4,2],
    "price":[30,35,45,50,55,60,68,72,80,85]
}
df = pd.DataFrame(data)
print(df)
 
#split data in x and y
x = df[['size','bedrooms','age']]
y = df['price']
 
# split data in training and testing
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
 
# training -> ridge regression
ridge = Ridge(alpha=1.0)
ridge.fit(x_train,y_train)
 
# prediction
ridge_p = ridge.predict(x_test)
print("x test")
print(x_test)
print("prediction")
print(ridge_p)
 
 
# mae
mae = mean_absolute_error(y_test,ridge_p)
print("mae =>>>",mae)
 
# mse
mse = mean_squared_error(y_true, y_pred)
print(f"\n2. MSE (Mean Squared Error): {mse:.2f}")

# Ridge Regression adds a penalty to the model.
# This penalty controls the size of the coefficients.

# Penalty:
# Penalty means extra punishment added to the model when coefficients become too large.
# Ridge Regression uses L2 penalty.

# L2 Penalty:
# L2 penalty adds the square of coefficient values to the error.
# Formula:
# Cost = Error + alpha * sum(coefficient^2)

# alpha:
# alpha controls the strength of the penalty.
# If alpha is small, penalty is weak.
# If alpha is large, penalty is strong.

# Important:
# Ridge reduces coefficient values close to zero.
# But Ridge usually does not make coefficients exactly zero.
# It keeps all features in the model.

# Use:
# Ridge Regression is useful when many features are important,
# but we want to control overfitting.

# Ridge Regression:
# Ridge Regression gives penalty to large coefficients.
# Large coefficients become smaller after applying penalty.

# Example before penalty:
# size = 145
# bedroom = 80
# parking = 200
# garden = 150

# After Ridge penalty:
# size = 40
# bedroom = 60
# parking = 150
# garden = 120

# Important:
# Ridge makes coefficients smaller,
# but it usually does not make them exactly zero.
# Lasso Regression:
# Lasso Regression also gives penalty to large coefficients.
# But Lasso can make some coefficients exactly zero.

# This means Lasso can remove less important features from the model.

# Example:
# If garden is not useful for predicting house price,
# Lasso can make garden coefficient = 0.

# Important:
# Lasso makes coefficients smaller,
# and some coefficients can become zero.

# training -> lasso regression
lasso = Lasso(alpha=1.0)
lasso.fit(x_train, y_train)

# prediction
lasso_p = lasso.predict(x_test)
print("lasso prediction")
print(lasso_p)

# mae
lasso_mae = mean_absolute_error(y_test, lasso_p)
print("lasso mae =>>>", lasso_mae)

# mse
lasso_mse = mean_squared_error(y_test, lasso_p)
print("lasso mse =>>>", lasso_mse)
#model intercept 
print("lasso intercept")
print(lasso.intercept_)
#model coefficeet 
print("lasso coefficients")
print(lasso.coef_)

# Simple meaning:
# Lasso also gives penalty to large coefficients.
# If any feature is not useful, Lasso can make its coefficient zero.
# Zero coefficient means that feature is removed from the model.

# logistic regression
import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "hours": [1, 2, 3, 4, 5, 6, 7],
    "result": [0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)

x = df[["hours"]]
y = df["result"]

log_model = LogisticRegression()
log_model.fit(x, y)

new_data = pd.DataFrame({
    "hours": [2.5]
})
pred_d = log_model.predict(new_data)

if pred_d[0] == 0:
    print("fail")
else:
    print("pass")

# KNN (K-Nearest Neighbors):
# KNN is a machine learning algorithm used for classification and regression.
# In classification, KNN checks the nearest neighbors of a new data point.
# Then it gives the class which is in majority.

# Example:
# If nearest students are:
# CSE, CSE, CSE, DS
# Then new student will be predicted as CSE.

# Why?
# Because CSE is in majority.

# K means number of nearest neighbors.
# If K = 4, model checks 4 nearest neighbors.

# KNN does not train like Linear Regression.
# It stores the data and compares new data with old data.
# KNN
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# data set
data = {
    "weight": [100, 110, 120, 170, 180, 190],
    "fruits": [0, 0, 0, 1, 1, 1]  # 0 => apple and 1 => orange
}

df = pd.DataFrame(data)
print(df)

#split x and y
x = df[["weight"]]
y = df["fruits"]
# model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x, y)

# new data
new_data = pd.DataFrame({
    "weight": [160]
})

pred_d = model.predict(new_data)
print(pred_d)

if pred_d[0] == 0:
    print("apple")
else:
    print("orange")

