# Author: Anna Mikhailova
# Date: 09/29/21
# Purpose: A leap year is defined as follows:
# a) A year is a leap year if it is divisible by 400  (Example: 2000)
# b) A year is a not a leap year if it is divisible by 100 but not by 400 (Example: 1900, 2100)
# c)  A year is a leap year if it is divisible by 4 but not by 100 (Example: 2008)
# d) All other years are not leap years
# Define a function is_leap that takes year (positive integer) as parameter and prints True or False.

def is_leap(n):
    if n % 400 == 0:
        print(True)
    elif (n % 100 == 0) and (n % 400 != 0):
        print(False)
    elif (n % 4 == 0) and (n % 100 != 0):
        print(True)
    else:
        print(False)

year = int(input("Enter the year you want to check:"))
is_leap(year)