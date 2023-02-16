# 24. Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

lst = list(map(int, input("Enter number separated by space : ").split()))
num = int(input("Enter number to find : "))

if num in lst:
    print("Entered number lies within the container.")
else:
    print("Element Not found")
