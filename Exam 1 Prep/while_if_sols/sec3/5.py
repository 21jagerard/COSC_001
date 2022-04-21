# Define a function last_k_evens3 that takes two positive integers
# n and k as parameters. Your function should do the following:
# print the last k even numbers between 1 and n if there are k or more
# even numbers between 1 and n. Otherwise it should print all the
# even numbers between 1 and n.

def last_k_evens3(n, k):
    if n%2 == 0:
        i = n
    else:
        i = n - 1

    count = 0

    while (count < k) and (i > 0):
        print(i)
        i = i - 2
        count = count + 1

last_k_evens3(10, 5)
print("-------")
last_k_evens3(9, 5)