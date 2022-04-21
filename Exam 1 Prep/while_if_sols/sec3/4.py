# Define a function check_number_evens that takes two
# positive integers n and k as parameters. Your function prints
# “at least k evens” if there are at least k even numbers
# between 1 and n, or prints “less than k evens” if there are
# less than k even numbers between 1 and n.

def check_number_evens(n, k):
    i = 2
    count = 0

    while i <= n:
        count = count + 1
        i = i + 2

    if count >= k:
        print("at least k evens")
    else:
        print("less than k evens")


check_number_evens(10, 3)
check_number_evens(9, 5)