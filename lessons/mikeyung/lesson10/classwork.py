from sklearn import datasets, metrics, tree, cross_validation
from matplotlib import pyplot as plt

iris = datasets.load_iris()

y_pred = tree.DecisionTreeClassifier().fit(iris.data, iris.target).predict(iris.data)

print "Number of mislabeled points : %d" % (iris.target != y_pred).sum()
print "Absolutely ridiculously overfit score: %d" % (tree.DecisionTreeClassifier().fit(iris.data,
    iris.target).score(iris.data, iris.target))


clf = 
metrics.confusion_matrix(iris.target, clf.predict(iris.data))

