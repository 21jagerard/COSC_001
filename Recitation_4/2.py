# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/11/21
# Purpose: Problem 2 -- Define a function that takes a list of positive integers as a parameter and returns True
# if all of the integers are prime, and false otherwise

def is_prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
        i += 1
    return True

def all_prime_list(glist):
    for i in glist:
        if not is_prime(i):
            return False
    return True

print(all_prime_list([3, 5, 7]))