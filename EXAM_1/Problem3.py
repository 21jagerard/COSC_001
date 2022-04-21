# Author: Anna Mikhailova
# Date: 09/30/21
# Purpose: Define a function count_factorials that takes three positive integers m, n and k as parameters.
# Your function should print True if there are exactly k integers between m and n (including m and n)
# that are equal to factorial of some positive integer. Otherwise it should print False.


# Purpose: this function takes an interval and a quantity and prints out t/f depending on if the number of factorials
# in the interval is equal to the parameter quantity.
# Parameters: three integers, m, n, and k, where m and n are the lower and upper bounds of the interval, respectively
# and k is the quantity of factorials we want to check for.
def count_factorials(m, n, k):
    fact = 1
    i = 1
    fact_count = 0
    current_val = m
    if n < m:
        print(False)
        return
    while current_val <= n:
        if current_val == fact and fact_count <= k:
            fact_count += 1
            current_val += 1
        elif current_val != fact and current_val > fact and fact_count <= k:
            i += 1
            fact *= i
        elif current_val != fact and current_val < fact and fact_count <= k:
            current_val += 1
    if fact_count != k:
        print(False)
    elif fact_count == k:
        print(True)

low_lim = int(input("Enter a lower limit:"))
up_lim = int(input("Enter an upper limit:"))
k_tf = int(input("How many factorials would you like to check for?"))

count_factorials(low_lim, up_lim, k_tf)
