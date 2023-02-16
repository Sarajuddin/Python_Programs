# 23. Write a Python program to test whether a passed letter is a vowel or not.

s = input("Enter a character : ")
if len(s)>1:
    print("Please enter a single character.")
else:
    if s.lower()=='a' or s.lower()=='e' or s.lower()=='i' or s.lower()=='o' or s.lower()=='u':
        print("Passed charachter is a vowel")
    else:
        print("Passed charachter is not a vowel")