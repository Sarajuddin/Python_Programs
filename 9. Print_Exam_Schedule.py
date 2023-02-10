# 9. Write a Python program to display the examination schedule.

roll = input("Enter your roll no. : ")
name = input("Enter your name : ")
sem = input("Enter semester : ")

print("\n\tYour Examination Schedule is here.......")

myTuple = (('01-01-2023', '02:00 PM - 05:00 PM', 'KCS-101', 'Math-I'), ('04-01-2023', '02:00 PM - 05:00 PM', 'KCS-102', 'Chemistry'), ('07-01-2023', '02:00 PM - 05:00 PM', 'KCS-103', 'C Language'), ('10-01-2023', '02:00 PM - 05:00 PM', 'KCS-101', 'Data Structure'))

print(f"\n\tDate\t\tTime\t\t\tSub-Code\tSub-Name")

for tup in myTuple:
    print(f"\t{tup[0]}\t{tup[1]}\t{tup[2]}\t\t{tup[3]}")