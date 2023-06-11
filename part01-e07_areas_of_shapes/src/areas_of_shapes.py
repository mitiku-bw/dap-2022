#!/usr/bin/env python3
 
import math
 
 
def main():
    # enter you solution here
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape not in ["triangle", "rectangle", "circle"]:
            if shape:
                print("Unknown shape!")
            else:
                break
        else:
            if shape == "triangle":
                base = float(input("Give base of the triangle: "))
                height = float(input("Give height of the triangle: "))
                area = base * height / 2
            elif shape == "rectangle":
                base = float(input("Give width of the rectangle: "))
                height = float(input("Give height of the rectangle: "))
                area = base * height
            else:
                radius = float(input("Give radius of the circle: "))
                area = math.pi*radius**2
            print("The area is %f" % area)
 
if __name__ == "__main__":
    main()
 