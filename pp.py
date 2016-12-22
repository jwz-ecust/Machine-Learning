# -*- coding: utf-8 -*-

import operator
from math import log


def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    shannonEnt = 0.0
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        bestInfoGain = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        print newEntropy
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    # ==> ['yes', 'yes', 'no', 'no', 'yes']
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):    # 数据都对应一个标签, 不需要分类了
        return classList[0]
    if len(dataSet[0]) == 1:   # 数据只有一个特征
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)     # 选择最好的特征的编号
    bestFeatLabel = labels[bestFeat]      # 对应的最好特征的标签内容
    myTree = {bestFeatLabel: {}}     # 建立一个树
    del labels[bestFeat]
    featValues = [example[bestFeat] for example in dataSet]
    print featValues
    uniqueVals = set(featValues)
    print uniqueVals
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(
            splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


myData = [[1, 1, 'yes'], [1, 1, 'yes'], [
    1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]

labels = ['zjw', 'cbb']

print chooseBestFeatureToSplit(myData)

# print createTree(myData, labels)
# answer:  {'cbb': {0: 'no', 1: {'zjw': {0: 'no', 1: 'yes'}}}}
