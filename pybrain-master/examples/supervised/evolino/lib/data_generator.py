# -*- coding: utf-8 -*-
__author__ = 'Michael Isik'


from pybrain.datasets.sequential import SequentialDataSet

from numpy import array, sin, apply_along_axis, ones, arange


class SuperimposedSine(object):
    """ Small class for generating superimposed sine signals
    """

    def __init__(self, lambdas=[1.]):
        self.lambdas = array(lambdas, float)
        self.yScales = ones(self.lambdas.shape)

    def getFuncValue(self, x):
        val = 0.
        for i, l in enumerate(self.lambdas):
            print i, l, self.yScales[i]
            val += sin(x * l) * self.yScales[i]     # 这里x*l的单位不是度数
            print val
        return val

    def getFuncValues(self, x_array):
        values = apply_along_axis(self.getFuncValue, 0, x_array)
        return values


def generateSuperimposedSineData(sinefreqs, space, yScales=None):
    sine = SuperimposedSine(sinefreqs)
    if yScales is not None:
        sine.yScales = array(yScales)
    dataset = SequentialDataSet(0, 1)
    data = sine.getFuncValues(space)

    dataset.newSequence()
    for i in range(len(data)):
        dataset.addSample([], data[i])

    return dataset


sinefreqs = (0.2, 0.311, 0.42, 0.51, 0.74)
metascale = 8.
scale = 0.5 * metascale
stepsize = 0.1 * metascale
zz = SuperimposedSine(sinefreqs)
space = arange(1, 10)

a = zz.getFuncValue(space)
print a, space
