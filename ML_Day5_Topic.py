# # ==========================================================
# # Machine Learning
# # Day 5
# # Topic: Decision Tree and Classification
# # ==========================================================

# # Notes for you:
# # - The code below is only a starting point.
# # - You can type your own code and examples instead of running this file.
# # - Keep the explanations in comments, and add real code where needed.

# # What is classification?
# # - Classification predicts a category or class label.
# # - Example: "buy" or "not buy", "spam" or "not spam", "pass" or "fail".
# # - The output is discrete.

# # What is regression?
# # - Regression predicts a continuous numeric value.
# # - Example: house price, salary, temperature.
# # - The output is a number.

# # What is a Decision Tree?
# # - A decision tree learns rules from data by splitting on feature values.
# # - It can be used for both classification and regression.
# # - For classification, the tree predicts class labels.
# # - For regression, the tree predicts numeric values.

# # Example summary:
# # - Decision Tree Classification = predict class labels.
# # - Decision Tree Regression = predict numeric values.

# # Your task:
# # 1. Write a small dataset (age, salary, buy) or any example you want.
# # 2. Use train_test_split to split the data.
# # 3. Train DecisionTreeClassifier for classification.
# # 4. Print the predictions and accuracy.

# if __name__ == '__main__':
#     print('ML Day 5 topic file created.')

# #decision tree
# # Optimized tool selectionI will explain the concepts clearly and simply, focusing on decision trees and how they relate to classification and regression.

# # Here is a simple explanation:

# # - Classification means predicting a category or class.
# #   - Example: spam or not spam, pass or fail, yes or no.
# #   - The output is discrete.

# # - Regression means predicting a continuous numeric value.
# #   - Example: house price, salary, temperature.
# #   - The output is a number.

# # Decision Tree:
# # - A decision tree is a supervised learning algorithm that splits data based on conditions.
# # - It can be used for both:
# #   - Classification trees: when the target is categorical
# #   - Regression trees: when the target is numeric
# #

# #decision tree


# # So:
# # - Decision Tree Classification = predict class labels
# # - Decision Tree Regression = predict numeric values

# # Simple example:
# # - Classification: “Will the student pass?” → Yes/No
# # - Regression: “What will the student’s marks be?” → 78, 82, 91, etc.

# # In short:
# # - Classification = category
# # - Regression = number
# # - Decision tree can do both depending on the type of target variable

# # If you want, I can also give you:
# # - a very short exam-style answer, or
# # - a real-world example with a diagram.




# # decision tree example with comments
# # Step 1: import the required libraries
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score, mean_absolute_error
 
# # Step 2: define the dataset
# data = {
#     "age":[20,22,25,28,30,35,40,45,50,55],
#     "salary":[20000,25000,27000,32000,45000,50000,60000,70000,80000,9000],
#     "buy":[0,0,0,0,1,1,1,1,1,0]
# }
 
# # Step 3: convert the data into a DataFrame and print it
# # This shows the input table before training the model.
# df = pd.DataFrame(data)
# print(df)
 
# # Step 4: prepare features and target
# # x contains the input features (age and salary)
# # y contains the target labels (buy or not buy)
# x = df[['age','salary']] # features
# y = df['buy'] # target
 
# # Step 5: split data into training and testing sets
# # test_size=0.2 means 20% of the data is used for testing.
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
 
# # Step 6: create and train the Decision Tree classifier
# model = DecisionTreeClassifier(random_state=42)
# model.fit(x_train,y_train)
 
# # Step 7: make predictions on the test set
# y_pred = model.predict(x_test)

# # Step 8: print actual and predicted values
# print("actual data: ", y_test)
# print("prediction: ", y_pred)

# # Decision tree split criteria:
# # - Gini index: measures impurity. Lower is better. For a node with class probabilities p_i:
# #     Gini = 1 - sum(p_i^2)
# #   It is the default criterion for sklearn DecisionTreeClassifier.
# # - Entropy: measures disorder or information content. For probabilities p_i:
# #     Entropy = -sum(p_i * log2(p_i))
# #   When using entropy, the tree selects splits that maximize information gain.
# #
# # In short:
# # - Gini is faster and often gives similar results.
# # - Entropy is based on information theory and can be more sensitive to probability changes.


