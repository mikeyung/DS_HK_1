import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import feature_selection

cars1920 = pd.read_csv('/Users/michaelyung/DS_HK_1/data/cars1920.csv')

print "=== Details of the dataframe"
print cars1920.describe
print "=== Get Numeric Data"
print cars1920._get_numeric_data()

lm = linear_model.LinearRegression()
log_lm = linear_model.LinearRegression()

speed = [ [x] for x in cars1920['speed'].values]
log_speed = [ [x] for x in np.log(cars1920['speed'].values)]

dist = cars1920['dist'].values
log_dist = np.log(cars1920['dist'].values)

lm.fit(speed, dist)
log_lm.fit(log_speed, log_dist)

print "      Model Intercept: ", lm.intercept_
print "    Model Coefficient: ", lm.coef_
print "  Log Model Intercept: ", log_lm.intercept_
print "Log Model Coefficient: ", log_lm.coef_
print "         f_regression: ", feature_selection.univariate_selection.f_regression(speed, dist)


lm.predict(speed)
cars1920['predict'] = lm.predict(speed)

log_lm.predict(log_speed)
cars1920['log_predict'] = np.exp(log_lm.predict(log_speed))

# Sort by response:
cars1920 = cars1920.sort('dist')
# Sort by prediction:
cars1920_log_sort = cars1920.sort('log_predict')

plt.title("Scatter of the distance and prediction")
plt.scatter(cars1920['dist'], cars1920['predict'])
plt.show()
plt.title("speed, Prediction and Log speed ...")
plt.plot(speed, lm.predict(speed), np.exp(log_speed),np.exp(log_lm.predict(log_speed)))
plt.show()

"""
Polynomial Regression 
"""

cars1920['speed_squared'] = cars1920['speed']**2
speed_squared = [ [x, y] for x,y in zip(cars1920['speed'].values, cars1920['speed_squared'].values)]

ridge = linear_model.Ridge()
ridge.fit(speed_squared, dist)

print "=== Polynomial Regression ==="
print "      Ridge Intercept: ", ridge.intercept_
print "    Ridge Coefficient: ", ridge.coef_

print ((ridge.coef_[1] * cars1920['speed'])**2) + ((ridge.coef_[0] * cars1920['speed'])) + ridge.intercept_

ridge.predict(speed_squared)
cars1920['ridge'] = ridge.predict(speed_squared)

plt.title("Polynomial Regression")
plt.plot(speed, ridge.predict(speed_squared))
plt.show()
