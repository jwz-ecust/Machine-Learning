from sklearn import datasets
from sklearn import random_projection
from sklearn import svm
import pickle
import numpy as np
'''
given an image,  represent in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
fit an estimator to predict the classes to which unseen samples belong
'''

# digits = datasets.load_digits()
#
# clf = svm.SVC(gamma=0.001, C=100.)
# clf.fit(digits.data[:-1], digits.target[:-1])
# print clf.predict(digits.data[-1:])
# print digits.target[-1]

# clf = svm.SVC()
# iris = datasets.load_iris()
# X, y = iris.data, iris.target
#
# clf.fit(X, y)
# s = pickle.dumps(clf)
# clf2 = pickle.loads(s)
#
# print clf2.predict(X[0:1]), y[0]

# rng = np.random.RandomState(0)
# X = rng.rand(10, 2000)
# X = np.array(X, dtype="float32")
# # print X.dtype
# transformer = random_projection.GaussianRandomProjection()
# X_new = transformer.fit_transform(X)
# print X_new.dtype
# # print X_new

iris = datasets.load_iris()
# clf = svm.SVC()
# clf.fit(iris.data, iris.target)
#
# print clf.predict(iris.data[:3])
#
#
# clf.fit(iris.data, iris.target_names[iris.target])
# print clf.predict(iris.data[:3])


print iris.target_names
