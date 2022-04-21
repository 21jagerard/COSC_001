# Author: Anna Mikhailova
# Date: 09/18/21
# Purpose: Short Assignment 2, Problem 1 -- a Python program that computes
# my current wealth: the balance of the account after 5% interest was compounded 2018 times
# note to self: constants in all caps!!

INIT_DEP = 1.00
current_wealth = INIT_DEP
year = 0

while year < 2022:
    current_wealth *= 1.05  # I know the *= operator from prior coding experience in Python
    # print(current_wealth)
    year += 1  # I know the += operator from prior coding experience in Python
    # print("At the end of year", year, ", the balance is equal to $", current_wealth)
    # I used the line above while writing my code to double check the numbers

print("At the end of year", year, ", the balance is equal to $", current_wealth)
