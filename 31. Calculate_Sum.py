# 31. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

sum = 0
if a==b or b==c or c==a:
    print("Sum is : {}".format(sum))
else:
    sum = a+b+c
    print("Sum is : {}".format(sum))