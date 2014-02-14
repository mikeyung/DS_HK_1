"""

Lesson 05 Classwork

Michael Yung
2014-02-12

"""

"""

Mammals data

"""

print "==== Plotting Mammals data ===="
import pandas as pd
import matplotlib.pyplot as plt

mammals = pd.read_csv('/Users/michaelyung/DS_HK_1/data/mammals.csv')

plt.title("Mammals - Body vs Brain size")
plt.scatter(mammals['body'], mammals['brain'])
plt.show()

#plt.hist(mammals['body'], bins=range(0, 10000, 100))
#plt.show()
#plt.hist(mammals['brain'], bins=range(0, 10000, 100))
#plt.show()

"""
Log to evenly space out ...
"""

print "==== log the Mammal data and plot again ===="
from numpy import log
from numpy import exp
from numpy import mean

mammals['log_body'] = log(mammals['body'])
mammals['log_brain'] = log(mammals['brain'])

plt.title("Mammals - Body vs Brain size - Log values")
plt.scatter(mammals['log_body'], mammals['log_brain'])
plt.show()

print "==== Using Linear Regression on the Mammal data ===="

from sklearn import linear_model

# Make the model object
regr = linear_model.LinearRegression()

# Fit the data
body = [[x] for x in mammals['body'].values]
brain = mammals['brain'].values
regr.fit(body, brain)

print "          Intercept :", regr.intercept_
print "               Coef :", regr.coef_
print "Sum of square error :", mean((regr.predict(body) - brain) ** 2)
print " Score (~1 is good) :", regr.score(body, brain)

plt.scatter(body, brain)
plt.title("Mammals - Body vs Brain size, with prediction")
plt.plot(body, regr.predict(body), color='blue', linewidth=3)
plt.show()

print "==== Using Linear Regression, cleaned data by applying log to the data ===="

regr2 = linear_model.LinearRegression()
# Fit the data
log_body = [[x] for x in mammals['log_body'].values]
log_brain = mammals['log_brain'].values
regr2.fit(log_body, log_brain)
print "          Intercept :", regr2.intercept_
print "               Coef :", regr2.coef_
print "Sum of square error :", mean((regr2.predict(log_body) - log_brain) ** 2)
print " Score (~1 is good) :", regr2.score(log_body, log_brain)

plt.scatter(log_body, log_brain)
plt.title("Mammals - Body vs Brain size Log values, with prediction")
plt.plot(log_body, regr2.predict(log_body), color='red', linewidth=3)
plt.show()

plt.title("Mammals - Body vs Brain size Normalized Log values, with prediction")
plt.scatter(log_body, log_brain)
plt.plot(body, regr.predict(body), exp(log_body), exp(regr2.predict(log_body)), color='blue', linewidth=3)
plt.show()

