import numpy as np
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm


iris = datasets.load_iris()

#t rain test split, 40% is for testing
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

clf = svm.SVC(kernel='linear', C=1).fit(x_train, y_train)
print('Linear')
print(clf.score(x_test, y_test))

#k = 5
scores = cross_validate(clf, iris.data, iris.target, cv=5)

print(scores['test_score'])
print(scores['test_score'].mean())

clf = svm.SVC(kernel='poly', gamma='scale', C=1).fit(x_train, y_train)

scores = cross_validate(clf, iris.data, iris.target, cv=5)
print('Polynomial')
print(scores['test_score'])
print(scores['test_score'].mean())
print('Added higher dimensionality caused overfitting')
