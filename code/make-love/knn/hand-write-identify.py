import numpy as np


def img2vector(filename):
    returnvector = np.zeros((1, 1024))
    fr = open(filename)
    linestr = fr.readlines()
    for i in range(32):
        for j in range(32):
            returnvector[0, 32*i+j] = int(linestr[i][j])
    return returnvector
    fr.close()


path = '/Users/zhangjiawei/Dropbox/Machine-Learning/code/make-love/knn/digits/testDigits/0_0.txt'
print img2vector(path)
