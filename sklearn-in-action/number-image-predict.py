from sklearn import datasets
from sklearn import svm
'''
given an image,  represent in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
fit an estimator to predict the classes to which unseen samples belong
'''

iris = datasets.load_iris()
digits = datasets.load_digits()

clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
print clf.predict(digits.data[-1:])
print digits.target[-1]
