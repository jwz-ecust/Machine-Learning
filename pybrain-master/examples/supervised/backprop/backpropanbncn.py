from __future__ import print_function    # use print function in python3
#!/usr/bin/env python
# A simple recurrent neural network that learns a simple sequential data set.

__author__ = 'Tom Schaul, tom@idsia.ch and Daan Wierstra, review by zjw@ecust'

from datasets import AnBnCnDataSet    # @UnresolvedImport
from pybrain.supervised import BackpropTrainer
from pybrain.structure import FullConnection, RecurrentNetwork, TanhLayer, LinearLayer, BiasUnit


def testTraining():
    # the AnBnCn dataset (sequential)
    d = AnBnCnDataSet()

    # build a recurrent network to be trained
    hsize = 2
    n = RecurrentNetwork()
    n.addInputModule(LinearLayer(2, name='in'))
    n.addModule(TanhLayer(hsize, name='h'))
    n.addModule(BiasUnit(name='bias'))
    n.addOutputModule(LinearLayer(1, name='out'))
    n.addConnection(FullConnection(n['in'], n['h']))
    n.addConnection(FullConnection(n['bias'], n['h']))
    n.addConnection(FullConnection(n['h'], n['out']))
    n.addRecurrentConnection(FullConnection(n['h'], n['h']))
    n.sortModules()

    # initialize the backprop trainer and train (100 times)
    t = BackpropTrainer(n, learningrate=0.1, momentum=0.0, verbose=True)
    t.trainOnDataset(d, 100)

    # the resulting weights are in the network:
    print('Final weights:', n.params)

if __name__ == '__main__':
    testTraining()
