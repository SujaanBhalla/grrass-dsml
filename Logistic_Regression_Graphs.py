# ==========================================================
# Machine Learning - Logistic Regression
# Graphs & Visualizations
# ==========================================================

# Logistic Regression:
# Logistic Regression is used when the target/output variable is categorical (binary).
# Examples: Pass/Fail, Yes/No, Spam/Not Spam, Approved/Rejected, etc.

# The output is a probability between 0 and 1.
# If probability >= 0.5, predict class 1 (Yes/Positive)
# If probability < 0.5, predict class 0 (No/Negative)

# ==========================================================
# GRAPH 1: Logistic Regression Probability Curve
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Sample Data: Study Hours vs Pass/Fail
# X = Hours studied, Y = Pass (1) or Fail (0)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Train Logistic Regression Model
model = LogisticRegression()
model.fit(X, y)

# Create a range of values for smooth curve
X_range = np.linspace(0, 11, 300).reshape(-1, 1)
y_prob = model.predict_proba(X_range)[:, 1]  # Probability of class 1

# Graph: Sigmoid Curve (S-shaped curve)
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', s=100, label='Actual Data', alpha=0.6)
plt.plot(X_range, y_prob, color='red', linewidth=2, label='Logistic Regression Curve')
plt.axhline(y=0.5, color='green', linestyle='--', label='Decision Boundary (0.5)')
plt.xlabel('Hours Studied')
plt.ylabel('Probability of Passing')
plt.title('Logistic Regression: Probability Curve')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# ==========================================================
# GRAPH 2: Decision Boundary (2D Classification)
# ==========================================================

from sklearn.datasets import make_classification

# Generate random data with 2 features
X_2d, y_2d = make_classification(n_samples=100, n_features=2, n_informative=2, 
                                  n_redundant=0, random_state=42)

# Train model
model_2d = LogisticRegression()
model_2d.fit(X_2d, y_2d)

# Create mesh for decision boundary
xx = np.linspace(X_2d[:, 0].min() - 1, X_2d[:, 0].max() + 1, 100)
yy = np.linspace(X_2d[:, 1].min() - 1, X_2d[:, 1].max() + 1, 100)
XX, YY = np.meshgrid(xx, yy)

# Predict for all points in mesh
Z = model_2d.predict(np.c_[XX.ravel(), YY.ravel()])
Z = Z.reshape(XX.shape)

# Plot
plt.figure(figsize=(10, 6))
plt.contourf(XX, YY, Z, alpha=0.3, cmap='viridis')  # Decision regions
plt.scatter(X_2d[y_2d == 0, 0], X_2d[y_2d == 0, 1], color='blue', label='Class 0', s=50)
plt.scatter(X_2d[y_2d == 1, 0], X_2d[y_2d == 1, 1], color='red', label='Class 1', s=50)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Logistic Regression: Decision Boundary (2D)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# ==========================================================
# GRAPH 3: Actual vs Predicted Values
# ==========================================================

# Using the original 1D data
y_pred = model.predict(X)
y_prob_train = model.predict_proba(X)[:, 1]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# Subplot 1: Actual vs Predicted Classes
ax1.scatter(X, y, color='blue', label='Actual', s=100, alpha=0.6)
ax1.scatter(X, y_pred, color='red', marker='x', label='Predicted', s=100, linewidth=2)
ax1.set_xlabel('Hours Studied')
ax1.set_ylabel('Class (0 or 1)')
ax1.set_title('Actual vs Predicted Classes')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Subplot 2: Probability Distribution
ax2.bar(X.flatten(), y_prob_train, color='green', alpha=0.6, label='Class 1 Probability')
ax2.axhline(y=0.5, color='red', linestyle='--', label='Decision Boundary')
ax2.set_xlabel('Hours Studied')
ax2.set_ylabel('Probability')
ax2.set_title('Predicted Probability Distribution')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ==========================================================
# GRAPH 4: Confusion Matrix Heatmap
# ==========================================================

from sklearn.metrics import confusion_matrix
import seaborn as sns

# Calculate confusion matrix
cm = confusion_matrix(y, y_pred)

# Plot
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Failed', 'Passed'],
            yticklabels=['Failed', 'Passed'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Logistic Regression')
plt.show()

# ==========================================================
# GRAPH 5: ROC Curve (Receiver Operating Characteristic)
# ==========================================================

from sklearn.metrics import roc_curve, auc

# Calculate ROC curve
fpr, tpr, thresholds = roc_curve(y, y_prob_train)
roc_auc = auc(fpr, tpr)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='red', lw=2, linestyle='--', label='Random Classifier')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Logistic Regression')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# ==========================================================
# EXAMPLE: Predict from User Input
# ==========================================================

hours = float(input("Enter hours studied: "))
prob = model.predict_proba([[hours]])[0][1]  # Probability of passing
prediction = model.predict([[hours]])[0]

print(f"\nHours Studied: {hours}")
print(f"Probability of Passing: {prob:.2f}")
print(f"Prediction: {'PASS' if prediction == 1 else 'FAIL'}")
