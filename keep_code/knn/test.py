import numpy as np
import operator

label = ['A', 'A', 'B', 'B']

dataset = np.array([[1., 1.1], [1., 1.], [0., 0.], [0., 0.1]])

inX = np.array([1.2, 1.0])
dataSetSize = dataset.shape[0]
diffMat = np.tile(inX,
                  (dataSetSize, 1), ) - dataset
a = diffMat**2
dis = np.sqrt(a.sum(axis=1))
print dis
print dis.argsort()
sss = dis.argsort()
# sorted_dist_indicies_answer = [1, 0, 3, 2]

classCount = {}
for i in range(3):
    v = label[sss[i]]
    classCount[v] = classCount.get(v, 0) + 1
sortclass = sorted(
    classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
print sortclass
