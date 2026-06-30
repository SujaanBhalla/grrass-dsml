# # ==========================================================
# # Machine Learning
# # Day 3
# # Topic : Polynomial Regression with Graph
# # ==========================================================

# # Regression:
# # Regression is used when the target/output variable is numerical.
# # Examples: salary, house price, marks, temperature, sales, etc.

# # Polynomial Regression:
# # Polynomial Regression is used when the relationship between
# # the input feature (X) and output variable (Y) is non-linear.

# # Example:
# # Salary may not increase at a constant rate as experience increases.
# # In such cases, a curved regression line can fit the data better.

# # Formula:
# # y = b0 + b1x + b2x^2 + b3x^3 + ...

# # In this code:
# # X = Experience
# # Y = Salary/Package
# # degree=3 means the model uses Experience, Experience^2, and Experience^3.

# # Polynomial Regression
# import pandas as pd
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt


# # Data
# # A DataFrame is used to store data in tabular form.
# # Here, Experience is the input feature.
# df = pd.DataFrame({
#     "Experience": [1, 2, 3, 4, 5]
# })

# # x is the independent variable/input feature.
# x = df

# # y is the dependent variable/output.
# # These values can be considered salary/package values.
# y = [10, 20, 50, 90, 150]

# # Polynomial feature transformation
# # PolynomialFeatures converts the original input into polynomial columns.
# # For degree=3, the generated columns are:
# # 1, Experience, Experience^2, Experience^3
# poly = PolynomialFeatures(degree=3)  # x**2
# x_poly = poly.fit_transform(x)

# # Print the transformed polynomial feature matrix.
# print(x_poly)

# # Print generated feature names to understand the polynomial columns.
# print(poly.get_feature_names_out(["Experience"]))

# # Model training
# # LinearRegression is trained on polynomial features.
# # The algorithm is still linear, but the input features are polynomial.
# model = LinearRegression()
# model.fit(x_poly, y)

# # Prediction
# # Take experience input from the user.
# input_data = int(input('Enter the experience: '))
# new_data = pd.DataFrame({
#     "Experience": [input_data]
# })

# # Convert new data into polynomial format.
# # The new input must have the same feature format as the training data.
# # Learning note:
# # fit_transform is used for training data.
# # transform is generally preferred for prediction/new data.
# # The internship/online learning version is kept below for reference.
# u_new_data = poly.fit_transform(new_data)
# predicted_data = model.predict(u_new_data)

# # Print the predicted salary/package.
# print(predicted_data[0])

# # Graph
# # y_pred contains the model predictions for the training data.
# y_pred = model.predict(x_poly)

# # Clear visualization:
# # Blue dots show the actual data points.
# # The red line shows the polynomial regression curve.
# plt.scatter(x["Experience"], y, color="blue", label="Actual Data")
# plt.plot(x["Experience"], y_pred, color="red", label="Polynomial Regression")
# plt.xlabel("Experience")
# plt.ylabel("Salary / Package")
# plt.title("Polynomial Regression Graph")
# plt.legend()

# # Original learning code:
# # x_poly contains multiple transformed columns, so this line can plot
# # multiple transformed feature lines.
# plt.plot(x_poly, y)
# plt.show()

# # ==========================================================
# # Overfitting vs Underfitting
# # ==========================================================

# # Overfitting
# # - Happens when a model learns the training data too well.
# # - It captures noise and details that do not generalize.
# # - Result: high accuracy on training data, poor accuracy on new/unseen data.

# # Underfitting
# # - Happens when a model is too simple to capture the underlying pattern.
# # - It fails to learn from the training data well enough.
# # - Result: poor accuracy on both training data and new data.

# # In short
# # - Overfitting = model is too complex / fits training data too closely.
# # - Underfitting = model is too simple / cannot learn the pattern.

# #  How to tell
# # - Overfitting: training error low, validation/test error high.
# # - Underfitting: both training error and validation/test error are high.

# # Polynomial Regression -> Overfitting with Graph

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression

# df = pd.DataFrame({
#     "label": [1, 2, 3, 4, 5]
# })

# x = df
# y = [10, 20, 50, 90, 150]

# # Polynomial feature
# poly = PolynomialFeatures(degree=10)

# x_poly = poly.fit_transform(x)

# # Model
# model = LinearRegression()
# model.fit(x_poly, y)

# # Predict training data for graph
# y_pred = model.predict(x_poly)

# # Graph
# plt.scatter(x["label"], y, color="blue", label="Actual Data")
# plt.plot(x["label"], y_pred, color="red", label="Polynomial Regression Curve")
# plt.xlabel("Label")
# plt.ylabel("Value")
# plt.title("Polynomial Regression - Overfitting")
# plt.legend()
# plt.show()