# #code 
# from sklearn.tree import DecisionTreeClassifier
# model = DecisionTreeClassifier(
#     random_state=42,
#     criterion="entropy"
# )

# model = DecisionTreeClassifier(
#     random_state=42,
#     criterion="gini"
# )

# # Random Forest = multiple decision trees
# # ----------------------------------------------------------
# # A single decision tree can be weak sometimes.
# # It may take one decision path and make a wrong prediction.
# #
# # Random Forest makes the decision stronger by using many trees.
# # Each tree gives one prediction, then we count the votes.
# # The final output is the class with the majority vote.
# #
# # Example:
# # Suppose you want to buy a laptop and you ask many friends.
# #
# # Friend 1 says: Dell
# # Friend 2 says: HP
# # Friend 3 says: Dell
# # Friend 4 says: Lenovo
# # Friend 5 says: Dell
# #
# # Vote count:
# # Dell   = 3 votes
# # HP     = 1 vote
# # Lenovo = 1 vote
# #
# # Final decision = Dell, because Dell got the majority votes.
# #
# # In the same way:
# # - One decision tree = one friend's suggestion
# # - Random forest = suggestions from many friends
# # - Final prediction = majority vote of many trees
# #
# # This is why random forest is usually stronger than a single decision tree.

# #code 
# #random forest
# #step 1: import libraries
# import pandas as pd
# from sklearn.model_selection import train_test_split 
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score #model accuracy
# #step 2 : define the dataset
# data = {
#     "age":[20,22,25,28,30,35,40,45,50,55],
#     "salary":[20000,25000,27000,32000,45000,50000,60000,70000,80000,9000],
#     "buy":[0,0,0,0,1,1,1,1,1,0]
# }
# #step 3 : convert the data into a dataframe and print it
# df = pd.DataFrame(data)
# print(df)

# #Step 4: x,y split 
# x = df[["age","salary"]]
# y = df["buy"] 

# #Step 5: train split
# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# #Step 6: model train
# model = RandomForestClassifier(random_state=42,n_estimators=10) # n estimators
# model.fit(x_train,y_train)

# #Step 7: prediction
# y_pred = model.predict(x_test)

# print("prediction: ", y_pred)
# print("actual data: ", y_test)
# print("accuracy: ", accuracy_score(y_test,y_pred))

# # EXAMPLE: now example of decision tree and random forest of this laptop example only and graph of 
# # decision tree and random forest with matplotlib
# #step 1: import libraries
# import pandas as pd
# from sklearn.model_selection import train_test_split 
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score #model accuracy
# import matplotlib.pyplot as plt

# #step 2 : define the dataset
# #dataset of friends suggestion of laptop
# data = {
#     "friend":["emily","gabriel","hannah","garrett","olivia","sophia"],
#     "laptop_suggestion":["dell","hp","dell","lenovo","dell","hp"],
#     "buy":[1,0,1,0,1,0]
# }
# #step 3 : convert the data into a dataframe and print it
# df = pd.DataFrame(data)
# print(df)

# #Step 4: x,y split 
# # convert friend and laptop_suggestion into numeric columns
# # so the model can use them correctly
# encoded = pd.get_dummies(df, columns=["friend", "laptop_suggestion"])
# x = encoded.drop("buy", axis=1)
# y = encoded["buy"] 

# #Step 5: train split
# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# #Step 6: model train
# model = RandomForestClassifier(random_state=42,n_estimators=10) # n estimators
# model.fit(x_train,y_train)

# #Step 7: prediction
# y_pred = model.predict(x_test)

# print("prediction: ", y_pred)
# print("actual data: ", y_test)
# print("accuracy: ", accuracy_score(y_test,y_pred))

# #graph of dicision tree and random forest with matplotlib
# from sklearn.tree import plot_tree

# # Decision tree
# dt = DecisionTreeClassifier(random_state=42)
# dt.fit(x_train, y_train)

# fig, ax = plt.subplots(figsize=(12, 7))
# plot_tree(
#     dt,
#     feature_names=x.columns,
#     class_names=["not buy", "buy"],
#     filled=True,
#     rounded=True,
#     ax=ax
# )
# ax.set_title("Decision Tree")
# plt.tight_layout()
# plt.show()

