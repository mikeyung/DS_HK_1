from sklearn import datasets, metrics
from matplotlib import pyplot as plt

iris = datasets.load_iris()
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)

print("Number of mislabeled points : %d" % (iris.target != y_pred).sum())