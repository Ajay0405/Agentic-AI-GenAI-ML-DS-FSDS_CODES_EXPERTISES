# Random Forest Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv(r"D:\AI ML\FSDS AI\FSDS AI CLASS DOCS AND CODE\Dec\26th - dtr,rf,svr,knn\23rd, 24th, 26th, - Svr, Dtr, Rf, Knn\emp_sal.csv")

x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=15)
regressor.fit(x, y) 

# Predicting a new result
y_pred = regressor.predict([[6.5]])

# Visualising the Random Forest Regression results (higher resolution)one
x_grid = np.arange(min(x), max(x), 0.01)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, regressor.predict(x_grid), color = 'blue')
plt.title('Truth or Bluff (Random Forest Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=20, random_state=43)
rf_reg.fit(x, y)

rf_pred = rf_reg.predict([[6.5]])
print(rf_pred)