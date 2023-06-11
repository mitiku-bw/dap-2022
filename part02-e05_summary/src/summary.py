#!/usr/bin/env python3
 
import math
#from math import sqrt
import sys
 
def summary(filename):
    L=[]
    with open(filename) as f:
        for line in f:
            try:
                L.append(float(line))
            except ValueError:
                continue
    n = len(L)
    s = sum(L)
    a = s/n
    stddev = math.sqrt(sum( (x - a)**2 for x in L ) / (n-1))
    return s, a, stddev
 
def main():
    for filename in sys.argv[1:]:
        s, a, stddev = summary(filename)
        print("File: %s Sum: %f Average: %f Stddev: %f" % (filename, s, a, stddev))
    
if __name__ == "__main__":
    main()
