# -*- coding: utf-8 -*-
# @Date    : 2017-03-14 23:01:45
# @Author  : "zhangjiawei"
# @Email  : "aaronzjw@icloud.com"
# @Link    : ${https://github.com/jwz-ecust}
# @Version : $Id$
# regressor prediction: house price of Boston

from sklearn.datasets import load_boston
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score
# mean_absolute_error, mean_squared_error

data = load_boston()
x, y = data.data, data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=33)    # 默认分割比例0.25

ss_x = StandardScaler()
ss_y = StandardScaler()
x_train = ss_x.fit_transform(x_train)
x_test = ss_x.transform(x_test)
y_train = ss_y.fit_transform(y_train)
y_test = ss_y.fit_transform(y_test)

lr = LinearRegression()
lr.fit(x_train, y_train)
y_lr = lr.predict(x_test)
sgd = SGDRegressor()
sgd.fit(x_train, y_train)
y_sgd = sgd.predict(x_test)
svr = SVR(kernel="rbf")
svr.fit(x_train, y_train)
y_svr = svr.predict(x_test)
knn = KNeighborsRegressor()
knn.fit(x_test, y_test)
y_knn = knn.predict(x_test)
gbr = GradientBoostingRegressor()
gbr.fit(x_train, y_train)
y_gbr = gbr.predict(x_test)


# r2_score
print lr.score(x_test, y_test)
print r2_score(y_test, y_lr)

print sgd.score(x_test, y_test)
print r2_score(y_test, y_sgd)

print svr.score(x_test, y_test)
print r2_score(y_test, y_svr)


print knn.score(x_test, y_test)
print r2_score(y_test, y_knn)

print gbr.score(x_test, y_test)
print r2_score(y_test, y_gbr)
# Grident Boosting Regressor is the best!
'''
0.653695874281
0.653695874281
0.641265650648
0.641265650648
0.705700759368
0.705700759368
0.742688488384
0.742688488384
0.824091358241
0.824091358241

'''

# # mean squared error
# print mean_squared_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(y_lr))
# print mean_squared_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(y_sgd))

# # mean absulote error
# print mean_absolute_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(y_lr))
# print mean_absolute_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(y_sgd))
