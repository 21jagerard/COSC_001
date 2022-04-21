# Author: Anna Mikhailova
# Date: 09/29/21
# Purpose: Define a function that takes a positive integer year as parameter
# and prints all the leap years between the first year of the current day calendar, i.e year 1, and year.

# def all_leap(n):
#     count = 0
#     while count < n:
#         count += 4
#         print(count)
#
# year = int(input("Enter a year:"))
# print("The leap years between year 1 and year", year, "are:")
# all_leap(year)

def all_leap(year):
    n = 1
    while n <= year:
        if (n % 400 == 0):
            print(n)
            n += 1
        elif (n % 4 == 0) and (n % 100 != 0):
            n += 1
        elif (n % 100 == 0) and (n % 400 != 0):
            print(n)
            n += 1
        else:
            n += 1

all_leap(200)