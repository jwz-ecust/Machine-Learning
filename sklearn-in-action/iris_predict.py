from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report


iris = load_iris()

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=33)

ss = StandardScaler()
ss.fit_transform(x_train)
ss.transform(x_test)

# knn
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
y_knn = knn.predict(x_test)


#r random forest
random_forest = RandomForestClassifier()
random_forest.fit(x_train, y_train)
# print clf.score(x_test, y_test)
y_random_forest = random_forest.predict(x_test)


print classification_report(y_test, y_knn)
print classification_report(y_test, y_random_forest)
