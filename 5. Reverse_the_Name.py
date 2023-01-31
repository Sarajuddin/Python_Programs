# 5. Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them

fname = input("Enter first name : ")
lname = input("Enter last name : ")

fullname = fname+" "+lname
print(f"Reversed Name : {fullname[::-1]}")