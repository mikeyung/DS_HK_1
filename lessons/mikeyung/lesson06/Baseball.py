import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

baseball = pd.read_csv('/Users/michaelyung/DS_HK_1/data/baseball.csv')

lm = linear_model.LinearRegression()
log_lm = linear_model.LinearRegression()

hr = [ [x] for x in baseball['HR'].values]
rbi = [ [x] for x in baseball['RBI'].values]
r = [ [x] for x in baseball['R'].values]
g = [ [x] for x in baseball['G'].values]
sb = [ [x] for x in baseball['SB'].values]
height = [ [x] for x in baseball['height'].values]
weight = [ [x] for x in baseball['weight'].values]
yearid = [ [x] for x in baseball['yearID'].values]
salary = [ [x] for x in baseball['salary'].values]

# log_hr = np.log(baseball['HR'].values)
# log_salary = [ [x] for x in np.log(baseball['salary'].values)]

lm.fit(yearid, salary)

#log_lm.fit(log_salary, log_hr)

print "      Model Intercept: ", lm.intercept_
print "    Model Coefficient: ", lm.coef_
# print "  Log Model Intercept: ", log_lm.intercept_
# rint "Log Model Coefficient: ", log_lm.coef_

lm.predict(salary)
baseball['predict'] = lm.predict(salary)

#log_lm.predict(log_hr)
#baseball['log_predict'] = np.exp(log_lm.predict(log_hr))

plt.title("Scatter of yearID and the prediction")
plt.scatter(baseball['yearID'], baseball['predict'])
plt.show()

plt.title("yearID, Prediction ...")
plt.plot(yearid, lm.predict(salary))
plt.show()


