#Define a function gcd that prints the greatest common divisor
#of two positive integers m and n that are passed as parameters to the function.

def gcd(m, n):

    #gcd of two number cannot be greater than
    #the given two numbers. So we start with
    #1 and go till smaller of the two numbers

    if m < n:
        smaller = m
    else:
        smaller = n

    i = 1
    gcd = 1

    while i <= smaller:

        if (m%i == 0) and (n%i == 0):
            gcd = i

        i = i + 1

    print(gcd)

gcd(6, 15)
gcd(7, 29)
gcd(10, 30)