# # Random forest - plot one of the trees
# rf = RandomForestClassifier(random_state=42, n_estimators=5)
# rf.fit(x_train, y_train)

# fig, ax = plt.subplots(figsize=(12, 7))
# plot_tree(
#     rf.estimators_[0],
#     feature_names=x.columns,
#     class_names=["not buy", "buy"],
#     filled=True,
#     rounded=True,
#     ax=ax
# )
# ax.set_title("Random Forest - Tree 0")
# plt.tight_layout()
# plt.show()

# # Simple line graph example
# # This draws a basic line plot for any numeric x and y values.
# x_line = [1, 2, 3, 4, 5]
# y_line = [10, 15, 12, 18, 22]
# plt.figure(figsize=(8, 4))
# plt.plot(x_line, y_line, marker='o', linestyle='-', color='blue')
# plt.title('Simple Line Graph')
# plt.xlabel('X values')
# plt.ylabel('Y values')
# plt.grid(True)
# plt.show()

# # Ensemble Learning:
# # Ensemble learning means combining multiple machine learning models
# # to make a stronger and more accurate final model.
# #
# # Simple example:
# # Instead of asking only one friend for a laptop suggestion,
# # you ask many friends and take the final decision by majority vote.
# #
# # In machine learning:
# # - One model may make mistakes.
# # - Many models together can reduce mistakes.
# # - Final prediction becomes more stable and reliable.
# #
# # Random Forest is an example of ensemble learning because
# # it combines many decision trees.

# # Bagging:
# # Bagging means Bootstrap Aggregating.
# #
# # Bootstrap means creating different small training datasets
# # by randomly selecting rows from the original dataset.
# #
# # Aggregating means combining the results of all models.
# #
# # In Random Forest:
# # - Many decision trees are trained.
# # - Each tree gets a different random sample of data.
# # - Each tree gives its own prediction.
# # - For classification, the final answer is decided by majority vote.
# # - For regression, the final answer is usually the average prediction.
# #
# # Simple example:
# # Tree 1 predicts: Dell
# # Tree 2 predicts: HP
# # Tree 3 predicts: Dell
# # Tree 4 predicts: Lenovo
# # Tree 5 predicts: Dell
# #
# # Final prediction = Dell, because Dell has the majority vote.
# #
# # So:
# # Ensemble Learning = combining many models.
# # Bagging = training many models on different random samples.
# # Random Forest = bagging + many decision trees.

# # Evaluating Model
# # Test the model on unseen data.
# # Use metrics like accuracy, precision, recall, MAE, or confusion matrix.
# #
# # Confusion matrix explained simply:
# # Imagine the model predicts pass/fail for students.
# # Actual = real result, Predicted = model result.
# #
# # Example:
# # Actual:    pass, pass, fail, pass, fail
# # Predicted: pass, fail, fail, pass, pass
# #
# # Compare each result:
# # - True Positive (TP): model said pass, actual was pass.
# #   Example count = 2
# # - True Negative (TN): model said fail, actual was fail.
# #   Example count = 1
# # - False Positive (FP): model said pass, actual was fail.
# #   Example count = 1
# # - False Negative (FN): model said fail, actual was pass.
# #   Example count = 1
# #
# # Metrics from this example:
# # - Accuracy = (TP + TN) / total = (2 + 1) / 5 = 60%
# # - Precision = TP / (TP + FP) = 2 / (2 + 1) = 66.7%
# # - Recall = TP / (TP + FN) = 2 / (2 + 1) = 66.7%
# # - F1-score = 2 * (precision * recall) / (precision + recall)
# #   F1 is the balance between precision and recall.
# #
# # In simple language:
# # - Accuracy = how many predictions were correct overall.
# # - Precision = when the model says yes, how often it is right.
# # - Recall = how many real yes cases the model caught.
# # - F1-score = a combined score of precision and recall.
# #
# # Use these metrics to understand the model better, not just accuracy.

