import random
import numpy as np


def func_randomly_init_bia_wei(sizes):
    biases = [np.random.randn(y, 1) for y in sizes[1:]]
    weights = [np.random.randn(y, x)
                for x, y in zip(sizes[:-1], sizes[1:])]

    return (biases, weights)


def func_feedforward(a, biases, weights):

    for b, w in zip(biases, weights):
        a = sigmoid(np.dot(w, a)+b)
        
    return a


def sigmoid(z):
    
    return 1.0/(1.0+np.exp(-z))
