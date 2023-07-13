#!/usr/bin/env python3
 
import pandas as pd
 
def swedish_and_foreigners():
    data = pd.read_csv("src/municipal.tsv", sep="\t")
    df = pd.DataFrame(data).set_index("Region 2018")
    df = df["Akaa": "Äänekoski"]
    df = df[(df["Share of Swedish-speakers of the population, %"] > 5) & (df["Share of foreign citizens of the population, %"] > 5)]
    return df[["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]
    
def main():
    print(swedish_and_foreigners())
 
if __name__ == "__main__":
    main()
 