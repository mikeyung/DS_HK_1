import re
import pandas as pd
from numpy import log, exp, mean
from sklearn import linear_model, feature_selection
import matplotlib.pyplot as plt

url = 'http://www-958.ibm.com/software/analytics/manyeyes/datasets/af-er-beer-dataset/versions/1.txt'

beer = pd.read_csv(url, delimiter="\t")
beer = beer.dropna()

def good(x):
  if x > 4.3:
    return 1
  else:
    return 0

beer['Good'] = beer['WR'].apply(good)

inputdata = beer[ ['Reviews', 'ABV'] ].values
good = beer['Good'].values

#input.hist()
#plt.show()

logm = linear_model.LogisticRegression()
logm.fit(inputdata, good)
logm.predict(inputdata)

print "      Model Intercept: ", logm.intercept_
print "    Model Coefficient: ", logm.coef_
print "          Model Score: ", logm.score(inputdata, good)

plt.title("Scatter of input and good")
plt.scatter(beer['Reviews'], beer['Good'])
plt.show()

plt.title("inputdata, Prediction ...")
plt.plot(inputdata, logm.predict(inputdata))
plt.show()

"""
"""

beer_types = ['Ale', 'Stout', 'IPA', 'Lager']
for t in beer_types:
	beer[t] = beer['Type'].str.contains(t) * 1

inputdata = beer[ ['Reviews', 'ABV', 'Ale', 'Stout', 'IPA', 'Lager']].values

fp_value = feature_selection.univariate_selection.f_regression(inputdata, good)

inputdata = beer[ ['ABV', 'Ale', 'Stout']].values
logm.fit(inputdata, good)
logm.predict(inputdata)

print "      Model Intercept: ", logm.intercept_
print "    Model Coefficient: ", logm.coef_
print "          Model Score: ", logm.score(inputdata, good)

