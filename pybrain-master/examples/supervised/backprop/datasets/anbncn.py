#!/usr/bin/env python
__author__ = 'Tom Schaul, tom@idsia.ch and Daan Wierstra'

from pybrain.datasets import SequentialDataSet

# TODO: make it *real* AnBnCn


class AnBnCnDataSet(SequentialDataSet):
    """ A Dataset partially modeling an AnBnCn grammar. """

    def __init__(self):
        SequentialDataSet.__init__(self, 2, 1)

        self.newSequence()
        self.addSample([1, 1], [0])
        self.addSample([1, 2], [1])
        self.addSample([1, 3], [0])
        self.addSample([1, 4], [1])
        self.addSample([1, 5], [0])
        # print self.getField('sequence_index')
        self.addSample([1, 6], [1])

        self.newSequence()
        self.addSample([1, 2], [0])
        self.addSample([1, 3], [1])
        self.addSample([1, 4], [0])
        self.addSample([1, 5], [1])
        self.addSample([1, 6], [0])
        self.addSample([1, 7], [1])
        # print self.getField('sequence_index')
