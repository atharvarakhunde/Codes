import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(0)
x = np.random.rand(150, 1)
y = 2 + 3 * x + np.random.rand(150, 1)

regression_model = LinearRegression()
regression_model.fit(x, y)

y_predicted = regression_model.predict(x)

rmse = mean_squared_error(y, y_predicted)
r2 = r2_score(y, y_predicted)

print('Slope (Coefficient):', regression_model.coef_)
print('Intercept:', regression_model.intercept_)
print('Root Mean Squared Error (RMSE):', rmse)
print('R2 Score:', r2)

plt.scatter(x, y, s=10, label="Actual Data")
plt.plot(x, y_predicted, color='red', label="Regression Line")
plt.xlabel('x-values from 0 to 1')
plt.ylabel('y-values from 2 to 5')
plt.title("Linear Regression using Scikit-learn")
plt.legend()
plt.show()
