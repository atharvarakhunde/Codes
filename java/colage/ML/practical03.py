# Importing required libraries
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Loading the iris data
data = load_iris()
print("Classes to predict:", data.target_names)

# Extracting features and target
X = data.data
y = data.target

print("Number of samples:", X.shape[0])
print("First 4 feature rows:\n", X[:4])

# Splitting data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=47)

# Training with default Decision Tree
clf = DecisionTreeClassifier(criterion='entropy', random_state=47)
clf.fit(X_train, y_train)

# Prediction and accuracy
y_pred = clf.predict(X_test)
print("\nInitial Model Performance:")
print("Train Accuracy:", accuracy_score(y_train, clf.predict(X_train)))
print("Test Accuracy :", accuracy_score(y_test, y_pred))

# Visualization of the decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=data.feature_names, class_names=data.target_names)
plt.title("Decision Tree (Default)")
plt.show()

# Parameter tuning: Preventing overfitting using min_samples_split
clf_pruned = DecisionTreeClassifier(criterion='entropy', min_samples_split=50, random_state=47)
clf_pruned.fit(X_train, y_train)

# Prediction and accuracy after tuning
print("\nAfter Tuning (min_samples_split = 50):")
print("Train Accuracy:", accuracy_score(y_train, clf_pruned.predict(X_train)))
print("Test Accuracy :", accuracy_score(y_test, clf_pruned.predict(X_test)))

# Visualization of pruned tree
plt.figure(figsize=(12, 8))
plot_tree(clf_pruned, filled=True, feature_names=data.feature_names, class_names=data.target_names)
plt.title("Decision Tree (Pruned)")
plt.show()
