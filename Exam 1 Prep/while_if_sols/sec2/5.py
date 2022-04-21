#Define a function product_odd that takes two positive integers m and n as
#parameters and prints the product of all odd numbers between m and n
#(including n if it is odd).
# You may assume m < n and m is odd.

def product_odd_m_n(m, n): #assume m < n and m is odd
    i = m
    prod = 1
    while i <= n:
        prod = prod * i
        i = i + 2

    print(prod)

product_odd_m_n(3, 7)
print("------")
product_odd_m_n(3, 8)