#!/usr/bin/env python3
 
import pandas as pd
import numpy as np
 
def missing_value_types():
    nan_float = float("nan")
    state = ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"]
    yoi = [nan_float, 1917, 1776, 1523, nan_float,1992]
    president = [None, "Niinistö", "Trump", None, "Steinmeier","Putin"]
    df=pd.DataFrame({ "Year of independence": yoi, "President": president }, index=state)
    print(float("nan"))
    return df
               
def main():
    print(missing_value_types())
 
if __name__ == "__main__":
    main()