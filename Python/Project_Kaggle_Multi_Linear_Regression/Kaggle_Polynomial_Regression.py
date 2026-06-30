# ==========================================================
# Kaggle Polynomial Regression Project
# Student Placement Salary Prediction
# ==========================================================

# Import Libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# ==========================================================
# Read Dataset from GitHub
# ==========================================================

url = "https://raw.githubusercontent.com/SujaanBhalla/grrass-dsml/main/Python/Project_Kaggle_Multi_Linear_Regression/student_placement_dataset.csv"

df = pd.read_csv(url)

print("Dataset")
print(df.head())

print("\nColumns")
print(df.columns)


# ==========================================================
# Select Numerical Features
# ==========================================================

X = df[[
    "cgpa",
    "coding_skill_score",
    "aptitude_score",
    "study_hours_per_day"
]]

y = df["salary_package_lpa"]


# ==========================================================
# Polynomial Features
# ==========================================================

poly = PolynomialFeatures(degree=2)

X_poly = poly.fit_transform(X)


# ==========================================================
# Train Test Split
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X_poly,
    y,
    test_size=0.2,
    random_state=3
)


# ==========================================================
# Train Model
# ==========================================================

model = LinearRegression()

model.fit(X_train, y_train)

print("\nPolynomial Regression Model Trained Successfully")


# ==========================================================
# Model Evaluation
# ==========================================================

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"\nTraining Score: {train_score:.4f}")
print(f"Testing Score: {test_score:.4f}")


# ==========================================================
# Prediction
# ==========================================================

new_data = pd.DataFrame({

    "cgpa": [8.5],
    "coding_skill_score": [90],
    "aptitude_score": [85],
    "study_hours_per_day": [5]

})

new_data_poly = poly.transform(new_data)

prediction = model.predict(new_data_poly)

print("\nPredicted Salary Package (LPA)")
print(f"Salary: {prediction[0]:.2f} LPA")


# ==========================================================
# Pair Plot (Relationship between features)
# ==========================================================

print("\nGenerating Pair Plot...")

sns.pairplot(
    df[[
        "cgpa",
        "coding_skill_score",
        "aptitude_score",
        "salary_package_lpa"
    ]]
)

plt.show()


# ==========================================================
# Correlation Heatmap
# ==========================================================

print("\nGenerating Correlation Heatmap...")

plt.figure(figsize=(8, 6))

sns.heatmap(
    df[[
        "cgpa",
        "coding_skill_score",
        "aptitude_score",
        "salary_package_lpa"
    ]].corr(),
    annot=True,
    cmap="Blues",
    fmt=".2f"
)

plt.title("Correlation Heatmap - Feature Relationships", fontsize=14, fontweight="bold")

plt.tight_layout()

plt.show()


# ==========================================================
# Scatter Plot: CGPA vs Salary
# ==========================================================

print("\nGenerating Scatter Plot...")

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="cgpa",
    y="salary_package_lpa",
    color="blue",
    s=100,
    alpha=0.6
)

plt.title("CGPA vs Salary Package", fontsize=14, fontweight="bold")

plt.xlabel("CGPA", fontsize=12)

plt.ylabel("Salary Package (LPA)", fontsize=12)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()


# ==========================================================
# Scatter Plot: Coding Skills vs Salary
# ==========================================================

print("\nGenerating Coding Skills vs Salary Plot...")

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="coding_skill_score",
    y="salary_package_lpa",
    color="green",
    s=100,
    alpha=0.6
)

plt.title("Coding Skills vs Salary Package", fontsize=14, fontweight="bold")

plt.xlabel("Coding Skill Score", fontsize=12)

plt.ylabel("Salary Package (LPA)", fontsize=12)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()


# ==========================================================
# Scatter Plot: Aptitude vs Salary
# ==========================================================

print("\nGenerating Aptitude vs Salary Plot...")

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="aptitude_score",
    y="salary_package_lpa",
    color="red",
    s=100,
    alpha=0.6
)

plt.title("Aptitude Score vs Salary Package", fontsize=14, fontweight="bold")

plt.xlabel("Aptitude Score", fontsize=12)

plt.ylabel("Salary Package (LPA)", fontsize=12)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()


# ==========================================================
# Distribution Plot: Salary Distribution
# ==========================================================

print("\nGenerating Salary Distribution Plot...")

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="salary_package_lpa",
    kde=True,
    color="skyblue",
    bins=20
)

plt.title("Salary Package Distribution", fontsize=14, fontweight="bold")

plt.xlabel("Salary Package (LPA)", fontsize=12)

plt.ylabel("Frequency", fontsize=12)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()


# ==========================================================
# Box Plot: Salary Distribution by Categories
# ==========================================================

print("\nGenerating Box Plot...")

plt.figure(figsize=(12, 6))

sns.boxplot(
    data=df,
    y="salary_package_lpa",
    color="lightblue"
)

plt.title("Salary Package Distribution - Box Plot", fontsize=14, fontweight="bold")

plt.ylabel("Salary Package (LPA)", fontsize=12)

plt.grid(True, alpha=0.3, axis="y")

plt.tight_layout()

plt.show()


# ==========================================================
# Save Model using Pickle
# ==========================================================

with open("polynomial_regression_model.pkl", "wb") as file:

    pickle.dump(model, file)

print("\nModel Saved Successfully as 'polynomial_regression_model.pkl'")


# ==========================================================
# Load Model (For Future Use)
# ==========================================================

# with open("polynomial_regression_model.pkl", "rb") as file:
#     loaded_model = pickle.load(file)
# print("Model Loaded Successfully")
