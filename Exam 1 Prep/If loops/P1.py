# Author: Anna Mikhailova
# Date: 09/29/21
# Purpose: Given the three inner angles of a triangle they are valid if the sum of three angles is 180.
# If they are valid then using the following conditions you can identify
# if it is an equilateral, isosceles or scalene triangle.
# -- A triangle is equilateral if all three angles are equal
# -- A triangle is isosceles is any of the two angles are equal
# -- A triangle is scalene otherwise
#
# Define a function identify_triangle that takes three integers that represent
# the values of three angles as parameters and does the following:
# -- If they can form a triangle then it prints the type of the triangle (equilateral, isosceles, or scalene)
# In this problem you can assume that the given values for parameters add up to 180 and need not check that condition.

def identify_triangle(x, y, z):
    if x + y + z != 180:
        print("Invalid input: those angles do not form a triangle")
    elif (x == y) and (x == z):
        print("The triangle is equilateral.")
    elif ((x == y) and (x != z)) or ((x == z) and (x!= y)) or ((y == z) and (x != y)):
        print("The triangle is isosceles.")
    elif ((x != y) and (y != z) and (x != z)):
        print("The triangle is scalene.")

ax = float(input("Enter the first angle measurement:"))
ay = float(input("Enter the second angle measurement:"))
az = float(input("Enter the third angle measurement:"))

identify_triangle(ax, ay, az)
