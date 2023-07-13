#!/usr/bin/env python3
 
import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype
 
def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    # Replace "New" with "Re"
    df = df.replace("New", "Re")
    df.LW = pd.to_numeric(df.LW, errors='coerce').fillna(40).astype(object)
    wh = df[ (df.Pos > df.LW) ]
    return wh
 
def main():
    print(special_missing_values())
 
if __name__ == "__main__":
    main()