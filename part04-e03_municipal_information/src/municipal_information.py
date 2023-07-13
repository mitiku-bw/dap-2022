#!/usr/bin/env python3
 
import pandas as pd
 
def main():
    return
#!/usr/bin/env python3
import pandas as pd
 
def main():
    data = pd.read_csv("src/municipal.tsv", sep="\t")
    df = pd.DataFrame(data)
    print("Shape:", '{0[0]}, {0[1]}'.format(df.shape))
    print("Columns:", *df.columns, sep = "\n")
 
if __name__ == "__main__":
    main()
 
 
if __name__ == "__main__":
    main()
 