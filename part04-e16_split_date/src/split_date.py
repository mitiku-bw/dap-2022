#!/usr/bin/env python3
 
import pandas as pd
import numpy as np
 
 
def split_date():
    data = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", header = 0, sep=";")
    data = data.dropna(axis=0, how='all')
    data = data.dropna(axis=1, how='all')
    data2 = data["Päivämäärä"].str.split(expand=True)
 
    paiva = ['ma', 'ti', 'ke', 'to', 'pe', 'la', 'su']
    day = ['Mon', 'Tue','Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    kuukausi = ['tammi', 'helmi', 'maalis','huhti','touko','kesä', 'heinä','elo','syys','loka','marras','joulu']
    month = [1,2,3,4,5,6,7,8,9,10,11,12]
    
    data2[0] = data2[0].replace(paiva, day)
    data2[2]=data2[2].replace(kuukausi, month)
       
 
    data2[4]= data2[4].str.split(":", expand=True)
 
    data2.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    
    
    return data2.astype({ 'Day': int, 'Year': int, 'Hour': int })
 
def main():
    print(split_date())
    return
       
if __name__ == "__main__":
    main()