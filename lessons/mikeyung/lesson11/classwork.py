import numpy as np
import matplotlib.pyplot as plt

from sklearn import svm, datasets, metrics
iris = datasets.load_iris()
classifier = svm.SVC().fit(iris.data, iris.target)
classifier.predict(iris.data)

print metrics.classification_report(classifier.predict(iris.data), iris.target)

# get support vectors
classifier.support_vectors_

# get indices of support vectors
classifier.support_

# get number of support vectors for each class
classifier.n_support_

###

# To make plotting easier, let's just use the first two features.
# X = iris.data[:, :2]
# To make plotting easier, let's just use the last two features.
X = iris.data[:, 2:]
Y = iris.target
h = .02  # step size in the mesh

# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
# SVM regularization parameter

# Looks like value of C has no major effect to the generation (?)

C = 1  

svc = svm.SVC(kernel='linear', C=C).fit(X, Y)
rbf_svc = svm.SVC(kernel='rbf', gamma=1.5, C=C).fit(X, Y)
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, Y)
lin_svc = svm.LinearSVC(C=C).fit(X, Y)

# create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# title for the plots
titles = ['SVC with linear kernel',
          'SVC with RBF kernel',
          'SVC with polynomial (degree 3) kernel',
          'LinearSVC (linear kernel)']

for i, clf in enumerate((svc, rbf_svc, poly_svc, lin_svc)):
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    plt.subplot(2, 2, i + 1)
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    #
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
    plt.axis('off')
    #
    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)
    #
    plt.title(titles[i])

plt.show()

###

from pandas import DataFrame, read_csv

mammals = read_csv('http://bit.ly/1f2YPsC').sort('body')
lm = svm.SVR(kernel='linear', C=1e1)
lm_rbf = svm.SVR(kernel='rbf', C=1e1)

body = mammals[ ['body'] ].values
brain = mammals.brain.values

lm.fit(body, brain)
lm_rbf.fit(np.log(body), np.log(brain))

## Compare to the original log fit model, as well as other svm kernels:
from sklearn.linear_model import LinearRegression
logfit = LinearRegression().fit(np.log(body), np.log(brain))
mammals['log_regr'] = np.exp(logfit.predict(np.log(body)))
mammals['linear_svm'] = lm.predict(body)
mammals['rbf_svm'] = np.exp(lm_rbf.predict(np.log(body)))

plt.scatter(body, brain)
plt.plot(body, mammals['linear_svm'].values, c='r', label='linear svm')
plt.plot(body, mammals['rbf_svm'].values, c='g', label='gaussian svm')
plt.plot(body, mammals['log_regr'].values, c='b', label='linear regression')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend(loc=2)
plt.show()

for prediction in ('linear_svm', 'rbf_svm', 'log_regr'):
    print 'Mean Squared Error for', prediction, ':', metrics.mean_squared_error(mammals[ [prediction] ].values, mammals[ ['brain'] ].values)
    print 'R-Squared for', prediction, ':', metrics.r2_score(mammals[ [prediction] ].values, mammals[ ['brain'] ].values)
