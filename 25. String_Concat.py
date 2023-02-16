# 25. Write a Python program to concatenate all elements in a list into a string and return it.

def concatenate(arr):
    return "".join(arr)

arr = input("Enter numbers separated by space : ").split()
print(f"String is : {concatenate(arr)}")