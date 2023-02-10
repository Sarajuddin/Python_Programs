# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

n = int(input("Enter an integer : "))
for i in range(1,n+1):
    print(str(n)*i)