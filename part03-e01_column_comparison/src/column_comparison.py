#!/usr/bin/env python3
 
import numpy as np
 
def column_comparison(matrix):
    # Get the index of elements where second column is greater than second last column
    result = np.where(matrix[:,1:2] > matrix[:,-2:-1])
    d=np.array(matrix[result[0],:])
    return d
    
def main():
    # Create a matrix
    matrix = np.array([[8,9,3,8,8],[0,5,3,9,9],[5,7,6,0,4],[7,8,1,6,2],[2,1,3,5,8]])
    print(column_comparison(matrix))
 
if __name__ == "__main__":
    main()
