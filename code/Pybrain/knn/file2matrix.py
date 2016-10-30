import numpy as np


def file2matrix(filename):
    fr = open(filename)
    arrayoline = fr.readlines()
    numberoflines = len(arrayoline)
    returnmatrix = np.zeros((numberoflines, 3))
    classlabervector = []
    index = 0
    for line in arrayoline:
        line = line.strip()
        listfromline = line.split('\t')
        returnmatrix[index, :] = listfromline[0:3]
        classlabervector.append(listfromline[-1])
    index += 1
    return returnmatrix, classlabervector


filepath = "E:/Dropbox/Machine-Learning/code/Pybrain/knn/datingTestSet.txt"
matrix, label = file2matrix(filepath)
print matrix
print label
