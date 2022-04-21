# Author: Anna Mikhailova
# Date: 09/30/21
# Purpose: Define a function get_max that takes three integers n1, n2 and n3
# as parameters and prints the parameter that has the maximum value. If there are two
# parameters that have the same maximum value then either of the two can be printed (but not
# both).

# Purpose: this function takes three integers and prints out the biggest one only
# Parameters: three integers, n1, n2, and n3
def get_max(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        print(n1)
    elif n2 >= n1 and n2 >= n3:
        print(n2)
    elif n3 >= n2 and n3 >= n1:
        print(n3)
    else:
        print(n1)

num1 = int(input("Enter an integer:"))
num2 = int(input("Enter another integer:"))
num3 = int(input("Enter a third integer:"))

get_max(num1, num2, num3)