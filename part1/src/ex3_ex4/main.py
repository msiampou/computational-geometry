from point import *
from plane import *
import numpy as np
import matplotlib.pyplot as plt
import time
RANGE_XY = 10000
def parse_input():
    points = []
    ch = raw_input("To autogenerate write ->AUTO<- else just type something: ")
    if ch != "AUTO":
        print("Give Points of the Plane in the form x,y to stop type ->quit<-: ")
        while True:
            in_str = raw_input()
            #sometimes i forget what i have to write :P
            if in_str == "quit" or in_str == "exit" or in_str == "stop":
                break
            in_str = in_str.split(",")
            points.append(Point(int(in_str[0]),int(in_str[1])))
    else:
        num_points = int(raw_input("Enter number of Points: "))
        points = np.array([Point(np.random.randint(0, RANGE_XY),np.random.randint(0, RANGE_XY)) for i in range(num_points)])
    return Plane(points)


def main():
    try:
        plane = parse_input()
    except:
        print("Error on input of the plane data points")
    #check for SAME X Points
    if plane.check_points() == True:
        print("***Found 2 Points with same x, Algorithm ends***")
        return
    choice = raw_input("Type (1) for Incremental / Type (2) for Gift Wrap")
    while True:
        if choice == "1":
            print(plane.incremental_convex_hull())
            break
        elif choice == "2":
            plane.gift_wrap_convex_hull()
            break
        else:
            print ("Wrong input Please choose again")

if __name__ == "__main__":
    main()