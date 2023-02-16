# 22. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

def count(mystr, n):
    count = 0
    if len(mystr) < 2:
        return mystr*n
    return mystr[:2]*n

mystr = input("Enter a string : ")
n = int(input("How many copies you want to print : "))
print(f"Expected output : {count(mystr, n)}")