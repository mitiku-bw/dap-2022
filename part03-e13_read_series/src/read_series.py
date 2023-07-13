#!/usr/bin/env python3
import pandas as pd    # This is the standard way of importing the Pandas library
import numpy as np
 
def read_series():
    index = ""
    values = []
    print("Please write an index and value. Both are strings separated \nby whitespace, f.ex 'a 14'. Empty ends repeat.")    
 
    while True:
        i = input("Input index followed by value: ")
        
        if i == "" :
            break
        else :
            try :
                i = i.rstrip()
                arr = i.split()
                if len(arr) != 2 :
                    print("Input was malformed. Please try again. Make sure to add both index \nand value and separate them with a space. Empty ends repeat.")
                    continue
                else :
                    index += arr[0]
                    values.append(arr[1])
            except :
                print("Input was malformed. Please try again. Make sure to add both index \nand value and separate them with a space. Empty ends repeat.")
                continue
 
    series = pd.Series(values, index=list(index))
    print("index length:", len(index))
    return series
 
def main():
    series = read_series()
    print(f"dtype: {series.dtype}, size: {series.size}")
    print(series)
 
if __name__ == "__main__":
    main()
 