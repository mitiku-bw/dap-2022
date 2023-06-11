#!/usr/bin/env python3
 
import numpy as np
import scipy.linalg
 
def vector_angles(X, Y):
    ip=np.sum(X*Y, axis=1)
    print("Inner product:", ip)
    Xlen = scipy.linalg.norm(X, 2, axis=1)
    Ylen = scipy.linalg.norm(Y, 2, axis=1)
    print("Xlen:", Xlen)
    print("Ylen:", Ylen)
    temp=ip/(Xlen*Ylen)
    temp = np.clip(temp, -1.0, 1.0)
    print(temp)
    result =  np.arccos(temp) / np.pi * 180
    print(result)
    return result
 
def main():
    np.random.seed(0)
    X=np.random.randn(10,3)
    Y=np.random.randn(10,3)
    print(vector_angles(X, Y))
    A=np.array([[0,0,1], [-1,1,0]])
    B=np.array([[0,1,0], [1,1,0]])
    print(vector_angles(A, B))
    
if __name__ == "__main__":
    main()
