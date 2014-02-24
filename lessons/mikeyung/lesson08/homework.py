import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from numpy import log, exp, mean
from sklearn import linear_model, feature_selection, neighbors, datasets
from matplotlib.colors import ListedColormap

"""
Beers using logistic Regression

"""

logm = linear_model.LogisticRegression()

def score(input, response):
  logm.fit(input, response)
  score = logm.score(input, good)
  print 'R^2 Score : %.03f' % (score)

def good(x):
  if x > 4.3:
    return 1
  else:
    return 0

url = 'http://www-958.ibm.com/software/analytics/manyeyes/datasets/af-er-beer-dataset/versions/1.txt'

beer = pd.read_csv(url, delimiter="\t")
beer = beer.dropna()
beer['Good'] = beer['WR'].apply(good)

# Original attempt

input = beer[ ['Reviews', 'ABV'] ].values
good = beer['Good'].values

score(input, good)

# Second attempt, with beer types

beer_types = ['Ale', 'Stout', 'IPA', 'Lager']

for t in beer_types:
	beer[t] = beer['Type'].str.contains(t) * 1

select = ['Reviews', 'ABV', 'Ale', 'Stout', 'IPA', 'Lager']
input = beer[select].values

score(input, good)

# Third attempt, with beer breweries

dummies = pd.get_dummies(beer['Brewery'])
input = beer[select].join(dummies.ix[:, 1:])

score(input, good)

"""
KNN model now ... give it a try
"""

def good2(x):
  if x > 4.3:
    return 1
  else:
    return 0


n_neighbors = range(1, 101, 2)
np.random.seed(1234)

beer2 = pd.read_csv(url, delimiter="\t")
beer2 = beer2.dropna()

print beer2
beer2['Good'] = beer2['WR'].apply(good2)

print beer2
print beer2[:10]

X = beer2['ABV', 'WR']
y = beer2['Good']

print X
print y

# Create the training (and test) set using the rng in numpy
n = len(y) * .7

# Or more concisely, but achieve the same result as the above block of code
idx = np.random.uniform(0, 1, len(X)) <= 0.3
X_train, X_test = X[idx], X[idx==False]
y_train, y_test = y[idx], y[idx==False]

