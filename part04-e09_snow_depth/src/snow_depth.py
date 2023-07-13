#!/usr/bin/env python3
 
import pandas as pd
 
def snow_depth():
    wh = pd.read_csv("src/kumpula-weather-2017.csv", sep=",")
    wh2 = wh["Snow depth (cm)"]
    return wh2.max()
 
def main():
    print("Max snow depth: ", snow_depth())
 
if __name__ == "__main__":
    main()