# 16. Write a Python program to test whether a number is within 100 of 1000 or 2000.

num = int(input("Enter a number : "))
if num > 0 and num < 100:
    print(f"{num} lies within 100.")
elif num > 100 and num < 1000:
    print(f"{num} lies within 1000.")
elif num > 1000 and num < 2000:
    print(f"{num} lies within 2000.")
else:
    print("Enter a valid number....")