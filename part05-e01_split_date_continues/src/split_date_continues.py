#!/usr/bin/env python3
 
import pandas as pd
import numpy as np
 
days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1,13)))
 
def split_date(gg):
    df = gg.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
 
    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:,0]
 
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d
 
def split_date_continues():
    # This functoion reads the bicycle data set,
    # clean the data set of columns/rows that contain only missing values,
    # drops the Päivämäärä column and replaces it with its splitted components as before
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    wh = df.dropna(how="all")   # Default axis is 0
    wh1 = wh.dropna(axis=1, how="all")
    pd_left = split_date(wh1)
    pd_right = wh1.drop("Päivämäärä", axis=1)
    return pd.concat([pd_left,pd_right], axis=1)
 
def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())
 
 
if __name__ == "__main__":
    main()