#!/usr/bin/env python3
 
import numpy as np
 
def first_half_second_half(a):
    c = int(a.shape[1]/2)
    result = np.where(np.sum(a[:,:c], 1) > np.sum(a[:,c:], 1))
    d=np.array(a[result[0],:])
    return d
 
def main():
    a = np.array([[1, 3, 4, 2], [2, 2, 1, 2]])
    print(first_half_second_half(a))
 
if __name__ == "__main__":
    main()
