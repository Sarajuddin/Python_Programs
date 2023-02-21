# 38. Write a Python program to compute the distance between the points (x1, y1) and (x2,y2).

x1 = int(input("Value of x1 : "))
y1 = int(input("Value of y1 : "))
x2 = int(input("Value of x2 : "))
y2 = int(input("Value of y2 : "))

distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

print(f"Distance between {x1, y1} and {x2, y2} is : {distance}")