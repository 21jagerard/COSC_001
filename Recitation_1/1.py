# Author: Anna Mikhailova
# Date: 09/20/21
# Purpose: Practice Assignment 1
# Write code that prints the factorial of first n numbers
# Assign a value to n to test your code
# If n is 4 your code should print
# 1 2 6 24 in separate lines

n = int(input("Enter a number!"))
print("The first", n, "factorials are:")
count = 1
fact = 1

while count <= n:
    fact *= count
    print(fact)
    count += 1

# tip: sometimes it's helpful to make the condition of the while loop is the last thing getting changed

