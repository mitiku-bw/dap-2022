#!/usr/bin/env python3
 
import pandas as pd
 
def top_bands():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df['Artist'] = df['Artist'].str.lower()
    df2 = pd.read_csv("src/bands.tsv", sep="\t")
    df2['Band'] = df2['Band'].str.lower()
    merged_df = df.merge(df2, left_on='Artist', right_on='Band')
    return merged_df
 
def main():
    wh = top_bands()
    print("Shape:", wh.shape)
    print("Column names:\n", wh.columns)
    print(wh.head())
 
if __name__ == "__main__":
    main()