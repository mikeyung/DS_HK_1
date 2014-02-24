"""
Lesson 8 - KNN
Michael Yung

How to find the best "K" ?

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets, feature_selection

#
# Various variables we'll need to set intially.
# Generate from 1 to 100, with step 2, i.e. odd numbers
#
n_neighbors = range(1, 101, 2)
np.random.seed(1234)

# Load in the data and seperate the class labels and input data
iris = datasets.load_iris()

X = iris.data[:, :4]
y = iris.target

# Create the training (and test) set using the rng in numpy
n = len(y) * .7

# set some to True, and others to False
ind = np.hstack((np.ones(n, dtype=np.bool), np.zeros(len(y) - n, dtype=np.bool)))
np.random.shuffle(ind)

X_train, X_test = X[ind], X[ind == False]
y_train, y_test = y[ind], y[ind == False]

# Or more concisely, but achieve the same result as the above block of code
idx = np.random.uniform(0, 1, len(X)) <= 0.3
X_train, X_test = X[idx], X[idx==False]
y_train, y_test = y[idx], y[idx==False]

# Loop through each neighbors value from 1 to 100 and append
# the scores
scores = []

for n in n_neighbors:
	#
	# Why only "n" is passed to it, but no training data is needed ?
	#
    clf = neighbors.KNeighborsClassifier(n, weights='uniform')
    clf.fit(X_train, y_train)    
    scores.append(clf.score(X_test, y_test))

plt.plot(n_neighbors, scores)
plt.show()

"""
Cross validations
"""

scores = []
#for k in range(5):
for n in [7, 9, 11, 13, 15]:
    np.random.shuffle(ind)
    X_train, X_test = X[ind], X[ind == False]
    y_train, y_test = y[ind], y[ind == False]
    clf = neighbors.KNeighborsClassifier(n, weights='uniform')
    clf.fit(X_train, y_train)
    scores.append(clf.score(X_test, y_test))

print scores
print np.mean(scores)

"""
Plot the model - with numbers of neighbors set as 11
"""

# Below returns highest signifiance for features 2 and 3
# (remember, Python uses index 0). 
feature_selection.f_classif(X, y)

h = .02  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

clf = neighbors.KNeighborsClassifier(11, weights='uniform')
clf.fit(X[:, 2:4], y)

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
x_min, x_max = X[:, 2].min() - 1, X[:, 2].max() + 1
y_min, y_max = X[:, 3].min() - 1, X[:, 3].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)

plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

# Plot also the training points
plt.scatter(X[:, 2], X[:, 3], c=y, cmap=cmap_bold)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("3-Class classification (k = %i, weights = '%s')"
         % (11, 'uniform'))

plt.show()