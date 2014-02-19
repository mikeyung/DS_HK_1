import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

mammals = pd.read_csv('/Users/michaelyung/DS_HK_1/data/mammals.csv')

lm = linear_model.LinearRegression()
log_lm = linear_model.LinearRegression()

body = [ [x] for x in mammals['body'].values]
log_body = [ [x] for x in np.log(mammals['body'].values)]

brain = mammals['brain'].values
log_brain = np.log(mammals['brain'].values)

lm.fit(body, brain)
log_lm.fit(log_body, log_brain)

print "      Model Intercept: ", lm.intercept_
print "    Model Coefficient: ", lm.coef_
print "  Log Model Intercept: ", log_lm.intercept_
print "Log Model Coefficient: ", log_lm.coef_

lm.predict(body)
mammals['predict'] = lm.predict(body)

log_lm.predict(log_body)
mammals['log_predict'] = np.exp(log_lm.predict(log_body))

# Sort by response:
mammals = mammals.sort('brain')
# Sort by prediction:
mammals_log_sort = mammals.sort('log_predict')

plt.title("Scatter of brain and the prediction")
plt.scatter(mammals['brain'], mammals['predict'])
plt.show()
plt.title("Body, Prediction and Log Body ...")
plt.plot(body, lm.predict(body), np.exp(log_body),np.exp(log_lm.predict(log_body)))
plt.show()

"""
Polynomial Regression 
"""

mammals['body_squared'] = mammals['body']**2
body_squared = [ [x, y] for x,y in zip(mammals['body'].values, mammals['body_squared'].values)]

ridge = linear_model.Ridge()
ridge.fit(body_squared, brain)

print "=== Polynomial Regression ==="
print "      Ridge Intercept: ", ridge.intercept_
print "    Ridge Coefficient: ", ridge.coef_

print ((ridge.coef_[1] * mammals['body'])**2) + ((ridge.coef_[0] * mammals['body'])) + ridge.intercept_

ridge.predict(body_squared)
mammals['ridge'] = ridge.predict(body_squared)

plt.title("Polynomial Regression")
plt.plot(body, ridge.predict(body_squared))
plt.show()
