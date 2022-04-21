# Author: Anna Mikhailova
# Date: 09/30/21
# Purpose: Exam 1 Question 1 -- Define a function product_m_n that takes two positive
# integers m and n as parameters and prints the product of all integers between m and
# n, including n but not m in the product. You may assume m < n.

# Purpose: this function takes two positive integers and prints the products of all the integers between them,
# including the upper limit, but not including the lower limit
# Parameters: two integers, m and n
def product_m_n(m, n):
    count = m + 1
    prod = 1
    while count <= n:
        prod *= count
        count += 1
    print("The product of all integers between", m, "and", n, "including", n, "but not", m, "is:", prod)

int1 = int(input("Enter an integer:"))
int2 = int(input("Enter a bigger integer:"))

product_m_n(int1, int2)