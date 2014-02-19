import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import feature_selection

cars93 = pd.read_csv('/Users/michaelyung/DS_HK_1/data/cars93.csv')

print "=== Details of the dataframe"
print cars93.describe
#print "=== Get Numeric Data"
#print cars93._get_numeric_data()

lm = linear_model.LinearRegression()
log_lm = linear_model.LinearRegression()

MPG_city = [ [x] for x in cars93['MPG.city'].values]
log_MPG_city = [ [x] for x in np.log(cars93['MPG.city'].values)]

MPG_highway = cars93['MPG.highway'].values
log_MPG_highway = np.log(cars93['MPG.highway'].values)

lm.fit(MPG_city, MPG_highway)
log_lm.fit(log_MPG_city, log_MPG_highway)

print "      Model Intercept: ", lm.intercept_
print "    Model Coefficient: ", lm.coef_
print "  Log Model Intercept: ", log_lm.intercept_
print "Log Model Coefficient: ", log_lm.coef_


lm.predict(MPG_city)
cars93['predict'] = lm.predict(MPG_city)

log_lm.predict(log_MPG_city)
cars93['log_predict'] = np.exp(log_lm.predict(log_MPG_city))

# Sort by response:
cars93 = cars93.sort('MPG.highway')
# Sort by prediction:
cars93_log_sort = cars93.sort('log_predict')

plt.title("Scatter of MPG.city and the MPG.highway")
plt.scatter(cars93['MPG.highway'], cars93['predict'])
plt.show()
plt.title("MPG.city, Prediction and Log MPG.city ...")
plt.plot(MPG_city, lm.predict(MPG_city), np.exp(log_MPG_city),np.exp(log_lm.predict(log_MPG_city)))
plt.show()

"""
Polynomial Regression 
"""

cars93['MPG.city_squared'] = cars93['MPG.city']**2
MPG_city_squared = [ [x, y] for x,y in zip(cars93['MPG.city'].values, cars93['MPG.city_squared'].values)]

ridge = linear_model.Ridge()
ridge.fit(MPG_city_squared, MPG_highway)

print "=== Polynomial Regression ==="
print "      Ridge Intercept: ", ridge.intercept_
print "    Ridge Coefficient: ", ridge.coef_

ridge.predict(MPG_city_squared)
cars93['ridge'] = ridge.predict(MPG_city_squared)
print "Hand Ridge Coefficient: "
print ((ridge.coef_[1] * cars93['MPG.city'])**2) + ((ridge.coef_[0] * cars93['MPG.city'])) + ridge.intercept_

plt.title("Polynomial Regression")
plt.plot(MPG_city, ridge.predict(MPG_city_squared))
plt.show()
