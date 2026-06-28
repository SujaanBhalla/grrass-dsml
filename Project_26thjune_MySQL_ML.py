# ==========================================================
# Project : MySQL Integrated Machine Learning Project
# Author  : Sujaan Bhalla
# Internship : GRRAS Solutions
# Date    : 26 June 2026
# ==========================================================

# """
# Project Workflow

# MySQL Database
#         ↓
# Python Backend
#         ↓
# Read Data
#         ↓
# Train-Test Split
#         ↓
# Simple Linear Regression
#         ↓
# Save Model (Joblib)
#         ↓
# Load Model
#         ↓
# Prediction
# """

#project using mysql and joblib
# ==========================================================
# Project using MySQL + Joblib + SLR / MLR
# ==========================================================

# Import Libraries
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Create Sample Dataset


# This dataset contains customer information
# that will be used to train the Machine Learning model.

# data = {
#     "name": [ "sujaan","emily","gabriel","cammiel"
#         # Customer Names
#     ],

#     "avg_income": [ 5000,4000,3000,2000
#         # Average Monthly Income
#     ],

#     "house_age": [ 10,8,6,4
#         # Age of House (Years)
#     ],

#     "num_rooms": [ 4,3,2,1
#         # Number of Rooms
#     ],

#     "price": [ 10000,9000,8000,7000
#         # House Price (Target Variable)
#     ]
# }
# MySQL Connector

# Install Package
# pip install mysql-connector-python

import mysql.connector
import pandas as pd

# pymysql dynamic data
# !pip install pymysql cryptography
conn = mysql.connector.connect(
    host="13.220.156.88",
    user="mluser",
    password="mlpass123",
    database="ml_db"
)



# # Convert Dictionary into DataFrame
# df = pd.DataFrame(data)
# print("Original Dataset")
# print(df)


# Handle Missing Values
# Drop 'name' column because it is not required
# for Machine Learning model training.

df.drop("name", axis=1, inplace=True)


# Feature Scaling
# Create StandardScaler object
scaler = StandardScaler()

# Scale the numerical feature columns
df[['avg_income', 'house_age', 'num_rooms']] = scaler.fit_transform(
    df[['avg_income', 'house_age', 'num_rooms']]
)
print("\nAfter Feature Scaling")
print(df)


# Split Features and Target
# Input Features (Independent Variables)
x = df[['avg_income', 'house_age', 'num_rooms']]
# Target Variable (Dependent Variable)
y = df['price']
print("\nInput Features (X)")
print(x)
print("\nTarget Variable (y)")
print(y)


# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=3
)

# Model Training
# Create Linear Regression Model
model = LinearRegression()
# Train the model using training data
model.fit(x_train, y_train)


# Prediction
# New customer data for prediction
new_data = {
    "avg_income": [4500],
    "house_age": [9],
    "num_rooms": [3]
}

# Convert dictionary into DataFrame
df1 = pd.DataFrame(new_data)
print("\nNew Input Data")
print(df1)

# Scale new input data
df1[['avg_income', 'house_age', 'num_rooms']] = scaler.transform(
    df1[['avg_income', 'house_age', 'num_rooms']]
)

# Predict House Price
prediction = model.predict(df1)
print("\nPredicted Price")
print(prediction[0])

import joblib

joblib.dump(model, "house_model.joblib")

print("Model saved successfully.")