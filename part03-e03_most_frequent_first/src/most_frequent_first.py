#!/usr/bin/env python3
 
from operator import le
import numpy as np
from numpy.core.fromnumeric import argsort
from numpy.core.numeric import identity
 
def most_frequent_first(a, c):
    x = a[:, c]
    y = np.argsort(x)
    u, c = np.unique(x, return_counts=True)
    idx = np.argsort(-c)
    b = np.arange(len(x))
    counter = 0
    for i in range(len(idx)):
        for j in range( startAt(c, idx[i]), startAt(c, idx[i]) + c[idx[i]]):
            b[counter] = y[j]
            counter +=1
    return a[b]
def startAt(arr, index):
    sum = 0
    for i in range(index):
        sum += arr[i]
    return sum
 
 
def main():
    a = np.array([
                  [5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
                  [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
                  [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
                  [2, 3, 8, 1, 3, 3, 3, 7, 0, 1],
                  [9, 9, 0, 4, 7, 3, 2, 7, 2, 0],
                  [0, 4, 5, 5, 6, 8, 4, 1, 4, 9],
                  [8, 1, 1, 7, 9, 9, 3, 6, 7, 2],
                  [0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
                  [4, 4, 8, 4, 3, 7, 5, 5, 0, 1],
                  [5, 9, 3, 0, 5, 0, 1, 2, 4, 2]
                ])
    print(most_frequent_first(a, -1))
 
if __name__ == "__main__":
    main()
