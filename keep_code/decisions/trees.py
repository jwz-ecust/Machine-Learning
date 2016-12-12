# -*- coding: utf-8 -*-
from math import log


def chooseBestFeatureToSplit(dataset):
    numFeature = len(dataset[0]) - 1
    baseEntropy = calcShannonEnt(dataset)
    print 'base entropy is {}'.format(baseEntropy)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeature):
        featList = [example[i] for example in dataset]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataset, i, value)
            prob = len(subDataSet) / float(len(dataset))
            newEntropy += prob * calcShannonEnt(subDataSet)
        print 'new entropy is {}'.format(newEntropy)
        infoGain = baseEntropy - newEntropy
        if infoGain > bestFeature:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def calcShannonEnt(dataset):
    # 计算基本的香农熵
    numEntries = len(dataset)
    laberlCounts = {}
    for featVec in dataset:
        currentLabel = featVec[-1]
        if currentLabel not in laberlCounts.keys():
            laberlCounts[currentLabel] = 0
        laberlCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in laberlCounts:
        pro = float(laberlCounts[key]) / numEntries
        shannonEnt -= pro * log(pro, 2)
    return shannonEnt


def splitDataSet(dataset, axis, value):
    retdataset = []
    for featVec in dataset:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retdataset.append(reducedFeatVec)
    return retdataset


mydata = [[1, 1, 'yes'],
          [1, 1, 'yes'],
          [0, 1, 'no'],
          [1, 1, 'yes'],
          [0, 1, 'yes'],
          [1, 1, 'yes'],
          [1, 1, 'yes'],
          [1, 1, 'yes'],
          [1, 1, 'yes'],
          [1, 1, 'yes'],
          [1, 1, 'no'],
          [1, 1, 'yes'],
          [1, 1, 'yes'],
          [1, 1, 'yes'],
          [1, 1, 'yes'],
          [1, 1, 'yes'],
          [1, 1, 'yes'],
          [1, 1, 'yes'],
          [1, 1, 'yes']]

print chooseBestFeatureToSplit(mydata)
