print("Welcome to the circumference program")

import math 

def circumference():
    num = int(input("Enter the diameter of the circle"))
    ans =  math.pi * num
    print("The circumference is: ", ans)

circumference()