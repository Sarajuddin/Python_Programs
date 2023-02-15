# 19. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

mystr = "Hello "
n = int(input("Enter a number : "))

print(mystr*abs(n))