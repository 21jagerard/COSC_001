#Define a function is_factorial, that takes a positive integer n
#as parameter and prints True if it is a factorial of a positive integer.

# def is_factorial(n):
#     i = 1
#     fact = 1
#
#     while fact < n:
#         i = i + 1
#         fact = fact * i
#
#     print(fact == n)
#
# is_factorial(1)
# is_factorial(119)
# is_factorial(121)
# is_factorial(120)

def is_factorial(n):
    prod = 1
    count = 1

    while prod < n:
        prod = prod * count
        count = count + 1

    print(prod == n)

is_factorial(6)