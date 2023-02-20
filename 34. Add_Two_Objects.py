# 34. Write a Python program to add two objects if both objects are an integer type.

a = eval(input("Enter first Number : "))
b = eval(input("Enter second Number : "))

if type(a) is int and type(b) is int:
    print("Sum is : ", a+b)
else:
    print("Both numbers are not of the same type")