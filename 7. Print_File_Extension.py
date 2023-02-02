# 7. Write a Python program to accept a filename from the user and print the extension of that.

filename = input("Enter the filename : ")

lst = []
for i in range(1, len(filename)+1):
    if filename[-i] != '.':
        lst.append(filename[-i])
    else:
        lst.append(filename[-i])
        break
lst.reverse()
ext = "".join(lst)
print(f"File Extension is : {ext}")