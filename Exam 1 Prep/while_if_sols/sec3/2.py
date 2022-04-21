#Define a function last_k_evens2 that takes two positive integers n and k as
# parameters. It should print the last k even numbers between 1 and n.
# You can make the following assumptions:
#  a) There are at least k even numbers between 1 and n

def last_k_evens2(n, k):
    if n%2 == 0:
        i = n
    else:
        i = n - 1

    count = 0
    while count < k:
        print(i)
        i = i - 2
        count = count + 1

last_k_evens2(10, 4)
print("-------")
last_k_evens2(9, 4)