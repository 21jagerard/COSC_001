3#Define a function print_evens that takes a positive integer n as
#parameter and prints all the even numbers between 0 and n, excluding n
#irrespective of if it is even or odd.

def print_evens(n):
    i = 0
    while i < n:
        print(i)
        i = i + 2

print_evens(25)
print_evens(28)