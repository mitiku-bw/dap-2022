#!/usr/bin/env python3
 
class Prepend(object):
    def __init__(self, start):
        self.start = start
 
    def write(self, char):
        print(self.start + char)
    
def main():
    p=Prepend("+++ ")
    p.write("Hello")
 
if __name__ == "__main__":
    main()

