# 37. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

p = float(input("Enter Principle : "))
r = float(input("Enter Rate : "))
t = int(input("Enter years : "))

amount = p*(1+r/100)**t

print(f"After {t} years, the amount will be {amount}.")