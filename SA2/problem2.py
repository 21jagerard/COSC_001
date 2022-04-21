# Author: Anna Mikhailova
# Date: 09/18/21
# Purpose: Short Assignment 2, Problem 1 -- a Python program that computes
# the first year in which Brutus's balance exceeds Portia's balance, and
# prints out that year and the two balances in that year.

B_INIT_DEP = 1.00
P_INIT_DEP = 100000.00
b_current_wealth = B_INIT_DEP
p_current_wealth = P_INIT_DEP
year = 0

while b_current_wealth <= p_current_wealth:
    b_current_wealth *= 1.05
    p_current_wealth *= 1.04
    year += 1
    # print(year, b_current_wealth, p_current_wealth)
    # I used the line above while writing my code to double check the numbers

print("Brutus's balance first exceeds Portia's balance in the year", year)
print("In the year", year, ", Brutus has $", b_current_wealth)
print("In the year", year, ", Portia has $", p_current_wealth)
