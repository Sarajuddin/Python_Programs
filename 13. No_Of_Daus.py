# 13. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

day1, month1, year1 = list(map(int, input("Enter first date (DD/MM/YYYY) : ").split('/')))
day2, month2, year2 = list(map(int, input("Enter second date (DD/MM/YYYY) : ").split('/')))
y, m, d = 0, 0, 0
if year2 > year1:
    y = (year2 - year1)*365
if month2 > month1:
    m = (month2 - month1)*31
if day2 > day1:
    d = day2 - day1

print(f"Total days : {y+m+d}")