def is_leap(year):
    if year%400 == 0:
        print(True)
    elif year%100 == 0:
        print(False)
    elif year%4 == 0:
        print(True)
    else:
        print(False)

is_leap(2100)
is_leap(2000)
is_leap(2008)
is_leap(2019)