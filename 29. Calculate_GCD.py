# 29. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

a = int(input("Enter first Number : "))
b = int(input("Enter second Number : "))

min_num = min(list((a,b)))

gcd = 0
for i in range(1, min_num+1):
    if a%i==0 and b%i==0:
        gcd = i

print(f"GCD of {a} and {b} is : {gcd}")