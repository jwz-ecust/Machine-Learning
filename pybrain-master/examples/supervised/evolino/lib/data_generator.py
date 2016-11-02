__author__ = 'Michael Isik'


from pybrain.datasets.sequential import SequentialDataSet

from numpy import array, sin, apply_along_axis, ones, arange


class SuperimposedSine(object):
    """ Small class for generating superimposed sine signals
    """

    def __init__(self, lambdas=[1.]):
        self.lambdas = array(lambdas, float)
        self.yScales = ones(len(self.lambdas))

    def getFuncValue(self, x):
        val = 0.
        for i, l in enumerate(self.lambdas):
            val += sin(x * l) * self.yScales[i]
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

trnInputSpace = arange(0 * scale, 190 * scale, stepsize)
trnData = generateSuperimposedSineData(sinefreqs, trnInputSpace)

tstInputSpace = arange(400 * scale, 540 * scale, stepsize)
tstData = generateSuperimposedSineData(sinefreqs, tstInputSpace)

zjw = SuperimposedSine(sinefreqs)
print zjw.getFuncValue(trnInputSpace)
print zjw.getFuncValues(trnInputSpace)
