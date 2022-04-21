#Define a function product_even that takes a positive integer n
#as parameter and prints the product of all even numbers
#between 1 and n (including n).

def product_even(n):
    prod = 1
    i = 2
    while i <= n:
        prod = prod * i
        i = i + 2

    print(prod)

product_even(10)
print("----------")
product_even(7)