# # Predict
# input_data = int(input("Enter the label: "))

# new_data = pd.DataFrame({
#     "label": [input_data]
# })

# new_data_poly = poly.transform(new_data)

# predicted_data = model.predict(new_data_poly)
# print(predicted_data[0])

# # Linear Regression -> Underfitting with Graph

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# df = pd.DataFrame({
#     "label": [1, 2, 3, 4, 5]
# })

# x = df
# y = [10, 20, 50, 90, 150]

# # Model
# model = LinearRegression()
# model.fit(x, y)

# # Predict training data for graph
# y_pred = model.predict(x)

# # Graph
# plt.scatter(x["label"], y, color="blue", label="Actual Data")
# plt.plot(x["label"], y_pred, color="red", label="Linear Regression Line")
# plt.xlabel("Label")
# plt.ylabel("Value")
# plt.title("Linear Regression - Underfitting")
# plt.legend()
# plt.show()

# # Predict
# input_data = int(input("Enter the label: "))

# new_data = pd.DataFrame({
#     "label": [input_data]
# })

# predicted_data = model.predict(new_data)
# print(predicted_data[0])

# #classification 
# import numpy as np 
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier

# df = pd.DataFrame({
#     "Weight": [ 120,140,150,170],
#     "Size": [6,7,7,8]
# })

# y = ["Apple", "Apple", "Orange", "Orange"]

# #Model
# model = DecisionTreeClassifier()
# model.fit(df, y)

# # Graph
# colors = []

# for fruit in y:
#     if fruit == "Apple":
#         colors.append("red")
#     else:
#         colors.append("orange")

# plt.scatter(df["Weight"], df["Size"], c=colors)

# plt.xlabel("Weight")
# plt.ylabel("Size")
# plt.title("Fruit Classification")
# plt.show()

# #Prediction
# input_weight = int(input("Enter the weight:" ))
# input_size = int(input("Enter the size: "))
# new_data = pd.DataFRame({
#     "Weight " : [input_weight],
#     "Size": [ input_size]

# })

# predicted_data = pd.DataFrame({
#     "Weight": [ input_weight],
#     "Size": [input_size]
# })

# # Prediction
# predicted_data = model.predict(new_data)

# print(predicted_data)

# # pass 40 above -> pass | less than 40 fail
# # Classification -> Pass or Fail

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

df = pd.DataFrame({
    "Marks": [10, 20, 30, 40, 50, 60, 70, 80, 90]
})

y = ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]

#model 
model = DecisionTreeClassifier()
model.fit(df, y)

#prediction
input_marks = int(input("Enter the marks:"))
new_data = pd.DataFrame({
    "Marks": [input_marks]

})

predicted_data = model.predict(new_data)
print(predicted_data[0])

# Graph
colors = []

for result in y:
    if result == "Pass":
        colors.append("green")
    else:
        colors.append("red")

plt.scatter(df["Marks"], y, c=colors, label="Training Data")
plt.scatter(input_marks, predicted_data[0], color="blue", marker="x", s=120, label="New Data")

plt.axvline(x=40, color="black", linestyle="--", label="Pass/Fail Boundary")

plt.xlabel("Marks")
plt.ylabel("Result")
plt.title("Pass/Fail Classification")
plt.legend()
plt.show()

 # Logistic Regression with Graph

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

X = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6]
})

y = [0, 0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)

# Generate smooth curve for the graph
X_range = np.linspace(0, 7, 300).reshape(-1, 1)
y_prob = model.predict_proba(X_range)[:, 1]  # Probability of class 1

# Create Graph
plt.figure(figsize=(10, 6))

# Plot training data points
plt.scatter(X["Hours"], y, color="blue", s=100, label="Training Data", alpha=0.7)

# Plot logistic regression curve
plt.plot(X_range, y_prob, color="red", linewidth=2, label="Logistic Regression Curve")

# Plot decision boundary at 0.5
plt.axhline(y=0.5, color="green", linestyle="--", linewidth=2, label="Decision Boundary (0.5)")

# Labels and title
plt.xlabel("Hours Studied", fontsize=12)
plt.ylabel("Probability of Passing", fontsize=12)
plt.title("Logistic Regression: Pass/Fail Classification", fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.xlim(0, 7)
plt.ylim(-0.1, 1.1)
plt.show()

# Prediction
new_data = pd.DataFrame({
    "Hours": [5]
})

prediction = model.predict(new_data)
probability = model.predict_proba(new_data)[0][1]

print(f"Prediction for 5 hours: {prediction[0]}")
print(f"Probability: {probability:.2f}")


#train-test split...
from sklearn.model_selection import train_test_split
x = [[2],[3],[4],[5],[6]]
y = [30,40,50,60,70]

#split