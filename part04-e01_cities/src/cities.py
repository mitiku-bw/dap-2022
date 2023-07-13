#!/usr/bin/env python3
 
import pandas as pd
import numpy as np
 
def cities():
    city = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    pop = [643272, 279044, 231853, 223027, 201810]
    area = [715.48, 528.03, 689.59, 240.35, 3817.52]
    df=pd.DataFrame({"Population": pop, "Total area": area}, index=city)
    return df
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()