#!/usr/bin/env python3
 
import numpy as np
import math 
import matplotlib.pyplot as plt
 
def center(a):
    y,x = a.shape[:2]
    center_y,center_x = (x-1)/2, (y-1)/2
    return (center_x,center_y)
 
def radial_distance(a):
    #b = a.copy()
    h,w = a.shape[0],a.shape[1]
    cY,cX = center(a)
    c = np.zeros((h,w))
 
    for i in range(c.shape[0]):
        for j in range(c.shape[1]):
            c[i,j] = math.sqrt((i-cY)**2 + (j-cX)**2)
 
    return c
 
def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    if a.min()==a.max():
        return a*0
    else:    
        return np.interp(a, (a.min(), a.max()), (tmin, tmax))
 
 
def radial_mask(a):
    return np.abs(scale(radial_distance(a)) - 1)
 
def radial_fade(a):
    return radial_mask(a)[:, :, np.newaxis]*a
 
 
def main():
    a = plt.imread("src/painting.png")
    fig, ax = plt.subplots(3,1)
 
    x,y = center(a)
    radial_distance(a)    
    scale(a)
    ax[0].imshow(a)
    ax[1].imshow(radial_mask(a))
    ax[2].imshow(radial_fade(a))
    # ax[0].imshow(radial_fade(a))
    plt.show()
 
if __name__ == "__main__":
    main()
 