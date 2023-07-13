#!/usr/bin/env python3
 
import pandas as pd
 
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
 
def split_date_continues():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = split_date(df)
    df = df.drop("Päivämäärä", axis=1)
    result = pd.concat([d, df], axis=1)
    return result
 
def cycling_weather():
    df = pd.read_csv("src/kumpula-weather-2017.csv", sep=",")
    df2 = split_date_continues()
    lkey = ["Year", "Month", "Day"]
    rkey = ["Year", "m", "d"]
    merged_df = pd.merge(df2, df, left_on=lkey, right_on=rkey)
    merged_df = merged_df.drop(['m', 'd', 'Time', 'Time zone'], axis=1)
    return merged_df
 
def main():
    wh = cycling_weather()
    print("Shape:", wh.shape)
    print("Column names:\n", wh.columns)
    print(wh.head())
 
if __name__ == "__main__":
    main()