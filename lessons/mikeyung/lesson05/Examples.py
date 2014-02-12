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


import pandas as pd
import matplotlib.pyplot as plt
mammals = pd.read_csv('/Users/michaelyung/DS_HK_1/data/class/mammals.csv')
plt.scatter(mammals['body'], mammals['brain'])
plt.show()
plt.hist(mammals['body'], bins=range(0, 10000, 100))
plt.show()
plt.hist(mammals['brain'], bins=range(0, 10000, 100))
plt.show()

from numpy import log
mammals['log_body'] = log(mammals['body'])
mammals['log_brain'] = log(mammals['brain'])
plt.scatter(mammals['log_body'], mammals['log_brain'])


