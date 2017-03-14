# -*- coding: utf-8 -*-
# @Date    : 2017-03-14 19:21:41
# @Author  : "zhangjiawei"
# @Email  : "aaronzjw@icloud.com"
# @Link    : ${https://github.com/jwz-ecust}
# @Version : $Id$

import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.ensemble import GradientBoostingClassifier

titantic = pd.read_csv(
    "http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")

print titantic.columns

# ['row.names', 'pclass', 'survived', 'name', 'age', 'embarked',
#     'home.dest', 'room', 'ticket', 'boat', 'sex']

x = titantic[["pclass", "age", "sex"]]
# print x

x['age'].fillna(x['age'].mean(), inplace=True)

# 对没有记录年龄的数据，填充为平均值，这样对整体数据的影响较小
# print x
# print x['sex']
y = titantic['survived']
# print y

x_train, x_test, y_train, y_test = train_test_split(x, y)

vec = DictVectorizer(sparse=False)
x_train = vec.fit_transform(x_train.to_dict(orient="record"))
x_test = vec.transform(x_test.to_dict(orient="record"))


knn = KNeighborsClassifier()
random_forest = RandomForestClassifier()
gbc = GradientBoostingClassifier()


knn.fit(x_train, y_train)
random_forest.fit(x_train, y_train)
gbc.fit(x_train, y_train)

y_knn = knn.predict(x_test)
y_random_forest = random_forest.predict(x_test)
y_gbc = gbc.predict(x_test)

print classification_report(y_test, y_knn)
print classification_report(y_test, y_random_forest)
print classification_report(y_test, y_gbc)
