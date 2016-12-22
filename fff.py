from math import log


def calcShannonEnt(dataset):
    numEntries = len(dataset)
    labelCounts = {}
    shannonEnt = 0.0
    for featVec in dataset:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def splitDataSet(dataset, axis, value):
    retDataSet = []
    for featVec in dataset:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet





myDat = [[1, 1, 1, 2, 'yes'], [1, 2, 1, 2, 'yes'], [
    5, 0, 4, 1, 'no'], [0, 1, 2, 1, 'no'], [0, 1, 1, 4, 'no']]

print chooseBestFeatureToSplit(myDat)
