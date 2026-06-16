import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

np.random.seed(0)
x = np.random.rand(150, 1)
y = (3 * x + np.random.rand(150, 1)) > 2.5
y = y.astype(int).ravel()

model = LogisticRegression()
model.fit(x, y)

y_pred = model.predict(x)
y_proba = model.predict_proba(x)[:, 1]

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Accuracy:", accuracy_score(y, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y, y_pred))
print("Classification Report:\n", classification_report(y, y_pred))

plt.scatter(x, y, c=y, cmap='bwr', label='Actual Data')
plt.plot(np.sort(x, axis=0), np.sort(y_proba), color='black', linewidth=2, label='Logistic Curve')
plt.xlabel('x')
plt.ylabel('Probability of y=1')
plt.title("Logistic Regression")
plt.legend()
plt.show()
