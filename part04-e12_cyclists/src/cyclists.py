#!/usr/bin/env python3
 
import pandas as pd
 
def cyclists():
    wh = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    # The dropna method of a DataFrame drops columns or rows that contain missing values from the DataFrame, depending on the axis parameter.
    wh1 = wh.dropna(how="all")   # Default axis is 0
    return wh1.dropna(axis=1, how="all")
 
 
def main():
    print(cyclists())
    
if __name__ == "__main__":
    main()