# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(66)
# data = np.random.randn(20, 3)

data = np.array([[1.0, 2.0], [2.0, 2.5], [4.5, 5.0], [
                0.0, -1.0], [-1., 3.0], [-2.5, -4.4]])
labels = [-1, -1, 1, 1, -1, 1]

# labels = [np.random.choice([-1, 1]) for i in range(data.shape[0])]
# labels = [1 if i > 50 else -1 for i in data[:, -1]]
# initing w, b
w = np.random.randn(data.shape[-1])
b = np.random.randn()


def check(data, w, b, labels):
    temp = []
    for i in xrange(data.shape[0]):
        wxb = np.dot(data[i], w) + b
        result = -labels[i] * np.sign((np.dot(data[i], w[:]) + b))
        if result > 0:
            temp.append(i)
    return temp


wrong = check(data, w, b, labels)
nnn = 0.5
s = 0
flag = True
print len(wrong)
while flag:
    if len(wrong) == 0:
        print wrong
        print w, b
        flag = False
        break
    zjw = wrong.pop()
    index_i = data[zjw]
    w = w + nnn * labels[zjw] * index_i
    b = b + nnn * labels[zjw]
    wrong = check(data, w, b, labels)
    s = s + 1
    print '第{}步: {}'.format(s, len(wrong))
