#Define a function print_evens that takes a positive integer n
#as parameter and prints all the even numbers between 0 and n,
#including n if it is an even number.

def print_evens(n):
    i = 0
    while i <= n:
        print(i)
        i = i + 2

print_evens(25)
print("------------")
print_evens(28)