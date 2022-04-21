#Define a function factorial_limit1 that takes a positive integer
#limit as parameter and prints the largest number whose
#factorial is strictly less than the value limit.

def factorial_limit1(limit):
    i = 1
    fact = 1

    while fact < limit:
        i = i + 1
        fact = fact * i

    print(i - 1)

factorial_limit1(116)
factorial_limit1(120)
factorial_limit1(125)

def factorial_limit1(limit):
    count = 1
    prod = 1

    while prod < limit:
        prod = prod * count
        count = count + 1

    count = count - 1 #Can I find a way to do this without having to subtract one?

    print(count)

factorial_limit1(115)