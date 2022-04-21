#Define a function that takes a positive integer year as parameter and
#prints all the leap years between the first year of the current
#day calendar, i.e year 1, and year.

def all_leap_years(year):
    i = 1
    while i <= year:
        if i % 400 == 0:
            print("year", i, "is a leap year")
        elif i % 100 == 0:
            print("year", i, "is not a leap year")
        elif i % 4 == 0:
            print("year", i, "is a leap year")
        else:
            print("year", i, "is not a leap year")

        i = i + 1

all_leap_years(1000)