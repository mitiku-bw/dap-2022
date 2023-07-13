#!/usr/bin/env python3
 
import pandas as pd
 
def municipalities_of_finland():
    data = pd.read_csv("src/municipal.tsv", sep="\t")
    df = pd.DataFrame(data).set_index("Region 2018")
    return df["Akaa": "Äänekoski"]
    
def main():
    print(municipalities_of_finland())
    
if __name__ == "__main__":
    main()