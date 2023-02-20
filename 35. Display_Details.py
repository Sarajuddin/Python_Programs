# 35. Write a Python program to display your details like name, age, address in three different lines.

name = input("Enter your name : ")
age = input("ENter your age : ")
address = input("Enter your Address : ")

print("\tDetails are :\n\t---------------------------")
print(f"\tName : {name}\n\tAge : {age}\n\tAddress : {address}")