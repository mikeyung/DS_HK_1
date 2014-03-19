import random
from pandas import read_csv
from sklearn.cross_validation import train_test_split
from sklearn.ensemble.forest import ExtraTreesClassifier
from sklearn import metrics
from sklearn import preprocessing
authorship = read_csv('http://people.stern.nyu.edu/jsimonof/AnalCatData/Data/Comma_separated/authorship.csv')
authors = list(set(authorship.Author.values))
le = preprocessing.LabelEncoder()
le.fit(authors)
authorship['Author_num'] = le.transform(authorship['Author'])

# Create a random variable (random forests work best with a random variable)
authorship['random'] = [random.random() for i in range(841)]

#What are some of the stop words we're looking at?
features = list(authorship.columns)
print features
features.remove('Author')
features.remove('Author_num')
print features

# create a test and training set
x_train, x_test, y_train, y_test = train_test_split(authorship[features], authorship.Author_num.values, test_size=0.4, random_state=123)


# Fit Model
etclf = ExtraTreesClassifier(n_estimators=20)
etclf.fit(x_train, y_train)

# Print Confusion Matrix
print "=== Confusion matrix ==="
print metrics.confusion_matrix(etclf.predict(x_test), y_test)