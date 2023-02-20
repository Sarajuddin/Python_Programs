# 33. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

def sumDiff(a, b):
    if a == b:
        return True
    elif a+b == 5:
        return True
    elif a-b == 5:
        return True
    else:
        return False

a = int(input("Enter first Number : "))
b = int(input("Enter second Number : "))

print("Result is : ", sumDiff(a, b))