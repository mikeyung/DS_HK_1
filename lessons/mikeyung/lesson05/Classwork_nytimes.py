"""

Lesson 05 Classwork

Michael Yung
2014-02-12

"""

import pandas as pd

import matplotlib.pyplot as plt

from numpy import log, array
from numpy import exp, mean, log

from sklearn import linear_model

"""

NY Times Aggregate data

"""

def AG(x,y):
	return [ x, y]

nytimes = pd.read_csv('/Users/michaelyung/DS_HK_1/data/nyagg.csv')
nytimes['Age_gender'] = map(AG, nytimes['Age'], nytimes['Gender'])

print nytimes
print nytimes[:10]

# Fit the data

age = [[x] for x in nytimes['Age'].values]
gender = [[x] for x in nytimes['Gender'].values]
ctr = nytimes['Ctr'].values
age_gender = [[x] for x in nytimes['Age_gender'].values]

print age[:10]
print gender[:10]
print ctr[:10]
print age_gender[:10]

nytimes['log_age'] = log(nytimes['Age'])
nytimes['log_gender'] = log(nytimes['Gender'])
nytimes['log_ctr'] = log(nytimes['Ctr'])

log_age = [[x] for x in nytimes['log_age'].values]
log_gender = [[x] for x in nytimes['log_gender'].values]
log_ctr = nytimes['log_ctr'].values


print "==== Age ===="

regr_age = linear_model.LinearRegression()
regr_age.fit(age, ctr)

print "          Intercept :", regr_age.intercept_
print "               Coef :", regr_age.coef_
print "Sum of square error :", mean((regr_age.predict(age) - ctr) ** 2)
print " Score (~1 is good) :", regr_age.score(age, ctr)

plt.scatter(age, ctr)
plt.title("NYTimes - Predict by Age")
plt.plot(age, regr_age.predict(age), color='blue', linewidth=3)
plt.show()

print "==== Both Gender ===="

regr_gender = linear_model.LinearRegression()
regr_gender.fit(gender, ctr)

print "          Intercept :", regr_gender.intercept_
print "               Coef :", regr_gender.coef_
print "Sum of square error :", mean((regr_gender.predict(gender) - ctr) ** 2)
print " Score (~1 is good) :", regr_gender.score(gender, ctr)

plt.scatter(gender, ctr)
plt.title("NYTimes - Predict by both gender")
plt.plot(gender, regr_gender.predict(gender), color='blue', linewidth=3)
plt.show()

print "==== Male Gender ===="

nytimes_male = nytimes[nytimes['Gender']==1]
gender = [[x] for x in nytimes_male['Gender'].values]
ctr = nytimes_male['Ctr'].values
regr_male = linear_model.LinearRegression()
regr_male.fit(gender, ctr)

print "          Intercept :", regr_male.intercept_
print "               Coef :", regr_male.coef_
print "Sum of square error :", mean((regr_male.predict(gender) - ctr) ** 2)
print " Score (~1 is good) :", regr_male.score(gender, ctr)

plt.scatter(gender, ctr)
plt.title("NYTimes - Predict by Male Gender")
plt.plot(gender, regr_male.predict(gender), color='blue', linewidth=3)
plt.show()

print "==== Female Gender ===="

nytimes_female = nytimes[nytimes['Gender']==0]
gender = [[x] for x in nytimes_female['Gender'].values]
ctr = nytimes_female['Ctr'].values
regr_female = linear_model.LinearRegression()
regr_female.fit(gender, ctr)

print "          Intercept :", regr_female.intercept_
print "               Coef :", regr_female.coef_
print "Sum of square error :", mean((regr_female.predict(gender) - ctr) ** 2)
print " Score (~1 is good) :", regr_female.score(gender, ctr)

plt.scatter(gender, ctr)
plt.title("NYTimes - Predict by Female Gender")
plt.plot(gender, regr_female.predict(gender), color='blue', linewidth=3)
plt.show()



print "==== Age / Gender ===="

regr_age_gender = linear_model.LinearRegression()
regr_age_gender.fit(age_gender, ctr)

print "          Intercept :", regr_age_gender.intercept_
print "               Coef :", regr_age_gender.coef_
print "Sum of square error :", mean((regr_age_gender.predict(age_gender) - ctr) ** 2)
print " Score (~1 is good) :", regr_age_gender.score(age_gender, ctr)

plt.scatter(age_gender, ctr)
plt.plot(age_gender, regr_age_gender.predict(age_gender), color='blue', linewidth=3)
plt.show()
