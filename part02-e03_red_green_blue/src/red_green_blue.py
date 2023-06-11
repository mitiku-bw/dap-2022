#!/usr/bin/env python3
 
import re
 
def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)
 
def red_green_blue():
    filename="rgb.txt"
    with open(get_path(filename)) as f:
        lines = f.readlines()
    result=[]
    for line in lines[1:]:
        m = re.match(r"\s*(\d+)\s+(\d+)\s+(\d+)\s+(.+)", line)
        result.append("\t".join(m.groups()))
        
    return result
 
 
def main():
    lines = red_green_blue()
    for line in lines:
        print(line)
 
if __name__ == "__main__":
    main()
 