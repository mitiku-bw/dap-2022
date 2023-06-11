#!/usr/bin/env python3
 
import numpy as numpy
 
def get_row_vectors(a):
    return numpy.split(a, a.shape[0], axis=0)
    
def get_column_vectors(a):
    return numpy.split(a, a.shape[1], axis=1)
    
def main():
    numpy.random.seed(0)
    a=numpy.random.randint(0,10, (4,4))
    a=numpy.random.randint(0,10, (2,3))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))
 
if __name__ == "__main__":
    main()
