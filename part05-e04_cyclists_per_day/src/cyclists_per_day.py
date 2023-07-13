#!/usr/bin/env python3
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.indexes.base import Index
 
 
days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1, 13)))
 
def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
 
    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]
 
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d
 
 
def cyclists_per_day():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = split_date(df)
    d = d.drop(["Weekday", "Hour"], axis=1)
    df = df.drop(["Päivämäärä"], axis=1)
    result = pd.concat([d, df], axis=1)
    # group by year, month and day and get sum
    grouped_multiple = result.groupby(["Year", "Month", "Day"]).sum()
    return grouped_multiple
    
def main():
    wh = cyclists_per_day()
    test = wh.loc[(2017, 8,)]
    test.plot()
    plt.show()
 
 
if __name__ == "__main__":
    main()
 