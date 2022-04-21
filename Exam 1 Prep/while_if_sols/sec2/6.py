#Define a function last_k_evens1 that takes two positive integer n and k
# as parameters. It should print the last k even numbers between 1 and n.
# You can make the following assumptions:
# a) There are at least k even numbers between 1 and n
# b) n is an even number

def last_k_evens1(n, k):
    i = n
    count = 0
    while count < k:
        print(i)
        i = i - 2
        count = count + 1

last_k_evens1(10, 4)
