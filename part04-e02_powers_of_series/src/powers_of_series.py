#!/usr/bin/env python3
 
import pandas as pd
import numpy as np
 
def powers_of_series(s, k):
    c = np.ones((s.size, k), dtype=int)
    for i in range(k):
        for j in range(s.size):
            c[j][i] = s.values[j]**(i+1)
    df = pd.DataFrame(c, index=s.index, columns=np.arange(1,k+1))
    return df
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))
    
if __name__ == "__main__":
    main()