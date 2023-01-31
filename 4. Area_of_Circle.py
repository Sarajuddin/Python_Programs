# 4. Write a Python program which accepts the radius of a circle from the user and compute
# the area.

import math

radius = float(input("Enter the radius : "))
area = math.pi*radius**2

print(f"Area of Circle is : {area}")