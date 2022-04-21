#  Define a function print_odds that takes a positive integer
#  n as parameter and prints all the odd numbers between 0 and n.

def print_odds(n):
    i = 1
    while i <= n:
        print(i)
        i = i + 2

print_odds(25)
print("----------")
print_odds(22)