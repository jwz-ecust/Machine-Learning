from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report

digit = load_digits()

x_train, x_test, y_train, y_test = train_test_split(digit.data, digit.target)


ss = StandardScaler()
x_train = ss.fit_transform(x_train)
x_test = ss.transform(x_test)

clf = SVC()
clf.fit(x_train, y_train)
y_pre = clf.predict(x_test)
print classification_report(y_test, y_pre)
