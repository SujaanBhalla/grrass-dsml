# # ==========================================================
# # GRRAS Solutions - DSML with AI
# # Author : Sujaan Bhalla
# # Day 02 - Machine Learning Basics
# # Topic : Feature Scaling using StandardScaler
# # ==========================================================

# # ==========================================================
# # Import Libraries
# # ==========================================================

# import numpy as np              # Used for numerical operations
# import pandas as pd             # Used for creating and handling DataFrames
# import matplotlib.pyplot as plt # Used for data visualization (graphs)

# # Import StandardScaler
# # StandardScaler is used to scale numerical features.
# # It converts data so that:
# # Mean = 0
# # Standard Deviation = 1
# from sklearn.preprocessing import StandardScaler

# # ==========================================================
# # Create Dataset
# # ==========================================================

# data = {
#     "experience": [300, 600, 900, 1500],
#     "salary": [1000, 1500, 2000, 3000]
# }

# # Convert dictionary into DataFrame
# df = pd.DataFrame(data)

# print("Original Dataset")
# print(df)

# # ==========================================================
# # Feature Scaling
# # ==========================================================

# # Create StandardScaler object
# # This object will perform feature scaling.
# scaler = StandardScaler()

# # fit_transform() performs two tasks:
# #
# # fit()       -> Learns the mean and standard deviation of the data.
# #
# # transform() -> Uses those values to scale the data.
# #
# # fit_transform() = fit() + transform()

# # Double brackets [[ ]] are used because
# # StandardScaler expects a 2-dimensional input
# # (DataFrame), not a 1-dimensional Series.

# df["experience"] = scaler.fit_transform(df[["experience"]])

# print("\nAfter Feature Scaling")
# print(df)

# # ==========================================================
# # Split Data into Features (X) and Target (y)
# # ==========================================================

# # X = Independent Variable (Input Feature)
# # This is the data that will be given to the machine learning model.
# # Here, Experience is used as the input feature.

# X = df["experience"]

# # y = Dependent Variable (Target / Output)
# # This is the value that the model has to predict.
# # Here, Salary is the target variable.

# y = df["salary"]

# # Display Features and Target
# print("Input Feature (X)")
# print(X)

# print("\nTarget Variable (y)")
# print(y)
# # graph plot 


# #important note : # fit()
# # Reads the training data and learns its pattern.
# # Example:
# # - Calculates Mean
# # - Calculates Standard Deviation
# # - Learns the relationship in the data

# # transform()
# # Uses the learned information to convert or scale the data.

# # fit_transform()
# # First learns from the data (fit),
# # then immediately transforms the data (transform).

# # inverse_transform() converts the scaled data
# # back to its original values.
# #
# # Example:
# #
# # Original Experience = 300
# # After Scaling = -1.18
# #
# # inverse_transform(-1.18)
# # Output = 300

# # predict() is used after training the model.
# #
# # It predicts the output for new input data.
# #
# # Example:
# #
# # Experience = 5 Years
# #
# # model.predict([[5]])
# #
# # Output:
# # Predicted Salary = 45000
# # ==========================================================
# # Plot Graph
# # ==========================================================

# plt.figure(figsize=(6,4))

# plt.plot(df["experience"], df["salary"],
#          marker="o",
#          color="blue")

# plt.title("Experience vs Salary")

# plt.xlabel("Experience (Scaled)")
# plt.ylabel("Salary")

# plt.grid(True)

# plt.show()


# # Train Test Split
# # Import train_test_split
# # It is used to divide the dataset into
# # Training Data and Testing Data.

# from sklearn.model_selection import train_test_split
# print("spliting training and testing")
# # Split the dataset
# # X -> Input Feature (Independent Variable)
# # y -> Output / Target (Dependent Variable)

# # test_size = 0.2
# # Means 20% data will be used for Testing
# # and 80% data will be used for Training.

# x_train, x_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2
# )
# # x_train
# # Input data used to train the machine learning model.

# # x_test
# # Input data used to test the trained model.

# # y_train
# # Actual output values corresponding to x_train.

# # y_test
# # Actual output values corresponding to x_test.

# # Display Training and Testing Data
# print("display training and testing(20%)")
# print("X Train")
# print(x_train)

# print("\nX Test")
# print(x_test)

# print("\nY Train")
# print(y_train)

# print("\nY Test")
# print(y_test)


# x_train, x_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.5
# )
# print("display training and testing(50%)")
# print("X Train")
# print(x_train)

# print("\nX Test")
# print(x_test)

# print("\nY Train")
# print(y_train)

# print("\nY Test")
# print(y_test)

#lets work on sample dataset
# ==========================================================
# Import Libraries
# ==========================================================

import pandas as pd
from sklearn.model_selection import train_test_split

# Read Dataset
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/extended_salary_data.csv"

df = pd.read_csv(url)

print(df.columns)

# Features
X = df[["experience"]]

# Target
y = df["salary"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=3
)

print("X Train")
print(X_train)

print("\nX Test")
print(X_test)

print("\nY Train")
print(y_train)

print("\nY Test")
print(y_test)

# Simple Linear Regression
# Creates a Simple Linear Regression model.
from sklearn.linear_model import LinearRegression
# Model Training
# Create Linear Regression Model
model = LinearRegression()

# Train the model
# fit() studies the training data and learns the relationship
# between Experience (X) and Salary (y)

model.fit(X_train, y_train)

# Model Prediction
# New input data for prediction
new_data = {
    "experience": [10]
}
# Convert dictionary into DataFrame
df1 = pd.DataFrame(new_data)
print("New Input Data")
print(df1)
# Predict Salary
# model.predict() expects 2D input.
prediction = model.predict(df1)
# Predicts the salary for the given experience.
print("\nPredicted Salary")
print(prediction)
