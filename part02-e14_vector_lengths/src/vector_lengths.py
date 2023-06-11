#!/usr/bin/env python3
 
import numpy as numpy
 
def vector_lengths(a):
    return numpy.sqrt(numpy.sum(a**2, axis=1))
 
def main():
    numpy.random.seed(0)
    a=numpy.random.randn(10,3)
    print("a:", a)
    print("Lengths:", vector_lengths(a))
 
if __name__ == "__main__":
    main()