# # code 
from sklearn.metrics import confusion_matrix
actual = [ 1,0,1,1,0,1,0,0]
predicted = [ 1,0,1,0,0,1,1,0]
cm = confusion_matrix(actual,predicted)
print("Confusion Matrix:\n", cm)

import matplotlib.pyplot as plt 
from sklearn.metrics import ConfusionMatrixDisplay
actual = [ 1,0,1,1,0,1,0,0]
predicted = [ 1,0,1,0,0,1,1,0]
ConfusionMatrixDisplay.from_predictions(actual,predicted)
plt.title("Confusion Matrix")
plt.show()
# precision = when the model predicts positive, how often it is correct.
#   formula: TP / (TP + FP)
# recall = when the answer is actually positive, how often the model finds it.
#   formula: TP / (TP + FN)
#
# Difference:
# - Precision cares about false positives (FP).
#   It answers: "Of all positive predictions, how many were right?"
# - Recall cares about false negatives (FN).
#   It answers: "Of all real positives, how many did the model find?"
#
# f1 score = the balance between precision and recall.
#   formula: 2 * (precision * recall) / (precision + recall)

#precision| recall|f1 score
import pandas as pd
import sklearn.metrics as metrics
from sklearn.metrics import precision_score, recall_score, f1_score

actual = [1,0,1,1,0,1,0,0]
predicted = [1,0,1,0,0,1,1,0]
cm = confusion_matrix(actual,predicted)
print("confusion matrix:\n",cm)
print(f"Precision: {cm[1,1] / (cm[1,1] + cm[0,1])}")
print(3/(3+1))
#precision score
precision = precision_score(actual,predicted)
print(f"Precision_Score:", precision)
print(f"Recall: {cm[1,1] / (cm[1,1] + cm[1,0])}")
#recall 
recall = recall_score(actual,predicted)
print(f"Recall_Score:", recall)
print(f"F1 Score: {2 * (cm[1,1] / (cm[1,1] + cm[0,1])) * (cm[1,1] / (cm[1,1] + cm[1,0])) / ((cm[1,1] / (cm[1,1] + cm[0,1])) + (cm[1,1] / (cm[1,1] + cm[1,0])))}")
#f1 score
f1 = f1_score(actual,predicted)
print(f"F1_Score:", f1)

# ## Unsupervised learning

# - It means the algorithm learns from data without labels.
# - The model does not know the correct answer in advance.
# - It finds patterns, groups, or structure by itself.

# ## Example with images

# - Suppose you have many pictures of animals but no labels.
# - Unsupervised learning can group similar pictures together:
#   - group all cats in one cluster
#   - group all dogs in another cluster
# - Or it can learn a simpler image representation:
#   - compress images using an autoencoder
#   - then the model can recreate the image from a small code

# ## Types of unsupervised learning

# 1. Clustering
#    - Groups data points that are similar.
#    - Example: group similar images together by shape or color.
#    - Common methods: K-means, hierarchical clustering.

# 2. Dimensionality reduction
#    - Reduces image data to fewer features.
#    - Example: turn a 1000-pixel image into 50 numbers that still describe it.
#    - Common methods: PCA, t-SNE, autoencoders.

# 3. Association
#    - Finds rules between items.
#    - Example: in image data, it can discover that certain objects appear together.
#    - Common method: market basket-style rule mining.

# ## Simple image example in plain words

# - You give the model many photos.
# - It does not know the labels.
# - It groups photos by similarity.
# - That is unsupervised learning.

## Difference between supervised and unsupervised learning

# ### Supervised learning
# - Data has labels/answers already.
# - The model learns from examples like:
#   - input = image, label = cat or dog
#   - input = email text, label = spam or not spam
# - The goal is to predict the correct label for new data.
# - Example: train a model to classify images into classes.

# ### Unsupervised learning
# - Data has no labels/answers.
# - The model finds patterns or groups by itself.
# - It clusters similar items or reduces data size.
# - Example: group similar images together without knowing their names.

# ### Simple way to remember
# - Supervised = learning with teacher / known answers
# - Unsupervised = learning without teacher / no answers

# ### Example
# - Supervised: teach with image + label, then predict if new image is “dog”
# - Unsupervised: give many animal images and let the model group them into similar clusters

# If you want, I can also give one line of code example for each.