# Project : Student Placement Package Predictor
# Author : Sujaan Bhalla

# Import Libraries


import numpy as np
import pandas as pd
import pymysql
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Connect Python with Local MySQL Database
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="sujaan@123",
    database="placement_db"
)

print("Database Connected Successfully")
# Read Data from MySQL

query = """
SELECT cgpa,
       dsa_score,
       communication,
       internships,
       package_lpa,
       name
FROM students
"""
df = pd.read_sql(query, conn)

print("\nOriginal Dataset")
print(df)


# Data Preprocessing

# Remove name column
df.drop("name", axis=1, inplace=True)


# Feature Scaling

scaler = StandardScaler()

df[["cgpa", "dsa_score", "communication", "internships"]] = scaler.fit_transform(
    df[["cgpa", "dsa_score", "communication", "internships"]]
)

print("\nAfter Feature Scaling")
print(df)


# Split Features and Target

x = df[["cgpa", "dsa_score", "communication", "internships"]]

y = df["package_lpa"]


# Train Test Split

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=3
)


# Model Training

model = LinearRegression()

model.fit(x_train, y_train)

print("\nModel Trained Successfully")


# Prediction

new_data = pd.DataFrame({
    "cgpa": [8.8],
    "dsa_score": [90],
    "communication": [85],
    "internships": [2]
})

print("\nNew Student Data")
print(new_data)


# Feature Scaling

new_data[["cgpa", "dsa_score", "communication", "internships"]] = scaler.transform(
    new_data[["cgpa", "dsa_score", "communication", "internships"]]
)


# Predict Package

prediction = model.predict(new_data)

print("\nPredicted Package")
print(prediction[0], "LPA")


# Save Model

joblib.dump(model, "placement_model.joblib")

print("\nModel Saved Successfully")