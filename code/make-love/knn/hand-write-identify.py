# -*- coding: utf-8 -*-
import numpy as np
import os
import operator
'''
K-邻近算法, 执行效率偏低
每次需要2000次距离计算, 每个距离包含了1024个纬度浮计算
'''


def img2vector(filename):
    returnvector = np.zeros((1, 1024))
    fr = open(filename)
    linestr = fr.readlines()
    for i in range(32):
        for j in range(32):
            returnvector[0, 32 * i + j] = int(linestr[i][j])
    return returnvector
    fr.close()


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(
        classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def handwritingclasstest():
    hwlabels = []
    path = '/Users/zhangjiawei/Dropbox/Machine-Learning/code/make-love/knn/digits'
    train_path = os.path.join(path, 'trainingDigits')
    test_path = os.path.join(path, 'testDigits')
    trainingfilelist = os.listdir(train_path)
    m = len(trainingfilelist)
    trainingmatrix = np.zeros((m, 1024))
    for i in range(m):
        filenamestr = trainingfilelist[i]
        filestr = filenamestr.split('.')[0]
        classnumstr = int(filestr.split('_')[0])
        hwlabels.append(classnumstr)
        trainingmatrix[i, :] = img2vector(
            os.path.join(train_path, filenamestr))
    testfilelist = os.listdir(test_path)
    errorcount = 0.0
    mytest = len(testfilelist)
    for i in range(mytest):
        filenamestr = testfilelist[i]
        filestr = filenamestr.split('.')[0]
        classnumstr = int(filestr.split('_')[0])
        vectorundertest = img2vector(os.path.join(test_path, filenamestr))
        classifierresult = classify0(
            vectorundertest, trainingmatrix, hwlabels, 3)
        if classifierresult != classnumstr:
            errorcount += 1
            print "the wrong file is: %s" % filenamestr
            print "the classifier came back with: %d, the real answer is: %d" % (classifierresult, classnumstr)
    print "\nthe total number of error is: %d" % errorcount
    print "\nthe error rate is: %f" % (errorcount / float(mytest))


handwritingclasstest()
