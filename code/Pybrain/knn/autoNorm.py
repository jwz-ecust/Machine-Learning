import numpy as np
'''
(a, b, c, d, e) --->  (0, b-a, c-a, d-a, e-a)
---> (0, b-a/e-a, c-a/e-a, d-a/e-a, 1)
'''


def autoNorm(dataset):
    minvals = dataset.min(axis=0)
    maxvals = dataset.max(axis=0)
    ranges = maxvals - minvals
    normdataset = np.zeros(dataset.shape)
    m = dataset.shape[0]
    normdataset = dataset - np.tile(minvals, (m, 1))
    normdataset = normdataset / np.tile(ranges, (m, 1))
    return normdataset, ranges, minvals


dataset = np.array([
    [0.8, 400, 0.5], [12, 13400, 0.9], [0, 20000, 1.1], [67, 3200, 0.1]
])

print autoNorm(dataset)
