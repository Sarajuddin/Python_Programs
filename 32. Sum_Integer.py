# 32. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

a = int(input("Enter first Number : "))
b = int(input("Enter second Number : "))

sum = a+b
if sum >= 15 and sum <= 20:
    print(f"Sum is : 20")
else:
    print(f"Sum is : {sum}")