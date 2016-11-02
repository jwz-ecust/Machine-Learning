# -*- coding: utf-8 -*-
'''
kNN: k Nearest Neighbors

Input:      inX: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)

Output:     the most popular class label
'''

from numpy import *
import operator
from os import listdir


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
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


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def file2matrix(filename):
<<<<<<< HEAD
    data = loadtxt(filename)
    returnMat, classLaberVector = data[:, 0:3], data[:, -1]
    classlabelvector  = classLaberVector.astype(int)
    return returnMat, classlabelvector
=======
    fr = open(filename)
    lines = fr.readlines()
    numberOfLines = len(lines)  #get the number of lines in the file
    returnMat = zeros((numberOfLines, 3))  #prepare matrix to return
    classLabelVector = []  #prepare labels return
    index = 0
    for line in lines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    fr.close()
    return returnMat, classLabelVector
>>>>>>> f08d54db75abb441c25ebffad608f8cf9e77cccc


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))  #element wise divide
    return normDataSet, ranges, minVals


def datingClassTest():
    hoRatio = 0.50  # 50%的数据进行训练, 50%的数据作为验证
<<<<<<< HEAD
    datingDataMat, datingLabels = file2matrix('/Users/zhangjiawei/\
Dropbox/Machine-Learning/code/make-love/knn/datingTestSet2.txt')
    # load dataset from file
=======
    datingDataMat, datingLabels = file2matrix('/Users/zhangjiawei/Dropbox/Machine-Learning\
/code/make-love/knn/datingTestSet2.txt')  #load data setfrom file
>>>>>>> f08d54db75abb441c25ebffad608f8cf9e77cccc
    # 首先对数据进行归一化
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :],
                                     datingLabels[numTestVecs:m], 3)
        print "the classifier came back with: %d, the real answer is: %d" % (
            classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print "the total error rate is: %f" % (errorCount / float(numTestVecs))
    print errorCount


def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect


def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')  #load the training set
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]  #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')  #iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]  #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print "the classifier came back with: %d, the real answer is: %d" % (
            classifierResult, classNumStr)
        if (classifierResult != classNumStr): errorCount += 1.0
    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount / float(mTest))


<<<<<<< HEAD
# datingClassTest()    # 分类器针对约会网站的测试代码




def classfyperson():
    resultlist = ['not at all', 'in small does', 'in large doss']
    percentTats = float(raw_input("percentage of time spent playing video games?"))
    ffMiles = float(raw_input("frequent filer miles earned per year?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    datingdatamat, datinglabels = file2matrix('/Users/zhangjiawei/Dropbox/Machine-Learning/code/make-love/knn/datingTestSet2.txt')
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0(inArr, datingdatamat, datinglabels, 3)
    print "you will probably like this person: ", resultlist[classifierResult - 1]

classfyperson()
=======
datingClassTest()    # 分类器针对约会网站的测试代码
>>>>>>> f08d54db75abb441c25ebffad608f8cf9e77cccc
