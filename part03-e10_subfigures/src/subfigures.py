#!/usr/bin/env python3
 
import numpy as np
import matplotlib.pyplot as plt
 
def subfigures(a):
    sorted_a = a[np.argsort(a[:,0])]
    x = sorted_a[:, 0]
    y = sorted_a[:, 1]
    s = sorted_a[:, 3]
    colors = a[:, 2]
    print(sorted_a, x, y, s)
 
    plt.subplot(1, 2, 1)    # Note the 1-indexing of subplots.
    plt.plot(x, y)
    plt.subplot(1, 2, 2)
    plt.scatter(x, y, s=s, c=colors )
    plt.show()
 
def main():
    a = np.array([[5,9, 100, 12], [7, 0, 150, 13], [2, 4, 1, 18 ]])  # Two-dimensional array
    subfigures(a)
if __name__ == "__main__":
    main()
 