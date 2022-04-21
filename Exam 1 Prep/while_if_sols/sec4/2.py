#Define a function factorial_limit2 that takes a positive integer limit
#as parameter and prints the largest number whose factorial is less
#than or equal to limit.

def factorial_limit2(limit):
    i = 1
    fact = 1

    while fact <= limit:
        i = i + 1
        fact = fact * i

    print(i - 1)

factorial_limit2(116)
factorial_limit2(120)
factorial_limit2(125)