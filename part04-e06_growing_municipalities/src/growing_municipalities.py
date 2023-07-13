#!/usr/bin/env python3
 
import pandas as pd
 
def growing_municipalities(df):
    column = df[df["Population change from the previous year, %"] > 0]
    proportion = column.size/df.size
    return proportion
 
def main():
    data = pd.read_csv("src/municipal.tsv", sep="\t")
    df = pd.DataFrame(data).set_index("Region 2018")
    df = df["Akaa": "Äänekoski"]
    print("Proportion of growing municipalities:", "{:.1%}".format(growing_municipalities(df)))
 
if __name__ == "__main__":
    main()
 