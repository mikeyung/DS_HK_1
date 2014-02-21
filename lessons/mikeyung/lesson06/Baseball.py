import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

baseball = pd.read_csv('/Users/michaelyung/DS_HK_1/data/baseball.csv')
#baseball = baseball.fillna(0)

lm = linear_model.LinearRegression()
#log_lm = linear_model.LinearRegression()

hr = [ [x] for x in baseball['HR'].values]
rbi = [ [x] for x in baseball['RBI'].values]
r = [ [x] for x in baseball['R'].values]
g = [ [x] for x in baseball['G'].values]
sb = [ [x] for x in baseball['SB'].values]
height = [ [x] for x in baseball['height'].values]
weight = [ [x] for x in baseball['weight'].values]
yearid = [ [x] for x in baseball['yearID'].values]
salary = [ [x] for x in baseball['salary'].values]


#log_yearid = np.log(baseball['yearID'].values)
#log_salary = [ [x] for x in np.log(baseball['salary'].values)]

lm.fit(yearid, salary)

#log_lm.fit(log_yearid, log_salary)

print "      Model Intercept: ", lm.intercept_
print "    Model Coefficient: ", lm.coef_
#print "  Log Model Intercept: ", log_lm.intercept_
#print "Log Model Coefficient: ", log_lm.coef_

lm.predict(yearid)
baseball['predict'] = lm.predict(yearid)

#log_lm.predict(log_yearid)
#baseball['log_predict'] = np.exp(log_lm.predict(log_yearid))

plt.title("Scatter of yearID and the salary")
plt.scatter(baseball['yearID'], baseball['salary'])
plt.show()

plt.title("yearID, Prediction ...")
plt.plot(yearid, lm.predict(yearid))
plt.show()

#plt.title("Log yearID, Prediction ...")
#plt.plot(log_yearid, log_lm.predict(log_yearid))
#plt.show()


"""
Looks like recent years have higher salary
"""


lm_height = linear_model.LinearRegression()

lm_height.fit(height, salary)

# log_lm.fit(log_salary, log_hr)

print "      Model Intercept: ", lm_height.intercept_
print "    Model Coefficient: ", lm_height.coef_
# print "  Log Model Intercept: ", log_lm.intercept_
# rint "Log Model Coefficient: ", log_lm.coef_

lm_height.predict(height)
baseball['predict'] = lm_height.predict(height)

plt.title("Scatter of height and the salary")
plt.scatter(baseball['height'], baseball['salary'])
plt.show()

plt.title("height, Prediction ...")
plt.plot(height, lm.predict(height))
plt.show()

"""
Looks like taller player have higher salary
"""

lm_weight = linear_model.LinearRegression()

lm_weight.fit(weight, salary)

# log_lm.fit(log_salary, log_hr)

print "      Model Intercept: ", lm_weight.intercept_
print "    Model Coefficient: ", lm_weight.coef_
# print "  Log Model Intercept: ", log_lm.intercept_
# rint "Log Model Coefficient: ", log_lm.coef_

lm_weight.predict(weight)
baseball['predict'] = lm_weight.predict(weight)

plt.title("Scatter of weight and the salary")
plt.scatter(baseball['weight'], baseball['salary'])
plt.show()

plt.title("weight, Prediction ...")
plt.plot(weight, lm.predict(weight))
plt.show()

"""
Looks like lighter player have higher salary
"""

