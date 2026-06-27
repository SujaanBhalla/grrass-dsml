# ==========================================================
# Project : Kaggle Multiple Linear Regression
# Author  : Sujaan Bhalla
# Date    : 27 June 2026
# ==========================================================

# Import Libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Read Dataset
#directly from vs code
# df = pd.read_csv("studentperformance.csv")

# print("Dataset")
# print(df.head())

# print("\nColumns")
# print(df.columns)

df = pd.read_csv(
    "https://raw.githubusercontent.com/SujaanBhalla/grrass-dsml/main/Python/Project_Kaggle_Multi_Linear_Regression/studentperformance.csv"
)
print("Dataset")
print(df.head())

print("\nColumns")
print(df.columns)


# Select Numeric Columns

X = df[["reading score", "writing score"]]
y = df["math score"]


# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=3
)


# Model Training

model = LinearRegression()

model.fit(X_train, y_train)

print("\nModel Trained Successfully")


# Prediction

new_data = pd.DataFrame({
    "reading score": [85],
    "writing score": [90]
})

prediction = model.predict(new_data)

print("\nPredicted Math Score")
print(prediction[0])


# ===============================
# Seaborn Graphs
# ===============================

# Pair Plot
sns.pairplot(df)
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(
    df[["math score","reading score","writing score"]].corr(),
    annot=True,
    cmap="Blues"
)
plt.show()

# Reading vs Math
plt.figure(figsize=(6,4))
sns.scatterplot(
    x="reading score",
    y="math score",
    data=df
)
plt.show()

# Writing vs Math
plt.figure(figsize=(6,4))
sns.scatterplot(
    x="writing score",
    y="math score",
    data=df
)
plt.show()
#Save Model using Joblib(dump)
import joblib
joblib.dump(model,
            "student_performance_model.joblib")
print("\nModel Saved Successfully")