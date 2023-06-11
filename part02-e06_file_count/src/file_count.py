#!/usr/bin/env python3
 
import sys
 
def file_count(filename):
    lines=0
    words=0
    characters=0
    with open(filename) as f:
        for line in f:
            lines += 1
            words += len(line.split())
            characters += len(line)
           
    return (lines, words, characters)
 
def main():
    for filename in sys.argv[1:]:
        lines, words, characters = file_count(filename)
        print("%i\t%i\t%i\t%s" % ( lines, words, characters, filename))
 
if __name__ == "__main__":
    main()
