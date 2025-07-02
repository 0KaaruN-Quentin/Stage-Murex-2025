import numpy as np
from random import *

def initialisation (l, c):
    res = np.random.randn(l, c)
    res1 = np.ones((l, 1))
    res = np.concatenate((res, res1), axis = 1)
    return res

print(initialisation(4,3))