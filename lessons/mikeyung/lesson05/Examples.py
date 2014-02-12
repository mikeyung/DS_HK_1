from numpy import array, dot
from scipy.linalg import inv

X = array([ [1, 1], [1, 2], [1, 3], [1, 4] ])
y = array([ [1], [2], [3], [4] ])
n = inv(dot(X.T, X))
k = dot(X.T, y)

coef_ = dot(n, k)

print "==== Step by step ==="
print coef_

"""
Or we can do that ...
"""

def regression(input, response):
    return dot(inv(dot(input.T, input)), dot(input.T, response))

print "==== thru the regression function ==="
print regression(X, y)

print "==== Plotting data ===="
import pandas as pd
import matplotlib.pyplot as plt
mammals = pd.read_csv('/Users/michaelyung/DS_HK_1/data/mammals.csv')

plt.scatter(mammals['body'], mammals['brain'])
plt.show()
plt.hist(mammals['body'], bins=range(0, 10000, 100))
plt.show()
plt.hist(mammals['brain'], bins=range(0, 10000, 100))
plt.show()

"""
Log to evenly space out ...
"""

print "==== log the data ===="
from numpy import log
mammals['log_body'] = log(mammals['body'])
mammals['log_brain'] = log(mammals['brain'])
plt.scatter(mammals['log_body'], mammals['log_brain'])
plt.show()

print "==== Using Linear Regression ===="

from sklearn import linear_model
# Make the model object
regr = linear_model.LinearRegression()
# Fit the data
body = [[x] for x in mammals['body'].values]
brain = mammals['brain'].values
regr.fit(body, brain)

plt.scatter(body, brain)
plt.plot(body, regr.predict(body), color='blue', linewidth=3)
plt.show()



