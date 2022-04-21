# Author: Anna Mikhailova
# Date: 09/20/21
# Purpose: Practice Assignment 2
# Write code that prints sum of all odd numbers
# between 1 and n (including n), where n is positive integer (n can be even or odd)
# 1 + 3 + 5

m = int(input("Enter a number!"))
print("The sum of the first", m, "odd numbers is:")
n = 2*m - 1
count = 1
sum = 0

while count <= n:
    sum += count
    count += 2
print(sum)