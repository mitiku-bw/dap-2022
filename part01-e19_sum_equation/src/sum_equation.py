#!/usr/bin/env python3
 
def sum_equation(L):
    if not L:
        return "0 = 0"
    s = sum(L)
    result = list(map(str, L))
    result[-1] = result[-1] + (" = %i" % s)
    return " + ".join(result)
 
def main():
    print(sum_equation([1, 5, 7]))
 
if __name__ == "__main__":
    main()
 