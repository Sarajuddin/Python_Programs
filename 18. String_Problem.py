# 18. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

str1 = input("ENter a string : ")

if str1.startswith('Is'):
    print("No changes required")
else:
    print(f"New string is : {'Is'+str1}")