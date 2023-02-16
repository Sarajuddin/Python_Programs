# 21. Write a Python program to count the number 4 in a given list.

myList = list(map(int, input("Enter number : ").split()))

target = 4
print(f"Total count of {target} are : {myList.count(target)}")