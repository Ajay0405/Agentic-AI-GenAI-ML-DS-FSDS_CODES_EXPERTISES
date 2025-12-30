import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\ANIL\Downloads\emp_sal.csv")

x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

# linear regression visualizaton 
plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg.predict(x), color = 'blue')
plt.title('Linear regration graph')
plt.xlabel('Position level')
plt.ylabel('salary')
plt.show()

linear_model_pred = lin_reg.predict([[6.5]])
print(linear_model_pred)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=5)
x_poly = poly_reg.fit_transform(x)

poly_reg.fit(x_poly, y)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

plt.scatter(x, y, color = 'red')
plt.plot(x, y, color = 'red')
plt.title('Truth or Bluff (polynomial Regression)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print(poly_model_pred)

#SVR Model
from sklearn.svm import SVR
svr_regressor = SVR(kernel='poly',degree=4,gamma='auto')
svr_regressor.fit(x, y)

svr_model_pred =svr_regressor.predict([[6.5]])
print(svr_model_pred)
# KNN MOdel

from sklearn.neighbors import KNeighborsRegressor
knn_reg = KNeighborsRegressor(n_neighbors=2, weights='distance',algorithm='brute')
knn_reg.fit(x,y)

knn_pred = knn_reg.predict([[6.5]])
print(knn_pred)

# Decission Tree
from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor(criterion='poisson', max_depth=3, random_state=0)
dt_reg.fit(x, y)

dt_pred = dt_reg.predict([[6.5]])
print(dt_pred)

# Random Forest Algorithm
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=20, random_state=43)
rf_reg.fit(x, y)

rf_pred = rf_reg.predict([[6.5]])
print(rf_pred)
