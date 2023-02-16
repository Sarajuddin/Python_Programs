# 15. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

def difference(num):
    diff = num - 17
    if diff > 17:
        return diff*2
    return abs(diff)
    

num = int(input("Enter an Integer : "))
ans = difference(num)
print(f"Here is the answer : {ans}")