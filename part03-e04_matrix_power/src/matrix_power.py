#!/usr/bin/env python3
 
from functools import reduce
from operator import ge
import numpy as np
from numpy.core.defchararray import replace
 
def matrix_power(a, n):
    c = [a] * n 
    if n > 0:
        return reduce((lambda x, y: x @ y), c )
    if n < 0:
        c = [np.linalg.inv(a)] * abs(n)
        return reduce((lambda x, y: x @ y), c )
    else:
        return np.eye(len(a))
def main():
    np.random.seed(0)
    a = np.random.randint(0,10, (2,2))
    print(matrix_power(a, -1))
 
if __name__ == "__main__":
    main()
 