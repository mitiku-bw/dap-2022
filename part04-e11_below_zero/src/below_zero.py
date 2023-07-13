#!/usr/bin/env python3
 
import pandas as pd
 
def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    df2 = df.loc[df['Air temperature (degC)'] < 0 ]
    df3 = df2.groupby(by='m', as_index=False).agg({'d': pd.Series.nunique})
    return df3["d"].sum()
 
def main():
    cold_days = below_zero()
    print(f"Number of days below zero: {cold_days}")
    
if __name__ == "__main__":
    main()