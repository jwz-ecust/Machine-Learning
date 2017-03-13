from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
import numpy as np


X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
y = [0, 0, 1, 1, 2]

classif = OneVsRestClassifier(estimator=SVC(random_state=0))
y_pre = classif.fit(X, y).predict(X)
print y_pre


yy = LabelBinarizer().fit_transform(y)
print yy


zjw = [1,2,3,4,5,6,0,0,1,1,3,4]
zzz = LabelBinarizer().fit_transform(zjw)
print zzz

# print type(zzz)
b = np.arange(zzz.shape[1])
b = b.reshape((zzz.shape[1],1))
print zzz.dot(b)

# print dir(zzz)
